# Task Management

> **Status:** 🟡 Draft — Core concepts defined, component details in progress

Task Management handles the **creation, assignment, tracking, and lifecycle of tasks**—the units of work delegated to agents (human and AI) within a Workbench.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Manage task queues, allocation, escalation, and lifecycle |
| **Scope** | Workbench-level task orchestration |
| **Consumers** | Hub Applications, Human Agents, AI Agents, Supervisors |
| **Integration** | Signal Exchange, Cipher IAM, Workbench Management, Notification Services |

---

## Core Premise

Hub Applications orchestrate work by delegating tasks to agents in their Workbench. The flow is:

```
Hub Application                    Signal Exchange               Task Management
      │                                  │                              │
      │ ─── CREATE_TASK ───────────────> │                              │
      │                                  │ ──── Observe Task ─────────> │
      │                                  │                              │
      │                                  │ <─── Assign to Agent ─────── │
      │                                  │                              │
      │ <── TASK_STATUS_CHANGED ──────── │                              │
      │                                  │                              │
```

From this perspective:
- **Hub Application** is an orchestrator of updates from agents regarding their tasks
- **Signal Exchange** routes task-related messages and notifies applications of status changes
- **Task Management** observes tasks and handles allocation, escalation, and SLA tracking

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Task Lifecycle](./task-lifecycle.md) | Task entity, states, and transitions | 🟡 Draft |
| [Task Queues](./task-queues.md) | Queue definitions, escalation matrix, special queues | 🟡 Draft |
| [Task Allocation](./task-allocation.md) | Allocation algorithms and workload balancing | 🟡 Draft |
| [Agent Task Operations](./agent-task-operations.md) | How agents work on and complete tasks | 🟡 Draft |

---

## Core Concepts

### Task

A **Task** is a unit of work to be completed by one or more agents within a Request context.

| Attribute | Description |
|-----------|-------------|
| **Belongs to Request** | Every task is scoped to a Request |
| **Typed** | Task type is defined in Scenario; each type has a creation template |
| **Queue-Attributed** | Always attributed to exactly one Task Queue |
| **Multi-Assignee** | Can have multiple assignees across escalation levels |
| **First-to-Complete Wins** | Any assignee can mark complete |

### Task Queue

A **Task Queue** is a conceptual grouping of outstanding tasks, not an agent's inbox.

| Attribute | Description |
|-----------|-------------|
| **Workbench-Scoped** | Each queue belongs to a Workbench |
| **Candidate Agents** | Defined by role, group, or explicit list |
| **Escalation Matrix** | Multi-level assignment structure |
| **Allocation Algorithm** | Determines how tasks are assigned to agents |

### Escalation Matrix

The **Escalation Matrix** defines multiple levels of agent assignment within a Task Queue.

| Attribute | Description |
|-----------|-------------|
| **Levels** | 0 to N, where 0 is the default starting level |
| **Threshold Time** | Duration after which task escalates to next level |
| **Level Candidates** | Agents eligible at each level (by role, group, etc.) |
| **Cumulative Assignment** | All levels become assignees; does not replace lower levels |

### Allocation vs Assignment

| Term | Description |
|------|-------------|
| **Allocation** | The process executed by the allocation algorithm to match tasks to agents |
| **Assignment** | The result of allocation—an agent is now assigned to the task |

### Actors and Assignees

| Role | Description |
|------|-------------|
| **Assignee** | Agent currently assigned to a task (can be multiple across escalation levels) |
| **Actor** | Any agent who has ever been associated with the Request through any task at any escalation level |

---

## Task Creation Sources

Tasks can be created by:

| Source | Description |
|--------|-------------|
| **Hub Applications** | Primary source—applications delegate work to agents |
| **Supervisors** | Can create tasks through any available channel |
| **Agents** | Can create tasks if permitted in the Scenario |
| **External Systems** | Authorized enterprise systems can create tasks via signals |

**Constraint:** All tasks must be of a type supported in the Scenario. Each task type has a **Task Creation Template** that defines required information for creation and completion.

### Scenario Task Controls

Scenarios can configure:
- **Task Source Restriction:** Disallow tasks from any source other than the Hub Application
- **Concurrency Control:** Prevent concurrent pending/incomplete tasks within a request

