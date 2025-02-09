# How would you handle PSD2/SCA and EU DORA requirements without assuming every fintech has the same obligations?

[Back to questions](../../README.md#fintech-domain)

**Level:** Middle · **Topic:** Fintech Domain · **Reviewed:** 2026-10-30

## Answer

Establish **which entity performs which regulated activity, in which market, and under which obligations**. A software supplier, merchant, payment institution, and bank can have different duties even when they use the same application.

## Keep the frameworks separate

| Framework or topic | What to investigate |
| --- | --- |
| PSD2 and SCA | Applicable payment-service and authentication requirements, exemptions, and technical standards |
| PSD3/PSR transition | Legislative status, entry into force, application dates, and national implementation where relevant |
| EU DORA | ICT risk management, incident handling/reporting, resilience testing, and third-party arrangements within its scope |
| Local and contractual rules | Licensing, privacy, outsourcing, payment-scheme and client obligations |

EU DORA has applied since **January 17, 2025** to entities within its scope. A technology supplier can also have relevant contractual duties or a specific oversight position; do not assume every supplier is directly regulated in the same way as a financial entity.

Political agreement, formal adoption, publication, entry into force, and application are distinct milestones. For a real launch, establish the currently applicable PSD2/PSD3/PSR position from the current official texts. Do not replace an existing applicable requirement merely because a newer package has been announced.

## Make an applicability matrix

Record obligation, jurisdiction, entity/activity, source/version, effective date, interpretation owner, implementation item, evidence, and ongoing owner. Resolve unclear scope before turning it into a dated commitment.

For an authentication change, ask compliance and engineering which journeys, exemptions, fallbacks, evidence, and customer communications apply. For DORA-related work, coordinate operations and vendor management as well as software changes.

## Example

A supplier building a bank's onboarding platform may need to provide incident information, control evidence, and contractual cooperation even though the bank retains its own regulatory responsibilities. A signed supplier contract does not transfer those responsibilities wholesale.

The PM tracks decisions and evidence; compliance/legal owners determine applicability. **DORA software delivery research** is a separate measurement framework and provides no EU DORA compliance status.

## References

- [European Commission: payment services and official reform links](https://finance.ec.europa.eu/consumer-finance-and-payments/payment-services/payment-services_en)
- [ESMA: DORA, application, scope, and technical standards](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/digital-operational-resilience-act-dora)
- [DORA research: software delivery metrics, a different use of the acronym](https://dora.dev/guides/dora-metrics/)
