# How do you manage cybersecurity risk from suppliers, subcontractors, and software dependencies?

[Back to questions](../../README.md#cybersecurity-domain)

**Level:** Senior · **Topic:** Cybersecurity Domain · **Reviewed:** 2026-10-30

## Answer

Identify the capability being supplied and the exposure it creates: access, data processing, service criticality, software components, update channels, subcontractors, or recovery dependencies. Assess suppliers proportionately to that context.

## Evaluate more than a questionnaire

Establish relevant assurance evidence, scope and exclusions, control ownership, incident cooperation, change notification, data handling, continuity, and exit arrangements. A certificate or report can inform the assessment but must relate to the actual service and period.

For software dependencies, clarify inventory, provenance, vulnerability intake, supported updates, and ownership after handover. An SBOM improves visibility; it does not by itself establish safety or ensure timely remediation.

## Example: hidden common dependency

Two nominally independent suppliers rely on the same hosting region or identity service. A plan that treats them as independent fallback paths can underestimate correlated failure. Ask for evidence about the operating dependency and assess a realistic recovery scenario.

## Follow risk through the lifecycle

| Stage | Work to coordinate |
| --- | --- |
| Selection | Criticality, access/data scope, alternatives, and evidence |
| Agreement | Responsibilities, relevant obligations, support, and exit |
| Onboarding | Safe access, integration, controls, and verification |
| Operation | Material changes, incidents, findings, and ongoing ownership |
| Exit | Access removal, data and knowledge transfer, residual obligations |

Maintain owners and escalation for unresolved exposure. Reassess when the service, data use, subcontractors, or critical dependencies change; procurement approval is not a permanent security assessment.

The PM integrates these activities into sourcing and delivery. Security, business, commercial, privacy, and legal owners make their respective decisions. NIST SP 800-161 supplies a systems-and-organizations reference; actual contractual and regulatory requirements depend on the engagement.

## References

- [NIST SP 800-161 Rev. 1, updated 2024: cybersecurity supply-chain risk](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final)
- [NIST SSDF: secure development and software acquisition context](https://csrc.nist.gov/pubs/sp/800/218/final)
