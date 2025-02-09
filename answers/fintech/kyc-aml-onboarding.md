# What should a PM include in KYC and AML onboarding scope?

[Back to questions](../../README.md#fintech-domain)

**Level:** Middle · **Topic:** Fintech Domain · **Reviewed:** 2026-10-30

## Answer

Begin with **the legal entity, jurisdictions, customer types, products, and assessed risk**. Customer identification, due diligence, sanctions screening, fraud controls, and ongoing monitoring are related but distinct processes.

FATF Recommendations are an international standard implemented through jurisdiction-specific arrangements, not directly one identical law for every fintech. The checked consolidated publication is amended **June 2026**. Use applicable local rules and institutional policy with compliance.

## Plan more than the vendor check

| Area | Scope to clarify |
| --- | --- |
| Identity and due diligence | Required evidence, verification, beneficial ownership where relevant |
| Risk assessment | Customer/product/geography factors and appropriate treatment |
| Screening | Relevant lists, matching rules, investigations, and decision authority |
| Operations | Review queues, escalation, quality control, and capacity |
| Ongoing obligations | Refresh, changed circumstances, monitoring, records, reporting where required |

A provider returning “pass” is one input. Establish who makes the onboarding decision and how uncertain, conflicting, or incomplete evidence is handled. Avoid forcing every case into a binary automated result.

## Example: conversion improves, but the queue grows

A new onboarding flow sends more cases to manual review. Apparent completion improves at the front end while customers wait days for activation and investigators accumulate unresolved cases.

Model expected arrival volume and handling effort with operations. Trial representative case mixes, inspect false positives and false negatives with specialists, and monitor queue age and decision quality alongside conversion. Do not weaken essential controls simply to remove a delivery bottleneck.

## Acceptance and authority

Test approved, rejected, inconclusive, duplicate, expired-document, provider-outage, and changed-customer scenarios. Confirm access restrictions, audit evidence, retention, and permitted disclosure. Include procedures for suspicious-activity handling and reporting where applicable; do not invent a universal deadline or customer communication rule.

The PM ensures scope, capacity, and evidence are planned. Compliance and authorized business owners define policy and make relevant decisions. A launch-ready UI is incomplete if no operating process can safely handle the resulting cases.

## References

- [FATF: consolidated Recommendations, amended June 2026](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html)
- [GovS 002 v2.1: capacity, risk, and transition practices](https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/)
