# Evolve Definition Task

**Model:** Work Model
**Track:** Track 5: Evolve (Process Evolution)
**Owner:** Process Leads, Product Ops, Engineering Managers

## Definition

Evolve Definition Task is the core meta-work entity — the work of creating or updating Work Model and Operating Model definitions. This includes: (a) work entity definitions (fields, statuses, relationships), (b) artifact type definitions and assessment criteria, (c) Definition of Done criteria (entry/exit criteria, artifact checklists), and (d) Operating Model guidance structures (playbook templates, ceremony definitions, role descriptions).

## Purpose

The Work Model and Operating Model are living documents that must evolve as the product, organization, and market change. Evolve Definition Task is where that evolution happens — it is the mechanism by which process improvements, new entity types, refined artifact criteria, and updated guidance are formally defined and applied. Without it, model evolution is informal and inconsistent — changes happen in people's heads but not in the shared model.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive name (e.g., "Define DoD for Win Engagement entities") |
| Definition Scope | Enum | `Work Entity Definition`, `Artifact Type Definition`, `DoD Criteria`, `Guidance Structure`, `Assessment Criteria`, `Track Introduction` |
| Target Track(s) | List | Which track(s) the definition change affects |
| Target Entity/Artifact | Reference | Specific entity types or artifact types being defined or updated |
| Change Type | Enum | `New` (creating from scratch), `Update` (refining existing), `Deprecate` (retiring), `Restructure` (significant reorganization) |
| Triggered by | Reference | Evolve Findings, Evolve Planning, or ad hoc need |
| Rationale | Text | Why this definition change is needed — references findings, gaps, or improvement objectives |

## Statuses

| Status | Description |
|---|---|
| Planned | Definition work is scoped and assigned |
| In Progress | Definition is being authored or revised |
| Reviewed | Definition has been reviewed by affected track owners and stakeholders |
| Applied | Definition has been committed to the model (entity files updated, framework updated) |
| Rejected | Definition was reviewed and not accepted (with rationale) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Scoped by | Evolve Planning (Track 5) | Planning cycle defines which definitions to create or update |
| Triggered by | Evolve Findings (Track 5) | Findings identify gaps that require definition work |
| Updates | Work entities (Tracks 1–5) | Creates or modifies entity definitions |
| Updates | Artifact types (all tracks) | Creates or modifies artifact type definitions and assessment criteria |
| Updates | Operating Model guidance | Creates or modifies playbook templates, ceremony definitions, role descriptions |
| Produces | Decision Record (DR) | Significant definition changes are documented as Decision Records |

## Outputs / Artifacts

| Artifact | Category | Description | Downstream Consumer |
|---|---|---|---|
| Updated entity file(s) | Specification | Modified entity definition with new/updated fields, statuses, relationships | All tracks (practitioners use entity definitions) |
| Updated artifact type definition | Specification | New or revised artifact type with assessment criteria | All tracks (artifact producers and reviewers) |
| Updated DoD criteria | Specification | New or revised entry/exit criteria and artifact checklists | All tracks (work item owners) |
| Guidance structure template | Specification | Playbook template or ceremony definition structure | Operating Model (guidance authors) |
| Decision Record | Decision | DR documenting significant definition changes with rationale | UPIM stakeholders |

## Example

**Name:** "Define DoD for Win Engagement entities"
**Definition Scope:** DoD Criteria
**Target Track(s):** Track 4: Win
**Target Entity/Artifact:** Win Engagement (all 7 subtypes)
**Change Type:** New
**Triggered by:** Evolve Findings from "Q3 Win Track Artifact Quality Review" — finding: Implementation/Onboarding missing integration verification in 35% of cases
**Rationale:** Win Engagement entities currently have no formal DoD. The absence leads to inconsistent quality — some engagements are closed without complete artifacts. Defining DoD ensures all subtypes have explicit exit criteria and artifact checklists.
**Output:** 7 updated entity files with DoD sections; updated Work Execution Framework artifact inventory

---
