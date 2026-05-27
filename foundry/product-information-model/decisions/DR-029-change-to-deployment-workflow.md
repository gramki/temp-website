# DR-029: Change-to-Deployment Workflow Redesign

> **Superseded for operational use by DR-036 (2026-05-19).** Module Version, Module/Product Package, and SDD/MDD/PDD are retired. See DR-036 and Amended Records table in DR-036.

**Status:** Accepted
**Date:** 2026-02-15
**Builds on:** DR-027 (Composition Levels), DR-028 (Deployment Descriptors)
**Analysis:** [change-to-deployment-analysis.md](../stories/change-to-deployment-analysis.md)

## Context

After DR-027 (Module Package, Product Package) and DR-028 (SDD, MDD, PDD), the model still had structural gaps in the deployment workflow:

1. **Deployment was both work entity and record.** `Deployment` had `Planned` and `In Progress` statuses (work-in-progress) alongside `Succeeded` (terminal record). Every other track separates "work to be done" from "artifact produced by work."
2. **Change Request was skeletal.** No fields, no statuses, no type taxonomy, no relationship to deployment workflow. In regulated fintech, change management is a compliance requirement.
3. **No promotion path entities.** The sequence of environments a deployment progresses through was tribal knowledge, not a structured entity with contractual and governance significance.
4. **Package specification had no Definition Model home.** The structural definition of what constitutes a Module Package (which operational systems, which wiring) was implicit in the Work Model artifact, rediscovered with each new version.
5. **No structured post-deployment verification.** Verification was either unstructured (part of Deployment) or absent. Compliance requires auditable verification with evidence.
6. **No deployment rehearsal capability.** High-risk deployments (DB migrations, multi-module orchestration) had no structured rehearsal entity.

## Decisions

### D1: Module Package (specification) is a Dim 7 Definition Model entity

**Decision:** Introduce Module Package as a Dim 7 entity — a composition specification defining which operational systems and wiring enrich a Module (Dim 8).

**Rationale:** The structural definition of what constitutes a package (healthcheck, reconciler, operational wiring) is a stable, reusable template. It belongs in the Definition Model alongside other Dim 7 operational entities. It lives in Dim 7 (not Dim 8) because package composition is an operator-facing concern (probes, dashboards, reconcilers — not tenant-serving systems), not visible to customers.

### D2: Product Package (specification) is a Dim 7 Definition Model entity

**Decision:** Introduce Product Package as a Dim 7 entity — a composition specification defining which Module Packages and cross-module wiring compose a deployable product.

**Rationale:** Same reasoning as D1, applied at the product level.

### D3: Module Package Version and Product Package Version are Work Model artifacts

**Decision:** Rename the existing `Module Package` (Track 3) to `Module Package Version` and `Product Package` (Track 3) to `Product Package Version`. These are versioned instances that instantiate their respective Dim 7 specifications.

**Rationale:** Follows the Definition Model → Work Model pattern: Module (Dim 8) → Module Version (Track 2). The specification defines the template; the version is the specific instance produced by work.

### D4: Deployment Train is a Dim 7 entity

**Decision:** Introduce Deployment Train as a Dim 7 entity — a reusable, ordered promotion path with contractual and governance significance.

**Rationale:** Promotion paths are not ad-hoc workflows; they are structured entities that carry contractual commitments (tenants rely on them for planning), governance requirements (regulated vs. standard), and operating model enablement (certain models require certain trains). The same train is reused across releases.

### D5: Station is a Dim 7 entity

**Decision:** Introduce Station as a Dim 7 entity — a checkpoint within a Deployment Train targeting a specific Deployment Environment.

**Rationale:** Each stop in the promotion path needs structured entry criteria, exit criteria, approval requirements, and soak times. The same environment can be a station in multiple trains with different governance per train.

### D6: Environment Change Cycle is a field cluster on Deployment Environment

**Decision:** Add Change Windows, Freeze Periods, Cycle Cadence, and Override Rules as structured fields on the existing Deployment Environment entity rather than creating a standalone entity.

**Rationale:** Conceptual reuse exists (PCI Freeze Cycle concept applies to all production environments), but entity instances need not be reused — each environment defines its own cycle parameters.

### D7: Deployment is refactored from work entity to work artifact

**Decision:** Refactor Deployment from a work entity (Planned → In Progress → Succeeded) to a work artifact / durable record (Active → Superseded → Rolled Back).

**Rationale:** A Deployment is a record that something happened — a descriptor was applied to an environment. It is not work to be done. The "work to be done" is the Deployment Task.

### D8: Deployment Task is a new work entity

