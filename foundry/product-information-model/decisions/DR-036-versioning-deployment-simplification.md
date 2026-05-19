# DR-036: Versioning and Deployment Simplification — Component/System/Product Version Chain, Deployment Specifications, Package Removal

**Status:** Accepted
**Date:** 2026-05-19

---

## Context

DR-035 redefined Dim 5: **Component** is the individually buildable deployable artifact; **System** is the operational deployment grouping of Components, versioned and deployed as a whole by SRE/ops. That amendment exposed a structural mismatch in the versioning and deployment model established by DR-026 through DR-029:

1. **Misaligned versioning tiers.** DR-026 introduced three tiers — System Version (atomic) → Module Version (integration-verified composition) → Product Version — when "System" meant the atomic deployable. Under DR-035, the atomic tier is **Component Version**; **System Version** must mean a sealed BOM of Component Versions for a Dim 5 System.

2. **Redundant middle tier.** Module Version existed to bridge individual System builds and Product certification. With Systems as sealed deployment units and Product Version composing System Versions directly, Module Version adds ceremony without a distinct operational artifact.

3. **Operator-facing package layers.** DR-027 and DR-029 introduced Module Package / Product Package (Dim 7 specifications + Track 3 versions) and MDD/PDD as separate operator-facing composition layers atop Module Version. SRE operational Systems are legitimate Dim 5 Systems (DR-035, DR-027); they belong in the same Build Track versioning chain as product Systems, not in a parallel Package entity.

4. **Descriptor proliferation.** SDD, MDD, and PDD (DR-028) mirrored the three composition levels. With Module Package and MDD removed, deployment specifications collapse to **System Deployment Specification** (per System Version, per environment) and **Product Deployment Specification** (composes System Deployment Specs for cross-System orchestration).

5. **Missing Product-level composition spec.** No Definition Model entity declared which Systems constitute a Product. Module boundaries (Dim 8) do not define deployment topology — a Product may span many Systems across many Modules with equal structural standing.

6. **Dim 7 scope creep.** Module Package and Product Package entities placed composition templates in Dim 7 alongside runtime operational entities (Deployment Environment, Deployment Train, Station). Dim 7 should retain runtime and governance concerns only.

This decision set resolves the post-DR-035 versioning and deployment model in one coherent pass.

---

## Decisions

### D1: Component Version is the atomic build artifact

**Decision:** **Component Version** is the versioned, quality-gated output of building a single Component (Dim 5) — the atomic build artifact (container image, Lambda package, frontend bundle, etc.). It replaces the semantic role previously assigned to "System Version" in DR-026 (when System meant atomic deployable).

**Rationale:** DR-035 anchors atomic deployability at Component. CI/CD pipelines produce Component Versions; they are the inputs to System assembly, not independently deployed to production.

---

### D2: System Version is a sealed immutable BOM of Component Versions

**Decision:** **System Version** is a sealed, immutable Bill of Materials (BOM) of specific Component Versions that constitute one Dim 5 System. System assembly work verifies Component integration within the System boundary. System Versions are produced by the **Build Track** (engineers and SREs building operational Systems alike).

**Rationale:** SRE/ops deploy Systems as wholes. A System Version is the auditable, immutable answer to "what Component Versions are running in this System instance?" Sealing prevents drift between declared and deployed composition.

---

### D3: Product Version composes System Versions directly

**Decision:** **Product Version** is a certified composition (BOM) of specific System Versions. There is no Module Version tier. Cross-System integration verification occurs at Product Version assembly (and via Integration Epics/Stories scoped appropriately).

**Rationale:** Module Version existed to manage O(n²) integration at Module scope. With Systems as the deployment unit and Product Specification declaring all Systems (D4), Product Version is the natural integration-verification boundary for cross-System behavior. Removing Module Version eliminates a tier that duplicated communication-bridge roles now served by System Version (within-System) and Product Version (cross-System).

---

### D4: Product Specification is a new Dim 5 entity

**Decision:** Introduce **Product Specification** as a Definition Model entity in Dim 5. It has a 1:1 relationship with Product (Dim 8) and declares all Systems that constitute the Product — product-serving and SRE operational Systems alike.

