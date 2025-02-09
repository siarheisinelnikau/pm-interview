# How would you forecast a date using throughput or Monte Carlo simulation?

[Back to questions](../../README.md#planning-and-estimation)

**Level:** Senior · **Topic:** Planning and Estimation · **Reviewed:** 2026-10-30

## Answer

Use completion history from work with comparable size and workflow boundaries. Simulate possible future completion sequences to produce a distribution of dates or scope. State the period, assumptions, capacity changes, and chosen confidence level.

![Illustrative completion distribution: median 5 weeks, 85th percentile 6 weeks. This is a model, not a commitment.](../../assets/diagrams/forecast-distribution.svg)

For example, a forecast might suggest an 85 percent chance of completing the current backlog by a given date. That result is conditional on stable scope and representative history. Large hidden dependencies, changing item size, or new teams can invalidate the model. Track new work and actual completion, rerun when assumptions change, and explain the result as a forecast rather than a guarantee.

## Explain a simulation clearly

For an illustrative 20-item backlog, sample historical weekly completion counts, accumulate them until 20 items finish, and repeat many times. Report the resulting completion-date percentiles: for example, the median and the 85th percentile. The chart's probabilities describe the model, conditional on its assumptions.

Check that historical weeks represent the planned work and capacity. Split unusually large items, identify work that cannot start until an external event, and model scope arrival when scope is not fixed. Pure throughput resampling does not resolve those dependencies.

Compare forecasts with later outcomes and investigate systematic optimism. More simulation runs reduce simulation noise; they do not repair biased input data or establish a guaranteed date.

## References

- [GAO Schedule Assessment Guide: schedule risk analysis](https://www.gao.gov/products/gao-16-89g)
- [GovS 002 v2.1: section 7.2, evidence and probabilistic simulation](https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/)
- [The Kanban Guide (May 2025)](https://kanbanguides.org/the-kanban-guide/2025.5/)
