# Phase 1 Open Questions

Remaining decisions not yet captured in Phase 1 build contracts. Resolved questions live in the linked docs — do not re-decide here.

| Resolved in | Covers |
|-------------|--------|
| [phase-1-scope.md](phase-1-scope.md) | Tracks, OIs, integrations, success criteria, real vs mocked |
| [golden-path.md](golden-path.md) | End-to-end sequence, actors, demo script |
| [module-boundaries.md](module-boundaries.md) | Module ownership for entities and flows |
| [scenario-catalog.md](scenario-catalog.md) | Phase 1 scenario set |
| [governance-mvp.md](governance-mvp.md) | Transition gates; deferred governance scope |
| [repository-contracts.md](repository-contracts.md) | Entity storage, `workRepo*` fields, `foundry-*` labels, artifact URIs |
| [api-surface.md](api-surface.md) | Repo-based artifact routes vs track-based work-item routes |
| [event-contracts.md](event-contracts.md) | Atropos paths, event envelope, delivery semantics, minimum gate events |
| [orchestrator-rules.md](orchestrator-rules.md) | State store, retry semantics, workflow versioning, cross-track handoff |
| [workspace-runtime-contracts.md](workspace-runtime-contracts.md) | Session ↔ WO attachment, parallel scheduling, context compilation, Git branches |

---

## UI-to-module contracts

- Exact API calls per Web App console (PI Console, Workspaces Console, Track Console)
- Which governance consoles exist in Phase 1 UI vs read-only/deferred
- IDE extension surface for scenario authoring and Personal Work
- Loading, error, and stale-state UX requirements per console

## Traceability

- Minimum graph query API for Phase 1 (parent/child only vs full traversal)
- Whether traceability is computed on demand or materialized
- Which maps (Executive Strategy, PM Intent, Delivery Execution) are named but not built

## Discovery and Product Intent product rules

- Discovery Case status enum for Phase 1 UI (full UPIM set vs workflow stages only?)
- PM alignment field representation for PDR (approval event vs signature vs comment)
- Product Intent purpose enum — when to add Discovery Support and other purposes post-Phase 1
- Kill and Pivot PDR behavior on golden path (out of scope or manual?)

## Governance (deferred detail)

- When to implement Governance Ritual track and which rituals first
- Control Objective / Indicator model and BQO/BQI aliasing
- Debt Register, Exception/Waiver lifecycle
- Release Readiness Review as formal ritual vs transition gates only

## Security and tenancy

- Customer-bank builder scoping in multi-tenant demo
- Agent permission model vs human permission model
- Audit record schema per governed action

## Observability

- Required metrics per module for Phase 1 (Orchestrator throughput, WO duration, session count)
- End-to-end trace: one Product Intent from creation to delivery
- Minimum audit dashboard

---

When a question is answered, move the decision into the appropriate Phase 1 doc and remove it from this list.
