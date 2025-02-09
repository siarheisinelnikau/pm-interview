# What do PV, EV, AC, CPI, and SPI tell you, and what are their limitations?

[Back to questions](../../README.md#budget-and-commercial-management)

**Level:** Middle · **Topic:** Budget and Commercial Management · **Reviewed:** 2026-10-30

## Answer

Planned Value (PV) is the budgeted value of scheduled work. Earned Value (EV) is the budgeted value of completed work using agreed earning rules. Actual Cost (AC) is the cost incurred.

![PV 100, EV 80, AC 90. CPI equals 0.89; SPI equals 0.80. Schedule variance is work value, not days.](../../assets/diagrams/earned-value.svg)

CPI = EV / AC; SPI = EV / PV. If PV = 100, EV = 80, and AC = 90, CPI is about 0.89 and SPI is 0.80. The project earned less value than planned and spent more than the value earned. EV is budgeted work value, not customer revenue. SPI is not a direct percentage of calendar delay; inspect the critical path and the quality of the baseline and earning rules.

## Extend the worked example

Treat the example amounts as thousands of currency units. Cost variance is EV − AC = −10; schedule variance is EV − PV = −20. Both are expressed in budgeted work-value units, not days.

If BAC is 200 and current cost efficiency is expected to persist, BAC / CPI gives an illustrative EAC of 225. Use that assumption only when justified. If the overrun was a one-off, a fresh remaining-work estimate may be more appropriate.

Choose objective earning rules, such as accepted milestones, before measuring progress. Traditional SPI approaches 1 when all planned work is complete even if the project finishes late. Calendar forecasts therefore still need schedule logic and actual completion dates.

## References

- [NSF: Earned Value Management Gold Card](https://www.nsf.gov/od/ori/evm-gold-card)
- [GAO: Schedule Assessment Guide](https://www.gao.gov/products/gao-16-89g)
