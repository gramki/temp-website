# Business Outcome

**Model:** Definition Model
**Dimension:** Dimension 3: The Customer Value Dimension (Why Buy)
**Owner:** Product Marketing, Sales

## Definition

The macro-level benefit the purchasing organization (buyer) needs to achieve — the buyer's "job to be done" at a strategic level. Business Outcomes represent the high-level "Why Buy" justification that the Buying Persona (typically the Economic Buyer) uses to secure internal budget approval.

> **JTBD Mapping:** In Jobs-to-Be-Done terminology, Business Outcome represents the *buyer's job* — the strategic goal the budget-holder needs to accomplish. This is distinct from the *user's job* (captured as User Journey in Dim 4). A buyer's job is "reduce FX costs by 40%"; the user's job is "process a cross-border payout without errors."

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
| Buying Persona | Reference (Dim 3) | Which buying persona (typically Economic Buyer) pursues this outcome |
| Customer Segment | Reference (Dim 3) | Which segment (inherited from buyer persona) |
| Quantifiable Target | Text | How the buyer would express success numerically |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Draft | Outcome is being identified and validated |
| Active | Outcome is actively used in positioning and sales |
| Retired | Outcome is no longer relevant |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Buying Persona (Dim 3) | Buying Persona (Economic Buyer) pursues this Business Outcome |
| Downstream | Value Proposition (Customer Promise, Dim 3) | Business Outcome is addressed by Value Proposition(s) |
| Downstream | Customer Value Metric / ROI (Dim 3) | Business Outcome is measured by ROI Metrics |
| Work Model | Modeling Task (Track 1) | Modeling Tasks identify and validate Business Outcomes |

## Example

"Eliminate manual FX hedging and reduce cross-border wire fees" — pursued by CFO at LATAM Enterprise, quantifiable target: "reduce per-transaction cost from $6.25 to <$2.50."
