# How does shared responsibility affect a cloud migration or managed-service project?

[Back to questions](../../README.md#cybersecurity-domain)

**Level:** Middle · **Topic:** Cybersecurity Domain · **Reviewed:** 2026-10-30

## Answer

Assign security and operational responsibilities for the actual services being used. A provider managing infrastructure does not mean it manages every customer configuration, application, identity, or data decision.

## Build a service-specific ownership matrix

| Area | Responsibility to establish |
| --- | --- |
| Infrastructure and platform | Provider scope, service guarantees, and evidence |
| Workload and configuration | Application behavior, relevant patching, network and tenant settings |
| Identity and access | Human/workload roles, privileged access, removal, and recovery |
| Data | Classification, permitted use, retention, protection, and key arrangements |
| Operations | Monitoring, incident coordination, backup, restore, and continuity |

The boundary changes with the service model and contract. In AWS's EC2 example, customers manage the guest operating system and their applications, including relevant patches. A managed service has a different boundary; confirm it rather than copying an IaaS checklist.

## Example: successful migration, exposed data

A service moves to managed storage, but an inappropriate access policy exposes customer data. Availability and infrastructure patching can be healthy while the customer's configuration is unsafe.

Plan configuration review, appropriate access tests, audit evidence, monitoring, and response ownership. Include secondary environments, exports, service accounts, and supplier support paths.

## Verify the operating capability

Confirm who can change policies, detect misuse, restore data, handle unavailable identity services, and communicate with the provider. Test representative recovery and incident-coordination scenarios; do not assume “managed backup” proves the required restoration result.

The PM coordinates the responsibilities, capacity, and evidence across teams and suppliers. Security and technical owners assess the controls. Shared responsibility should produce explicit ownership, not a gap where each party assumes the other will act.

## References

- [AWS: shared responsibility and service-dependent customer obligations](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [NIST SP 800-161: supplier and service dependency context](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final)
