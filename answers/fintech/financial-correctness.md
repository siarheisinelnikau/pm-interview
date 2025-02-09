# How would you plan for duplicate requests, asynchronous events, and financial reconciliation?

[Back to questions](../../README.md#fintech-domain)

**Level:** Senior · **Topic:** Fintech Domain · **Reviewed:** 2026-10-30

## Answer

Agree **financial invariants and authoritative records before designing recovery**. Idempotency, event deduplication, transactional recording, and reconciliation solve different parts of the problem.

![Reconciliation compares independent records. Example: 100 gross minus 3 fee gives 97 net. A mismatch needs an owner and controlled resolution; replaying every record can move money twice.](../../assets/diagrams/reconciliation.svg)

## Separate the controls

| Control | What it helps establish | What it does not establish alone |
| --- | --- | --- |
| Idempotent operation | A retry under the same defined contract avoids duplicate effect | One global exactly-once process across providers |
| Event deduplication | A repeated notification does not repeat a business action | Correct order or completeness of all events |
| Controlled accounting record | Financial state changes are recorded under agreed rules | Agreement with the provider or bank |
| Reconciliation | Differences between independent records are detected and resolved | Automatic correctness of every proposed correction |

Define amount and currency representation, rounding, fees, capture/refund limits, immutable audit history or controlled correction, and who owns exceptions. Engineers and finance determine the actual model and invariants.

## Example: timeout after capture

The provider captures 100, but the response is lost. A blind new request with a new operation identifier may charge again. Preserve the original business operation and provider correlation, establish status, and follow the provider's documented retry contract.

Idempotency keys have scope, retention, and parameter rules. Confirm those for the actual API rather than assuming a key works forever or across providers. Webhooks can be duplicated or delivered out of order; verify authenticity and process business transitions safely.

## Reconcile at the right boundaries

Compare internal records with provider events and balance movements, then reconcile applicable payouts to bank evidence. In an illustrative 100 gross payment with a 3-unit fee, a 97 net movement is not automatically a missing 3-unit payment.

Test partial failure, delayed settlement, duplicate events, partial refunds, amended records, and recovery after interruption. Track unmatched items, their age and value, investigation ownership, and resolution evidence.

The PM coordinates these scenarios, operational capacity, and acceptance. A lower mismatch count is useful only if exceptions were actually understood and resolved rather than hidden or written off without authority.

## References

- [Stripe: idempotent requests and contract boundary](https://docs.stripe.com/api/idempotent_requests)
- [Stripe: duplicate events, event ordering, and signature verification](https://docs.stripe.com/webhooks)
- [Stripe: balance summary and reconciliation](https://docs.stripe.com/reports/balance)
- [Stripe: advanced error handling and uncertain outcomes](https://docs.stripe.com/error-low-level)
