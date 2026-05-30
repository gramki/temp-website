# ACE Objectives

This document states what ACE — and the Foundry Platform that delivers ACE and UPIM capabilities — aims to achieve, and what it explicitly does not aim to achieve. It is the contract between the theory in [ace-model.md](ace-model.md) and the engineering work in [../foundry-platform/](../foundry-platform/README.md).

## Objectives

ACE aims to make the following true at Zeta:

### 1. Scenario-driven, agent-native work

Every unit of work in a Workspace originates from a well-defined Scenario and decomposes into Tasks completed by a Human–Agent Team. Free-form prompting against a code repository is a degenerate case, not the norm. Sources: [ace-model.md](ace-model.md) lines 44-48; [../foundry-platform/platform.TODO](../foundry-platform/platform.TODO) "Workbench Engineering" line 17.

### 2. IDE-mediated human entry per workspace

Humans enter each Workspace through an IDE configured for that workspace's purpose. The IDE is not a single shared tool; it is a context — plugins, views, settings, repositories — that differs per workspace and is loaded automatically. Concrete realization in Zeta tooling: Olympus Workspace and Olympus Rocket per Workshop, with Workshop-driven Rocket profiles. Source: [../engagement-engineering/tenant-developer-tooling/TD.TODO](../engagement-engineering/tenant-developer-tooling/TD.TODO).

### 3. Repository-backed truth

Every workspace reads and writes well-defined repositories. There is no ambient state in slack threads or undocumented conventions; if it matters, it lives in a repository. The canonical repository inventory is in [repositories.md](repositories.md); the conceptual model in [ace-model.md](ace-model.md) lines 16-28.

### 4. Product Intent as a routed bridge asset

Product Intent is a hybrid bridge entity: definition-bearing, work-triggering, and routable. It flows through the workspaces along a defined path: Discovery/product decisions → Specification (PSD refinement) → UX/Specification → Development + QA → Release as Product Delivery and renewal, with optional return to Specification. Routing is explicit and traceable, not implicit. Source: [ace-model.md](ace-model.md) lines 51-58; detail in [product-evolution-cycle.md](product-evolution-cycle.md).

### 5. Governance on every transition

Every transition of Product Intent invokes Scenarios in the Governance Workspace. Governance is a property of motion, not a stage gate at the end. Source: [ace-model.md](ace-model.md) line 62; detail in [governance.md](governance.md).

### 6. Agents as workforce members

Agents — human and AI alike — are members of the Workforce. The Workforce Repository (WFR) contains role bindings, skills, availability, and governance for both. Source: UPIM `repositories.md` description and [../product-information-model/README.md](../product-information-model/README.md).

### 7. Measurable agent effectiveness

Because Tasks are entities and Workspaces are stations with named inputs and outputs, the contribution of any participant — human or agent — is observable. Concrete platform objectives include agent efficiency and effectiveness metrics, project KPIs (Say/Do, Cost per Story Point, Velocity, Quality), and Workbench metrics/reporting/analytics/insights. Source: [../foundry-platform/platform.TODO](../foundry-platform/platform.TODO) lines 14-16; [../engagement-engineering/1.TODO](../engagement-engineering/1.TODO) lines 41-46.

### 8. Multi-tenant readiness

ACE is designed so that an extension — Engagement Engineering — can model the delivery of software to clients without breaking the base system. Workshops, Workforce, and Repositories all behave correctly when an Engagement spans multiple Workshops or a Product spans multiple Engagements. See [../engagement-engineering/extension-to-ace.md](../engagement-engineering/extension-to-ace.md).

### 9. Security, compliance, audit, observability by construction

The Foundry Platform delivers ACE and UPIM under explicit security, compliance, audit, monitoring, and logging constraints. These are first-class objectives of the Foundry Specification, not afterthoughts. Source: [../foundry-platform/platform.TODO](../foundry-platform/platform.TODO) lines 1-9.

### 10. Self-evolving practice

The system is expected to evolve. UPIM's Track 5 (Evolve) explicitly accounts for the evolution of the Work and Operating Models; ACE inherits that property. The model that cannot evolve is dead. Source: [../product-information-model/README.md](../product-information-model/README.md).

## Non-goals

These are not what ACE is for, and the Foundry Platform should not be evaluated against them.

### A. Not a generic IDE

ACE specifies that each workspace has an IDE context. It does not aim to build a new general-purpose code editor. The IDE is composed from existing technology (Olympus Rocket profiles, plugins, Workshop-specific views) rather than authored from scratch.

### B. Not a CI vendor replacement

Foundry CI is the CI capability inside the Foundry Platform. It composes existing CI primitives (test runners, evidence packs, build quality indicators, agentic quality gates) into a workshop-aware experience. It is not aiming to displace standard CI infrastructure where that infrastructure already serves. Source: [../foundry-platform/release-tools/platform-developer-guide/ci/ci.TODO](../foundry-platform/release-tools/platform-developer-guide/ci/ci.TODO).

### C. Not a substitute for UPIM

ACE does not redefine entities that UPIM already defines. Where UPIM specifies a Definition Model entity, a Work Model artifact, or an Operating Model pattern, ACE references it. The repository inventory in [repositories.md](repositories.md) is UPIM-aligned by construction. See [relationships.md](relationships.md).

### D. Not a marketing artifact

The Foundry Platform's value perspective for customers (typically Bank CIOs) is captured in [../stakeholder-briefs/](../stakeholder-briefs/README.md). That folder exists so that builders can internalize what a customer would value — it is not external positioning. ACE itself is engineered, not pitched.

### E. Not a production operations or runtime deployment ontology

ACE concerns itself with **software product manufacturing** — how products are specified, built, verified, released, and governed — not with how they are run in production. **Estate** (deployment locus, SRE workforce) appears only at the **Engagement Engineering** boundary as the handoff surface for Run-related work; full production-operations ontology is out of scope here. See [../engagement-engineering/extension-to-ace.md](../engagement-engineering/extension-to-ace.md); [../1.TODO](../1.TODO) lines 14-17.

### F. Not a bound-to-one-tech-stack platform

The Propeller workstream provides cross-stack frameworks, libraries, and conventions used by Workspaces, but neither ACE nor the Foundry Platform mandates a single tech stack. Source: [../propeller/propeller.TODO](../propeller/propeller.TODO).

## Success criteria (qualitative)

A Foundry Platform that fulfills ACE's objectives (while delivering UPIM-backed capabilities) is one where:

- A new engineer can join a Workshop and be productive within their workspace's IDE without out-of-band onboarding rituals.
- A new agent type can be introduced as a workforce member, gain skills, and be measured the same way a human peer is.
- Product Intent can be traced from origin (Discovery decision or Release renewal) to delivery without manual narration.
- A governance question (was this transition validated? what scenario did it invoke? what evidence was captured?) returns a deterministic answer from the repositories.
- An Engagement spanning multiple Workshops sees consolidated Velocity, Predictability, Quality, Cost, and Risk without bespoke reporting per project. Source: [../engagement-engineering/1.TODO](../engagement-engineering/1.TODO) line 12.

These criteria are written as qualitative properties because the platform is in active build. Quantitative targets attach to specific module specifications under [../foundry-platform/](../foundry-platform/README.md) over time.
