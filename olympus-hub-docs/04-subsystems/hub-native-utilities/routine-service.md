# Routine Service

> **Status:** 🔴 Stub — Placeholder for expansion

The Routine Service provides **agent-scoped scheduled operations** — essentially a personal or assigned checklist for a single agent or supervisor.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Personal/assigned scheduled work items for individual agents |
| **Scope** | Single Agent (vs. Checklist which is workbench-scoped) |
| **Nature** | Stateful — tracks routine instances and completion |
| **Created by** | Supervisors (assigned) or Agents (self-created) |
| **Trigger Source** | Kale (Scheduler) — Time-based signals |

---

## Routine vs Checklist

| Aspect | Checklist | Routine |
|--------|-----------|---------|
| **Scope** | Workbench-level | Agent-level |
| **Ownership** | Workbench governance | Assigned to or created by a single agent |
| **Created by** | Process Architects, Supervisors | Supervisors (assigned) or Agents (self) |
| **Visibility** | Workbench dashboard (supervisors, auditors) | Agent's personal dashboard |
| **Purpose** | Organizational governance and control | Personal productivity or assigned duties |

> **A Routine is a Checklist scoped to a single Agent.**

### Important: Task Assignment is Separate

Both Checklists and Routines invoke **Requests**, not Tasks directly:

1. Checklist/Routine triggers a Request
2. The Hub Application (Scenario) processes the Request
3. The Hub Application creates Tasks (if any) per its own assignment policy
4. Task assignment follows the application's rules, not the Checklist/Routine ownership

**Routine ownership ≠ Task ownership.** However, a common use case for Routines is initiating work that the routine's assignee will likely handle — but this is determined by the Hub Application's assignment policy, not by the Routine itself.

---

## Routine Types

### Assigned Routine

Created by a **Supervisor** and assigned to a specific Agent:

```yaml
routine:
  id: "morning-triage-routine"
  name: "Morning Triage Routine"
  type: assigned
  
  assigned_by: "supervisor-jane"
  assigned_to: "agent-john"
  
  schedule:
    type: daily
    cron_expression: "0 8 * * 1-5"  # 08:00 Mon-Fri
  
  items:
    - name: "Review overnight alerts"
      scenario_id: "alert-review"
    - name: "Check pending escalations"
      scenario_id: "escalation-check"
    - name: "Update daily log"
      scenario_id: "daily-log-update"
```

### Self-Created Routine

Created by an **Agent** for themselves:

```yaml
routine:
  id: "my-eod-routine"
  name: "My End-of-Day Routine"
  type: self_created
  
  created_by: "agent-john"
  assigned_to: "agent-john"  # Same person
  
  schedule:
    type: daily
    cron_expression: "0 17 * * 1-5"  # 17:00 Mon-Fri
  
  items:
    - name: "Complete pending tasks"
      scenario_id: "task-completion-check"
    - name: "Document blockers"
      scenario_id: "blocker-documentation"
    - name: "Prepare handoff notes"
      scenario_id: "handoff-prep"
```

---

## Routine Structure

```
┌─────────────────────────────────────────────────────────────────┐
│                         ROUTINE                                  │
│                   (Agent: john.doe)                              │
│                                                                  │
│  Name: "Morning Triage Routine"                                  │
│  Schedule: Daily at 08:00 (Mon-Fri)                             │
│  Type: Assigned (by: supervisor-jane)                           │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                    ROUTINE ITEMS                            ││
│  │                                                             ││
│  │  ☐ Review overnight alerts                                  ││
│  │  ☐ Check pending escalations                                ││
│  │  ☐ Update daily log                                         ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  Status: [1/3 Complete] [1 In Progress] [1 Pending]             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Routine Definition Schema

```yaml
routine:
  # Identity
  id: string
  name: string
  description: string
  workbench_id: string
  
  # Type
  type: enum                    # assigned | self_created
  
  # Ownership
  created_by: string            # Supervisor or Agent
  assigned_to: string           # Target Agent
  
  # Schedule (Kale configuration)
  schedule:
    type: enum                  # hourly | daily | weekly | monthly | cron
    cron_expression: string
    timezone: string
    effective_from: datetime
    effective_until: datetime   # Optional
  
  # Routine Items
  items:
    - id: string
      name: string
      description: string
      
      # What to initiate
      scenario_id: string       # Scenario to invoke
      
      # Priority
      priority: enum            # low | normal | high
      
      # Sequence
      sequence: number
  
  # Status
  status: enum                  # active | paused | archived
