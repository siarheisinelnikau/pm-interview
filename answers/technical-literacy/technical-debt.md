# How would you prioritize technical debt against new functionality?

[Back to questions](../../README.md#technical-literacy-for-pms)

**Level:** Middle · **Topic:** Technical Literacy for PMs · **Reviewed:** 2026-10-30

## Answer

Describe the concrete consequence: recurring incidents, slow changes, security exposure, expensive support, or an approaching platform constraint. Ask for evidence, options, effort, and the expected effect of improvement. Connect the discussion to the product and service objectives.

If a fragile test suite delays every release, trial a targeted fix and measure waiting or failure reduction. Some debt is an informed short-term trade-off; some creates unacceptable risk. Record intentional deferrals with an owner and revisit trigger. Avoid assuming every refactor creates business value or demanding a precise financial return for every necessary engineering improvement.

## Compare treatment options

For a flaky integration test suite, options might include fixing the highest-impact tests, improving the environment, replacing a dependency, or accepting a bounded manual check temporarily. Estimate the expected reduction in waiting and failure, plus implementation and maintenance effort.

Prioritize debt linked to an actual constraint or unacceptable exposure. Some preventive work is necessary even when its avoided cost is difficult to quantify. Ask for the mechanism and evidence rather than a fabricated ROI.

Review after the intervention: did releases become easier to verify, did incidents fall, or did the bottleneck move elsewhere? A refactoring ticket closing is an output; the expected delivery or risk improvement needs inspection.

## References

- [DORA: software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
