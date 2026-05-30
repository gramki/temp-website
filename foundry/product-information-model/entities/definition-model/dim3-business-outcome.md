# Business Outcome

**Model:** Definition Model
**Dimension:** Customer Value (Why Buy)
**Owner:** Product Marketing, Sales

## Definition

The macro-level benefit the purchasing organization (buyer) needs to achieve — the buyer's "job to be done" at a strategic level. Business Outcomes represent the high-level "Why Buy" justification that the Buying Persona (typically the Economic Buyer) uses to secure internal budget approval.

> **JTBD Mapping:** In Jobs-to-Be-Done terminology, Business Outcome represents the *buyer's job* — the strategic goal the budget-holder needs to accomplish. This is distinct from the *user's job* (captured as User Journey in User Experience). A buyer's job is "reduce FX costs by 40%"; the user's job is "process a cross-border payout without errors."

## Purpose

Connects the buyer's strategic needs to the product's Customer Promises. Business Outcomes are:
- The justification for the purchase (for the buyer)
- The anchoring point for Value Propositions (which explain how the product delivers these outcomes)
- The basis for ROI metrics (which measure whether the outcome was achieved)

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Short outcome description |
| Description | Text | Detailed description of what this outcome means for the buyer |
| Buying Persona | Reference (Customer Value) | Which buying persona (typically Economic Buyer) pursues this outcome |
| Customer Segment | Reference (Customer Value) | Which segment (inherited from buyer persona) |
| Quantifiable Target | Text | How the buyer would express success numerically |
| Buyer's Internal KPI | Text | How the purchasing organization measures this outcome internally — the metric the Economic Buyer reports to their board. Distinct from Customer Value Metric (Customer Value), which measures the *vendor's promise fulfillment*. The buyer's KPI is the buyer's own yardstick for whether the investment paid off. |
| Current Baseline | Text | The buyer's current state for this outcome — what they'd improve from. Establishes the "before" that makes the ROI case concrete. Often sourced from pre-sales discovery or sales qualification. |

## Statuses

| Status | Description |
|---|---|
| Draft | Outcome is being identified and validated |
| Active | Outcome is actively used in positioning and sales |
| Retired | Outcome is no longer relevant |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Buying Persona (Customer Value) | Buying Persona (Economic Buyer) pursues this Business Outcome |
| Downstream | Value Proposition (Customer Promise, Customer Value) | Business Outcome is addressed by Value Proposition(s) |
| Downstream | Customer Value Metric / ROI (Customer Value) | Business Outcome is measured by ROI Metrics |
| Work Model | Modeling Task (Discovery) | Modeling Tasks identify and validate Business Outcomes |

## Examples

| Business Outcome | Segment | Buyer | Quantifiable Target | Buyer's Internal KPI | Current Baseline |
|---|---|---|---|---|---|
| "Eliminate manual FX hedging and reduce cross-border wire fees" | LATAM Enterprise | CFO | Reduce per-transaction cost from $6.25 to <$2.50 | Cross-border payment cost as % of revenue (reported quarterly to board) | $6.25/transaction; 4 hours/day manual reconciliation; 3 FX systems |
| "Consolidate payment operations onto a single platform" | LATAM Enterprise | CTO | Reduce integration maintenance from 5 point-to-point connections to 1 API | IT operational cost per payment channel (annual budget line) | 5 separate vendor integrations; 2 FTE dedicated to payment maintenance |
| "Reduce time-to-pay for international suppliers" | US Mid-Market | AP Ops Manager | Reduce supplier payment cycle from 14 days to 2 days | Average days-to-pay (DPO) and supplier satisfaction score | 14-day average; 23% of suppliers on late payment penalty |
