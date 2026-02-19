# Evolve Planning

**Model:** Work Model
**Track:** Track 5: Evolve (Process Evolution)
**Owner:** Process Leads, Product Ops, Engineering Managers

## Definition

Evolve Planning is work to plan evolution cycles — scoping which processes to review, which artifact types to define or refine, which guidance to develop, and which cross-track handoffs to audit. It aligns to strategic or operational improvement objectives and produces a scoped evolution agenda for the cycle.

## Purpose

Without deliberate planning, process evolution happens reactively (only when something breaks) or not at all. Evolve Planning ensures that Work Model and Operating Model improvements are intentional, prioritized, and resourced — preventing both model stagnation and unfocused process churn.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive name for the evolution cycle (e.g., "Q3 2026 Process Evolution Cycle") |
| Scope | Structured | Which tracks, entities, artifact types, and guidance areas are in scope |
| Improvement Objectives | List | What the cycle aims to achieve (e.g., "Define DoD for all Win Track entities", "Reduce PSD rejection rate by improving template") |
| Timeline | Date range | Start and end of the evolution cycle |
| Participants | List | Roles and individuals involved in review and definition work |
| Triggered by | Enum | `Scheduled` (periodic), `Evolve Monitoring Alert`, `Cross-Track Retrospective`, `Organizational Change`, `New Track/Entity Introduction` |
| Priority | Enum | `Critical` (blocking process failure), `High` (measurable quality gap), `Normal` (planned improvement), `Low` (nice-to-have refinement) |

## Statuses

| Status | Description |
|---|---|
| Draft | Cycle scope is being defined |
| Planned | Scope finalized, participants identified, timeline set |
| Active | Evolution cycle is underway — reviews and definition tasks are executing |
| Completed | All planned reviews and definition tasks are done |
| Cancelled | Cycle cancelled (with rationale) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Produces | Evolve Review (Track 5) | Plans which reviews to conduct |
| Produces | Evolve Definition Task (Track 5) | Plans which definitions to create or update |
| Informed by | Evolve Findings (Track 5) | Previous cycle findings feed next cycle planning |
| Informed by | Evolve Monitoring (Track 5) | Monitoring alerts inform planning priorities |
| Aligns to | Objective (Dim 1) | May align to strategic improvement objectives |

## Example

**Name:** "Q3 2026 Process Evolution Cycle"
**Scope:** Win Track (all entity DoDs), Discovery Track (artifact quality review), Cross-Track (PSD → Build handoff audit)
**Improvement Objectives:** (1) Define DoD for all 7 Win Engagement subtypes, (2) Review and update PSD template based on Build Track feedback, (3) Audit Feedback → Signal promotion rate
**Timeline:** July 1 – September 15, 2026
**Participants:** Product Ops Lead, Win Track Process Owner, Discovery Track PM Lead, Build Track Tech Lead
**Triggered by:** Scheduled (quarterly)
**Priority:** High

---
