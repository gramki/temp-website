# Foundry Platform

This folder is the home of the **engineering documentation for the Foundry Platform** — the implementation that **delivers ACE and UPIM capabilities**. It contains architecture, module specifications, UX, deployment, security/compliance posture, observability, and CI documentation. Module-level specs grow here as they are produced.

The primary readers are the product and engineering teams **building the Foundry Platform**. If you are looking for the model the platform delivers, read [../ace/](../ace/README.md). If you are looking for the formal information schema the platform stores and mutates, read [../product-information-model/](../product-information-model/README.md).

## Foundry vs Foundry Platform

These docs use **Foundry Platform** consistently for the implementation. Bare "Foundry" is reserved for the architectural construct in ACE. See [../glossary.md](../glossary.md) and the [top-level README](../README.md) for the full disambiguation.

## What the platform delivers

The Foundry Platform is the system that turns the ACE model and UPIM entities into running software:

- **Workshops** with their repositories.
- **Workbenches** with intent routing, scenarios, and tasks (each Workbench corresponds to a Product in UPIM — the locus where that Product is evolved).
- **Workspaces** (six types) with their IDE-mediated entry, scenario catalogs, and runtime engineering.
- **Governance hooks** on every transition of Product Intent.
- **Foundry CI** for evidence packs, test runners, build quality indicators, and agentic quality gates.
- **UPIM-backed data** — storage, lifecycles, and APIs for the entities UPIM defines (Definition, Work, Operating Model layers), without introducing divergent ontology.
- **Engagement Engineering** is documented separately as an ACE extension; it is *not* a Foundry Platform module — see [../engagement-engineering/](../engagement-engineering/README.md).
- **Propeller** is *not* part of the Foundry Platform — it is a parallel workstream of cross-stack frameworks consumed by Workspaces. See [../propeller/](../propeller/README.md).

## Platform Modules

The platform decomposes into the following modules, each with its own folder. See [../tldr.md](../tldr.md) for the one-page overview and [../tldr-faq.md](../tldr-faq.md) for module design decisions.

| Module | Folder | Scope |
|--------|--------|-------|
| **Foundry Management** | [management/](management/README.md) | Admin plane — Workbenches, repositories (as services), teams, agents, knowledge, tenancy |
| **Foundry IDE** | [ide/](ide/README.md) | Builder-facing interface — workspace-specific views |
| **Agent Model** | [agent-model/](agent-model/README.md) | Agent architecture — Capable Agents, Skilled Agents, Employed Agents, Access Gateway |
| **Work Order Runtime** | [work-order-runtime/](work-order-runtime/README.md) | Execution engine — context compilation, agent lifecycle for WO execution, agent delegation, human-task surfacing |
| **Foundry Orchestrator** | [orchestrator/](orchestrator/README.md) | Coordination — route orchestration items per Track, create Workspace Work Orders, invoke Governance Scenarios, enforce gates |
| **Scenario Authoring** | [scenario-authoring/](scenario-authoring/README.md) | Per (Track, Workspace) — scenario discovery & definition; Skills, Knowledge, Tools; agent recommendations |
| **Release Tools** | [release-tools/](release-tools/README.md) | CI/CD pipelines with embedded agents, CD integrations, distribution stores |
| **Platform Ops** | [platform-ops/](platform-ops/README.md) | Plumbing — observability dashboards, standard tooling, infrastructure |

### Key design decisions

- **Agent lifecycle is context-dependent.** Work Order Runtime owns it for Work Order execution; Release Tools (CI) owns it for pipeline-embedded agents.
- **Governance is distributed.** Definition via Scenarios, enforcement via Orchestrator, evidence in repositories.
- **Orchestration items are Track-scoped; Work Orders are Workspace-scoped.** One orchestration item can create many Workspace Work Orders.
- **Repositories are services, not stores.** Each provides injection/access interfaces; Foundry Management exposes the access layer.
- **Integrations are owned by modules.** Release Tools owns CI/CD integrations; no horizontal "Integrations" module.
- **Scenario Authoring is scoped to (Track, Workspace) pairs.**

### Legacy structure

The backlog in [platform.TODO](platform.TODO) uses an older structure (Foundry Specification, Workshop Engineering, etc.). That structure is superseded by the module breakdown above, but the backlog items remain valid and should be mapped to the new modules.

### CI folder

The [ci/](release-tools/ci/README.md) folder (now under Release Tools) contains Foundry CI documentation. Release Tools extends and generalizes the CI work.

### Where Engagement Engineering belongs

Engagement Engineering is documented separately as an **extension to ACE** at [../engagement-engineering/](../engagement-engineering/README.md), because it changes ACE concepts for client delivery rather than only adding platform features.

## How to write specifications under this folder

Module specifications added here should:

1. **Open with the ACE concept being realized.** Cite [../ace/concepts.md](../ace/concepts.md) or [../ace/repositories.md](../ace/repositories.md) for the concept the module operationalizes.
2. **Identify the UPIM entities involved.** Cite [../product-information-model/README.md](../product-information-model/README.md) and the relevant entity files. The platform stores and mutates UPIM-defined entities; it must not introduce divergent ontology.
3. **Specify the module itself.** Architecture, interfaces, dependencies, deployment, security, observability — at the level of detail appropriate to the module.
4. **Identify governance scenarios that apply.** What transitions does this module participate in, and what governance scenarios run on those transitions? See [../ace/governance.md](../ace/governance.md).
5. **Identify reusable foundations.** If the module relies on Propeller frameworks/libraries, cite [../propeller/](../propeller/README.md).
6. **Identify engagement-extension behavior.** If the module behaves differently in an Engagement context, document the variance and cross-link to [../engagement-engineering/extension-to-ace.md](../engagement-engineering/extension-to-ace.md).

The intent is that any module specification reads first as an ACE/UPIM consumer and second as a piece of independent engineering — never the other way around.

## Read next

- [phase-1/](phase-1/README.md) — Phase 1 implementation-readiness outline and open questions.
- [platform.TODO](platform.TODO) — current build backlog.
- [ci/ci.TODO](ci/ci.TODO) — current CI backlog.
- [../ace/](../ace/README.md) — what the platform is realizing.
- [../product-information-model/](../product-information-model/README.md) — the formal schema the platform implements.
- [../foundry-work-plan/](../foundry-work-plan/README.md) — the project plan for building this platform.
