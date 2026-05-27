---
name: Build Track Detailing
overview: Detail the Build Track (Track 2) with properly scoped work entities (Module vs System/Component), integration entities, three-tier versioning artifacts, Design Deliberation, and all cross-cutting updates across the UPIM model.
todos:
  - id: phase1-renames
    content: "Phase 1: Rename track2-module-version -> track2-system-version, track2-user-story -> track2-story, rewrite all 8 existing entity files with full detail"
    status: completed
  - id: phase2-new-entities
    content: "Phase 2: Create 5 new entity files (integration-epic, integration-story, design-deliberation, technical-debt-item, new module-version)"
    status: completed
  - id: phase3-work-model
    content: "Phase 3: Rewrite Build Track section in draft-work-model.md"
    status: completed
  - id: phase4-wef
    content: "Phase 4: Update draft-work-execution-framework.md (cross-track inventory, artifact sections)"
    status: completed
  - id: phase5-xrefs
    content: "Phase 5: Cross-cutting reference updates (Dim 5, Dim 7, Run Track, Win Track, Dim 1, other entities)"
    status: completed
  - id: phase6-docs
    content: "Phase 6: DR-026, narrative seeds, FAQs, READMEs, broad Module Version -> System Version rename in existing docs"
    status: completed
isProject: false
---

# Build Track Detailing Plan

## Context

The Build Track has 10 skeletal entity files. This plan implements 16 design decisions (S1-S16) from the planning discussion, introducing key structural changes:

- **Scoping correction:** Epic/Story are Module-scoped (Dim 8); Technical Task is System/Component-scoped (Dim 5)
- **Work entity vs artifact distinction:** Epics, Stories, Tasks are work entities; System Version, Module Version, Product Version are artifacts
- **Three-tier versioning:** System Version (deployment unit) -> Module Version (integration unit) -> Product Version (certification unit)
- **Integration entities:** Integration Epic and Integration Story as separate entities
- **New entities:** Design Deliberation, Technical Debt Item
- **Renames:** Module Version -> System Version, User Story -> Story

## Phase 1: Rename and Rewrite Existing Entity Files

### 1a. Rename `track2-module-version.md` -> `track2-system-version.md`

Rewrite as **System Version**: versioned, quality-gated artifact of a System (Dim 5). Add quality gate fields (test coverage, security scan, performance benchmark results). Note that quality gates reflect in Operational Readiness (Dim 7). Status lifecycle: `Building` -> `Released`.

### 1b. Rename `track2-user-story.md` -> `track2-story.md`

Rewrite as **Story**: unit of work within an Epic, Module-scoped (Dim 8). Not necessarily user-facing — can be technical or user-facing. Full fields, statuses, relationships including "implemented by -> Technical Task(s) (System/Component, Dim 5)".

### 1c. Rewrite 5 skeletal entity files with full detail

- `**track2-epic.md**` — Module-scoped (Dim 8), decomposed from PSD. Fields: Module reference, PSD reference, acceptance criteria, effort. Statuses: `Defined` -> `In Progress` -> `Done`. Relationship: "implemented by -> Technical Task(s)".
- `**track2-technical-task.md**` — System/Component-scoped (Dim 5). Serves both regular Stories and Integration Stories. Fields: System reference, Component reference (optional).
- `**track2-bug.md**` — Add provenance field (`Build` / `Run` / `Win`). Add relationships: "originated from -> Incident (Track 3)" and "originated from -> Win Case (Track 4)".
- `**track2-release-planning-task.md**` — Add responsibility for identifying Integration Epics alongside PSD-driven Epics. Full fields, statuses.
- `**track2-milestone-planning-task.md**` — Add cross-Epic dependency gating, integration verification gates. Full fields, statuses.
- `**track2-iteration-planning-task.md**` — Assigns Stories and Technical Tasks to sprints. Full fields, statuses.

### 1d. Update `track2-product-version.md`

Update to compose **Module Versions** (not System Versions directly). Add end-to-end test suite field. Update BOM to reference Module Versions containing System Versions.

## Phase 2: Create New Entity Files (5 files)

