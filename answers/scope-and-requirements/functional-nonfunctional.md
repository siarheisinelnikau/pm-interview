# How do you capture nonfunctional requirements early enough to affect delivery?

[Back to questions](../../README.md#scope-and-requirements)

**Level:** Middle · **Topic:** Scope and Requirements · **Reviewed:** 2026-10-30

## Answer

Cover performance, availability, accessibility, security, privacy, operability, and data integrity alongside business behavior. Express important requirements as measurable conditions under a stated load or scenario, with an owner and verification method.

“Fast” is ambiguous; “95 percent of eligible searches complete within two seconds at the agreed test load” can be checked. Identify whether the target applies to the service, client, or complete user journey. Budget time for environments and evidence. A late requirement for auditable access or recovery testing can change architecture and schedule, so raise it during discovery and revisit it as scope evolves.

## Specify the measurement boundary

For a two-second response target, define the user journey, start and end events, population, percentile, load, observation period, and excluded conditions. A client-visible p95 is different from a server average. An average can hide a small group with very poor experience.

Add failure behavior: what users see after a timeout, how access is checked, and how operators detect trouble. For recovery, distinguish the target time to restore service (RTO) from the acceptable data-loss window (RPO).

Choose verification evidence with specialists and budget for it. Accessibility also needs an agreed scope and standard, such as applicable WCAG 2.2 criteria, plus user testing where useful; a passing automated scan is incomplete evidence.

## Include accessibility in usable acceptance

Define relevant user needs and applicable accessibility criteria early. Ask representative users to complete the important journey, including errors and recovery, with relevant assistive technologies and interaction methods. A form may pass automated checks while its validation messages remain difficult to find or understand.

Budget for design, specialist assessment where needed, remediation, and retesting. Record known limitations and their effect on the intended population; a scanner result alone does not establish that the service is usable or meets every applicable obligation.

## References

- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [W3C: WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/)
