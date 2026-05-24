# DR-035: Dim 8 & PSD Structural Decisions — Module Functional Classification, Capability Templates, System/Component Redefinition, PSD Authorship Split

**Status:** Accepted
**Date:** 2026-05-19

---

## Context

Three overlapping design pressures converged in this session:

1. **Dim 8 entity detailing.** The Module entity in Dim 8 carried an "archetype" field inherited from early architecture-oriented thinking (HI / Programmatic / Reactive). This taxonomy described *how* a module was built, not *what business function* it served. Customer-value-oriented classification was missing.

2. **PSD authorship clarity gap.** The Product Specification Document had no formal partition of PM-authored vs. architect-authored sections, leading to uncertainty about scope, readiness gates, and who was responsible for what before a PSD could enter the Build Track.

3. **Dim 5 System/Component inversion.** DR-024 defined System as "independently deployable technical unit" and Component as "significant architectural building block within a System." This inverted the operational reality: engineers deploy Systems (the whole), not individual Components. A Component in the real world (a container image, a Lambda package) is individually buildable but always deployed as part of its parent System. The DR-024 definitions had inadvertently elevated Components to deployment-unit status and conflated internal code building blocks with deployable artifacts.

These three design pressures were resolved together because the Dim 5 redefinition directly affects the PSD authorship split (architect-authored sections reference Dim 5 entities), and the Module Functional Classification feeds the PSD header. They are logically one decision set.

---

## Decisions

### D1: Product lifecycle statuses

**Decision:** The Product entity carries five lifecycle statuses in sequence:

`Incubating → Preview (Beta) → GA → Maintenance → End-of-Life`

**Rationale:** This sequence mirrors real-world product commercialization stages. "Incubating" accommodates internal or pre-announcement products. "Preview (Beta)" signals limited availability with known roughness. "GA" is the general-availability commitment threshold. "Maintenance" signals no new investment but continued support. "End-of-Life" marks the formal sunset boundary.

---

### D2: Module lifecycle statuses

**Decision:** The Module entity carries the same five lifecycle statuses as Product:

`Incubating → Preview (Beta) → GA → Maintenance → End-of-Life`

**Rationale:** Modules evolve independently within a Product lifecycle. A GA Product may contain Incubating Modules (e.g., an experimental capability added after initial launch) and Maintenance-mode Modules (e.g., a feature preserved for existing customers but receiving no new investment). Using the same vocabulary across Product and Module reduces cognitive overhead while preserving the independence of each entity's lifecycle trajectory.

---

### D3: Tenancy Model for Product and Module

**Decision:** Both Product and Module carry a `Tenancy Model` attribute with two values: `Single-Tenant` / `Multi-Tenant`. The "Hybrid" value considered during discussion is dropped.

**Constraint:** A Multi-Tenant Product requires all of its Modules to be Multi-Tenant. A Single-Tenant Module cannot belong to a Multi-Tenant Product.

**Rationale:** Hybrid tenancy is an implementation detail (e.g., tenant-isolated data within a shared application tier), not a product-level strategic classification. Encoding it in the Definition Model would require tracking the specific partitioning mechanism, which belongs below the Definition Model waterline. The constraint (Multi-Tenant Product → all Modules Multi-Tenant) exists because a product's tenancy promise to customers is undermined if any Module fails to deliver it.

---

### D4: Module Functional Classification (replaces Module Archetype)

**Decision:** The `Module Archetype` field on the Module entity is replaced by `Module Functional Classification`. Values are drawn from the Twelve System Types, a FinTech/banking-specific taxonomy:

`Record` / `Enforcement` / `Data` / `Engagement` / `Action` / `Intelligence` / `Identity` / `Influence` / `Memory` / `Product` / `Innovation` / `Integration`

**Rationale:** The prior archetype taxonomy (HI / Programmatic / Reactive) described the module's *interaction model* — an architectural concern. Functional Classification describes *what business function the module serves* — a product and commercial concern. "Record" (golden source), "Enforcement" (rules, compliance), "Data" (analytics, reporting), "Engagement" (customer-facing UX) are categories that PMs, commercial teams, and buyers can reason about. The Twelve System Types taxonomy is an established domain model for FinTech/banking contexts, reducing the need to invent a proprietary classification from scratch.

