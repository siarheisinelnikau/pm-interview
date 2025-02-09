# How would you run a useful incident postmortem and track improvements?

[Back to questions](../../README.md#metrics-and-continuous-improvement)

**Level:** Middle · **Topic:** Metrics and Continuous Improvement · **Reviewed:** 2026-10-30

## Answer

Document impact, timeline, detection, response, and contributing conditions using available evidence. Explore why the system made the failure possible, including unclear ownership or incentives. Keep accountability for improvement without turning the review into personal blame.

Choose specific actions with owners, deadlines, and verification. “Be more careful” is not a durable control. An action might add a reconciliation alert, test a recovery procedure, or change release criteria. Review completion and whether recurrence or impact declined. Keep sensitive incident detail appropriately restricted, and feed relevant findings into risk management, planning, and future readiness decisions.

## Track the improvement beyond ticket closure

Separate immediate recovery, contributing conditions, and prevention. A useful action might change retry behavior, add a missing reconciliation signal, or rehearse recovery with the actual on-call team.

Record the intended effect and verification method. “Alert configured” is incomplete if it has never detected the relevant scenario or reached someone able to respond. Prefer a small set of consequential actions over a long list nobody can fund.

Blameless analysis does not remove responsibility for decisions or misconduct processes; it helps people report evidence and examine system conditions. Review similar incidents over time to see whether repeated patterns require changes to ownership, architecture, capacity, or incentives.

## References

- [Google SRE Workbook: Postmortem Culture](https://sre.google/workbook/postmortem-culture/)
