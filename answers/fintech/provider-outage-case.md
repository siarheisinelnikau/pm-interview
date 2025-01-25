# A payment provider times out after a customer confirms payment. How do you coordinate the response?

[Back to questions](../../README.md#fintech-domain)

**Level:** Senior · **Topic:** Fintech Domain · **Source review:** 2026-10-30

## Answer

Treat the financial outcome as uncertain until authoritative evidence establishes it. Coordinate engineering, operations, finance, support, and the provider. Avoid blindly retrying through the same or another provider because the original operation may already have succeeded.

Use the agreed incident process, preserve correlation evidence without exposing sensitive data, and assess affected transactions. Define customer messaging, status checks, idempotent recovery where supported, reconciliation, and ownership of exceptions. Consider controlled fallback only after financial and technical consequences are understood. Restore service and resolve uncertain money movements; a recovered API alone does not close the incident's business impact.

## References

- [Stripe: webhook handling (provider-specific example)](https://docs.stripe.com/webhooks)
- [Google SRE Workbook: Incident Response](https://sre.google/workbook/incident-response/)
