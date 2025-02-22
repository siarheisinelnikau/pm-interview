# How does a lending project differ from a payment integration project?

[Back to questions](../../README.md#fintech-domain)

**Level:** Middle · **Topic:** Fintech Domain · **Reviewed:** 2026-10-30

## Answer

Lending creates an ongoing customer and financial relationship. Scope extends beyond a successful application or disbursement to decisioning, agreed terms, account servicing, repayments, changes, complaints, and resolution.

## Map the lifecycle and owners

| Stage | Questions for the delivery plan |
| --- | --- |
| Application and verification | Required information, permissions, evidence, and incomplete cases |
| Credit decision | Policy/model owner, decision evidence, review and explanation requirements |
| Offer and funding | Approved terms, disclosures where applicable, acceptance, and disbursement |
| Servicing | Balances, schedules, payment allocation, statements, and changes |
| Difficulties and closure | Arrears, support, complaints, corrections, settlement, and records |

Products and jurisdictions differ. US mortgage examination procedures provide a concrete origination/servicing example, not a complete rulebook for every loan or market.

## Example: disbursement works, servicing does not

The team demonstrates a funded loan but has not verified partial repayment, an early payment, a rate or schedule change where allowed, or correction of a misapplied payment. Customers may then receive incorrect balances or communications even though the launch metric looks successful.

Agree financial invariants and representative scenarios with credit, finance, servicing, engineering, and compliance owners. Validate rounding, relevant date boundaries, histories, adjustments, and reconciliation according to the approved product rules.

## Plan responsible decisioning and operations

Identify relevant obligations around customer treatment, disclosures, privacy, decision explanation, and complaints. If automated decisioning is used, establish data/model ownership, review, change control, and the evidence required to assess relevant risks.

Plan specialist participation, data migration, borrower communications, staff capability, and ongoing support. The PM does not independently set lending policy or legal interpretations. A credible delivery boundary includes the operating capability needed after origination, not only the application front end.

## References

- [CFPB: mortgage origination examination procedures, a US example](https://www.consumerfinance.gov/compliance/supervision-examinations/mortgage-origination-examination-procedures/)
- [CFPB: mortgage servicing examination procedures, July 2026 US example](https://files.consumerfinance.gov/f/documents/cfpb_mortgage-servicing-exam-procedures_2026-07.pdf)
