# How do you capture nonfunctional requirements early enough to affect delivery?

[Back to questions](../../README.md#scope-and-requirements)

**Level:** Middle · **Topic:** Scope and Requirements

## Answer

Cover performance, availability, accessibility, security, privacy, operability, and data integrity alongside business behavior. Express important requirements as measurable conditions under a stated load or scenario, with an owner and verification method.

“Fast” is ambiguous; “95 percent of eligible searches complete within two seconds at the agreed test load” can be checked. Identify whether the target applies to the service, client, or complete user journey. Budget time for environments and evidence. A late requirement for auditable access or recovery testing can change architecture and schedule, so raise it during discovery and revisit it as scope evolves.

## References

- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [W3C: WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/)
