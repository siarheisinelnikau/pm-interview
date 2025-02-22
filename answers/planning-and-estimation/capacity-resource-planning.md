# How do you plan capacity when people support several projects and production?

[Back to questions](../../README.md#planning-and-estimation)

**Level:** Middle · **Topic:** Planning and Estimation · **Reviewed:** 2026-10-30

## Answer

Start with actual availability, required skills, planned leave, support demand, and coordination time. Separate headcount from usable capacity. Obtain explicit allocation decisions when the same specialist appears in several plans.

![Forty person-days minus four leave, six support and four coordination leaves twenty-six planned person-days, subject to skills and dependencies.](../../assets/diagrams/capacity.svg)

If a security engineer has two days per week for the project, a five-day review will not necessarily finish in one calendar week. Sequence work and protect review windows. Use historical interruption patterns to make realistic forecasts and revisit them when demand changes. Treat persistent overload as a prioritization or staffing problem; assigning every person 100 percent to planned tasks leaves no room for uncertainty.

## Build a capacity calculation

Suppose four people have 40 nominal person-days over two weeks. Subtract four days of leave, six days of expected support, and four days for known training and coordination. The resulting 26 days is an illustrative planning allowance, not a standardized productivity factor.

Next check skills and sequence. Twenty-six general person-days cannot replace a specialist's required review window. Avoid subtracting the same meetings twice if the team's historical throughput already includes them.

Review actual interruptions against the assumption. If support repeatedly consumes more capacity, negotiate priority, staffing, service improvements, or scope. Preserve slack for variability; a plan that requires perfect availability is fragile even when its arithmetic adds up.

## Resolve competing project demands

If two initiatives require the same specialist in the same window, show their dependency paths, consequences, and alternatives to the person who can prioritize across both. Compare sequencing, reduced scope, qualified support, or changed dates. An allocation decision should appear in both plans; two separate promises cannot create a second specialist.

Inspect whether the apparent conflict is active work, review waiting, or a scarce approval. A reserved review window or better-prepared input may solve a different problem from adding headcount. Reforecast after the decision and make displaced work visible.

## References

- [GovS 002 v2.1: section 7.2: planning and estimating](https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/)
