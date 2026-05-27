# Governance Ritual

**Model:** Work Model
**Track:** Track 6: Governance (ACE extension)
**Category:** Orchestration
**Owner:** Role accountable for ritual outcomes
**Governance Admin:** Role that maintains the Ritual Definition this item executes

## Definition

Governance Ritual is a cadence-based or event-triggered governance orchestration item that executes a Ritual Definition from the Operating Model.

It organizes participants, inputs, reports, dashboards, evidence, decisions, action items, findings, recognitions, and register outputs.

## Purpose

Governance Ritual makes governance practices explicit and executable. It prevents governance from being modeled only as blocking gates or policy checks. Rituals also create appreciation, recognition, shared learning, and operating-model improvement signals.

## Fields

| Field | Type | Description |
|---|---|---|
| Ritual ID | String | Unique ritual instance identifier |
| Ritual Definition | Reference (Operating Model) | Definition being executed |
| Governance Admin Scope | Reference | Foundry, Workspace, or Workbench scope where the ritual is configured |
| Accountable Owner | Reference (WFR role binding) | Role accountable when ritual outputs age without follow-up |
| Ritual Definition Maintainer | Reference (WFR role binding) | Governance Admin binding for the Operating Model definition |
| Cadence / Trigger | Enum / Reference | Weekly, sprintly, release-bound, transition-triggered, quarterly, on-demand |
| Participants | List | People, roles, teams, or agents involved |
| Input Artifacts | List | Reports, dashboards, metrics, evidence, orchestration items, Work Orders, register entries |
| Decisions | List | Decisions made during the ritual |
| Action Items | List | Follow-up actions or Work Orders |
| Findings | List | Governance Findings produced |
| Recognitions | List | WFR Recognition entries or Kudos outputs |
| Register Outputs | List | Risk, debt, compliance, or finding entries |
| Status | Enum | Current lifecycle status |

## Statuses

| Status | Description |
|---|---|
| Scheduled | Ritual instance is planned |
| In Preparation | Inputs and reports are being assembled |
| In Progress | Ritual is underway |
| Decisions Recorded | Decisions and action items are captured |
| Follow-up Routed | Findings, register entries, or Work Orders are routed |
| Closed | Ritual instance is complete |
| Cancelled | Ritual instance is cancelled with rationale |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Executes | Ritual Definition (Operating Model) | Ritual is an instance of an Operating Model ritual definition |
| Consumes | Reports / Dashboards / Evidence | Ritual reviews operating state and evidence |
| May contain | Governance Enforcement (Track 6) | Ritual may run policy assertions as part of its work |
| Produces | Governance Finding (artifact) | Ritual may produce findings |
| Produces | Recognition Entry (WFR register artifact) | Ritual may produce kudos/recognition |
| May trigger | Evolve Case (Track 5) | Ritual may trigger governance practice evolution |
| May create | Workspace Work Order | Ritual may create action-item Work Orders |

## Examples

- Product Intent Review
- Release Readiness Review
- Customer Release Intent Readiness Review
- Architecture Review Board
- Compliance Evidence Review
- Discovery Case Review
- Governance Trend Review
