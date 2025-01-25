# How do you plan clinical workflow validation separately from ordinary UAT?

[Back to questions](../../README.md#healthcare-domain)

**Level:** Senior · **Topic:** Healthcare Domain · **Source review:** 2026-10-30

## Answer

Ask the clinical and quality owners which evidence is required for the function's intended use and risk. Distinguish usability and workflow testing from formal clinical evaluation or validation required for a regulated function. Do not treat one successful demonstration as proof of clinical safety or effectiveness.

Include realistic scenarios, patient matching, abnormal data, escalation, downtime, and staff responsibilities. Record acceptance authority, limitations, and unresolved hazards. For an alerting workflow, test what happens when the intended recipient is unavailable. The PM coordinates scope, participants, evidence, and remediation; qualified clinical and regulatory owners determine whether the evidence is sufficient.

## References

- [FDA: device software functions and mobile medical applications](https://www.fda.gov/medical-devices/digital-health-center-excellence/device-software-functions-including-mobile-medical-applications)
