# Feature

**Model:** Definition Model
**Dimension:** Structural
**Owner:** Enterprise Architects, Product Management

## Definition

A granular, distinct tool or behavior — the most specific functional unit in the structural taxonomy. The leaf node of the Product → Module → Capability → Feature hierarchy.

## Purpose

Features represent individual product behaviors that users or consuming systems can act on directly. Features are what PSDs specify at the finest grain and what Engineering implements in Stories. Entitlement (Pricing Tier) operates at the Module level, not the Feature level — features are too granular for commercial packaging at this stage (D7).

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Feature name (e.g., "Real-time FX auto-conversion lock," "One-click OFAC re-screen") |
| Description | Text | What behavior this Feature provides — 1–2 sentences |
| Capability | Reference (Structural) | The Capability this Feature belongs to |
| Maturity Stage | Enum | `Alpha` (experimental, not for production use) / `Beta` (limited availability) / `GA` (generally available, stable) — inherited from or consistent with parent Capability Maturity |

## Statuses

| Status | Description |
|---|---|
| Planned | Feature is specified but not yet built |
| Available | Feature is built and available to customers |
| Deprecated | Feature is being phased out; replacement or alternative exists |
| Retired | Feature has been removed from the product |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Capability (Structural) | Feature belongs to a Capability |
| Specified in | Product Specification Document (Strategy) | PSDs add, modify, or retire this Feature |
| Implemented by | Story (Build) | Build Track Stories implement Features |

> **Note:** Features are NOT directly linked to Pricing Tiers. Entitlement is managed at the Module level (D7). This may evolve in future.

## Example

- "Real-time FX auto-conversion lock" — Capability: Real-Time FX Rate Lock, Maturity Stage: GA, Status: Available
- "Rate lock expiry SMS notification" — Capability: Real-Time FX Rate Lock, Maturity Stage: Beta, Status: Available
- "Bulk OFAC re-screen trigger" — Capability: OFAC Sanctions Screening, Maturity Stage: Alpha, Status: Available
