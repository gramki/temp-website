# Task Allocation

> **Status:** 🟡 Draft — Allocation engine and algorithms defined

Task Allocation handles how tasks are **matched to agents** through allocation algorithms that consider workload, capacity, and queue configuration.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Match tasks to appropriate agents from queue candidates |
| **Process** | Allocation (algorithm execution) → Assignment (result) |
| **Triggers** | Task creation, escalation, abandon, periodic rebalancing |

---

## Terminology

| Term | Description |
|------|-------------|
| **Allocation** | The process of running an algorithm to select agent(s) for a task |
| **Assignment** | The result of allocation—agent is now assigned to the task |
| **Candidate** | Agent eligible for assignment based on queue definition |
| **Resolved Candidates** | Actual users after resolving role/group references |

---

## Allocation Engine

The Allocation Engine executes allocation algorithms to assign tasks to agents.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          ALLOCATION ENGINE                                   │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                      CANDIDATE RESOLVER                                │  │
│  │                                                                        │  │
│  │  Inputs:                                                               │  │
│  │  • Queue candidate specification (role, group, explicit, request-role) │  │
│  │  • Escalation level                                                    │  │
│  │  • Request context (for request-role resolution)                       │  │
│  │                                                                        │  │
│  │  Outputs:                                                              │  │
│  │  • List of eligible user IDs                                           │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                    │                                         │
│                                    ▼                                         │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                      AGENT STATE COLLECTOR                             │  │
│  │                                                                        │  │
│  │  For each candidate, collects:                                         │  │
│  │  • Current task load                                                   │  │
│  │  • Availability status                                                 │  │
│  │  • Affinity data (past work on same request/subject)                   │  │
│  │  • Skill profile                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                    │                                         │
│                                    ▼                                         │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                      ALGORITHM EXECUTOR                                │  │
│  │                                                                        │  │
│  │  Inputs:                                                               │  │
│  │  • Resolved candidates with state                                      │  │
│  │  • Task context                                                        │  │
│  │  • Algorithm parameters from queue configuration                       │  │
│  │                                                                        │  │
│  │  Executes: Selected allocation algorithm                               │  │
│  │                                                                        │  │
│  │  Outputs:                                                              │  │
│  │  • Selected agent(s) for assignment                                    │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                    │                                         │
│                                    ▼                                         │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                      ASSIGNMENT RECORDER                               │  │
│  │                                                                        │  │
│  │  • Records assignment in Task Registry                                 │  │
│  │  • Publishes TASK_ASSIGNED event                                       │  │
│  │  • Triggers notification to assigned agent(s)                          │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Allocation Triggers

| Trigger | Description |
|---------|-------------|
| **Task Created** | New task enters queue at Level 0 |
| **Escalation** | Task escalates to higher level; allocate at new level |
| **Abandon** | Agent abandons task; reallocate at same level |
| **Manual Release** | Agent releases task back to queue |
| **Periodic Rebalance** | Algorithm-specific periodic review of assignments |

---

## Allocation Algorithms

Each Task Queue specifies an allocation algorithm. Algorithms may provide tunable parameters.

### Round Robin

Distributes tasks evenly across available agents in rotation.

```json
{
  "algorithm": "round-robin",
  "parameters": {
    "skip_unavailable": true
  }
}
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `skip_unavailable` | Skip agents marked unavailable | true |

**Behavior:**
- Maintains rotation pointer per queue
- Assigns to next agent in rotation
- Wraps around when reaching end of candidate list

### Round Robin with Capacity

Like Round Robin, but respects agent capacity limits.

```json
{
  "algorithm": "round-robin-with-capacity",
  "parameters": {
    "max_concurrent_tasks": 5,
    "skip_unavailable": true
  }
}
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `max_concurrent_tasks` | Maximum concurrent tasks per agent | 10 |
| `skip_unavailable` | Skip agents marked unavailable | true |

