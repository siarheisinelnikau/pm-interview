# What should a PM clarify before planning a healthcare project?

[Back to questions](../../README.md#healthcare-domain)

**Level:** Middle · **Topic:** Healthcare Domain · **Reviewed:** 2026-10-30

## Answer

Healthcare discovery starts with **the workflow and the consequence of being wrong**. A booking service, a clinical record viewer, and a function recommending treatment can share a technology stack while needing very different evidence and governance.

## Map the complete care process

Ask who initiates the workflow, who receives the output, what decision it influences, and what happens if the output is missing, late, incorrect, or attached to the wrong patient. Observe work across shifts and systems, including telephone calls and manual workarounds.

| Area | Questions that change the plan |
| --- | --- |
| Intended use | Administrative support, information display, diagnosis, monitoring, or treatment? |
| Setting and market | Which country, care setting, sites, and intended patient population? |
| Identity and data | How are patient records matched, corrected, accessed, and transferred? |
| Clinical ownership | Who assesses hazards, clinical evidence, and readiness? |
| Operations | What happens during downtime, staff absence, or a failed integration? |

Identify accessibility, staff training, device availability, and integration constraints before estimating a rollout.

## Example: referral intake

A request for “automatic referral triage” may conceal two problems: missing information and a clinical routing decision. The first might be reduced by a better intake process. The second needs a separate intended-use, clinical-risk, and potentially medical-device assessment.

Produce a problem statement, workflow map, boundary, measurable outcome, initial hazard list, and validation plan. Assign clinical, product, technical, operational, privacy, and regulatory decisions explicitly.

## Evidence and applicability

For health IT within the relevant NHS England context, investigate DCB0129 for manufacture and DCB0160 for deployment and use. These are jurisdiction-specific examples, not worldwide requirements. Medical-device qualification and clinical-safety assessment are related but distinct: a product outside device regulation can still create harmful workflow failures.

The PM coordinates evidence and decision timing. Qualified clinical and regulatory owners determine the required assessment and whether the proposed use is supported.

## References

- [NHS England: clinical risk management standards, DCB0129 and DCB0160](https://digital.nhs.uk/services/clinical-safety/clinical-risk-management-standards)
- [FDA: device software functions and platform-independent assessment](https://www.fda.gov/medical-devices/digital-health-center-excellence/device-software-functions-including-mobile-medical-applications)
- [GOV.UK: learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs)
