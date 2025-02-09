# A hospital wants to launch despite unresolved patient-matching errors. What do you do?

[Back to questions](../../README.md#healthcare-domain)

**Level:** Senior · **Topic:** Healthcare Domain · **Reviewed:** 2026-10-30

## Answer

Treat unresolved patient-matching errors as a **clinical and data-integrity issue requiring an explicit readiness decision**. A sponsor's preferred date is not evidence that the workflow is safe.

## Establish and contain the exposure

Bring together the clinical safety owner, engineering, quality, operations, privacy, and release authority as relevant. Identify affected patients or record sets, failure conditions, existing exposure, detectability, and possible consequences. Preserve appropriate evidence and restrict the affected workflow while the assessment is unresolved.

Check whether incorrect associations already reached users or downstream systems. Stopping new exposure does not correct records already affected; reconciliation and authorized clinical review may remain necessary.

## Compare feasible options

| Option | Evidence needed before choosing it |
| --- | --- |
| Fix and retest | Root cause understood; representative regression and clinical workflow evidence |
| Narrow the release | Affected paths are demonstrably excluded and the remaining use is supported |
| Approved fallback | Clinical and operational owners confirm capacity, safe use, and limitations |
| Postpone | Consequences and revised evidence plan understood |

A pilot helps only if its boundary and controls address this failure. Fewer users do not make an unresolved harmful failure acceptable by themselves. Do not invent a manual safeguard in the meeting without the clinical owner's assessment.

## Make and record the decision

Present the impact, evidence gaps, options, recommendation, and next useful decision time. Record who can authorize the release and any permissible residual-risk decision, the allowed cohort and workflow, and what invalidates approval. Risk acceptance cannot waive applicable legal duties.

Set stop conditions, support arrangements, and a review of affected records. Reopen readiness after material corrections or scope changes. Close the issue only when both the technical behavior and remaining clinical/data consequences have been verified by the appropriate owners.

In an interview, explain the actions you coordinate and the specialist decisions you obtain; a PM should not independently declare clinical safety.

## References

- [NHS England: manufacture and deployment/use clinical risk management](https://digital.nhs.uk/services/clinical-safety/clinical-risk-management-standards)
- [GovS 002 v2.1: sections 8.6–8.9, validation and transition](https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/)
- [IMDRF: SaMD clinical evaluation, where applicable](https://www.imdrf.org/documents/software-medical-device-samd-clinical-evaluation)
