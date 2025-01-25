# How should PCI DSS scope influence a payment project?

[Back to questions](../../README.md#fintech-domain)

**Level:** Middle · **Topic:** Fintech Domain · **Source review:** 2026-10-30

## Answer

Map where cardholder data and sensitive authentication data are stored, processed, or transmitted, and which systems can affect that environment. Confirm assessment scope and obligations with the organization's PCI owner and appropriate assessor.

Hosted payment components or tokenization can reduce exposure, but outsourcing does not automatically remove all responsibilities. Include logs, analytics, support tools, access, and supplier interfaces in the assessment. Plan evidence and assessment time using the applicable PCI DSS version and validation route. Avoid a blanket promise that a provider integration makes the product “PCI compliant” without examining the actual data flow and integration.

## References

- [PCI SSC: PCI DSS](https://www.pcisecuritystandards.org/standards/pci-dss/)
