# Task Lifecycle

> **Status:** 🟡 Draft — Core states and transitions defined

Task Lifecycle defines the **states, transitions, and entity structure** of tasks as they move from creation to completion.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Define task entity structure, states, and valid transitions |
| **States** | Pending, Assigned, In Progress, Completed, Cancelled |
| **Scope** | Always within a Request context |

---

## Task Entity Structure

```json
{
  "task_id": "task-12345",
  "request_id": "req-67890",
  "tenant_id": "acme-bank",
  "subscription_id": "sub-prod-001",
  "workbench_id": "dispute-ops",
  
  "task_type": {
    "type_id": "verify-kyc-documents",
    "scenario_id": "dispute-resolution",
    "scenario_version": "2.1.0"
  },
  
  "queue": {
    "queue_id": "doc-verification-queue",
    "current_escalation_level": 1
  },
  
  "assignees": [
    {
      "user_id": "agent-alice",
      "escalation_level": 0,
      "assigned_at": "2026-01-05T10:00:00Z",
      "assigned_by": "allocation-engine"
    },
    {
      "user_id": "agent-bob",
      "escalation_level": 1,
      "assigned_at": "2026-01-05T12:00:00Z",
      "assigned_by": "escalation-manager"
    }
  ],
  
  "state": {
    "current": "IN_PROGRESS",
    "previous": "ASSIGNED",
    "changed_at": "2026-01-05T10:15:00Z",
    "changed_by": "agent-alice"
  },
  
  "sla": {
    "response_due_at": "2026-01-05T11:00:00Z",
    "resolution_due_at": "2026-01-05T14:00:00Z",
    "response_met": true,
    "resolution_met": null
  },
  
  "priority": {
    "level": "normal",
    "override_reason": null
  },
  
  "payload": {
    "content_type": "application/json",
    "semantic_type": "com.acme.dispute.VerifyKYCTask",
    "data": {
      "customer_id": "cust-11111",
      "document_types": ["passport", "utility_bill"],
      "instructions": "Verify identity documents match customer record"
    }
  },
  
  "outcome": null,
  
  "metadata": {
    "created_at": "2026-01-05T09:55:00Z",
    "created_by": "app-dispute-handler",
    "source": "hub_application"
  }
}
```

---

## Task States

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
    │ finished    │ │ for     │       │
    │             │ │ external│       ▼
    └─────────────┘ │ input   │ ┌───────────┐
                    └────┬────┘ │  PENDING  │
                         │      │ (re-queue)│
                         ▼      └───────────┘
                  ┌─────────────┐
                  │ IN_PROGRESS │
                  └─────────────┘
