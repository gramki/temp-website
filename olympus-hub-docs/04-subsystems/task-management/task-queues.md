# Task Queues

> **Status:** 🔴 Stub — Placeholder for expansion

Task Queues are the **containers that organize and route tasks** to available agents based on skills, priority, and capacity.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Organize tasks for efficient assignment |
| **Routing** | Skills, priority, capacity, affinity |
| **Integration** | Cipher (groups), Workbench (context) |

---

## Queue Types

| Type | Description | Use Case |
|------|-------------|----------|
| **Priority Queue** | Tasks ordered by priority | Urgent work handling |
| **Skill-based Queue** | Tasks routed by required skills | Specialized work |
| **Round-robin Queue** | Even distribution across agents | Load balancing |
| **Affinity Queue** | Prefer agents with context | Case continuity |

---

## Queue Definition Schema

```yaml
queue:
  # Identity
  id: string
  name: string
  workbench_id: string
  
  # Assignment
  assignment:
    type: enum  # priority | skill | round_robin | affinity
    eligible_groups: array   # Cipher groups
    eligible_roles: array    # Cipher roles
    eligible_agents: array   # specific agents (optional)
  
  # Routing
  routing:
    required_skills: array   # skills required to work queue
    priority_weight: number  # relative queue priority
    max_concurrent: number   # max tasks per agent from this queue
  
  # SLA
  sla:
    response_time: duration  # time to first response
    resolution_time: duration # time to completion
    escalation_rules: array
  
  # Metadata
  status: enum  # active | paused | archived
```

---

## Queue Operations

| Operation | Description |
|-----------|-------------|
| `enqueue` | Add task to queue |
| `claim` | Agent claims next task |
| `assign` | Explicitly assign to agent |
| `release` | Release task back to queue |
| `escalate` | Move to escalation queue |

---

## Queue Metrics

| Metric | Description |
|--------|-------------|
| **Depth** | Number of tasks in queue |
| **Wait Time** | Average time in queue |
| **Processing Time** | Average completion time |
| **SLA Compliance** | % meeting SLA targets |

---

## Related Documentation

- [Task Management Overview](./README.md)
- [Task Assignment](./task-assignment.md)
- [Task Lifecycle](./task-lifecycle.md)

---

*TODO: Detailed design — routing algorithms, capacity management, SLA escalation*

