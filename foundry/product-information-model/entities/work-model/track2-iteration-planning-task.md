# Iteration Planning Task

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction)
**Owner:** Tech Lead, Developers

## Definition

Work to assign Stories and Technical Tasks to a time-boxed iteration (sprint), balance team capacity, and identify dependencies and risks for the iteration. Iteration Planning operates at the intersection of Module-scoped Stories and System-scoped Technical Tasks — pulling Stories into the sprint and ensuring their Technical Tasks are assigned and sequenced.

## Purpose

The tactical planning unit within the Build Track. Without Iteration Planning Tasks:
- Stories and Technical Tasks are not assigned to sprints — work is unsequenced
- Capacity balancing is ad hoc — team members are over- or under-committed
- Sprint-level dependencies are invisible — a Story requiring Technical Tasks across multiple Systems may block on another team's work

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Descriptive title (e.g., "Sprint 14 Planning — FX Team") |
| Iteration | String | Sprint/iteration identifier (e.g., "Sprint 14") |
| Stories Assigned | List of References (Track 2) | Stories pulled into this iteration |
| Integration Stories Assigned | List of References (Track 2) | Integration Stories pulled into this iteration |
| Technical Tasks Assigned | List of References (Track 2) | Technical Tasks assigned to developers for this iteration |
| Capacity | Text | Team capacity — available person-days, velocity, PTO adjustments |
| Dependencies | Text | Cross-team, cross-System dependencies for this iteration |
| Sprint Goal | Text | Overarching goal for the iteration |
| Carry-Over | List of References (Track 2) | Incomplete Stories/Tasks from previous iteration |

## Statuses

| Status | Description |
|---|---|
| Planning | Sprint is being planned — Stories and Tasks being assigned |
| Committed | Sprint plan is finalized and committed |
| In Flight | Sprint is underway |
| Completed | Sprint has ended — retrospective due |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Assigns | Story(ies) (Track 2) | Iteration Planning assigns Stories to iterations |
| Assigns | Integration Story(ies) (Track 2) | Iteration Planning assigns Integration Stories to iterations |
| Assigns | Technical Task(s) (Track 2) | Iteration Planning assigns Technical Tasks to iterations |
| Part of | Milestone (Track 2) | Iteration contributes to Milestone progress |
| Tracks | Bug(s) (Track 2) | Iteration may include Bug resolution work |

## Examples

| Iteration Planning | Sprint | Stories | Technical Tasks | Sprint Goal |
|---|---|---|---|---|
| "Sprint 14 — FX Team" | Sprint 14 | "Lock FX rate for 24 hours", "Display rate lock countdown" | 6 TTs across fx-service, 2 TTs in payments-service | Complete rate locking feature end-to-end |
| "Sprint 14 — Compliance Team" | Sprint 14 | "Add LATAM OFAC screening" | 4 TTs in compliance-service, 1 TT in payments-service | OFAC screening API complete |
| "Sprint 15 — Integration" | Sprint 15 | 2 Integration Stories (Payments↔FX) | 3 TTs in payments-service, 2 TTs in fx-service | Payments-FX integration verified |

---
