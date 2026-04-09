# Business KPI

**Model:** Definition Model
**Dimension:** Dimension 2: The Vendor Value Dimension (Why It Wins)
**Owner:** Product Marketing, Executive Leadership, Finance

## Definition

A quantitative measure of the product's commercial health at a specific AAARRR stage. Business KPIs carry explicit targets, thresholds, measurement cadence, and ownership. They are typed as Revenue, Cost, or Activity metrics. The Definition Model captures metric *definitions and targets* — actual measured values are operational state tracked at runtime.

## Purpose

Analogous to Customer Value Metric (Dim 3), which measures whether the product keeps its promises to customers. Business KPI measures whether the product delivers on the vendor's commercial expectations. Without Business KPIs with teeth:
- Win Outcomes are aspirational statements without measurable evidence
- Opportunities (Dim 1) reference vague "business improvement" rather than specific KPI targets
- Initiative targets have no Dim 2 anchor to calibrate against

**AAARRR staging:** Each Business KPI is tagged to an AAARRR stage, making it possible to diagnose *where* in the vendor lifecycle the product is underperforming. "Revenue is down" is a symptom; "Acquisition CAC is 2x target while Activation rate is healthy" is a diagnosis.

**Cost KPIs:** Explicitly included alongside Revenue and Activity KPIs. Cost-to-serve, infrastructure cost per customer, implementation cost, and CAC are critical for unit economics and often invisible in product planning.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Metric name (e.g., "Customer Acquisition Cost") |
| AAARRR Stage | Enum | `Awareness` / `Acquisition` / `Activation` / `Retention` / `Revenue` / `Referral` |
| Type | Enum | `Revenue` / `Cost` / `Activity` |
| Customer Segment | Reference (Dim 3) | Which segment this KPI target applies to (may differ per segment) |
| Target | Text | The goal value (e.g., "< $25K", "95%", "$500K") |
| Threshold | Text | The minimum acceptable value / alert threshold (e.g., "$40K — above this, deal is unprofitable") |
| Measurement Cadence | Enum | `Daily` / `Weekly` / `Monthly` / `Quarterly` / `Annually` |
| Owner | String | Role/person accountable for this KPI |
| Win Outcome(s) evidenced | List of References (Dim 2) | Which Win Outcomes this KPI measures |
| _Other fields to be refined._ | | |

## Statuses

_Not applicable — Business KPI is a metric definition. Targets may be revised (via PDR + Modeling Task); the entity itself doesn't have a lifecycle._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Evidences | Win Outcome (Dim 2) | Business KPI measures whether Win Outcomes are achieved |
| Scoped to | Customer Segment (Dim 3) | KPI targets may differ per segment |
| Referenced by | Opportunity (Dim 1) | Opportunity Signals may target improvement of a Business KPI |
| Tracked by | Initiative (Dim 1) | Initiative embedded targets operationalize Business KPIs |
| Assessed by | Win Review (Track 4) | Win Reviews assess Business KPI progress |
| Context | Business Model (Dim 2) | Business Model determines which KPIs are relevant |

## KPI Types with Examples

### Revenue KPIs

| KPI | Stage | Segment | Target | Threshold |
|---|---|---|---|---|
| Annual Contract Value (ACV) | Acquisition | LATAM Enterprise | $500K | $300K |
| Monthly Recurring Revenue (MRR) | Revenue | All segments | $2M | $1.5M |
| Lifetime Value (LTV) | Revenue | LATAM Enterprise | $2M | $1M |
| Net Revenue Retention (NRR) | Revenue + Retention | LATAM Enterprise | 120% | 100% |
| Expansion Revenue | Revenue | US Enterprise | 30% of existing ARR | 15% |

### Cost KPIs

| KPI | Stage | Segment | Target | Threshold |
|---|---|---|---|---|
| Customer Acquisition Cost (CAC) | Acquisition | LATAM Enterprise | < $25K | $40K (unprofitable above) |
| Implementation Cost | Activation | LATAM Enterprise | < $30K | $80K |
| Cost-to-Serve (monthly) | Retention | US Mid-Market | < $500/month | $1K/month |
| Infrastructure Cost per Customer | Retention | All segments | < $200/month | $500/month |
| LTV:CAC Ratio | Acquisition + Revenue | LATAM Enterprise | > 5:1 | 3:1 |

### Activity KPIs

| KPI | Stage | Segment | Target | Threshold |
|---|---|---|---|---|
| Brand Awareness Score | Awareness | LATAM Enterprise | 80% unaided recall | 50% |
| Sales Cycle Length | Acquisition | LATAM Enterprise | < 90 days | 120 days |
| Time-to-First-Value | Activation | LATAM Enterprise | < 30 days | 60 days |
| Activation Rate | Activation | US Mid-Market | 85% | 60% |
| NPS | Retention | All segments | > 50 | 30 |
| Gross Retention Rate | Retention | LATAM Enterprise | 95% | 85% |
| Churn Rate | Retention | US Mid-Market | < 10% annually | 15% |
| Referral Pipeline Rate | Referral | LATAM Enterprise | 30% of new pipeline | 10% |
