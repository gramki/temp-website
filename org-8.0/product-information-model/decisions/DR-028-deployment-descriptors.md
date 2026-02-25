# DR-028: Deployment Descriptors — SDD, MDD, PDD

**Status:** Accepted (refined by DR-029)
**Date:** 2026-02-15
**Related FAQ:** Q96
**Refined by:** DR-029 — Deployment refactored from work entity to work artifact; Deployment Task introduced as the work entity; descriptors now reference Module Package Version / Product Package Version (renamed from Module Package / Product Package)

## Context

After the introduction of Module Package and Product Package (DR-027), the model conflated two concerns in a single entity:

1. **The deployable composition** (environment-independent): which systems and operational wiring constitute the deployment unit.
2. **The deployment specification** (environment-specific): how that composition is deployed to a specific environment — resource sizing, monitoring thresholds, deployment scripts, target environment.

Module Package and Product Package carried environment-specific fields (`Target Environment(s)`, `Operational Configuration`) and an environment-dependent lifecycle status (`Deployed`). This created several problems:

- **Version confusion:** A monitoring threshold change in production-latam was not a Module Package change (no new operational systems, no new wiring), but the model had no separate entity to version deployment configuration independently.
- **Environment coupling:** A single Module Package targeting production-latam could not be reused for production-us without creating a separate Module Package, even though the composition (systems + wiring) was identical.
- **Missing deployment logic:** Pre-rollout scripts (database migrations), validation scripts (health checks), and rollback scripts (state restoration) had no structured home. They existed alongside deployments, not within a versioned specification.
- **Atomic level gap:** System Versions were deployed directly, with no corresponding specification entity for their environment-specific configuration. Environment-specific values were applied ad-hoc during deployment.

## Decisions

### D1: Introduce System Deployment Descriptor (SDD)

**Decision:** Introduce SDD as an environment-specific deployment specification for a single System Version. SDD maps to runtime-defined artifacts (K8s resources, cloud-native primitives) and has its own version reflecting deployment progression.

**Rationale:** Every deployable needs a corresponding deployment descriptor. System Versions are the atomic deployment unit — their environment-specific configuration (resource limits, replicas, network policies, environment variables) needs a versioned, structured home. SDDs are composed by reference into MDDs, providing the atomic building blocks for integrated deployment specifications.

### D2: Introduce Module Deployment Descriptor (MDD)

**Decision:** Introduce MDD as an environment-specific deployment specification for a Module Package. MDD composes SDDs by reference, adds Module-level environment configuration, and includes pre-rollout/validation/rollback scripts. MDD has its own version (deployment progression), independent of Module Version and Module Package version. Multiple MDDs per environment are valid.

**Rationale:** The MDD is the integrated deployment specification — it captures everything needed to deploy a Module Package to a specific environment as a coordinated unit. By separating this from Module Package, the model achieves: (a) independent versioning of deployment configuration, (b) environment-independent Module Packages reusable across environments, (c) a structured home for deployment scripts as first-class artifacts, (d) support for multiple deployment configurations in the same environment (fault isolation, service quality differentiation).

### D3: Introduce Product Deployment Descriptor (PDD)

**Decision:** Introduce PDD as an environment-specific deployment specification for a Product Package. PDD composes MDDs by reference, adds product-level cross-module environment configuration, defines deployment ordering, and includes product-level deployment scripts. PDD has its own version.

**Rationale:** Mirrors MDD at the product level. Cross-module deployment coordination (ordering, product-wide health verification, coordinated rollback) needs a specification entity that is environment-specific and independently versioned.

### D4: Refactor Module Package and Product Package to Environment-Independent

**Decision:** Remove environment-specific fields from Module Package (`Target Environment(s)`, `Operational Configuration`) and Product Package (`Target Environment(s)`). Remove the `Deployed` status. Module Package and Product Package become environment-independent artifacts that define *what* is deployed; deployment descriptors define *how* and *where*.

**Rationale:** Clean separation of concerns. The deployable composition (systems + wiring) does not change per environment — only the deployment specification does. Making packages environment-independent enables a single Module Package to be deployed to multiple environments via different MDDs without duplication.

### D5: Deployment Applies Descriptors

**Decision:** Update the Deployment entity to apply descriptor versions (SDD, MDD, PDD) instead of referencing deployable artifacts (System Version, Module Package, Product Package) directly. The deployable artifact is referenced indirectly through the descriptor.

**Rationale:** Deployment is the act of applying a specification to an environment. The specification (descriptor) contains the environment-specific configuration, scripts, and artifact references. Deploying "payments-service v2.3.3 to production-latam" is operationally "applying SDD v1.2 to production-latam" — the SDD contains the System Version reference plus all environment-specific deployment details.

### D6: Deployment Planning Task Produces Descriptors

**Decision:** Elevate Deployment Planning Task from a skeletal entity to a detailed entity that **produces** SDD/MDD/PDD versions. Scripts within descriptors (pre-rollout, validation, rollback) are engineering work performed as sub-tasks.

**Rationale:** Deployment descriptors do not materialize from thin air. They are the output of explicit planning work — environment configuration, script authoring, risk assessment, change management review. Making this relationship explicit connects the planning work to the produced artifact.

### D7: Operating Model Determines Change Management Unit

**Decision:** The Operating Model determines whether SDD (atomic) or MDD (integrated) is the logical unit for change management in a given organization. Both are supported by the information model.

**Rationale:** Organizations differ in their change management granularity. Some review and approve each System deployment independently (SDD-centric). Others review and approve at the Module level (MDD-centric). The model should not prescribe the operating model — it should support both.

## Consequences

**Positive:**
- Clean four-layer separation: Build artifact → Run artifact → Deployment descriptor → Deployment act
- Three independent version streams at the integrated level (Module Version, Module Package, MDD)
- Environment-independent Module Package and Product Package — reusable across environments
- Deployment scripts (migrations, health checks, rollback) are first-class versioned artifacts within descriptors
- Multiple MDDs per environment support fault isolation, service quality differentiation, and deployment staging
- Full audit trail: Deployment → Descriptor version → Package version → Build artifact version → Code

**Negative:**
- Three new entity types increase model complexity
- Tooling investment required for descriptor assembly, composition validation, and version management
- Three independent version streams require clear naming conventions and governance
- Learning curve for distinguishing Module Package (what) from MDD (how/where)
- Descriptor maintenance overhead — each environment-specific change requires an MDD version bump

**Updates to existing decisions:**
- DR-027 is refined (not superseded) — Module Package and Product Package remain as defined, but are now environment-independent; deployment-specific concerns move to SDD/MDD/PDD
- DR-026 S16 is further refined — deployment at the atomic level now applies SDDs, not System Versions directly

---
