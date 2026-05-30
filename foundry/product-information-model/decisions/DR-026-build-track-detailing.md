> **📌 Note (DR-035, 2026-05-19):** In the new Technical model (DR-035), the atomic deployable artifact is a **Component** (not a System). This means the "System Version" construct in this DR — which was defined as the atomic build artifact for a single deployable — logically maps to what should be called "Component Version." The System is now the operational deployment grouping of Components. The versioning model rename (System Version → Component Version) is deferred to **DR-036** to avoid scope expansion. References to "System Version" in this DR should be read with this context in mind.

# DR-026: Build Track Detailing — Work Entity/Artifact Distinction, Scoping Corrections, Three-Tier Versioning

> **Superseded for operational use by DR-036 (2026-05-19).** Module Version, Module/Product Package, and SDD/MDD/PDD are retired. See DR-036 and Amended Records table in DR-036.

**Status:** Accepted
**Date:** 2026-02-15

## Context

Build had 10 skeletal entity files with minimal detail. During the detailing session, several structural issues were identified:

1. **Work entities and work artifacts were conflated.** Module Version and Product Version were listed alongside Epics and Stories as "build entities," but they are fundamentally different: Epics are *work to be done*; Module Versions are *things produced by work*. This conflation obscured the Build Track's structure.

2. **Scoping was incorrect.** Epics and Stories were not explicitly scoped. In practice, PMs plan Epics at the Module level (Structural — functional boundary) while developers implement Technical Tasks at the System level (Technical — technical boundary). The original skeletal files did not capture this distinction.

3. **The versioning model was incomplete.** "Module Version" was misnamed — the Build Track builds Systems (Technical), not Modules (Structural). `payments-service v2.3.3` is a System Version, not a Module Version. The gap between individual System Versions and Product Version (no integration verification layer) was also unaddressed.

4. **Integration work was invisible.** Cross-System integration work had no dedicated entities — it was assumed to be part of regular Epics, hiding it from planning and tracking.

5. **Build Track ADR production had no mechanism.** DR-024 established that ADRs can originate from Build Track work, but no entity existed to model the process.

## Decisions

### S1: Work Entity vs. Work Artifact Distinction

**Decision:** Classify Build Track entities into two categories: *work entities* (work to be done — Epic, Story, Technical Task, Bug, Integration Epic, Integration Story) and *work artifacts* (things produced by work — System Version, Module Version, Product Version, ADR, Technical Debt Item).

**Rationale:** Work entities have assignees, sprints, and status lifecycles driven by human effort. Work artifacts emerge from completed work and have quality-gated lifecycles. Conflating them obscures what the Build Track actually does.

### S2: Epic = Module Scope (Structural)

**Decision:** Epics are scoped to a single Module (Structural), decomposed from a PSD. A cross-Module PSD produces multiple Epics — one per affected Module.

**Rationale:** PMs and Tech Leads plan at the Module level ("Build the FX Rate Locking feature for the FX Module"). Module scope keeps Epics accessible to product stakeholders while deferring technical decomposition to Technical Tasks.

### S3: Story = Module Scope (Structural), Renamed from User Story

**Decision:** Rename "User Story" to "Story." Stories are Module-scoped, inheriting from their parent Epic. Stories are not necessarily user-facing — they may be technical or enablement Stories.

**Rationale:** "User Story" implies user-facing work. Many Stories are infrastructure, data migration, or technical enablement — calling them "User Stories" is misleading. "Story" is the more general term.

### S4: Technical Task = System/Component Scope (Technical)

**Decision:** Technical Tasks are scoped to a specific System (Technical) and optionally a Component. They serve both regular Stories and Integration Stories.

**Rationale:** Developers work on Systems, not Modules. "Implement gRPC endpoint in fx-service" is how engineering work is actually assigned. Technical Tasks bridge the functional intent (Stories, Module-scoped) to technical implementation (Systems, Technical).

### S5: System Version (Renamed from Module Version)

**Decision:** Rename the original "Module Version" to "System Version." System Version is a versioned, quality-gated artifact of a single System (Technical) — the atomic deployment unit.

**Rationale:** The Build Track builds Systems, not Modules. Engineers produce `payments-service v2.3.3` (a System Version), not "Payments Module v2.3.3." The Run Track deploys System Versions to environments.

### S6: Three-Tier Versioning Model

**Decision:** Establish a three-tier versioning model: System Version (atomic deployment unit) → Module Version (integrated deployment + integration verification unit) → Product Version (complete deployment + certification unit). Each tier is a **composite system** with emergent operational properties at its composition level, a **deployable** at its composition granularity, and a **communication bridge** at progressively broader organizational scope.

**Rationale:** The original two-tier model (Module Version → Product Version) missed the integration verification layer. In reality, individual Systems are built and deployed independently (System Versions), then verified to work together within a Module boundary (Module Versions), then the full product composition is certified (Product Version). DR-004 ("Three-Layer Versioning") described Module Version → Product Version → Customer Release — the artifact tiers are now System Version → Module Version → Product Version, with DR-038 clarifying the strategy-layer business delivery entity as Customer Release Intent.

Beyond verification scope, each tier fulfills two additional roles. First, **each tier is a system in its own right** — Module Version has emergent properties (end-to-end latency, integrated failure modes, cross-system data consistency) that do not exist at the individual System level; Product Version has product-level emergent properties (end-to-end user journeys, cross-module workflows, product-wide compliance posture). All tiers are operable and observable. Second, **each tier provides shared vocabulary** at a different organizational scope: System Version is Build+Run language; Module Version bridges Build+Run+Product (PMs, SREs, and engineers all reference "Payments Module v4.1"); Product Version is the ubiquitous language across all teams and customers. See `stories/versioning-alternatives-analysis.md` for how alternative approaches address these challenges.

