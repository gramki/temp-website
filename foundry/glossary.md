# Glossary

A single source of truth for terminology used across the Foundry documentation tree. Definitions here are deliberately terse; deeper treatment lives in the linked source documents.

If a term feels overloaded, first check whether it has multiple senses below (some do — Foundry, Workshop, Operating Model). When writing new docs in this tree, prefer the qualified form whenever a sentence could ambiguously refer to more than one sense.

---

## Core ACE terms

**ACE — Agent-Centric Engineering.** An agent-centric product development system: the way of building software in which human–agent teams operate in specialized workspaces, governed by shared models. ACE defines the workspaces, the flow of Product Intent across them, the human entry surface (IDE), and the governance applied to handoffs. Source: [`ace/ace-model.md`](ace/ace-model.md), [`ace/README.md`](ace/README.md).

**Foundry (concept).** The architectural construct in ACE: the place where software products are crafted, governed by Product, Work, and Operating models, and hosting workshops. A Foundry is an organization-scoped construct — there can be multiple Foundries, typically one per Organization. See [`foundry/1.TODO`](1.TODO) line 21.

**Foundry Platform.** The implementation of the Foundry concept: the software, infrastructure, modules, deployments, security and compliance posture, observability, and CI being engineered. It **delivers ACE and UPIM capabilities** — ACE workspaces, intent flow, governance, and the storage and mutation of UPIM-defined entities. Always written in capitalized form to disambiguate from the conceptual Foundry. Source: [`foundry-platform/`](foundry-platform/).

**Workshop.** A body of work inside a Foundry owned by a product team, product suite, or organization. A Workshop holds repositories and hosts **multiple Workshop Projects**; it is not a single Product. In client delivery, an **Engagement is modeled as a Workshop** (e.g. a Bank-X Engagement is a Workshop named for that client). Source: [`ace/concepts.md`](ace/concepts.md); [`engagement-engineering/extension-to-ace.md`](engagement-engineering/extension-to-ace.md).

**Workshop Project.** Corresponds to a **Product** in UPIM: the venue (locus) where that Product is evolved through workspaces and scenarios; it is **not** the Product entity itself. A Workshop Project contains Workspaces, each for a distinct functional team. In an Engagement Workshop, each Product under delivery is evolved in an **Engagement Workshop Project**. Source: [`ace/concepts.md`](ace/concepts.md); [`ace/relationships.md`](ace/relationships.md).

**Workspace.** A specialized station inside a Workshop Project, owned by a single functional team. A Workspace has a Human–Agent Team and tools, is interfaced by humans through an IDE, owns well-defined Scenarios, and produces Tasks completed by the team. Workspaces read and write the workshop's repositories.

**Workspace types (six).** Product Specification, UX Design, Development, QA, Release, Governance. Each has its own role in the Product Evolution Cycle.

**Human–Agent Team.** The composition of human practitioners and AI agents that completes the work of a Workspace. ACE treats agents as members of the workforce, not as external automations.

**IDE (in ACE).** The interface a human uses to enter a Workspace. ACE treats each Workspace as having its own IDE context — the same human can step into different Workspaces and find different views, plugins, and behaviors. The concrete realization in Zeta tooling uses Olympus Workspace and Olympus Rocket; see [`engagement-engineering/tenant-developer-tooling/TD.TODO`](engagement-engineering/tenant-developer-tooling/TD.TODO).

**Scenario.** A well-defined situation a Workspace is set up to handle. A Scenario, when triggered, creates Tasks.

**Task.** A unit of work created by a Scenario, completed by the Workspace's Human–Agent Team.

**Repositories (ACE sense).** The collection of stores that workshops use and update. ACE names a conceptual repository set in [`ace/ace-model.md`](ace/ace-model.md). The canonical inventory — UPIM-aligned with codes (PIR, DKB, DAR, POR, CAR, QVS, OPR, PFR, PPR, WR, WFR, ESR, PEIR) — lives in [`ace/repositories.md`](ace/repositories.md). Some repositories are Foundry-scoped (e.g. WFR), others are Workshop-scoped; see [`foundry/1.TODO`](1.TODO) line 9.