Task sequencing and dependencies are managed by Hub Applications, not Task Management.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           TASK MANAGEMENT                                    │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                         TASK OBSERVER                                  │  │
│  │      (Registered as Observer with Signal Exchange for Task events)     │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                    │                                         │
│         ┌──────────────────────────┼──────────────────────────┐             │
│         ▼                          ▼                          ▼             │
│  ┌─────────────┐          ┌─────────────────┐         ┌─────────────────┐  │
│  │    TASK     │          │   ESCALATION    │         │   ALLOCATION    │  │
│  │  REGISTRY   │          │    MANAGER      │         │     ENGINE      │  │
│  │             │          │                 │         │                 │  │
│  │ • Task CRUD │          │ • Time-based    │         │ • Algorithm     │  │
│  │ • State     │          │   escalation    │         │   execution     │  │
│  │   machine   │          │ • Level mgmt    │         │ • Workload      │  │
│  │ • History   │          │ • SLA tracking  │         │   balancing     │  │
│  └─────────────┘          └─────────────────┘         └─────────────────┘  │
│         │                          │                          │             │
│         └──────────────────────────┴──────────────────────────┘             │
│                                    │                                         │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                      TASK QUEUE MANAGER                                │  │
│  │                                                                        │  │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐       │  │
│  │  │  Default   │  │  Subject   │  │ Originator │  │ Supervisor │       │  │
│  │  │   Queue    │  │   Queue    │  │   Queue    │  │   Queue    │       │  │
│  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘       │  │
│  │                                                                        │  │
│  │               ┌────────────────────────────────┐                      │  │
│  │               │     Custom Scenario Queues      │                      │  │
│  │               └────────────────────────────────┘                      │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                      INTEGRATION LAYER                                 │  │
│  │                                                                        │  │
│  │  • Signal Exchange (task events, status updates)                       │  │
│  │  • Cipher IAM (role/group resolution)                                  │  │
│  │  • Notification Services (agent notifications)                         │  │
│  │  • Workbench Management (queue configuration)                          │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Task Flow

### 1. Task Creation

```
Hub Application / Agent / External System
         │
         │  CREATE_TASK (with task_type, task_queue_id, payload)
         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SIGNAL EXCHANGE                                    │
│                                                                              │
│  • Validates task type against Scenario                                      │
│  • Associates task with Request                                              │
│  • Publishes TASK_CREATED event                                              │
└─────────────────────────────────────────────────────────────────────────────┘
         │
         │  TASK_CREATED event
         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           TASK MANAGEMENT                                    │
│                                                                              │
│  1. Task Registry creates task record                                        │
│  2. Queue Manager attributes task to queue                                   │
│     • Explicit queue from request, OR                                        │
│     • Scenario default queue, OR                                             │
│     • Workbench default queue                                                │
│  3. Allocation Engine runs allocation algorithm                              │
│  4. Agent(s) assigned at Escalation Level 0                                  │
└─────────────────────────────────────────────────────────────────────────────┘
         │
         │  TASK_ASSIGNED event
         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SIGNAL EXCHANGE                                    │
│                                                                              │
│  • Notifies Hub Application of assignment                                    │
│  • Notification Services alerts assigned agent(s)                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2. Task Escalation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ESCALATION MANAGER                                     │
│                                                                              │
│  For each pending task:                                                      │
│                                                                              │
│  1. Check time since last escalation (or creation for level 0)               │
│  2. If threshold exceeded for current level:                                 │
│     a. Resolve candidate agents for next level                               │
│     b. Run allocation algorithm for next level                               │
│     c. Add new assignees (cumulative—lower levels remain)                    │
│     d. Publish TASK_ESCALATED event                                          │
│  3. Continue monitoring until task completed or cancelled                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3. Task Completion

```
Agent (via Task Solver, MCP, or other channel)
         │
         │  COMPLETE_TASK (outcome, result_payload)
         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           TASK MANAGEMENT                                    │
