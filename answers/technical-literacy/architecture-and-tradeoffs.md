# How do you participate in architecture decisions without acting as the architect?

[Back to questions](../../README.md#technical-literacy-for-pms)

**Level:** Middle · **Topic:** Technical Literacy for PMs · **Reviewed:** 2026-10-30

## Answer

Ask the technical owner to explain options in terms of user needs, constraints, delivery cost, operational impact, and reversibility. Make architectural dependencies and uncertainty visible in the plan. Record important decisions with context and consequences.

If a team proposes replacing a legacy component, compare incremental integration, replacement, and temporary containment. Ask what evidence could reduce uncertainty and whether a bounded spike is worthwhile. The PM coordinates timing, funding, and cross-team effects; engineers own the technical assessment. Avoid choosing technology from popularity or treating a large rewrite as a guaranteed shortcut to delivery.

## Use a short decision record

Capture context, decision owner, viable options, recommendation, evidence, consequences, and review trigger. For a rewrite, compare migration complexity, coexistence with the old system, training, operating cost, and the path back if assumptions fail.

Ask which decisions are reversible and which create long-lived constraints. A bounded technical experiment can be worthwhile if its result changes an expensive decision. Set the hypothesis and useful output before funding it.

Connect the decision to the integrated plan. A new shared service may reduce future duplication while introducing present dependencies and support obligations. The PM helps the sponsor understand those consequences without claiming to determine technical correctness independently.

## References

- [GovS 002 v2.1: sections 8.4–8.6: design, integration and verification](https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/)
- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
