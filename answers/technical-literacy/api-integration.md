# What questions should a PM ask before committing to an API integration?

[Back to questions](../../README.md#technical-literacy-for-pms)

**Level:** Middle · **Topic:** Technical Literacy for PMs · **Reviewed:** 2026-10-30

## Answer

Clarify the business journey, system owners, contract and version, authentication, limits, availability, and failure behavior. Confirm sandbox access, test data, certification, support, and the process for breaking changes.

Ask what happens on timeout, duplicate submission, partial success, or delayed notification. Establish who can verify the real business outcome. In payments, an HTTP response or callback alone may not settle the financial state. Schedule an early end-to-end integration test and track external prerequisites separately. A vendor's successful demonstration does not prove your environment, credentials, data mapping, and exception paths will work.

## Turn uncertainty into acceptance scenarios

Create a small contract checklist: valid request, invalid input, missing permission, rate limit, timeout, duplicate operation, and changed response. Confirm how correlation identifiers connect the client's request to the provider's record.

Include the operational contract: support hours, escalation, status lookup, version policy, and certificate or credential rotation. Test at least one representative journey early, then exercise failure cases.

An asynchronous acceptance response may mean work was queued, not completed. A transport timeout means the caller lacks a result; it does not prove the business action failed. Ask the technical owner how that uncertainty is resolved before using automatic retries or promising customer-visible recovery behavior.

## References

- [Stripe: webhook handling (provider-specific example)](https://docs.stripe.com/webhooks)
- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
