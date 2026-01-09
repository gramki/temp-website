# Agent Task Operations

> **Status:** 🟡 Draft — Agent and Supervisor operations defined  
> **Last Updated:** 2026-01-08

This document describes how **agents work on tasks** and the operations available to agents and supervisors within Task Management.

This document includes **Directability Operations** — how agents and supervisors handle escalation tasks created when agent outputs are rejected. See [Agent Directability](../../02-system-design/implementation-concepts/agent-directability.md) for the full directability model.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Define agent and supervisor operations on tasks |
| **Channels** | Agent Desk, MS Teams, MCP (Agent Gateway), mobile |
| **Key Component** | Task Solver Interface (UX component) |

---

## Agent Task Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          AGENT TASK WORKFLOW                                 │
│                                                                              │
│  1. NOTIFICATION (optional)                                                  │
│     └── Agent notified of new task assignment                                │
│         (based on workbench, scenario, and agent preferences)                │
│                                                                              │
│  2. DISCOVERY                                                                │
│     └── Agent retrieves assigned tasks through UX channels                   │
│         • Agent Desk (Tasks Console)                                         │
│         • MS Teams                                                           │
│         • MCP (Agent Gateway)                                                │
│         • Mobile app                                                         │
│                                                                              │
│  3. INVESTIGATION                                                            │
│     └── Agent uses Task Solver to understand task and request context        │
│         • Read-only view for investigation                                   │
│         • Access to request history, memos, related tasks                    │
│         • Knowledge base and SOP lookup                                      │
│                                                                              │
│  4. ACTION                                                                   │
│     └── Agent takes action to progress the task                              │
│         • Complete task with outcome                                         │
│         • Add memos/thoughts                                                 │
│         • Reassign to another agent (if permitted)                           │
│         • Place on hold (waiting for external input)                         │
│         • Abandon task (if permitted)                                        │
│                                                                              │
│  5. COMPLETION                                                               │
│     └── Task marked complete or moved to next state                          │
│         • Result payload captured                                            │
│         • Hub Application notified                                           │
│         • Request progresses                                                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Task Discovery

Agents can retrieve their assigned tasks through multiple channels:

### Agent Desk (Tasks Console)

Primary interface for viewing and managing tasks.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          TASKS CONSOLE                                       │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  FILTERS                                                                 ││
│  │  [All Tasks ▼] [All Queues ▼] [Priority ▼] [SLA Status ▼]               ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  TASK LIST                                                               ││
│  │                                                                          ││
│  │  ⚠ Verify KYC Documents          REQ-1234    SLA: 45min    [ASSIGNED]   ││
│  │    Customer: John Smith                                                  ││
│  │                                                                          ││
│  │  ● Review Evidence               REQ-5678    SLA: 2h       [IN_PROGRESS]││
│  │    Customer: Jane Doe                                                    ││
│  │                                                                          ││
│  │  ○ Approve Resolution            REQ-9012    SLA: 4h       [PENDING]    ││
│  │    Customer: Bob Wilson                                                  ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  Click task to open Task Solver                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### MS Teams Integration

Tasks appear as actionable cards in Teams.

### MCP (Agent Gateway)

AI agents retrieve tasks programmatically:

```json
{
  "method": "tasks.list",
  "params": {
    "assignee": "agent-alice",
    "status": ["ASSIGNED", "IN_PROGRESS"],
    "workbench_id": "dispute-ops"
  }
}
```

---

## Task Solver Interface

The Task Solver is a **UX component** that provides agents with context and actions for completing tasks.

### Characteristics

| Aspect | Description |
|--------|-------------|
| **Custom per Task Type** | Each task type has its own solver template |
| **Developer-Defined** | Workbench developers create solver templates in Workbench Studio |
| **Context-Rich** | Presents all relevant information for decision-making |
| **Action-Oriented** | Clear paths to completion |

### View Modes

| Mode | Purpose |
|------|---------|
| **Read-Only View** | Investigation, context gathering |
| **Solver View** | Decision-making, action execution |

