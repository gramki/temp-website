# Release Planning Task

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction)
**Owner:** Product Management, Tech Lead

## Definition

Work to scope a Customer Release — determining which PSDs/Initiatives are included, defining timeline and milestones, allocating team capacity, and **identifying Integration Epics** alongside PSD-driven Epics. Release Planning is the bridge between strategic intent (Initiatives, PSDs) and tactical execution (Epics, Integration Epics).

Release Planning is responsible for:
1. **PSD decomposition into Epics** — one Epic per affected Module per PSD
2. **Integration Epic identification** — recognizing cross-System integration work that emerges when multiple Epics (and their Systems) must interoperate
3. **Milestone definition** — setting checkpoints with entry/exit criteria
4. **Capacity allocation** — team assignment and timeline

## Purpose

Makes the release scoping work explicit in the Build Track. Without Release Planning Tasks:
- PSDs are not decomposed into Epics — there is no bridge from specification to build work
- Integration work is invisible — cross-System integration is discovered late and causes delays
- Customer Release scope is ambiguous — what is in vs. out of a release is unclear

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Descriptive title (e.g., "Release Planning: LATAM Expansion R1") |
| Customer Release | Reference (Dim 1) | Which Customer Release is being planned |
| PSDs in Scope | List of References (Dim 1) | PSDs included in this release |
| Initiatives | List of References (Dim 1) | Initiatives advanced by this release |
| Epics Identified | List of References (Track 2) | PSD-derived Epics identified during planning |
| Integration Epics Identified | List of References (Track 2) | Integration Epics identified during planning |
| Milestones Defined | List of References (Track 2) | Milestones defined for this release |
| Capacity Plan | Text | Team allocation, velocity assumptions, timeline |
| Risks and Dependencies | Text | Known risks, external dependencies, blockers |

## Statuses

| Status | Description |
|---|---|
| Initiated | Release planning has begun; PSDs are being reviewed |
| In Progress | Epics are being decomposed, Integration Epics identified, Milestones drafted |
| Finalized | Release scope is locked; Epics and Milestones are committed |
| Revised | Scope has been adjusted mid-release (scope change recorded) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Scopes | Customer Release (Dim 1) | Release Planning Tasks scope Customer Releases |
| References | PSD (Dim 1) | Release Planning considers which PSDs are included |
| References | Initiative (Dim 1) | Release Planning considers which Initiatives are advanced |
| Produces | Epic(s) (Track 2) | Release Planning decomposes PSDs into Epics |
| Produces | Integration Epic(s) (Track 2) | Release Planning identifies cross-System integration work |
| Produces | Milestone(s) (Track 2) | Release Planning defines Milestones for the release |

## Examples

| Release Planning Task | Customer Release | PSDs | Epics Identified | Integration Epics |
|---|---|---|---|---|
| "Plan LATAM Expansion R1" | LATAM Expansion v1.0 | PSD-042, PSD-043, PSD-044 | 5 Epics across 3 Modules | 2 Integration Epics (Payments↔FX, Payments↔Compliance) |
| "Plan Settlement Enhancements Q3" | Settlement Q3 | PSD-045, PSD-046 | 3 Epics in Settlement Module | 1 Integration Epic (Settlement↔Bank Adapter) |

---
