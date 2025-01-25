# What should a project quality strategy cover?

[Back to questions](../../README.md#quality-release-and-operations)

**Level:** Junior · **Topic:** Quality, Release, and Operations

## Answer

Define the important product and service risks, expected quality, evidence needed, and owners. Agree how reviews, automated tests, integration checks, exploratory testing, and operational validation contribute. Plan environments and data as explicit dependencies.

Prioritize evidence around critical journeys and damaging failures. For example, a refund service needs duplicate-handling and reconciliation checks as well as successful-path testing. Review quality throughout delivery rather than collecting it in a final phase. Test counts and code coverage can inform investigation, but neither proves that users can safely complete the intended workflow.

## References

- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
- [OWASP: Application Security Verification Standard](https://asvs.owasp.org/)
