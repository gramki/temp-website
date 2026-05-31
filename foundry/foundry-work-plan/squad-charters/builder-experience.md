# Squad Charter — Builder Experience

**Stream:** Builder Experience  
**Squad lead:** TBD

## Purpose

Build the **surfaces builders and PMs use**: IDE extensions for in-session work, and Web App consoles for orchestration visibility, OI management, and traceability.

## Boundaries

### In scope

- [Foundry IDE](../../foundry-platform/ide/README.md) — work orders panel, task graph, employed agents, Foundry workspace panel, scenario authoring (user catalog), session entry
- [Foundry Web App](../../foundry-platform/foundry-web-app/README.md) — PI/Track Console, Workspaces Console, basic governance verdict views, traceability (M4)

### Out of scope

- Orchestrator workflow engine — Control Plane
- WO execution internals — Execution Plane
- Work Catalog platform defaults authoring — Work Catalog Authoring
- Foundry Platform Admin Web App (minimal only if needed for demo setup)
- Release Tools / CI — Release Engineering

## Phase 1 deliverables

| Milestone | Deliverable |
|-----------|-------------|
| M1 | IDE: work orders list, human task completion, session open |
| M2 | Web App: create/list Product Intent; show OI stage; IDE task graph |
| M3 | Web App: create Discovery Case; decision gate UI |
| M4 | Governance verdict display; traceability chain view |
| M5 | Demo-polished UX; error/loading states on golden-path screens |

## Dependencies

| Depends on | For |
|------------|-----|
| Control Plane | Entity/OI APIs, traceability query |
| Execution Plane | Session URL, WO/task APIs |
| Integration lead | E2E flows for UX acceptance |

Can start with **mock APIs** before M1; must integrate by M2.

## Interfaces

See [../integration/contract-gates.md](../integration/contract-gates.md). This stream **consumes**:

- Management entity APIs (Discovery Case, Product Intent, PDR)
- Orchestrator OI stage / user task APIs
- Session Management + WO Runtime (IDE)
- Traceability query (M4)

Detailed console → API mapping: pending `phase-1/ui-module-contracts.md`.

## Backlog themes

- IDE: builder, task-graph-view, employed-agents-panel, foundry-workspace-panel, workspace-sessions user guide flows
- Web App: persona consoles per [foundry-web-app/user-guide/personas/](../../foundry-platform/foundry-web-app/user-guide/personas/README.md)
- UX requirements: [ide/platform-developer-guide/ux-requirements.md](../../foundry-platform/ide/platform-developer-guide/ux-requirements.md)

## Read next

- [../milestones.md](../milestones.md)
- [../phase-1/golden-path.md](../phase-1/golden-path.md) — actors and surfaces per step
- [../../foundry-platform/ide/README.md](../../foundry-platform/ide/README.md)
