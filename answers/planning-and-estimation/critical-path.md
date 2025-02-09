# What is the critical path, and how does it affect a delivery forecast?

[Back to questions](../../README.md#planning-and-estimation)

**Level:** Middle · **Topic:** Planning and Estimation · **Reviewed:** 2026-10-30

## Answer

The critical path is the longest-duration path through the activity network under the current assumptions. Its activities determine the earliest modeled finish. Float indicates how much an activity can move without delaying the relevant milestone; resource constraints may require revising the network.

![Integration 0–5, verification 5–8, approval 8–10 form a ten-day critical path. UI 0–6 has four days of float.](../../assets/diagrams/critical-path.svg)

If integration takes five days, verification three, and approval two in sequence, that path takes ten days even when separate UI work takes six. Accelerating UI work does not shorten it. Inspect assumptions, approval queues, and resource availability before choosing acceleration. More than one path can become critical after a change.

## Calculate float in the example

With both paths starting at day 0, integration plus verification plus approval finishes at day 10. UI work finishes at day 6, giving it four days of total float before it delays this launch, under the simplified assumptions.

If the same engineer must perform integration and UI work, the parallel model is invalid. Add that resource constraint and recalculate. Likewise, reducing verification from three days to one can change exposure and requires technical and quality judgment.

Use the critical path to target an intervention: shorten a genuinely driving activity, remove a dependency, or change scope. Monitor near-critical paths because an improvement to one path can make another path determine the finish.

## References

- [GovS 002 v2.1: section 7.2: planning and estimating](https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/)
