# What makes acceptance criteria useful, and how do they differ from a Definition of Done?

[Back to questions](../../README.md#scope-and-requirements)

**Level:** Junior · **Topic:** Scope and Requirements · **Reviewed:** 2026-10-30

## Answer

Acceptance criteria describe observable behavior or conditions for a particular item. A Definition of Done establishes the quality state required of an Increment in Scrum. Specific criteria do not replace shared quality expectations.

For a refund, criteria might cover eligible payments, amount limits, duplicate submissions, permissions, and customer-visible status. The shared quality requirements may include reviewed changes, relevant tests, and appropriate security checks. Discuss examples before implementation and identify who can accept the business result. Avoid using “works correctly” as a criterion or treating unfinished testing as acceptable because a demonstration succeeded.

## Use concrete examples

For a refund item, discuss cases before coding:

| Case | Observable expectation |
| --- | --- |
| Authorized user refunds an eligible amount | One refund is created and status is visible |
| Same business operation is submitted twice | No duplicate financial effect |
| Amount exceeds refundable balance | Clear rejection; no movement |
| Provider result is uncertain | Pending or investigation state, with an owner |

These are illustrative criteria, not a complete payment specification. Add relevant shared quality checks through the Definition of Done.

In Scrum, an item that does not meet the DoD is not part of the Increment. A Sprint Review is not a mandatory release gate; a usable Increment may be delivered before it. Keep business or contractual acceptance rules explicit alongside Scrum's quality commitment.

## References

- [The Scrum Guide (2020)](https://scrumguides.org/scrum-guide.html)
