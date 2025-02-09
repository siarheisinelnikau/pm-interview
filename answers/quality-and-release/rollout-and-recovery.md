# How would you design a staged rollout and recover from a bad release?

[Back to questions](../../README.md#quality-release-and-operations)

**Level:** Senior · **Topic:** Quality, Release, and Operations · **Reviewed:** 2026-10-30

## Answer

Agree cohorts, observation windows, user-impact signals, and stop conditions. Start with a limited population where useful and compare behavior against a meaningful baseline. Ensure someone can act on the signals.

Stopping further exposure does not undo changes already applied to users or data. Recovery may require a flag, corrective deployment, compatible rollback, or reconciliation. Check whether flags can affect the failure path and whether an older version can interpret newly written data. Assign the recovery authority and rehearse critical actions. Resume only when the team understands the exposure and has evidence that the corrective action works.

## Use a meaningful comparison

An illustrative rollout might begin with a small cohort, then expand after sufficient observations of critical journeys, error rates, and support demand. Cohort size and observation time depend on traffic, risk, and how quickly failures emerge; fixed percentages are not universal best practice.

Compare similar populations and account for traffic mix. A quiet pilot can miss failures that appear only at scale or at a billing boundary.

Distinguish containment from restoration. Disabling a feature can stop new harm while leaving already changed data to reconcile. Assign that remaining work and verify recovery before closing the incident. A successful redeployment alone does not prove the affected users or records are repaired.

## References

- [Google SRE Workbook: Canarying Releases](https://sre.google/workbook/canarying-releases/)
