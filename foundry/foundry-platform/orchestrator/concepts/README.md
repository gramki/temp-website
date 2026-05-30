# Orchestrator Concepts

This folder contains module-specific concept definitions for the Foundry Orchestrator. These concepts describe Orchestrator internals — components, patterns, and mechanisms that belong to this module.

## How to use these concepts

- **Module-scoped.** These concepts explain Orchestrator implementation details.
- **Link to platform concepts.** When a concept references a platform-wide construct (Work Order, Scenario, etc.), link to [../concepts/](../../concepts/).
- **Complement, don't duplicate.** If you need to explain what a Work Order *is*, link to the platform concept. If you need to explain how the Orchestrator *creates* Work Orders, that's module-specific.

## Concept Index

| Concept | Definition |
|---------|------------|
| [Workflow Engine](workflow-engine.md) | Event-driven processor that evaluates OI Workflow definitions and invokes handlers |
| [Action Executor](action-executor.md) | Component that executes workflow actions: creating WOs, transitioning items, invoking governance |
| [Work Order Group](work-order-group.md) | Mechanism for atomically creating and tracking multiple parallel Work Orders |
| [Dead Letter Queue](dead-letter-queue.md) | Queue for failed workflow actions requiring manual intervention |
| [Gate Enforcement](gate-enforcement.md) | Mechanism that blocks or allows orchestration item transitions based on governance verdicts |

## Relationship to Platform Concepts

These module concepts build on platform-wide concepts defined in [../../concepts/](../../concepts/):

| Platform Concept | Orchestrator Realization |
|------------------|--------------------------|
| [Work Order](../../concepts/work-order.md) | Created by Action Executor via `create-work-order` |
| [Scenario](../../concepts/scenario.md) | Referenced in workflow actions; validated before WO creation |
| [Orchestration Item](../../concepts/orchestration-item.md) | Routed through stages by Workflow Engine |
| [Governance](../../concepts/governance.md) | Invoked via Gate Enforcement at transitions |

## Read next

- [workflow-engine.md](workflow-engine.md) — Core execution loop
- [../README.md](../README.md) — Module overview and architecture
- [../../concepts/README.md](../../concepts/README.md) — Platform-wide concepts
