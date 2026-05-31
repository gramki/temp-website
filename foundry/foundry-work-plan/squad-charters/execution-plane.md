# Squad Charter — Execution Plane

**Stream:** Execution Plane  
**Squad lead:** TBD

## Purpose

Build the **runtime where work happens**: Workspace Sessions, Work Order execution, agent employment, and Git automation per Work Order. When Orchestrator assigns a WO, this stream makes it runnable in a builder's session.

## Boundaries

### In scope

- [Workspace Session Infrastructure](../../foundry-platform/workspace-session-infrastructure/README.md) — K8s pods, Coder, networking, IDE extension packaging
- [Workspace Session Management](../../foundry-platform/workspace-session-management/README.md) — session lifecycle control plane
- [Work Order Runtime](../../foundry-platform/work-order-runtime/README.md) — task graph, management-plane interface, context compilation, Personal Work, Git per-WO branches
- [Agent Fabric](../../foundry-platform/agent-fabric/README.md) — **minimal Phase 1**: skill registry lookup, one capable-agent routing path, stub skills acceptable

### Out of scope

- OI workflow logic — Control Plane
- Work Catalog content — Work Catalog Authoring
- Web App / IDE feature UX — Builder Experience (consumes Runtime APIs)
- Foundry CI on product repos — Release Engineering

## Phase 1 deliverables

| Milestone | Deliverable |
|-----------|-------------|
| M0 | Session Infrastructure can provision a pod (hello-world session) |
| M1 | Full WO execution loop; Git branch; completion event |
| M2 | Execute all Build-track WOs on golden path |
| M3 | Execute all Discovery-track WOs including parallel groups |
| M4 | Governance WO execution; evidence attachment on WO outputs |
| M5 | Stable enough for unattended demo |

## Dependencies

| Depends on | For |
|------------|-----|
| Control Plane | WO creation events; session assignment; entity context |
| Work Catalog Authoring | Scenario definitions Runtime executes |
| Builder Experience | IDE integration for task/human-task APIs |
| Release Engineering | CI triggered from Development WO outputs (M2+) |

## Interfaces

See [../integration/contract-gates.md](../integration/contract-gates.md). This stream **produces**:

- Session lifecycle API (create, active, stopping, stopped)
- WO Runtime task APIs (IDE-facing)
- `work-order-completed` / `work-order-failed` events
- Git operations under `work-orders/WO-{id}/`

This stream **consumes**:

- WO assignment from Orchestrator
- Resolved scenario definition (via Runtime startup context)
- Skill/agent routing from Agent Fabric

## Backlog themes

- WSI: pod spec, Coder wildcard proxy, tenant isolation
- WSSM: lifecycle state machine, URL registry
- WOR: management-plane protocol, task manager, local state, workspace-local tasks, ide-integration
- Agent Fabric: minimal skill registry + employment path
- Git: per-WO branch policy per Management git-infrastructure spec

## Read next

- [../milestones.md](../milestones.md)
- [../phase-1/golden-path.md](../phase-1/golden-path.md) — Part C session flow
- [../../foundry-platform/work-order-runtime/README.md](../../foundry-platform/work-order-runtime/README.md)
