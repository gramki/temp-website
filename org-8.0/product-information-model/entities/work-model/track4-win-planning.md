# Win Planning

**Model:** Work Model
**Track:** Track 4: The Win Track (Value Realization)
**Category:** Planning
**Owner:** Product Marketing, Sales, Customer Success

## Definition

A parent entity type for planning Win Track work, with five lever-specific subtypes. Each subtype plans a different kind of Win Track activity aligned to the lever it activates:

1. **Customer Release Planning** (Product lever) — Coordinates market delivery of a Customer Release: segment sequencing, market readiness, and coordination with Build Track's Release Planning Task. This is the Win Track's counterpart to Build Track release planning — Build plans technical delivery, Win plans market delivery.

2. **GTM Planning** (GTM lever) — Plans launch messaging, pricing communication, partnership execution, and marketing campaigns. Supersedes the earlier GTM Planning Task entity with broader lever-aligned scope.

3. **Sales Enablement Planning** (Sales Enablement lever) — Plans competitive programs, demo environment programs, and sales training to equip the sales organization for acquisition and expansion.

4. **Customer Success Planning** (Customer Success lever) — Plans onboarding programs, retention programs, expansion programs, and advocacy initiatives across the post-sale lifecycle.

5. **Engagement Planning** (cross-lever) — Plans which prospects, customers, segments, and partners to engage, sequencing, and prioritization. Determines where Win Teams focus their one-to-one (and one-to-partner) engagement effort. Includes partner prioritization and sequencing when the product has a channel/partner model. Engagement Planning is lever-agnostic because it coordinates across multiple levers — an engagement plan may involve Product, GTM, Sales Enablement, CS, and partner work simultaneously.

## Purpose

Makes Win Track planning work explicit and lever-aligned. Without Win Planning:
- Market delivery of Customer Releases happens ad hoc without coordinated sequencing
- GTM, Sales Enablement, and CS activities lack a planning artifact that connects them to Initiatives and Win Outcomes
- There is no structured way to decide which customers and segments to prioritize for engagement
- The relationship between planning and the enablement/engagement work it drives is invisible

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Concise planning scope statement |
| Subtype | Enum | `Customer Release Planning` / `GTM Planning` / `Sales Enablement Planning` / `Customer Success Planning` / `Engagement Planning` |
| Initiative(s) | List of References (Dim 1) | Which Initiative(s) this planning advances |
| Lever(s) Activated | List of Enums | Which lever(s) this planning activates (Product / GTM / Sales Enablement / Customer Success) |
| Win Outcome(s) Targeted | List of References (Dim 2) | Which Win Outcome(s) this planning aims to achieve |
| Customer Segment(s) | List of References (Dim 3) | Which segment(s) this planning covers |
| Planning Cycle | String | The planning period (e.g., "Q3 2026", "H2 2026") |
| Description | Text | Detailed scope and approach for this planning cycle |
| Owner | String | Role/person accountable for this planning work |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Planned | Planning work is scoped but not started |
| In Progress | Planning is actively underway |
| Completed | Planning is finalized; downstream enablement and engagement work is defined |

> **Note:** Subtypes may extend this base lifecycle with additional statuses appropriate to their lever (e.g., GTM Planning adds `Ready` and `Launched`).

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Advances | Initiative (Dim 1) | Win Planning advances one or more Initiatives |
| Targets | Win Outcome (Dim 2) | Win Planning targets specific Win Outcomes |
| Activates | Lever (structural) | Win Planning activates specific levers |
| Drives | Win Enablement (Track 4) | Win Planning drives creation of enablement assets and programs |
| Drives | Win Engagement (Track 4) | Win Planning drives engagement activities |
| Coordinates with | Release Planning Task (Track 2) | Customer Release Planning coordinates with Build Track's Release Planning Task |
| Scoped to | Customer Segment (Dim 3) | Win Planning is scoped to specific segments |

## Examples

| Subtype | Title | Initiative | Lever | Win Outcome | Segment | Cycle |
|---|---|---|---|---|---|---|
| Customer Release Planning | "LATAM Expansion market delivery plan" | LATAM Cross-Border Expansion | Product | "First live transaction within 30 days" | LATAM Enterprise | Q3 2026 |
| GTM Planning | "LATAM launch messaging and pricing communication" | LATAM Cross-Border Expansion | GTM | "Close LATAM deals within 90-day cycle" | LATAM Enterprise | Q3 2026 |
| Sales Enablement Planning | "LATAM competitive program and demo environment" | LATAM Cross-Border Expansion | Sales Enablement | "Close LATAM deals within 90-day cycle" | LATAM Enterprise | Q3 2026 |
| Customer Success Planning | "LATAM onboarding and retention program" | LATAM Cross-Border Expansion | Customer Success | "95% annual gross retention" | LATAM Enterprise | H2 2026 |
| Engagement Planning | "Q3 LATAM prospect engagement sequencing" | LATAM Cross-Border Expansion | GTM, Sales Enablement, Customer Success | "Close LATAM deals within 90-day cycle" | LATAM Enterprise | Q3 2026 |
