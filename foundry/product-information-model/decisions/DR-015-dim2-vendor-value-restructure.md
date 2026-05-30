# DR-015: Restructure Vendor Value

**Status:** Accepted
**Date:** 2026-02-15

## Context

Vendor Value ("Business Value — Vendor Economics") was the thinnest dimension in the UPIM — 4 shell entities (Business Model, Pricing Tier, Value Metric, Business KPI) with `_To be refined._` fields, minimal relationships, and no cross-dimensional links. It modeled the product as a simple financial vehicle, ignoring the full complexity of how the vendor succeeds commercially.

A critical review identified several gaps:

1. **No vendor-side stakeholder modeling.** Customer Value has Buying Personas (4 role types) representing the customer's buying committee. Vendor Value had nothing analogous for the vendor's "winning committee" — the Pre-Sales Engineers, Implementation Consultants, CS Managers, Account Managers who make the product commercially successful.

2. **No structured definition of "what winning looks like."** Business KPIs existed but had no context — "CAC < $25K" is a number; without a Win Outcome ("close LATAM deals in 90-day cycle"), it's disconnected from the commercial story.

3. **No vendor-side pain modeling.** Customer Value has Pain (user suffering that motivates purchase). Vendor Value had nothing for vendor suffering — "implementation costs $80K per customer" or "POC takes 6 weeks" were invisible.

4. **No vendor-side barrier modeling.** Customer Value has Adoption Barrier (8 types). Vendor Value had no equivalent for structural impediments to vendor success — competitive, regulatory, financial, resource constraints.

5. **No AAARRR lifecycle coverage.** Revenue was the only stage modeled. Awareness, Acquisition, Activation, Retention, and Referral were absent — yet each has distinct stakeholders, outcomes, frictions, and KPIs.

6. **No cross-dimensional links.** Pricing Tiers had no link to Customer Segments (Customer Value). Business KPIs had no link to Objectives (Strategy). The dimension was isolated.

7. **Win Track disconnected.** The Win Track existed to drive "value realization" but had a weak structural connection to Vendor Value — Adoption Goals only tracked usage, not the full AAARRR lifecycle.

## Decisions

### 1. Rename to Vendor Value

Parallel to Customer Value ("Why Buy"). Emphasizes that Vendor Value models the complete vendor-side commercial success story, not just pricing mechanics.

### 2. Introduce Win Stakeholder entity

Functional archetypes in the vendor's AAARRR journey. Distinct from Operating Model roles — Vendor Value defines what roles the commercial model *requires*; Operating Model defines how teams are *staffed*. Engaged with Customer Segments; endures Delivery Frictions; responsible for Win Outcomes.

### 3. Introduce Win Outcome entity

Per-segment, per-AAARRR-stage definition of success. Structural and persistent (unlike time-bound Objectives). Referenced by Objectives and Initiatives (Strategy). Evidenced by Business KPIs. Operationalized by Adoption Goals (Win Track).

### 4. Introduce Delivery Friction entity

Vendor-side suffering — specific, concrete, discoverable. Endured by Win Stakeholders. Distinct from Pain (Customer Value): Pain is endured by User Persona, cared about by Buying Persona. Delivery Friction is endured by Win Stakeholder, suffered by the vendor. Surfaces as Signals in Strategy when observed in the field.

### 5. Introduce Win Barrier entity

Structural impediments to vendor success. 8 types: Competitive, Technical, Regulatory, Operational, Financial, Contractual, Resource, Market. Always articulated with aggrieved party (Win Stakeholder or vendor). Distinct from Adoption Barrier (Customer Value): customer's impediment vs. vendor's impediment.

### 6. Populate existing entities

Business Model: revenue streams, cost structure summary, target markets. Pricing Tier: target segments, included features, value metrics, contract terms, lifecycle statuses. Value Metric: unit, rate structure, scaling behavior. Business KPI: AAARRR stage, type (Revenue/Cost/Activity), target, threshold, cadence, owner.

### 7. Add cost KPIs

Business KPI now explicitly includes Cost type alongside Revenue and Activity. CAC, implementation cost, cost-to-serve, infrastructure cost per customer — critical for unit economics.

### 8. Scope all Vendor Value entities to Customer Segments

All Win entities are scoped directly or transitively to Customer Segments (Customer Value). Customer Segment is the shared anchor between Vendor Value and Customer Value.

### 9. Require PDR for all Vendor Value changes

All Vendor Value modifications follow governed paths: Deliberation → PDR → Modeling Task (for strategic design), or Signal → Discovery → PDR → Modeling Task (for field observations). Win Stakeholders are Signal sources and Deliberation participants, not entity authors.

### 10. Strengthen Strategy cross-references

Objective and Initiative now reference Win Outcomes as targets. Opportunity now references Delivery Friction and Win Barrier.

### 11. Strengthen Win Track connection

Win Track goal updated to reference AAARRR lifecycle. Adoption Goal now covers usage, revenue, and cost targets (not just usage). Feedback now explicitly surfaces Win Stakeholder observations as Signals. GTM Planning Task references Vendor Value entities.

## Rationale

- **Vendor Value ↔ Customer Value symmetry through Customer Segment:** The same segment modeled from two perspectives — customer's buying journey (Customer Value) and vendor's winning journey (Vendor Value)
- **AAARRR provides a proven lifecycle framework** that covers the full vendor journey, not just revenue
- **Enterprise B2B complexity justifies the depth:** Implementation is bespoke, sales cycles are long, multiple stakeholders engage from pre-sales to renewal. These are discoverable, not self-evident.
- **Win Stakeholder as functional archetype (not org role)** keeps Vendor Value in the Definition Model without overstepping into the Operating Model
- **PDR governance ensures commercial model stability** — pricing and KPI changes have real consequences

> **Subsequent evolution:** DR-016 restructured the Win Track and deprecated the Adoption Goal entity. Targets are now embedded in Initiatives (see DR-017). References to "Adoption Goal" in the decisions above reflect the model state at the time of this DR; see DR-016 and DR-017 for the current design.

## Consequences

### Positive
- Vendor Value is now fully specified — no remaining `_To be refined._` placeholders for core fields/statuses
- Complete traceability: Theme → Objective → Win Outcome → Business KPI → Adoption Goal
- Vendor-side journey is visible and queryable across all AAARRR stages
- Delivery Frictions and Win Barriers are first-class entities that drive Opportunity Signals
- Win Track has a strong structural anchor in Vendor Value
- Cost KPIs make unit economics visible to product planning

### Negative
- Vendor Value now has 8 entities (up from 4): +Win Stakeholder, +Win Outcome, +Delivery Friction, +Win Barrier
- Win Stakeholder may be confused with Operating Model roles — clear documentation and FAQ mitigate this
- PDR requirement for all Vendor Value changes adds governance overhead — justified by commercial impact
