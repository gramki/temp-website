# Manual Task Application

> **Status:** 🔴 Stub — Placeholder for expansion

The Manual Task Application is a **pass-through Hub Application** that creates a single manual task for a Request when no automation is available. The Request status is auto-wired to the Task status.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Create manual tasks for requests without automation |
| **Task Creation** | Exactly one task per request |
| **Assignment** | Explicit — to a queue or specific agent |
| **Status Wiring** | Request status = Task status (1:1 auto-wired) |
| **Runtime** | Built-in Hub Application (no external runtime) |

---

## When to Use

Use the Manual Task Application when:

1. **No automation exists yet** — A scenario needs human handling before automation is built
2. **Pure manual work** — The work is inherently manual with no automation benefit
3. **Fallback scenario** — As a fallback when automated processing fails
4. **Simple pass-through** — Signal needs to become a task without processing logic

---

## How It Works

```
Signal
   │
   ▼
Trigger → Scenario (Manual Task Application)
   │
   ▼
┌─────────────────────────────────────────┐
│      Manual Task Application            │
│                                         │
│  1. Receive Request                     │
│  2. Create exactly ONE Task             │
│  3. Assign to queue or agent            │
│  4. Wire Task status → Request status   │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│              Task                        │
│                                         │
│  Queue: specified-queue                  │
│  OR                                      │
│  Agent: specified-agent                  │
│                                         │
│  Status changes auto-update Request     │
└─────────────────────────────────────────┘
```

---

## Status Auto-Wiring

The Manual Task Application creates a **1:1 relationship** between Request and Task:

| Task Status | Request Status |
|-------------|----------------|
| Created | Active |
| Assigned | Active |
| In Progress | Active |
| Completed | Completed |
| Cancelled | Cancelled |
| Failed | Failed |

This is different from other Hub Applications where:
- Multiple tasks may exist per request
- Request status is determined by application logic
- Task completion may not directly map to Request completion

---

## Configuration

### Scenario Definition

```yaml
scenario:
  id: "manual-review-scenario"
  name: "Manual Review"
  
  # Use Manual Task Application
  application:
    type: manual_task_application    # Built-in type
  
  # Task Configuration
  task_config:
    # Assignment (one of the following)
    assignment:
      type: enum                     # queue | agent | role
      queue_id: string               # If type is queue
      agent_id: string               # If type is agent
      role_id: string                # If type is role (any agent with role)
    
    # Task Details
    task_template:
      title: string                  # Task title template (supports variables)
      description: string            # Task description template
      priority: enum                 # low | normal | high | critical
      
      # SLA
      sla:
        target_time: duration        # e.g., "PT4H" (4 hours)
        escalation_policy: string    # Reference to escalation policy
    
    # What the agent sees
    display:
      instructions: string           # Instructions for the agent
      form_id: string                # Optional form to complete
      entity_view: string            # Entity view to display
```

### Example: Unrecognized Exception Handler

```yaml
scenario:
  id: "unrecognized-exception"
  name: "Handle Unrecognized Exception"
  description: "Route unrecognized exceptions to operations team for manual review"
  
  application:
    type: manual_task_application
  
  task_config:
    assignment:
      type: queue
      queue_id: "ops-exceptions-queue"
    
    task_template:
      title: "Review Exception: {{signal.exception_type}}"
      description: |
        An unrecognized exception was received from {{signal.source}}.
        Please investigate and take appropriate action.
      priority: high
      sla:
        target_time: "PT2H"
        escalation_policy: "ops-escalation"
    
    display:
      instructions: |
        1. Review the exception details
        2. Investigate the root cause
        3. Take corrective action or escalate
        4. Document findings in the resolution notes
      entity_view: "exception-detail-view"
```

### Example: Manual Approval

```yaml
scenario:
  id: "manual-approval"
  name: "Manual Approval Required"
  
  application:
    type: manual_task_application
  
  task_config:
    assignment:
      type: role
      role_id: "approver"
    
    task_template:
      title: "Approval Required: {{request.subject}}"
      description: "Review and approve or reject the request"
      priority: normal
      sla:
        target_time: "PT24H"
    
    display:
      instructions: "Review the request details and approve or reject"
      form_id: "approval-form"  # Form with Approve/Reject buttons
```

---

## Task Assignment Options

| Type | Description | Use Case |
|------|-------------|----------|
| **Queue** | Assign to a task queue | General pool of agents |
| **Agent** | Assign to specific agent | Known responsible person |
| **Role** | Assign to any agent with role | Capability-based assignment |

### Dynamic Assignment

Assignment can use template variables from the signal/request:

```yaml
assignment:
  type: queue
  queue_id: "{{signal.department}}-queue"  # Dynamic based on signal
```

---

## Agent Experience

When a Manual Task is created, the assigned agent sees:

```
┌─────────────────────────────────────────────────────────────────┐
│  TASK: Review Exception: PAYMENT_TIMEOUT                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Priority: HIGH          SLA: 2 hours          Status: Assigned │
│                                                                  │
│  ─────────────────────────────────────────────────────────────  │
│                                                                  │
│  INSTRUCTIONS:                                                   │
│  1. Review the exception details                                 │
│  2. Investigate the root cause                                   │
│  3. Take corrective action or escalate                          │
│  4. Document findings in the resolution notes                   │
│                                                                  │
│  ─────────────────────────────────────────────────────────────  │
│                                                                  │
│  EXCEPTION DETAILS:                                              │
│  Source: Payment Gateway                                         │
│  Time: 2026-01-04 14:32:15 UTC                                  │
│  Type: PAYMENT_TIMEOUT                                           │
│  Details: Transaction ID TXN-12345 timed out after 30s          │
│                                                                  │
│  ─────────────────────────────────────────────────────────────  │
│                                                                  │
│  [Start Working]  [Reassign]  [Escalate]                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Task Actions

The agent can:

| Action | Effect on Task | Effect on Request |
|--------|---------------|-------------------|
| **Start Working** | In Progress | Active |
| **Complete** | Completed | Completed |
| **Cancel** | Cancelled | Cancelled |
| **Reassign** | Reassigned (stays active) | Active |
| **Escalate** | Escalated | Active (escalation tracked) |

---

## Comparison with Other Applications

| Aspect | Manual Task App | Other Hub Apps |
|--------|-----------------|----------------|
| **Tasks per Request** | Exactly 1 | 0 to many |
| **Task Logic** | None (pass-through) | Application-defined |
| **Status Wiring** | Automatic 1:1 | Application-controlled |
| **Assignment** | Explicit in config | Application policy |
| **Use Case** | No automation needed | Automated processing |

---

## When NOT to Use

Don't use Manual Task Application when:

- Multiple tasks are needed for a request
- Task creation depends on business logic
- Request may complete without a task
- Complex assignment rules are needed
- Multiple agents need to collaborate

In these cases, build a proper Hub Application using an Automation Runtime.

---

## Related Documentation

- [Hub Native Utilities](./README.md) — Overview
- [Task Management](../task-management/README.md) — Task queues and lifecycle
- [Workbench Management](../workbench-management/README.md) — Scenario configuration
- [Signal Exchange](../signal-exchange/README.md) — Request creation

---

*TODO: Detailed design — form integration, escalation handling, SLA enforcement*

