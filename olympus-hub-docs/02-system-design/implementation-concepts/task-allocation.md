# Task Allocation

> **Category:** Request and Task

---

## Overview

**Task Allocation** is the process by which tasks are assigned to agents from a Task Queue. The allocation engine evaluates candidate agents, applies configured algorithms, and records assignments. Allocation can be immediate or deferred, and may be rebalanced as workload changes.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Task** as a unit of work and **Agent** as the executor. Task Allocation is the implementation of how tasks reach agents.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Task assignment | Task Allocation | How tasks are assigned to agents |
| Agent availability | Agent State | Allocation considers agent capacity |

### Gap This Fills

The ontology describes tasks and agents. Task Allocation specifies:
1. **Algorithm**: How are agents selected?
2. **Timing**: When does allocation happen?
3. **Rebalancing**: How is workload managed over time?

---

## Definition

**Task Allocation** is the process of:
- Resolving candidate agents from queue specification
- Collecting agent state (capacity, current load)
- Executing allocation algorithm
- Recording assignment and notifying

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Task Queue scoped; per queue configuration |
| **Lifecycle** | Triggered on task creation or state change |
| **Ownership** | Task Management system performs allocation |
| **Multiplicity** | Multiple algorithms available |

---

## Structure

### Allocation Engine Components

```
Allocation Engine
├── Candidate Resolver
│   └── Resolve agents from queue specification
├── Agent State Collector
│   └── Get current load, capacity, availability
├── Algorithm Executor
│   └── Run configured algorithm
└── Assignment Recorder
    └── Record assignment, notify agent
```

### Allocation Algorithms

| Algorithm | Description | Use Case |
|-----------|-------------|----------|
| **Round Robin** | Rotate through agents | Fair distribution |
| **Least Loaded** | Assign to least busy agent | Workload balancing |
| **Skill-Based** | Match task skills to agent skills | Specialized work |
| **Affinity-Based** | Same agent for related tasks | Continuity |
| **Pull-Based** | Agent chooses from queue | Self-service |

### Algorithm Configuration

```yaml
task_queue:
  id: tier-1-disputes
  
  allocation:
    algorithm: least_loaded
    
    parameters:
      # Algorithm-specific settings
      load_metric: active_tasks      # active_tasks | weighted_complexity
      capacity_source: iam_profile   # Where to find agent capacity
      
    timing:
      mode: immediate               # immediate | deferred | pull
      rebalance_interval_minutes: 30
      
    fallback:
      algorithm: round_robin        # If primary fails
```

---

## Behavior

### Allocation Flow

```
1. Task created and assigned to queue
   └── Task status: PENDING

2. Candidate Resolver runs:
   ├── Read queue specification
   ├── Resolve logical references (role, group, etc.)
   └── Build candidate agent list

3. Agent State Collector gathers:
   ├── Current task count per agent
   ├── Capacity from IAM profile
   └── Availability status

4. Algorithm Executor selects agent:
   ├── Apply algorithm logic
   ├── Consider escalation level
   └── Select best candidate

5. Assignment Recorder:
   ├── Update task with assignee
   ├── Update task status: ASSIGNED
   └── Notify agent
```

### Timing Modes

| Mode | Behavior |
|------|----------|
| **Immediate** | Assign as soon as task created |
| **Deferred** | Wait for agent availability |
| **Pull** | Agent retrieves from queue |

### Rebalancing

```
Periodic rebalancing:
1. Scheduler triggers rebalance
2. For each non-terminal task:
   ├── Recalculate optimal assignment
   ├── If better candidate exists and allowed:
   │   └── Reassign (with notification)
   └── Record rebalance event
```

### Candidate Resolution

| Source Type | Resolution |
|-------------|------------|
| **IAM Role** | Query Cipher IAM for role members |
| **IAM Group** | Query Cipher IAM for group members |
| **Workbench Role** | Resolve from workbench config |
| **Request Role** | Dynamic: subject, originator, all actors |
| **Explicit Users** | Direct user list |

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Task Queue | ← configured by | Queue defines algorithm |
| Cipher IAM | → queries | Resolve candidates, skills |
| Agent | → assigns to | Agent receives task |
| Notification Services | → triggers | Agent notified of assignment |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Single assignee per level** | One agent assigned per escalation level |
| **Capacity respected** | Don't exceed agent capacity |
| **Algorithm configured** | Queue must have valid algorithm |
| **Candidate required** | At least one candidate must exist |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Flexible algorithms** | Choose appropriate for use case |
| ✅ **Automatic assignment** | No manual intervention |
| ✅ **Load balancing** | Workload distributed fairly |
| ✅ **Skill matching** | Right agent for right task |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Algorithm complexity** | Start with simple; iterate |
| ⚠️ **State synchronization** | Periodic refresh of agent state |

---

## Examples

### Example 1: Least Loaded Allocation

```
Queue: tier-1-disputes
Algorithm: least_loaded

Candidates (at allocation time):
├── agent-alice: 3 tasks (capacity: 5)
├── agent-bob: 4 tasks (capacity: 5)
└── agent-carol: 2 tasks (capacity: 5)

Selection: agent-carol (least loaded)
```

### Example 2: Skill-Based Allocation

```yaml
task:
  required_skills:
    - fraud_investigation
    - spanish_language

candidates:
  - agent-alice:
      skills: [fraud_investigation, english_language]
      match_score: 50%
  - agent-bob:
      skills: [general_investigation, spanish_language]
      match_score: 50%
  - agent-carol:
      skills: [fraud_investigation, spanish_language]
      match_score: 100%

selection: agent-carol (best skill match)
```

---

## Implementation Notes

### For Developers

- Configure appropriate algorithm for workload type
- Ensure IAM skills are maintained for skill-based routing
- Consider escalation interaction with allocation

### For Operators

- Monitor allocation queue depth
- Check for stuck tasks (no candidates)
- Review rebalancing frequency and impact

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Escalation Matrix](./escalation-matrix.md) | Escalation adds candidates for allocation |
| [Request Lifecycle](./request-lifecycle.md) | Tasks created within requests |
| [Persona](./persona.md) | Agents are users with Agent persona |

---

## References

- [Task Allocation Subsystem](../../04-subsystems/task-management/task-allocation.md)
- [Task Management Overview](../../04-subsystems/task-management/README.md)

