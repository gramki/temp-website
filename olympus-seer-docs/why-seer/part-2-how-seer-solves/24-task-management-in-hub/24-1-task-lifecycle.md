# 24.1 Task Lifecycle

Task Management handles the lifecycle of tasks—units of work delegated to agents (human and AI) within a workbench. Tasks move through states from creation to completion, with transitions triggered by agent actions, allocation algorithms, and system events. Task lifecycle management ensures that work is tracked comprehensively, SLAs are monitored, and outcomes are captured for audit and downstream processing.

Task lifecycle is a foundational capability that enables Hub Applications to orchestrate work by delegating tasks to agents, tracking progress, and capturing outcomes. Task lifecycle management integrates with Signal Exchange for observability, Notification Services for agent notifications, and Hub Applications for outcome processing.

## Purpose of this Subsection

This subsection describes how Hub manages task lifecycle. It explains task creation, task states and transitions, SLA tracking, outcome capture, and how tasks integrate with Hub Requests and Signal Exchange.

## Core Concepts & Definitions

### Task

A **Task** is a unit of work to be completed by one or more agents within a Request context. Tasks:
*   **Belong to Request**: Every task is scoped to a Request
*   **Are Typed**: Task type is defined in Scenario; each type has a creation template
*   **Are Queue-Attributed**: Always attributed to exactly one Task Queue
*   **Support Multi-Assignee**: Can have multiple assignees across escalation levels
*   **Follow First-to-Complete Wins**: Any assignee can mark complete

Tasks are the primary mechanism for delegating work to agents within Hub.

### Task States

**Task states** represent the current status of a task in its lifecycle:

| State | Description |
|-------|-------------|
| **PENDING** | Task created, awaiting allocation to agent(s) |
| **ASSIGNED** | Agent(s) allocated, work not yet started |
| **IN_PROGRESS** | Agent actively working on the task |
| **ON_HOLD** | Paused, waiting for external input or action |
| **COMPLETED** | Successfully finished by an assignee |
| **ABANDONED** | Agent opted out without reassigning; returns to PENDING for reallocation |
| **CANCELLED** | Terminated without completion (by request cancellation or explicit action) |

Task states enable tracking of task progress and status.

### Task Creation

**Task creation** is the process by which Hub Applications create tasks via Signal Exchange:

```
Hub Application                    Signal Exchange               Task Management
      │                                  │                              │
      │ ─── CREATE_TASK ───────────────> │                              │
      │                                  │ ──── Observe Task ─────────> │
      │                                  │                              │
      │                                  │ <─── Assign to Agent ─────── │
      │                                  │                              │
      │ <── TASK_STATUS_CHANGED ──────── │                              │
```

Tasks are created with a task type, queue assignment, payload, and SLA configuration.

### Task Outcome

**Task outcome** is the result captured when a task reaches COMPLETED state:

| Outcome | Description |
|---------|-------------|
| **success** | Task completed successfully as intended |
| **rejected** | Task rejected by agent (e.g., not applicable, duplicate) |
| **partial** | Partially completed; may require follow-up |
| **deferred** | Deferred to later; creates new task or reminder |
| **escalated_out** | Moved outside Hub (e.g., to external system) |

Task outcomes enable downstream processing and audit.

## Conceptual Models / Frameworks

### The Task Lifecycle Model

Tasks move through states:

```
                              ┌─────────────┐
                              │   PENDING   │
                              │             │
                              │ Awaiting    │
                              │ allocation  │
                              └──────┬──────┘
                                     │
                         ┌───────────┴───────────┐
                         │                       │
                         ▼                       ▼
                  ┌─────────────┐         ┌─────────────┐
                  │  ASSIGNED   │         │  CANCELLED  │
                  │             │         │             │
                  │ Agent(s)    │         │ Terminated  │
                  │ allocated   │         │ before      │
                  │             │         │ completion  │
                  └──────┬──────┘         └─────────────┘
                         │                       ▲
                         ▼                       │
                  ┌─────────────┐                │
                  │ IN_PROGRESS │────────────────┤
                  │             │                │
                  │ Agent       │                │
                  │ working     │                │
                  └──────┬──────┘                │
                         │                       │
           ┌─────────────┼─────────────┐         │
           │             │             │         │
           ▼             ▼             ▼         │
    ┌─────────────┐ ┌─────────┐ ┌───────────┐    │
    │  COMPLETED  │ │ ON_HOLD │ │ ABANDONED │────┘
    │             │ │         │ └───────────┘
    │ Successfully│ │ Waiting │       │
    │ finished    │ │ for     │       ▼
    └─────────────┘ │ external│ ┌───────────┐
                    │ input   │ │  PENDING  │
                    └────┬────┘ │ (re-queue)│
                         │      └───────────┘
                         ▼
                  ┌─────────────┐
                  │ IN_PROGRESS │
                  └─────────────┘
```

This model ensures that tasks are tracked comprehensively throughout their lifecycle.

### The Task Creation Template Model

Each task type in a Scenario has a **Task Creation Template** that defines:

