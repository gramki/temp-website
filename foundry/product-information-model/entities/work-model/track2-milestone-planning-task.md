# Milestone Planning Task

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction)
**Owner:** Tech Lead, Product Management

## Definition

Work to define checkpoints within a Customer Release with clear entry/exit criteria. Milestones serve as progress gates that verify the release is on track. Milestone Planning includes:

1. **Cross-Epic dependency gating** — identifying and sequencing dependencies between Epics (e.g., "FX Module Epic must complete before Payments Module Epic can start integration testing")
2. **Integration verification gates** — defining checkpoints where System Versions must be verified and Product Version certification scoped (e.g., "API Complete milestone: all cross-border endpoints passing integration tests; Systems X and Y at Released System Versions")
3. **Quality gates** — defining System Version quality thresholds that must be met at each Milestone

## Purpose

Milestones provide intermediate verification points within a Customer Release's build cycle. Without Milestone Planning:
- Cross-Epic dependencies are invisible — parallel Epics proceed without awareness of each other's constraints
- Integration verification happens too late — incompatibilities between Systems are discovered only at release time
- Progress assessment is subjective — "are we on track?" has no structured answer

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Descriptive title (e.g., "Define 'API Complete' Milestone for LATAM R1") |
| Customer Release | Reference (Dim 1) | Which Customer Release these Milestones belong to |
| Milestone Name | String | Name of the milestone (e.g., "API Complete", "Integration Verified", "Compliance Ready") |
| Entry Criteria | Text | What must be true to enter this milestone |
| Exit Criteria | Text | What must be true to pass this milestone |
| Epic Dependencies | List of References (Track 2) | Epics that must be complete or at specific status |
| Integration Gate | Text | Integration verification requirements (e.g., which System Versions must be Released; Product Version certification scope) |
| Quality Gate | Text | System Version quality thresholds required (e.g., "All Systems > 90% test coverage") |
| Target Date | Date | When this milestone should be achieved |

## Statuses

| Status | Description |
|---|---|
| Defined | Milestone criteria are drafted |
| Active | The milestone period is underway; Epics are progressing toward criteria |
| Achieved | All entry/exit criteria met |
| At Risk | Dependencies or quality gates indicate the milestone may slip |
| Missed | Target date passed without meeting exit criteria |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Part of | Customer Release (Dim 1) | Milestones are checkpoints within a Customer Release |
| Verifies | Epic(s) (Track 2) | Milestones verify completion or progress of specific Epics |
| Verifies | Integration Epic(s) (Track 2) | Milestones may gate Integration Epic completion |
| Gates | System Version(s) (Track 2) | Milestones require System Versions to meet quality thresholds |
| Gates | Product Version (Track 2) | Milestones may require Product Version certification or scoped System Versions at Released |

## Examples

| Milestone | Customer Release | Exit Criteria | Epic Dependencies | Status |
|---|---|---|---|---|
| "API Complete" | LATAM Expansion v1.0 | All cross-border API endpoints passing integration tests | FX Rate Locking Epic, Payment Execution Epic | Active |
| "Compliance Ready" | LATAM Expansion v1.0 | OFAC screening passing with 100% match rate on test dataset | LATAM OFAC Screening Epic | Defined |
| "Integration Verified" | LATAM Expansion v1.0 | System Versions for payments, FX, compliance Systems Released; Product Version certification scoped | All Integration Epics | Defined |
| "Settlement Complete" | Settlement Q3 | Settlement reconciliation running end-to-end with partner banks | Settlement Reconciliation Epic | Active |

---
