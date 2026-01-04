# Task Lifecycle

> **Status:** 🔴 Stub — Placeholder for expansion

Task Lifecycle defines the **states and transitions** that tasks move through from creation to completion.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Define task states and valid transitions |
| **States** | Created, Queued, Assigned, In Progress, Completed, etc. |
| **Integration** | Automation Runtimes, CAF (for decision tasks) |

---

## Task States

```
[Created] → [Queued] → [Assigned] → [In Progress] → [Completed]
                │          │             │
                │          │             ├─→ [On Hold]
                │          │             │
                │          └─────────────├─→ [Reassigned] → [Queued]
                │                        │
                └────────────────────────├─→ [Escalated]
                                         │
                                         └─→ [Cancelled]
```

---

## State Definitions

| State | Description |
|-------|-------------|
| **Created** | Task created, not yet queued |
| **Queued** | Waiting in queue for assignment |
| **Assigned** | Assigned to specific agent |
| **In Progress** | Agent actively working |
| **On Hold** | Paused, waiting for external input |
| **Completed** | Successfully finished |
| **Escalated** | Moved to higher tier/authority |
| **Reassigned** | Moved to different agent |
| **Cancelled** | Terminated without completion |

---

## State Transitions

| From | To | Trigger |
|------|-----|---------|
| Created | Queued | Routing complete |
| Queued | Assigned | Agent claims or assignment |
| Assigned | In Progress | Agent starts work |
| In Progress | Completed | Agent marks complete |
| In Progress | On Hold | Agent pauses |
| In Progress | Escalated | SLA breach or explicit escalation |
| On Hold | In Progress | Agent resumes |
| Assigned | Queued | Agent releases |
| * | Cancelled | Explicit cancellation |

---

## Task Outcome

When completed, tasks have an outcome:

| Outcome | Description |
|---------|-------------|
| **Success** | Task completed successfully |
| **Rejected** | Task rejected by agent |
| **Partial** | Partially completed |
| **Deferred** | Deferred to later |

---

## SLA Tracking

| Metric | Description |
|--------|-------------|
| **Response SLA** | Time from Created to In Progress |
| **Resolution SLA** | Time from Created to Completed |
| **Touch Time** | Actual work time |

---

## Related Documentation

- [Task Management Overview](./README.md)
- [Task Queues](./task-queues.md)
- [Task Assignment](./task-assignment.md)

---

*TODO: Detailed design — state machine implementation, SLA triggers, audit events*

