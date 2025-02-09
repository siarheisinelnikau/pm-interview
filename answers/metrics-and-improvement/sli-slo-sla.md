# How do SLIs, SLOs, SLAs, and error budgets differ?

[Back to questions](../../README.md#metrics-and-continuous-improvement)

**Level:** Middle · **Topic:** Metrics and Continuous Improvement · **Reviewed:** 2026-10-30

## Answer

An SLI measures service behavior, such as successful requests or eligible journeys. An SLO sets a target for that indicator over a defined window. An SLA is an agreement that can include consequences for missing a service level. An error budget expresses the allowed unreliability under the SLO.

![The budget is one thousand failed requests. Seven hundred failures consume seventy percent, leaving three hundred. This is not an outage-minute calculation.](../../assets/diagrams/error-budget.svg)

Define boundaries and exclusions carefully. A backend uptime target can be met while customers cannot complete onboarding. Agree how budget consumption affects delivery decisions, such as prioritizing reliability work. No universal percentage is appropriate for every service; choose targets with business and engineering owners using user needs, cost, and risk.

## Calculate a request-based budget

For 1,000,000 eligible requests and a 99.9 percent success SLO, the illustrative error budget is 1,000 failed requests. If 700 failures occur, 70 percent of the budget has been consumed. This is a request-based calculation; do not convert it directly into outage minutes.

A time-based availability measure uses a different denominator. User-journey measures may also need rules for retries, missing events, and abandoned attempts.

Agree a policy for fast budget consumption, such as investigating a release or prioritizing a reliability improvement. Targets and policies should reflect user needs and service risk. A strict target without an affordable engineering and operating plan is not a credible service commitment.

## References

- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
