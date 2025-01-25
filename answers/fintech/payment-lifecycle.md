# How do authorization, capture, settlement, refunds, and disputes affect delivery planning?

[Back to questions](../../README.md#fintech-domain)

**Level:** Middle · **Topic:** Fintech Domain · **Source review:** 2026-10-30

## Answer

For a card-payment example, authorization approves or reserves an amount, capture initiates collection, and settlement concerns movement and accounting of funds. Refunds and disputes are separate later flows with their own states and timing. Other payment rails differ.

Agree the provider's actual state model, time windows, fees, currencies, and exception behavior. Design acceptance scenarios for partial capture, expired authorization, delayed events, refunds, and disputes. Define what the user sees when the state is pending or uncertain. A successful checkout response does not prove settlement; plan operational reconciliation and support as part of the delivery boundary.

## References

- [Stripe: Payment Intents (provider-specific example)](https://docs.stripe.com/payments/payment-intents)