### Standard Sections

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TASK SOLVER                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  TASK HEADER                                                             ││
│  │  Task: Verify KYC Documents | Request: REQ-1234 | SLA: 45min remaining  ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  ┌──────────────────────────────┐  ┌──────────────────────────────────────┐ │
│  │  REQUEST CONTEXT             │  │  TASK DETAILS                        │ │
│  │                              │  │                                      │ │
│  │  Customer: John Smith        │  │  Documents to Verify:                │ │
│  │  Subject ID: cust-67890      │  │  • Passport                          │ │
│  │  Scenario: Dispute           │  │  • Utility Bill                      │ │
│  │  Resolution                  │  │                                      │ │
│  │                              │  │  Instructions:                       │ │
│  │  Request Status: Active      │  │  Verify identity documents           │ │
│  │  Created: 2 hours ago        │  │  match customer record               │ │
│  └──────────────────────────────┘  └──────────────────────────────────────┘ │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  ATTACHED DOCUMENTS                                                      ││
│  │  📄 passport.pdf    📄 utility_bill.pdf                                  ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  ACTIONS                                                                 ││
│  │                                                                          ││
│  │  [✓ Approve]  [✗ Reject]  [⏸ Hold]  [↗ Reassign]  [Abandon]             ││
│  │                                                                          ││
│  │  Notes: _______________________________________________                  ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Agent Operations

### Start Work

Agent indicates they are starting work on a task.

```json
{
  "operation": "start_work",
  "task_id": "task-12345",
  "agent_id": "agent-alice"
}
```

**Effect:** Task moves from ASSIGNED to IN_PROGRESS.

### Complete Task

Agent marks task as complete with an outcome.

```json
{
  "operation": "complete",
  "task_id": "task-12345",
  "agent_id": "agent-alice",
  "outcome": {
    "result": "success",
    "payload": {
      "verification_status": "approved",
      "notes": "All documents verified successfully"
    }
  }
}
```

**Effect:**
- Task moves to COMPLETED
- Escalation timers cancelled
- Hub Application notified
- Request may progress

### Place on Hold

Agent pauses work waiting for external input.

```json
{
  "operation": "hold",
  "task_id": "task-12345",
  "agent_id": "agent-alice",
  "reason": "Waiting for customer to provide additional documents"
}
```

**Effect:** Task moves to ON_HOLD. SLA clock behavior depends on configuration.

### Resume Work

Agent resumes work after hold.

```json
{
  "operation": "resume",
  "task_id": "task-12345",
  "agent_id": "agent-alice"
}
```

**Effect:** Task moves from ON_HOLD to IN_PROGRESS.

### Add Memo

Agent adds notes at various scopes.

```json
{
  "operation": "add_memo",
  "agent_id": "agent-alice",
  "memo": {
    "scope": "task",
    "scope_id": "task-12345",
    "content": "Called customer, awaiting callback",
    "visibility": "all_assignees"
  }
}
```

**Memo Scopes:**

| Scope | Description |
|-------|-------------|
| **task** | Attached to specific task |
| **request** | Attached to the request |
| **subject** | Attached to the subject (e.g., customer) |

### Add Thought

Agent adds private working notes (thoughts).

```json
{
  "operation": "add_thought",
  "agent_id": "agent-alice",
  "thought": {
    "scope": "task",
    "scope_id": "task-12345",
    "content": "Need to double-check address format",
    "visibility": "private"
  }
}
```

**Thoughts** are private to the agent unless explicitly shared.

### Reassign Task

Agent reassigns task to another agent (if permitted).

```json
{
  "operation": "reassign",
  "task_id": "task-12345",
  "agent_id": "agent-alice",
  "reassign_to": "agent-bob",
  "reason": "Specialist knowledge required"
}
```

**Constraints (from Scenario configuration):**

| Setting | Behavior |
|---------|----------|
| `same_level` | Can only reassign to agents at same escalation level |
| `higher_level` | Can reassign to same or higher level agents |
| `any` | Can reassign to any eligible agent in the queue |

### Abandon Task

Agent opts out of task without explicit reassignment.

```json
{
  "operation": "abandon",
  "task_id": "task-12345",
  "agent_id": "agent-alice",
  "reason": "Conflict of interest"
}
```

**Effect:**
- Task returns to PENDING at same escalation level
- Allocation algorithm runs to find new assignee
- Abandon recorded as request-scoped memo
- Agent may be excluded from reallocation (algorithm-dependent)

