# What should a PM understand about eligibility, prior authorization, claims, and remittance workflows?

[Back to questions](../../README.md#healthcare-domain)

**Level:** Middle · **Topic:** Healthcare Domain · **Reviewed:** 2026-10-30

## Answer

Map the administrative and financial journey separately from clinical care. A patient receiving care, a claim passing technical validation, a payer making a coverage/payment decision, and the provider reconciling a payment are different events.

## Follow the workflow

| Stage | Scope to clarify |
| --- | --- |
| Eligibility and benefits | Identity, coverage information, timing, and missing responses |
| Authorization or referral | Whether applicable, required information, status, and follow-up |
| Claim submission | Coding inputs, validation, acknowledgment, rejection, and resubmission |
| Adjudication | Payer decision, adjustments, denial reasons, and review paths |
| Remittance and reconciliation | What was paid, adjusted, or remains outstanding |

The exact process depends on the market, payer, provider, product, and agreement. US HIPAA transaction materials are one example; do not assume a single protocol or rule applies worldwide.

## Example: accepted is not paid

A clearinghouse accepts a claim file, but a later payer decision denies a claim because required information is missing. A dashboard that marks the account complete at file acknowledgment will hide the unresolved work and cash impact.

Agree the state model, identifiers linking submissions and corrections, responsible teams, aging measures, and escalation. Repeated submission without understanding the state can create duplicates or additional manual work.

## Plan exceptions and operations

Include incomplete eligibility information, missing authorization where relevant, changed demographics, rejected claims, partial payment, denials, corrections, and remittance matching. Define who supplies coding and billing expertise and who can approve a correction.

Estimate integration, representative test data, payer validation, staff training, and operating capacity. Measure successful completion and aged exceptions alongside submission volume.

Eligibility or authorization information should not be presented as an unconditional promise of payment. The PM coordinates the evidence and workflow; clinical, billing, payer, and compliance owners determine the relevant business rules.

## References

- [CMS: health care transactions, standards, and operating-rule FAQs](https://www.cms.gov/priorities/key-initiatives/burden-reduction/administrative-simplification/transactions/faqs)
