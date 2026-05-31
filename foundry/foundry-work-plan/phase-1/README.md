# Foundry Work Plan — Phase 1

Implementation-readiness workspace for **Phase 1 of the Foundry Platform**. For product and engineering teams building the platform — not ACE theory.

## Build question

> Can Foundry take a product-relevant discovery question, form Product Intent, refine it into buildable work, execute Workspace Work Orders, govern transitions, and publish Product Delivery with traceability?

## Documentation

| Document | Status | Purpose |
|----------|--------|---------|
| [phase-1-scope.md](phase-1-scope.md) | **Draft** | Inclusions, exclusions, assumptions, success criteria |
| [golden-path.md](golden-path.md) | **Draft** | End-to-end demo path step by step |
| [module-boundaries.md](module-boundaries.md) | **Draft** | Which module owns which Phase 1 behavior |
| [scenario-catalog.md](scenario-catalog.md) | **Draft** | Phase 1 scenarios mapped to platform defaults |
| [governance-mvp.md](governance-mvp.md) | **Draft** | Transition gates and deferred governance scope |
| [open-questions.md](open-questions.md) | Living | Remaining decisions not yet in build contracts |
| [repository-contracts.md](repository-contracts.md) | **Authoritative** | Entity storage, `workRepo*` fields, labels, artifact URIs |
| [api-surface.md](api-surface.md) | **Authoritative** | Repo-based vs track-based HTTP routes |
| [event-contracts.md](event-contracts.md) | **Authoritative** | Atropos paths, event envelope, minimum gate events |
| [orchestrator-rules.md](orchestrator-rules.md) | **Authoritative** | State store, retry, workflow versioning, cross-track handoff |
| [workspace-runtime-contracts.md](workspace-runtime-contracts.md) | **Authoritative** | Session ↔ WO, parallel scheduling, context compilation, Git branches |

### Still to write

| Document | Purpose |
|----------|---------|
| `ui-module-contracts.md` | Console → API mapping |
| `observability-and-audit.md` | Logs, metrics, audit trail for Phase 1 |

Entity, API, event, orchestrator, and workspace runtime contracts are authoritative in `repository-contracts.md`, `api-surface.md`, `event-contracts.md`, `orchestrator-rules.md`, and `workspace-runtime-contracts.md`.

## Scope anchor

Phase 1 exercises Discovery → Build with transition governance:

```text
Discovery Case → research → PDR → proceed-to-build
  → Product Intent → specification → UX → development → QA → release
  → governance evidence at each transition
```

Platform default workflows: [../../foundry-platform/work-catalogues/platform-defaults/work-catalog/discovery/discovery-case/](../../foundry-platform/work-catalogues/platform-defaults/work-catalog/discovery/discovery-case/), [../../foundry-platform/work-catalogues/platform-defaults/work-catalog/build/product-intent/](../../foundry-platform/work-catalogues/platform-defaults/work-catalog/build/product-intent/).

## Relationship to existing docs

| Source | Use for |
|--------|---------|
| [../../ace/](../../ace/README.md) | ACE concepts and execution model |
| [../../ace/how-product-evolves/](../../ace/how-product-evolves/README.md) | Discovery and Build practitioner framing |
| [../../product-information-model/](../../product-information-model/README.md) | UPIM entities and lifecycles |
| [../../foundry-platform/](../../foundry-platform/README.md) | Module specs and platform concepts |
| [../../foundry-platform/work-catalogues/](../../foundry-platform/work-catalogues/README.md) | Work Catalog definitions |
| [../../tldr-faq.md](../../tldr-faq.md) | Platform design decisions |

## Read next

- [../people-plan.md](../people-plan.md) — team structure and streams
- [../milestones.md](../milestones.md) — M0–M5 delivery sequence
- [phase-1-scope.md](phase-1-scope.md) — start here for scope
- [golden-path.md](golden-path.md) — the demo path
