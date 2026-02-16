# Initiative

**Model:** Definition Model
**Dimension:** Dimension 1: The Strategy Dimension
**Owner:** Product Management, Executive Leadership

## Definition

A strategic program to advance one or more Objectives. An Initiative is the prioritization vehicle that associates Signals (Problems, Needs, Opportunities) for discovery investment. Signals may exist independently before being associated with an Initiative during a planning cycle.

## Purpose

Initiatives bridge the gap between high-level strategic Objectives and the Signals awaiting investigation. Without Initiatives, there is no mechanism to group and prioritize related Signals for coordinated discovery and delivery. An Initiative provides the "why now?" and "why together?" context for a set of Signals, and maps downstream to Customer Release(s) that deliver the Initiative's outcomes to customers (see FAQ Q11).

## Fields

| Field | Type | Description |
|---|---|---|
| ID | String | Unique identifier (e.g., `INIT-2026-04`) |
| Title | String | Descriptive name of the initiative |
| Description | Text | Scope, target outcomes, and success criteria |
| Sponsor | Role/Person | Executive or PM sponsor |
| Target Horizon | String | Expected delivery timeframe |
| External Constraints | List (text) | Regulatory deadlines, partnership timelines, competitive threats, contractual obligations that constrain timing or scope |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Proposed | Initiative has been identified but not yet approved |
| Approved | Initiative is approved for planning and discovery investment |
| In Progress | Discovery and/or build work is actively underway |
| Completed | All target outcomes have been delivered |
| Cancelled | Initiative is abandoned (with rationale documented) |

**State Diagram:**

```
Proposed ──[approved for investment]──► Approved ──[work begins]──► In Progress
                                                                        │
                                                              ┌─────────┼─────────┐
                                                              │                   │
                                                       [all outcomes         [abandoned;
                                                        delivered]            rationale
                                                              │               documented]
                                                              ▼                   ▼
                                                          Completed           Cancelled

Proposed ──[rejected or abandoned]──► Cancelled
Approved ──[abandoned before work starts]──► Cancelled
```

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Objective (Dim 1) | Initiative advances Objective(s) |
| Associated | Problem (Dim 1) | Initiative ← associated → Problem(s) (many-to-many, during planning) |
| Associated | Need (Dim 1) | Initiative ← associated → Need(s) (many-to-many, during planning) |
| Associated | Opportunity (Dim 1) | Initiative ← associated → Opportunity(s) (many-to-many, during planning) |
| Downstream | Customer Release (Dim 1) | Initiative maps to Customer Release(s) |
| Work Model | Initiative Scoping Task (Track 1) | Initiative Scoping Tasks define Initiatives |
| Work Model | Prioritization Task (Track 1) | Prioritization Tasks associate Signals to Initiatives |

## Example

"LATAM Currency Expansion — enable FX payouts in BRL, MXN, COP, and CLP."
- External Constraints: "LGPD data residency enforcement: March 2027", "Partner X expects LATAM integration by Q3 2026"