**Product Intent.** The thread that flows through workspaces. Release Workspace produces Product Intent; Product Specification triggers on it; it moves to UX Design and back, then to Development and QA in parallel, on to Release as Product Delivery, optionally returning to Specification from Development or QA. Source: [`ace/ace-model.md`](ace/ace-model.md) lines 51-58.

**Product Evolution Cycle.** The named flow of Product Intent across workspaces. Detailed in [`ace/product-evolution-cycle.md`](ace/product-evolution-cycle.md).

**Governance Workspace.** The workspace whose Scenarios are invoked on every Product Intent transition. It does not own task content; it owns handoff validation. Primary human personas include **Engineering Managers** (and Product Operations / audit roles where applicable). Source: [`ace/ace-model.md`](ace/ace-model.md) line 62; [`ace/workspaces/governance.md`](ace/workspaces/governance.md).

## ACE governing models

**Product Model.** The model that describes what the product is and where it is going. In UPIM, this corresponds to the Definition Model plus the strategy/intent dimensions.

**Work Model.** The model that describes what work exists — entities, artifacts, state transitions. In UPIM, this is structured as five tracks (Discovery, Build, Run, Win, Evolve).

**Operating Model.** The model that describes how the organization executes — coordination (ceremonies, cadences, rituals, rhythms) and organization (roles, teams, skills, training, tools). Earlier ACE drafts referred to this as "Org Model"; that name is deprecated because it implied structure-and-people only and omitted coordination. See UPIM [`product-information-model/README.md`](product-information-model/README.md).

> **Note on three names.** ACE's three governing models map to UPIM's Definition / Work / Operating layers. They are aligned but not identical: ACE's "Product Model" emphasizes intent and aspiration alongside structure; UPIM's "Definition Model" is the formal articulation. The mapping is documented in [`ace/relationships.md`](ace/relationships.md).

## UPIM terms

**UPIM — Unified Product Information Model.** A formal information model with three layers — Definition Model, Work Model, Operating Model — that gives entities, dimensions, tracks, and lifecycles to product, work, and operating concerns. UPIM is one layer in the **concretization of ACE** (it gives formal structure to the things ACE moves around), but **UPIM is independent of ACE**: an organization can adopt UPIM without adopting ACE, and ACE references UPIM rather than embeds it. UPIM is **not the most concrete form** of that information; it can be further specialized for specific products. Source: [`product-information-model/README.md`](product-information-model/README.md).

**Product (UPIM).** A Definition Model entity. In ACE, a **Workshop Project** corresponds to a Product and is where that Product is evolved; the Workshop Project is not the Product itself.

**Win Engineering (aka Product Operations Engineering).** A **UPIM** construct (Win Track / Track 4 engineering body): tooling for Support, Advocacy, Feedback loops, Product Analytics, and related capabilities that help Win teams achieve Win outcomes **beyond** the customer-facing functional surface of the product. **Distinct from Engagement Engineering** (client-delivery extension to ACE). Source: [`product-information-model/README.md`](product-information-model/README.md); this glossary.

**Definition Model.** What the product is — its complete structural description across nine dimensions in four tiers. Source: UPIM README.

**Dimensions (1–9).** Strategy & Intent (1); Vendor Value (2); Customer Value (3); User-Centric Experience (4); Technical & Architectural (5); Ecosystem & Extensibility (6); Operational Runtime & DevOps (7); Structural Topology (8); Data & Information (9). Source: UPIM README.

**Tracks (1–5).** Discovery (1); Build (2); Run (3); Win (4); Evolve (5). Each track owns its own planning alongside core activities. Source: UPIM README.

## Engagement terms

**Engagement.** In Engagement Engineering, an **Engagement is a Workshop** — program-managed, consolidating Velocity, Predictability, Quality, Cost, and Risk for the Products delivered under it. Each Product built for that client corresponds to a **Workshop Project** inside the Engagement Workshop. Source: [`engagement-engineering/extension-to-ace.md`](engagement-engineering/extension-to-ace.md); [`foundry/1.TODO`](1.TODO) lines 5-12.

