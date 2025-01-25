# How would you plan for duplicate requests, asynchronous events, and financial reconciliation?

[Back to questions](../../README.md#fintech-domain)

**Level:** Senior · **Topic:** Fintech Domain · **Source review:** 2026-10-30

## Answer

Agree the financial invariants and authoritative records with engineering and finance. Examples include avoiding duplicate charges, preserving an auditable posting history, and identifying unmatched movements. Test timeout, retry, duplicate event, out-of-order event, and partial-failure scenarios.

Idempotency helps prevent repeating the same operation under a defined contract; it does not reconcile independent systems or create universal exactly-once processing. Plan internal deduplication, provider status checks, reconciliation, exception ownership, and controlled correction. Review currency precision and cut-off rules. A discrepancy needs investigation and a business-safe response, not an automated replay that could move money twice.

## References

- [Stripe: idempotent requests (provider-specific example)](https://docs.stripe.com/api/idempotent_requests)
- [Stripe: webhook handling (provider-specific example)](https://docs.stripe.com/webhooks)
