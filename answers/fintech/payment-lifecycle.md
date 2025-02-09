# How do authorization, capture, settlement, refunds, and disputes affect delivery planning?

[Back to questions](../../README.md#fintech-domain)

**Level:** Middle · **Topic:** Fintech Domain · **Reviewed:** 2026-10-30

## Answer

Use a **provider- and payment-rail-specific state model**. For a card example, authorization, capture, settlement, and payout describe different events. A single “paid” flag can conceal important uncertainty.

![A card payment has several distinct states. Refunds, reversals, disputes, and fees add separate events. Checkout success, authorization, settlement, and payout are not interchangeable.](../../assets/diagrams/payment-lifecycle.svg)

## Follow the money and the evidence

| Stage | Meaning in the simplified card example | Planning consequence |
| --- | --- | --- |
| Authorization | Issuer approves or reserves the amount | Expiry and release behavior matter |
| Capture | Merchant requests collection of an authorized amount | Full/partial capture and retries need agreed rules |
| Clearing and settlement | Transaction information and funds are processed between participants | Timing and reconciliation differ from checkout |
| Payout | Provider transfers available balance to the merchant's bank | Fees, reserves, and payout timing affect operations |

A provider may combine or automate stages. Its object names and state transitions are not a universal financial model. Refunds, disputes, reversals, and failed payouts introduce further events; they are not simply deletion of the original payment.

## Example: a 100-unit purchase

The customer can see an authorization while the merchant has not captured funds. After capture, a provider balance movement may be 100 gross minus fees, while the bank payout includes many payments and adjustments. Comparing each order directly to one bank deposit will not reconcile correctly.

Agree which record is authoritative for each question: customer order state, provider processing state, internal accounting, and bank movement. Keep correlation between them.

## What the PM should plan

Include expiration, partial capture, authentication where relevant, asynchronous results, refunds, disputes, currencies, cut-off times, fees, and support workflows in estimates and acceptance. Test unavailable providers, delayed events, and uncertain outcomes as well as the successful path.

Establish who investigates each mismatch and how customers see pending states. Define completion for both the user journey and financial operations. An HTTP success, a browser redirect, or an authorization alone does not prove final settlement.

The diagram is an illustrative card flow, not a claim that all rails or providers implement the same sequence.

## References

- [Stripe: separate authorization and capture, provider-specific example](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [Stripe: payment lifecycle and asynchronous processing example](https://docs.stripe.com/payments/payment-intents)
- [Stripe: balance reporting and reconciliation](https://docs.stripe.com/reports/balance)
