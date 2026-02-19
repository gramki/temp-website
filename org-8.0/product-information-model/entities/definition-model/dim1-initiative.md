# Initiative

**Model:** Definition Model
**Dimension:** Dimension 1: The Strategy Dimension
**Owner:** Product Management, Executive Leadership

## Definition

A cross-track strategic program to advance one or more Objectives. An Initiative is the coordination construct that associates Signals for discovery, targets Win Outcomes, declares a Lever Mix (weighted from the Business Model's Lever Portfolio), and carries embedded Targets (like Key Results in an OKR). Initiatives drive work across all tracks — not just Discovery → Build.

## Purpose

Initiatives bridge the gap between high-level strategic Objectives and the Signals awaiting investigation. Without Initiatives, there is no mechanism to group and prioritize related Signals for coordinated discovery and delivery. An Initiative provides the "why now?" and "why together?" context for a set of Signals, and maps downstream to Customer Release(s) that deliver the Initiative's outcomes to customers (see FAQ Q11).

With the addition of Lever Mix and embedded Targets, Initiatives evolve from being primarily Discovery-focused 'programs of Signals' to cross-track coordination constructs. A 'LATAM Enterprise Market Entry' Initiative with lever mix Product 40% / GTM 25% / Sales Enablement 20% / CS 15% tells downstream planners in each track what kinds of work to expect.

## Fields

| Field | Type | Description |
|---|---|---|
| ID | String | Unique identifier (e.g., `INIT-2026-04`) |
| Title | String | Descriptive name of the initiative |
| Description | Text | Scope, target outcomes, and success criteria |
| Sponsor | Role/Person | Executive or PM sponsor |
| Target Horizon | String | Expected delivery timeframe |
| External Constraints | List (text) | Regulatory deadlines, partnership timelines, competitive threats, contractual obligations that constrain timing or scope |
| Lever Mix | List (Lever + Weight%) | Weighted allocation of effort across levers from the Business Model's Lever Portfolio (e.g., Product 40%, GTM 25%, Sales Enablement 20%, CS 15%) |
| Win Outcome(s) Targeted | List of References (Dim 2) | Which Win Outcomes this Initiative aims to advance |
| Embedded Targets | List (Target definition) | Time-bound, quantitative measures of success — like Key Results in an OKR. Each target references a Win Outcome + Business KPI, specifies a target value and time period. (e.g., "Q3: 85% activation rate for LATAM Enterprise", "Q3: CAC below $25K") |
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
| Targets | Win Outcome (Dim 2) | Initiative may target specific Win Outcomes (per AAARRR stage, per segment) |
| Downstream | Customer Release (Dim 1) | Initiative maps to Customer Release(s) |
| Work Model | Initiative Scoping Task (Track 1) | Initiative Scoping Tasks define Initiatives |
| Work Model | Prioritization Task (Track 1) | Prioritization Tasks associate Signals to Initiatives |
| Declares | Lever Mix (Business Model Dim 2) | Initiative declares lever allocation from Business Model's Lever Portfolio |
| Drives | Win Planning (Track 4) | Win Track planning aligns to Initiative |
| Drives | Win Enablement (Track 4) | Win Track enablement aligns to Initiative |
| Drives | Win Engagement (Track 4) | Win Track engagement aligns to Initiative |
| Assessed by | Win Review (Track 4) | Win Reviews assess Initiative target progress |

## Example

"LATAM Enterprise Market Entry" — Lever Mix: Product 40%, GTM 25%, Sales Enablement 20%, CS 15%. Targets: "Q3: 15 LATAM Enterprise deals closed", "Q3: 85% activation within 30 days", "Q3: CAC below $25K for LATAM Enterprise." External Constraints: "LGPD data residency enforcement: March 2027", "Partner X expects LATAM integration by Q3 2026"
