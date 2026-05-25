# Foundry Platform Phase 1

This folder is the implementation-readiness workspace for **Phase 1 of the Foundry Platform**. It is for product and engineering teams building the platform, not for restating ACE theory.

The goal is to turn ACE and UPIM into build contracts: module boundaries, event contracts, scenario catalogues, repository/API contracts, governance behavior, and UI-to-module responsibilities.

## Phase 1 build question

Phase 1 should answer:

> Can Foundry take a product-relevant discovery question, form Product Intent, refine it into buildable work, execute Workspace Work Orders, govern transitions, and publish Product Delivery with traceability?

## Phase 1 scope anchor

The working Phase 1 slice exercises:

```text
Discovery Case
  -> PDR
  -> Product Intent
  -> PSD refinement
  -> Workspace Work Orders
  -> QA / Release
  -> Governance evidence
```

It should use the current ACE / UPIM concepts:

- **Discovery Case** — Discovery Track orchestration item.
- **Product Intent** — Build Track orchestration item.
- **Workspace Work Order** — Scenario execution instance in a Workspace.
- **Governance Case** — validation/evidence/audit item on transitions.
- **Product Intent Repository (PIR)**, **Work Repository (WR)**, and evidence repositories as the durable stores.

## Eventual documentation set

The following docs should be created under this folder as decisions are answered.

| Document | Purpose | Primary audience |
|----------|---------|------------------|
| `golden-path.md` | End-to-end happy path from Discovery Case to Product Delivery, step by step. | All builders |
| `phase-1-scope.md` | Explicit Phase 1 inclusions, exclusions, assumptions, and deferred capabilities. | Product + engineering leads |
| `module-boundaries.md` | Which platform module owns which behavior. | Tech leads |
| `event-contracts.md` | Events emitted/consumed across modules. | Backend/platform engineers |
| `orchestrator-rules.md` | Rules that create Work Orders from orchestration item state changes. | Orchestrator + Runtime teams |
| `scenario-catalog.md` | Minimal Phase 1 scenarios by Track, Workspace, trigger, input, and output. | Scenario Authoring + Runtime teams |
| `repository-contracts.md` | Minimal data ownership, storage, IDs, and API contracts for Phase 1 entities. | Management + repository service teams |
| `api-surface.md` | API contracts exposed by modules and consumed by web/IDE/runtime. | Full-stack engineers |
| `ui-module-contracts.md` | Which console/page calls which module APIs and with what state model. | Web App + platform teams |
| `governance-mvp.md` | Required Phase 1 governance gates, evidence, verdicts, and rejection behavior. | Governance + Orchestrator teams |
| `workspace-runtime-contracts.md` | Workspace Session, Work Order attachment, context assembly, task execution, and completion contracts. | Runtime + IDE teams |
| `observability-and-audit.md` | Logs, traces, audit events, and operational dashboards needed for Phase 1. | Platform Ops + Governance |
| `open-questions.md` | Current unanswered questions, organized by logical build area. | Product + engineering leads |

## Recommended order for preparing the docs

1. **`golden-path.md`** — define one concrete working path.
2. **`phase-1-scope.md`** — freeze what is and is not included.
3. **`module-boundaries.md`** — assign ownership.
4. **`event-contracts.md`** and **`orchestrator-rules.md`** — make module integration possible.
5. **`scenario-catalog.md`** — define executable work.
6. **`repository-contracts.md`** and **`api-surface.md`** — define data and APIs.
7. **`governance-mvp.md`** — define gates and evidence.
8. **`ui-module-contracts.md`** and **`workspace-runtime-contracts.md`** — wire user flows to modules.
9. **`observability-and-audit.md`** — make the system operable and auditable.

## Relationship to existing docs

| Existing source | How Phase 1 docs should use it |
|-----------------|--------------------------------|
| [../../ace/](../../ace/README.md) | Source of ACE concepts and execution model. |
| [../../ace/how-product-evolves/](../../ace/how-product-evolves/README.md) | Practitioner framing for Discovery, Build, and orchestration items. |
| [../../product-information-model/](../../product-information-model/README.md) | Source of UPIM entities and lifecycles. |
| [../orchestrator/](../orchestrator/README.md) | Coordination module concepts. |
| [../work-order-runtime/](../work-order-runtime/README.md) | Execution module concepts. |
| [../foundry-web-app/](../foundry-web-app/README.md) | Web app surfaces and personas. |
| [../scenario-authoring/](../scenario-authoring/README.md) | Scenario catalog structure. |

## Current status

This folder currently contains the outline and open questions. It is not yet a build contract. Teams should use [open-questions.md](open-questions.md) to converge on the missing decisions before implementation begins.
