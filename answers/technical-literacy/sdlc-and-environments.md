# What should a PM understand about the software development lifecycle and environments?

[Back to questions](../../README.md#technical-literacy-for-pms)

**Level:** Junior · **Topic:** Technical Literacy for PMs · **Reviewed:** 2026-10-30

## Answer

Understand how a change moves from a need through design, implementation, verification, deployment, and operation. Map where feedback, approvals, and handoffs occur. Different environments provide different evidence; a working developer setup does not prove production readiness.

Plan for representative integration access, safe test data, configuration, permissions, and release ownership. If the client provides a staging environment late, include that dependency in the forecast. Ask engineers which conditions are not reproduced in tests and how the remaining exposure will be managed. Focus on the decisions and constraints rather than attempting to prescribe implementation details.

## Ask what each environment proves

A development environment supports rapid implementation. Integration or staging environments can test dependencies and production-like configuration, but their fidelity varies. Production adds real traffic, data, permissions, and operational constraints.

Ask engineers which differences remain and how they affect confidence. For example, a test environment with one tenant and synthetic records may not expose permission isolation or realistic query load. Plan targeted verification rather than assuming the environment's name guarantees representativeness.

Track release artifacts and configuration so evidence refers to the actual change. Include test-data access, environment ownership, deployment permissions, and rollback feasibility in the schedule. A late environment is both a dependency and a constraint on the evidence available for launch.

## References

- [GovS 002 v2.1: sections 8.4–8.6: design, integration and verification](https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/)
- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
