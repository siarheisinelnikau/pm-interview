# Content review and source audit

[All questions](../README.md) · [Source notes](source-notes.md) · [Visual guide](visual-guide.md)

**Review date: 2026-10-30.** Reviewed all **100 answers**, the **38 distinct original answer-reference URLs**, and additional primary sources used in this revision. Revised answers reference **63 distinct primary-source URLs**.

## Method and scope

Checked definitions, arithmetic, limitations, role authority, source relevance, publication status, versions, and jurisdiction. Distinguished general project practice from normative and legal requirements. Scenarios, numerical examples, and figures are illustrative.

This is a dated review, not automatic monitoring of future source changes. Qualified owners establish applicability to a real project.

## Material corrections and additions

| Area | Finding and revision |
| --- | --- |
| Generic references | 47 original answers cited the GovS 002 landing page. References now use full v2.1 text and relevant section labels, with additional specific sources where appropriate. |
| STAR | Added the National Careers Service source for STAR instead of relying on a postmortem chapter for the interview technique. |
| Planning and metrics | Added effort/duration, resource constraints, float, simulation assumptions, scope arrival, error-budget denominators, EVM assumptions, and SPI calendar limitations. |
| Healthcare | Added current FDA CDS, QMSR, device cybersecurity, EU software guidance, clinical evaluation, and NHS clinical safety. Distinguished HIPAA, GDPR, and FTC scope. |
| Fintech | Distinguished authorization/capture/settlement/payout, uncertain outcomes, retry boundaries, reconciliation, and operational onboarding capacity. Added PCI version and effective-date context. |
| Cybersecurity | Distinguished SSDF final/draft status, ASVS 5.0.0, Rev. 3 incident response, CVSS 4.0, EPSS, KEV, and authentication assurance. |
| Visuals | Replaced three Mermaid-only diagrams and added 32 SVG images, including seven numeric charts, embedded in answers and collected in the visual guide. |

## Source access

The two original EBA pages and the CISA catalog returned access restrictions during direct retrieval. A 403 response does not establish that a page or requirement is obsolete. Payment-services references now use the European Commission; EU DORA uses ESMA; CISA is accompanied by its official GitHub data mirror. No inaccessible page is represented as having been read in full.

The source notes record confirmed versions and status, including January 29, 2026 FDA CDS, February 2026 FDA cybersecurity, QMSR effective February 2, 2026, June 2026 FATF, and final-versus-draft SSDF. PSD3/PSR discussion distinguishes legal status from application and avoids inventing a universal transition date.

## Coverage of all answers

| Topic | Reviewed | Changes |
| --- | ---: | --- |
| [foundations](../answers/foundations/business-case.md) | 8 | Success, benefits, authority, delivery approach, closure. |
| [planning-and-estimation](../answers/planning-and-estimation/capacity-resource-planning.md) | 8 | Capacity, float, estimating, forecasts, dependencies, recovery. |
| [scope-and-requirements](../answers/scope-and-requirements/acceptance-criteria.md) | 6 | Acceptance cases, measurable requirements, scope decisions, traceability. |
| [agile-and-flow](../answers/agile-and-flow/agile-values.md) | 8 | Scrum commitments and timeboxes, adaptation, WIP, clocks, experiments. |
| [risk-and-issues](../answers/risk-and-issues/contingency-and-reserves.md) | 6 | State changes, responses, opportunities, scales, reserves, escalation. |
| [budget-and-commercials](../answers/budget-and-commercials/budget-baseline-forecast.md) | 5 | Forecast arithmetic, EVM limits, contracts, margin, supplier exit. |
| [stakeholders-and-communication](../answers/stakeholders-and-communication/bad-news-and-expectations.md) | 6 | Engagement, RACI, concrete reporting, conflict, negotiation. |
| [leadership-and-behavioral](../answers/leadership-and-behavioral/conflict-and-team-health.md) | 5 | Feedback, authority, STAR evidence, inherited-project assessment. |
| [technical-literacy](../answers/technical-literacy/api-integration.md) | 6 | Environment fidelity, API uncertainty, decisions, debt, migration recovery. |
| [quality-and-release](../answers/quality-and-release/defect-triage.md) | 6 | Evidence, acceptance, triage, release boundaries, operational exit. |
| [metrics-and-improvement](../answers/metrics-and-improvement/burndown-burnup.md) | 6 | Denominators, worked charts, metric pitfalls, action verification. |
| [healthcare](../answers/healthcare/clinical-validation.md) | 6 | All six rewritten: workflow, HIPAA/GDPR/FTC, FHIR, clinical evidence, device boundaries, safety. |
| [fintech](../answers/fintech/financial-correctness.md) | 6 | All six rewritten: lifecycle, uncertainty, reconciliation, KYC operations, PCI and applicability. |
| [cybersecurity](../answers/cybersecurity/cyber-incident-coordination.md) | 6 | All six rewritten: outcomes, secure development, vulnerability signals, incidents, IAM, SOC. |
| [product-adjacent](../answers/product-adjacent/outcomes-and-experiments.md) | 4 | Compact discovery, RICE calculation, roadmap boundaries, evaluation. |
| [delivery-adjacent](../answers/delivery-adjacent/delivery-operating-model.md) | 4 | Continuing remit, queues, reliability policy, operating agreements. |
| [presales-adjacent](../answers/presales-adjacent/poc-and-demo.md) | 4 | Qualification, procurement boundaries, POC decisions, final-agreement handover. |

## Original reference disposition

“Readable” means the page or relevant official document was inspected for its use. It does not imply the source authored the original project scenario.