**Behavior:**
- Skips agents at capacity in rotation
- If all agents at capacity, task remains in PENDING until capacity frees

### Least Loaded

Assigns to the agent with the fewest current tasks.

```json
{
  "algorithm": "least-loaded",
  "parameters": {
    "consider_task_weight": false
  }
}
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `consider_task_weight` | Weight tasks by estimated effort | false |

**Behavior:**
- Calculates current load for each candidate
- Assigns to agent with lowest load
- Ties broken by round-robin

### Affinity-Based

Prefers agents with prior context on the same request or subject.

```json
{
  "algorithm": "affinity-based",
  "parameters": {
    "affinity_weight": 0.7,
    "load_weight": 0.3,
    "affinity_sources": ["same_request", "same_subject"]
  }
}
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `affinity_weight` | Weight for affinity score | 0.7 |
| `load_weight` | Weight for load balancing | 0.3 |
| `affinity_sources` | What constitutes affinity | ["same_request"] |

**Behavior:**
- Calculates affinity score based on prior work
- Balances affinity against current load
- Useful for case continuity

### Skill-Based

Matches tasks to agents with required skills.

```json
{
  "algorithm": "skill-based",
  "parameters": {
    "required_skills": ["fraud-investigation", "spanish"],
    "skill_match_mode": "all"
  }
}
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `required_skills` | Skills required for this queue | [] |
| `skill_match_mode` | "all" = must have all, "any" = must have at least one | "all" |

**Behavior:**
- Filters candidates by skill match
- Falls back to least-loaded among qualified agents

### Pull-Based (Agent Claims)

Tasks wait in queue; agents pull/claim when ready.

```json
{
  "algorithm": "pull-based",
  "parameters": {
    "visibility_scope": "all_candidates",
    "claim_timeout_minutes": 5
  }
}
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `visibility_scope` | Who can see unclaimed tasks | "all_candidates" |
| `claim_timeout_minutes` | Time before claim expires if not started | 5 |

**Behavior:**
- Task enters PENDING, visible to all candidates
- Agent claims task → moves to ASSIGNED
- If claim times out without action, returns to PENDING

---

## Allocation Timing

Algorithms can specify when allocation occurs:

| Mode | Description |
|------|-------------|
| **immediate** | Allocate as soon as task enters queue |
| **on_availability** | Wait until an agent becomes available |
| **scheduled** | Allocate at specific intervals |

```json
{
  "algorithm": "round-robin-with-capacity",
  "timing": {
    "mode": "immediate",
    "retry_interval_seconds": 30
  }
}
```

---

## Workload Rebalancing

Some algorithms support periodic rebalancing of assignments.

```json
{
  "algorithm": "least-loaded",
  "rebalancing": {
    "enabled": true,
    "interval_minutes": 15,
    "threshold_imbalance_percent": 30
  }
}
```

| Parameter | Description |
|-----------|-------------|
| `enabled` | Whether rebalancing is active |
| `interval_minutes` | How often to check for imbalance |
| `threshold_imbalance_percent` | Imbalance threshold to trigger rebalance |

**Behavior:**
- Periodically reviews task distribution
- If imbalance exceeds threshold, may reassign tasks
- Only reassigns tasks still in ASSIGNED state (not IN_PROGRESS)

---

## Candidate Resolution

### Resolution Process

```
Queue Candidate Specification
         │
         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      CANDIDATE RESOLVER                                      │
│                                                                              │
│  1. Parse candidate specification type                                       │
│                                                                              │
│  2. Resolve based on type:                                                   │
│     • iam_role → Query Cipher IAM for users with role                        │
│     • iam_user_group → Query Cipher IAM for group members                    │
│     • workbench_role → Query Workbench config for named users                │
│     • request_role → Query Request for subject/originator/actors             │
│     • explicit_users → Use provided user list                                │
│                                                                              │
│  3. Filter by:                                                               │
│     • Active status (not suspended/disabled)                                 │
│     • Workbench enrollment                                                   │
│                                                                              │
│  4. Return resolved user ID list                                             │
└─────────────────────────────────────────────────────────────────────────────┘
         │
         ▼
    Resolved Candidates
```