**Constraint:** Only permitted if Scenario configuration allows (`allow_abandon: true`).

---

## Supervisor Operations

Supervisors have elevated privileges for task management.

### View All Tasks

Supervisors can view all tasks in their workbench, not just their own assignments.

### Reassign Any Task

Supervisors can reassign tasks regardless of Scenario reassignment settings.

```json
{
  "operation": "supervisor_reassign",
  "task_id": "task-12345",
  "supervisor_id": "supervisor-jane",
  "reassign_to": "agent-charlie",
  "reason": "Workload balancing",
  "override_scenario_settings": true
}
```

### Cancel Task

Supervisors can cancel tasks.

```json
{
  "operation": "cancel",
  "task_id": "task-12345",
  "supervisor_id": "supervisor-jane",
  "reason": "Request closed by customer"
}
```

### Add/Remove Queue Agents

Supervisors can manually add or remove agents from queue candidates.

```json
{
  "operation": "modify_queue_candidates",
  "queue_id": "doc-verification-queue",
  "supervisor_id": "supervisor-jane",
  "add_users": ["agent-dave"],
  "remove_users": ["agent-eve"],
  "escalation_level": 0
}
```

### Force Escalation

Supervisors can manually escalate a task.

```json
{
  "operation": "force_escalate",
  "task_id": "task-12345",
  "supervisor_id": "supervisor-jane",
  "to_level": 2,
  "reason": "Customer escalation"
}
```

### SLA Override

Supervisors can extend SLA deadlines.

```json
{
  "operation": "extend_sla",
  "task_id": "task-12345",
  "supervisor_id": "supervisor-jane",
  "new_resolution_due_at": "2026-01-06T14:00:00Z",
  "reason": "Customer requested additional time"
}
```

---

## Directability Operations

When an agent's output is **rejected** (by guardrails, policies, or applications), an escalation task is created for human intervention. These operations handle escalation task resolution.

### Acknowledge Escalation

Human acknowledges they are reviewing the rejection.

```json
{
  "operation": "acknowledge_escalation",
  "task_id": "esc-task-12345",
  "agent_id": "supervisor-jane"
}
```

**Effect:**
- Escalation task moves to IN_PROGRESS
- DirectiveResolution record created (subtype: `ack`)
- Accountable Human notification cleared

### Override Decision

Human overrides the rejected decision with a new value.

```json
{
  "operation": "override_decision",
  "task_id": "esc-task-12345",
  "agent_id": "supervisor-jane",
  "override": {
    "original_decision_id": "dec-11111",
    "new_decision": {
      "action": "approve_refund",
      "amount": 150.00,
      "confidence": 1.0
    },
    "rationale": "Customer history justifies approval despite low model confidence",
    "rationale_category": "new_information"
  }
}
```

**Effect:**
- Override Record created in CAF
- DirectiveResolution record created (subtype: `outcome`)
- Escalation task marked COMPLETED
- Original scenario continues with overridden decision

### Change Context and Re-run

Human modifies context and requests agent to re-run.

```json
{
  "operation": "change_context_rerun",
  "task_id": "esc-task-12345",
  "agent_id": "supervisor-jane",
  "context_changes": {
    "additional_context": {
      "customer_tier": "platinum",
      "previous_disputes": [],
      "account_age_years": 12
    },
    "instructions": "Consider customer's long tenure and clean history"
  }
}
```

**Effect:**
- ContextIntervention Record created in CAF
- DirectiveResolution record created (subtype: `outcome`)
- Escalation task marked COMPLETED
- Agent receives new context and re-runs decision

### Reassign to Alternative Agent

Human reassigns the original task to a different agent.

```json
{
  "operation": "reassign_for_retry",
  "task_id": "esc-task-12345",
  "agent_id": "supervisor-jane",
  "reassign": {
    "original_task_id": "task-99999",
    "new_assignee": "senior-analyst-bob",
    "reason": "Specialist required for edge case"
  }
}
```

**Effect:**
- Original task reassigned
- Task History updated (REASSIGNED)
- DirectiveResolution record created (subtype: `outcome`)
- Escalation task marked COMPLETED

### Fail Scenario

Human decides to fail the scenario due to unresolvable rejection.

