# Customer Segment

**Model:** Definition Model
**Dimension:** Dimension 3: The Customer Value Dimension (Why Buy)
**Owner:** Product Management, Product Marketing

## Definition

A defined group of potential buyers sharing common characteristics — industry vertical, company size, geography, maturity stage. Segments have distinct buyer personas, outcomes, promise expectations, and adoption patterns. All other Dim 3 entities are anchored to one or more Customer Segments.

## Purpose

Customer Segment is the organizing entity for the entire Customer Value Dimension. Without it, buyer personas are unanchored ("CFO" is too generic), business outcomes can't be differentiated by market, and Customer Promises can't be tailored. Segments also connect to Pricing Tiers (Dim 2), enabling segment-specific packaging and pricing.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive segment name (e.g., "LATAM Enterprise") |
| Industry Vertical | String | Target industry or industries |
| Company Size | Range | Employee count or revenue range |
| Geography | String | Target geography or region |
| Maturity Stage | Enum | Startup / Growth / Enterprise / Regulated |
| Key Characteristics | Text | Defining traits that distinguish this segment |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Draft | Segment is being defined |
| Active | Segment is actively targeted |
| Deprioritized | Segment is known but not currently targeted |
| Retired | Segment is no longer relevant |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Downstream | Buying Persona (Dim 3) | Segment has Buying Persona(s) |
| Downstream | Pain (Dim 3) | Segment has Pain(s) |
| Downstream | Customer Promise (Dim 3) | Segment is promised Customer Promise(s) |
| Downstream | Adoption Barrier (Dim 3) | Segment is blocked by Adoption Barrier(s) |
| Cross-dim | Pricing Tier / Package (Dim 2) | Segment may map to Pricing Tier(s) |
| Work Model | Modeling Task (Track 1) | Modeling Tasks define/refine Segments |

## Example

"LATAM Enterprise (500+ employees, cross-border payables)" — CFO buyer, outcomes focused on FX cost reduction and regulatory compliance, barriers include data residency requirements.