│                                                                              │
│  1. Validate agent is an assignee                                            │
│  2. Update task state to COMPLETED                                           │
│  3. Record outcome and result                                                │
│  4. Cancel any pending escalation timers                                     │
│  5. Publish TASK_COMPLETED event                                             │
└─────────────────────────────────────────────────────────────────────────────┘
         │
         │  TASK_COMPLETED event
         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SIGNAL EXCHANGE                                    │
│                                                                              │
│  • Notifies Hub Application                                                  │
│  • Updates Request state if applicable                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Request and Task Relationship

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              REQUEST                                         │
│                                                                              │
│  request_id: req-12345                                                       │
│  scenario: dispute-resolution                                                │
│  subject: customer-67890                                                     │
│  originator: channel-web                                                     │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │                              TASKS                                       ││
│  │                                                                          ││
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐          ││
│  │  │ Task: Verify    │  │ Task: Review    │  │ Task: Approve   │          ││
│  │  │ Documents       │  │ Evidence        │  │ Resolution      │          ││
│  │  │                 │  │                 │  │                 │          ││
│  │  │ Queue: doc-     │  │ Queue: review-  │  │ Queue: super-   │          ││
│  │  │ verification    │  │ queue           │  │ visor-queue     │          ││
│  │  │                 │  │                 │  │                 │          ││
│  │  │ Assignees:      │  │ Assignees:      │  │ Assignees:      │          ││
│  │  │ • agent-a (L0)  │  │ • agent-b (L0)  │  │ (pending)       │          ││
│  │  │ • agent-c (L1)  │  │                 │  │                 │          ││
│  │  │                 │  │                 │  │                 │          ││
│  │  │ Status:         │  │ Status:         │  │ Status:         │          ││
│  │  │ IN_PROGRESS     │  │ COMPLETED       │  │ PENDING         │          ││
│  │  └─────────────────┘  └─────────────────┘  └─────────────────┘          ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  ACTORS (cumulative across all tasks):                                       │
│  • agent-a, agent-b, agent-c                                                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Integration Points

| System | Integration |
|--------|-------------|
| **Signal Exchange** | Registered as Observer; receives REQUEST_UPDATE events containing task operations; publishes TASK_* events back to SX |
| **Cipher IAM** | Resolves roles, groups, and user identities for allocation |
| **Workbench Management** | Queue configuration, Scenario definitions |
| **Notification Services** | Agent notifications for task assignment/escalation |
| **Request Management** | Request context for task creation and resolution |

### Observer Registration

Task Management registers with Signal Exchange as an observer, similar to Notification Services:

```json
{
  "observer_id": "task-management",
  "subscription": {
    "scope": "tenant",
    "event_types": ["REQUEST_UPDATE"],
    "filter": {
      "update_types": ["CREATE_TASK", "COMPLETE_TASK", "ABANDON_TASK", "REASSIGN_TASK", "HOLD_TASK", "RESUME_TASK"]
    }
  }
}
```

Task Management publishes events back to Signal Exchange, which routes them to Hub Applications and other observers.

### Task Creation via REQUEST_UPDATE

`CREATE_TASK` is a `REQUEST_UPDATE` message type. Tasks can be created by:
- **Hub Applications** — Primary source via REQUEST_UPDATE
- **External Systems** — Via signals that result in REQUEST_UPDATE
- **Agents/Supervisors** — Via channels that emit REQUEST_UPDATE

**Validation:** Task payload must conform to the task type schema defined in the Scenario. No additional validation is performed by Task Management.

---

## SLA vs Escalation

| Concept | Description |
|---------|-------------|
| **SLA** | Contracted time to complete the task; defines compliance requirements |
| **Escalation** | Mechanism to bring in additional help; should trigger before SLA breach |

Best practice: Configure escalation thresholds to allow newly assigned agents sufficient time to act before SLA breach.

---

## Related Documentation

- [Signal Exchange](../signal-exchange/README.md) — Task event routing
- [Request Management](../request-management/README.md) — Request lifecycle
- [Workbench Management](../workbench-management/README.md) — Queue configuration
- [Agent Desk](../../06-ux-architecture/tenant-domain/agent-desk.md) — Task Solver UI
- [Cipher IAM](../supporting-systems/cipher-iam.md) — Identity and access

---
