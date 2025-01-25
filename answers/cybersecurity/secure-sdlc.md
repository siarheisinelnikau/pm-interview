# How do you include security in delivery without relying on a final penetration test?

[Back to questions](../../README.md#cybersecurity-domain)

**Level:** Middle · **Topic:** Cybersecurity Domain · **Source review:** 2026-10-30

## Answer

Agree security requirements and threat-related assumptions early. Plan appropriate design review, code and dependency checks, secrets handling, verification, remediation, and operational response. NIST SSDF and OWASP ASVS can support the work; select the practices and requirements relevant to the product.

Give findings owners and include remediation and retest capacity in the plan. A penetration test provides evidence within a scope and time window; it cannot prove the absence of vulnerabilities. Track third-party components and how future issues will be handled. Release evidence should show what was assessed, what remains, and who made the residual-risk decision.

## References

- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
- [OWASP: Application Security Verification Standard](https://asvs.owasp.org/)
