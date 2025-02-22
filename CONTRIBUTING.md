# Contributing

Keep the guide focused on **Project Manager** interviews. Add domain depth where it changes decisions; keep Product, Delivery, and Presales coverage concise.

Select questions by distinct decisions and learning needs. Use existing answers for closely related examples; add a question when it teaches a missing competency. There is no target question count or equal-size requirement for sections. Keep the main README focused on the guide's scope and navigation; review history and asset-generation details belong in supporting documentation.

Each question belongs in the main README with a `j`, `m`, or `s` label and links to one answer under `answers/<topic>/`. Use English to match the companion Android guide.

An answer should contain a direct explanation, practical reasoning or an illustrative example, meaningful limitations, a link back to its topic, and primary-source references. Explain enough locally that the answer remains useful without opening every reference. Preserve the distinction between standard-defined requirements and suggested project practice.

For domain and version-sensitive claims, verify the primary source, record the review date, and specify jurisdiction, organizational role, and relevant version. Avoid universal compliance claims and invented legal deadlines.

When changing the catalog, update counts in both indexes, keep topic anchors aligned with README headings, and check all relative links and images. Do not present illustrative project results as actual experience or certification requirements.

Run `python scripts/check_docs.py` for catalog, local link, image, and SVG checks. This validates repository structure, not the truth or currency of external sources. Record manual source review and any access limitations in the review notes.

Use ordinary local images for explanatory figures so they render independently of Mermaid support. Keep SVG titles, descriptions, text alternatives, explicit units, and illustrative-data labels. Regenerate the original figures with `python scripts/generate_visuals.py`; add `--preview-dir <directory>` for PNG visual review. Review both the numeric assumptions and the rendered result after a change.
