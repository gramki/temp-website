---
name: ontology revision round 2
overview: Apply the 50+ clarifications from the todo.md Q&A session to [olympus-ontology.md](/Users/ramki/Git/personal-projects/olympus-diagrams/olympus-ontology.md). This includes new entities (PDD, RRSD, APD, Hercules, zone-init-0), expanded Velos scope, Descriptor taxonomy, Tenant Subscription lifecycle split, and numerous precision fixes.
todos:
  - id: velos-scope-infra
    content: Update §1, §11 — Velos (World) creates Sites, Zones, Enclaves, Spaces; Zone-local Velos provides CSP resources. World SRE exclusivity. Zone containment.
    status: completed
  - id: csp-fixes
    content: Update §2 — DC strictly scoped to Zone; CSP Subscriptions/DCs created by World SRE; no preferred DC.
    status: completed
  - id: ds-fixes
    content: Update §3 — Service Catalog versioning at ZDD level; Velos provisions Service Accounts; DS decommissioning as archived descriptor.
    status: completed
  - id: spec-descriptors
    content: Update §4 — RRSD as first-class entity; Application Descriptor schema by kind; Module Spec must be in a Product; Subscription Questionnaire as Admin Space Application; MSD/PSD document names.
    status: completed
  - id: descriptor-taxonomy
    content: Add Descriptor Taxonomy subsection — classify all descriptor types (Specification, Deployment, Subscription, Policy, Schema); add versioning scheme (SemVer vs YYYYMMDD).
    status: completed
  - id: deployment-pdd
    content: Update §5 — Add PDD as first-class entity; MDD scope/content precision; PD in-place update semantics.
    status: completed
  - id: resources-velos
    content: Update §6 — Velos as CSP resource host/tagger; Consumer:RD 1:1; Resource GC by Resource Provider.
    status: completed
  - id: admin-constraints
    content: Update §7 — Exactly one Admin Enclave per Zone; Admin Space cannot span Enclaves; each OE module has own MD.
    status: completed
  - id: identity-fixes
    content: Update §8 — Multi-role Orgs not modeled; admission via World SRE; RBAC/OPA note; confirmed clarifications (cross-Landlord SRE, whitelist granularity, APD).
    status: completed
  - id: tenancy-lifecycle
    content: Update §9 — Tenant:TenantOrg 1:1; split inactive/terminated; APD as sub-component; TSD internal structure (Module Subscription Sections); PD pinning.
    status: completed
  - id: olympus-bootstrap
    content: Update §10 — Bootstrap sequence; zone-init-0; Zone-local Velos scope; Weave Store hub-spoke; OWP spawns all non-World infra.
    status: completed
  - id: estate-modules
    content: Update §11 — Add Hercules; Velos dual role (World vs Zone-local); zone-init-0; acknowledge other modules exist.
    status: completed
  - id: overlapping-identity
    content: Update §12 — Identity hierarchy is flat; PD->SRE is cross-axis join not a single hierarchy.
    status: completed
  - id: versioning-descriptors
    content: Update §13 — Descriptor versioning scheme (YYYYMMDD.count); PD version semantics; TS lifecycle split.
    status: completed
  - id: relationships-new-rows
    content: Update §14 — Add new relationship rows for PDD, ZDD, RRSD, APD, Module Subscription Section, Velos infrastructure creation.
    status: completed
  - id: glossary-runtime-descriptor
    content: Update §16 — Add Runtime abstract entity; add Descriptor abstract concept with taxonomy.
    status: completed
  - id: todo-update
    content: Update todo.md — Check off answered questions; add any new follow-ups.
    status: completed
isProject: false
---

# Ontology Revision Round 2

## A. New entities to introduce

### A1. Deployment Descriptors

