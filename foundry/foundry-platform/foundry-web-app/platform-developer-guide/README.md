# Foundry Web App — Foundry Platform developer guide

This guide contains UI specifications for engineers building the **Foundry Web App** components of the Foundry Platform.

## Implementation overview

The Foundry Web App is the primary web interface for Foundry members and Foundry Admins. It consumes and surfaces capabilities from all platform modules — Work Orders, orchestration flow, admin console, Work Catalog browsing, and CI/CD status.

## Specification index

| Document | Scope |
|----------|-------|
| [pages/README.md](pages/README.md) | Page index |
| [pages/foundry-home.md](pages/foundry-home.md) | Foundry-wide dashboard |
| [pages/workshop-home.md](pages/workshop-home.md) | Workshop dashboard |
| [pages/workbench-home.md](pages/workbench-home.md) | Workbench dashboard |
| [pages/consoles/README.md](pages/consoles/README.md) | Console specifications |
| [pages/consoles/CONSOLE-GUIDE.md](pages/consoles/CONSOLE-GUIDE.md) | Console guide |

## Dependencies

| Module / foundation | Integration |
|---------------------|-------------|
| [Management](..//management/platform-developer-guide/) | Admin console, Workbench configuration |
| [Work Order Runtime](..//work-order-runtime/platform-developer-guide/) | Work Order views and Task queues |
| [Orchestrator](..//orchestrator/platform-developer-guide/) | Orchestration item flow visualization |
| [Release Tools](..//release-tools/platform-developer-guide/) | CI/CD status |

## Related documentation

- [Module concepts](../README.md) — scope, boundaries, and documentation index
- [Foundry Web App user guide](../user-guide/) — persona journeys
- [Foundry Platform README](../../README.md) — platform-wide module map and spec authoring rules
