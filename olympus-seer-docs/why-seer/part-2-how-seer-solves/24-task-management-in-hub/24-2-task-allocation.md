# 24.2 Task Allocation

Task Allocation handles how tasks are matched to agents through allocation algorithms that consider workload, capacity, skills, and queue configuration. Allocation algorithms execute when tasks are created, escalated, or abandoned, ensuring that work is distributed efficiently and fairly across available agents.

Task allocation is a critical capability that enables Hub to match tasks to agents based on workload, skills, and availability. Allocation algorithms support various strategies (round-robin, least-loaded, affinity-based, skill-based, pull-based) and can be configured per queue to match organizational needs.

## Purpose of this Subsection

This subsection describes how Hub allocates tasks to agents. It explains allocation algorithms, escalation mechanisms, special queues, and how allocation integrates with agent state and Cipher IAM.

## Core Concepts & Definitions

### Allocation vs Assignment

| Term | Description |
|------|-------------|
| **Allocation** | The process executed by the allocation algorithm to match tasks to agents |
| **Assignment** | The result of allocation—an agent is now assigned to the task |

Allocation is the process; assignment is the result.

### Allocation Engine

The **Allocation Engine** executes allocation algorithms to assign tasks to agents. The Allocation Engine:
*   **Resolves Candidates**: Resolves queue candidate specifications to actual user IDs
*   **Collects Agent State**: Collects current task load, availability, affinity, and skills for each candidate
*   **Executes Algorithm**: Executes the selected allocation algorithm with agent state and task context
*   **Records Assignment**: Records assignment in Task Registry and publishes TASK_ASSIGNED event

Allocation Engine ensures that tasks are matched to agents efficiently and fairly.

### Allocation Algorithms

**Allocation algorithms** determine how tasks are matched to agents:

| Algorithm | Description |
|-----------|-------------|
| **Round Robin** | Distributes tasks evenly across available agents in rotation |
| **Round Robin with Capacity** | Like Round Robin, but respects agent capacity limits |
| **Least Loaded** | Assigns to the agent with the fewest current tasks |
| **Affinity-Based** | Prefers agents with prior context on the same request or subject |
| **Skill-Based** | Matches tasks to agents with required skills |
| **Pull-Based** | Tasks wait in queue; agents pull/claim when ready |

Allocation algorithms enable organizations to match tasks to agents based on their specific needs.

### Escalation Matrix

The **Escalation Matrix** defines multiple levels of agent assignment within a Task Queue:

| Attribute | Description |
|-----------|-------------|
| **Levels** | 0 to N, where 0 is the default starting level |
| **Threshold Time** | Duration after which task escalates to next level |
| **Level Candidates** | Agents eligible at each level (by role, group, etc.) |
| **Cumulative Assignment** | All levels become assignees; does not replace lower levels |

Escalation Matrix enables multi-level assignment for complex work.

## Conceptual Models / Frameworks

### The Allocation Engine Model

Allocation Engine executes allocation:

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

This model ensures that allocation is efficient, fair, and configurable.

### The Escalation Model

Escalation adds assignees without changing task state:

```
Task Created (Level 0)
    ↓
Allocated to Level 0 Agents
    ↓
Threshold Time Exceeded
    ↓
Escalated to Level 1
    ↓
Allocated to Level 1 Agents (in addition to Level 0)
    ↓
Both Levels Remain Assignees
```

This model enables multi-level assignment for complex work.

## Systemic and Enterprise Considerations

### Allocation Triggers

Allocation is triggered by:
*   **Task Created**: New task enters queue at Level 0
*   **Escalation**: Task escalates to higher level; allocate at new level
*   **Abandon**: Agent abandons task; reallocate at same level
*   **Manual Release**: Agent releases task back to queue
*   **Periodic Rebalance**: Algorithm-specific periodic review of assignments

Allocation triggers ensure that tasks are allocated promptly and fairly.

### Candidate Resolution

