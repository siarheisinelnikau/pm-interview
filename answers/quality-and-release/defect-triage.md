# How would you triage defects when there is not enough time to fix all of them?

[Back to questions](../../README.md#quality-release-and-operations)

**Level:** Middle · **Topic:** Quality, Release, and Operations · **Reviewed:** 2026-10-30

## Answer

Assess user impact, severity, frequency, exposure, workarounds, and release scope. Priority also considers urgency and business context. Ask the relevant product, engineering, quality, and risk owners to agree treatment.

A rare defect that changes a payment amount can be more serious than a frequent cosmetic issue. Choose among fixing and retesting, removing affected scope, delaying release, or accepting a tolerable residual exposure with the right authority. Record the decision and monitoring or support response. Do not hide an unresolved defect by relabeling it a change request or accepting it solely to preserve a date.

## Make severity and priority explicit

Severity describes the consequence of the defect; priority describes when it should be treated in the current context. Record affected users, exposure conditions, reproducibility, workaround, and evidence.

A severe failure in an inaccessible, excluded feature may lead to removing that feature from release. A cosmetic problem in a legally required disclosure can still need prompt correction. Bring the relevant business and specialist owners into those judgments.

Each disposition needs verification: a fix is retested, a removed feature is demonstrably inaccessible, and an accepted exception has a permissible scope, authority, expiry or review trigger, and response plan. Closing the ticket without changing or accepting the exposure is not a resolution.

## References

- [GovS 002 v2.1: sections 8.2, 8.6–8.9: quality, validation and transition](https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/)
- [OWASP: Application Security Verification Standard](https://asvs.owasp.org/)
