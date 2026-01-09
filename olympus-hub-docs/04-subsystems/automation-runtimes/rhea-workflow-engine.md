# Rhea - BPMN Workflow Engine

> **Status:** 🔴 Stub — Placeholder for expansion

Rhea is the Automation Runtime for **deterministic Workflows**—multi-step operations modeled using BPMN that orchestrate activities across multiple roles.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Operation Types** | Deterministic Workflows |
| **Modeling Language** | BPMN 2.0 |
| **Execution Model** | Token-based workflow execution |
| **State Management** | Persistent workflow state |
| **Integration** | Seer (Employed Agents), Task Management, CAF |

---

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Approval Workflows** | Multi-level approval chains |
| **Onboarding Processes** | Customer/employee onboarding with multiple steps |
| **Compliance Workflows** | Regulatory review and sign-off processes |
| **Order Fulfillment** | End-to-end order processing |
| **Incident Response** | Structured incident handling procedures |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                          RHEA                                    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                  PROCESS REPOSITORY                      │    │
│  │          (BPMN Process Definitions)                      │    │
│  └─────────────────────────┬───────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │                 WORKFLOW ENGINE                          │    │
│  │                                                          │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐   │    │
│  │  │  Token   │  │  Task    │  │  Gateway             │   │    │
│  │  │  Manager │  │ Executor │  │  Evaluator           │   │    │
│  │  └──────────┘  └──────────┘  └──────────────────────┘   │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 SEER AGENT CONNECTOR                     │    │
│  │        (Employed Agent participation in Workflows)       │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Process Definition** | BPMN model defining the workflow structure |
| **Process Instance** | A running execution of a process definition |
| **Token** | Execution pointer tracking progress through the process |
| **Task** | A unit of work within the workflow |
| **Gateway** | Decision point (exclusive, parallel, inclusive) |
| **Event** | Start, intermediate, or end events |
| **Swimlane** | Role assignment for activities |

---

## BPMN Element Support

| Element Type | Supported Elements |
|--------------|-------------------|
| **Tasks** | User Task, Service Task, Script Task, Manual Task |
| **Gateways** | Exclusive, Parallel, Inclusive, Event-based |
| **Events** | Start, End, Timer, Message, Signal, Error |
| **Subprocesses** | Embedded, Call Activity |
| **Artifacts** | Data Objects, Annotations |

---

## Agent Integration

Rhea integrates with Seer for AI Agent participation in workflows:

| Integration Point | Description |
|-------------------|-------------|
| **Employed Agent as Participant** | Seer provides Employed Agents that can execute User Tasks |
| **Task Delegation** | Workflow tasks can be assigned to AI agents via Task Management |
| **Agent Decision Points** | AI agents can make decisions at gateways |
| **Human-AI Handoff** | Seamless handoff between human and AI participants |

---

## Workflow Lifecycle

```
[Deployed] → [Instantiated] → [Running] → [Completed]
                                  │
                                  ├─→ [Suspended] → [Resumed] → [Running]
                                  │
                                  ├─→ [Failed] → [Compensating] → [Compensated]
                                  │
                                  └─→ [Cancelled]
```

---

## Integration Points

| System | Integration |
|--------|-------------|
| **Seer** | Employed Agent provider for workflow tasks |
| **Task Management** | Task creation and assignment |
| **CAF** | Decision audit at gateway points |
| **Cipher** | Role-based participant assignment |

---

## Related Documentation

- [Automation Runtimes Overview](./README.md)
- [Seer Case Automation](./seer-case-automation.md)
- [Task Management](../task-management/README.md)

---

*TODO: Detailed design — BPMN modeling guidelines, process repository, versioning, compensation patterns*

