# How would you turn an ambiguous request into shared requirements?

[Back to questions](../../README.md#scope-and-requirements)

**Level:** Junior · **Topic:** Scope and Requirements · **Reviewed:** 2026-10-30

## Answer

Clarify the problem, affected users, current workflow, desired outcome, and constraints before accepting a proposed solution. Use examples, observation, and short conversations with actual users and operational teams. Record what remains uncertain.

If a client asks for an AI triage tool, investigate the triage problem, consequences of error, intended use, and existing escalation process before estimating a model implementation. Summarize the smallest valuable scope and observable acceptance conditions. Validate that summary with the relevant decision makers. Requirements become useful when people can identify different interpretations, not when a large document hides them.

## Turn a solution request into a problem statement

“Build AI triage” might become: “Nurses spend 20 minutes gathering missing information before routing a referral; reduce avoidable collection work while preserving clinical escalation.” Those example numbers require validation before becoming a business case.

Map the current journey, observe exceptions, and ask what happens when the tool is wrong or unavailable. Test whether a simpler form, integration, or process change solves the problem first.

Produce a short output: user need, outcome measure, boundaries, examples, constraints, assumptions, and next validation step. Agree which uncertainty blocks an estimate and which can be explored during delivery. Discovery is complete enough when the next investment decision is supported, not when all uncertainty disappears.

## References

- [GOV.UK Service Manual: discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works)
- [GOV.UK Service Manual: learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs)