**Rationale:** Deployment topology and System membership are product-architecture concerns, not Module-boundary concerns. A Product Specification is the stable template; Product Version is the versioned, verified instance produced by Build Track work.

---

### D5: System Deployment Specification replaces SDD

**Decision:** **System Deployment Specification** replaces the System Deployment Descriptor (SDD). It is the environment-specific deployment specification for a single System Version (resource limits, replicas, env vars, runtime mappings, deployment scripts at System scope).

**Rationale:** Renaming aligns vocabulary with DR-035 System semantics and drops the "Descriptor" suffix in favor of "Specification," consistent with Product Deployment Specification (D6).

---

### D6: Product Deployment Specification replaces PDD

**Decision:** **Product Deployment Specification** replaces the Product Deployment Descriptor (PDD). It composes System Deployment Specifications by reference, adds product-level cross-System environment configuration, deployment ordering, and product-level deployment scripts.

**Rationale:** Product-level deployment coordination remains necessary; it no longer composes MDDs because Module Package and MDD are removed (D7, D8).

---

### D7: Remove Module Package Spec/Version and Product Package Spec/Version

**Decision:** Remove the following entities from the model:
- Module Package (Dim 7 specification)
- Module Package Version (Work Model artifact)
- Product Package (Dim 7 specification)
- Product Package Version (Work Model artifact)

SRE operational Systems are declared in Product Specification (D4) and versioned through the same Component Version → System Version → Product Version chain (D10).

**Rationale:** Package entities duplicated composition already expressible as Systems in Dim 5. Operator-facing probes, reconcilers, and dashboards are Systems with operational Purpose — they receive Component and System Versions like any other System, not a parallel Package layer.

---

### D8: MDD removed

**Decision:** Remove the Module Deployment Descriptor (MDD). Environment-specific deployment at integrated scope is expressed only through System Deployment Specifications (per System) and Product Deployment Specification (cross-System orchestration).

**Rationale:** MDD existed to deploy Module Package Versions. With Packages removed, there is no integrated deployable between System and Product that requires a separate deployment specification tier.

---

### D9: All Systems are equal in Product Specification

**Decision:** In Product Specification, all declared Systems have equal structural standing. **Purpose** and **Serving Persona** attributes distinguish product-serving Systems from SRE operational Systems — not a separate entity type or Package layer.

**Rationale:** Structural equality keeps the Product Specification a single authoritative System catalog. Purpose/Persona carry the semantic distinction without inventing hierarchy or secondary composition entities.

---

### D10: Build Track produces all System Versions

**Decision:** The Build Track produces System Versions for **all** Systems in Product Specification — including SRE operational Systems (probes, reconcilers, dashboards, log shippers). Run Track engineering work (Run Epics, Run Stories, Run Technical Tasks) feeds the same versioning chain; it does not produce Package Versions.

**Rationale:** DR-027 correctly identified operational Systems as legitimate Dim 5 Systems with code and CI/CD. The error was routing their versions through a parallel Package artifact. One Build Track, one versioning chain, preserves traceability from deployment back to build artifacts.

---

### D11: Change Request scopes to System Deployment or Product Deployment

**Decision:** A **Change Request** references either a **System Deployment** (application of a System Deployment Specification to an environment) or a **Product Deployment** (application of a Product Deployment Specification). The Change Request type taxonomy reflects this binary scope.

**Rationale:** With MDD and Package-level deployments removed, change management aligns to the two remaining deployment granularities: single-System changes and coordinated multi-System product changes.

---

### D12: Capability availability follows System → System Version in Product Version BOM

**Decision:** Capability availability in a deployed Product is determined by tracing: **Capability** (Dim 8) → realizing **System(s)** (Dim 5) → **System Version** in the Product Version BOM → deployed via System Deployment Specification.

**Rationale:** Capabilities map to Systems (DR-035 D12). Availability is a property of which System Versions are in the certified Product Version composition, not of a removed Module Version or Module Package layer.

---

### D13: Dim 7 retains runtime concerns only; no Package entities

**Decision:** Dimension 7 retains runtime, environment, and governance entities (Deployment Environment, Deployment Train, Station, Cluster, Host, etc.). No Package specification entities remain in Dim 7.

