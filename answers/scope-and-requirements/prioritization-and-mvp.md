# How do you prioritize scope and define an MVP under a deadline?

[Back to questions](../../README.md#scope-and-requirements)

**Level:** Middle · **Topic:** Scope and Requirements · **Reviewed:** 2026-10-30

## Answer

Start with the outcome and constraints, then identify the smallest end-to-end solution that can produce useful evidence or value. Consider user impact, urgency, effort, dependencies, and risk. Make trade-offs explicit with the person who owns priority.

For a patient intake service, a narrower supported workflow can be preferable to many incomplete forms. Essential identity, privacy, safety, and recovery controls still belong in the release boundary. Use MoSCoW or a scoring model to structure discussion, and validate the inputs. Calling everything a must-have prevents prioritization; calling an unsafe prototype an MVP does not justify exposing users to it.

## Make an end-to-end boundary

An intake MVP could support one referral type at one site, including identity checks, error handling, staff escalation, and operational support. It could defer other referral types or optional analytics. It should still let the intended user complete a coherent, supported journey.

Distinguish a prototype used for learning, a controlled pilot, and a production service. Each needs an explicit audience, data policy, permitted use, and exit or expansion decision.

MoSCoW or another score supports the conversation, but the decision maker must explain mandatory constraints and dependencies. Reducing breadth is often possible; removing essential controls changes the release's risk and may make it impermissible rather than merely minimal.

## References

- [GOV.UK Service Manual: discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works)
