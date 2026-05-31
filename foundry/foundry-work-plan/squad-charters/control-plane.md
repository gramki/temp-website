# Squad Charter — Control Plane

**Stream:** Control Plane  
**Squad lead:** TBD

## Purpose

Build and operate the **coordination and admin layer** of Foundry: provisioning, entity lifecycle, Work Catalog resolution engine, and Orchestrator workflow execution. This stream turns ACE/UPIM concepts into running state machines that create Work Orders and invoke governance.

## Boundaries

### In scope

- [Foundry Management](../../foundry-platform/management/README.md) — Workshop/Workbench provisioning, Metadata Service, repository metadata APIs, Validation, Team Management
- [Work Catalog Management](../../foundry-platform/management/platform-developer-guide/work-catalog-management/README.md) — schema, validation, resolution, sync (**engine only**)
- [Foundry Orchestrator](../../foundry-platform/orchestrator/README.md) — workflow engine, WO creation, governance invocation, cross-track handoff
- Entity APIs: Discovery Case, PDR, Product Intent, Work Order (metadata), governance verdict persistence
- OI state store (Orchestrator Postgres)

### Out of scope

- Work Catalog **content** authoring — [Work Catalog Authoring](work-catalog-authoring.md)
- In-session WO execution — [Execution Plane](execution-plane.md)
- IDE / Web App UI — [Builder Experience](builder-experience.md)
- Product repo CI — [Release Engineering](release-engineering.md)

## Phase 1 deliverables

| Milestone | Deliverable |
|-----------|-------------|
| M0 | Workbench provision; WCM resolves platform defaults; Validation gate |
| M1 | WO record API; Orchestrator accepts `work-order-completed` |
| M2 | Product Intent lifecycle; full Build workflow execution |
| M3 | Discovery Case lifecycle; parallel WO groups; cross-track handoff |
| M4 | Governance invoke/verdict; traceability query API |

## Dependencies

| Depends on | For |
|------------|-----|
| Work Catalog Authoring | Authoritative workflows/scenarios before Orchestrator implements handlers |
| Execution Plane | WO completion events; session query/create for assignment |
| Platform architect | Contract gate approval |

## Interfaces

See [../integration/contract-gates.md](../integration/contract-gates.md). This stream **produces**:

- Entity and OI CRUD APIs
- Orchestrator events (`orchestration-item-created`, stage transitions)
- WO creation and assignment
- Governance invocation and verdict storage
- Traceability query (M4)

This stream **consumes**:

- Resolved Work Catalog definitions (WCM)
- `work-order-completed` from Execution Plane
- Authoritative workflow YAML from Work Catalog Authoring

## Backlog themes

Reference module requirements — do not duplicate FR lists here.

- Management: provisioning, Metadata Service, git-infrastructure alignment
- WCM: resolution hierarchy, validation on publish
- Orchestrator: workflow engine, action executor, user tasks, WO groups, `create-orchestration-item`
- Entity schemas (pending `phase-1/repository-contracts.md`)

## Read next

- [../milestones.md](../milestones.md)
- [../phase-1/module-boundaries.md](../phase-1/module-boundaries.md)
- [../../foundry-platform/orchestrator/README.md](../../foundry-platform/orchestrator/README.md)
