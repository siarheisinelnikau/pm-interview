# What security and privacy questions belong in a PM's delivery plan?

[Back to questions](../../README.md#technical-literacy-for-pms)

**Level:** Middle · **Topic:** Technical Literacy for PMs · **Reviewed:** 2026-10-30

## Answer

Identify sensitive data, systems, users, trust boundaries, and third parties. Agree requirements with security and privacy owners, then plan implementation and verification work. Include access, test data, logging, retention, incident handling, and supplier dependencies.

Ask who authorizes data use, who can access it, how access is removed, and where evidence is stored. A penetration test near launch cannot replace earlier requirements and design decisions. Track findings through remediation, verification, and any approved residual-risk decision. The PM coordinates ownership and evidence; the specialist and authorized business owners make the relevant security and privacy judgments.

## Make a control verifiable

“Only support supervisors can export sensitive records” needs a defined role model, export scope, authorization checks, appropriate audit evidence, and tests for both permitted and denied access. Include service accounts and administrative paths.

Track each material requirement through implementation, evidence, findings, and ownership after release. Security tooling does not replace this chain. Clarify which practices are selected from the applicable framework and which are contractual or regulatory obligations.

Review data leaving through logs, analytics, error reporting, and vendor support. A design can secure the main database while exposing the same information through a secondary tool. Plan fixes and verification time instead of discovering that entire path during the final review.

## References

- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
- [OWASP: Application Security Verification Standard](https://asvs.owasp.org/)
