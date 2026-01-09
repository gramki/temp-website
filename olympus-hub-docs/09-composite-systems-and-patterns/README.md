# Composite Systems and Patterns

> **Status:** 🟡 WIP — Patterns for composing Hub components

## Overview

Olympus Hub is designed as a **composable platform** where Workbenches, Scenarios, and Automations can be combined, nested, and reused to create sophisticated operational solutions. This section documents the patterns and architectural approaches for building composite systems.

---

## The Composite Philosophy

Hub's composability is built on several core principles:

### 1. Components as First-Class Citizens

Every Hub component can participate in multiple roles:

| Component | Can Act As |
|-----------|------------|
| **Scenario** | Agent, Tool, Signal Provider |
| **Workbench** | Machine, Service Endpoint |
| **Hub Application** | Tool for other applications |

### 2. Interface Alignment

Composite patterns work because Hub components expose standard interfaces:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    INTERFACE ALIGNMENT PRINCIPLE                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────┐     Standard Interface     ┌─────────────────┐        │
│   │                 │  ━━━━━━━━━━━━━━━━━━━━━━━▶  │                 │        │
│   │  HUB COMPONENT  │                            │  CONSUMING      │        │
│   │  (Provider)     │  ◀━━━━━━━━━━━━━━━━━━━━━━━  │  COMPONENT      │        │
│   │                 │     Standard Interface     │                 │        │
│   └─────────────────┘                            └─────────────────┘        │
│                                                                              │
│   Examples:                                                                  │
│   • Scenario exposes Agent REST Interface → Can be employed in Task Queues  │
│   • Scenario exposes Tool Interface → Can be invoked by Hub Applications    │
│   • Workbench exposes Machine Interface → Can be used by other Workbenches  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 3. Separation of Orchestration and Execution

Composite patterns maintain clear boundaries:

- **Orchestrating Component**: Initiates, coordinates, receives results
- **Executing Component**: Performs work, returns outcomes
- **Contract**: Well-defined interface between them

### 4. Identity and Security

Each composite relationship is secured through:

- IAM identities for components acting as agents
- Bot tokens for machine-to-machine communication
- Scoped permissions matching the composite role

---

## Pattern Categories

### Scenario Composition Patterns

Patterns where Scenarios participate in or invoke other Scenarios:

| Pattern | Description | Use Case |
|---------|-------------|----------|
| [Scenario as an Agent](./scenario-as-an-agent.md) | A Scenario enrolled as an Agent in another Scenario's task queue | Automating tasks (rule-based, workflow, AI, or other) in pre-existing Scenarios |
| [Scenario as a Tool](./scenario-as-a-tool.md) | A Scenario invocable as a Tool by Hub Applications | Reusing complex automation as callable procedures |
| *Scenario Chaining* | One Scenario triggering another upon completion | Multi-phase processes with different automation needs |

### Workbench Composition Patterns

Patterns where Workbenches interact with or consume other Workbenches:

| Pattern | Description | Use Case |
|---------|-------------|----------|
| [Workbench as a Machine](./workbench-as-a-machine.md) | A Workbench registered as a Machine in another Workbench | Cross-domain operations, shared services |
| [DevOps Workbench](./devops-workbench/README.md) | A dedicated Workbench automating development activities | Agentic automation of development persona workflows |
| *Federated Workbenches* | Multiple Workbenches collaborating on shared Requests | Enterprise-wide processes spanning departments |

### Application Composition Patterns

Patterns for composing Hub Applications:

| Pattern | Description | Use Case |
|---------|-------------|----------|
| *Application as a Tool* | Hub Application callable as a Tool | Reusing application logic across Scenarios |
| *Nested Workflows* | Workflows invoking other workflows | Complex processes with reusable sub-processes |

---

## When to Use Composite Patterns

### Use Composite Patterns When:

1. **Existing Automation Exists** — You have pre-existing Scenarios that work well and don't want to modify them
2. **Separation of Concerns** — Different teams own different parts of the process
3. **Flexibility Required** — You want to mix human and automated execution dynamically
4. **Reuse is Valuable** — The same automation can serve multiple Scenarios
5. **Gradual Automation** — You're incrementally automating tasks in a larger process

### Avoid When:

1. **Single Responsibility** — The entire process fits naturally in one Scenario
2. **Tight Coupling** — Components need real-time, synchronous, low-latency interaction
3. **Simple Processes** — Overhead of composition exceeds value
4. **No Reuse** — Automation is specific to one context

---

## Composite Pattern Architecture

All composite patterns share common architectural elements:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COMPOSITE PATTERN ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                     CONSUMING CONTEXT                                  │  │
│  │                                                                        │  │
│  │   Workbench A / Scenario A / Application A                            │  │
│  │                                                                        │  │
│  │   ┌─────────────────────────────────────────────────────────────────┐ │  │
│  │   │  1. Discovery    — Find available composite components          │ │  │
│  │   │  2. Binding      — Establish relationship at deployment time    │ │  │
│  │   │  3. Invocation   — Trigger the composite component at runtime   │ │  │
│  │   │  4. Observation  — Receive updates from composite component     │ │  │
│  │   │  5. Completion   — Process results from composite component     │ │  │
│  │   └─────────────────────────────────────────────────────────────────┘ │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                    │                                         │
│                                    │ Standard Interface                      │
│                                    ▼                                         │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                     PROVIDING CONTEXT                                  │  │
│  │                                                                        │  │
│  │   Workbench B / Scenario B / Application B                            │  │
│  │                                                                        │  │
│  │   ┌─────────────────────────────────────────────────────────────────┐ │  │
│  │   │  1. Registration — Publish as composite-ready component         │ │  │
│  │   │  2. Identity     — IAM identity for the composite role          │ │  │
│  │   │  3. Reception    — Receive invocations via standard interface   │ │  │
│  │   │  4. Execution    — Process the work within own context          │ │  │
│  │   │  5. Reporting    — Send updates/results to consuming context    │ │  │
│  │   └─────────────────────────────────────────────────────────────────┘ │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Related Documentation

- [Developer Operators](../04-subsystems/operators/developer-operators.md) — Operators for composite patterns
- [Task Management](../04-subsystems/task-management/README.md) — Task queues and agent enrollment
- [Signal Exchange](../04-subsystems/signal-exchange/README.md) — Signal-based integration
- [REST Channels](../06-ux-architecture/tenant-domain/rest-channels.md) — Agent REST APIs

---

## Pattern Index

| Pattern | Status | Description |
|---------|--------|-------------|
| [Scenario as an Agent](./scenario-as-an-agent.md) | 🟡 Draft | Expose Scenario (any automation type) as an Agent for task completion |
| [Scenario as a Tool](./scenario-as-a-tool.md) | ✅ Documented | Expose Scenario as a callable Tool for Hub Applications |
| [Hub Application as Standalone Tool](./hub-application-as-standalone-tool.md) | 🟡 Draft | Hub Application as directly invocable tool (workbench = machine) |
| [Workbench as a Machine](./workbench-as-a-machine.md) | 🟡 Draft | Expose Workbench as a Machine for cross-workbench tool invocation |
| [DevOps Workbench](./devops-workbench/README.md) | 🟡 Draft | Automate development workflows with AI-assisted agents |


