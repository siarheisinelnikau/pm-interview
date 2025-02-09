# How do you plan clinical workflow validation separately from ordinary UAT?

[Back to questions](../../README.md#healthcare-domain)

**Level:** Senior · **Topic:** Healthcare Domain · **Reviewed:** 2026-10-30

## Answer

Separate **technical verification, clinical evaluation, and safe use in the deployed workflow**. User Acceptance Testing can inform the third, but does not establish all three.

![Clinical evaluation asks three different evidence questions. Workflow safety also depends on identity, handoffs, people, downtime, and response. UAT alone does not establish all clinical evidence.](../../assets/diagrams/clinical-evaluation.svg)

## Ask which evidence question is being answered

For SaMD, IMDRF N41 describes a clinical-evaluation framework with three related questions:

| Evidence area | Question |
| --- | --- |
| Valid clinical association | Is the relationship between the output and the clinical condition scientifically supported? |
| Analytical or technical validation | Does the software correctly and reliably generate the intended output from its inputs? |
| Clinical validation | Does the output achieve its intended clinical purpose for the intended population and use? |

The evidence strategy depends on intended use, risk, existing evidence, and the applicable framework. It does not imply that every software change requires the same study or a new clinical trial.

## Add the real workflow

Consider a result-alerting function. A correct calculation can still fail in use if the message reaches an unstaffed inbox, the result lacks context, or the escalation path is unclear. Test patient matching, missing or amended inputs, abnormal conditions, unavailable recipients, downtime, and recovery.

For clinical performance, specialists should define relevant measures and acceptance bounds. Sensitivity, specificity, false-positive burden, subgroup behavior, and reference-standard quality can matter; the appropriate choices depend on the clinical claim. A single aggregate accuracy percentage can hide an important failure mode.

## Plan ownership and change

The PM organizes clinical participation, test populations or data access, protocol and evidence dependencies, findings, and decision dates. Clinical, quality, and regulatory owners determine adequacy. Record the software version, intended population, limitations, and unresolved hazards associated with acceptance.

After a material change to an algorithm, data mapping, population, or workflow, assess which earlier evidence remains valid. Clinical evaluation is not automatically completed forever by a one-time UAT signature.

For health IT in the relevant NHS England setting, DCB0129 and DCB0160 provide separate manufacture and deployment/use clinical-risk requirements. Apply their actual scope rather than treating them as global medical-device rules.

## References

- [IMDRF N41FINAL:2017: SaMD clinical evaluation](https://www.imdrf.org/documents/software-medical-device-samd-clinical-evaluation)
- [IMDRF N41: full clinical-evaluation document](https://www.imdrf.org/sites/default/files/docs/imdrf/final/technical/imdrf-tech-170921-samd-n41-clinical-evaluation_1.pdf)
- [NHS England: clinical risk management standards](https://digital.nhs.uk/services/clinical-safety/clinical-risk-management-standards)
