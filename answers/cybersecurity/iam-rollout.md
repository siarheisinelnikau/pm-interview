# How would you plan an IAM or MFA rollout without locking out critical users?

[Back to questions](../../README.md#cybersecurity-domain)

**Level:** Middle · **Topic:** Cybersecurity Domain · **Source review:** 2026-10-30

## Answer

Inventory users, service accounts, privileged access, integrations, and recovery paths. Agree access policies and exceptions with security and service owners. Pilot representative users and applications, including emergency and operational scenarios.

Plan enrollment, communications, support capacity, break-glass controls, and monitoring. Test loss of an authenticator, account recovery, joiner/mover/leaver flows, and service dependencies. Roll out in controlled cohorts with stop conditions. Measure effective protection and adoption as well as configuration coverage. An MFA setting enabled in a console does not prove that every critical access path is protected or that legitimate recovery is safe.

## References

- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [OWASP: Application Security Verification Standard](https://asvs.owasp.org/)