Candidate Resolution resolves queue candidate specifications to actual user IDs:

| Candidate Type | Resolution |
|----------------|------------|
| **iam_role** | Query Cipher IAM for users with role |
| **iam_user_group** | Query Cipher IAM for group members |
| **workbench_role** | Query Workbench config for named users |
| **request_role** | Query Request for subject/originator/actors |
| **explicit_users** | Use provided user list |

Candidate Resolution ensures that allocation algorithms operate on actual user IDs.

### Agent State

Allocation Engine considers agent state when making decisions:

| State | Description |
|-------|-------------|
| **available** | Ready to receive new tasks |
| **busy** | Working, but can receive if under capacity |
| **away** | Temporarily unavailable (break, meeting) |
| **offline** | Not logged in or off shift |
| **do_not_disturb** | Explicitly blocked from new assignments |

Agent state ensures that allocation respects agent availability and capacity.

### Workload Rebalancing

Some algorithms support periodic rebalancing of assignments:

| Parameter | Description |
|-----------|-------------|
| `enabled` | Whether rebalancing is active |
| `interval_minutes` | How often to check for imbalance |
| `threshold_imbalance_percent` | Imbalance threshold to trigger rebalance |

Workload rebalancing ensures that work is distributed fairly over time.

### Abandon Handling

When an agent abandons a task:
1. **Record Abandon**: Capture abandon event as memo
2. **Return to Queue**: Task returns to PENDING at same escalation level
3. **Exclude Recent Abandoner**: Algorithm may exclude the abandoning agent
4. **Reallocate**: Run allocation algorithm again

Abandon handling ensures that abandoned tasks are reallocated promptly.

## Common Misconceptions & Failure Modes

### Misconception: One Algorithm Fits All

Some organizations assume that one allocation algorithm fits all queues. However, different queues have different needs: some need round-robin for fairness, others need skill-based for expertise, others need affinity-based for continuity.

**Failure mode**: Organizations use a single algorithm for all queues, resulting in suboptimal allocation and reduced productivity.

### Misconception: Escalation Replaces Assignees

Some organizations assume that escalation replaces lower-level assignees. However, escalation adds assignees cumulatively—all levels remain assignees.

**Failure mode**: Organizations design systems where escalation replaces assignees, causing confusion and breaking workflows.

### Misconception: Allocation Is Always Immediate

Some organizations assume that allocation is always immediate. However, allocation can be deferred when no eligible agents are available, and some algorithms support scheduled allocation.

**Failure mode**: Organizations expect immediate allocation, leading to confusion when tasks remain PENDING.

## Practical Implications

### Algorithm Selection

Organizations should select allocation algorithms that:
*   **Match Queue Needs**: Algorithms match the specific needs of each queue
*   **Support Escalation**: Algorithms support escalation mechanisms
*   **Respect Capacity**: Algorithms respect agent capacity limits
*   **Enable Rebalancing**: Algorithms support workload rebalancing when needed

Algorithm selection directly impacts allocation efficiency and fairness.

### Escalation Configuration

Organizations should configure escalation that:
*   **Matches Work Complexity**: Escalation thresholds match work complexity
*   **Supports Multi-Level Assignment**: Escalation supports cumulative assignment
*   **Aligns with SLAs**: Escalation thresholds align with SLA thresholds
*   **Enables Proactive Intervention**: Escalation enables proactive intervention before SLA breach

Escalation configuration directly impacts work quality and customer satisfaction.

## Cross-References

*   **Section 24.1 (Task Lifecycle)**: Describes task states that allocation affects
*   **Section 24.3 (Agent Task Operations)**: Describes how agents work on allocated tasks
*   **Section 12.4 (Deep Observability)**: Describes how Signal Exchange provides allocation observability

---

**References:**

*   `olympus-hub-docs/04-subsystems/task-management/task-allocation.md` — Task allocation design
*   `olympus-hub-docs/04-subsystems/task-management/task-queues.md` — Task queue design