```

---

## State Definitions

| State | Description |
|-------|-------------|
| **PENDING** | Task created, awaiting allocation to agent(s) |
| **ASSIGNED** | Agent(s) allocated, work not yet started |
| **IN_PROGRESS** | Agent actively working on the task |
| **ON_HOLD** | Paused, waiting for external input or action |
| **COMPLETED** | Successfully finished by an assignee |
| **ABANDONED** | Agent opted out without reassigning; returns to PENDING for reallocation |
| **CANCELLED** | Terminated without completion (by request cancellation or explicit action) |

---

## State Transitions

| From | To | Trigger | Actor |
|------|-----|---------|-------|
| — | PENDING | Task created | Hub Application, Agent, External System |
| PENDING | ASSIGNED | Allocation algorithm assigns agent(s) | Allocation Engine |
| PENDING | CANCELLED | Request cancelled or explicit cancellation | System, Supervisor |
| ASSIGNED | IN_PROGRESS | Agent starts work | Agent |
| ASSIGNED | ABANDONED | Agent opts out without starting | Agent |
| ASSIGNED | CANCELLED | Request cancelled | System, Supervisor |
| IN_PROGRESS | COMPLETED | Agent marks complete | Any Assignee |
| IN_PROGRESS | ON_HOLD | Agent pauses for external input | Agent |
| IN_PROGRESS | ABANDONED | Agent opts out (if permitted) | Agent |
| IN_PROGRESS | CANCELLED | Request cancelled | System, Supervisor |
| ON_HOLD | IN_PROGRESS | Agent resumes after input received | Agent |
| ON_HOLD | CANCELLED | Request cancelled | System, Supervisor |
| ABANDONED | PENDING | System re-queues for allocation | Task Management |

### Request Cancellation Cascade

When a Request is cancelled:
- **All tasks** are automatically cancelled (regardless of current state)
- **All assignees** are notified
- Tasks in **IN_PROGRESS** state are cancelled; any completion submitted after cancellation is **ignored**
- No provision for agents to save work before cancellation

---

## Escalation During Lifecycle

Escalation is **orthogonal to state**—it adds assignees without changing the task state.

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

---

## Task Outcome

When a task reaches COMPLETED state, it includes an outcome:

```json
{
  "outcome": {
    "result": "success",
    "completed_by": "agent-alice",
    "completed_at": "2026-01-05T13:30:00Z",
    "result_payload": {
      "content_type": "application/json",
      "semantic_type": "com.acme.dispute.VerifyKYCResult",
      "data": {
        "verification_status": "approved",
        "notes": "All documents verified successfully",
        "verified_documents": ["passport", "utility_bill"]
      }
    }
  }
}
```

### Outcome Types

| Outcome | Description |
|---------|-------------|
| **success** | Task completed successfully as intended |
| **rejected** | Task rejected by agent (e.g., not applicable, duplicate) |
| **partial** | Partially completed; may require follow-up |
| **deferred** | Deferred to later; creates new task or reminder |
| **escalated_out** | Moved outside Hub (e.g., to external system) |

---

## Abandon Behavior

When an agent abandons a task:

1. **Permission Check:** Scenario configuration must permit abandonment
2. **State Change:** Task moves to ABANDONED, then immediately to PENDING
3. **History Recording:** Abandon action recorded as request-scoped memo
4. **Reallocation:** Allocation algorithm runs again at the same escalation level
5. **Exclusion (Optional):** Allocation may exclude recently-abandoned agents (algorithm-specific)

```json
{
  "abandon_record": {
    "task_id": "task-12345",
    "abandoned_by": "agent-alice",
    "abandoned_at": "2026-01-05T11:00:00Z",
    "escalation_level_at_abandon": 0,
    "reason": "Conflict of interest",
    "recorded_as_memo": true
  }
}
```

---

## Task Creation Template

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
    "required_fields": [
      "customer_id",
      "document_types"
    ],
    "optional_fields": [
      "instructions",
      "priority_override"
    ],
    "field_definitions": {
      "customer_id": {
        "type": "string",
        "label": "Customer ID",
        "validation": "required"
      },
      "document_types": {
        "type": "array",
        "items": "string",
        "label": "Document Types to Verify",
        "options": ["passport", "drivers_license", "utility_bill", "bank_statement"]
      },
      "instructions": {
        "type": "string",
        "label": "Additional Instructions"
      }
    }
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
  },
  
  "solver_template_id": "kyc-verification-solver"
}
```

---

## SLA Tracking

| Metric | Description |
|--------|-------------|
| **Response SLA** | Time from PENDING to IN_PROGRESS |
| **Resolution SLA** | Time from PENDING to COMPLETED |
| **Touch Time** | Actual time spent in IN_PROGRESS (excluding ON_HOLD) |

### SLA Events

| Event | Description |
|-------|-------------|
| **SLA_WARNING** | Approaching SLA breach (configurable threshold) |
| **SLA_BREACHED** | SLA time exceeded |

**Note:** SLA tracking is separate from escalation. Configure escalation thresholds to trigger before SLA breach.

### SLA and Escalation Clock Behavior During ON_HOLD

| Configuration | Behavior |
|---------------|----------|
| `pause_on_hold: true` | SLA clock AND escalation timers pause while task is ON_HOLD |
| `pause_on_hold: false` | SLA clock and escalation timers continue (default) |

This is configured at the Scenario or Queue level. SLA and escalation timers pause together.

---

## Task History

All task state changes are recorded:

```json
{
  "task_id": "task-12345",
  "history": [
    {
      "timestamp": "2026-01-05T09:55:00Z",
      "event": "CREATED",
      "actor": "app-dispute-handler",
      "details": { "source": "hub_application" }
    },
    {
      "timestamp": "2026-01-05T10:00:00Z",
      "event": "ASSIGNED",
      "actor": "allocation-engine",
      "details": { "assignee": "agent-alice", "level": 0 }
    },
    {
      "timestamp": "2026-01-05T10:15:00Z",
      "event": "STATE_CHANGED",
      "actor": "agent-alice",
      "details": { "from": "ASSIGNED", "to": "IN_PROGRESS" }
    },
    {
      "timestamp": "2026-01-05T12:00:00Z",
      "event": "ESCALATED",
      "actor": "escalation-manager",
      "details": { "to_level": 1, "assignee": "agent-bob" }
    },
    {
      "timestamp": "2026-01-05T13:30:00Z",
      "event": "STATE_CHANGED",
      "actor": "agent-alice",
      "details": { "from": "IN_PROGRESS", "to": "COMPLETED" }
    }
  ]
}
```

---

## Related Documentation

- [Task Management Overview](./README.md)
- [Task Queues](./task-queues.md)
- [Task Allocation](./task-allocation.md)
- [Agent Desk - Task Solver](../../06-ux-architecture/tenant-domain/agent-desk.md#task-solver-interface)

---
