# How would you plan a data migration and decide whether cutover is safe?

[Back to questions](../../README.md#technical-literacy-for-pms)

**Level:** Senior · **Topic:** Technical Literacy for PMs

## Answer

Define data scope, mapping, ownership, quality checks, reconciliation, access controls, and the permitted service interruption. Rehearse with representative data and record runtime, exceptions, and recovery evidence. Agree a freeze or delta-sync approach when source data continues changing.

Set go/no-go conditions and a last safe decision point. Check whether rollback can preserve writes made after cutover; restoring old code may not restore consistent data. Include operational staffing, user communications, and exception handling. For a patient or financial record migration, unresolved identity or balance discrepancies require an explicit decision by the accountable business and risk owners.

## References

- [UK Government: Project Delivery Functional Standard](https://www.gov.uk/government/publications/project-delivery-functional-standard)
- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
