# When do you need requirements traceability and an assumption log?

[Back to questions](../../README.md#scope-and-requirements)

**Level:** Middle · **Topic:** Scope and Requirements · **Reviewed:** 2026-10-30

## Answer

Traceability links a need or obligation to requirements, implementation, verification, and acceptance evidence. Use enough detail to answer what changes if a requirement changes and how completion can be demonstrated. The necessary rigor depends on product risk and governance.

Track unverified assumptions separately with an owner, validation action, and deadline. For example, “the client's identity service supports the required role claims” should trigger an integration check. Do not let an assumption silently become a confirmed requirement. A lightweight matrix can be enough for a small project; safety-critical work may require controlled evidence and formal change review.

## Keep a small evidence chain

| Need or obligation | Requirement | Verification evidence | Acceptance owner |
| --- | --- | --- | --- |
| Only an authorized reviewer sees a record | Access rules for defined roles | Positive and negative access tests | Business and security owners |
| Finance can resolve mismatches | Correlated transaction history | Reconciliation scenario | Finance operations |

Add versions when a requirement or result changes. Traceability works in both directions: a changed requirement identifies affected evidence, and a failed test identifies the need at risk.

For an assumption, record the consequence if false. “Client identity roles available” needs an access test before a dependent commitment, not merely an entry in a register. Match rigor to risk and applicable controls.

## References

- [GovS 002 v2.1: sections 7.7–7.8 and 8.3: change, traceability and requirements](https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/)
- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
