# Task Queues

> **Status:** 🟡 Draft — Queue structure and escalation matrix defined

Task Queues are **conceptual groupings of outstanding tasks** that organize work and define escalation paths for agent assignment.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Group tasks logically and define escalation paths |
| **Scope** | Workbench-level |
| **Key Feature** | Escalation Matrix with multi-level assignment |

**Note:** A Task Queue is not an agent's inbox. It is a logical container that groups tasks for allocation purposes.

---

## Task Queue Structure

```json
{
  "queue_id": "doc-verification-queue",
  "name": "Document Verification Queue",
  "description": "Tasks related to customer document verification",
  
  "scope": {
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001",
    "workbench_id": "dispute-ops"
  },
  
  "allocation": {
    "algorithm": "round-robin-with-capacity",
    "parameters": {
      "max_concurrent_tasks": 5,
      "consider_affinity": true
    }
  },
  
  "escalation_matrix": {
    "levels": [
      {
        "level": 0,
        "candidates": {
          "type": "iam_role",
          "value": "document-verifier"
        },
        "threshold_minutes": null
      },
      {
        "level": 1,
        "candidates": {
          "type": "iam_user_group",
          "value": "senior-verifiers"
        },
        "threshold_minutes": 60
      },
      {
        "level": 2,
        "candidates": {
          "type": "workbench_role",
          "value": "supervisor"
        },
        "threshold_minutes": 30
      }
    ]
  },
  
  "sla_defaults": {
    "response_minutes": 30,
    "resolution_minutes": 240
  },
  
  "settings": {
    "allow_manual_reassignment": true,
    "allow_abandon": true,
    "manual_add_remove_agents": true
  },
  
  "status": "active",
  
  "metadata": {
    "created_at": "2026-01-01T00:00:00Z",
    "created_by": "supervisor-jane",
    "version": 3
  }
}
```

---

## Candidate Agent Specification

Task Queue candidates at each escalation level can be specified using logical references:

### Reference Types

| Type | Description | Resolution |
|------|-------------|------------|
| **iam_role** | IAM Role from Cipher | Users with this role in tenant |
| **iam_user_group** | IAM User Group from Cipher | Members of the group |
| **workbench_role** | Role defined in Workbench | Named users for this role (e.g., Supervisor, Administrator) |
| **request_role** | Role relative to Request | Dynamically resolved per request per allocation |
| **explicit_users** | Explicit list of user IDs | Specific named users |

### IAM Role Reference

```json
{
  "type": "iam_role",
  "value": "document-verifier"
}
```

Resolves to: All users in the tenant with the `document-verifier` IAM role.

### IAM User Group Reference

```json
{
  "type": "iam_user_group",
  "value": "senior-verifiers"
}
```

Resolves to: All members of the `senior-verifiers` user group in Cipher.

### Workbench Role Reference

```json
{
  "type": "workbench_role",
  "value": "supervisor"
}
```

Resolves to: Users named for the Supervisor role in the Workbench configuration.

**Note:** Hub creates a User Group per each Workbench role for each Workbench automatically.

### Request Role Reference

```json
{
  "type": "request_role",
  "value": "subject"
}
```

| Value | Resolution |
|-------|------------|
| **subject** | The subject of the Request (e.g., customer being served) |
| **originator** | The entity that originated the Request |
| **all_assignees** | All agents currently assigned to any task in the Request |
| **all_actors** | All agents who have ever been associated with the Request |

**Dynamic Resolution:** Request roles are resolved at each allocation algorithm run, not at queue definition time.

### Explicit Users Reference

```json
{
  "type": "explicit_users",
  "value": ["user-alice", "user-bob", "user-charlie"]
}
```

Resolves to: The specific named users.

---

## Escalation Matrix

The Escalation Matrix defines multiple levels of agent assignment within a Task Queue.

### Structure

```json
{
  "escalation_matrix": {
    "levels": [
      {
        "level": 0,
        "candidates": { /* candidate specification */ },
        "threshold_minutes": null
      },
      {
        "level": 1,
        "candidates": { /* candidate specification */ },
        "threshold_minutes": 60
      },
      {
        "level": 2,
        "candidates": { /* candidate specification */ },
        "threshold_minutes": 30
      }
    ]
  }
}
```

### Escalation Behavior

