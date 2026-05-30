# Customer Value Metric

**Model:** Definition Model
**Dimension:** Customer Value (Why Buy)
**Owner:** Product Management, Customer Success

## Definition

A measurable indicator that evidences whether a Customer Promise is being kept. A unified metric entity with subtypes corresponding to promise types. All subtypes share a common structure (target, actual, measurement method, frequency) but measure different things.

## Purpose

Customer Value Metrics provide the concrete, quantifiable evidence for Customer Promises. They replace the earlier "ROI Metric" entity (which only measured Business Outcomes) with a broader concept that spans all promise types — financial return, service levels, and compliance adherence. This enables a complete view: "Show me all Customer Value Metrics for Segment X" returns financial, operational, and compliance evidence in one query.

Different Value Proposition mapping types produce different metric profiles:
- **Value Stream-mapped** promises → measured by **end-to-end flow metrics** (cycle time, throughput, cost per flow)
- **Capability-mapped** promises → measured by **point metrics** (feature performance, coverage, availability)

## Subtypes

### ROI Metric (subtype)

Measures Value Proposition claims — the financial or time-based return the customer receives.

*Value Stream-mapped examples:*
- End-to-end cycle time: "Cross-border payout processed in <4 hours"
- Throughput: "Process 500+ payouts per batch"
- Cost reduction: "60% reduction in per-transaction cost"
- Error rate: "<0.1% failed payouts end-to-end"

*Capability-mapped examples:*
- Feature performance: "FX rate locked within 200ms"
- Coverage: "35+ supported currencies"
- Availability of specific capability: "Rate locking available 24/7"

### Service Level Metric (subtype)

Measures Service Commitment guarantees.

*Examples:*
- Actual uptime vs. SLA: "99.95% actual vs. 99.9% committed"
- P95 latency: "180ms actual vs. 200ms committed"
- Incident response time: "12-minute average SEV-1 response vs. 15-minute SLA"
- Mean time to resolution: "3.2 hours average SEV-1 MTTR vs. 4-hour SLA"

### Compliance Metric (subtype)

Measures Compliance Posture adherence.

*Examples:*
- Audit result: "PCI-DSS Level 1 audit passed — zero findings"
- Certification validity: "SOC 2 Type II valid through 2027-03-15"
- Vulnerability remediation: "Average critical vulnerability remediation: 18 hours (target: <48 hours)"
- Compliance incident count: "Zero compliance incidents in trailing 12 months"

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | What's being measured |
| Subtype | Enum | `ROI` / `Service Level` / `Compliance` |
| Target | String | The promised or aspirational value (e.g., "99.9% uptime", "<4 hours cycle time") |
| SLA Threshold | String | The contractual minimum before breach consequences (e.g., "99.5% before credits apply"). May not apply to all metric subtypes. |
| Measurement Method | Text | How it's measured (financial analysis, monitoring, audit) |
| Frequency | Enum | Real-time / Daily / Weekly / Monthly / Quarterly / Annually |
| Measures | Reference (Customer Value) | Which Customer Promise this metric evidences |
| _Other fields to be refined._ | | |

> **Note:** The Definition Model captures metric *definitions and targets* — what we promise and the threshold at which we breach. Actual measured values are operational state tracked in runtime systems and Win activities, not part of the product's self-description.

## Statuses

_Not applicable — metrics are continuously measured. Metric definitions may be `Active` or `Retired`._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Customer Promise (Customer Value) | Customer Value Metric evidences a Customer Promise |
| Fed by | Incident (Track 3, artifact) | Incident response/resolution times feed Service Level Metric actuals (e.g., "SEV-1 incident MTTR: 3.2 hours vs. 4-hour SLA") |
| Work Model | Modeling Task (Discovery) | Modeling Tasks define metric targets and measurement methods |

## Example

For Customer Segment "LATAM Enterprise," Value Proposition "Reduce cross-border payment cost by 60%":
- ROI Metric (VS-mapped): "End-to-end payout cycle time: target <4 hours, SLA threshold: <8 hours"
- ROI Metric (VS-mapped): "Per-transaction cost: target $2.50, SLA threshold: <$4.00"
- Service Level Metric: "API uptime: target 99.9%, SLA threshold: 99.5% (credits apply below)"
- Compliance Metric: "PCI-DSS audit: target pass with zero findings, SLA threshold: pass (any findings trigger remediation plan)"
