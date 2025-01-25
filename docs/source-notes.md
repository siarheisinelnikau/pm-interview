# Source and applicability notes

[Back to questions](../README.md)

**Reference baseline checked:** 2026-10-30.

Answers combine established concepts with original, illustrative project scenarios. References support the underlying concepts; the examples and suggested actions are applications of those concepts, not quotations from a standard. No single source defines the correct operating model for every organization.

## Delivery frameworks and measurements

| Area | Reference baseline | How to use it |
| --- | --- | --- |
| Project delivery | [PMI overview](https://www.pmi.org/about/what-is-project-management) and [UK GovS 002](https://www.gov.uk/government/publications/project-delivery-functional-standard) | General foundations and an example of structured governance; UK government requirements are not universal private-sector obligations |
| Scrum | [Scrum Guide, November 2020](https://scrumguides.org/scrum-guide.html) | Distinguish defined accountabilities from local job titles; a Definition of Ready is not a required Scrum artifact |
| Kanban | [Kanban Guide, May 2025](https://kanbanguides.org/the-kanban-guide/2025.5/) | Define workflow boundaries before interpreting flow measurements |
| Software delivery research | [DORA metrics guide](https://dora.dev/guides/dora-metrics/) | The checked guide uses five metrics, including deployment rework rate and failed deployment recovery time; older material may use four |
| Secure development | [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) and [OWASP ASVS](https://asvs.owasp.org/) | Select and version relevant practices and requirements for the actual product |
| Incident response | [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | The checked final publication is dated April 2025 and supersedes Rev. 2 |

The source baseline is not a claim that a method guarantees an outcome or that these materials form a certification syllabus. Check the current source when a version or requirement matters to an interview or real project.

## Healthcare

- [HIPAA scope](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html) depends on covered-entity and business-associate status. A health-related app is not automatically within that scope.
- [GDPR data guidance](https://europa.eu/youreurope/business/governance-and-sustainability/digital-and-data-compliance/data-protection-gdpr/index_en.htm) includes special-category data. Determine territorial scope, organizational role, processing basis, and relevant conditions with the privacy owner.
- [FDA software guidance](https://www.fda.gov/medical-devices/digital-health-center-excellence/device-software-functions-including-mobile-medical-applications) provides a US example. Intended use, claims, function, and market affect assessment; it does not classify every healthcare product in every country.
- The [versioned FHIR R4 overview](https://hl7.org/fhir/R4/overview.html) is an integration example, not a claim that every partner uses R4 or that R4 is the newest release. Agree the release, profiles, implementation guide, and security model with the partner.

## Fintech

- [FATF recommendations](https://www.fatf-gafi.org/en/topics/fatf-recommendations.html) are an international baseline implemented through jurisdiction-specific arrangements. They are not a substitute for identifying local obligations.
- [PCI DSS](https://www.pcisecuritystandards.org/standards/pci-dss/) scope and assessment depend on the actual environment and payment data flow. Confirm the applicable version and validation route with the PCI owner.
- [EBA payment-services materials](https://www.eba.europa.eu/regulation-and-policy/payment-services-and-electronic-money) support the PSD2/SCA discussion. For a real launch, verify the current applicable framework, technical standards, exemptions, and any legislative transition.
- [EU DORA](https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act) concerns digital operational resilience and entities within its scope. It is distinct from DORA software delivery metrics.
- Stripe documentation is used as a concrete provider example. Payment rails, state models, idempotency retention, event delivery, and recovery contracts vary by provider.

## Cybersecurity

Use [NIST CSF](https://www.nist.gov/cyberframework), [FIRST CVSS](https://www.first.org/cvss/), [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), and [MITRE ATT&CK](https://attack.mitre.org/) for their different purposes. They do not individually establish organizational compliance, risk acceptance, or detection effectiveness.

Security findings need asset and business context. Notification and remediation deadlines depend on the actual legal, contractual, and organizational requirements; the guide deliberately avoids assigning one universal deadline.

## Maintenance

When updating an answer, check the primary source, preserve a concise local explanation, and record a review date for version-sensitive or regulatory changes. Keep applicability and role authority explicit. Update question counts and navigation if the catalog changes.
