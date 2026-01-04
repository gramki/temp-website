# Task Management

> **Status:** 🔴 Stub — Placeholder for expansion

Task Management handles the **assignment, routing, and lifecycle of tasks**—the units of work assigned to agents (human and AI) within operations.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Manage task queues, assignment, and lifecycle |
| **Consumers** | Human Agents, AI Agents, Automation Runtimes |
| **Integration** | Cipher IAM, Seer, Rhea, ChronoShift |

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Task Queues](./task-queues.md) | Task queue definitions and routing | 🔴 Stub |
| [Task Lifecycle](./task-lifecycle.md) | Task states and transitions | 🔴 Stub |
| [Task Assignment](./task-assignment.md) | Assignment to human and AI agents | 🔴 Stub |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   TASK MANAGEMENT                                │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 TASK CREATION                            │    │
│  │       (From Automation Runtimes, Operations)              │    │
│  └─────────────────────────┬───────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │                 TASK ROUTING                             │    │
│  │                                                          │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │    │
│  │  │    Queue     │  │    Direct    │  │    Group     │   │    │
│  │  │  Assignment  │  │  Assignment  │  │  Assignment  │   │    │
│  │  └──────────────┘  └──────────────┘  └──────────────┘   │    │
│  └──────────────────────────────────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │                 AGENT INTERFACES                         │    │
│  │                                                          │    │
│  │  ┌──────────────┐  ┌──────────────┐                     │    │
│  │  │    Human     │  │      AI      │                     │    │
│  │  │   Agents     │  │   Agents     │                     │    │
│  │  │  (via UI)    │  │  (via Seer)  │                     │    │
│  │  └──────────────┘  └──────────────┘                     │    │
│  └──────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Task Types by Agent

From Hub Architecture:

| Agent Type | Assignment Method | Description |
|------------|-------------------|-------------|
| **Human Agent** | Task Queue | Assigned to a queue managed by a Task Assignment System |
| **Human Agent** | Direct User | Assigned to a specific user |
| **Human Agent** | User Group | Assigned to a group where any member can complete |
| **AI Agent** | Delegation | Hub provides specification for delegating to AI agents |

---

## AI Agent Task Considerations

From Hub Architecture:
- Hub must have a clear specification for **delegation of tasks** to AI agents
- For Case Management, Hub needs clear specification for **announcing case progression** and events
- AI Agents may subscribe to only a **subset of case progression updates** relevant to their role

---

## Task Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Review** | Review and approve/reject | Document review, decision approval |
| **Action** | Perform an action | Call customer, send email |
| **Data Entry** | Enter or update data | Fill form, update record |
| **Investigation** | Research and analyze | Investigate issue, gather evidence |
| **Decision** | Make a choice | Select path, approve exception |

---

## External Task Systems

Hub can integrate with external task management systems:

| System | Integration |
|--------|-------------|
| **Jira** | Task creation, status sync |
| **ServiceNow** | Incident and request tasks |
| **Slack/Teams** | Task notifications |

---

## Seer Integration

| Integration Point | Description |
|-------------------|-------------|
| **Hub-to-Seer Connector** | Accept, complete, or assign tasks |
| **Case Progression Events** | Announce events to subscribed agents |
| **Task Delegation Spec** | Clear contract for AI task handling |

---

## Related Documentation

- [Hub Architecture - Task Management](../../02-system-design/hub-architecture.md#111-task-management)
- [Cipher IAM](../supporting-systems/cipher-iam.md) — Agent identity
- [Rhea Workflow](../automation-runtimes/rhea-workflow-engine.md) — Task creation from workflows

---

*TODO: Detailed design — queue configuration, routing rules, SLA management, escalation*

