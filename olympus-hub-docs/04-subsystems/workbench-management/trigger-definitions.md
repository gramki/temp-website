# Trigger Definitions

> **Status:** 🔴 Stub — Placeholder for expansion

Defines how Triggers are configured within Workbenches.

---

## Overview

A **Trigger** binds Signals from Signal Providers to Scenarios:
- Matches signals based on conditions
- Transforms signals to Request format
- Routes to appropriate Scenario
- Defines response transformation for I/O Gateways

---

## Trigger Schema

```yaml
trigger:
  id: string
  name: string
  workbench_id: string
  
  # Signal source
  signal_source:
    provider: string        # atropos | cronus | heracles | dia | kale | custom
    gateway_config: object  # Provider-specific configuration
  
  # Matching conditions
  conditions:
    - field: string         # JSONPath to field in signal
      operator: string      # eq, ne, gt, lt, contains, matches, etc.
      value: any
    - field: string
      operator: string
      value: any
  
  # Transformation (signal → request)
  transformation:
    request_type: string    # ServiceRequest | BusinessRequest | SystemRequest
    mappings:
      - source: string      # JSONPath in signal
        target: string      # Field in request
    enrichments:
      - source: string      # External data source
        fields: array
  
  # Target scenario
  scenario_id: string
  
  # Request behavior
  request_behavior:
    mode: enum              # create_new | update_existing | create_or_update
    correlation_key: string # Field(s) for correlating updates
    idempotency_key: string # Field(s) for deduplication
  
  # Response transformation (for I/O Gateways)
  response:
    enabled: boolean        # Whether to send response
    success:
      template: object      # Success response mapping
    error:
      template: object      # Error response mapping
  
  # Access control
  access:
    auth_required: boolean
    auth_methods: array
    scopes: array
  
  # Metadata
  priority: number          # For multi-match ordering
  status: enum              # active | disabled
```

---

## Condition Operators

| Operator | Description |
|----------|-------------|
| `eq` | Equals |
| `ne` | Not equals |
| `gt` | Greater than |
| `lt` | Less than |
| `gte` | Greater than or equal |
| `lte` | Less than or equal |
| `contains` | String contains |
| `matches` | Regex match |
| `in` | Value in list |
| `exists` | Field exists |

---

## Transformation Mapping

```yaml
mappings:
  - source: "$.event.customer_id"
    target: "customer_id"
  - source: "$.event.transaction.amount"
    target: "disputed_amount"
  - source: "$.headers.X-Correlation-ID"
    target: "correlation_id"
  - source: "'DISPUTE_FILING'"   # Literal value
    target: "request_type"
```

---

## Persona Twin Trigger Types

Persona Twin Scenarios support specialized trigger types for personal delegation:

### Task Assignment Trigger

Triggers when a task is assigned to the delegator:

```yaml
trigger:
  id: "trg-john-task-assignment"
  name: "John's Task Assignment"
  type: task_assignment
  workbench_id: "wb-disputes"
  
  # Task assignment specific configuration
  task_assignment:
    delegator: "user:john.smith@acme.com"  # Watch for tasks assigned to this user
    
    # Optional OPA filter (evaluated before triggering)
    opaFilter: |
      package persona.twin.task_filter
      default allow = false
      allow {
        input.payload.task.priority == "high"
      }
      allow {
        input.payload.task.priority == "critical"
      }
  
  # Target Persona Twin Scenario
  scenario_id: "sc-john-task-assistant"
  
  # Transformation
  transformation:
    request_type: "PersonaTwinTask"
    mappings:
      - source: "$.task.id"
        target: "original_task_id"
      - source: "$.task.assignee"
        target: "delegator"
      - source: "$.task.priority"
        target: "priority"
      - source: "$.task.scenario_id"
        target: "source_scenario"
  
  # Request behavior
  request_behavior:
    mode: create_new
    idempotency_key: "$.task.id"
```

### Platform Notification Trigger

Triggers when a platform notification is sent to the delegator:

```yaml
trigger:
  id: "trg-john-notifications"
  name: "John's Notifications"
  type: platform_notification
  workbench_id: "wb-disputes"
  
  # Platform notification specific configuration
  platform_notification:
    recipient: "user:john.smith@acme.com"
    scope: workbench  # Only workbench-scoped notifications
    
    # Optional OPA filter
    opaFilter: |
      package persona.twin.notification_filter
      default allow = false
      allow {
        input.payload.notification.category == "high_priority"
      }
  
  # Target Persona Twin Scenario
  scenario_id: "sc-john-notification-handler"
  
  # Transformation
  transformation:
    request_type: "PersonaTwinNotification"
    mappings:
      - source: "$.notification.id"
        target: "notification_id"
      - source: "$.notification.category"
        target: "category"
      - source: "$.notification.message"
        target: "message"
```

### Time Schedule Trigger

Triggers on a cron-like schedule via Kale:

```yaml
trigger:
  id: "trg-john-daily-summary"
  name: "John's Daily Summary"
  type: time_schedule
  workbench_id: "wb-disputes"
  
  # Time schedule configuration (uses Kale)
  time_schedule:
    gateway: kale
    schedule:
      cron: "0 17 * * 1-5"  # 5 PM Mon-Fri
      timezone: "America/New_York"
  
  # Target Persona Twin Scenario
  scenario_id: "sc-john-daily-summary"
  
  # Transformation
  transformation:
    request_type: "ScheduledSummary"
    mappings:
      - source: "'daily_summary'"
        target: "summary_type"
      - source: "$.triggered_at"
        target: "timestamp"
```

### OPA Filter Evaluation

Persona Twin triggers support OPA-based filtering similar to COG Sentinel patterns:

```yaml
# OPA Filter Input Structure
input:
  delegator_id: "user:john.smith@acme.com"
  payload:
    task:
      id: string
      assignee: string
      priority: string
      category: string
    # OR
    notification:
      id: string
      recipient: string
      category: string
      scope: string
  timestamp: datetime

# OPA Filter Output
# If allow == true, trigger fires
# If allow == false, signal is ignored for this trigger
```

### Persona Twin Trigger Schema

Extended schema for Persona Twin triggers:

```yaml
personaTwinTrigger:
  id: string
  name: string
  type: enum  # task_assignment | platform_notification | time_schedule
  workbench_id: string
  
  # Type-specific configuration
  task_assignment:  # For type: task_assignment
    delegator: string
    opaFilter: string  # Optional Rego policy
  
  platform_notification:  # For type: platform_notification
    recipient: string
    scope: enum  # workbench | subscription | platform
    opaFilter: string  # Optional Rego policy
  
  time_schedule:  # For type: time_schedule
    gateway: kale
    schedule:
      cron: string
      timezone: string
  
  # Target and transformation
  scenario_id: string  # Must reference Persona Twin Scenario
  transformation:
    request_type: string
    mappings: array
  
  # Request behavior
  request_behavior:
    mode: enum
    idempotency_key: string
```

---

## Related Documentation

- [Workbench Management Overview](./README.md)
- [Scenario Definitions](./scenario-definitions.md)
- [Signal Exchange - Trigger Evaluator](../signal-exchange/trigger-evaluator.md)
- [Kale Scheduler](../signal-providers/kale-scheduler.md)
- [Persona Twins](../../../olympus-seer-docs/seer-design/implementation-concepts/persona-twins.md) — Persona Twin concept documentation

---

*Trigger Definitions describe how triggers are configured, including specialized Persona Twin trigger types for task assignments, platform notifications, and scheduled activities.*

