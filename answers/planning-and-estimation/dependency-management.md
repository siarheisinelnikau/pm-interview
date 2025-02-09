# How would you manage dependencies across teams, vendors, and a client?

[Back to questions](../../README.md#planning-and-estimation)

**Level:** Middle · **Topic:** Planning and Estimation · **Reviewed:** 2026-10-30

## Answer

Record what is needed, from whom, by when, with acceptance conditions and a fallback. Map the dependency to the milestone it can affect. Give each side an owner and establish escalation before the deadline is missed.

For a provider integration, track contract approval, credentials, test data, certification slots, and production access separately. An API specification alone does not mean integration is ready. Review the most time-sensitive dependencies frequently and seek early evidence, such as a working test transaction. Escalate the decision or resource needed, with impact and alternatives, rather than only reporting that another team is late.

## Track the last responsible decision

A dependency entry needs both a required-by date and the latest date at which a fallback remains feasible. If certification is needed on day 20 and an alternative takes eight days, waiting until day 20 to escalate may eliminate the alternative.

For a provider sandbox, define ready as credentials issued, representative roles enabled, test data loaded, and one successful verification request. Separate those conditions when different owners control them.

Use dependency reviews to obtain evidence or decisions, not to recite a list. If another team cannot commit, reflect that uncertainty in the forecast and take a prioritization decision to the person who owns both demands.

## References

- [GovS 002 v2.1: section 7.2: planning and estimating](https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/)
