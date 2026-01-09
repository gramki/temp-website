# Architecture Layers

> **How Hub components map to the four-layer ontology**

---

## Overview

Olympus Hub implements the four-layer ontology of Human-AI Team Operations. Each layer represents a distinct concern—from perceiving what's happening to codifying how work is done. This document shows how Hub components, specifications, and runtime elements map to these layers.

---

## The Four Layers

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  4. AUTOMATION LAYER — "How is it codified and scaled?"                     │
│                                                                              │
│     Hub Applications, Automation Runtimes, Tool Registry, Command Registry  │
├─────────────────────────────────────────────────────────────────────────────┤
│  3. EXECUTION LAYER — "How is it done?"                                     │
│                                                                              │
│     Requests, Tasks, Task Queues, Escalation Matrix, Agent Assignment       │
├─────────────────────────────────────────────────────────────────────────────┤
│  2. NORMATIVE LAYER — "What ought to be done?"                              │
│                                                                              │
│     Scenarios, Roles, Goals, SOPs, Decision Criteria, Compliance Rules      │
├─────────────────────────────────────────────────────────────────────────────┤
│  1. PERCEPTION LAYER — "What's happening?"                                  │
│                                                                              │
│     I/O Gateways, Signal Exchange, Triggers, Normalized Signals             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Layer 1: Perception — *"What's happening?"*

The Perception Layer observes and interprets reality. It captures how signals from the environment are sensed, transformed, and matched to meaningful scenarios.

### Hub Components

| Component | Purpose | Implementation |
|-----------|---------|----------------|
| **I/O Gateways** | Sense signals from specific protocols | Heracles (HTTP), Atropos (Events), Cronus (Exceptions), Dia (Files), Kale (Time) |
| **Signal Exchange** | Route and match signals to triggers | Central routing engine |
| **Triggers** | Transform signals into requests | Workbench-defined trigger configurations |
| **Normalized Signal Format** | Standard DTO for signal transport | Common envelope for all signal types |

### Implementation Concepts

- [I/O Gateway](./implementation-concepts/io-gateway.md)
- [Signal Exchange](./implementation-concepts/signal-exchange.md)
- [Normalized Signal Format](./implementation-concepts/normalized-signal-format.md)

### Example

```
Login logs show 5 failed attempts in 2 minutes
    ↓
Atropos senses "security-alert" event from identity provider
    ↓
Signal Exchange matches to "suspicious-login-trigger"
    ↓
Trigger creates "Account Security Review" Request
```

---

## Layer 2: Normative — *"What ought to be done?"*

The Normative Layer defines standards, rules, and goals that shape expected behavior. It encodes what *ought* to be done, not just what can be done.

### Hub Components

| Component | Purpose | Implementation |
|-----------|---------|----------------|
| **Scenario Normative Spec** | Define roles, goals, SOPs for a scenario | CRD owned by Process Architect |
| **SOPs** | Standardized procedures | Referenced documents and checklists |
| **Decision Criteria** | Rules for making decisions | Configured in Normative Spec |
| **Compliance Requirements** | Regulatory constraints | Part of Normative Spec |

### Specification Content

The **Scenario Normative Specification** captures:

| Element | Description |
|---------|-------------|
| **Roles** | Who is responsible (dispute-analyst, supervisor) |
| **Goals** | What outcomes must be achieved |
| **Responsibilities** | Specific duties of each role |
| **SOPs** | References to standard procedures |
| **Decision Criteria** | How to make judgment calls |
| **Evidence Requirements** | What documentation is needed |
| **Escalation Rules** | When to escalate |
| **Compliance** | Regulatory requirements |

### Implementation Concepts

- [Scenario Specification Types](./implementation-concepts/scenario-specification-types.md) (Normative section)

### Example

```yaml
# What ought to be done for "Suspicious Login"
roles:
  - name: security-analyst
    goals: ["Prevent account takeover", "Verify user identity"]
    responsibilities: ["Check login patterns", "Contact user"]
sops:
  - ref: sop-account-lockout
  - ref: sop-user-verification
```

---

## Layer 3: Execution — *"How is it done?"*

The Execution Layer is where work actually happens. Normative rules are operationalized into requests, tasks, and agent assignments.

### Hub Components

| Component | Purpose | Implementation |
|-----------|---------|----------------|
| **Request** | Instance of an operation | Created by triggers, managed through lifecycle |
| **Task** | Unit of work for an agent | Assigned via queues or direct assignment |
| **Task Queue** | Pool of available work | Skill-based, priority-ordered |
| **Escalation Matrix** | Multi-level agent assignment | Time-based and condition-based escalation |
| **Agent** | Human or AI executor | Enrolled in workbench with roles |

### Specification Content

The **Scenario Deployment Specification** captures execution-level settings:

| Element | Description |
|---------|-------------|
| **Task Queue Mappings** | Which queues handle which task types |
| **Agent Enrollment** | Which agent pools are eligible |
| **SLA Parameters** | Target completion times, warnings |
| **Activation Settings** | When the scenario is active |

### Request Lifecycle

```
Created → Acknowledged → In Progress → Pending (external) → Completed/Cancelled
```

