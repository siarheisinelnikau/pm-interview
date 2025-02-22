# How do consent, representative access, and sensitive-record restrictions affect a patient-facing project?

[Back to questions](../../README.md#healthcare-domain)

**Level:** Middle · **Topic:** Healthcare Domain · **Reviewed:** 2026-10-30

## Answer

Separate who the person is, whom they may represent, which information they may access, and the purpose under which information is processed. One account relationship or checkbox cannot answer all four questions.

## Clarify the decisions

Clinical consent, authorization or another legal basis for data processing/disclosure, and a patient's communication preferences serve different purposes. Establish the applicable rules with clinical and privacy owners for the market and organization.

For representative access, determine how authority is established, its scope and duration, how it changes, and which exceptions apply. In the US HIPAA context, personal-representative and parental-access rules interact with state and other law. Do not implement a worldwide age threshold or assume a parent or caregiver always receives every record.

## Example: linked family accounts

A parent has portal access on behalf of a child. The project must consider changes in authority or applicable restrictions, record categories, identity verification, and access to messages, exports, notifications, and historic documents. Hiding one screen is insufficient if another path reveals the same information.

Translate approved rules into an access matrix and representative test cases. Include granted, refused, expired, disputed, and revoked authority, plus staff-assisted and emergency workflows where applicable.

## Preserve safe operation

Plan how decisions are recorded, reviewed, communicated, and propagated to connected systems. Specify what revocation means for future access and existing records; it does not automatically require deleting every record that the organization must retain.

Audit evidence should support investigation without creating another uncontrolled copy of sensitive information. Assign ownership for correction requests and contested access.

The PM plans dependencies, validation, rollout, and exception handling. Qualified owners establish the legal and clinical rules. The acceptance evidence should show that those approved rules hold across the actual access paths.

## References

- [HHS: personal representatives and minors](https://www.hhs.gov/hipaa/for-professionals/faq/personal-representatives-and-minors/index.html)
- [European Union: GDPR processing and special-category data](https://europa.eu/youreurope/business/governance-and-sustainability/digital-and-data-compliance/data-protection-gdpr/index_en.htm)