| Original reference | Disposition |
| --- | --- |
| [Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html) | Readable; retained where relevant, with expanded local explanation. |
| [The Scrum Guide (2020)](https://scrumguides.org/scrum-guide.html) | Readable; retained where relevant, with expanded local explanation. |
| [The Kanban Guide (May 2025)](https://kanbanguides.org/the-kanban-guide/2025.5/) | Readable; retained where relevant, with expanded local explanation. |
| [Google SRE Workbook: Incident Response](https://sre.google/workbook/incident-response/) | Readable; retained where relevant, with expanded local explanation. |
| [Google SRE Workbook: Postmortem Culture](https://sre.google/workbook/postmortem-culture/) | Retained for learning; STAR also cites the specific interview-method source. |
| [UK Government: Project Delivery Functional Standard](https://www.gov.uk/government/publications/project-delivery-functional-standard) | Replaced landing page with full GovS 002 v2.1 and relevant section labels. |
| [NSF: Earned Value Management Gold Card](https://www.nsf.gov/od/ori/evm-gold-card) | Readable; retained where relevant, with expanded local explanation. |
| [GAO: Schedule Assessment Guide](https://www.gao.gov/products/gao-16-89g) | Readable; retained where relevant, with expanded local explanation. |
| [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) | Final 1.1 retained; official index added to distinguish draft 1.2. |
| [NIST SP 800-61 Rev. 3: incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Readable; retained where relevant, with expanded local explanation. |
| [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) | Readable; retained where relevant, with expanded local explanation. |
| [OWASP: Application Security Verification Standard](https://asvs.owasp.org/) | Checked stable 5.0.0; distinguished from development content. |
| [NIST: Cybersecurity Framework](https://www.nist.gov/cyberframework) | Readable; retained where relevant, with expanded local explanation. |
| [MITRE ATT&CK: adversary tactics and techniques](https://attack.mitre.org/) | Readable; retained where relevant, with expanded local explanation. |
| [FIRST: Common Vulnerability Scoring System](https://www.first.org/cvss/) | Replaced broad index with CVSS 4.0 specification; added EPSS distinctions. |
| [CISA: Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Direct access restricted; official CISA mirror added and limitation disclosed. |
| [DORA: software delivery performance metrics](https://dora.dev/guides/dora-metrics/) | Readable; retained where relevant, with expanded local explanation. |
| [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) | Readable; retained where relevant, with expanded local explanation. |
| [Stripe: idempotent requests (provider-specific example)](https://docs.stripe.com/api/idempotent_requests) | Readable; retained where relevant, with expanded local explanation. |
| [Stripe: webhook handling (provider-specific example)](https://docs.stripe.com/webhooks) | Readable; retained where relevant, with expanded local explanation. |
| [FATF Recommendations](https://www.fatf-gafi.org/en/topics/fatf-recommendations.html) | Replaced with consolidated Recommendations, amended June 2026. |
| [Stripe: Payment Intents (provider-specific example)](https://docs.stripe.com/payments/payment-intents) | Readable; retained where relevant, with expanded local explanation. |
| [PCI SSC: PCI DSS](https://www.pcisecuritystandards.org/standards/pci-dss/) | Readable; retained where relevant, with expanded local explanation. |
| [EBA: payment services and electronic money](https://www.eba.europa.eu/regulation-and-policy/payment-services-and-electronic-money) | Direct access restricted; replaced by readable European Commission material. |
| [EBA: Digital Operational Resilience Act](https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act) | Direct access restricted; replaced by readable ESMA DORA material. |
| [PMI: what is project management](https://www.pmi.org/about/what-is-project-management) | Readable; retained where relevant, with expanded local explanation. |
| [FDA: device software functions and mobile medical applications](https://www.fda.gov/medical-devices/digital-health-center-excellence/device-software-functions-including-mobile-medical-applications) | Retained for general scope; added specific current and clinical-safety references. |
| [HL7: FHIR R4 overview (versioned example)](https://hl7.org/fhir/R4/overview.html) | Retained as partner-version example; publication directory and status added. |
| [HL7: FHIR security considerations](https://hl7.org/fhir/security.html) | Readable; retained where relevant, with expanded local explanation. |
| [GOV.UK Service Manual: learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) | Readable; retained where relevant, with expanded local explanation. |
| [HHS: covered entities and business associates](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html) | Readable; retained where relevant, with expanded local explanation. |
| [European Union: data protection under GDPR](https://europa.eu/youreurope/business/governance-and-sustainability/digital-and-data-compliance/data-protection-gdpr/index_en.htm) | Readable; retained where relevant, with expanded local explanation. |
| [HHS: guidance on de-identification of PHI](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html) | Readable; retained where relevant, with expanded local explanation. |
| [GOV.UK Service Manual: discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) | Readable; retained where relevant, with expanded local explanation. |
| [Intercom: RICE prioritization](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers) | Readable; retained where relevant, with expanded local explanation. |
| [Google SRE Workbook: Canarying Releases](https://sre.google/workbook/canarying-releases/) | Readable; retained where relevant, with expanded local explanation. |
| [NIST SP 800-30 Rev. 1: risk assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final) | Readable; retained where relevant, with expanded local explanation. |
| [W3C: WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/) | Readable; retained where relevant, with expanded local explanation. |

## Verification

Local checks cover the catalog, relative links, section anchors, images, accessible SVG descriptions, and figure coverage. Calculations are explicit in the reproducible generator. All 32 PNG previews were visually inspected; overflowing text and misleading category arrows were corrected.

Every answer carries its review date and references. Run `python scripts/check_docs.py` to reproduce local link and asset checks. This check does not replace human source interpretation.