### Implementation Concepts

- [Request Lifecycle](./implementation-concepts/request-lifecycle.md)
- [Task Allocation](./implementation-concepts/task-allocation.md)
- [Escalation Matrix](./implementation-concepts/escalation-matrix.md)
- [Scenario Specification Types](./implementation-concepts/scenario-specification-types.md) (Deployment section)

### Example

```yaml
# How work is assigned for "Suspicious Login"
task_queues:
  - task_type: investigate
    queue_ref: security-tier-1
sla:
  target_completion_hours: 4
  warning_threshold_hours: 2
agents:
  default_pool: security-analysts
```

---

## Layer 4: Automation — *"How is it codified and scaled?"*

The Automation Layer represents codified definitions of operations and the systems that run them. Automations are software representations that can be reliably repeated and scaled.

### Hub Components

| Component | Purpose | Implementation |
|-----------|---------|----------------|
| **Hub Application** | Automation artifact | Procedures, workflows, cases, agents |
| **Automation Runtime** | Execution host | Atlantis (containers), Rhea (BPMN), ChronoShift (durable) |
| **Tool Registry** | Available tools | Commands exposed by machines |
| **Command Registry** | Available commands | Actions that can be executed |

### Specification Content

The **Scenario Automation Specification** captures:

| Element | Description |
|---------|-------------|
| **Hub Application** | Which application handles this scenario |
| **Triggers** | Which triggers activate the scenario |
| **Tool Bindings** | Which tools are available |
| **Notification Templates** | How to notify participants |

### Automation Runtimes

| Runtime | Type | Use Case |
|---------|------|----------|
| **Atlantis** | Container Runtime | Procedures, Decision/Prediction Applications |
| **Perseus** | Batch Processing | File applications, map-reduce |
| **Rhea** | Workflow Engine | Deterministic BPMN workflows |
| **ChronoShift** | Durable Workflow | Long-running operations, cases |

### Implementation Concepts

- [Hub Application](./implementation-concepts/hub-application.md)
- [Automation Runtime](./implementation-concepts/automation-runtime.md)
- [Direct Tool Dispatcher](./implementation-concepts/direct-tool-dispatcher.md)
- [Scenario Specification Types](./implementation-concepts/scenario-specification-types.md) (Automation section)

### Example

```yaml
# How "Suspicious Login" is automated
application:
  ref: account-security-handler
  version: "2.1.0"
triggers:
  - ref: suspicious-login-trigger
tools:
  - name: account-lockout
    ref: identity-provider-lock
```

---

## Layer Interaction Pattern

The layers interact through a defined flow:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           RUNTIME FLOW                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   PERCEPTION                NORMATIVE              EXECUTION                 │
│                                                                              │
│   ┌─────────────┐          ┌─────────────┐        ┌─────────────┐           │
│   │   Signal    │─────────▶│  Scenario   │───────▶│   Request   │           │
│   │   arrives   │          │  activated  │        │   created   │           │
│   └─────────────┘          └─────────────┘        └──────┬──────┘           │
│                                                          │                   │
│                                                          ▼                   │
│   AUTOMATION                                      ┌─────────────┐           │
│                                                   │    Tasks    │           │
│   ┌─────────────┐                                 │  assigned   │           │
│   │     Hub     │◀────────────────────────────────┤  to agents  │           │
│   │ Application │                                 └─────────────┘           │
│   │  executes   │                                                            │
│   └──────┬──────┘                                                            │
│          │                                                                   │
│          ▼                                                                   │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  Agent executes Actions → Automations call Tools → Work completes    │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Three-Specification Model

Hub separates Scenario definitions into three specifications that align with ontology layers and persona responsibilities:

| Specification | Ontology Layer | Owner | Focus |
|---------------|----------------|-------|-------|
| **Normative Spec** | Normative | Process Architect | What ought to be done |
| **Automation Spec** | Automation | Developer | How it's codified |
| **Deployment Spec** | Execution | Supervisor | How it's deployed |

### Development Journey

```
Phase 1: DESIGN (Process Architect)
    │
    │   ScenarioNormativeSpec
    │   • Roles, Goals, SOPs
    │   • Decision Criteria, Compliance
    │
    ▼
Phase 2: BUILD (Developer)
    │
    │   ScenarioAutomationSpec
    │   • Hub Application binding
    │   • Triggers, Tools, Notifications
    │
    ▼
Phase 3: DEPLOY (Supervisor)

    ScenarioDeploymentSpec
    • Task Queues, Agent Pools
    • SLA Parameters, Activation
```

→ **Details:** [Scenario Specification Types](./implementation-concepts/scenario-specification-types.md)

---

## Related Documentation

| Document | Purpose |
|----------|---------|
| [Ontology Reference](../01-concepts/ontology-reference.md) | Theoretical foundation for layers |
| [Signal Flow](./signal-flow.md) | How signals traverse the system |
| [Scenario Specification Types](./implementation-concepts/scenario-specification-types.md) | Three-spec model details |
| [Hub Application](./implementation-concepts/hub-application.md) | Automation artifact details |

