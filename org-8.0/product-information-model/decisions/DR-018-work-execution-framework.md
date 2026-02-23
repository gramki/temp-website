# DR-018: Introduce Work Execution Framework — Artifacts, Definition of Done, and Guidance Patterns

**Status:** Accepted
**Date:** 2026-02-15

## Context

The Work Model defines what work exists (entity types, state transitions, relationships) across four tracks. However, it was inconsistent in capturing three execution dimensions:

1. **Artifacts** — what structured outputs each work type produces. Some artifacts were well-modeled because they feed back into the Definition Model (PDR, PSD, Feedback), but most were implied rather than structurally captured (Research findings, deployment runbooks, enablement assets, case resolution records).

2. **Definition of Done** — when work is complete. No work entity had explicit entry/exit criteria or artifact checklists. Stakeholders could see what work to do but not what "done" means structurally.

3. **Guidance** — how to navigate work from initiation to completion. Playbooks, guidelines, and decision frameworks were entirely absent from the model, leaving no reference point for execution methodology.

This asymmetry meant:
- Downstream consumers couldn't reliably expect specific outputs from upstream work
- Quality assessment was implicit — no quality gates or completion criteria
- Cross-track handoffs were defined by relationships but lacked artifact contracts
- New team members had no structured entry point for understanding how to perform a work type

## Decisions

### 1. Introduce Work Execution Framework as a Work Model concern

A new framework document (`draft-work-execution-framework.md`) establishes the systematic approach for capturing artifacts, Definition of Done, and guidance across all four tracks. The framework sits within the Work Model, not as a separate model.

### 2. Define five-category artifact taxonomy

All work outputs are classified as: **Decision** (recorded choices with rationale), **Evidence** (findings and observations), **Specification** (descriptions of what to build/deliver), **Delivery** (versioned, quality-gated outputs), **Assessment** (evaluations against targets or criteria). Work entities may produce artifacts in multiple categories.

### 3. Distinguish transitional from terminal artifacts

Transitional artifacts are born in one track and consumed by another (PSD: Discovery → Build; System Version: Build → Run; Feedback: Win → Discovery). Terminal artifacts are consumed within their own track or by external systems. This distinction identifies integration points and handoff contracts.

### 4. Define common DoD structure: entry criteria, exit criteria, artifact checklist

Every work entity's Definition of Done has three components: what must be true before work starts (entry), what must be true for completion (exit), and which artifacts must be produced. Entity-level DoD (Work Model concern) may be extended by instance-level DoD (Operating Model concern, per-team).

### 5. Define guidance structure but locate content in Operating Model

The Work Model defines what a playbook should cover (triggers, key activities, decision points, artifacts, quality considerations, common pitfalls, related work) but not the playbook content itself. Content lives in the Operating Model, referenced from entity files. This maintains the Work Model / Operating Model boundary.

### 6. Extend work entity file template

Three new optional sections are added to the work entity file template: `Outputs / Artifacts`, `Definition of Done`, and `Guidance Reference`. These sections are populated incrementally as each track is detailed.

### 7. Phase the detailing iteratively by track

The framework is designed for incremental development: framework structure (Phase 0), then one track at a time (Phases 1–4), then cross-track integration validation (Phase 5). Tracks can be detailed in any order.

## Rationale

- **Artifacts are information model entities.** What a work type produces is a structural property of that work — not a team-specific practice. A Win Review always produces Feedback and target progress updates, regardless of which team runs it. This belongs in the Work Model.
- **DoD is a completion contract.** Entry/exit criteria and artifact checklists define the shape of "done" — they are structural, not procedural. Different teams may extend DoD but the base criteria are universal.
- **Guidance content varies by team.** Playbooks and procedures are methodology — they depend on team size, product context, and organizational maturity. This is Operating Model territory. The Work Model captures *what a playbook should cover*, not *what it says*.
- **The framework enables self-service.** New stakeholders can look at any work entity and understand: what it produces, when it's done, and where to find guidance. This reduces onboarding friction and improves work quality.

## Consequences

### Positive
- Systematic coverage of work outputs across all four tracks
- Explicit quality gates and completion criteria for every work entity
- Clear cross-track handoff contracts via transitional artifact identification
- Stakeholders can self-serve understanding of any work type's execution expectations
- Incremental development — framework provides value before all tracks are detailed

### Negative
- Entity files become longer with three new sections (mitigated: sections start as `_To be refined._` and are filled incrementally)
- Potential confusion about Work Model vs. Operating Model boundary for guidance (mitigated: clear boundary rule — structure here, content there)
- Artifact taxonomy must be maintained as new work entities are added (low cost: five categories are stable)
