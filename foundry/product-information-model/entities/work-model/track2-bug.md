# Bug

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction)
**Owner:** QA, Developers

## Definition

A work entity for defect resolution — a report of incorrect, unexpected, or broken behavior that requires a fix. Bugs are unplanned work that disrupts the planned delivery of Epics and Stories.

Bugs carry a **provenance** field indicating where the defect was discovered:
- **Build** — discovered during Build Track work (development, testing, code review)
- **Run** — originated from Incident Response Task (Track 3) during incident investigation, or from Post-Incident Review corrective actions. Links back to the Incident artifact.
- **Win** — originated from a Win Track Win Case (Track 4), where a customer complaint or escalation reveals a product defect

Provenance enables traceability: a Run-originated Bug links back to its Incident (artifact) and the Incident Response Task or Post-Incident Review that identified it; a Win-originated Bug links back to its Win Case.

> **P0 and the emergency fix path.** Run-provenance Bugs from SEV-0/SEV-1 Incidents default to P0 at triage, signaling sprint-boundary bypass and eligibility for the Emergency quality gate profile on the resulting System Version. P0 Bugs may be fixed via an Emergency System Version (reduced gate profile: peer review + security scan + smoke tests required; full regression + performance benchmarks deferred). The Bug carries a `Deferred Gate Obligation` referencing the Emergency System Version and remains at `Fixed` status until a subsequent Standard System Version passes all deferred gates, at which point the Bug moves to `Verified`/`Closed`. This prevents emergency hotfixes from permanently lowering quality standards. See DR-031.

> **Known Error / Workaround pattern.** When an Incident is resolved with a workaround (not a permanent fix), the resulting Bug carries the workaround description in its `Workaround` field. This makes the workaround discoverable for future incidents of the same type — the Bug serves as the Known Error registry until the permanent fix is delivered.

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
| Originating FIR | Reference (Track 4) | Optional — the FIR from which this Bug was routed, for Win-provenance and Run-provenance Bugs that trace back to an FIR (DR-032) |
| Environment | Reference (Dim 7) | Where the defect was observed |
| Assignee | String | Developer assigned |
| Root Cause | Text | Root cause analysis (filled after resolution) |
| Workaround | Text | Temporary workaround for the defect, if known (e.g., from Incident Response Task). Makes this Bug discoverable as a Known Error for future incidents of the same type. |
| Deferred Gate Obligation | Reference (Track 2) | Optional — when a P0 Bug is fixed via an Emergency System Version, references the System Version carrying deferred quality gates. Bug stays at `Fixed` until deferred gates pass on a subsequent Standard System Version, then moves to `Verified`/`Closed`. See DR-031 D3. |

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
| Originated from | Incident (Track 3, artifact) | Run-provenance Bug originated from a production Incident |
| Produced by | Incident Response Task or Post-Incident Review (Track 3) | The work entity that identified this defect during incident handling |
| Originated from | Win Case (Track 4) | Win-provenance Bug originated from a customer complaint/escalation |
| May originate from | FIR (Track 4, PFR-Win) | Win/Run-provenance Bugs may trace back to an FIR (DR-032) |
| Fixed in | System Version (Track 2) | Bug fix is included in a System Version |
| Fixed in (Emergency) | System Version (Track 2) | P0 fix via Emergency gate profile; deferred gates tracked via this Bug's Deferred Gate Obligation field (DR-031) |

## Examples

| Bug | Provenance | Severity | System | Origin |
|---|---|---|---|---|
| "FX rate calculation returns incorrect rounding for JPY" | Build | Major | fx-service | Discovered in unit tests during Story implementation |
| "Payment timeout on cross-border transfers > $50K" | Run | Critical | payments-service | Incident INC-2847 — production timeout spike |
| "Settlement file missing header for Bank of Brazil" | Win | Major | bank-adapter | Win Case WC-312 — partner bank complaint |
| "Dashboard shows stale compliance status" | Build | Minor | compliance-service | Found during code review |

---