- `**track2-integration-epic.md**` — Cross-System integration work, emerging from Build Track planning. References PSD-derived Epic(s)/Story(ies) being integrated. References Interaction Pattern (Dim 5).
- `**track2-integration-story.md**` — Unit of integration work within an Integration Epic. Produces integration contracts, integration test suites.
- `**track2-design-deliberation.md**` — Build Track's collaborative technical discussion. Produces ADR(s) (Dim 5). Narrower scope than Discovery Track Deliberation.
- `**track2-technical-debt-item.md**` — Work artifact documenting accumulated debt. When prioritized, resolved via Epic.
- `**track2-module-version.md**` (NEW) — Integration-verified composition of System Versions for a Module (Dim 8). Contains integration contracts (API schemas, event schemas) and integration test suite. Status: `Integrating` -> `Verified`.

## Phase 3: Update `draft-work-model.md` — Build Track Section

Complete rewrite of the Build Track section (lines 55-84) to reflect:

- Work entities vs work artifacts distinction
- Three-tier versioning (System Version -> Module Version -> Product Version)
- Epic = Module scope, Technical Task = System scope
- Integration Epic/Story as separate entities from Build planning
- Design Deliberation producing ADRs
- Technical Debt Item as artifact
- Story (not User Story)
- Bug provenance (Build/Run/Win)

## Phase 4: Update `draft-work-execution-framework.md`

### 4a. Build Track cross-track inventory (lines 164-178)

- Rename User Story -> Story
- Replace Module Version row with System Version
- Add Module Version row (the integration artifact)
- Add Integration Epic, Integration Story rows
- Add Design Deliberation row (produces ADR)
- Add Technical Debt Item row (artifact)
- Update Product Version to reference Module Versions

### 4b. Delivery Artifacts section

Add System Version, Module Version (integration), update Product Version definition.

## Phase 5: Cross-Cutting Reference Updates

### 5a. Dim 5 entity updates

- `**dim5-system.md**` — Update relationship: "Produces -> Module Version (Track 2)" becomes "Produces -> System Version (Track 2)". Add "Design Deliberation (Track 2)" as relationship.
- `**dim5-interaction-pattern.md**` — Add relationship: "Realized by -> Integration Epic (Track 2)".

### 5b. Dim 7 entity update

- `**dim7-operational-readiness.md**` — Add note: System Version quality gate fields feed Operational Readiness assessment.

### 5c. Run Track updates

- `**track3-deployment.md**` — Replace all "Module Version" references with "System Version" (you deploy Systems, not Modules). Update fields and relationships.
- `**track3-incident.md**` — Verify "May produce -> Bug (Track 2)" relationship exists (it does). Add provenance note.

### 5d. Win Track update

- `**track4-win-case.md**` — Add relationship: "May produce -> Bug (Track 2, provenance: Win)" for complaints/escalations that reveal product defects.

### 5e. Dim 1 entity updates

- `**dim1-customer-release.md**` — Update references from Module Version to System Version/Product Version as appropriate.

### 5f. Other entity cross-reference updates

Update "Module Version" -> "System Version" and "User Story" -> "Story" in:

- `track2-build-monitoring.md`
- Various relationship tables in updated entity files

## Phase 6: Documentation Updates

### 6a. DR-026

Create `DR-026-build-track-detailing.md` covering all 16 decisions:

- Work entity vs artifact distinction
- Epic = Module scope, Technical Task = System scope
- System Version (not Module Version) as deployment artifact
- Three-tier versioning
- Integration Epic/Story as separate entities
- Design Deliberation, Technical Debt Item
- Story (not User Story)
- Bug provenance

### 6b. Narrative seeds

Add Build Track session seeds: Epic/Story Module scoping, Technical Task System scoping, three-tier versioning, integration entities, Design Deliberation, work entity vs artifact distinction.

### 6c. FAQs

Add Q85-Q90 covering: Why Epic = Module and Task = System? Why three-tier versioning? Why separate Integration Epic? Why Design Deliberation distinct from Discovery Deliberation? Why Technical Debt as artifact? Why Bug provenance?

### 6d. READMEs

- `**entities/README.md**` — Update directory listing (renames, new files)
- `**README.md**` — Update Build Track summary row
- `**decisions/README.md**` — Add DR-026

### 6e. Broad "Module Version" -> "System Version" rename

Update remaining references in:

- `draft-modeling-faqs.md` (lines 149, 160, 166-167, 171-172, 175, 191, 197)
- `narrative-seeds.md` (lines 259, 435, 439, 664)
- `draft-definition-model.md` (lines 70, 299)
- `decisions/DR-003-customer-release.md`, `DR-004-three-layer-versioning.md`, `DR-005-deployment-per-environment.md`

Note: DR-004 ("Three-Layer Versioning") will need significant updates since the three layers are now System Version -> Module Version -> Product Version (previously Module Version -> Product Version -> Customer Release).