---

### D5: Capability Templates as PM-facing specification guides

**Decision:** Three Capability Templates are introduced as PM-facing specification guides, decoupled from System Archetypes. Each template defines what a PM is responsible for specifying when authoring a Capability in the PSD:

| Template | PM Specifies |
|---|---|
| **Experience** | User journey, interaction model, UX channel, personas, accessibility requirements |
| **Integration** | API intent, consumer personas, SLO targets, contract shape, backward compatibility requirements |
| **Processing** | Trigger/input, processing intent, data produced/consumed, SLA requirements, error handling expectations |

**Rationale:** PM specifications need to be concrete, bounded, and actionable for architect review — but PMs should not be specifying technical architecture. The three templates establish what PMs *do* specify (functional intent, user impact, quality expectations) without requiring them to specify what belongs in the architect-authored sections (Dim 5/6/7/9 mapping). Decoupling from System Archetypes means the templates remain stable even when system architecture evolves.

---

### D6: Capability has two independent attributes — Maturity and Lifecycle Stage

**Decision:** The Capability entity carries two independent attributes:

- **Maturity** (how proven the capability is): `Alpha → Beta → Gamma`
- **Lifecycle Stage** (where in the capability's lifecycle): `Planned → Available → Deprecated → Retired`

These attributes are set independently. A GA Module may contain Alpha Capabilities (newly introduced, not yet proven). A Gamma Capability may be Deprecated (proven, but being retired). The combination is always valid.

**Rationale:** Maturity and lifecycle stage are orthogonal concerns that are commonly conflated. A capability's maturity reflects operational confidence — has it run in production under real load? A lifecycle stage reflects commercial intent — are we investing in it, maintaining it, or sunsetting it? Conflating them would force imprecise combinations ("an Alpha capability that is Deprecated" cannot be expressed). Keeping them independent allows the model to accurately describe, for example, a new experimental capability (Alpha/Planned) alongside a proven capability being wound down (Gamma/Deprecated).

---

### D7: Entitlement at Module level

**Decision:** Pricing Tier (Dim 2) is linked to Module, not to Feature. Feature-level entitlement is explicitly out of scope for the Definition Model.

**Rationale:** Entitlement at Feature granularity would require the Definition Model to track every commercial variation of every capability — a maintenance burden that belongs in billing systems, not in a product model. Module-level entitlement aligns with how products are actually sold (customers buy access to modules/products, not individual features). Feature-level entitlement is a pricing enforcement concern handled below the Definition Model waterline.

---

### D8: PSD authorship split

**Decision:** The PSD (Product Specification Document) is formally divided into two authorship zones with a clear gate between them:

**PM-Authored Zone (Product Draft phase):**
- PSD objective and traceability to PDR
- Capability specifications (using Capability Templates — D5)
- Feature specifications
- Acceptance Criteria intent
- Epic decomposition proposal

**Architect-Authored Zone (Technical Review phase):**
- System mapping (Dim 5 — which Systems realize the Module)
- Dim 5, Dim 6, Dim 7, Dim 9 sections (technical, ecosystem, operational, security mapping)

**Gate — Approved status:** Both zones complete and signed off → Product Intent is sufficiently refined for Build Track entry

**Rationale:** Without a formal partition, Product Intent could move into Build with incomplete technical mapping, or architects were expected to fill in PM sections, or neither happened and Build Track work began on underspecified requirements. The split creates a two-phase authorship model with a clear gate: PM delivers functional specification; architect delivers technical mapping; both must be complete before any Build Track work begins.

---

### D9: PSD header field change — Module Archetype removed

**Decision:** The `Module Archetype` field in the PSD header is removed and replaced by `Module Functional Classification` (per D4).

**Rationale:** Follows directly from D4. PSD headers reference Module-level metadata; as the Module entity changes its classification field, PSD headers must reflect the same vocabulary.

---

### D10: Dim 5 System and Component redefined

**Decision:** System and Component in Dim 5 are redefined as follows:

**System** = a named operational grouping of Components. Versioned as a whole. Deployed as a whole by SRE/ops. Maps many-to-many to Dim 8 Modules.

**Component** = an individual deployable artifact within a System (container image, Lambda package, frontend bundle). Independently buildable with its own artifact version. Not independently deployed to production — always deployed as part of its parent System.

**Component Archetypes:**
`API Service` / `Web Application` / `Event-Driven Worker` / `Batch Job` / `Data Store` / `Integration Adapter` / `Gateway` / `CLI/SDK`

**Retired from Dim 5:** Internal code building blocks (FX Rate Calculator, Payment State Machine, etc.) are code-level concerns below the Definition Model waterline.

**Three deprecated Dim 5 files removed:** `dim5-subsystem.md`, `dim5-function-method.md`, `dim5-class-component.md` (previously deprecated by DR-024) are formally deleted.

**Rationale:** The DR-024 definitions inverted the operational reality. In practice, SRE/ops teams deploy Systems — they run a deployment pipeline that produces a versioned System artifact. Individual Components are not independently deployed to production; they are assembled into a System and deployed together. What was called "Component" in DR-024 (a "significant architectural building block") was an imprecise description that could include anything from a payment processor class to a container image. The redefinition anchors both entities to concrete operational realities: Systems are what you deploy; Components are what you build and assemble into Systems.

---

### D11: Module → System relationship (one-to-many)

**Decision:** A Module (Dim 8) is realized by one or more Systems (Dim 5). This relationship is architect-defined.

**Rationale:** A Module is a functional unit; a System is an operational deployment grouping. They are independent decompositions. A simple Module may map to a single System; a complex Module may span multiple Systems. The many-to-one direction (multiple Systems serving one Module) is the common case. Architect-defined means this mapping is captured during the Technical Review phase of PSD authorship (D8), not by PMs.

---

### D12: Capability → System relationship (many-to-many)

**Decision:** Architects map Capabilities (and their constituent Features) to Systems (Dim 5) in a many-to-many relationship.

**Rationale:** A Capability may be implemented by components across multiple Systems (e.g., a Payment Initiation capability that spans an API Service System and a Processing System). A System may implement capabilities from multiple Modules (shared infrastructure). This many-to-many mapping is the architect's primary artifact in the Technical Review phase and is what enables Build Track work to be scoped to the correct Systems.

---

### D13: PSD templates converted to Capability-level specification guidance

**Decision:** Three files previously described as Module-level PSD templates are converted to Capability-level specification guidance documents, renamed to reflect the three Capability Templates:
- `capability-template-experience.md`
- `capability-template-integration.md`
- `capability-template-processing.md`

**Rationale:** The templates were misaligned at the Module level — a PSD contains multiple Capabilities, each of which may follow a different template. Moving specification guidance to the Capability level matches the D5 decision and allows a single PSD to contain, for example, an Experience Capability and a Processing Capability under the same Module, each specified according to the appropriate template.

---

### D14: dim8-value-stream.md structure is sufficient — deferred

**Decision:** The current structure of `dim8-value-stream.md` is sufficient for now. The `_Other fields to be refined_` note is marked as deferred and will be addressed in a future session.

**Rationale:** Value Stream entity detailing is not on the critical path for the PSD authorship split or Module Functional Classification. Attempting to complete it in this session would expand scope without yielding immediate structural benefit.

---

### D15: Module / System naming — vocabulary rule

**Decision:** The following vocabulary rule is established and must be consistently applied across all UPIM documentation:

- **Module** = the functional unit in Dim 8 (what the product does, from a PM/business perspective)
- **System** = the operational deployment grouping in Dim 5 (what engineers build and SRE/ops deploy)

**Alternatives considered and rejected for Dim 5:**
- "Deployment Module" — ambiguates bare "Module" (which must unambiguously refer to Dim 8)
- "Cluster" — carries infrastructure/Kubernetes connotation unrelated to functional grouping
- "Service Group" / "Deployment Unit" — functional but clinical; lose the intuitive "system" sense

**Alternatives considered and rejected for Dim 8:**
- "Domain" — too conceptual; loses the product-feature connotation
- Using "Module" for Dim 5 — would create a naming collision with the established Dim 8 term

**Rationale:** Naming collisions in a layered model are a high tax — every reference to "module" becomes ambiguous. The Module/System pairing preserves the established Dim 8 vocabulary while giving Dim 5's operational grouping a name that is intuitive (a "system" is naturally understood as a running thing), distinct, and free of infrastructure over-connotation.

---

## Rationale (Grouped)

**Why redefine System/Component rather than introduce a new entity?**
Introducing a new entity alongside the existing System/Component would have preserved the confusion. The conceptual issue is the abstraction level — not a missing entity. A clean redefinition, documented as an amendment to DR-024, is preferable to entity proliferation.

**Why Twelve System Types for Functional Classification?**
The prior HI/Programmatic/Reactive taxonomy was derived from technical interaction patterns. The Twelve System Types taxonomy is a recognized domain model for FinTech/banking that describes what systems *do* — their business function — rather than how they are built. It is more stable (business functions change slowly; technical interaction models change with each architectural trend) and more useful to PMs and commercial teams.

**Why split PSD authorship formally?**
Build Track entry gates fail when PSDs contain incomplete sections with no clear owner. The PM/architect split makes ownership explicit and the approval gate enforces completeness. It also prevents architect time from being consumed on functional specification work that belongs to PMs.

**Why Maturity and Lifecycle Stage independent?**
A capability can be operationally proven (Gamma) but commercially deprecated. A capability can be commercially planned but architecturally Alpha. These are different facts about the same capability and are maintained by different stakeholders (engineering judges maturity; product/commercial drives lifecycle stage). Conflating them would require either losing information or encoding artificial constraints that don't reflect reality.

**Why Module-level entitlement?**
Feature-level entitlement would require the Definition Model to track every commercial SKU and every capability toggle — a scope that properly belongs in billing systems and feature flag infrastructure. Module-level entitlement keeps the Definition Model at the right abstraction level while still enabling meaningful commercial differentiation.

---

## Consequences

**Positive:**
- Module Functional Classification gives PMs, commercial teams, and buyers a common vocabulary for describing what modules do
- PSD authorship split eliminates the ambiguity about who owns which sections and creates a clean Build Track entry gate
- Dim 5 System/Component redefinition aligns the model with operational reality — Systems are deployed; Components are built
- Capability Maturity and Lifecycle Stage as independent attributes enable accurate modeling of capability state without artificial constraints
- Module-level entitlement keeps the Definition Model at the right abstraction level
- Vocabulary rule (Module = functional; System = operational) reduces documentation ambiguity across all UPIM artifacts

**Negative:**
- DR-024 and DR-021 are partially superseded — existing documentation referencing the old System/Component definitions or Deployment Topology axis must be read with the amendments in mind
- PSD templates at the Module level must be migrated to Capability-level guidance documents (D13)
- The "System Version" construct in DR-026 is now semantically misaligned — it was defined as the atomic build artifact for a single deployable, which is now a Component (not a System)

**Deferred:**
- **DR-036 (planned):** Versioning rename — "System Version" → "Component Version." The DR-026 versioning model used "System Version" to mean what is now a Component's version. Renaming it is the correct next step but is deferred to avoid scope explosion in this session. DR-026 carries a note directing readers to this context.
- **Value Stream entity detailing** (dim8-value-stream.md fields) — deferred per D14.

---

## Amended Records

| Record | Amendment |
|---|---|
| DR-024 | D3 (System definition) and D8 (Component definition) superseded by D10 of this record |
| DR-021 | D6 (Client-Distributed Deployment Topology), Consequence #3, and D4 (archetype classification language) amended by this record |
| DR-026 | Note added: "System Version" semantically maps to what should be called "Component Version" under the new Dim 5 model; rename deferred to DR-036 |