**Home Workshop.** The Workshop in which a **Workshop Project** primarily lives. Every Workshop Project has a Home Workshop. For a Product that spans multiple Workshops, the Home Workshop is typically the permanent product team's Workshop; for a Product that exists only inside one client engagement, the **Engagement Workshop is the Home Workshop**. Source: [`engagement-engineering/extension-to-ace.md`](engagement-engineering/extension-to-ace.md).

**Home Workshop Project.** The **canonical Workshop Project** for a Product across Workshops — the primary locus where that Product's evolution is tracked when the Product is not engagement-only. Source: [`engagement-engineering/extension-to-ace.md`](engagement-engineering/extension-to-ace.md).

**Engagement Workshop Project.** A Workshop Project inside an **Engagement Workshop** (client delivery). Source: [`engagement-engineering/extension-to-ace.md`](engagement-engineering/extension-to-ace.md).

**Contributing Workshop Project.** A **special kind of Engagement Workshop Project** that holds a reference to a **Home Workshop Project** elsewhere (the Product's canonical evolution locus). Not every Engagement Workshop Project is Contributing — standalone engagement-specific Products exist without an external Home Workshop Project. Source: [`engagement-engineering/extension-to-ace.md`](engagement-engineering/extension-to-ace.md).

**Engagement Engineering.** The body of platform engineering work that extends ACE for client delivery — multi-tenant realities, customer-facing release artifacts, evidence packs, customer-side feedback channels, tenant developer tooling. Source: [`engagement-engineering/`](engagement-engineering/).

## Adjacent constructs (mentioned, not detailed here)

**Estate.** The runtime locus where a Product is deployed; contains the SRE workforce. A Product may be deployed across multiple Estates. Estate ontology is intentionally not expanded in this documentation — see [`foundry/1.TODO`](1.TODO) lines 14, 30.

**Olympus World.** Zeta's **Production Operations** ontology — how production is organized and named at runtime. It is **not** a software-product manufacturing construct; it is out of scope of ACE, UPIM, Foundry Platform, and Engagement Engineering documentation except where the **boundary** between software manufacturing and production operations must be named (e.g. Estate handoff). Source: Zeta internal production-operations documentation; [`foundry/1.TODO`](1.TODO) lines 30, 33-34 for historical coupling notes in scratch material.

## Tooling and workstream terms

**Foundry CI.** The CI capability inside the Foundry Platform. Concrete components include evidence packs, test runners and reports, build quality indicators, technical-debt management, agentic quality gates, MS Teams integration, Test Rail support. Source: [`foundry-platform/ci/ci.TODO`](foundry-platform/ci/ci.TODO).

**Olympus Workspace.** The concrete workspace implementation in Zeta tooling, one per Foundry Workshop (multiple workspaces per workshop). Source: [`engagement-engineering/tenant-developer-tooling/TD.TODO`](engagement-engineering/tenant-developer-tooling/TD.TODO).

**Olympus Rocket.** The concrete IDE in Zeta tooling. Each Workshop has a Rocket profile that determines default plugins, views, and settings. Source: same as above.

**Olympus Hub Workbench.** The view of the Workshop as a hub. Source: same as above.

**Propeller.** A parallel workstream of the Foundry engineering team — frameworks, libraries, and conventions used across Zeta tech stacks (Java 21, GraalVM, Spring Boot, distroless images, etc.). Sometimes called **Build Accelerators** in executive narrative; **Propeller** is the canonical name in [`propeller/`](propeller/). Not a Foundry Platform module; consumed by Workspaces. Source: [`propeller/propeller.TODO`](propeller/propeller.TODO); [`propeller/README.md`](propeller/README.md).

**Tenant Developer Tooling.** Tooling delivered to a tenant's developers when the Workshop is configured for tenant-side use. Source: [`engagement-engineering/tenant-developer-tooling/`](engagement-engineering/tenant-developer-tooling/).

## Deprecated or evolving terms

**Org Model.** Deprecated. Replaced by **Operating Model** (see above). Older drafts of ACE used "Org Model"; new docs should not.

---

This glossary lists terms; it does not duplicate definitions that have a single canonical source. When a term has both a short definition here and a longer treatment elsewhere, the linked source is authoritative.
