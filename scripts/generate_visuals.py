"""Generate original SVG teaching figures and PNG previews. Requires Pillow.

Run: python scripts/generate_visuals.py --preview-dir <directory>
Charts use explicit illustrative data; no external images or web assets are used.
"""
from pathlib import Path
from html import escape
import argparse
import json
import math
import random
from collections import Counter
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'diagrams'
W, H = 1200, 660
INK, MUTED, GRID = '#16324f', '#526579', '#dce5ee'
BLUE, TEAL, RED, AMBER = '#2563eb', '#0f766e', '#b42318', '#a65b00'
PALE = ['#eaf1ff', '#e5f5f1', '#fff2dc', '#f1edff']
PREVIEW = None
MANIFEST = []


def font(size, bold=False):
    names = ([r'C:/Windows/Fonts/segoeuib.ttf', 'DejaVuSans-Bold.ttf'] if bold
             else [r'C:/Windows/Fonts/segoeui.ttf', 'DejaVuSans.ttf'])
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    raise RuntimeError('Install Segoe UI or DejaVu Sans to render previews')


class Canvas:
    def __init__(self, slug, title, subtitle, answer, alt):
        self.slug, self.answer, self.alt, self.title = slug, answer, alt, title
        self.im = Image.new('RGB', (W, H), '#f8fafc')
        self.draw = ImageDraw.Draw(self.im)
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
                    f'<title id="title">{escape(title)}</title><desc id="desc">{escape(alt)}</desc>',
                    f'<rect width="{W}" height="{H}" fill="#f8fafc"/>']
        self.rect(32, 24, 1136, 612, '#ffffff', GRID, 18)
        self.text(64, 49, title, 32, INK, True)
        self.wrap(64, 99, subtitle, 1060, 21, MUTED, max_lines=2)

    def rect(self, x, y, w, h, fill, stroke=None, radius=0):
        self.draw.rounded_rectangle((x, y, x+w, y+h), radius=radius, fill=fill,
                                    outline=stroke, width=1)
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}"' + (f' stroke="{stroke}"' if stroke else '') + '/>')

    def text(self, x, y, value, size=22, color=INK, bold=False, anchor='start'):
        value = str(value)
        f = font(size, bold)
        width = self.draw.textlength(value, font=f)
        left = x if anchor == 'start' else x-width/2 if anchor == 'middle' else x-width
        if left < 28 or left+width > W-28 or y < 24 or y+size+5 > H-24:
            raise ValueError(f'Clipped label in {self.slug}: {value!r}')
        self.draw.text((left, y), value, font=f, fill=color, anchor='lt')
        self.svg.append(f'<text x="{x}" y="{y}" font-family="Segoe UI, Arial, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}" text-anchor="{anchor}" dominant-baseline="text-before-edge">{escape(value)}</text>')

    def wrap(self, x, y, value, width, size=21, color=INK, bold=False, max_lines=8):
        lines, line = [], ''
        for word in value.split():
            trial = f'{line} {word}'.strip()
            if self.draw.textlength(trial, font=font(size, bold)) > width and line:
                lines.append(line)
                line = word
            else:
                line = trial
        if line:
            lines.append(line)
        if len(lines) > max_lines:
            raise ValueError(f'Text overflow in {self.slug}: {value!r}')
        for i, line in enumerate(lines):
            self.text(x, y+i*(size+9), line, size, color, bold)
        return len(lines)*(size+9)

    def line(self, points, color=INK, width=3, dashed=False, arrow=False):
        if dashed:
            for p, q in zip(points, points[1:]):
                length = math.dist(p, q)
                for s in range(0, int(length), 14):
                    t1, t2 = s/length, min(s+7, length)/length
                    a = (p[0]+(q[0]-p[0])*t1, p[1]+(q[1]-p[1])*t1)
                    b = (p[0]+(q[0]-p[0])*t2, p[1]+(q[1]-p[1])*t2)
                    self.draw.line((a, b), fill=color, width=width)
        else:
            self.draw.line(points, fill=color, width=width)
        pts = ' '.join(f'{x},{y}' for x,y in points)
        self.svg.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{width}"' + (' stroke-dasharray="7 7"' if dashed else '') + '/>')
        if arrow:
            a, b = points[-2:]
            angle = math.atan2(b[1]-a[1], b[0]-a[0])
            tri = [b, (b[0]-12*math.cos(angle-.45), b[1]-12*math.sin(angle-.45)),
                   (b[0]-12*math.cos(angle+.45), b[1]-12*math.sin(angle+.45))]
            self.poly(tri, color)

    def poly(self, points, color):
        self.draw.polygon(points, fill=color)
        pts = ' '.join(f'{x},{y}' for x,y in points)
        self.svg.append(f'<polygon points="{pts}" fill="{color}"/>')

    def card(self, x, y, w, h, title, body, color_index=0):
        self.rect(x, y, w, h, PALE[color_index % 4], None, 12)
        th = self.wrap(x+18, y+18, title, w-36, 25, INK, True, 2)
        bh = self.wrap(x+18, y+th+29, body, w-36, 21, INK, max_lines=5)
        if th+bh+35 > h:
            raise ValueError(f'Card overflow in {self.slug}: {title}')

    def note(self, text):
        self.rect(64, 476, 1072, 98, '#eef4f8', None, 10)
        self.wrap(84, 493, text, 1028, 22, INK, max_lines=3)

    def finish(self, footer='Original teaching figure. Scenarios and numbers are illustrative.'):
        self.text(64, 599, footer, 18, MUTED)
        self.svg.append('</svg>')
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT/f'{self.slug}.svg').write_text('\n'.join(self.svg)+'\n', encoding='utf-8')
        if PREVIEW:
            PREVIEW.mkdir(parents=True, exist_ok=True)
            self.im.save(PREVIEW/f'{self.slug}.png')
        MANIFEST.append({'slug':self.slug, 'title':self.title, 'answer':self.answer,
                         'alt':self.alt, 'width':W, 'height':H})