**Rationale:** Separating composition templates (now Product Specification in Dim 5) from runtime topology (Dim 7) restores a clean Definition Model boundary. Dim 7 answers "where and how governed execution happens," not "what Systems constitute the product."

---

## Rationale (Grouped)

**Why remove Module Version rather than rename it?**
Under DR-035, System Version is the sealed deployment BOM. Module Version's integration-verification role splits naturally: within-System integration is System assembly; cross-System integration is Product Version assembly. Keeping Module Version would preserve a tier whose deployable artifact (Module Package) is also removed.

**Why collapse deployment specs to two tiers?**
Deployment specifications mirror deployable granularity. Atomic deployment is System-scoped (System Version + System Deployment Specification). Coordinated multi-System deployment is Product-scoped (Product Version + Product Deployment Specification). No intermediate integrated deployable exists after Package removal.

**Why Product Specification in Dim 5?**
Product Specification declares Systems — Dim 5 entities. It is architect-authored (alongside PSD technical mapping per DR-035) and stable across Product Versions. Placing it in Dim 8 would conflate commercial product definition with technical System topology.

**Why one Build Track for SRE Systems?**
Operational Systems are code with repos and pipelines. Separating their versions into Run Track Packages created dual traceability paths and implied Run Track "builds" what Build Track "composes." A single chain preserves DR-035's operational reality: everything deployable is a System Version.

---

## Consequences

**Positive:**
- Versioning chain aligns with DR-035 Dim 5 semantics: Component Version → System Version → Product Version
- Eliminates Module Version, Module Package, Product Package, and MDD — reducing entity count and documentation ambiguity
- Product Specification provides a single authoritative System catalog per Product
- SRE operational Systems participate in the same build/deploy traceability as product Systems
- Dim 7 scope is narrowed to runtime and governance; composition moves to Dim 5
- Change Request scope is simplified to System-level or Product-level deployment
- Capability availability traceability is direct: Capability → System → System Version in BOM

**Negative:**
- DR-004, DR-026, DR-027, DR-028, and DR-029 require amendment; substantial narrative and entity files still reference Module Version, Packages, and MDD/SDD/PDD vocabulary
- Organizations with tooling built around Module Version / Module Package / MDD must migrate to System Version / Product Specification / System Deployment Specification
- Product Version assembly absorbs cross-System integration verification previously scoped to Module Version — may increase Product Version verification cost for very large products unless Integration Epics provide intermediate checkpoints
- DR-035 deferred note ("rename System Version → Component Version") is now executed — all DR-026 "System Version = atomic" references must be re-read as Component Version

**Migration notes:**
- `track2-system-version.md` → Component Version semantics; new System Version entity for sealed BOM
- Deployment descriptor entity files (SDD, MDD, PDD) → System Deployment Specification, Product Deployment Specification; MDD deleted
- Dim 7 Module Package / Product Package entity files → removed; Product Specification added to Dim 5
- Stories `versioning-alternatives-analysis.md`, `deployment-artifacts-analysis.md`, `change-to-deployment-analysis.md` were updated in the DR-036 pass; Track 3 entity files, draft references, and narrative seeds require follow-on consistency updates (see `1.TODO`)

---

## Amended Records

| Record | Amendment |
|---|---|
| DR-026 | S5 (System Version as atomic unit), S6 (three-tier versioning), S7 (Module Version), and work-artifact taxonomy superseded by D1–D3, D10 of this record; DR-035 note on semantic rename fulfilled |
| DR-027 | C1–C4 (composition levels via Module/Product Package), C3/C4 Package artifacts, and Run Track Package production superseded by D3, D7, D9, D10; operational Systems remain valid, versioning path changed |
| DR-028 | D1 (SDD) superseded by D5; D2 (MDD) removed per D8; D3 (PDD) superseded by D6; D4 (Package environment-independence) moot — Packages removed per D7 |
| DR-029 | D1–D3 (Module/Product Package spec and versions in Dim 7 / Track 3) superseded by D4, D7, D13; Change Request and deployment workflow decisions amended by D11 to System Deployment / Product Deployment scope |
