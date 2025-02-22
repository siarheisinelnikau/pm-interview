# How do UAT, verification, business acceptance, and release approval differ?

[Back to questions](../../README.md#quality-release-and-operations)

**Level:** Junior · **Topic:** Quality, Release, and Operations · **Reviewed:** 2026-10-30

## Answer

Verification checks whether specified requirements are met. User Acceptance Testing (UAT) helps representative business users assess intended workflows. Business acceptance confirms agreed deliverables or outcomes at the relevant level. Release approval determines whether deployment or exposure can proceed.

These decisions may involve overlapping people, but do not assume one signature covers them all. Prepare scenarios, realistic data, entry and exit conditions, defect handling, and named authorities. A successful UAT session does not remove a security finding or establish operational readiness. Record exceptions and their owners explicitly, including the effect on contractual acceptance where relevant.

## Separate the records

| Decision | Example evidence |
| --- | --- |
| Verification | Requirements and design checks with recorded results |
| UAT | Representative users complete agreed workflows and exceptions |
| Business acceptance | Authorized owner accepts deliverables and documented qualifications |
| Release approval | Readiness evidence, residual exposure, operational and recovery arrangements |

A quality owner may verify requirements while an operational owner still rejects handover because no support team has been assigned. That is a real readiness gap even when UAT passed.

Agree entry criteria before asking users to test: a stable build, safe data, scenarios, access, and a process for findings. Record acceptance against the relevant version and scope. A later material change may invalidate earlier evidence.

## Handle contested acceptance

If the client refuses sign-off, compare the disputed behavior with the agreed scope, criteria, evidence, and version. Separate a defect, an ambiguous requirement, a readiness gap, and newly requested scope. Establish the acceptance authority and relevant contractual process with the commercial owner.

Propose a factual resolution: repair and retest, clarify the agreed interpretation, accept with documented qualifications where appropriate, or assess a change. Record the decision and its effect on release, payment, and remaining obligations. A demonstration or a ticket marked done does not independently settle contractual acceptance.

## References

- [GovS 002 v2.1: sections 8.2, 8.6–8.9: quality, validation and transition](https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/)
