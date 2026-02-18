# Value Metric (Pricing Axis)

**Model:** Definition Model
**Dimension:** Dimension 2: The Vendor Value Dimension (Why It Wins)
**Owner:** Product Marketing, Executive Leadership

## Definition

The unit of measurement along which revenue scales — the pricing axis that ties product usage to revenue generation. A product may have multiple Value Metrics across different Pricing Tiers or within the same tier (e.g., per-transaction fee + monthly platform fee).

## Purpose

Defines the commercial mechanism that makes the Business Model concrete. Value Metrics answer "what exactly does the customer pay for?" The choice of Value Metric is a critical product decision — it determines whether revenue scales with customer value (aligning incentives) or independently of it (creating friction).

**Alignment with Customer Value Metric (Dim 3):** Ideally, the vendor's Value Metric aligns with the customer's Customer Value Metric — the vendor charges based on the value delivered. "Per-transaction fee" aligns with "transaction volume processed" (customer value). Misalignment (e.g., per-seat pricing for a product where value scales with data volume) creates commercial friction.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive name (e.g., "Per-transaction fee") |
| Unit | String | What is measured (e.g., "successful cross-border transaction", "API call", "user seat") |
| Rate Structure | Text | How the price is calculated (e.g., "0.5% of transaction value", "$0.01 per API call", "$50/seat/month") |
| Scaling Behavior | Text | How revenue scales with usage (linear, tiered/volume discounts, capped) |
| Used by Tier(s) | List of References (Dim 2) | Which Pricing Tiers use this Value Metric |
| _Other fields to be refined._ | | |

## Statuses

_Not applicable — Value Metric is a structural descriptor. Changes are rare and warrant PDRs (e.g., shifting from per-seat to per-transaction pricing is a major strategic decision)._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Business Model (Dim 2) | Value Metric is defined by the Business Model |
| Used by | Pricing Tier / Package (Dim 2) | Value Metric is used by Pricing Tiers |
| Aligns with | Customer Value Metric (Dim 3) | Value Metric should ideally align with Customer Value Metrics |

## Examples

| Value Metric | Unit | Rate Structure | Used by Tiers |
|---|---|---|---|
| Per-transaction fee | Successful cross-border transaction | 0.5% of transaction value | Enterprise Volume Plan, Mid-Market Plan |
| FX markup | FX conversion event | 1% on baseline exchange rate | Enterprise Volume Plan, Mid-Market Plan |
| Monthly platform fee | Monthly access | $5K/month (Enterprise), $500/month (Mid-Market) | Enterprise Volume Plan, Mid-Market Plan |
| Implementation services | One-time engagement | Custom scoping per customer | Enterprise Volume Plan (add-on) |
