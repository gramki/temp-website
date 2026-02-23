# Bug

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction)
**Owner:** QA, Developers

## Definition

A work entity for defect resolution — a report of incorrect, unexpected, or broken behavior that requires a fix. Bugs are unplanned work that disrupts the planned delivery of Epics and Stories.

Bugs carry a **provenance** field indicating where the defect was discovered:
- **Build** — discovered during Build Track work (development, testing, code review)
- **Run** — originated from a Run Track Incident (Track 3), escalated to Build for resolution
- **Win** — originated from a Win Track Win Case (Track 4), where a customer complaint or escalation reveals a product defect

Provenance enables traceability: a Run-originated Bug links back to its Incident; a Win-originated Bug links back to its Win Case.

## Purpose

Captures unplanned defect-resolution work within the Build Track. Without Bugs:
- Defect work is invisible — it hides inside Stories or is tracked outside the model
- Root cause traceability is lost — was this defect caught in testing, or did it cause a production incident?
- Cross-Track feedback loops are broken — Incidents (Track 3) and Win Cases (Track 4) have no mechanism to trigger fixes

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Brief description of the defect |
| Description | Text | Detailed reproduction steps, expected vs. actual behavior |
| Provenance | Enum | `Build` / `Run` / `Win` — where this Bug was discovered |
| Severity | Enum | `Critical` / `Major` / `Minor` / `Cosmetic` |
| Priority | Enum | `P0` / `P1` / `P2` / `P3` |
| System | Reference (Dim 5) | Which System the defect is in |
| Component | Reference (Dim 5) | Which Component within the System (optional) |
| Epic | Reference (Track 2) | Which Epic this Bug is associated with (if applicable) |
| Story | Reference (Track 2) | Which Story this Bug was discovered during (if Build provenance) |
| Incident | Reference (Track 3) | Source Incident (if Run provenance) |
| Win Case | Reference (Track 4) | Source Win Case (if Win provenance) |
| Environment | Reference (Dim 7) | Where the defect was observed |
| Assignee | String | Developer assigned |
| Root Cause | Text | Root cause analysis (filled after resolution) |

## Statuses

| Status | Description |
|---|---|
| New | Bug reported, not yet triaged |
| Triaged | Severity and priority assessed, assigned to a team |
| In Progress | Developer is actively working on the fix |
| In Review | Fix is written, awaiting code review |
| Fixed | Fix merged and included in a System Version |
| Verified | QA has verified the fix in the target environment |
| Closed | Bug is resolved and verified |
| Won't Fix | Intentional behavior, or fix is not justified |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| May relate to | Epic (Track 2) | Bug may be discovered during Epic execution |
| May relate to | Story (Track 2) | Bug may be discovered during Story implementation |
| Scoped to | System (Dim 5) | Bug is a defect within a specific System |
| Scoped to | Component (Dim 5) | Bug may be within a specific Component (optional) |
| Originated from | Incident (Track 3) | Run-provenance Bug originated from a production Incident |
| Originated from | Win Case (Track 4) | Win-provenance Bug originated from a customer complaint/escalation |
| Fixed in | System Version (Track 2) | Bug fix is included in a System Version |

## Examples

| Bug | Provenance | Severity | System | Origin |
|---|---|---|---|---|
| "FX rate calculation returns incorrect rounding for JPY" | Build | Major | fx-service | Discovered in unit tests during Story implementation |
| "Payment timeout on cross-border transfers > $50K" | Run | Critical | payments-service | Incident INC-2847 — production timeout spike |
| "Settlement file missing header for Bank of Brazil" | Win | Major | bank-adapter | Win Case WC-312 — partner bank complaint |
| "Dashboard shows stale compliance status" | Build | Minor | compliance-service | Found during code review |

---
