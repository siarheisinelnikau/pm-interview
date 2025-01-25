# What do DORA software delivery metrics measure, and how should a PM use them?

[Back to questions](../../README.md#metrics-and-continuous-improvement)

**Level:** Middle · **Topic:** Metrics and Continuous Improvement

## Answer

DORA's current guide describes five metrics: change lead time, deployment frequency, failed deployment recovery time, change fail rate, and deployment rework rate. The recovery measure concerns failed deployments; it is not a generic recovery clock for every incident.

Use the measures at an application or service boundary with engineering and operations. Inspect trends and bottlenecks alongside reliability and user outcomes. Avoid ranking individuals or comparing unlike services. A deployment is not necessarily a customer-visible release. Specify the definitions and observation window, and revisit the guide when using historical four-metric terminology. This DORA research is distinct from the EU DORA regulation.

## References

- [DORA: software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
