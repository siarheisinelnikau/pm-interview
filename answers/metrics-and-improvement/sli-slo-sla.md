# How do SLIs, SLOs, SLAs, and error budgets differ?

[Back to questions](../../README.md#metrics-and-continuous-improvement)

**Level:** Middle · **Topic:** Metrics and Continuous Improvement

## Answer

An SLI measures service behavior, such as successful requests or eligible journeys. An SLO sets a target for that indicator over a defined window. An SLA is an agreement that can include consequences for missing a service level. An error budget expresses the allowed unreliability under the SLO.

Define boundaries and exclusions carefully. A backend uptime target can be met while customers cannot complete onboarding. Agree how budget consumption affects delivery decisions, such as prioritizing reliability work. No universal percentage is appropriate for every service; choose targets with business and engineering owners using user needs, cost, and risk.

## References

- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
