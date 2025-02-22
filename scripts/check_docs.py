"""Check catalog, local Markdown links, image accessibility, and static SVG assets.

Run from any directory: python scripts/check_docs.py
Uses only the Python standard library; external source interpretation is manual.
"""
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []
LINK = re.compile(r'(!?)\[([^\]]*)\]\(([^\s)]+)\)')


def fail(message):
    ERRORS.append(message)


def main():
    files = sorted(ROOT.rglob('*.md'))
    files = [p for p in files if '.git' not in p.parts]
    anchors = {}
    for path in files:
        text = path.read_text(encoding='utf-8')
        values, seen = set(), Counter()
        for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
            base = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
            n = seen[base]
            values.add(base if n == 0 else f'{base}-{n}')
            seen[base] += 1
        anchors[path.resolve()] = values

    local_links, image_links = 0, 0
    sources = set()
    for path in files:
        text = path.read_text(encoding='utf-8')
        label = path.relative_to(ROOT).as_posix()
        if text.count('```') % 2:
            fail(f'Unclosed code fence: {label}')
        if re.search(r'\b(TODO|TBD|FIXME|coming soon)\b', text, re.I):
            fail(f'Unfinished placeholder: {label}')
        if text != text.rstrip()+'\n':
            fail(f'Expected one final newline: {label}')
        for n,line in enumerate(text.splitlines(),1):
            if line != line.rstrip():
                fail(f'Trailing whitespace: {label}:{n}')
        for image,alt,dest in LINK.findall(text):
            if image and not alt.strip():
                fail(f'Missing image alternative: {label}')
            url = urlsplit(dest.strip('<>'))
            if url.scheme or url.netloc:
                if path.parent.parent.name == 'answers':
                    sources.add(dest)
                continue
            local_links += 1
            image_links += bool(image)
            target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
            if not target.is_relative_to(ROOT):
                fail(f'Link leaves repository: {label} -> {dest}')
            elif not target.exists():
                fail(f'Missing target: {label} -> {dest}')
            elif url.fragment and unquote(url.fragment) not in anchors.get(target,set()):
                fail(f'Missing anchor: {label} -> {dest}')

    readme = (ROOT/'README.md').read_text(encoding='utf-8')
    questions = re.findall(r'^- \*\*([jms])\*\* \[(.*?)\]\((answers/[^)]+)\)', readme, re.M)
    answer_files = sorted((ROOT/'answers').glob('*/*.md'))
    expected = {p.relative_to(ROOT).as_posix() for p in answer_files}
    listed = [q[2] for q in questions]
    if not questions:
        fail('Catalog contains no questions')
    if len(set(listed)) != len(listed):
        fail('Catalog contains duplicate answer links')
    if set(listed) != expected:
        fail('Catalog contains missing or orphaned answer paths')
    words = []
    illustrated = set()
    for level,question,relative in questions:
        text = (ROOT/relative).read_text(encoding='utf-8')
        if not text.startswith('# '+question+'\n'):
            fail(f'Question and answer title differ: {relative}')
        if text.count('## Answer\n') != 1 or text.count('## References\n') != 1:
            fail(f'Invalid answer structure: {relative}')
            continue
        if '**Reviewed:**' not in text:
            fail(f'Missing review date: {relative}')
        refs = text.split('## References\n',1)[1]
        if not re.search(r'\[.+?\]\(https://', refs):
            fail(f'Missing source reference: {relative}')
        body = text.split('## Answer\n',1)[1].split('## References\n',1)[0]
        body = re.sub(r'!\[[^]]*\]\([^)]+\)', '', body)
        words.append(len(body.split()))

    manifest = json.loads((ROOT/'assets/diagrams/manifest.json').read_text(encoding='utf-8'))
    svg_files = sorted((ROOT/'assets/diagrams').glob('*.svg'))
    if len({f['slug'] for f in manifest}) != len(manifest):
        fail('Figure manifest contains duplicate slugs')
    if {f['slug']+'.svg' for f in manifest} != {p.name for p in svg_files}:
        fail('SVG catalog and manifest differ')
    for figure in manifest:
        path = ROOT/'assets/diagrams'/(figure['slug']+'.svg')
        tree = ET.parse(path)
        svg = tree.getroot()
        tags = {e.tag.split('}')[-1] for e in svg.iter()}
        if not {'title','desc'}.issubset(tags):
            fail(f'Missing SVG title/description: {path.name}')
        if tags & {'script','foreignObject','image','iframe'}:
            fail(f'Unexpected external or active SVG content: {path.name}')
        for element in svg.iter():
            for key,value in element.attrib.items():
                if key.lower().startswith('on') or 'href' in key or 'url(' in value:
                    fail(f'Unexpected active or external SVG attribute: {path.name}')
        answer = ROOT/'answers'/(figure['answer']+'.md')
        if not answer.exists() or f"/{figure['slug']}.svg)" not in answer.read_text(encoding='utf-8'):
            fail(f'Figure not embedded in its answer: {path.name}')
        illustrated.add(figure['answer'])
    report = {'answers':len(answer_files),'primary_reference_urls':len(sources),
              'markdown_files':len(files),'local_links_checked':local_links,
              'image_links_checked':image_links,'svg_figures':len(svg_files),
              'answer_words':{'min':min(words,default=0),'max':max(words,default=0),
                              'mean':round(sum(words)/len(words)) if words else 0},'errors':ERRORS}
    print(json.dumps(report,indent=2))
    return bool(ERRORS)


if __name__ == '__main__':
    sys.exit(main())
