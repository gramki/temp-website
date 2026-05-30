# Objective

**Model:** Definition Model
**Dimension:** Strategy
**Owner:** Executive Leadership, Product Management

## Definition

A strategic goal over a defined planning horizon. Objectives answer "where are we going?" and are set by executive and product leadership. They provide the top-level filter for all downstream prioritization — Signals and Initiatives are evaluated against active Objectives.

## Purpose

Objectives introduce strategic direction into the UPIM. Without Objectives, every Signal (Problem, Need, Opportunity) is an equal candidate for discovery at every point in time. Objectives ensure that discovery work is purposefully prioritized — Signals are associated with Initiatives that advance specific Objectives, creating a clear line from business strategy to product execution (see FAQ Q11).

Objectives may optionally belong to a Strategic Theme, which provides persistent cross-horizon direction. Not every Objective must have a Theme — reactive Objectives (e.g., "Remediate critical security vulnerability") are Theme-independent.

## Fields

| Field | Type | Description |
|---|---|---|
| ID | String | Unique identifier (e.g., `OBJ-2026-H2-01`) |
| Title | String | Concise statement of the strategic goal |
| Horizon | String | Planning period (e.g., "H2 2026", "FY2027") |
| Strategic Theme | Reference (Strategy) | Optional — which Theme this Objective advances |
| Sponsor | Role/Person | Executive sponsor accountable for the Objective |
| Success Criteria | Text | Measurable criteria for achievement |
| External Constraints | List (text) | Regulatory deadlines, partnership timelines, competitive threats, contractual obligations that constrain timing or scope |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Draft | Objective is being formulated, not yet approved |
| Active | Objective is approved and guides current planning |
| Achieved | Success criteria have been met |
| Deferred | Objective is postponed to a future horizon |

**State Diagram:**

```
Draft ──[approved by leadership]──► Active
                                      │
                           ┌──────────┼──────────┐
                           │          │          │
                    [success     [postponed    [context
                     criteria     to future     changed;
                     met]         horizon]      no longer
                           │          │          relevant]
                           ▼          ▼          ▼
                       Achieved   Deferred    (Cancelled
                                      │        — remove or
                                      │        document)
                               [re-activated
                                in new horizon]
                                      │
                                      ▼
                                   Active
```

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Strategic Theme (Strategy) | Objective may advance a Strategic Theme (optional) |
| Downstream | Initiative (Strategy) | Objective is pursued through Initiative(s) |
| Targets | Win Outcome (Vendor Value) | Objective may target specific Win Outcomes (per AAARRR stage, per segment) |
| Work Model | Objective Setting Task (Discovery) | Objective Setting Tasks produce/refine Objectives |

## Example

"Expand cross-border payment coverage to LATAM markets by end of H2 2026."
- Theme: "LATAM Market Leadership" (Portfolio scope)
- Horizon: H2 2026
- External Constraints: "LGPD enforcement: March 2027", "Partner X LATAM launch: Q3 2026"