- **Product Deployment Descriptor (PDD)** -- First-class entity. Created by SRE Org. Top-level descriptor for a Product Deployment in an Enclave. Composed of MDDs (one per Module). Currently the doc only has MDD; PDD is its parent.
- **Zone Deployment Descriptor (ZDD)** -- Created by World SRE Org. Specifies the constituent infrastructure components of a Zone. Versioning happens at ZDD level (YYYYMMDD format). Site Deployment Descriptor is equivalent at Site level.
- **Site Deployment Descriptor** -- Created by World SRE Org. Specifies a Site's infrastructure. Parent of ZDDs.
- **World Descriptor** -- Already in the doc but needs tightening: it is also a Deployment Descriptor (for the World including the Olympus World Product Deployment Descriptor). Add descriptor versioning scheme.

### A2. Specification Documents

- **RRSD (Resource Requirement Specification Document)** -- First-class entity. Published by a Resource Provider for each kind of resource it provides. Provides the schemas for RRD, RSD, and Resource Descriptor for that resource kind. Serves as a brochure. Registered with Olympus Estate. The RRSD schema format itself is published by Olympus Estate Product.
- Note: Module Specification Descriptor (MSD) is the document name for a Module Specification; Product Specification Descriptor (PSD) for a Product Specification. These are document representations, not renames -- the entity names remain "Module Specification" and "Product Specification".

### A3. Subscription / Policy Documents

- **Module Subscription Section** -- Structural sub-element within a TSD, 1:1 to Module Specifications in the Product. Contains the RSDs required by that module. Named "Section" (not "Descriptor") to avoid collision with "MSD" = Module Specification Descriptor.
- **Access Policy Descriptor (APD)** -- Sub-component of a Module Subscription Section. Authored by Landlord. Defines fine-grained access restrictions (which Enclaves, which Product Deployments) for a Tenant within an Estate. Finest grain: Product Deployment.

### A4. Runtimes

- **Hercules** -- An Olympus Estate module providing a runtime for serving web applications. Add as an entry in the Olympus Estate Modules table (alongside Atlantis, Velos, Weave, Elenchos). Details beyond this are out of scope.
- **Runtime** -- Define as an abstract entity in the Glossary. A collective term for any Module Deployment that can host Applications of certain kinds (Kubernetes/Atlantis for container-based, Hercules for web apps, Flink for streaming jobs, BPMN engines for workflows, etc.).

### A5. Bootstrap

- **zone-init-0** -- A bootstrap application within the Velos module of the Olympus World Product. Automates Zone bootstrap (analogous to how the Bootstrap Workstation bootstraps the World). Add to the bootstrap sequence in section 10.

## B. Corrections and precision fixes by section

### B1. Section 1 -- Infrastructure Hierarchy

- **Velos scope expansion**: Velos (in the World Deployment) creates Sites, Zones, Enclaves, AND Spaces -- not just Spaces and network routes. Update the intro paragraph and Zone entity definition.
- **World SRE Org exclusivity**: Creation of Sites, Zones, Spaces, and Enclaves is the exclusive prerogative of the World SRE Org, who creates Site and Zone Deployment Descriptors.
- **Zone containment**: State explicitly that a Zone is strictly contained within a single Site (cannot span Sites). No constraint on how many Zones a Site can have.

### B2. Section 2 -- CSP Hierarchy

- **DC scope**: State explicitly that a DC is strictly scoped to one Zone. Two Zones must not share any infrastructure.
- **CSP Subscription/DC creation**: Created by the World Owner (via World SRE Org).
- **No preferred DC**: Remove any implication of DC preference; the choice is operational.

### B3. Section 3 -- Deployment Space

- **Service Catalog versioning**: Versioning happens at ZDD level, not independently.
- **Service Account provisioning**: Velos provisions Service Accounts and assigns them to relevant workloads. Granularity decisions are coded into Velos (informed by Security, FinOps, etc.).
- **DS decommissioning**: A decommissioned Deployment Space exists as a Descriptor in archived state; infrastructure is fully decommissioned.

### B4. Section 4 -- Specification Hierarchy

