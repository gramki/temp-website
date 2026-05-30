# Evolve Findings

**Model:** Work Model
**Track:** Evolve
**Category:** Artifact (transitional)
**Owner:** Process Leads, Product Ops, Engineering Managers

## Definition

Evolve Findings is a structured observation record produced by Evolve Reviews. It is an **artifact**, not a work item — you do an Evolve Review and *produce* Evolve Findings, just as you do a Win Review and *produce* Feedback, or a Deliberation and *produce* a PDR.

## Purpose

Evolve Findings captures process gaps, artifact quality issues, guidance deficiencies, and cross-track handoff failures in a structured, referenceable form. It is the mechanism by which assessment observations become actionable inputs — either for Evolve Definition Tasks (process changes) or, when a process gap reveals a product-level issue, for the Discovery Track as a Signal.

Evolve Findings is the Evolve Track's analog of Feedback (Track 4 → Track 1). Both are transitional artifacts that bridge assessment and action.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive summary (e.g., "Win Activity DoD gap — missing integration verification") |
| Source Review | Reference | The Evolve Review that produced this finding |
| Finding Type | Enum | `Process Gap` (entity/flow not serving purpose), `Artifact Quality Issue` (artifacts below criteria), `Guidance Deficiency` (guidance missing/outdated/unused), `Handoff Failure` (transitional artifact not flowing), `Structural Gap` (missing entity or artifact type) |
| Severity | Enum | `Critical` (process failure causing measurable harm), `High` (consistent quality gap), `Medium` (improvement opportunity), `Low` (minor refinement) |
| Affected Track(s) | List | Which track(s) the finding applies to |
| Affected Entity/Artifact | Reference | Specific entity types or artifact types affected |
| Evidence | Text | Data, examples, and observations supporting the finding |
| Recommendation | Text | Suggested action — what should change in the Work Model or Operating Model |

## Statuses

| Status | Description |
|---|---|
| Captured | Finding has been recorded from an Evolve Review |
| Reviewed | Finding has been assessed for actionability and priority |
| Actioned | Finding has been consumed by an Evolve Definition Task |
| Promoted | Finding has been promoted to a Signal in the Discovery Track (product-level implication) |
| Archived | Finding does not warrant action (with rationale) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Produced by | Evolve Review (Evolve) | Reviews produce findings as their primary output |
| Consumed by | Evolve Definition Task (Evolve) | Findings trigger definition/update work |
| May promote to | Signal (Strategy, Discovery Track) | When a process gap reveals a product-level issue |
| Feeds | Evolve Planning (Evolve) | Unactioned findings inform next cycle's planning |

## Transitional Nature

Evolve Findings is a **transitional artifact** with two consumption paths:

1. **Evolve Track consumption** (primary): Findings feed Evolve Definition Tasks that update Work Model or Operating Model definitions. This is the normal path — most findings result in process improvements.
2. **Discovery Track consumption** (secondary): When a finding reveals that a process gap is actually a product gap (e.g., "Build Track has no entity for API contract testing because Ecosystem API Compatibility Contracts weren't properly linked to Build Track work"), the finding is promoted to a Signal for Discovery investigation.

Not every finding leads to action. Findings that don't warrant changes are archived with rationale — "process is working as intended despite perceived gap" or "cost of change exceeds benefit."

## Example

**Name:** "Win Activity DoD gap — missing integration verification"
**Source Review:** Q3 Win Track Artifact Quality Review
**Finding Type:** Artifact Quality Issue
**Severity:** High
**Affected Track(s):** Win
**Affected Entity/Artifact:** Implementation/Onboarding (Win Activity subtype)
**Evidence:** 35% of Implementation/Onboarding records closed without integration verification step; 3 post-implementation escalations traced to unverified integrations in Q2
**Recommendation:** Define DoD for Implementation/Onboarding with mandatory integration verification checklist; add "Integration Verification Report" as a required artifact
**Status:** Actioned → Evolve Definition Task "Define DoD for Win Activity entities"

---
