# Epic

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction)
**Owner:** Tech Lead, Product Management

## Definition

A large, committed body of work decomposed from a PSD (Dim 1), scoped to a single Module (Dim 8). An Epic delivers a coherent chunk of product functionality — it represents a significant capability increment within the Module. Where PSD defines *what* should be built (specification), Epic defines *how much work* is committed (scope).

A cross-Module PSD (or a PDR triggering multiple PSDs) results in multiple Epics — one per affected Module. Each Epic is independently plannable, trackable, and deliverable.

## Purpose

The top-level work entity in the Build Track's functional hierarchy under Product Intent. Epic is not a primary Build orchestration item; Product Intent is. Without Epics:
- PSDs have no decomposition into trackable build work — the gap between specification and sprint is unbridged
- Release Planning has no unit to scope and sequence
- Module-level progress is invisible — "how much of the Payments Module PSD is done?" has no structured answer

**Module scope, not System scope:** Epics speak the Module language ("Build Real-Time FX Rate Locking" for the FX Module). The technical decomposition into Systems happens at the Technical Task level within Stories. This keeps Epics accessible to PMs and Tech Leads while Technical Tasks are the engineering domain. See DR-026.

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Descriptive title (e.g., "Build Real-Time FX Rate Locking") |
| Product Intent | Reference (Dim 1) | Parent Product Intent this Epic helps realize or validate |
| PSD | Reference (Dim 1) | Which PSD this Epic is decomposed from |
| Module | Reference (Dim 8) | Which Module this Epic advances |
| Initiative | Reference (Dim 1) | Which Initiative this Epic is part of (inherited from PSD) |
| Acceptance Criteria | Text | What must be true for this Epic to be considered complete |
| Effort Estimate | String | High-level effort estimate (team-weeks, story points aggregate) |
| Target Milestone | Reference (Track 2) | Which Milestone this Epic targets |
| Customer Release Intent | Reference (Dim 1) | Which Customer Release Intent this Epic is part of |

## Statuses

| Status | Description |
|---|---|
| Defined | Epic has been identified and scoped from PSD; acceptance criteria drafted |
| Ready | Epic is refined, estimated, and ready for Story decomposition |
| In Progress | Stories within this Epic are being worked on |
| Done | All acceptance criteria met, all Stories complete |
| Deferred | Epic is postponed to a future release (scope change) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Decomposed from | PSD (Dim 1) | Epic is decomposed from a PSD |
| Parent | Product Intent (Dim 1) | Epic is subordinate to Product Intent orchestration |
| Scoped to | Module (Dim 8) | Epic advances a specific Module |
| Part of | Initiative (Dim 1) | Epic contributes to an Initiative |
| Part of | Customer Release Intent (Dim 1) | Epic is scoped to a Customer Release Intent |
| Contains | Story(ies) (Track 2) | Epic contains Stories |
| Referenced by | Integration Epic (Track 2) | Integration Epics reference the functional Epics they integrate |
| Targeted by | Milestone (Track 2) | Epic may be gated by a Milestone |
| Planned by | Release Planning Task (Track 2) | Epics are identified during Release Planning |
| May trigger | Design Deliberation (Track 2) | Architectural questions during Epic work trigger Design Deliberation |

## Examples

| Epic | PSD | Module | Target Milestone | Status |
|---|---|---|---|---|
| "Build Real-Time FX Rate Locking" | PSD-043 | FX Module | API Complete | In Progress |
| "Build Cross-Border Payment Execution" | PSD-042 | Payments Module | API Complete | Defined |
| "Add LATAM OFAC Screening" | PSD-044 | Compliance Module | Compliance Ready | Ready |
| "Build Settlement Reconciliation" | PSD-045 | Settlement Module | Settlement Complete | Defined |

---
