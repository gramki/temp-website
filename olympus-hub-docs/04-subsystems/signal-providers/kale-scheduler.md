# Kale - Scheduler Gateway

Kale is the I/O Gateway for **time-based signals** — scheduled triggers, recurring jobs, and time-driven operations.

## Overview

| Attribute | Value |
|-----------|-------|
| **Signal Type** | Time-based signals |
| **Protocol** | Scheduler (cron-like) |
| **Direction** | Generates signals at scheduled times |
| **Role** | Produces scheduled signals, executes Triggers, creates Requests |

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Periodic Processing** | Daily reconciliation, weekly reports |
| **Maintenance Windows** | Scheduled maintenance tasks |
| **SLA Monitoring** | Periodic SLA compliance checks |
| **Data Refresh** | Scheduled cache invalidation, data sync |
| **Reminder Generation** | Time-based notifications, follow-ups |

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                        KALE                              │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │              SCHEDULE REGISTRY                   │    │
│  │   (Workbench-defined schedules)                 │    │
│  └─────────────────────┬───────────────────────────┘    │
│                        │                                 │
│                        ▼                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │ Time        │  │ Trigger     │  │ Request     │      │
│  │ Evaluator   │→ │ Executor    │→ │ Publisher   │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
│                                                          │
└────────────────────────┬────────────────────────────────┘
                         │ Request
                         ▼
                   OPERATIONS CENTER
```

## Signal Generation

Unlike other I/O Gateways that sense external signals, Kale **generates** signals based on time:

| Signal Type | Description |
|-------------|-------------|
| **Scheduled** | Fixed-time triggers (cron expressions) |
| **Interval** | Recurring at fixed intervals |
| **Delayed** | One-time trigger after delay |
| **Deadline** | Trigger if condition not met by time |

## Trigger Configuration

```yaml
# Example: Daily reconciliation trigger
trigger:
  name: "daily-reconciliation"
  gateway: kale
  
  # Schedule definition
  schedule:
    cron: "0 6 * * *"  # 6 AM daily
    timezone: "America/New_York"
  
  # Context for the Request
  transform:
    request_type: "DailyReconciliation"
    mapping:
      scheduled_time: "$.trigger.scheduled_time"
      actual_time: "$.trigger.actual_time"
      run_id: "$.trigger.run_id"
      business_date: "$.trigger.business_date"
  
  # Target
  target:
    workbench: "finance-operations"
    scenario: "daily-reconciliation"
```

```yaml
# Example: SLA check trigger
trigger:
  name: "sla-compliance-check"
  gateway: kale
  
  # Schedule definition
  schedule:
    interval: "15m"  # Every 15 minutes
  
  # Context for the Request
  transform:
    request_type: "SLAComplianceCheck"
    mapping:
      check_window_start: "$.trigger.previous_run"
      check_window_end: "$.trigger.scheduled_time"
  
  # Target
  target:
    workbench: "service-operations"
    scenario: "sla-monitoring"
```

```yaml
# Example: Deadline trigger (SLA breach warning)
trigger:
  name: "pending-task-reminder"
  gateway: kale
  
  # Deadline-based trigger
  deadline:
    entity_type: "Task"
    condition: "status = 'PENDING'"
    deadline_field: "due_date"
    warning_offset: "-2h"  # 2 hours before due
  
  # Per-entity Request
  transform:
    request_type: "TaskDeadlineWarning"
    mapping:
      task_id: "$.entity.id"
      due_date: "$.entity.due_date"
      assigned_to: "$.entity.assignee"
  
  # Target
  target:
    workbench: "task-management"
    scenario: "deadline-reminder"
```

## Schedule Types

### Cron-based Schedules
Standard cron expressions with timezone support:

```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of week (0 - 6)
│ │ │ │ │
* * * * *
```

### Interval-based Schedules
- `5m` - Every 5 minutes
- `1h` - Every hour
- `1d` - Every day

### Business Calendar Aware
- Skip weekends/holidays
- Business hours only
- Custom calendar support

## Capabilities

### Schedule Management
- Dynamic schedule creation/modification
- Schedule enable/disable
- Manual trigger ("run now")
- Backfill support

### Execution Guarantees
- **At-least-once**: Missed schedules are caught up
- **Distributed**: Leader election for cluster
- **Idempotent**: Same run ID for retries

### Time Handling
- Timezone-aware scheduling
- Daylight saving time handling
- Business date calculation

### Monitoring
- Schedule health dashboard
- Missed execution alerts
- Execution history

## Integration Points

| System | Integration |
|--------|-------------|
| **Quartz** | Enterprise scheduler |
| **Kubernetes CronJob** | K8s native scheduling |
| **AWS EventBridge** | Scheduled rules |
| **Temporal** | Durable workflow scheduling |

## Observability

| Metric | Description |
|--------|-------------|
| `kale.schedules.active` | Active schedules |
| `kale.triggers.fired` | Scheduled triggers executed |
| `kale.triggers.missed` | Missed schedules (caught up) |
| `kale.requests.created` | Requests created |
| `kale.execution.drift` | Actual vs scheduled time drift |

## Related Documentation

- [Hub Architecture - Signals](../../02-system-design/hub-architecture.md#13-signals)
- [Hub Architecture - Triggers](../../02-system-design/hub-architecture.md#14-triggers)
- [Ontology - Signal](../../01-concepts/ontology-reference.md#signal)

---

*Status: 🟡 WIP - Definition phase*

