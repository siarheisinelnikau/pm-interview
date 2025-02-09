# What should a project quality strategy cover?

[Back to questions](../../README.md#quality-release-and-operations)

**Level:** Junior · **Topic:** Quality, Release, and Operations · **Reviewed:** 2026-10-30

## Answer

Define the important product and service risks, expected quality, evidence needed, and owners. Agree how reviews, automated tests, integration checks, exploratory testing, and operational validation contribute. Plan environments and data as explicit dependencies.

Prioritize evidence around critical journeys and damaging failures. For example, a refund service needs duplicate-handling and reconciliation checks as well as successful-path testing. Review quality throughout delivery rather than collecting it in a final phase. Test counts and code coverage can inform investigation, but neither proves that users can safely complete the intended workflow.

## Allocate evidence according to consequence

For a refund service, map financial correctness, permissions, duplicate handling, unavailable dependencies, and operator recovery to specific checks. Use fast automated checks where suitable, representative integration tests, and exploratory work for unexpected interactions.

Define who supplies test data, who reviews results, and what failures prevent further release activity. Make quality work part of capacity and completion, not an unestimated activity assigned to a final week.

A risk-based strategy explains why some scenarios need deeper evidence than others. Revisit it after a defect or scope change exposes a new failure mode. Passing the planned tests is useful evidence, but the team should still ask whether the plan covered the important risks.

## References

- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
- [OWASP: Application Security Verification Standard](https://asvs.owasp.org/)
