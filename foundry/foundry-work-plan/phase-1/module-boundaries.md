# Phase 1 Module Boundaries

Which platform module owns which behavior for Phase 1. Definitive module specs live under [../../foundry-platform/](../../foundry-platform/README.md); this document is the Phase 1 assignment summary.

## Entity ownership

| Entity / behavior | Owner module | Notes |
|-------------------|--------------|-------|
| Workshop, Workbench provisioning | **Management** | Declarative provisioning; GitHub App, Jira project setup |
| Repository metadata and access APIs | **Management** | Repositories are services; Management exposes access layer |
| ID generation (OI, WO, PDR, etc.) | **Management** (Metadata Service) | IDs assigned before artifact creation |
| Work Catalog schema, validation, resolution | **Management** (Work Catalog Management) | Engine; definitions in Work Catalogues folder |
| Discovery Case record | **Management** + **Work Repository** | Dual: Work Item + Intent Repository artifact; optional `sourceRefs[]` |
| Discovery Case lifecycle transitions | **Orchestrator** | Driven by Discovery Case workflow |
| PDR record | **Management** + **Intent Repository** | Artifact-only (no Work Item) |
| Product Intent record | **Management** + **Intent Repository** + **Work Repository** | Dual: artifact folder + Build-track Work Item |
| Product Intent lifecycle transitions | **Orchestrator** | Driven by Product Intent workflow |
| PSD metadata and artifact registration | **Management** + **Intent Repository** | Git-backed specification artifacts |
| Work Order creation (orchestrated) | **Orchestrator** | Via workflow `create-work-order` actions |
| Work Order creation (manual / Personal Work) | **WO Runtime** | Personal Work and ad-hoc WOs |
| Work Order execution and task lifecycle | **WO Runtime** | In-session worker |
| Work Order assignment discovery | **Orchestrator** (assign) + **WO Runtime** (discover via events) | |
| Scenario catalog content | **Work Catalogues** (definitions) + **Management** (resolution) | Platform defaults shipped; overrides at Foundry/Workshop/Workbench |
| Workspace Session lifecycle | **Session Management** | Control plane |
| Session pod provisioning | **Session Infrastructure** | K8s + Coder |
| Governance scenario definition | **Work Catalogues** | Governance station scenarios |
| Governance scenario invocation | **Orchestrator** | `invoke-governance-scenario` at transitions |
| Governance verdict storage | **Management** + evidence repositories | Verdict as governance event + artifact |
| Evidence attachment | **WO Runtime** (during WO) + **Management** (retrieval) | |
| Agent skills and capable agents | **Agent Fabric** | |
| Agent employment within WO | **WO Runtime** | Spawns employed agents |
| Git clone, branch, push, PR | **WO Runtime** + **Git Infrastructure** (Management spec) | Per-WO branch model |
| Builder IDE experience | **IDE** | Extensions packaged via Session Infrastructure |
| Web App consoles | **Foundry Web App** | Calls Management, Orchestrator, Session APIs |
| OI / WO state persistence | **Orchestrator** (Postgres per orchestrator README) | Not in Management entity store |
| Audit trail | **Each module** emits; aggregated for Phase 1 query | Full Platform Ops deferred |

## Cross-module flows

### Discovery Case creation

```text
Web App → Management API (create Work Item via track route)
       → Optional Intent Repository artifact (repo route)
       → Orchestrator (`orchestration-item-created`; may re-publish on Atropos)
       → Workflow engine (start → discovery-initiated)
       → create-work-order (frame-discovery-case)
       → Session Management (query/create session; emits `session-activated` on Atropos)
       → WO Runtime (execute WO)
```

### Discovery → Build handoff

```text
Orchestrator (user-task-completed: proceed-to-build)
       → create-orchestration-item (track: build, seed-from: discovery-case)
       → Product Intent workflow (start → draft-ready)
```

### WO completion → OI advance

```text
WO Runtime → Atropos: /{foundry-id}/foundry.wo-runtime.work-order-completed
Orchestrator → workflow handler → transition-orchestration-item / create-work-order / invoke-governance-scenario
```

## Boundaries to preserve

| Must not cross | Rule |
|----------------|------|
| Orchestrator → execute tasks | Orchestrator creates WOs; WO Runtime executes |
| WO Runtime → transition OI | WO Runtime emits completion; Orchestrator transitions |
| Session Management → know about WOs | Session Management owns lifecycle only; Orchestrator assigns |
| Work Catalogues → implement resolution | Definitions only; Management WCM resolves |
| IDE → orchestrate | IDE surfaces work; Orchestrator coordinates |

## Phase 1 module readiness

Minimum "ready for Phase 1 engineering" per module:

| Module | Ready when |
|--------|------------|
| **Management** | Workbench provisioned; Metadata Service serves IDs; WCM resolves platform defaults; Validation gates config repos |
| **Orchestrator** | Runs Discovery + Build workflows; creates WOs; invokes governance; handles cross-track handoff |
| **WO Runtime** | Executes task graph; management-plane ack; Git per-WO branches; Personal Work |
| **Session Infrastructure** | Provisions pod; serves IDE URL |
| **Session Management** | Lifecycle API consumed by Orchestrator and WO Runtime |
| **IDE** | Work Orders panel, task graph, session entry |
| **Agent Fabric** | Skill registry lookup; at least one capable agent routable |
| **Web App** | Create Discovery Case; list OIs; show WO status; basic traceability |
| **Release Tools** | CI runs on product repo PR (build/test) |

## Read next

- [event-contracts.md](event-contracts.md) — Atropos paths and event envelope SSOT
- [orchestrator-rules.md](orchestrator-rules.md) — state store, retry, workflow versioning, cross-track handoff
- [golden-path.md](golden-path.md) — where these boundaries show up in the demo
- [../../foundry-platform/orchestrator/README.md](../../foundry-platform/orchestrator/README.md) — Orchestrator spec
- [../../foundry-platform/work-order-runtime/README.md](../../foundry-platform/work-order-runtime/README.md) — WO Runtime spec
- [repository-contracts.md](repository-contracts.md) — entity and storage SSOT
- [api-surface.md](api-surface.md) — route split (artifacts vs work items)
