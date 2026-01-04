# Checklist Service

> **Status:** 🔴 Stub — Placeholder for expansion

The Checklist Service provides **scheduled, multi-operation governance utilities** for Workbenches. A Checklist is a special kind of Trigger on a Kale schedule signal, with visualization and analytical capabilities on top.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Schedule and aggregate routine governance/control operations |
| **Nature** | Stateful — tracks aggregated status of initiated requests |
| **Defined by** | Process Architects, Supervisors |
| **Trigger Source** | Kale (Scheduler) — Time-based signals |
| **Operations** | Each item can invoke any Scenario on any Automation Runtime |

---

## What is a Checklist?

From the ontology:

> **Checklist:** A structured representation of routine reviews or checks that Agents are required to perform proactively on a schedule.

Key distinctions:
- A Checklist is **NOT** an Operation type (Procedure/Workflow/Case)
- A Checklist **IS** a special kind of Trigger that:
  - Fires on a Kale schedule
  - Initiates multiple Requests (one per checklist item)
  - Aggregates outcomes for visibility
  - Provides analytics and visualization

---

## Important: Checklists Create Requests, Not Tasks

```
Checklist Item
      │
      ▼
  Request (created by Checklist Service)
      │
      ▼
  Hub Application (Scenario)
      │
      ▼
  Tasks (if any) — created by Hub Application
      │
      ▼
  Assignment — per Hub Application's assignment policy
```

**Checklist ownership ≠ Task ownership.**

- Checklists invoke Requests for their configured Scenarios
- The Hub Application (Procedure, Workflow, Case, etc.) decides whether to create Tasks
- Task assignment follows the Hub Application's assignment policy
- The Checklist aggregates Request outcomes, not Task assignments

---

## Checklist Structure

```
┌─────────────────────────────────────────────────────────────────┐
│                        CHECKLIST                                 │
│                                                                  │
│  Name: "Daily Operations Review"                                 │
│  Schedule: Daily at 09:00 UTC (via Kale)                        │
│  Workbench: payment-operations                                   │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                    CHECKLIST ITEMS                          ││
│  │                                                             ││
│  │  ┌─────────────────────────────────────────────────────┐   ││
│  │  │ Item 1: Cash Position Verification                  │   ││
│  │  │   Scenario: cash-position-check                     │   ││
│  │  │   Runtime: Atlantis (Procedure Application)         │   ││
│  │  └─────────────────────────────────────────────────────┘   ││
│  │                                                             ││
│  │  ┌─────────────────────────────────────────────────────┐   ││
│  │  │ Item 2: Reconciliation Review                       │   ││
│  │  │   Scenario: daily-recon-review                      │   ││
│  │  │   Runtime: Rhea (Workflow Application)              │   ││
│  │  └─────────────────────────────────────────────────────┘   ││
│  │                                                             ││
│  │  ┌─────────────────────────────────────────────────────┐   ││
│  │  │ Item 3: Exception Triage                            │   ││
│  │  │   Scenario: exception-triage                        │   ││
│  │  │   Runtime: Seer (Case Orchestration Agent)          │   ││
│  │  └─────────────────────────────────────────────────────┘   ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  Aggregated Status: [2/3 Complete] [1 In Progress]              │
└─────────────────────────────────────────────────────────────────┘
```

---

## Checklist Definition Schema

```yaml
checklist:
  # Identity
  id: string
  name: string
  description: string
  workbench_id: string
  
  # Schedule (Kale configuration)
  schedule:
    type: enum              # hourly | daily | weekly | monthly | cron
    cron_expression: string # If type is cron
    timezone: string
    effective_from: datetime
    effective_until: datetime  # Optional
  
  # Checklist Items
  items:
    - id: string
      name: string
      description: string
      
      # What to trigger
      scenario_id: string          # Scenario to invoke
      request_type: enum           # service | business | system
      
      # Request context (optional — passed to Hub Application)
      request_context:
        suggested_queue: string    # Hint for task assignment (optional)
        suggested_role: string     # Hint for task assignment (optional)
        parameters: object         # Scenario-specific parameters
      
      # Priority and SLA (for the Request)
      priority: enum               # low | normal | high | critical
      sla_config:
        target_completion: duration
      
      # Order and dependencies
      sequence: number             # Order in checklist
      depends_on: array            # Other item IDs (optional)
  
  # Access Control
  visibility:
    roles: array                   # Roles that can view this checklist
    teams: array                   # Teams that can view
  
  # Ownership
  created_by: string
  owner: string                    # Process Architect or Supervisor
  
  # Status
  status: enum                     # active | paused | archived
```

---

## Checklist Execution Flow

```
Kale Scheduler
        │
        │ Time-Signal: "checklist/daily-ops-review/2026-01-04T09:00:00Z"
        ▼
┌─────────────────────────────────────────┐
│       Signal Exchange                    │
│                                         │
│  Trigger: checklist-trigger             │
│  (special trigger type for checklists)  │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│       Checklist Service                  │
│                                         │
│  1. Load Checklist definition           │
│  2. Create Checklist Instance           │
│  3. For each item:                      │
│     - Create Request via Signal Exchange│
│     - Track Request ID                  │
│  4. Link all Requests to Instance       │
└────────────────┬────────────────────────┘
                 │
        ┌────────┼────────┬────────┐
        ▼        ▼        ▼        ▼
    Request 1  Request 2  Request 3  ...
    (Item 1)   (Item 2)   (Item 3)
        │        │        │
        ▼        ▼        ▼
    Atlantis   Rhea     Seer
    (Procedure)(Workflow)(Case)
        │        │        │
        └────────┼────────┘
                 │
                 ▼ (Request updates via Signal Exchange)
┌─────────────────────────────────────────┐
│       Checklist Service                  │
│                                         │
│  Aggregates status from all Requests    │
│  Updates Checklist Instance status      │
└─────────────────────────────────────────┘
```

