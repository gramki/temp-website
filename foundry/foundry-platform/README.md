# Foundry Platform

This folder is the home of the **engineering documentation for the Foundry Platform** — the implementation that **delivers ACE and UPIM capabilities**. It contains architecture, module specifications, UX, deployment, security/compliance posture, observability, and CI documentation. Module-level specs grow here as they are produced.

The primary readers are the product and engineering teams **building the Foundry Platform**. If you are looking for the model the platform delivers, read [`../ace/`](../ace/). If you are looking for the formal information schema the platform stores and mutates, read [`../product-information-model/`](../product-information-model/).

## Foundry vs Foundry Platform

These docs use **Foundry Platform** consistently for the implementation. Bare "Foundry" is reserved for the architectural construct in ACE. See [`../glossary.md`](../glossary.md) and the [top-level README](../README.md) for the full disambiguation.

## What the platform delivers

The Foundry Platform is the system that turns the ACE model and UPIM entities into running software:

- **Workshops** with their repositories and projects.
- **Workshop Projects** with intent routing, scenarios, and tasks (each Workshop Project corresponds to a Product in UPIM — the locus where that Product is evolved).
- **Workspaces** (six types) with their IDE-mediated entry, scenario catalogs, and runtime engineering.
- **Governance hooks** on every transition of Product Intent.
- **Foundry CI** for evidence packs, test runners, build quality indicators, and agentic quality gates.
- **UPIM-backed data** — storage, lifecycles, and APIs for the entities UPIM defines (Definition, Work, Operating Model layers), without introducing divergent ontology.
- **Engagement Engineering** is documented separately as an ACE extension; it is *not* a Foundry Platform module — see [`../engagement-engineering/`](../engagement-engineering/).
- **Propeller** is *not* part of the Foundry Platform — it is a parallel workstream of cross-stack frameworks consumed by Workspaces. See [`../propeller/`](../propeller/).

## Sub-area map

The current backlog is captured in [`platform.TODO`](platform.TODO). The platform decomposes into the following sub-areas, mirrored in this folder over time as specifications mature.

### 1. Foundry Specification

The platform's own description as a system. Sources in [`platform.TODO`](platform.TODO) lines 1-9.

- Purpose, Objectives, and Scope
- Architecture
- Project Plan
- Security
- Compliance
- Audit
- Monitoring
- Logging

### 2. Workshop Engineering

How the Workshop construct is realized: how repositories are authored, stored, and served; the machines and tools that access them. Sources: [`platform.TODO`](platform.TODO) lines 10-12.

- Repositories — authoring, storage, serving
- Machines and tools for accessing repositories

### 3. Workshop Project Engineering

How a Workshop Project — including movement of Product Intent across Workspaces, KPIs and metrics, agent effectiveness, scenarios and tasks — is realized. Sources: [`platform.TODO`](platform.TODO) lines 13-17.

- Move Product Intent across Workspaces
- Workshop Project KPIs (Say/Do, Cost per Story Point, Velocity, Quality, etc.)
- Agent efficiency and effectiveness
- Scenarios and Tasks management

### 4. Per-Workspace Engineering

One sub-area per workspace type:

| Workspace | Sub-area | Source |
|---|---|---|
| Release | Release Workspace Engineering | [`platform.TODO`](platform.TODO) lines 18-22 |
| Development | Development Workspace Engineering | [`platform.TODO`](platform.TODO) line 23 |
| Governance | Governance Workspace Engineering | [`platform.TODO`](platform.TODO) line 24 |
| QA | QA Workspace Engineering | [`platform.TODO`](platform.TODO) line 25 |
| UX Design | UX Workspace Engineering | [`platform.TODO`](platform.TODO) line 26 |
| Product Specification | Product Specification Workspace Engineering | [`platform.TODO`](platform.TODO) line 27 |

Per-workspace specifications grow under this folder as modules are produced.

### IDE specifications (TBD)

Concrete IDE choices, editor integrations, and agent integrations (e.g. VS Code, Copilot, Claude, SDK integrations) will be specified when platform architecture choices are documented. At Zeta, the current realization is **Olympus Rocket** (IDE profiles per Workshop) inside **Olympus Workspace**; see [`../engagement-engineering/tenant-developer-tooling/TD.TODO`](../engagement-engineering/tenant-developer-tooling/TD.TODO).

### 5. CI

Foundry CI lives at [`ci/`](ci/). It composes existing CI primitives into a workshop-aware experience.

Concrete components from [`ci/ci.TODO`](ci/ci.TODO):

- Evidence packs
- Test runners and reports
- Build Quality Indicators (BQI)
- Tech debt management
- Agentic quality gates (crowd-sourced skills, project-template-specific triggers)
- MS Teams integration via Workspace settings
- TestRail test suite support in release pipelines

### Where Engagement Engineering belongs

Earlier drafts of [`platform.TODO`](platform.TODO) listed "Engagement Engineering" as a section under platform engineering (lines 28-33). That body of work is now documented separately as an **extension to ACE** at [`../engagement-engineering/`](../engagement-engineering/), because it changes ACE concepts (Workshop, Workforce, Repositories) for client delivery rather than only adding platform features. Cross-references between the two folders are maintained.

## How to write specifications under this folder

Module specifications added here should:

1. **Open with the ACE concept being realized.** Cite [`../ace/concepts.md`](../ace/concepts.md) or [`../ace/repositories.md`](../ace/repositories.md) for the concept the module operationalizes.
2. **Identify the UPIM entities involved.** Cite [`../product-information-model/README.md`](../product-information-model/README.md) and the relevant entity files. The platform stores and mutates UPIM-defined entities; it must not introduce divergent ontology.
3. **Specify the module itself.** Architecture, interfaces, dependencies, deployment, security, observability — at the level of detail appropriate to the module.
4. **Identify governance scenarios that apply.** What transitions does this module participate in, and what governance scenarios run on those transitions? See [`../ace/governance.md`](../ace/governance.md).
5. **Identify reusable foundations.** If the module relies on Propeller frameworks/libraries, cite [`../propeller/`](../propeller/).
6. **Identify engagement-extension behavior.** If the module behaves differently in an Engagement context, document the variance and cross-link to [`../engagement-engineering/extension-to-ace.md`](../engagement-engineering/extension-to-ace.md).

The intent is that any module specification reads first as an ACE/UPIM consumer and second as a piece of independent engineering — never the other way around.

## Read next

- [`platform.TODO`](platform.TODO) — current build backlog.
- [`ci/ci.TODO`](ci/ci.TODO) — current CI backlog.
- [`../ace/`](../ace/) — what the platform is realizing.
- [`../product-information-model/`](../product-information-model/) — the formal schema the platform implements.
- [`../foundry-work-plan/`](../foundry-work-plan/) — the project plan for building this platform.