```

---

## Routine Execution Flow

```
Kale Scheduler
        │
        │ Time-Signal: "routine/morning-triage/agent-john/2026-01-04T08:00:00Z"
        ▼
┌─────────────────────────────────────────┐
│       Signal Exchange                    │
│                                         │
│  Trigger: routine-trigger               │
│  (agent-scoped trigger)                 │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│       Routine Service                    │
│                                         │
│  1. Load Routine definition             │
│  2. Create Routine Instance             │
│  3. For each item:                      │
│     - Create Request (assigned to agent)│
│     - Track Request ID                  │
│  4. Notify agent of routine activation  │
└────────────────┬────────────────────────┘
                 │
        ┌────────┼────────┬────────┐
        ▼        ▼        ▼        ▼
    Request 1  Request 2  Request 3  ...
    (agent)    (agent)    (agent)
        │        │        │
        ▼        ▼        ▼
    All assigned to the same Agent
```

---

## Agent Experience

### Routine Notification

When a routine is triggered, the agent receives:
- Push notification (if configured)
- Routine appears in "My Routines" dashboard
- Items become available tasks

### Routine Dashboard (Agent View)

```
┌─────────────────────────────────────────────────────────────────┐
│  MY ROUTINES                                        Today       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ⏰ Morning Triage Routine              08:00     [In Progress] │
│     ├── ✅ Review overnight alerts       (completed 08:15)      │
│     ├── 🔄 Check pending escalations     (in progress)          │
│     └── ⬜ Update daily log              (pending)              │
│                                                                  │
│  ⏰ End-of-Day Routine                  17:00     [Upcoming]    │
│     ├── ⬜ Complete pending tasks                               │
│     ├── ⬜ Document blockers                                    │
│     └── ⬜ Prepare handoff notes                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Who Can Do What

| Persona | Assigned Routines | Self-Created Routines |
|---------|-------------------|----------------------|
| **Supervisor** | Create, assign, modify, view all | View (if shared) |
| **Agent** | Complete, view own | Create, modify, complete, archive |

---

## Relationship to Checklist Service

The Routine Service shares infrastructure with the Checklist Service:

| Component | Shared? |
|-----------|---------|
| **Kale Integration** | Yes — same scheduling mechanism |
| **Signal Exchange** | Yes — same trigger/request flow |
| **Instance Tracking** | Similar — routine instances vs checklist instances |
| **Aggregation** | Yes — same status aggregation logic |
| **Visualization** | Different — agent view vs workbench view |

> Implementation note: Routines may be implemented as a specialized form of Checklist with `scope: agent` and `assigned_to: single_agent`.

---

## Examples

### Supervisor-Assigned Routine

```yaml
routine:
  id: "new-hire-daily"
  name: "New Hire Daily Routine"
  type: assigned
  assigned_by: "supervisor-mary"
  assigned_to: "agent-newcomer"
  
  schedule:
    type: daily
    cron_expression: "0 9 * * 1-5"
  
  items:
    - name: "Review training materials"
      scenario_id: "training-review"
    - name: "Shadow senior agent"
      scenario_id: "shadow-session"
    - name: "Complete practice cases"
      scenario_id: "practice-cases"
    - name: "End-of-day debrief"
      scenario_id: "eod-debrief"
```

### Agent Self-Created Routine

```yaml
routine:
  id: "my-weekly-prep"
  name: "Monday Prep Routine"
  type: self_created
  created_by: "agent-experienced"
  assigned_to: "agent-experienced"
  
  schedule:
    type: weekly
    cron_expression: "0 8 * * 1"  # Monday 08:00
  
  items:
    - name: "Review last week's metrics"
      scenario_id: "metrics-review"
    - name: "Plan priority cases"
      scenario_id: "case-planning"
    - name: "Check upcoming deadlines"
      scenario_id: "deadline-check"
```

---

## Related Documentation

- [Hub Native Utilities](./README.md) — Overview
- [Checklist Service](./checklist-service.md) — Workbench-scoped checklists
- [Kale Scheduler](../signal-providers/kale-scheduler.md) — Time-based signals
- [Task Management](../task-management/README.md) — Task assignment

---

*TODO: Detailed design — Routine sharing, templates, completion tracking, supervisor oversight*

