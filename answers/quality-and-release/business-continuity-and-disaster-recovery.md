# How do you plan and verify business continuity and disaster recovery?

[Back to questions](../../README.md#quality-release-and-operations)

**Level:** Senior · **Topic:** Quality, Release, and Operations · **Reviewed:** 2026-10-30

## Answer

Business continuity concerns sustaining important business activities through disruption. Disaster recovery concerns restoring affected technology and data. They must connect, but restoring a server alone does not show that the business can operate.

## Start from business impact

Identify critical workflows, their dependencies, the consequences of interruption, and acceptable recovery objectives with business and service owners. An RTO is a restoration-time objective; an RPO describes an acceptable data-loss window. Document the measurement boundary and scenario.

Include people, identity, external suppliers, networks, data, communications, and manual or degraded modes. A fallback is useful only if it has capacity, authority, and a safe operating procedure.

## Example

A payment service can restore its application while still lacking provider connectivity or a reconciled financial state. A hospital may need a clinically approved downtime workflow while records are unavailable. Those outcomes require more than infrastructure availability.

## Verify the recovery capability

| Exercise | Evidence it can provide |
| --- | --- |
| Tabletop | Roles, decisions, missing dependencies, and communications |
| Data restore | Recoverability, integrity, permissions, and practical duration |
| Failover or recovery rehearsal | End-to-end behavior under the chosen failure scenario |
| Return to normal | Reconciliation, new writes, handback, and remaining exceptions |

A backup-job success proves neither successful restoration nor the required recovery time. Capture measured results and differences from the target.

Agree who declares the event, authorizes fallback or failback, communicates with affected users, and owns remaining exceptions. Plan recurring verification after important changes. NIST SP 800-34 provides a US federal information-system planning reference; tailor its use to the organization's actual context rather than assuming its scope creates a universal legal obligation.

## References

- [NIST SP 800-34 Rev. 1: contingency planning and business impact](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)
- [GovS 002 v2.1: transition and operational continuity](https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/)
