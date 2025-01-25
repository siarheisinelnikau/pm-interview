# What questions should a PM ask before committing to an API integration?

[Back to questions](../../README.md#technical-literacy-for-pms)

**Level:** Middle · **Topic:** Technical Literacy for PMs

## Answer

Clarify the business journey, system owners, contract and version, authentication, limits, availability, and failure behavior. Confirm sandbox access, test data, certification, support, and the process for breaking changes.

Ask what happens on timeout, duplicate submission, partial success, or delayed notification. Establish who can verify the real business outcome. In payments, an HTTP response or callback alone may not settle the financial state. Schedule an early end-to-end integration test and track external prerequisites separately. A vendor's successful demonstration does not prove your environment, credentials, data mapping, and exception paths will work.

## References

- [Stripe: webhook handling (provider-specific example)](https://docs.stripe.com/webhooks)
- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
