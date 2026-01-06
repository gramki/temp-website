# Escalation Matrix

> **Category:** Request and Task

---

## Overview

The **Escalation Matrix** is a multi-level agent assignment configuration within a Task Queue. When tasks remain unresolved beyond threshold times, escalation adds agents at higher levels to the assignment, creating cumulative visibility and accountability without removing original assignees.

---

## Ontology Context

### Relationship to Ontology

The ontology describes task completion and SLA but doesn't detail escalation mechanics. Escalation Matrix is the implementation of time-based workload escalation.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| SLA enforcement | Escalation triggers | Escalation helps meet SLA |
| Multi-level review | Escalation levels | Senior involvement when needed |

### Gap This Fills

The ontology focuses on concepts. Escalation Matrix specifies:
1. **Levels**: How many escalation tiers exist?
2. **Thresholds**: When does each level trigger?
3. **Cumulative assignment**: All levels remain assigned
4. **Candidate specification**: Who at each level?

---

## Definition

**Escalation Matrix** is a Task Queue configuration that:
- Defines escalation levels with time thresholds
- Specifies candidate agents per level
- Triggers escalation when tasks exceed thresholds
- Adds assignees cumulatively (doesn't replace)

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Task Queue level; applies to all tasks in queue |
| **Lifecycle** | Configured at queue creation; triggers during task lifecycle |
| **Ownership** | Supervisor configures; Task Management executes |
| **Multiplicity** | Multiple levels per matrix |

---

## Rationale

### Why This Design?

Cumulative escalation enables:
1. **Visibility**: Supervisors see tasks before they breach SLA
2. **Accountability**: Original assignee remains responsible
3. **Flexibility**: Multiple escalation strategies possible
4. **Documentation**: Clear record of escalation actions

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Replacement on escalation** | Loses context; disconnects original assignee |
| **Manual escalation only** | Reactive; may miss SLA |
| **Single escalation level** | Insufficient for complex workflows |

---

## Structure

### Escalation Matrix Schema

```yaml
task_queue:
  id: tier-1-disputes
  
  escalation_matrix:
    # Level 0: Default assignment
    - level: 0
      candidates:
        type: iam_role
        role: dispute-analyst
      threshold_minutes: 0  # Immediate
      
    # Level 1: Senior analyst after 2 hours
    - level: 1
      candidates:
        type: iam_role
        role: senior-dispute-analyst
      threshold_minutes: 120
      
    # Level 2: Supervisor after 4 hours
    - level: 2
      candidates:
        type: workbench_role
        role: supervisor
      threshold_minutes: 240
      
    # Level 3: Manager after 8 hours
    - level: 3
      candidates:
        type: explicit_users
        users: ["manager-alice", "manager-bob"]
      threshold_minutes: 480
```

### Candidate Specification Types

| Type | Description | Example |
|------|-------------|---------|
| **iam_role** | IAM role membership | `dispute-analyst` |
| **iam_group** | IAM group membership | `tier-1-team` |
| **workbench_role** | Workbench-defined role | `supervisor` |
| **request_role** | Request-scoped role | `subject`, `originator` |
| **explicit_users** | Named user list | `["user-a", "user-b"]` |

---

## Behavior

### How Escalation Works

```
Task created at T=0
├── Level 0 assignment (dispute-analyst)
│   └── Agent-Alice assigned
│
T+120 minutes (no completion)
├── Level 1 escalation triggered
│   ├── Senior-analyst candidates resolved
│   ├── Agent-Bob assigned (cumulative)
│   └── Agent-Alice remains assigned
│
T+240 minutes (no completion)
├── Level 2 escalation triggered
│   ├── Supervisor assigned (cumulative)
│   └── Agent-Alice, Agent-Bob remain assigned
│
Task completed at T+300 by Agent-Bob
└── All levels closed
```

### Escalation Triggers

| Trigger | Condition |
|---------|-----------|
| **Time-based** | Task age exceeds level threshold |
| **Manual** | Supervisor forces escalation |
| **Status-based** | Task put on hold (may pause escalation) |

### Cumulative Assignment

```
After escalation to Level 2:

Task assignees:
├── Level 0: Agent-Alice (original)
├── Level 1: Agent-Bob (senior)
└── Level 2: Supervisor-Carol

All are:
├── Notified
├── Can complete the task
├── Are actors on the request
└── Receive updates
```

### Timer Behavior

| Scenario | Timer Behavior |
|----------|----------------|
| **Task pending** | Timer running |
| **Task in progress** | Timer running (configurable) |
| **Task on hold** | Timer paused (configurable) |
| **Task completed/cancelled** | Timer stopped; no further escalation |

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Task Queue | ↑ belongs to | Matrix is queue configuration |
| Task Allocation | → triggers | Escalation triggers new allocation |
| Notification Services | → triggers | Escalation notifications sent |
| Agent | → assigns | Agents added at each level |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Level ordering** | Levels must be in ascending order |
| **Threshold ordering** | Higher levels have higher thresholds |
| **Cumulative only** | Lower level assignees never removed |
| **At least L0** | Level 0 must exist |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Visibility** | Senior staff see delayed tasks |
| ✅ **Accountability** | Original assignee stays involved |
| ✅ **Flexibility** | Configure thresholds per queue |
| ✅ **Audit trail** | Escalation events recorded |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Multiple assignees** | Clear "first to complete wins" |
| ⚠️ **Notification volume** | Escalation notifications configurable |

---

## Examples

### Example 1: Simple Two-Level Escalation

```yaml
escalation_matrix:
  - level: 0
    candidates:
      type: iam_group
      group: customer-service
    threshold_minutes: 0
    
  - level: 1
    candidates:
      type: workbench_role
      role: supervisor
    threshold_minutes: 60
```

### Example 2: Request-Scoped Escalation

```yaml
# Escalate to request originator if analyst doesn't complete
escalation_matrix:
  - level: 0
    candidates:
      type: iam_role
      role: analyst
    threshold_minutes: 0
    
  - level: 1
    candidates:
      type: request_role
      role: originator  # Person who initiated the request
    threshold_minutes: 120
```

---

## Implementation Notes

### For Supervisors

- Set thresholds with SLA in mind
- Consider time zones for threshold calculation
- Review escalation patterns for optimization

### For Operators

- Monitor escalation frequency per queue
- Check for queues with high escalation rates
- Verify candidate resolution is working

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Task Allocation](./task-allocation.md) | Escalation triggers allocation at new level |
| [Request Lifecycle](./request-lifecycle.md) | Task states affect escalation |
| [Notification Services](./notification-services.md) | Escalation generates notifications |

---

## References

- [Task Queues Subsystem](../../04-subsystems/task-management/task-queues.md)
- [Escalation Matrix Details](../../04-subsystems/task-management/task-queues.md#escalation-matrix)

