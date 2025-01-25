# How would you design a staged rollout and recover from a bad release?

[Back to questions](../../README.md#quality-release-and-operations)

**Level:** Senior · **Topic:** Quality, Release, and Operations

## Answer

Agree cohorts, observation windows, user-impact signals, and stop conditions. Start with a limited population where useful and compare behavior against a meaningful baseline. Ensure someone can act on the signals.

Stopping further exposure does not undo changes already applied to users or data. Recovery may require a flag, corrective deployment, compatible rollback, or reconciliation. Check whether flags can affect the failure path and whether an older version can interpret newly written data. Assign the recovery authority and rehearse critical actions. Resume only when the team understands the exposure and has evidence that the corrective action works.

## References

- [Google SRE Workbook: Canarying Releases](https://sre.google/workbook/canarying-releases/)
