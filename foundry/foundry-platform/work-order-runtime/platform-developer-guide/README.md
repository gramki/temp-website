# Work Order Runtime — Foundry Platform developer guide

This guide contains implementation specifications for engineers building the **Work Order Runtime** components of the Foundry Platform.

## Implementation overview

Work Order Runtime is the execution engine — context compilation, agent spawning, task tree management, Jira integration, human-task surfacing, and Workspace Session management. It runs as a daemon within each Workspace Session.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|----------------------------|
| [Work Order](../../ace/concepts.md) | Executes WOs as units of work |
| [Scenario](../../ace/concepts.md) | Reads Scenario definitions; spawns agents per Scenario |
| [Task](../../ace/concepts.md) | Manages Agent Tasks and Human Tasks within WOs |
| [Agent](../../ace/concepts.md) | Spawns Employed Agents with context and skills |

## Specification index

| Document | Scope |
|----------|-------|
| [requirements.md](requirements.md) | Implementation requirements (APIs, database, observability) |
| [task-execution.md](task-execution.md) | Task tree, state machine, Jira representation |
| [agent-spawning.md](agent-spawning.md) | Harness preparation and agent spawning |
| [ide-integration.md](ide-integration.md) | VS Code plugin architecture |
| [implementation-todos.md](implementation-todos.md) | Open items for engineering |
| [design-discussions/control-plane-and-agent-interfaces.md](design-discussions/control-plane-and-agent-interfaces.md) | Control plane options and agent interface patterns |
| [design-discussions/agent-harness-comparison.md](design-discussions/agent-harness-comparison.md) | Comparative analysis of agent harness projects |

## Dependencies

| Module / foundation | Integration |
|---------------------|-------------|
| [Orchestrator](..//orchestrator/platform-developer-guide/) | Creates Work Orders; receives completion notifications |
| [Agent Fabric](..//agent-fabric/platform-developer-guide/) | Skills, Capable Agents, gateway policy |
| [Management](..//management/platform-developer-guide/) | Workbench provisioning; Scenario resolution |

## Related documentation

- [Module concepts](../README.md) — scope, boundaries, and documentation index
- [Work Order Runtime user guide](../user-guide/) — Work Order lifecycle walkthrough
- [Foundry Platform README](../../README.md) — platform-wide module map and spec authoring rules