---

## Checklist Instance

Each scheduled execution creates a **Checklist Instance**:

```yaml
checklist_instance:
  id: string
  checklist_id: string
  scheduled_time: datetime
  triggered_at: datetime
  
  # Item Instances
  items:
    - item_id: string
      request_id: string        # Created Request
      status: enum              # pending | in_progress | completed | failed | skipped
      started_at: datetime
      completed_at: datetime
      outcome: object           # Request outcome summary
  
  # Aggregated Status
  aggregated_status:
    total_items: number
    completed: number
    in_progress: number
    pending: number
    failed: number
    skipped: number
  
  # Overall Status
  status: enum                  # in_progress | completed | partial | failed
  completed_at: datetime
```

---

## Aggregated Status Logic

| Instance Status | Condition |
|-----------------|-----------|
| **In Progress** | Any item is pending or in_progress |
| **Completed** | All items completed successfully |
| **Partial** | Some items completed, some failed/skipped |
| **Failed** | All items failed |

---

## Visualization & Analytics

The Checklist Service provides dashboards for:

### Checklist Dashboard (Supervisors)

| View | Purpose |
|------|---------|
| **Today's Checklists** | Status of all checklist instances scheduled today |
| **Pending Items** | Items not yet completed across all checklists |
| **Overdue Items** | Items past their SLA target |
| **Completion Rate** | Historical completion rates by checklist |

### Checklist Analytics

| Metric | Description |
|--------|-------------|
| **On-Time Completion %** | Items completed within SLA |
| **Average Completion Time** | By checklist, by item |
| **Failure Rate** | Items that failed or were skipped |
| **Agent Performance** | Completion rates by assigned agent/queue |

---

## Who Can Do What

| Persona | Capabilities |
|---------|--------------|
| **Process Architect** | Create, modify, archive checklists |
| **Supervisor** | Create, modify checklists; view all instances; pause/resume |
| **Agent** | Complete assigned tasks from checklist items |
| **Auditor** | View checklist history and completion records |

---

## Relationship to Other Subsystems

| Subsystem | Relationship |
|-----------|--------------|
| **Kale (Scheduler)** | Generates time signals that trigger checklists |
| **Signal Exchange** | Routes checklist signals; creates Requests for items |
| **Workbench Management** | Checklists are defined within Workbenches |
| **Task Management** | Tasks from checklist items flow through task queues |
| **Automation Runtimes** | Each item can use any runtime (Atlantis, Rhea, Seer, etc.) |

---

## Examples

### Daily Operations Checklist

```yaml
checklist:
  id: "daily-ops-review"
  name: "Daily Operations Review"
  schedule:
    type: daily
    cron_expression: "0 9 * * *"  # 09:00 daily
    timezone: "America/New_York"
  
  items:
    - id: "cash-position"
      name: "Verify Cash Position"
      scenario_id: "cash-position-check"
      assignment:
        queue_id: "treasury-queue"
      priority: high
      sla_config:
        target_completion: "PT2H"  # 2 hours
    
    - id: "recon-review"
      name: "Review Reconciliation Exceptions"
      scenario_id: "daily-recon-review"
      assignment:
        queue_id: "recon-queue"
      priority: normal
      sla_config:
        target_completion: "PT4H"
    
    - id: "exception-triage"
      name: "Triage Overnight Exceptions"
      scenario_id: "exception-triage"
      assignment:
        role_id: "senior-analyst"
      priority: high
      depends_on: ["recon-review"]  # After recon review
```

### Weekly Compliance Checklist

```yaml
checklist:
  id: "weekly-compliance"
  name: "Weekly Compliance Attestation"
  schedule:
    type: weekly
    cron_expression: "0 10 * * 1"  # Monday 10:00
    timezone: "UTC"
  
  items:
    - id: "aml-review"
      name: "AML Alert Review"
      scenario_id: "aml-weekly-review"
    
    - id: "sanctions-check"
      name: "Sanctions List Update Check"
      scenario_id: "sanctions-update-verification"
    
    - id: "attestation"
      name: "Compliance Officer Attestation"
      scenario_id: "compliance-attestation"
      depends_on: ["aml-review", "sanctions-check"]
```

---

## Storage

Checklist definitions and instances are stored in:

| Data | Storage Layer |
|------|---------------|
| **Checklist Definitions** | Tenant Spec (Workbench configuration) |
| **Checklist Instances** | Operations Data (per-workbench) |
| **Request Links** | Operations Data (Request records) |

---

## Related Documentation

- [Hub Native Utilities](./README.md) — Overview
- [Kale Scheduler](../signal-providers/kale-scheduler.md) — Time-based signals
- [Signal Exchange](../signal-exchange/README.md) — Request creation
- [Task Management](../task-management/README.md) — Task assignment
- [Workbench Management](../workbench-management/README.md) — Workbench configuration

---

*TODO: Detailed design — Checklist item dependencies, partial completion handling, missed schedule behavior*

