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

## References

- [GovS 002 v2.1: section 7.2: planning and estimating](https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/)
