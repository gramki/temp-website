# Foundry Orchestrator — Foundry Platform developer guide

This guide contains implementation specifications for engineers building the **Foundry Orchestrator** components of the Foundry Platform.

## Implementation overview

The Orchestrator coordinates Track-scoped orchestration items through Workspaces — creating Workspace Work Orders, invoking Governance Scenarios, and enforcing gates. Workflows are sourced from the Work Catalog with hierarchical resolution.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|----------------------------|
| [Track](../../ace/concepts.md) | Routes orchestration items through Track-specific flows |
| [Workspace](../../ace/workspaces/README.md) | Creates Work Orders when items reach Workspaces |
| [Governance](../../ace/governance.md) | Invokes Governance Scenarios at transition gates |
| [Work Order](../../ace/concepts.md) | Creates WOs; does not execute them |

## Specification index

| Document | Scope |
|----------|-------|
| [requirements.md](requirements.md) | Detailed implementation requirements (architecture, APIs, scalability) |

## Dependencies

| Module / foundation | Integration |
|---------------------|-------------|
| [Management](..//management/platform-developer-guide/work-catalog-management/oi-workflow-schema.md) | OI Workflow schema |
| [Work Order Runtime](..//work-order-runtime/platform-developer-guide/) | Executes Work Orders created by Orchestrator |
| [Work Catalogues](..//work-catalogues/platform-defaults/) | Platform default OI Workflows |

## Related documentation

- [Module concepts](../README.md) — scope, boundaries, and documentation index
- [Foundry Orchestrator user guide](../user-guide/) — OI Workflow authoring and journeys
- [Foundry Platform README](../../README.md) — platform-wide module map and spec authoring rules
