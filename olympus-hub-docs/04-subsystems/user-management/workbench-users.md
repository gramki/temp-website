# Workbench Users

> **Status:** 🔴 Stub — Placeholder for expansion

Workbench Users operate within specific workbenches and are responsible for day-to-day operational execution and supervision.

---

## Overview

| Aspect | Description |
|--------|-------------|
| **Scope** | Specific Workbench(es) |
| **Domain** | Tenant Domain(s) |
| **Personas** | Agent, Supervisor |
| **Access** | Workbench-scoped, queue-scoped |

---

## Personas

### Agent

| Attribute | Description |
|-----------|-------------|
| **Primary Focus** | Task execution and operational work |
| **Scope** | Assigned workbenches and queues |
| **Type** | Human Agent or AI Agent |

#### Responsibilities

| Area | Responsibilities |
|------|------------------|
| **Tasks** | Complete assigned tasks from queues |
| **Reassignment** | Reassign tasks when unable to complete |
| **Investigation** | Investigate business domain entities and signals |
| **Trigger Scenarios** | Manually trigger scenarios when required |
| **Decisions** | Make decisions within scope of authority |
| **Documentation** | Record thoughts, memos, and rationale |

#### Permissions

| Permission | Scope |
|------------|-------|
| View assigned tasks | Own queues |
| Complete tasks | Assigned tasks |
| Reassign tasks | Own tasks |
| View request details | Assigned requests |
| View entity data | Workbench scope |
| Trigger scenarios | As configured |
| Record decisions | Assigned requests |
| Add memos/thoughts | Assigned requests |

#### Agent Types

| Type | Description |
|------|-------------|
| **Human Agent** | Human user performing operational work |
| **AI Agent** | Seer-powered agent performing automated work |
| **Hybrid** | Tasks may be handled by either human or AI |

---

### Supervisor

| Attribute | Description |
|-----------|-------------|
| **Primary Focus** | Operations oversight and team management |
| **Scope** | Assigned workbenches |

#### Responsibilities

| Area | Responsibilities |
|------|------------------|
| **SLA Review** | Monitor and review SLA compliance |
| **Agent Efficiency** | Review agent performance and efficiency |
| **Operations Effectiveness** | Assess overall operations effectiveness |
| **Queue Management** | Define and manage task queues |
| **Agent Enrollment** | Enrol and remove agents from queues |
| **Escalation Matrix** | Define and manage escalation paths |
| **Availability Control** | Control which agents are available for task assignment |
| **Reassignment** | Override and reassign tasks |

#### Permissions

| Permission | Scope |
|------------|-------|
| View all tasks | Workbench scope |
| Reassign any task | Workbench scope |
| Define queues | Workbench scope |
| Manage queue membership | Workbench scope |
| View agent performance | Workbench scope |
| Define escalation matrix | Workbench scope |
| View SLA dashboards | Workbench scope |
| Override agent availability | Workbench scope |

---

## Queue-Based Access

Agents are enrolled in specific queues:

```yaml
agent:
  id: "agent-12345"
  type: "human"
  workbenches:
    - workbench_id: "dispute-ops"
      queues:
        - queue_id: "dispute-review"
          role: "reviewer"
        - queue_id: "dispute-escalation"
          role: "escalation_handler"
      max_concurrent_tasks: 5
      availability:
        status: "available"
        schedule: "9am-5pm EST"
```

---

## Task Assignment Flow

```
1. Request creates Task
2. Task assigned to Queue
3. Agent picks Task from Queue (or auto-assigned)
4. Agent works on Task
5. Agent completes or reassigns Task
6. If escalation needed → Escalation Matrix
7. Supervisor can override at any point
```

---

## Supervisor Controls

| Control | Description |
|---------|-------------|
| **Queue Definition** | Create queues, set priority, set SLAs |
| **Agent Enrollment** | Add/remove agents from queues |
| **Capacity Control** | Set max concurrent tasks per agent |
| **Availability Override** | Mark agents as available/unavailable |
| **Task Reassignment** | Force reassign tasks |
| **Escalation Override** | Bypass normal escalation, direct assignment |

---

## Related Documentation

- [User Management Overview](./README.md)
- [Tenant Subscription Users](./tenant-subscription-users.md)
- [Tenant Customers](./tenant-customers.md)
- [Task Management](../task-management/README.md)
- [Workbench Management](../workbench-management/README.md)

---

*TODO: Detailed design — queue enrollment, availability scheduling, performance metrics*