**Decision:** Introduce Deployment Task as a Run Track work entity — the act of applying a deployment descriptor to an environment. Deployment Task produces a Deployment (artifact).

**Rationale:** Separates "work in progress" from "durable record," consistent with every other track. The Deployment Task has transient statuses (Ready, Executing, Complete, Failed); the Deployment has durable statuses (Active, Superseded, Rolled Back).

### D9: Verification Task is a standalone Run Track work entity

**Decision:** Introduce Verification Task as a standalone work entity for structured post-deployment verification.

**Rationale:** Verification is distinct from Maintenance Tasks (recurring/preventative), Run Track Technical Tasks (serve Run Stories), and Deployment Tasks (apply descriptors). It produces evidence (metrics, test results) required for Change Request closure. It is not a subtype of an existing entity — it is a first-class verification concern.

### D10: Deployment Plan is a deliberation activity

**Decision:** Introduce Deployment Plan as a Run Track deliberation activity that encapsulates Deployment Planning Tasks and produces the full deployment workflow.

**Rationale:** The Run team needs a structured activity for scoping rollouts — determining promotion paths, identifying verification needs, assessing risks, and planning Deployment Drill Tasks. Deployment Plan governs the lifecycle of Deployment Planning Tasks, which in turn produce deployment descriptors, Verification Tasks, and Maintenance Tasks.

### D11: Deployment Drill Task is optional, scoped per Plan

**Decision:** Introduce Deployment Drill Task as an optional rehearsal scoped per Deployment Plan. When present, it is a predecessor to actual Deployment Tasks under the same Plan.

**Rationale:** Scoped per Plan (not per individual Deployment Task) because the value of a drill is rehearsing the orchestrated sequence — DB migrations, multi-module coordination, rollback procedures — not just a single atomic deployment.

### D12: Change Request governs deployment-related changes only

**Decision:** Change Request is the auditable envelope for deployment-related changes, scoped to a Deployment Train or Station. Three types: Standard, Emergency-Technical (incident-driven), Emergency-Business (business exigency-driven).

**Rationale:** Maintenance Tasks may need change management but through different processes. Change Request is specifically designed for the deployment workflow — its completion requires all Deployment Tasks and Verification Tasks to pass. Emergency-Business changes may originate from Release Plan acceleration (e.g., campaign deadline).

### D13: Customer Release Intent may span multiple Deployment Trains

**Decision:** A single Customer Release Intent may be associated with multiple Deployment Trains when different modules follow different promotion paths.

**Rationale:** A release intent like "LATAM Expansion" may include modules with different compliance requirements — payment modules on a PCI Regulated Train, marketing portal on a Fast-Track Train. The Customer Release Intent is the commercial planning unit; the Train is the operational promotion unit.

## Consequences

### Positive

- Clear separation between "work to do" (Deployment Task) and "record of what was done" (Deployment)
- Auditable change management with typed Change Requests and structured Verification Tasks
- Contractual promotion paths (Deployment Trains) that tenants and commercial partners can rely on
- Stable Definition Model specifications (Module Package, Product Package) separate from versioned instances
- Emergency change handling distinguishes technical hotfixes from business-driven acceleration
- Optional Deployment Drills reduce risk for high-stakes deployments

### Negative

- More entities to manage (Deployment Plan, Deployment Task, Verification Task, Drill Task, Station, Train)
- Module Package / Product Package rename ripples across many documents
- Change Request complexity increases (but this reflects actual regulatory requirements)

## Entity Summary

| Entity | Model | Layer | Entity File |
|---|---|---|---|
| Module Package (spec) | Definition Model, Dim 7 | `dim7-module-package.md` |
| Product Package (spec) | Definition Model, Dim 7 | `dim7-product-package.md` |
| Deployment Train | Definition Model, Dim 7 | `dim7-deployment-train.md` |
| Station | Definition Model, Dim 7 | `dim7-station.md` |
| Deployment Plan | Work Model, Track 3 | `track3-deployment-plan.md` |
| Deployment Task | Work Model, Track 3 | `track3-deployment-task.md` |
| Verification Task | Work Model, Track 3 | `track3-verification-task.md` |
| Deployment Drill Task | Work Model, Track 3 | `track3-deployment-drill-task.md` |
| Module Package Version | Work Model, Track 3 (renamed) | `track3-module-package-version.md` |
| Product Package Version | Work Model, Track 3 (renamed) | `track3-product-package-version.md` |
| Deployment (artifact) | Work Model, Track 3 (refactored) | `track3-deployment.md` |
| Change Request (detailed) | Work Model, Track 3 (elevated) | `track3-change-request.md` |

---