### Dynamic Resolution for Request Roles

Request-scoped roles are resolved at each allocation run:

```json
{
  "request_id": "req-12345",
  "resolved_roles": {
    "subject": "customer-67890",
    "originator": "channel-web",
    "all_assignees": ["agent-alice", "agent-bob"],
    "all_actors": ["agent-alice", "agent-bob", "agent-charlie"]
  }
}
```

**Note:** `all_actors` grows over time as more agents interact with the request.

---

## Abandon Handling

When an agent abandons a task:

1. **Record Abandon:** Capture abandon event as memo
2. **Return to Queue:** Task returns to PENDING at same escalation level
3. **Exclude Recent Abandoner:** Algorithm may exclude the abandoning agent
4. **Reallocate:** Run allocation algorithm again

```json
{
  "abandon_handling": {
    "exclude_abandoner": true,
    "exclusion_duration_minutes": 60,
    "max_abandons_per_task": 3
  }
}
```

| Parameter | Description |
|-----------|-------------|
| `exclude_abandoner` | Temporarily exclude agent who abandoned |
| `exclusion_duration_minutes` | How long to exclude |
| `max_abandons_per_task` | Max abandons before escalating to supervisor |

---

## Agent State

Allocation Engine considers agent state when making decisions:

```json
{
  "agent_state": {
    "user_id": "agent-alice",
    "availability": "available",
    "current_task_count": 3,
    "max_capacity": 5,
    "skills": ["document-verification", "spanish"],
    "affinity": {
      "recent_requests": ["req-12345", "req-67890"],
      "recent_subjects": ["customer-11111"]
    },
    "shift": {
      "on_shift": true,
      "shift_end": "2026-01-05T18:00:00Z"
    }
  }
}
```

### Availability States

| State | Description |
|-------|-------------|
| **available** | Ready to receive new tasks |
| **busy** | Working, but can receive if under capacity |
| **away** | Temporarily unavailable (break, meeting) |
| **offline** | Not logged in or off shift |
| **do_not_disturb** | Explicitly blocked from new assignments |

---

## Allocation Events

| Event | Description |
|-------|-------------|
| **ALLOCATION_STARTED** | Algorithm execution began |
| **ALLOCATION_COMPLETED** | Agent(s) selected and assigned |
| **ALLOCATION_DEFERRED** | No eligible agent available; will retry |
| **ALLOCATION_FAILED** | Allocation failed after retries |

---

## Integration with Cipher IAM

Allocation Engine queries Cipher IAM for:

| Query | Purpose |
|-------|---------|
| **Users by Role** | Resolve IAM role to user list |
| **Group Members** | Resolve user group to member list |
| **User Status** | Check if user is active/suspended |
| **User Attributes** | Retrieve skills, certifications |

### Skills in IAM Profiles

- Skills are defined in Workbench and Scenario Specifications
- All skills have a **tenant-wide unique code**
- Skills are stored as **Hub-specific extensions** to Cipher IAM profiles
- **Supervisors** assign skills to agents
- Allocation algorithms reference skills from IAM profiles

---

## Algorithm Extensibility

New allocation algorithms can be registered:

```json
{
  "algorithm_registration": {
    "algorithm_id": "custom-priority-based",
    "name": "Custom Priority-Based Allocation",
    "description": "Allocates based on custom priority rules",
    "parameters_schema": {
      "priority_rules": {
        "type": "array",
        "description": "Custom priority rules"
      }
    },
    "implementation": "com.acme.allocation.CustomPriorityAlgorithm"
  }
}
```

---

## Related Documentation

- [Task Management Overview](./README.md)
- [Task Queues](./task-queues.md)
- [Task Lifecycle](./task-lifecycle.md)
- [Cipher IAM](../supporting-systems/cipher-iam.md)

---