- **Application Descriptor schema**: Each Application Descriptor adheres to the schema of the Application kind it represents. Individual schemas are beyond scope.
- **RRSD**: Add as a first-class entity. It provides the schemas for RRD, RSD, and Resource Descriptor. Published by each Resource Provider. RRSD schema format is published by Olympus Estate Product.
- **Module Spec containment**: A Module Specification cannot exist outside a Product Specification.
- **Operator placement**: No constraints -- Operators can be in any Module Spec within a Product.
- **Subscription Questionnaire**: It is an Application deployed to Admin Space; its runtime is one supported by OEP (Atlantis, Hercules, etc.).
- **Document names**: Note that the document representation of a Module Specification is called a Module Specification Descriptor (MSD), and of a Product Specification is a Product Specification Descriptor (PSD).

### B5. Section 5 -- Deployment Hierarchy

- **PDD**: Add Product Deployment Descriptor as parent of MDDs. Created by SRE Org.
- **MDD scope**: Strictly one MDD per (Module Specification, Enclave). Resources and some applications may be hosted by runtimes in other Enclaves.
- **MDD content**: Captures all rollout decisions, target spaces for each Deployment, compute/memory/storage allocations. Syntax is out of scope.
- **Product Deployment in-place update**: A PD is in-place updated. Blue-Green is at MDI level within a logical PD. Multiple PDs in an Enclave serve business isolation, not version promotion.

### B6. Section 6 -- Resources vs. Deployments

- **Velos as CSP resource host**: Velos is the provider/host of all CSP resources and enforces tagging. All tag semantics apply to CSP Resources.
- **Consumer to RD**: Semantically 1:1 (unique RD per consumer). Underlying physical resources may be shared at Resource Provider's discretion.
- **Resource garbage collection**: Responsibility of the Resource Provider. Each RP defines what happens to unused resources.

### B7. Section 7 -- Admin Enclave and Admin Space

- **Exactly one** Admin Enclave per Zone.
- Admin Space **cannot** span multiple Enclaves.
- Each Olympus Estate module has its **own** Module Deployment in Admin Enclave.

### B8. Section 8 -- World, Identity, and Organizations

- **Multi-role Orgs**: A real-world org can manifest as multiple Org roles; the ontology does not model the real-world org.
- **Admission gate**: World SRE Org is the only gate. Onboarding details out of scope.
- **Org attributes**: Kept out of scope for this version.
- **World Owner SRE Org policies**: RBAC with OPA-based fine-grained policies. Details out of scope.
- **Confirmed**: SRE Org cross-Landlord, Publisher/Landlord independence, Tenant whitelist at Estate level with APD for fine-grained control.

### B9. Section 9 -- Tenancy Hierarchy

- **Tenant : Tenant Org**: Strictly 1:1.
- **Multiple subscriptions to same PD**: Not supported (current version).
- **Lease termination**: Immediate. Resource Providers may have their own protective semantics (out of scope).
- **Suspended to active**: Manual, World SRE decision.
- **Lifecycle split**: Split current `inactive` into `inactive` (reversible, resources retained) and `terminated` (irreversible, resources released, reason codes). `archived` follows only `terminated`. `inactive` can transition back to `active`.
- **APD**: Sub-component of Module Subscription Section within TSD. Authored by Landlord.
- **TSD internal structure**: TSD contains Module Subscription Sections (1:1 to Module Specs in the Product Spec). Each section contains RSDs and APDs.
- **Tenant Subscription pinning**: Pinned to a Product Deployment, not to a version. PD is in-place updated.

### B10. Section 10 -- Olympus Products

