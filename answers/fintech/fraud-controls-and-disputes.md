# How would you deliver fraud controls and dispute handling without measuring success only by blocked transactions?

[Back to questions](../../README.md#fintech-domain)

**Level:** Middle · **Topic:** Fintech Domain · **Reviewed:** 2026-10-30

## Answer

Define the fraud problem, affected journeys, decision authority, and acceptable exposure. Fraud prevention, customer due diligence, sanctions controls, and AML monitoring can share information but do not have identical objectives.

## Plan the complete decision path

Agree which signals can allow, block, challenge, or refer an operation for review. Include the information reviewers need, access restrictions, staffing, escalation, and a way to correct mistakes. A new score is not a complete operational capability.

| Measure | Why it matters |
| --- | --- |
| Confirmed loss or relevant fraud outcomes | Whether material harm is changing |
| Legitimate-customer friction | False declines, abandonment, and support demand |
| Review workload and age | Whether operations can resolve referred cases |
| Dispute outcomes and cost | Whether evidence and follow-through work |
| Coverage and model/rule health | Where the control is ineffective or unobserved |

Define denominators and observation windows. Fraud labels and disputes can arrive well after a transaction, so an early approval-rate change alone is weak evidence of improved loss outcomes.

## Example

A stricter rule blocks more payments and sends many more cases to manual review. The dashboard looks safer, but legitimate customers cannot complete purchases and the review queue is growing. Assess outcomes, segmentation, review capacity, and the rule's actual mechanism with fraud and product owners before expanding it.

## Include disputes as a separate workflow

For card disputes, establish provider/network-specific reason codes, evidence requirements, response windows, notifications, and financial adjustments. A dispute, refund, and payment reversal can have different rules and accounting effects.

Use the actual provider contract and current procedures rather than a universal deadline. Assign operations and finance owners for unresolved cases. The PM coordinates integration, evidence, rollout, and handover; authorized fraud, risk, and business owners set the treatment policy.

## References

- [Stripe Radar: fraud evaluation and manual-review examples](https://docs.stripe.com/radar)
- [Stripe: card disputes and response workflow](https://docs.stripe.com/disputes)
- [FATF Recommendations: distinct due-diligence and monitoring context](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html)
