# What additional planning does an open-banking integration need beyond connecting an API?

[Back to questions](../../README.md#fintech-domain)

**Level:** Middle · **Topic:** Fintech Domain · **Reviewed:** 2026-10-30

## Answer

Agree the market, participant roles, service, and supported bank contract. Account-information access and payment initiation have different journeys and consequences. UK Open Banking standards are a useful example, not a worldwide implementation requirement.

## Treat permission as a lifecycle

Establish how the customer understands and authorizes the service, authenticates with the relevant provider, sees connected access, and changes or revokes it. Confirm token and permission expiry, reauthentication conditions, error behavior, and responsibilities across parties.

Authentication and permission to use data are related but distinct. A successful redirect does not establish that all requested permissions were granted or that a payment completed.

## Test customer and operational journeys

| Concern | Example |
| --- | --- |
| Bank differences | Supported capabilities, profiles, and production onboarding |
| Customer return | Cancellation, interruption, missing state, or delayed outcome |
| Permission changes | Reduced scope, expiry, revocation, and reconnect |
| Data | Freshness, missing transactions, duplicates, and reconciliation |
| Operations | Availability, version changes, incidents, and support ownership |

For payment initiation, preserve the distinction between an uncertain result and a confirmed failure before considering a retry.

## Example

A customer disconnects an account, but a background job continues polling with an existing credential. The project needs a verified propagation path for the approved revocation behavior, plus the appropriate handling of data already received. Removing the visible connection alone is incomplete.

Plan representative banks, safe test data, production access, relevant security profiles, conformance evidence, monitoring, and customer support. Establish permitted data use and retention with the responsible owners.

A PM should expose differences that affect estimates and readiness rather than assuming one sandbox success proves every bank and customer journey is supported.

## References

- [Open Banking UK: customer-experience guidelines](https://standards.openbanking.org.uk/customer-experience-guidelines/latest/)
- [Open Banking UK: API specifications and participant resources](https://standards.openbanking.org.uk/)
