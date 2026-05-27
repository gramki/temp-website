---
name: Deployment Descriptors Refactor
overview: Introduce SDD, MDD, and PDD as environment-specific deployment specification entities; refactor Module Package and Product Package to be environment-independent artifacts; update Deployment and Deployment Planning Task entities; create a dedicated deployment artifacts analysis document; and update all referencing documents.
todos:
  - id: create-sdd-mdd-pdd
    content: Create track3-sdd.md, track3-mdd.md, track3-pdd.md entity files
    status: completed
  - id: refactor-packages
    content: Refactor track3-module-package.md and track3-product-package.md to be environment-independent
    status: completed
  - id: update-deployment-entities
    content: Update track3-deployment.md and track3-deployment-planning-task.md to reference descriptors
    status: completed
  - id: create-analysis-doc
    content: Create deployment-artifacts-analysis.md (dedicated analysis document with rationale, guide, pros/cons, dos/donts)
    status: completed
  - id: create-dr028
    content: Create DR-028 decision record for deployment descriptor introduction
    status: completed
  - id: update-summaries
    content: Update draft-work-model.md, draft-work-execution-framework.md, entities/README.md, narrative-seeds.md
    status: completed
  - id: update-crossrefs
    content: Update cross-references in dim1-customer-release.md, dim7-deployment-environment.md, dim7-operational-readiness.md, draft-definition-model.md, versioning-alternatives-analysis.md, 1.TODO
    status: completed
  - id: review-consistency
    content: Review all changes for consistency and completeness — verify bidirectional relationships, terminology alignment, no stale references, and cross-document coherence
    status: completed
isProject: false
---

# Deployment Descriptors: SDD, MDD, PDD

## Context

Discussion identified that Module Package and Product Package currently conflate the deployable artifact with the deployment specification (environment-specific config, target environments). The fix introduces a clean separation:

- **Module Package / Product Package** become environment-independent artifacts (enrichment of build artifacts with operational systems and wiring)
- **SDD / MDD / PDD** are new environment-specific deployment specification entities that describe *what is deployed where and how*
- **Deployment** (the act) references MDD/PDD versions instead of Module Package/Product Package directly

## Changes

### 1. Create new entity files (3 files)

`**track3-sdd.md**` (System Deployment Descriptor)

- Definition: Environment-specific deployment specification for a single System Version. Maps to one or more runtime-defined artifacts with platform-specific names (K8s Service, Pod spec, Deployment, CRDs, Helm releases, etc.).
- Fields: System Version reference, environment-specific config (resource limits, replicas, env vars), runtime artifact references
- Composed by reference into MDD
- Has its own version (deployment progression, not functional)

`**track3-mdd.md**` (Module Deployment Descriptor)

- Definition: Environment-specific deployment specification for a Module Package in a specific environment. Composes SDDs by reference + Module-level environment config + pre-rollout/validation/rollback scripts and applications. A "system" in its own right.
- Fields: Module Package reference, SDDs (by reference), environment-specific config (monitoring thresholds, scaling policies, probe schedules), pre-rollout scripts, validation scripts, rollback scripts, target environment
- Has its own version (deployment progression, independent from Module Version and Module Package version)
- Multiple MDDs per environment are valid (fault isolation, service quality differentiation, deployment stage, product-level isolation)
- Produced by Deployment Planning Task (scripts/applications are sub-tasks)

`**track3-pdd.md**` (Product Deployment Descriptor)

- Definition: Environment-specific deployment specification for a Product Package. Composes MDDs by reference + product-level cross-module environment config + product-level deployment scripts.
- Fields: Product Package reference, MDDs (by reference), cross-module environment config, product-level deployment scripts, target environment
- Has its own version

### 2. Refactor Module Package (`track3-module-package.md`)

- Remove `Target Environment(s)` field
- Remove `Operational Configuration` field (environment-specific values)
- Keep: Module Version reference, Operational System Versions, Binding Configuration (Operational) — all environment-independent
- Update definition text to clarify environment-independence
- Remove `Deployed` status (that belongs to MDD now). Lifecycle: `Assembling` -> `Ready`
- Update relationships: add `Described by | MDD (Track 3)`, remove `Targets | Deployment Environment(s)`
- Rework examples to be environment-independent

### 3. Refactor Product Package (`track3-product-package.md`)

- Same treatment: remove `Target Environment(s)`, remove environment-specific cross-module config
- Keep: Product Version reference, Module Packages, environment-independent cross-module operational wiring
- Remove `Deployed` status. Lifecycle: `Assembling` -> `Ready`
- Update relationships: add `Described by | PDD (Track 3)`, remove `Targets | Deployment Environment(s)`
- Rework examples

### 4. Update Deployment entity (`track3-deployment.md`)

- Update `Deployable` field to reference SDD/MDD/PDD versions instead of System Version/Module Package/Product Package directly
- Update relationships: `Applies | SDD Version`, `Applies | MDD Version`, `Applies | PDD Version`
- Update examples to show deployment of MDD/PDD versions

### 5. Update Deployment Planning Task (`track3-deployment-planning-task.md`)

- Elevate from skeletal to detailed: this entity now **produces** MDD/PDD versions
- Add proper Fields: Module Package/Product Package reference, target environment, deployment strategy, compliance windows, pre-rollout/validation/rollback scripts
- Add Statuses: `Planning` -> `Descriptor Ready` -> `Approved` -> `Executing`
- Update Relationships: `Produces | MDD Version`, `Produces | PDD Version`; sub-tasks create/modify scripts and applications within the descriptor
- Note: Operating Model determines if SDD (atomic) or MDD (integrated) is the logical unit for change management

