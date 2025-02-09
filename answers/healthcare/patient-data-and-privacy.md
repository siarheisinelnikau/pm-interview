# How do HIPAA, GDPR, and patient-data concerns affect the project plan?

[Back to questions](../../README.md#healthcare-domain)

**Level:** Middle · **Topic:** Healthcare Domain · **Reviewed:** 2026-10-30

## Answer

Start by establishing **jurisdiction, organizational role, purpose, and the actual data flow**. “Healthcare data” does not determine one worldwide compliance checklist.

![Patient data can leave through secondary paths. HIPAA scope, GDPR processing conditions, and other applicable duties require separate assessment. Removing names alone is not a de-identification method.](../../assets/diagrams/health-data.svg)

## Distinguish the frameworks

In the US, HIPAA applies to covered entities and business associates in its scope. Where a business-associate relationship exists, the relevant agreement and safeguards are part of delivery. A consumer health app outside HIPAA may still fall under FTC rules, including the Health Breach Notification Rule where its criteria apply, and other applicable law.

Where GDPR applies, processing health data generally needs both an Article 6 legal basis and an applicable Article 9 condition. Consent is not the only possible route, and a generic consent checkbox is not a universal solution. Establish controller/processor roles, purposes, retention, transfers, and the need for assessments with the privacy owner.

## Turn the assessment into work

Map collection, clinical storage, integrations, exports, logs, analytics, backups, and supplier support access.

| Work item | Evidence to plan |
| --- | --- |
| Access and identity | Appropriate roles, privileged paths, access removal, and tests |
| Secondary tools | What sensitive data reaches error reporting, analytics, and support |
| Agreements and suppliers | Responsibilities, permitted use, subcontractors, and incident contacts |
| Retention and recovery | Rules for deletion, archive, backup, and restoration |
| Incident handling | Escalation and applicable notification decisions |

Security safeguards and privacy permission answer different questions. Encryption does not establish a permitted purpose; a signed agreement does not prove the safeguards work.

## Example: test data

Removing patient names can leave dates, rare conditions, record identifiers, or free text that identify people. HIPAA describes Safe Harbor and Expert Determination methods; simple masking is not automatically either. Under GDPR, pseudonymized information can remain personal data. Prefer suitable synthetic data where feasible and validate any proposed use of real records.

**Review note:** HHS still labels the checked Security Rule update page as an NPRM. Do not present proposed measures as an enacted final rule merely because the proposal is recent.

## References

- [HHS: covered entities and business associates](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html)
- [European Union: GDPR, legal bases and special categories](https://europa.eu/youreurope/business/governance-and-sustainability/digital-and-data-compliance/data-protection-gdpr/index_en.htm)
- [HHS: de-identification methods and limitations](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html)
- [FTC: Health Breach Notification Rule](https://www.ftc.gov/legal-library/browse/rules/health-breach-notification-rule)
- [HHS: Security Rule NPRM, proposed status](https://www.hhs.gov/hipaa/for-professionals/security/hipaa-security-rule-nprm/index.html)