def flow(slug, title, subtitle, steps, note, answer, alt=None):
    c = Canvas(slug, title, subtitle, answer, alt or title+'. '+note)
    n = len(steps)
    gap = 26
    width = (1072-gap*(n-1))/n
    for i,(heading,body) in enumerate(steps):
        x = 64+i*(width+gap)
        c.card(x, 175, width, 255, heading, body, i)
        if i < n-1 and slug not in {'dora-metrics', 'scrum-goals', 'clinical-evaluation', 'incident-coordination', 'reconciliation'}:
            c.line([(x+width+4, 300), (x+width+gap-4, 300)], MUTED, 3, arrow=True)
    c.note(note)
    c.finish()


def grid(slug, title, subtitle, cells, note, answer):
    c = Canvas(slug, title, subtitle, answer, title+'. '+note)
    for i,(heading,body) in enumerate(cells):
        x, y = 64+(i%2)*548, 160+(i//2)*158
        c.card(x, y, 524, 144, heading, body, i)
    c.note(note)
    c.finish()


def axes(c, x, y, width, height, ymax, ticks=5):
    for i in range(ticks+1):
        value = ymax*i/ticks
        yy = y+height-height*i/ticks
        c.line([(x,yy),(x+width,yy)], GRID, 1)
        c.text(x-14, yy-11, f'{value:g}', 18, MUTED, anchor='end')
    c.line([(x,y),(x,y+height),(x+width,y+height)], MUTED, 2)


def charts():
    c = Canvas('critical-path', 'Critical path: improve the path that drives the finish',
               'Simplified schedule: parallel start, no shared-resource constraint.',
               'planning-and-estimation/critical-path',
               'Integration 0–5, verification 5–8, approval 8–10 form a ten-day critical path. UI 0–6 has four days of float.')
    x0, unit = 330, 77
    for d in range(0,11,2):
        x=x0+unit*d
        c.line([(x,172),(x,425)], GRID, 1)
        c.text(x, 435, d, 20, MUTED, anchor='middle')
    for i,(name,start,end,color) in enumerate([('Integration',0,5,RED),('Verification',5,8,RED),('Approval',8,10,RED),('UI work',0,6,BLUE)]):
        y=185+i*58
        c.text(78,y+9,name,23)
        c.rect(x0+start*unit,y,(end-start)*unit,40,color,None,5)
        c.text(x0+(start+end)*unit/2,y+8,f'{end-start} days',21,'#ffffff',True,'middle')
    c.line([(x0+6*unit,379),(x0+10*unit,379)], TEAL, 4, dashed=True)
    c.text(x0+8*unit,397,'4 days float',20,TEAL,anchor='middle')
    c.note('Ten days drives launch. Shortening UI alone does not move it. Recalculate if resources or dependencies change.')
    c.finish()

    rng=random.Random(42)
    history=[2,3,4,4,5,5,6,3,4,7,2,5]
    outcomes=[]
    for _ in range(20000):
        done,weeks=0,0
        while done<20:
            done+=rng.choice(history)
            weeks+=1
        outcomes.append(weeks)
    counts=Counter(outcomes)
    ordered=sorted(outcomes)
    p50,p85=[ordered[math.ceil(p*len(ordered))-1] for p in (.5,.85)]
    c=Canvas('forecast-distribution','A forecast is a distribution, conditional on assumptions',
             '20 items; 20,000 seeded simulations sampling illustrative weekly completions.',
             'planning-and-estimation/forecasting-under-uncertainty',
             f'Illustrative completion distribution: median {p50} weeks, 85th percentile {p85} weeks. This is a model, not a commitment.')
    axes(c,120,183,970,230,60,3)
    c.text(122,150,'Share of simulated completions (%)',19,MUTED)
    weeks=list(range(min(counts),max(counts)+1))
    bw=970/len(weeks)
    for i,w in enumerate(weeks):
        pct=counts[w]/200
        x=120+i*bw+16
        c.rect(x,413-pct/60*230,bw-32,pct/60*230,BLUE,None,4)
        c.text(x+(bw-32)/2,425,f'{w} wk',20,MUTED,anchor='middle')
        if pct>=1:
            c.text(x+(bw-32)/2,413-pct/60*230-28,f'{pct:.1f}%',18,INK,anchor='middle')
    c.note(f'Model result: P50 = {p50} weeks; P85 = {p85} weeks. More trials cannot repair biased history or hidden dependencies.')
    c.finish()

    c=Canvas('capacity','Capacity: nominal availability is only the starting point',
             'Illustrative two-week allowance for four people: 40 nominal person-days.',
             'planning-and-estimation/capacity-resource-planning',
             'Forty person-days minus four leave, six support and four coordination leaves twenty-six planned person-days, subject to skills and dependencies.')
    x=88
    vals=[('Leave',4,'#94a3b8'),('Support',6,AMBER),('Coordination',4,'#7c3aed'),('Planned work',26,TEAL)]
    for name,v,col in vals:
        width=v*25
        c.rect(x,224,width,82,col)
        c.text(x+width/2,246,v,28,'#ffffff',True,'middle')
        x+=width
    for i,(name,v,col) in enumerate(vals):
        xx=88+(i%2)*530
        yy=346+(i//2)*49
        c.rect(xx,yy+3,18,18,col)
        c.text(xx+31,yy,f'{name}: {v} person-days',22)
    c.note('26 person-days is not interchangeable specialist capacity. Avoid double-counting allowances already reflected in historical throughput.')
    c.finish()

    c=Canvas('earned-value','Earned value: compare planned work, accepted work, and cost',
             'Illustrative snapshot. All amounts are thousands of the same currency.',
             'budget-and-commercials/earned-value',
             'PV 100, EV 80, AC 90. CPI equals 0.89; SPI equals 0.80. Schedule variance is work value, not days.')
    axes(c,170,175,900,240,120,4)
    for x,name,v,col in [(285,'PV: planned',100,BLUE),(570,'EV: earned',80,TEAL),(855,'AC: actual',90,AMBER)]:
        c.rect(x,415-v*2,150,v*2,col,None,5)
        c.text(x+75,415-v*2-33,v,25,col,True,'middle')
        c.text(x+75,426,name,22,INK,anchor='middle')
    c.note('CPI = 80 / 90 = 0.89. SPI = 80 / 100 = 0.80. EV is budgeted work value, not revenue or calendar time.')
    c.finish()

    done=[0,2,4,6,8,11,14,17,20]
    scope=[20,20,20,20,28,28,28,28,28]
    remaining=[s-d for s,d in zip(scope,done)]
    c=Canvas('burnup-burndown','A burnup separates scope arrival from completed work',
             'Illustrative item counts: eight items are added at day 4.',
             'metrics-and-improvement/burndown-burnup',
             'Two charts show remaining work versus scope and completion. At day four remaining work rises because scope increases, despite continued completion.')
    for xx,title,series in [(112,'Burndown: remaining',[(remaining,BLUE)]),(680,'Burnup: scope and done',[(scope,AMBER),(done,TEAL)])]:
        c.text(xx,151,title,23,INK,True)
        axes(c,xx,200,410,210,30,3)
        for vals,col in series:
            c.line([(xx+i*410/8,410-v/30*210) for i,v in enumerate(vals)],col,4)
        for i in (0,4,8):
            c.text(xx+i*410/8,422,f'Day {i}',18,MUTED,anchor='middle')
    c.text(835,177,'Scope',18,AMBER,True)
    c.text(968,177,'Done',18,TEAL,True)
    c.note('Remaining work can rise while useful work finishes. Inspect scope changes before interpreting the trend as a delivery slowdown.')
    c.finish()

    done=[0,1,3,4,6,7,9,10,12]
    review=[1,2,3,4,5,6,6,7,6]
    dev=[2,3,4,4,4,4,3,2,2]
    c=Canvas('cumulative-flow','Cumulative flow: a growing band makes waiting visible',
             'Illustrative fixed scope of 20 items; the review band grows over time.',
             'delivery-adjacent/multi-team-flow',
             'A stacked area chart of done, review, development and not-started items totals twenty each day. Review accumulation warrants investigation.')
    x,y,pw,ph=118,188,970,240
    bands=[done,review,dev,[20-a-b-c for a,b,c in zip(done,review,dev)]]
    low=[0]*9
    for vals,col in zip(bands,['#79c6b5','#f3c983','#9dbaf5','#e8edf3']):
        high=[a+b for a,b in zip(low,vals)]
        pts=[(x+i*pw/8,y+ph-v/20*ph) for i,v in enumerate(low)]
        pts+=list(reversed([(x+i*pw/8,y+ph-v/20*ph) for i,v in enumerate(high)]))
        c.poly(pts,col)
        low=high
    axes(c,x,y,pw,ph,20,4)
    for i in (0,4,8):
        c.text(x+i*pw/8,438,f'Day {i}',18,MUTED,anchor='middle')
    for i,(label,col) in enumerate(zip(['Done','Review','Development','Not started'],['#79c6b5','#f3c983','#9dbaf5','#e8edf3'])):
        xx=120+i*255
        c.rect(xx,151,16,16,col)
        c.text(xx+25,148,label,19)
    c.note('Inspect aged and blocked review items. A wider band is evidence of accumulation, not proof of a particular root cause.')
    c.finish()

    c=Canvas('error-budget','Error budget: define the denominator before doing the math',
             'Request-based example: 1,000,000 eligible requests; success target 99.9%.',
             'metrics-and-improvement/sli-slo-sla',
             'The budget is one thousand failed requests. Seven hundred failures consume seventy percent, leaving three hundred. This is not an outage-minute calculation.')
    c.text(84,179,'Allowed failures: 1,000',29,INK,True)
    c.rect(84,249,1000,84,'#dceee8',None,7)
    c.rect(84,249,700,84,RED,None,7)
    c.text(434,270,'700 used',28,'#ffffff',True,'middle')
    c.text(934,270,'300 left',28,TEAL,True,'middle')
    c.text(84,369,'Budget = 1,000,000 x (1 - 0.999) = 1,000 failures',25)
    c.note('70% consumed. A request-based SLO cannot be converted directly into outage minutes; a time-based SLI uses a different denominator.')
    c.finish()


def main():
    global PREVIEW
    parser=argparse.ArgumentParser()
    parser.add_argument('--preview-dir',type=Path)
    args=parser.parse_args()
    PREVIEW=args.preview_dir
    charts()
    specs=[
      ('delivery-system','Project delivery connects decisions to outcomes','A PM coordinates the whole chain; each decision still needs an accountable owner.',
       [('Outcome','User need, benefit, constraints, and ownership'),('Plan and flow','Scope, capacity, dependencies, cost, and uncertainty'),('Validate and release','Accepted behavior, readiness, and safe recovery'),('Operate and learn','Support, measure benefits, inspect and improve')],
       'Healthcare, Fintech, and Cybersecurity change the evidence and consequences at every step. Product, Delivery, and Presales contribute at their boundaries.','foundations/project-success'),
      ('scope-change','Scope change is a decision with visible consequences','Clarify whether this is new scope, an agreed requirement, or a defect.',
       [('Request','Reason, user need, and affected baseline'),('Assess','Options, effort, timing, risk, and dependencies'),('Decide','Use the agreed scope, funding, and risk authority'),('Follow through','Update agreements and plans; verify the result')],
       'An adaptive backlog supports learning. It does not silently change a contract, funding boundary, or essential control.','scope-and-requirements/change-control'),
      ('scrum-goals','Scrum: artifacts make goals, plans, and quality inspectable','The three commitments connect different horizons of inspection.',
       [('Product Backlog','Commitment: Product Goal'),('Sprint Backlog','Commitment: Sprint Goal'),('Increment','Commitment: Definition of Done')],
       'Developers adapt the Sprint plan with the Product Owner as they learn. Selected items are a forecast; quality is not an optional leftover.','agile-and-flow/backlogs-and-goals'),
      ('flow-time','Lead time, cycle time, and age use explicit boundaries','A work item can wait before it starts, and remain unfinished after it starts.',
       [('Requested: day 0','Waiting before the workflow start'),('Started: day 4','At day 7, unfinished-item age is 3 days'),('Finished: day 9','Cycle time is 5 days; request-to-finish is 9 days')],
       'Use consistent calendar or working-time clocks. These numbers describe an illustrative example, not a forecast for every item.','agile-and-flow/flow-metrics'),
      ('risk-response','A risk record should lead to action and a decision','Cause, uncertain event, and consequence identify the exposure.',
       [('Assess','Likelihood, impact, urgency, and evidence'),('Treat','Avoid, mitigate, transfer, or accept within authority'),('Verify','Check residual exposure, triggers, and ownership')],
       'Completing a mitigation task does not prove the risk disappeared. A realized threat can become an issue requiring resolution.','risk-and-issues/risk-register'),
      ('status-decision','A status update should make the next decision easier','Lead with the forecast and evidence, then the decision or help needed.',
       [('Current evidence','Accepted work and unresolved dependencies'),('Forecast and impact','Date, cost, scope, quality, and uncertainty'),('Decision and action','Options, owner, deadline, next evidence check')],
       'Illustrative: certification threatens launch by one week; sponsor chooses smaller initial scope or a revised date by Friday.','stakeholders-and-communication/status-reporting'),
      ('star','A behavioral answer connects your action to evidence','Use a real experience; keep illustrative examples separate from personal claims.',
       [('Situation + task','Context, stakes, and your specific responsibility'),('Action','Your decision, reasoning, options, and coordination'),('Result + learning','Outcome evidence and what changed afterward')],
       'Spend most of the answer on your reasoning and actions. A polished story without a clear responsibility provides weak evidence.','leadership-and-behavioral/failure-star'),
      ('migration','Migration readiness includes a credible recovery path','Rehearse the data transition and its decision checkpoints.',
       [('Prepare','Map data, identities, invariants, and owners'),('Rehearse','Measure duration, reconcile, test recovery'),('Cut over','Apply go/no-go and the last safe abort point'),('Verify','Check live behavior and reconcile remaining exceptions')],
       'Reverting code is not enough if the new system has accepted writes. Assess data compatibility, RTO, RPO, and forward recovery.','technical-literacy/data-migration'),
      ('release-readiness','Release approval applies to an explicit boundary','Artifact, configuration, cohort, data change, and evidence must match.',
       [('Evidence','Behavior, quality, security, domain, and operations'),('Decision','Go, no-go, or supported narrower scope'),('Observe and respond','Agreed guardrails, stop authority, and recovery')],
       'Stopping further rollout does not undo data already changed. Reassess readiness after material changes or failed guardrails.','quality-and-release/release-readiness'),
      ('dora-metrics','DORA research measures delivery at a service boundary','Define event classification and the observation window before comparing trends.',
       [('Throughput','Change lead time; deployment frequency; failed deployment recovery time'),('Instability','Change fail rate; deployment rework rate')],
       'Five metrics in the checked guide. Pair them with user outcomes and service reliability. This research is distinct from EU DORA regulation.','metrics-and-improvement/dora-metrics'),
      ('health-data','Patient data can leave through secondary paths','Assess purpose, role, access, and safeguards across the complete data flow.',
       [('Collection','Patients, clinicians, devices, and intake'),('Clinical systems','Identity, records, and partner integrations'),('Secondary tools','Logs, analytics, exports, backups, and support')],
       'HIPAA scope, GDPR processing conditions, and other applicable duties require separate assessment. Removing names alone is not a de-identification method.','healthcare/patient-data-and-privacy'),
      ('fhir-layers','FHIR integration: transport success is one layer of evidence','Agree the partner release, profiles, operations, and implementation guide.',
       [('Exchange','API behavior, versions, retries, and access'),('Meaning','Patient identity, codes, units, time, provenance'),('Clinical workflow','Correct use, recipient, exceptions, and support')],
       'A successful response can still carry the wrong unit or patient mapping. FHIR does not itself implement the complete security or consent process.','healthcare/ehr-fhir-integration'),
      ('clinical-evaluation','Clinical evaluation asks three different evidence questions','IMDRF SaMD framework; apply according to intended use, risk, and jurisdiction.',
       [('Association','Is the output clinically and scientifically related to the condition?'),('Technical validation','Does the software correctly generate the intended output?'),('Clinical validation','Does the output achieve the intended purpose in the target use?')],
       'Workflow safety also depends on identity, handoffs, people, downtime, and response. UAT alone does not establish all clinical evidence.','healthcare/clinical-validation'),
      ('payment-lifecycle','A card payment has several distinct states','Simplified example; provider and rail contracts determine the actual transitions.',
       [('Authorize','Approval or hold; expiry matters'),('Capture','Request collection; partial and retry rules matter'),('Settle','Processing and funds movement across participants'),('Payout','Transfer available balance to the merchant bank')],
       'Refunds, reversals, disputes, and fees add separate events. Checkout success, authorization, settlement, and payout are not interchangeable.','fintech/payment-lifecycle'),
      ('payment-timeout','Timeout means the result is unknown to the caller','Resolve the original financial operation before creating a new effect.',
       [('Request sent','Preserve operation ID and provider correlation'),('Response lost','The provider may already have processed it'),('Establish state','Use documented status, retry, event, and reconciliation paths')],
       'Blind failover to another provider can duplicate a successful payment. Providers do not share one universal idempotency boundary.','fintech/provider-outage-case'),
      ('reconciliation','Reconciliation compares independent records','Match identifiers, amounts, currencies, fees, timing, and adjustments.',
       [('Internal record','Order and agreed accounting state'),('Provider record','Processing events and balance movements'),('Bank evidence','Applicable payout or settlement movements')],
       'Example: 100 gross minus 3 fee gives 97 net. A mismatch needs an owner and controlled resolution; replaying every record can move money twice.','fintech/financial-correctness'),
      ('pci-boundary','Draw payment-data scope before making compliance claims','Hosted components and tokens can reduce exposure; assessment determines scope.',
       [('Customer entry','Where raw card data enters and is transmitted'),('Provider service','Assessed responsibilities and integration conditions'),('Merchant paths','Application, scripts, logs, analytics, support, and access')],
       'Outsourcing does not automatically remove merchant obligations. Include secondary tools and systems that can affect the payment environment.','fintech/pci-scope'),
      ('security-evidence','Secure delivery is an evidence chain','Choose applicable practices and requirements; identify their versions.',
       [('Design','Threat context, data boundaries, requirements'),('Build and verify','Review, appropriate checks, findings, remediation, retest'),('Release and operate','Known artifact, residual exposure, response and update ownership')],
       'SSDF addresses development practices; ASVS supports verifiable application requirements. A final penetration test is one bounded assessment.','cybersecurity/secure-sdlc'),
      ('incident-coordination','Incident coordination needs parallel owners','A shared factual record connects technical response, business impact, and decisions.',
       [('Technical response','Investigation, containment, evidence, and recovery'),('Business and users','Continuity, impact, resources, and verified updates'),('Required decisions','Legal, privacy, notification, and risk authority')],
       'The PM supports coordination within the incident structure. Availability recovery does not automatically resolve data impact or investigation.','cybersecurity/cyber-incident-coordination'),
      ('iam-rollout','IAM rollout: protection, usability, and recovery travel together','Inventory human, privileged, service, legacy, and emergency access paths.',
       [('Pilot','Representative users, applications, and recovery scenarios'),('Expand','Enrollment, control health, exceptions, and support capacity'),('Operate','Access removal, recovery, monitoring, and policy ownership')],
       'MFA enabled in one portal does not prove every access path is protected. OTP and out-of-band methods are not automatically phishing-resistant.','cybersecurity/iam-rollout'),
      ('soc-detection','SOC capability is a tested detection-to-response chain','Start from relevant threat scenarios and assets, not maximum log volume.',
       [('Telemetry','Coverage, quality, identity, timing, and context'),('Detection','Logic tested against representative authorized scenarios'),('Investigation','Analyst context, runbook, access, capacity'),('Response','Authority, effective action, and verification')],
       'An ATT&CK mapping is not proof of detection. Test missing telemetry, noisy alerts, unavailable analysts, and the actual response path.','cybersecurity/soc-siem-delivery'),
      ('presales-handover','Presales evidence should survive the handover','Keep the buying decision, final agreement, estimate basis, and delivery plan connected.',
       [('Discover','Client outcome, decision path, constraints, unknowns'),('Validate','POC or investigation with explicit success evidence'),('Agree','Scope, acceptance, price basis, client inputs'),('Transfer','Final commitments, gaps, owners, and decision dates')],
       'A polished demo does not prove production readiness. Resolve differences between the signed agreement and the assumptions used for the estimate.','presales-adjacent/sales-to-delivery-handover')]
    for spec in specs:
        flow(*spec)
    grid('role-boundaries','Role boundaries follow decisions, not titles','Illustrative ownership to agree for the organization.',
         [('Product','Problem, value, direction, and priority'),('Project','Integrated constraints, dependencies, and decisions'),('Engineering','Technical approach, implementation, and evidence'),('Operations and risk','Service readiness and authorized exposure decisions')],
         'One person may hold several responsibilities. Preserve clear authority for each decision, including Scrum accountabilities where applicable.',
         'foundations/role-boundaries')
    grid('vulnerability-priority','Severity is one input to vulnerability prioritization','Two hypothetical findings; validate asset context before deciding.',
         [('A: base score 9.8','Isolated non-production asset; verify isolation'),('B: base score 8.1','Internet-facing payment service; known exploitation'),('Other evidence','Reachability, controls, criticality, and business impact'),('Treatment and proof','Contain or remediate; verify production; track exceptions')],
         'CVSS describes severity; EPSS predicts CVE exploitation; KEV records known exploitation. None alone gives organizational risk.',
         'cybersecurity/vulnerability-prioritization')
    grid('rice-example','RICE makes prioritization assumptions visible','Illustrative quarterly reach and person-month effort; not a universal ranking.',
         [('Option A','1,000 reach x 1 impact x 0.8 confidence / 2 effort = 400'),('Option B','400 reach x 2 impact x 0.5 confidence / 1 effort = 400'),('Investigate','Validate low-confidence assumptions and dependencies'),('Decide','Use product authority, strategy, and required constraints')],
         'A tied score does not make the options equivalent. Essential controls and applicable obligations require explicit treatment.',
         'product-adjacent/rice-and-priority')
    (OUT/'manifest.json').write_text(json.dumps(MANIFEST,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'figures':len(MANIFEST),'svg_directory':str(OUT),'previews':str(PREVIEW)},indent=2))


if __name__ == '__main__':
    main()