### 6. Create dedicated analysis document

`**deployment-artifacts-analysis.md**` (new file, peer to `versioning-alternatives-analysis.md`)

Structure (following the style of `versioning-alternatives-analysis.md`):

- **The Problem Being Solved** — the gap between "what is built" and "what is deployed"; environment-specific configuration, operational scripts, and deployment orchestration
- **The Four-Layer Model** — Build artifact -> Run artifact -> Deployment descriptor -> Deployment act, at each composition level
- **Three Independent Version Streams** — Module Version (functional), Module Package (operational enrichment), MDD (deployment progression)
- **SDD: Runtime-Specific Deployment Specification** — maps to K8s/cloud-native artifacts; platform-specific naming; composed by reference into MDD
- **MDD: The Integrated Deployment Specification** — composes SDDs, adds Module-level config, includes pre-rollout/validation/rollback scripts; is a "system" in its own right; multiple MDDs per environment
- **PDD: The Complete Deployment Specification** — composes MDDs, adds product-level cross-module deployment orchestration
- **Deployment Descriptors vs. Tenant Configuration** — tenant config is runtime-discovered, not deployment-time; the boundary between MDD and Tenant
- **Change Management Unit** — Operating Model determines SDD vs. MDD as the atomic unit of change approval
- **Pros and Cons** — clean separation of concerns, independent versioning, multi-environment reuse vs. more entities, tooling investment, assembly complexity
- **Dos and Don'ts for Run Track Participants** — practical guidance
- **Relationship to Existing Model** — how SDD/MDD/PDD relate to Module Version, Module Package, Deployment, Deployment Planning Task

### 7. Update summary/referencing documents

- `**draft-work-model.md**` — Update Run Track section: add SDD/MDD/PDD descriptions, update Module Package/Product Package descriptions (remove env-specific language), update Deployment description
- `**draft-work-execution-framework.md**` — Add SDD/MDD/PDD to Run Track cross-track inventory; update Module Package/Product Package/Deployment entries
- `**entities/README.md**` — Add `track3-sdd.md`, `track3-mdd.md`, `track3-pdd.md` to the entity catalog
- `**narrative-seeds.md**` — Add new narrative seeds: "Deployment Descriptors: the environment-specific specification layer", "MDD as a system: scripts, validation, and rollback", "Three independent version streams at the integrated level", "Tenant config vs. deployment config: the runtime boundary"
- `**DR-027**` or new `**DR-028**` — Record the decisions (MDD/PDD introduction, Module Package refactor, Deployment entity update, per-track change management unit). Given the scope, a new DR-028 is appropriate.
- `**decisions/README.md**` — Add DR-028
- `**1.TODO**` — Mark the Feature Flags item as resolved (reframed: entitlement toggles are Pricing Tier->Capability binding; ops toggles are operational config; release toggles are deployment workflow; mechanism is not a UPIM entity)

### 8. Update Definition Model cross-references

- `**dim1-customer-release.md**` — update "Deployed via | Product Package (Track 3)" to reference PDD; update Deployment Planning Task relationship to note it produces MDD/PDD versions
- `**dim7-deployment-environment.md**` — add relationships: `Targeted by | SDD / MDD / PDD (Track 3)` (deployment descriptors target specific environments)
- `**dim7-operational-readiness.md**` — add relationship: `Informs | MDD (Track 3)` (readiness status informs whether an MDD should be created for a given environment)
- `**versioning-alternatives-analysis.md**` — update the "Three Deployment Levels" section to reference SDD/MDD/PDD instead of direct Module Package/Product Package deployment; add a new section on the four-layer model
- `**draft-definition-model.md**` — if Dim 7 entity summaries reference deployment artifacts, update to reflect new descriptor entities

### 9. Review for consistency and completeness

After all changes are implemented, perform a systematic review:

- **Bidirectional relationships:** Verify every new entity (SDD, MDD, PDD) has matching reverse relationships on every entity it references (System Version, Module Package, Product Package, Deployment Environment, Deployment, Deployment Planning Task, etc.)
- **Stale references:** Search all files for outdated patterns — Module Package/Product Package described as environment-specific, "Target Environment" fields on Package entities, Deployment referencing packages directly instead of descriptors, "Deployed" status on Package entities
- **Terminology alignment:** Confirm "deployment descriptor" is used consistently across all documents; "deployment progression" for descriptor versioning; "environment-independent" for Module Package/Product Package; no conflation of "deployable artifact" with "deployment specification"
- **Internal consistency:** Verify narrative seeds, deployment-artifacts-analysis.md, and DR-028 are mutually consistent and aligned with entity files
- **Summary documents:** Check that draft-work-model.md, draft-work-execution-framework.md, and entities/README.md all reflect the new entities with accurate descriptions
- **No orphaned references:** Confirm no remaining references to old patterns (e.g., old "Deployed" status on Module Package, old "Targets | Deployment Environment" on Package entities, "Deployable | Module Package" on Deployment entity)
- **Cross-document coherence:** Verify that the four-layer model (Build artifact -> Run artifact -> Deployment descriptor -> Deployment act) is described consistently wherever it appears