**Consequences:** DR-004 is partially superseded by this decision. The three layers remain, but the bottom tier is now System Version (not Module Version), and the middle tier is now Module Version (integration-verified composition, not deployable artifact).

### S7: Module Version as Composite System and Integration Artifact

**Decision:** Introduce a new "Module Version" entity as a **composite system** — an integration-verified composition of System Versions for a Module (Structural). Contains integration contracts and integration test suites. Has emergent operational properties and serves as the shared vocabulary between Build, Run, and Product teams.

**Rationale:** Product Version cannot verify all Systems at once — that's an O(n²) integration problem. Module Version provides Module-scoped integration verification: "do the Systems implementing the Payments Module work together?" This is verified before Product Version certification. Module Version also provides a shared reference point that Build, Run, and Product teams can all use — without it, PMs say "the Payments capability," engineers say "payments-service v2.3.3," and SREs translate between the two ad hoc.

### S8: Integration Epic and Integration Story as Separate Entities

**Decision:** Introduce Integration Epic and Integration Story as distinct entities, separate from regular Epics and Stories.

**Rationale:** Integration work has fundamentally different characteristics from feature work: it spans multiple Systems (potentially from different Modules), validates Interaction Flows (Technical), and produces integration contracts and test suites. Conflating integration work into feature Epics hides cross-cutting work from planning. Integration Epics reference the PSD-derived Epics they integrate.

### S9: Design Deliberation

**Decision:** Introduce Design Deliberation as the Build Track's mechanism for producing ADRs.

**Rationale:** DR-024 established ADR dual provenance (Discovery + Build) but provided no Build Track entity for it. Design Deliberation is the tactical counterpart to Discovery Track's Deliberation — focused on implementation-time architectural questions ("gRPC vs REST for this service call?"). It makes architectural decision-making during build work explicit and traceable.

### S10: Technical Debt Item

**Decision:** Introduce Technical Debt Item as a work artifact documenting accumulated debt. When prioritized, resolved via an Epic or Story.

**Rationale:** Technical debt accumulates silently during development. Making it a documented artifact (not a work entity) means debt is visible and can compete with features for sprint capacity. Resolution happens through existing work entities (Epic, Story), not a separate mechanism.

### S11: Bug Provenance

**Decision:** Add a provenance field to Bug: `Build` / `Run` / `Win`.

**Rationale:** Bugs originate from three sources: discovered during development (Build), escalated from production Incidents (Run), or surfaced from customer complaints/Win Cases (Win). Provenance enables cross-Track traceability and root cause analysis patterns.

### S12: System Version Quality Gates Feed Operational Readiness

**Decision:** System Version quality gate results (test coverage, security scan, performance benchmarks) feed Operational Readiness (Operational) assessments.

**Rationale:** Operational Readiness assesses whether a System is production-ready in a given environment. Build Track quality gate data is a key input — if a System Version was released with security warnings, Operational Readiness should reflect that. Operational Readiness is per-System × per-Environment (not per-Module), because the Run Track operates Systems: SREs deploy, monitor, and write runbooks for `payments-service`, not "the Payments Module." Module-level readiness is a derived aggregation.

### S13: Release Planning Identifies Integration Epics

**Decision:** Release Planning Task is responsible for identifying Integration Epics alongside PSD-derived Epics.

**Rationale:** Integration work must be identified early during release planning, not discovered mid-sprint. When Release Planning decomposes PSDs into Epics across Modules, it naturally surfaces cross-System integration needs.

### S14: Milestone Planning Includes Integration Verification Gates

**Decision:** Milestone Planning includes cross-Epic dependency gating and integration verification gates (where Module Versions must be verified).

**Rationale:** Milestones need to gate not just feature completion (Epics) but integration verification (Module Versions). "API Complete" milestone should require both feature Epics done and Payments↔FX integration verified.

### S15: Iteration Planning Assigns Stories, Integration Stories, and Technical Tasks

**Decision:** Iteration Planning explicitly assigns Stories, Integration Stories, and Technical Tasks to sprints.

**Rationale:** Sprint planning operates at the intersection of Module-scoped Stories and System-scoped Technical Tasks. Integration Stories have the same sprint-level assignment needs as regular Stories.

### S16: Deployment Deploys System Versions (Not Module Versions)

> **Refined by DR-027 (C2, C3, C4).** This decision established System Version as the deployment unit. DR-027 refined this to recognize three deployment levels: System Version is the **atomic** deployment unit, Module Package is the **integrated** deployment unit, and Product Package is the **complete** deployment unit. All three are deployable. S16's intent (deploy Systems, not Modules-as-functional-boundaries) remains valid, but the Run Track also deploys composed artifacts at integrated and complete levels.

**Decision:** The Run Track's Deployment entity deploys System Versions, not Module Versions. All "Module Version" references in Run Track entities are updated to "System Version."

**Rationale:** You deploy Systems (deployable technical units), not Modules (functional boundaries). `payments-service v2.3.3` is deployed to production-us — `Payments Module v2.3.0` is an integration verification artifact, not a deployment unit.

## Consequences

**Positive:**
- Clear distinction between work to do (entities) and work produced (artifacts)
- Accurate scoping: PMs plan in Module terms; developers implement in System terms
- Three-tier versioning reflects actual deployment, integration, and certification units
- Integration work is visible and plannable from release planning onward
- Build Track ADR production has a named mechanism (Design Deliberation)
- Technical debt is visible in the model

**Negative:**
- More entities to manage (5 new entities: Integration Epic, Integration Story, Design Deliberation, Technical Debt Item, Module Version)
- DR-004 is partially superseded — the three layers have shifted
- All "Module Version" references in existing documents need updating to "System Version" where the old meaning applies

---