```json
{
  "operation": "fail_scenario",
  "task_id": "esc-task-12345",
  "agent_id": "supervisor-jane",
  "failure": {
    "reason": "Cannot proceed without customer documentation",
    "failure_code": "MISSING_REQUIRED_DOCS",
    "customer_notification": true
  }
}
```

**Effect:**
- Request marked as FAILED
- All pending tasks CANCELLED
- DirectiveResolution record created (subtype: `outcome`)
- Escalation task marked COMPLETED

### Create Corrective Action

Human creates a corrective action in a different scenario.

```json
{
  "operation": "create_corrective_action",
  "task_id": "esc-task-12345",
  "agent_id": "supervisor-jane",
  "corrective_action": {
    "scenario_id": "manual-review",
    "workbench_id": "dispute-ops",
    "payload": {
      "original_request_id": "req-67890",
      "correction_type": "manual_override",
      "notes": "Requires manual investigation of transaction chain"
    }
  }
}
```

**Effect:**
- New Request created (child of original, or Tool invocation if cross-workbench)
- DirectiveResolution record created (subtype: `outcome`, with spawned_request_id)
- Escalation task marked COMPLETED
- Original request may be put ON_HOLD pending corrective action

---

## AI Agent Operations

AI agents (via MCP) have the same operations as human agents, with additional considerations:

### Task Retrieval

```json
{
  "method": "tasks.get",
  "params": {
    "task_id": "task-12345",
    "include": ["request_context", "related_memos", "solver_template"]
  }
}
```

### Task Completion

```json
{
  "method": "tasks.complete",
  "params": {
    "task_id": "task-12345",
    "outcome": {
      "result": "success",
      "payload": {
        "analysis_complete": true,
        "recommendation": "approve"
      }
    }
  }
}
```

### AI-Specific Considerations

| Aspect | Description |
|--------|-------------|
| **Subscription** | AI agents may subscribe to specific task events |
| **Delegation Spec** | Clear contract for what AI is authorized to do |
| **Escalation/Abandon** | AI agent decides—no conceptual difference from human agents |
| **Audit Trail** | All AI actions recorded for compliance |

**Note:** There is no conceptual difference between Human Agents and AI Agents in Task Management. AI agents can escalate or abandon tasks using the same mechanisms as human agents.

---

## Operation Permissions

| Operation | Agent | Supervisor | AI Agent |
|-----------|-------|------------|----------|
| Start Work | ✓ (own tasks) | ✓ | ✓ (own tasks) |
| Complete | ✓ (own tasks) | ✓ | ✓ (own tasks) |
| Hold/Resume | ✓ (own tasks) | ✓ | ✓ (own tasks) |
| Add Memo | ✓ | ✓ | ✓ |
| Add Thought | ✓ | ✓ | ✓ |
| Reassign | Scenario-dependent | ✓ Always | Scenario-dependent |
| Abandon | Scenario-dependent | ✓ Always | Scenario-dependent |
| Cancel | ✗ | ✓ | ✗ |
| Force Escalate | ✗ | ✓ | ✗ |
| SLA Override | ✗ | ✓ | ✗ |
| Modify Queue | ✗ | ✓ | ✗ |

---

## Task Notifications

Agents are notified about tasks based on configuration layers:

| Layer | Description |
|-------|-------------|
| **Workbench Config** | Default notification settings for the workbench |
| **Scenario Config** | Scenario-specific overrides |
| **Agent Preferences** | Individual agent preferences |

### Notification Events

| Event | Description |
|-------|-------------|
| **TASK_ASSIGNED** | New task assigned to agent |
| **TASK_ESCALATED** | Task escalated (agent added at new level) |
| **SLA_WARNING** | SLA breach approaching |
| **TASK_REASSIGNED** | Task reassigned to/from agent |

---

## Related Documentation

- [Task Management Overview](./README.md)
- [Task Lifecycle](./task-lifecycle.md)
- [Task Queues](./task-queues.md)
- [Agent Desk](../../06-ux-architecture/tenant-domain/agent-desk.md)
- [MCP Channels](../../06-ux-architecture/tenant-domain/mcp-channels.md)
- [Notification Services](../notification-services/README.md)

---

