# Source and applicability notes

[Back to questions](../README.md) · [Review and source audit](source-audit.md) · [Visual guide](visual-guide.md)

References for the standards, frameworks, and jurisdiction-specific examples used in the guide. Version-sensitive answers record their review dates.

Examples, numbers, decision tables, and figures are original illustrative applications, not quotations from a standard or industry benchmarks. A framework's requirements apply within its scope; a suggested project practice is not automatically a legal obligation.

## Project delivery and measurement

| Area | Checked reference | Important boundary |
| --- | --- | --- |
| Governance and control | [GovS 002 v2.1, full text](https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/) | Answer references name relevant sections; UK-government requirements are not universal private-sector rules |
| Scheduling | [GAO Schedule Assessment Guide](https://www.gao.gov/products/gao-16-89g) | Assess dependencies, resources, critical/near-critical paths, uncertainty, and actual progress |
| Earned value | [NSF EVM Gold Card](https://www.nsf.gov/od/ori/evm-gold-card) | Work-value units differ from days; EAC formula assumptions matter |
| Scrum | [November 2020 Scrum Guide](https://scrumguides.org/scrum-guide.html) | Separate defined accountabilities and commitments from local practices |
| Kanban | [May 2025 Kanban Guide](https://kanbanguides.org/the-kanban-guide/2025.5/) | Define workflow boundaries, clocks, and policies before interpreting measures |
| DORA research | [Five-metric guide](https://dora.dev/guides/dora-metrics/) | Throughput includes failed deployment recovery time; instability includes change fail rate and deployment rework rate |
| Reliability | [Google SRE objectives](https://sre.google/sre-book/service-level-objectives/) | Request-based and time-based budgets have different denominators |
| Behavioral interviews | [National Careers Service STAR method](https://nationalcareers.service.gov.uk/careers-advice/interview-advice/the-star-method) | Use real experience; distinguish personal actions from collective results |

## Healthcare

| Topic | Checked baseline | Delivery implication |
| --- | --- | --- |
| HIPAA scope | [HHS covered entities and business associates](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html) | Establish organizational role; not every health app is in scope |
| Security Rule update | [HHS NPRM page](https://www.hhs.gov/hipaa/for-professionals/security/hipaa-security-rule-nprm/index.html) | The checked page identifies a proposal; distinguish proposed text from enacted requirements |
| Data handling | [GDPR guidance](https://europa.eu/youreurope/business/governance-and-sustainability/digital-and-data-compliance/data-protection-gdpr/index_en.htm), [HHS de-identification](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html) | Establish permitted processing and safeguards; masking or pseudonymization does not automatically remove all duties |
| Consumer health apps | [FTC Health Breach Notification Rule](https://www.ftc.gov/legal-library/browse/rules/health-breach-notification-rule) | Being outside HIPAA is not a universal exemption from health-data obligations |
| FHIR | [Publication directory](https://hl7.org/fhir/directory.html) | R5 5.0.0 is the checked current published release; R6 work-in-progress is not a final supported partner contract |
| US CDS boundary | [FDA final guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software) | January 29, 2026 supersedes January 6, 2026; assess all applicable criteria per function |
| US quality system | [FDA QMSR](https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr) | Effective February 2, 2026 for applicable device-manufacturer requirements |
| US device cybersecurity | [FDA February 2026 guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-medical-devices-quality-management-system-considerations-and-content-premarket) | Supersedes June 2025 guidance; assess actual applicability |
| EU device software | [MDCG 2019-11 Rev. 1](https://health.ec.europa.eu/system/files/2025-06/mdcg_2019_11_en.pdf) | June 2025 guidance distinguishes MDR/IVDR qualification and classification; guidance is not itself binding law |
| Clinical evaluation | [IMDRF N41FINAL:2017](https://www.imdrf.org/documents/software-medical-device-samd-clinical-evaluation) | Clinical association, technical validation, and clinical validation answer different evidence questions |
| Deployed clinical safety | [NHS England DCB0129/DCB0160](https://digital.nhs.uk/services/clinical-safety/clinical-risk-management-standards) | Manufacture and deployment/use duties have a jurisdiction-specific scope; UAT alone is incomplete evidence |

## Fintech

- [Consolidated FATF Recommendations](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html) are amended June 2026. Local arrangements implement this international baseline; it is not one identical law for every fintech.
- [PCI DSS](https://www.pcisecuritystandards.org/standards/pci-dss/) v4.0.1 is the checked baseline. The [limited revision](https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1) did not move March 31, 2025 for applicable future-dated requirements. Scope and validation depend on the actual environment.
- [European Commission payment-services materials](https://finance.ec.europa.eu/consumer-finance-and-payments/payment-services/payment-services_en) provide official PSD2 and reform links. Verify PSD3/PSR legal status and application dates separately from political agreement. The guide does not assign an unverified universal transition date.
- [EU DORA, described by ESMA](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/digital-operational-resilience-act-dora), has applied since January 17, 2025 to entities within its scope. It is distinct from DORA delivery research.
- Stripe supplies provider-specific examples of [authorization/capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method), [uncertain errors](https://docs.stripe.com/error-low-level), [events](https://docs.stripe.com/webhooks), and [reconciliation](https://docs.stripe.com/reports/balance). Other providers and rails differ; do not generalize one API's idempotency, state model, timing, or delivery contract globally.

## Cybersecurity

| Resource | Checked status or purpose | Boundary |
| --- | --- | --- |
| [NIST CSF](https://www.nist.gov/cyberframework) | CSF 2.0 outcomes | Framework alignment and deployment do not alone establish effectiveness or compliance |
| [NIST SSDF publication index](https://csrc.nist.gov/Projects/ssdf/publications) | SSDF 1.1 final; 1.2 draft in the checked index | Record the selected baseline; distinguish final and draft |
| [OWASP ASVS](https://asvs.owasp.org/) | Stable 5.0.0 in checked release information | Content and requirement identifiers are version-sensitive |
| [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Final April 2025; supersedes Rev. 2 | Response integrates with risk management and preparation |
| [CVSS 4.0](https://www.first.org/cvss/v4.0/specification-document) | Base, Threat, Environmental, Supplemental groups | Base severity is not complete organizational risk |
| [EPSS](https://www.first.org/epss/) | CVE exploitation probability over the next 30 days | Not an organization's breach probability |
| [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), [official mirror](https://github.com/cisagov/kev-data) | Known exploitation evidence | Absence is not safety; government-directive deadlines have a stated audience |
| [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) | Authentication, recovery, phishing resistance | MFA methods differ; normative requirements have a stated scope |
| [MITRE ATT&CK](https://attack.mitre.org/) | Evolving adversary-behavior knowledge base | A technique mapping is not proof of detection |

## Maintenance

Review material changes against a primary source, preserve local reasoning, and update the answer's date. Recheck versions, scope, legal status, and timing for a real project. Record access limits rather than converting them into unsupported claims of currency.