```
                    Task Created
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      LEVEL 0 (Default)                                       │
│                                                                              │
│  Candidates: iam_role:document-verifier                                      │
│  Threshold: N/A (starting level)                                             │
│                                                                              │
│  Allocation Engine assigns: agent-alice                                      │
└─────────────────────────────────────────────────────────────────────────────┘
                         │
                         │ 60 minutes elapsed, task still pending
                         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      LEVEL 1                                                 │
│                                                                              │
│  Candidates: iam_user_group:senior-verifiers                                 │
│  Threshold: 60 minutes from Level 0 assignment                               │
│                                                                              │
│  Allocation Engine assigns: agent-bob                                        │
│  agent-alice REMAINS an assignee (cumulative)                                │
└─────────────────────────────────────────────────────────────────────────────┘
                         │
                         │ 30 minutes elapsed, task still pending
                         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      LEVEL 2                                                 │
│                                                                              │
│  Candidates: workbench_role:supervisor                                       │
│  Threshold: 30 minutes from Level 1 assignment                               │
│                                                                              │
│  Allocation Engine assigns: supervisor-jane                                  │
│  agent-alice and agent-bob REMAIN assignees (cumulative)                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Key Principles

1. **Cumulative Assignment:** Higher levels add assignees; lower levels are not removed
2. **Any Can Complete:** Any assignee at any level can mark the task complete
3. **First Wins:** The first assignee to complete the task wins
4. **Nudging:** Higher-level assignees may coordinate with or nudge lower-level assignees
5. **Threshold Timing:** Each level's threshold is measured from the previous level's assignment
6. **Escalation Scope:** Escalation applies to tasks not yet COMPLETED or CANCELLED (includes PENDING, ASSIGNED, IN_PROGRESS, ON_HOLD states)

---

## Default Queues

### Workbench Default Queue

Every Workbench has a **Default Queue** for tasks not explicitly assigned to a queue.

```json
{
  "queue_id": "default-queue",
  "name": "Default Queue",
  "scope": {
    "workbench_id": "dispute-ops"
  },
  "is_default": true
}
```

### Scenario Default Queue

A Scenario can specify a **Scenario Default Queue** that overrides the Workbench default.

```json
{
  "scenario_id": "dispute-resolution",
  "defaults": {
    "task_queue_id": "dispute-triage-queue"
  }
}
```

### Queue Resolution Order

1. **Explicit Queue:** Task creation specifies queue_id → use that queue
2. **Scenario Default:** Scenario defines default queue → use scenario default
3. **Workbench Default:** Fall back to workbench default queue

---

## Special Task Queues

Special queues use request-scoped or workbench-scoped roles for dynamic candidate resolution.

### Subject Task Queue

Tasks assigned to the subject (e.g., customer) of the Request.

```json
{
  "queue_id": "subject-queue",
  "name": "Subject Task Queue",
  "type": "special",
  
  "escalation_matrix": {
    "levels": [
      {
        "level": 0,
        "candidates": {
          "type": "request_role",
          "value": "subject"
        },
        "threshold_minutes": null
      },
      {
        "level": 1,
        "candidates": {
          "type": "scenario_defined",
          "reference": "subject_escalation_path"
        },
        "threshold_minutes": 1440
      }
    ]
  }
}
```

**Use Case:** Tasks that the customer must complete (e.g., upload documents, provide information).

### Request Originator Task Queue

Tasks assigned to the entity that originated the Request.

```json
{
  "queue_id": "originator-queue",
  "name": "Request Originator Task Queue",
  "type": "special",
  
  "escalation_matrix": {
    "levels": [
      {
        "level": 0,
        "candidates": {
          "type": "request_role",
          "value": "originator"
        },
        "threshold_minutes": null
      },
      {
        "level": 1,
        "candidates": {
          "type": "scenario_defined",
          "reference": "originator_escalation_path"
        },
        "threshold_minutes": 120
      }
    ]
  }
}
```

**Use Case:** Tasks requiring action from the channel or system that started the request.

**Note:** The originator is resolved at Level 0. Subsequent escalation levels are Scenario-specific.

### Supervisor Task Queue

Tasks assigned to Workbench supervisors.

```json
{
  "queue_id": "supervisor-queue",
  "name": "Supervisor Task Queue",
  "type": "special",
  
  "escalation_matrix": {
    "levels": [
      {
        "level": 0,
        "candidates": {
          "type": "workbench_role",
          "value": "supervisor"
        },
        "threshold_minutes": null
      },
      {
        "level": 1,
        "candidates": {
          "type": "workbench_role",
          "value": "administrator"
        },
        "threshold_minutes": 60
      }
    ]
  }
}
```

**Use Case:** Approval tasks, exception handling, override decisions.

---

## Manual Queue Management

### Supervisor Actions

| Action | Description |
|--------|-------------|
| **Add Agent** | Manually add a user to queue candidates at a specific level |
| **Remove Agent** | Manually remove a user from queue candidates |
| **Reassign Task** | Move a task to a different assignee within the queue |

### Manual Reassignment Rules

| Scenario Setting | Behavior |
|------------------|----------|
| `reassign: same_level` | Can reassign to agents at the same escalation level |
| `reassign: higher_level` | Can reassign to agents at the same or higher level |
| `reassign: any` | Can reassign to any eligible agent |
| `reassign: supervisor_only` | Only supervisors can reassign |

### Supervisor Override

Supervisors can reassign tasks at any level at any time until completion, regardless of Scenario settings.

---

## Queue Metrics

| Metric | Description |
|--------|-------------|
| **Queue Depth** | Number of pending tasks in the queue |
| **Average Wait Time** | Average time from creation to first assignment |
| **Average Resolution Time** | Average time from creation to completion |
| **Escalation Rate** | Percentage of tasks escalated beyond Level 0 |
| **SLA Compliance** | Percentage of tasks meeting SLA targets |
| **Abandon Rate** | Percentage of tasks abandoned by agents |

---

## Queue Configuration Versioning

Queue configurations are versioned. Changes create a new version:

```json
{
  "queue_id": "doc-verification-queue",
  "version": 3,
  "changes": {
    "escalation_matrix.levels[1].threshold_minutes": {
      "from": 90,
      "to": 60
    }
  },
  "changed_at": "2026-01-05T14:00:00Z",
  "changed_by": "supervisor-jane"
}
```

**Note:** Active tasks continue under the queue configuration version at task creation time.

---

## Related Documentation

- [Task Management Overview](./README.md)
- [Task Lifecycle](./task-lifecycle.md)
- [Task Allocation](./task-allocation.md)
- [Workbench Management](../workbench-management/README.md)
- [Cipher IAM](../supporting-systems/cipher-iam.md)

---
