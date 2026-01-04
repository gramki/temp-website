# Task Assignment

> **Status:** 🔴 Stub — Placeholder for expansion

Task Assignment handles how tasks are **assigned to human and AI agents**—including direct assignment, queue-based assignment, and AI delegation.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Match tasks to appropriate agents |
| **Methods** | Queue, Direct, Group, AI Delegation |
| **Integration** | Cipher IAM, Seer |

---

## Assignment Methods

### Queue Assignment
Task assigned to a queue; agents claim from queue:
```
Task → Queue → Available Agent Claims
```

### Direct Assignment
Task assigned to specific user:
```
Task → Specific User (by ID)
```

### Group Assignment
Task assigned to group; any member can complete:
```
Task → User Group → Any Member Claims
```

### AI Delegation
Task delegated to AI agent via Seer:
```
Task → Seer Connector → Employed Agent
```

---

## Assignment Schema

```yaml
task_assignment:
  task_id: string
  
  # Assignment target (one of)
  queue_id: string          # queue assignment
  user_id: string           # direct assignment
  group_id: string          # group assignment
  ai_agent_id: string       # AI delegation
  
  # Assignment metadata
  assigned_by: string       # who/what created assignment
  assigned_at: datetime
  reason: string            # optional reason
  
  # Constraints
  due_date: datetime
  priority: enum
  required_skills: array
```

---

## AI Agent Delegation

From Hub Architecture:
> *"Hub must have a clear specification for delegation of tasks to AI agents"*

### Delegation Contract

| Element | Description |
|---------|-------------|
| **Task Specification** | What needs to be done |
| **Authority Scope** | What the agent is authorized to do |
| **Context** | Relevant information for the task |
| **Completion Criteria** | How to determine success |
| **Escalation Path** | What to do if stuck |

### AI Agent Subscription

AI Agents may subscribe to specific events:
- New task assigned
- Task deadline approaching
- Case phase changed
- Escalation triggered

---

## Skill Matching

| Factor | Description |
|--------|-------------|
| **Required Skills** | Skills needed for the task |
| **Agent Skills** | Skills the agent has |
| **Skill Level** | Proficiency level required |
| **Certification** | Required certifications |

---

## Workload Balancing

| Strategy | Description |
|----------|-------------|
| **Capacity** | Consider agent capacity |
| **Current Load** | Factor in current assignments |
| **Availability** | Check agent availability |
| **Affinity** | Prefer agents with context |

---

## Cipher Integration

Task assignment references Cipher for:
- User identity and groups
- Role-based eligibility
- Agent enrollment status
- Permission verification

---

## Related Documentation

- [Task Management Overview](./README.md)
- [Task Queues](./task-queues.md)
- [Task Lifecycle](./task-lifecycle.md)
- [Cipher IAM](../supporting-systems/cipher-iam.md)

---

*TODO: Detailed design — AI delegation protocol, skill matching algorithms, load balancing*