```json
{
  "task_type_id": "verify-kyc-documents",
  "scenario_id": "dispute-resolution",
  
  "display": {
    "name": "Verify KYC Documents",
    "description": "Verify customer identity documents",
    "icon": "document-check"
  },
  
  "creation_schema": {
    "required_fields": ["customer_id", "document_types"],
    "optional_fields": ["instructions", "priority_override"]
  },
  
  "defaults": {
    "queue_id": "doc-verification-queue",
    "sla": {
      "response_minutes": 60,
      "resolution_minutes": 240
    }
  },
  
  "permissions": {
    "can_create": ["hub_application", "supervisor", "agent"],
    "can_abandon": true,
    "can_reassign": ["same_level", "higher_level"]
  }
}
```

Task Creation Templates ensure consistent task creation and configuration.

## Systemic and Enterprise Considerations

### Task Creation Sources

Tasks can be created by:
*   **Hub Applications**: Applications create tasks via Signal Exchange as part of request processing
*   **Agents**: Agents can create tasks for delegation or escalation
*   **Supervisors**: Supervisors can create tasks for manual assignment
*   **External Systems**: External systems can create tasks via REST API

Task creation sources enable flexible work orchestration.

### SLA Tracking

Task Management tracks Service Level Agreements (SLAs) for tasks:

| Metric | Description |
|--------|-------------|
| **Response SLA** | Time from PENDING to IN_PROGRESS |
| **Resolution SLA** | Time from PENDING to COMPLETED |
| **Touch Time** | Actual time spent in IN_PROGRESS (excluding ON_HOLD) |

SLA tracking enables monitoring of task performance and agent productivity.

### SLA Events

Task Management generates SLA events:

| Event | Description |
|-------|-------------|
| **SLA_WARNING** | Approaching SLA breach (configurable threshold) |
| **SLA_BREACHED** | SLA time exceeded |

SLA events enable proactive intervention and escalation.

### Request Cancellation Cascade

When a Request is cancelled:
*   **All tasks** are automatically cancelled (regardless of current state)
*   **All assignees** are notified
*   Tasks in **IN_PROGRESS** state are cancelled; any completion submitted after cancellation is **ignored**
*   No provision for agents to save work before cancellation

Request cancellation cascade ensures that cancelled requests don't leave orphaned tasks.

### Escalation During Lifecycle

Escalation is **orthogonal to state**—it adds assignees without changing the task state:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TASK STATE: IN_PROGRESS                         │
│                                                                              │
│  Escalation Level 0                     Escalation Level 1                   │
│  ┌─────────────────────────┐            ┌─────────────────────────┐          │
│  │ Assignee: agent-alice   │  ────────> │ Assignee: agent-bob     │          │
│  │ Assigned: 10:00:00      │  Threshold │ Assigned: 12:00:00      │          │
│  │ Status: Working         │  Exceeded  │ Status: Monitoring      │          │
│  └─────────────────────────┘            └─────────────────────────┘          │
│                                                                              │
│  Both agents remain assignees. Either can complete the task.                 │
│  Higher-level agent may nudge lower-level agent.                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

Escalation enables multi-level assignment without disrupting task state.

## Common Misconceptions & Failure Modes

### Misconception: Tasks Are Agent Inboxes

Some organizations assume that tasks are agent inboxes. However, tasks are units of work that can be assigned to multiple agents across escalation levels, and agents can work on tasks from multiple queues.

**Failure mode**: Organizations design task queues as agent inboxes, limiting flexibility and scalability.

### Misconception: Task State and Escalation Are Coupled

Some organizations assume that task state changes when escalation occurs. However, escalation is orthogonal to state—it adds assignees without changing state.

**Failure mode**: Organizations design systems where escalation changes task state, causing confusion and breaking workflows.

### Misconception: Abandoned Tasks Are Lost

Some organizations assume that abandoned tasks are lost. However, abandoned tasks return to PENDING for reallocation, and the abandon action is recorded for audit.

**Failure mode**: Organizations avoid task abandonment, forcing agents to complete tasks they cannot handle, reducing productivity and quality.

## Practical Implications

### Task Design

Organizations should design tasks that:
*   **Are Atomic**: Each task represents a single, complete unit of work
*   **Have Clear Outcomes**: Task outcomes are well-defined and measurable
*   **Support Escalation**: Tasks support multi-level assignment for complex work
*   **Include Context**: Tasks include sufficient context for agent decision-making

Task design directly impacts agent productivity and work quality.

### SLA Configuration

Organizations should configure SLAs that:
*   **Match Work Complexity**: SLAs reflect the complexity and urgency of work
*   **Enable Proactive Intervention**: SLA warnings enable proactive intervention before breach
*   **Support Escalation**: SLA thresholds align with escalation thresholds
*   **Account for Hold Time**: SLA configuration accounts for ON_HOLD time appropriately

SLA configuration directly impacts agent productivity and customer satisfaction.

## Cross-References

*   **Section 24.2 (Task Allocation)**: Describes how tasks are allocated to agents
*   **Section 24.3 (Agent Task Operations)**: Describes how agents work on tasks
*   **Section 12.4 (Deep Observability)**: Describes how Signal Exchange provides task observability

---

**References:**

*   `olympus-hub-docs/04-subsystems/task-management/README.md` — Task Management design
*   `olympus-hub-docs/04-subsystems/task-management/task-lifecycle.md` — Task lifecycle design
