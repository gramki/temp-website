> **⚠ Amendment (DR-035, 2026-05-19):** Two decisions in this record are superseded by DR-035:
> - **D3 amended:** System is no longer "independently deployable technical unit." System is a named **operational grouping of Components** — versioned and deployed as a whole by SRE/ops. Component is the atomic deployable artifact.
> - **D8 amended:** Component is no longer "significant architectural building block within a System." Component is the **atomic deployable artifact** — independently buildable, but not independently deployed to production. Internal building blocks (FX Rate Calculator, Payment State Machine, etc.) are code-level concerns below the Definition Model waterline and are retired from Dim 5.
> See DR-035 for full rationale.

# DR-024: Dimension 5 — Technical & Architectural Dimension Expansion

**Status:** Accepted
**Date:** 2026-02-15

## Context

Dimension 5 (Technical & Architectural) had 3 skeletal entities (Subsystem/Service, Class/Component, Function/Method) aligned to C4 architecture levels — essentially a code-structure view of the product. This was the wrong abstraction: code-level structure is below the Definition Model waterline (same principle that deprecated Touchpoint from Dim 4, Payload Schema from Dim 6, and Cluster/Host from Dim 7). Meanwhile, the product's technical model — how it is architected, what systems exist, what technology choices were made, what dependencies the product relies on — had no representation in the Definition Model.

Dim 8 (Structural/Topology) already captures the functional view: Module → Capability → Feature, Value Streams. The product needed a complementary technical view: Architecture Model → System → Component, Interaction Flows, Dependencies. Two lenses on the same product, serving different audiences (PM/business vs. architects/engineering).

The discussion also revealed the need for Architecture Decision Records (ADRs) as a Dim 5 entity distinct from PDRs (Dim 1), and for a Technical Knowledge Base to make documentation gaps visible.

## Decisions

### D1: Reframe Dim 5 from code structure to technical model

Dim 5 is reframed from "codebase structure and processing logic" to "the product's technical model — how it is architected, what systems implement the functional modules, what technology choices were made, what dependencies exist, and how systems interact." The dimension now captures the architectural blueprint that complements Dim 8's functional topology.

### D2: Seven entities for the expanded Dim 5

Dim 5 is expanded from 3 skeletal entities to 7 detailed entities: **Architecture Model** (root), **System**, **Component**, **Dependency**, **Interaction Flow**, **Architecture Decision Record (ADR)**, **Technical Knowledge Base**. The entity set draws structural parallels from Dim 2 (Business Model → Architecture Model), Dim 7 (Infrastructure Model → Architecture Model), and Dim 8 (Module → System, Value Stream → Interaction Flow).

### D3: Dim 8 / Dim 5 duality — functional vs. technical view

Dim 8 provides the functional view of the product; Dim 5 provides the technical view. Same product, two lenses, different audiences. The System-to-Module mapping is explicitly many-to-many: a Module may be implemented by multiple Systems; a shared System may serve multiple Modules. This reflects reality — functional decomposition and technical decomposition are independent.

### D4: Technology choices are fields on System and Component

Technology choices (language, framework, database, protocols) are modeled as fields on System and Component entities rather than standalone entities. The rationale for each choice is captured in ADRs. A standalone "Technology Choice" entity would duplicate information already on Systems (what was chosen) and ADRs (why it was chosen).

### D5: ADR is a Dim 5 entity, distinct from PDR

Architecture Decision Record (ADR) captures technical/architectural decisions — the Dim 5 counterpart of PDR (Dim 1). Three relationship patterns: PDR triggers ADR(s), ADR exists independently, ADR constrains PDR. ADRs follow the Nygard format (Context, Decision, Consequences, Status). Separation respects the dimensional structure: Dim 1 = Strategy & Intent; Dim 5 = Technical & Architectural. Different audiences, governance, and lifecycles.

### D6: ADR has dual provenance — Discovery and Build

ADRs can be produced by both the Discovery Track (Deliberation-driven — strategic architecture decisions) and the Build Track (implementation-driven — decisions emerging during build work). Both paths produce the same Dim 5 entity; provenance is tracked through relationships. The Build Track's ADR production mechanism will be detailed when Build Track entities are fully specified.

### D7: Technical Knowledge Base as per-System assessment

Technical Knowledge Base is a per-System assessment entity (paralleling Operational Readiness in Dim 7) that tracks documentation coverage and currency — architecture docs, operational runbooks, release notes, integration guides, Win technical guides, troubleshooting playbooks. Makes documentation gaps visible in the Definition Model rather than leaving them implicit.

### D8: Component is always contained by System

Components are significant architectural building blocks within Systems. They are always contained by a System and transitively map to Dim 8 Modules through their parent System. System is always the container — there are no free-standing Components. Components are optional for simple Systems.

### D9: Deprecate Subsystem/Service, Class/Component, Function/Method

All three original Dim 5 entities are deprecated. Subsystem/Service is subsumed by the expanded System entity. Class/Component and Function/Method are below the Definition Model waterline — code-level structure belongs in PSD/Build Track artifacts.

## Rationale

**Why reframe rather than extend?** The original Dim 5 was at the wrong abstraction level. Adding entities alongside Subsystem/Class/Function would create an incoherent dimension mixing code-level detail with architectural strategy. A clean reframe to the architectural level provides the right abstraction for the Definition Model.

**Why not merge Dim 5 into Dim 8?** Dim 8 is the functional view; Dim 5 is the technical view. Merging them would overload Dim 8 with dual concerns and lose the explicit duality. The many-to-many System-to-Module mapping requires separate entities — you can't express "notification-service serves Payments, Compliance, and Onboarding modules" within a single Module entity.

**Why ADR separate from PDR?** Different dimensions (Dim 1 vs. Dim 5), different audiences (PM vs. architect), different governance (product deliberation vs. architecture review), different scopes (product strategy vs. technical implementation). But they cross-reference each other, maintaining full decision traceability.

**Why Technical Knowledge Base in Definition Model?** Documentation gaps are an operational and commercial risk. A System with no runbook is a Run Track impediment; a System with no integration guide is a Win Track impediment. Making gaps visible in the Definition Model gives them strategic weight and enables systematic remediation planning.

## Consequences

**Positive:**
- Dim 5 now captures the product's technical reality at the right abstraction level
- The Dim 8 / Dim 5 duality provides complete structural coverage — functional AND technical views
- ADRs create full decision traceability from product strategy (PDR) through technical implementation (ADR)
- Dependencies make external reliance explicit — risk, cost, and vendor lock-in are visible
- Interaction Flows bridge the gap between functional flows (Value Streams) and technical flows
- Technical Knowledge Base makes documentation gaps visible and actionable

**Negative:**
- Dim 5 grows from 3 to 7 entities, increasing model surface area
- ADR dual provenance (Discovery + Build) adds complexity to the artifact production model
- System-to-Module many-to-many mapping requires explicit maintenance

**Mitigations:**
- Entity count (7) is proportional to domain complexity and comparable to other expanded dimensions
- Build Track ADR production will be detailed incrementally (future Build Track expansion)
- System-to-Module mapping is maintained through Modeling Tasks, same as all Definition Model updates

---
