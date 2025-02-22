# How would you plan ISO 27001 certification or SOC 2 assurance work, and how do the outcomes differ?

[Back to questions](../../README.md#cybersecurity-domain)

**Level:** Middle · **Topic:** Cybersecurity Domain · **Reviewed:** 2026-10-30

## Answer

Establish the business objective, assessment scope, criteria, intended users of the result, assessor, and evidence needed. “Pass a security audit” is too ambiguous to plan.

## Distinguish the outcomes

ISO/IEC 27001 concerns an information security management system. Certification applies to a defined organizational scope; it does not certify that every product is free of vulnerabilities.

SOC 2 is an assurance reporting engagement about a service organization's system and relevant controls against selected criteria. It is not an ISO-style product certificate. Type 1 addresses the description and suitability of control design at a specified date; Type 2 also addresses operating effectiveness over a specified period. Agree the exact engagement with the qualified auditor.

A penetration test answers a different, bounded technical-assessment question. None of these outcomes automatically substitutes for the others.

## Plan evidence and operating work

Identify control owners, relevant systems and suppliers, policies, implemented processes, records, exceptions, and remediation. Schedule assessor availability and evidence collection. For an operating-period assessment, writing a policy at the end does not retrospectively demonstrate that the process operated throughout the period.

## Example

A team deploys access-review tooling but cannot show the defined population, decisions, removed access, or treatment of exceptions. Treat that as an evidence or control-operation gap rather than declaring the control complete because the product is installed.

Track findings to remediation and verification, preserve an accurate description of scope, and assign continuing ownership after the project. Confirm the applicable criteria/version and distinguish draft publications from adopted criteria.

The PM coordinates scope, readiness, evidence, and decisions. Management owns its system and assertions; qualified assessors determine the assessment outcome.

## References

- [ISO: ISO/IEC 27001:2022 and ISMS scope](https://www.iso.org/standard/27001)
- [AICPA: SOC suite and assurance reporting](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services)
