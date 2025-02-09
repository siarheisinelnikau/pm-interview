# When would you use a burndown, a burnup, or a cumulative flow diagram?

[Back to questions](../../README.md#metrics-and-continuous-improvement)

**Level:** Middle · **Topic:** Metrics and Continuous Improvement · **Reviewed:** 2026-10-30

## Answer

A burndown emphasizes remaining work against time. A burnup shows completed work and total scope separately, making scope changes easier to see. A cumulative flow diagram shows how items accumulate across workflow states and can reveal growing queues.

![Two charts show remaining work versus scope and completion. At day four remaining work rises because scope increases, despite continued completion.](../../assets/diagrams/burnup-burndown.svg)

Choose based on the decision. If remaining work stays flat, a burnup may distinguish slow completion from added scope. If review work accumulates, inspect blocked items and capacity rather than only changing a chart. Use consistent item definitions and check source data. None of these charts alone proves business value, calendar predictability, or product quality.

## Read a scope change correctly

Suppose scope grows from 20 to 28 comparable items while completed work rises from 8 to 14. Remaining work rises from 12 to 14 even though six items finished. A burndown alone can make that period look unproductive; a burnup separates new scope from completion.

For a cumulative flow diagram, inspect the width of the in-progress band. A growing review band suggests accumulation in review, but verify actual workflow and data quality before naming the bottleneck.

State the units and treatment of reopens, removals, and state changes. Story points, items, and accepted deliverables produce different pictures. Use charts to investigate causes, not infer team effort or value directly.

## References

- [The Kanban Guide (May 2025)](https://kanbanguides.org/the-kanban-guide/2025.5/)
