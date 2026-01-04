# Automation Runtimes

> **Status:** 🔴 Stub — Placeholder for expansion

Automation Runtimes are the engines that execute Operations (Procedures, Workflows, Cases) on Requests. They are channel-agnostic—a Request looks the same regardless of which I/O Gateway originated it.

---

## Architectural Role

```
┌─────────────────────────────────────────────────────────────────┐
│                     I/O GATEWAYS                                 │
│   (Atropos, Cronus, Heracles, Dia, Kale)                        │
└────────────────────────┬────────────────────────────────────────┘
                         │ Signal → Trigger → Request
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   AUTOMATION SYSTEMS                             │
│                                                                  │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│   │ Atlantis │  │ Perseus  │  │  Rhea    │  │Chronoshift│       │
│   │(Container)│ │ (Batch)  │  │ (BPMN)   │  │(Temporal) │       │
│   └──────────┘  └──────────┘  └──────────┘  └──────────┘       │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │              Seer Case Automation                         │  │
│   │        (AI Agent-driven Case Management)                  │  │
│   └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Automation Runtime Inventory

| System | Type | Operation Types | Description | Status |
|--------|------|-----------------|-------------|--------|
| [Atlantis](./atlantis-runtime.md) | Container Runtime | Procedures, Decision Apps, Prediction Apps | Knative/KServe-based runtime | 🔴 Stub |
| [Perseus](./perseus-batch-processing.md) | Batch Processing | File Apps, Map-Reduce, Complex Event Apps | Batch and event processing host | 🔴 Stub |
| [Rhea](./rhea-workflow-engine.md) | Workflow Engine | Deterministic Workflows | BPMN workflow host | 🔴 Stub |
| [ChronoShift](./chronoshift-temporal.md) | Durable Workflow | Long-running Operations, Cases | Temporal-based workflow host | 🔴 Stub |
| [Seer Case](./seer-case-automation.md) | AI Case Automation | Non-deterministic Cases | Seer Agent Engine for agentic case management | 🔴 Stub |

---

## Common Responsibilities

All Automation Runtimes share these responsibilities:

### 1. Operation Instantiation
- Receive standardized Requests from I/O Gateways
- Instantiate the appropriate Operation (Procedure, Workflow, Case)
- Manage Operation lifecycle (active → completed → archived)

### 2. Activity Execution
- Execute Activities within Operations
- Coordinate between Tasks and Actions
- Handle branching, looping, and conditional logic

### 3. Task Management Integration
- Create Tasks for human and AI agents
- Integrate with Task Management System for assignment
- Receive Task completion signals

### 4. State Management
- Persist Operation state
- Support resume after failure
- Enable audit and replay

### 5. Hub Integration
- Report Operation status to Hub
- Emit events for Observability
- Integrate with CAF for decision audit

---

## Operation Types by System

| Operation Type | Best System | Characteristics |
|----------------|-------------|-----------------|
| **Procedure** | Atlantis | Stateless, single-step, deterministic |
| **Decision Application** | Atlantis | Stateless, ML model invocation |
| **Workflow** | Rhea | Multi-step, deterministic, BPMN-modeled |
| **Long-running Workflow** | ChronoShift | Multi-step, durable, retryable |
| **Case** | ChronoShift or Seer Case | Non-deterministic, evolving, collaborative |
| **AI-driven Case** | Seer Case | Agent-orchestrated, goal-driven |
| **Batch Processing** | Perseus | File-based, map-reduce patterns |

---

## Hub Application

Each Automation Runtime may give a specialized name to the "Hub Application" concept:

| System | Hub Application Equivalent |
|--------|---------------------------|
| Atlantis | Procedure Definition |
| Perseus | Batch Job Definition |
| Rhea | BPMN Process Definition |
| ChronoShift | Temporal Workflow Definition |
| Seer Case | Case Specification |

---

## Related Documentation

- [Hub Architecture](../../02-system-design/hub-architecture.md) — System context
- [Ontology - Automation Layer](../../01-concepts/ontology-4-automation-layer.md) — Conceptual foundation
- [Signal Providers](../signal-providers/README.md) — I/O Gateway integration

---

*TODO: Expand each Automation Runtime document with detailed design*

