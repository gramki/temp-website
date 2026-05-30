# Strategic Theme

**Model:** Definition Model
**Dimension:** Strategy
**Owner:** Executive Leadership (Portfolio scope); Product Management (Product scope)

## Definition

A persistent, cross-cutting strategic direction that organizes and informs discovery, customer value positioning, and investment allocation across planning horizons. A Strategic Theme represents a sustained commitment — "we are investing in X" — that persists longer than any single Objective and provides continuity across planning cycles.

## Purpose

Objectives are time-bound ("achieve Y by H2 2026") and product-scoped. Strategic Themes provide the *why behind the why* — the persistent strategic direction that generates Objectives over multiple horizons. Without Themes:
- Strategic continuity across planning horizons is implicit (you must read a sequence of Objectives and infer the pattern)
- Resource allocation across strategic directions is invisible ("how much of our capacity goes to LATAM vs. Developer Experience?")
- Cross-product coordination has no shared language (multiple products investing in "LATAM" can't be queried)

**Scope: Portfolio vs. Product**

| Scope | Meaning | Example |
|---|---|---|
| **Portfolio** | Declared at portfolio level, adopted by multiple products. Originates outside the UPIM. | "LATAM Market Leadership" — all products in the Payments Portfolio contribute |
| **Product** | Originated by this product's team. May be elevated to Portfolio scope if adopted across products. | "Payment Adapter Consolidation" — initially a Payment Gateway optimization theme |

Portfolio-scoped Themes reference the thin Portfolio entity for traceability. Product-scoped Themes are fully owned by this UPIM instance.

**Cross-cutting influence:**

| Dimension | How Theme informs |
|---|---|
| Strategy (Strategy) | Which Objectives to pursue, which Initiatives to scope |
| Customer Value (Customer Value) | Which Customer Segments to focus on, which Value Propositions to craft, which Pains to prioritize |
| Structural (Structure) | Which Value Streams and Capabilities to invest in |
| Work Model (Discovery) | How to allocate discovery capacity across Signal Exploration |

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive theme name (e.g., "LATAM Market Leadership") |
| Scope | Enum | `Portfolio` / `Product` |
| Portfolio | Reference (Strategy) | For Portfolio scope: reference to the Portfolio entity. For Product scope: null. |
| Description | Text | What this theme means and why it matters |
| Investment Guidance | Text | Approximate resource allocation intent (e.g., "40% of discovery capacity in H2 2026") |
| Influenced Segments | List of References (Customer Value) | Which Customer Segments this theme focuses on |
| Influenced Capabilities / Value Streams | List of References (Structural) | Which structural elements this theme drives investment in |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Proposed | Theme is being considered (not yet driving investment) |
| Active | Theme is actively driving Objectives and resource allocation |
| Dormant | Theme has no current Objectives but is not retired (may be reactivated) |
| Retired | Theme is no longer relevant |

**State Diagram:**

```
Proposed ──[approved by leadership]──► Active
                                         │
                               [last Objective achieved/    [new Objective
                                deferred, no successor]     created]
                                         │                     │
                                         ▼                     │
                                      Dormant ◄────────────────┘
                                         │
                               [strategic direction
                                abandoned]
                                         │
                                         ▼
                                      Retired

Active ──[strategic direction abandoned]──► Retired
```

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Origin (Portfolio) | Portfolio (Strategy) | Portfolio-scoped Themes originate from Portfolio strategy |
| Downstream | Objective (Strategy) | Theme is pursued through Objective(s) across horizons |
| Influences | Customer Segment (Customer Value) | Theme focuses investment on specific segments |
| Influences | Value Stream / Capability (Structural) | Theme drives structural investment |
| Work Model | Deliberation (Discovery) | Theme-level strategy Deliberations may shape Themes |

## Examples

| Theme | Scope | Objectives (across horizons) |
|---|---|---|
| "LATAM Market Leadership" | Portfolio | H2 2026: "Expand to LATAM currencies" → H1 2027: "20% LATAM market share" → H2 2027: "#1 in Brazil" |
| "Developer Experience" | Portfolio | H2 2026: "Reduce API integration time to <4 hours" → H1 2027: "Launch SDK for 3 languages" |
| "Payment Adapter Consolidation" | Product | H1 2027: "Unified adapter framework" → H2 2027: "Migrate all providers to framework" |

## Notes

- A Theme without active Objectives is `Dormant` — it represents a strategic direction that's acknowledged but not currently driving work. This is distinct from `Retired` (abandoned).
- Not every Objective must belong to a Theme. Reactive Objectives (e.g., "Remediate critical security vulnerability") are Theme-independent.
- Product-scoped Themes may be elevated to Portfolio scope when the strategic direction is adopted across products. The `Scope` field changes; the entity persists.
