# Product

**Model:** Definition Model
**Dimension:** Dimension 8: The Structural Dimension (Topology)
**Owner:** Product Management, Enterprise Architecture

## Definition

A complete, marketable software offering — the top-level entity in the structural taxonomy. A Product is composed of Modules and is the customer-facing unit of strategic scope.

## Purpose

Anchors the Structural Dimension as the root of the Product → Module → Capability → Feature hierarchy. Bridges Strategy/Business intent to Technical execution. A Product defines the entitlement boundary at the highest level; Pricing Tier (Dim 2) operates at the Module level within a Product.

## Fields

| Field | Type | Description |
|---|---|---|
| Product Code | String | Short unique identifier (e.g., CPG, MPORT) |
| Name | String | Full product name (e.g., "Core Payment Gateway") |
| Aliases | List | Known alternate names or branded names |
| Product Archetype | String | Go-to-market classification: Target Market (B2B/B2C/B2B2C) × Delivery Model (SaaS/PaaS/On-Premise) × GTM Strategy (PLG/SLG) — e.g., "B2B + SaaS + SLG" |
| Target Market | Text | Primary customer segments and geographies |
| Tenancy Model | Enum | `Single-Tenant` / `Multi-Tenant`. Constraint: a Multi-Tenant Product requires all Modules to be Multi-Tenant. |
| Lifecycle Status | Enum | See Statuses below |
| Owner | Reference (WFR) | Product Manager / Product Owner responsible for this Product |

## Statuses

| Status | Description |
|---|---|
| Incubating | Product is in early formation — not yet available to customers |
| Preview (Beta) | Product is available to a limited set of customers for validation |
| GA | Product is generally available — full customer access and support |
| Maintenance | Product is no longer actively extended; only critical fixes shipped |
| End-of-Life | Product is retired — no new customers; existing customers migrated |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Belongs to | Portfolio (Dim 1) | Product belongs to a Portfolio |
| Contains | Module (Dim 8) | Product contains one or more Modules |
| Expresses | Value Stream(s) (Dim 8) | Product expresses Value Streams — horizontal flows across Modules |
| Referenced by | Product Decision Record (Dim 1) | PDRs specify strategic decisions affecting this Product |
| Referenced by | Product Specification Document (Dim 1) | PSDs specify changes to Modules within this Product |
| Delivered as | Product Version (Track 2) | Build Track produces versioned, certified Product Versions |
| Made available as | Customer Release (Dim 1) | Customer Releases bundle Product capability delivery |
| Technical twin | Product Specification (Dim 5) | Declares which Systems compose the product (product-facing and operational alike) |

## Example

"Core Payment Gateway" — B2B + SaaS + SLG. Status: GA. Tenancy Model: Multi-Tenant. Owner: PM-Payments. Modules: Payments Module (Record), FX Module (Intelligence), Compliance Module (Enforcement), Settlement Module (Record), Customer Portal Module (Engagement).