- **Bootstrap sequence**: World SRE builds World Descriptor -> creates Workstation from pre-built image -> bootstrap programs spawn World Infrastructure (1 Site, 1 Zone, 1 Enclave, 1 Space, 2 DCs) -> deploy OWP modules in order: Velos, Atlantis, Weave, then others.
- **Zone bootstrap**: Automated via zone-init-0 (within Velos in the World deployment). Similar model to World bootstrap.
- **OWP and OEP relationship**: OWP is a specialized OEP deployment. All non-World OEP deployments are initiated through OWP by World SRE.
- **Weave Store**: Federated Hub-and-Spoke model. Edge repository per Zone is lazy-loaded and serves as a cache. Details out of scope.
- **Zone-local Velos**: Provides CSP resources required by Product Deployments and Tenant Subscriptions in the Zone (not infrastructure creation -- that's World Velos).

### B11. Section 11 -- Olympus Estate Modules

- **Velos role expansion**: In World Deployment, Velos creates Sites, Zones, Enclaves, Spaces. In Zone-local deployment, Velos provides CSP resources for PDs and Tenant Subscriptions.
- **Hercules**: Add as an Olympus Estate module -- runtime for web applications.
- **Other modules**: Acknowledge more exist but are out of scope ("etc.").
- **Zone bootstrap**: zone-init-0 application within Velos (World deployment).

### B12. Section 12 -- Overlapping Hierarchies

- **Identity hierarchy**: Flat set of Org roles; no containment between them. Detailed IDP roles out of scope.
- **Publisher -> Product Spec -> Product Deployment -> SRE Org**: Not a single hierarchy; PD -> SRE Org is a cross-axis join.

### B13. Section 13 -- Lifecycle and Versioning

- **Descriptor versioning**: All Deployment Descriptors use YYYYMMDD.change-count (not SemVer). SemVer is only for Module/Product Specifications.
- **PD version coexistence**: Multiple PDs serve business isolation, not version promotion. Tenant Subscription pinned to PD, not version. In-place update via Blue-Green at MDI level.
- **Resource lifecycle**: Remains ontology-specific.
- **Tenant Subscription lifecycle**: Update with `inactive` (reversible) and `terminated` (irreversible) split.

### B14. Section 16 -- Glossary

- **Runtime**: Abstract entity. A Module Deployment that can host Applications of certain kinds. Examples: Kubernetes/Atlantis (containers), Hercules (web apps), Flink, BPMN engines.
- **Descriptor**: Abstract concept with taxonomy. Categories: Specification Descriptors (Application Descriptor, Resource Descriptor, RRD, MSD, PSD), Deployment Descriptors (MDD, PDD, ZDD, Site Descriptor, World Descriptor), Subscription Descriptors (TSD with Module Subscription Sections), Policy Descriptors (APD), Schema Documents (RRSD).

## C. New Descriptor Taxonomy subsection

Add a subsection (in section 4 or as a new standalone section between 4 and 5) that classifies all Descriptors:

- **Specification Descriptors** -- Describe what can be deployed: Module Specification Descriptor (MSD), Product Specification Descriptor (PSD), Application Descriptor, Resource Descriptor, RRD, RRSD
- **Deployment Descriptors** -- Describe how to deploy: World Descriptor, Site Deployment Descriptor, Zone Deployment Descriptor (ZDD), Product Deployment Descriptor (PDD), Module Deployment Descriptor (MDD)
- **Subscription Descriptors** -- Describe tenant subscriptions: TSD (containing Module Subscription Sections with RSDs and APDs)
- **Policy Descriptors** -- Describe access policies: Access Policy Descriptor (APD)
- **Versioning**: Specification documents use SemVer. Deployment/Subscription/Policy descriptors use YYYYMMDD.change-count.

## D. Updates to Relationships Reference (section 14)

Add new rows for:

- PDD -> MDD (1:N, containment)
- PDD -> SRE Org (authored-by, N:1)
- PDD -> Product Deployment (governs, 1:1)
- ZDD -> Zone (configures, 1:1)
- Site Descriptor -> Site (configures, 1:1)
- RRSD -> Resource Provider (published-by, N:1)
- RRSD -> RRD/RSD/RD schemas (provides, 1:1 per resource kind)
- TSD -> Module Subscription Section (contains, 1:N)
- Module Subscription Section -> RSD (contains, 1:N)
- Module Subscription Section -> APD (contains, 1:N)
- Tenant -> APD (associated-with, 1:N)
- Velos (World) -> Site, Zone, Enclave, Space (creates, 1:N each)
- Velos (Zone-local) -> CSP Resource (provides, 1:N)

## E. Update todo.md

Replace open questions with checked-off answers. Add any remaining follow-up questions from this round.