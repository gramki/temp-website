# Pricing Tier / Package

**Model:** Definition Model
**Dimension:** Dimension 2: The Vendor Value Dimension (Why It Wins)
**Owner:** Product Marketing, Executive Leadership

## Definition

A bundled commercial offering targeting a specific Customer Segment. A Package groups Features (Dim 8) into a marketable unit with associated pricing structured around Value Metrics. Pricing Tiers are the vendor's commercial packaging of the product — they define what the customer gets and what they pay.

## Purpose

Connects the vendor's business model to the product's functional reality by defining which Features are included in each commercial offering, at what price, for which segments. Without Pricing Tiers:
- There is no way to model feature gating ("Enterprise includes batch processing; Starter does not")
- The commercial relationship between product capabilities and revenue is implicit
- Win Barriers related to pricing competitiveness have nothing to challenge

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Market-facing tier name (e.g., "Enterprise Volume Plan") |
| Target Segment(s) | List of References (Dim 3) | Which Customer Segments this tier is designed for |
| Included Features | List of References (Dim 8) | Which Features are available in this tier |
| Add-on Features | List of References (Dim 8) | Optional features available at additional cost |
| Value Metric(s) | List of References (Dim 2) | Which pricing axes apply to this tier |
| Base Price | Text | Fixed/recurring component (e.g., "$5K/month platform fee") |
| Variable Pricing | Text | Usage-based component (e.g., "0.5% per transaction") |
| Contract Terms | Text | Typical commitment (e.g., "Annual, with quarterly billing") |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Draft | Tier is being designed (Deliberation or Modeling Task in progress) |
| Active | Tier is available for sale |
| Deprecated | Tier is no longer offered to new customers but existing customers are grandfathered |
| Retired | Tier is fully decommissioned — all customers migrated |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Business Model (Dim 2) | Pricing Tier operates within the Business Model |
| Targets | Customer Segment (Dim 3) | Pricing Tier is designed for specific segments |
| Contains | Feature (Dim 8) | Pricing Tier includes specific Features |
| Priced along | Value Metric (Dim 2) | Pricing Tier uses specific Value Metrics |
| Challenged by | Win Barrier (Dim 2) | Win Barriers may challenge the competitiveness of a Pricing Tier |
| Referenced by | PSD Section 2 (Dim 1) | PSDs reference pricing/packaging implications |

## Example

"Enterprise Volume Plan"
- Target Segments: LATAM Enterprise, US Enterprise
- Included Features: Cross-border payouts, batch processing, real-time FX rate locking, dedicated support, SFTP integration
- Add-on Features: Multi-currency reporting ($2K/month), Custom FX provider integration (one-time $50K)
- Value Metrics: Per-transaction fee (0.5%), FX markup (1%), Monthly platform fee ($5K)
- Contract Terms: Annual commitment, quarterly billing
- Status: Active
