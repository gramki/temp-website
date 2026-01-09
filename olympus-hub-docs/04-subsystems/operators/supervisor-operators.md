# Supervisor Operators

> **Status:** 🟡 Draft — Under active development

Supervisor Operators manage **operational configurations** for workbenches, including task queues, supervision settings, and runtime tuning. These operators are used by the **Supervisor** persona.

---

## Overview

| Operator | Specifications Managed |
|----------|------------------------|
| **workbench-supervisor-operator** | Task Queue Specification, Workbench Supervision Specification |

---

## Supervisor Role Context

The Supervisor persona bridges development and operations:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SUPERVISOR RESPONSIBILITIES                       │
│                                                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │  Task Queue Management                                       │   │
│   │  • Configure allocation algorithms                           │   │
│   │  • Define escalation matrices                                │   │
│   │  • Manage agent enrollment                                   │   │
│   │  • Monitor queue health                                      │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │  Workbench Supervision                                       │   │
│   │  • Configure supervision rules                               │   │
│   │  • Set alert thresholds                                      │   │
│   │  • Define shift schedules                                    │   │
│   │  • Configure workload balancing                              │   │
│   └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Workbench Supervisor Operator

The `workbench-supervisor-operator` reconciles operational configurations that supervisors manage on a day-to-day basis.

---

## Specifications

### Task Queue Specification

Defines a task queue with allocation algorithm, escalation matrix, and enrolled agents.

```yaml
apiVersion: hub.olympus.io/v1
kind: TaskQueueSpec
metadata:
  name: dispute-intake-queue
  namespace: acme-bank
  labels:
    workbench: dispute-operations
spec:
  # Identity
  queue:
    name: dispute-intake-queue
    display_name: "Dispute Intake Queue"
    description: "Queue for initial dispute review tasks"
    workbench_ref: dispute-operations

  # Task Types Served
  task_types:
    - initial-review
    - categorization
    - evidence-request

  # Allocation Algorithm
  allocation:
    algorithm: skill_based  # round_robin | least_loaded | affinity_based | skill_based | pull_based
    
    parameters:
      # Skill-based parameters
      skill_weights:
        dispute-resolution: 0.4
        card-network-rules: 0.3
        customer-communication: 0.3
      
      skill_threshold: 0.7  # Minimum skill match score
      
      # Fallback if no skilled agent available
      fallback:
        algorithm: least_loaded
        timeout_minutes: 15

  # Candidate Agents
  candidates:
    # By IAM role
    roles:
      - dispute-analyst
    
    # By user group
    groups:
      - dispute-ops-team
    
    # By workbench role
    workbench_roles:
      - agent
    
    # Explicit users (additions/overrides)
    explicit_users:
      - user_id: jane.smith@acme-bank.com
        priority: high
      - user_id: john.doe@acme-bank.com
        priority: normal

  # Escalation Matrix
  escalation:
    levels:
      - level: 0
        name: "Initial Assignment"
        candidates:
          roles:
            - dispute-analyst
        threshold_minutes: null  # No escalation trigger at level 0
      
      - level: 1
        name: "Senior Analyst Escalation"
        candidates:
          roles:
            - senior-analyst
        threshold_minutes: 120  # Escalate after 2 hours pending
        notification:
          recipients:
            - role: supervisor
          template: escalation_level_1
      
      - level: 2
        name: "Supervisor Escalation"
        candidates:
          workbench_roles:
            - supervisor
        threshold_minutes: 240  # Escalate after 4 hours (cumulative from level 1)
        notification:
          recipients:
            - role: supervisor
            - role: manager
          template: escalation_level_2
          urgency: high

    # Escalation applies to these states
    trigger_states:
      - PENDING
      - ASSIGNED
      - IN_PROGRESS

  # Queue Behavior
  behavior:
    # Assignment timing
    assignment_mode: immediate  # immediate | on_agent_available | pull
    
    # Rebalancing
    rebalancing:
      enabled: true
      interval_minutes: 30
      max_reassignments_per_task: 2
    
    # Agent capacity
    max_tasks_per_agent: 10
    
    # Priority handling
    priority_boost:
      sla_warning: 2    # Boost priority by 2 levels when SLA warning
      sla_critical: 5   # Boost priority by 5 levels when SLA critical
      vip_customer: 3   # Boost for VIP customers

  # Working Hours
  working_hours:
    timezone: "America/New_York"
    schedule:
      monday:
        start: "08:00"
        end: "18:00"
      tuesday:
        start: "08:00"
        end: "18:00"
      wednesday:
        start: "08:00"
        end: "18:00"
      thursday:
        start: "08:00"
        end: "18:00"
      friday:
        start: "08:00"
        end: "17:00"
    
    # After hours handling
    after_hours:
      action: queue  # queue | route_to_ai | route_to_on_call
      on_call_group: dispute-on-call

  # Metrics & Alerting
  metrics:
    track:
      - queue_depth
      - average_wait_time
      - average_handle_time
      - agent_utilization
      - escalation_rate
    
    alerts:
      - metric: queue_depth
        threshold: 50
        action: notify_supervisor
      
      - metric: average_wait_time
        threshold_minutes: 60
        action: notify_supervisor
```

### Special Queue Specifications

#### Subject Task Queue

Tasks assigned to the customer (subject) of the request.

```yaml
apiVersion: hub.olympus.io/v1
kind: TaskQueueSpec
metadata:
  name: customer-action-queue
  namespace: acme-bank
spec:
  queue:
    name: customer-action-queue
    display_name: "Customer Action Queue"
    type: subject  # Special queue type

  task_types:
    - document-upload
    - verification-confirmation
    - additional-information

  # Dynamic resolution
  candidates:
    request_roles:
      - subject  # Resolved to customer per request

  # No escalation within subject queue
  # Escalation happens via separate supervisor task creation

  # Notification to customer
  notifications:
    on_task_created:
      channels:
        - email
        - sms
        - push
      template: customer_action_required
    
    reminder:
      schedule: "0 9 * * *"  # Daily at 9 AM
      max_reminders: 3
      template: customer_action_reminder

  # Timeout handling
  timeout:
    duration_hours: 48
    action: create_supervisor_task
    supervisor_task_template: customer_unresponsive
```

#### Request Originator Queue

Tasks assigned to the originator of the request.

```yaml
apiVersion: hub.olympus.io/v1
kind: TaskQueueSpec
metadata:
  name: originator-followup-queue
  namespace: acme-bank
spec:
  queue:
    name: originator-followup-queue
    display_name: "Originator Follow-up Queue"
    type: originator

  task_types:
    - originator-review
    - completion-confirmation

  candidates:
    request_roles:
      - originator  # Resolved to original agent per request

  escalation:
    levels:
      - level: 0
        candidates:
          request_roles:
            - originator
      
      - level: 1
        candidates:
          workbench_roles:
            - supervisor
        threshold_minutes: 480  # 8 hours
```

#### Supervisor Queue

Tasks specifically for supervisors.

```yaml
apiVersion: hub.olympus.io/v1
kind: TaskQueueSpec
metadata:
  name: supervisor-queue
  namespace: acme-bank
spec:
  queue:
    name: supervisor-queue
    display_name: "Supervisor Queue"
    type: supervisor

  task_types:
    - approval-required
    - escalation-review
    - exception-handling
    - sla-breach-review

  candidates:
    workbench_roles:
      - supervisor

  allocation:
    algorithm: least_loaded
    parameters:
      consider_active_tasks: true

  escalation:
    levels:
      - level: 0
        candidates:
          workbench_roles:
            - supervisor
      
      - level: 1
        candidates:
          workbench_roles:
            - administrator
          explicit_users:
            - department_manager@acme-bank.com
        threshold_minutes: 120
```

---

### Workbench Supervision Specification

Defines supervision rules, alerts, and operational settings for the workbench.

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchSupervisionSpec
metadata:
  name: dispute-operations-supervision
  namespace: acme-bank
  labels:
    workbench: dispute-operations
spec:
  # Workbench Reference
  workbench_ref: dispute-operations

  # Supervision Team
  supervision_team:
    primary_supervisors:
      - user_id: sup1@acme-bank.com
        name: "Sarah Johnson"
        shift: day
      - user_id: sup2@acme-bank.com
        name: "Mike Chen"
        shift: evening
    
    backup_supervisors:
      - user_id: backup-sup@acme-bank.com
        name: "Alex Williams"
    
    escalation_manager:
      - user_id: manager@acme-bank.com
        name: "Pat Taylor"

  # Shift Configuration
  shifts:
    timezone: "America/New_York"
    definitions:
      - name: day
        start: "08:00"
        end: "16:00"
        days:
          - monday
          - tuesday
          - wednesday
          - thursday
          - friday
      
      - name: evening
        start: "16:00"
        end: "00:00"
        days:
          - monday
          - tuesday
          - wednesday
          - thursday
          - friday
      
      - name: weekend
        start: "10:00"
        end: "18:00"
        days:
          - saturday
          - sunday

  # SLA Monitoring
  sla_monitoring:
    overall_targets:
      resolution_time_hours: 240
      first_response_hours: 4
      customer_satisfaction: 4.0
    
    warning_thresholds:
      resolution_time_remaining_hours: 48
      first_response_remaining_minutes: 30
    
    critical_thresholds:
      resolution_time_remaining_hours: 24
      first_response_remaining_minutes: 10
    
    breach_handling:
      notify:
        - supervisor
        - manager
      create_task: sla-breach-review
      log_to_compliance: true

  # Workload Rules
  workload:
    # Agent capacity
    default_max_tasks_per_agent: 15
    
    # Overrides per role
    role_overrides:
      senior-analyst:
        max_tasks: 10  # Fewer but more complex
      trainee:
        max_tasks: 5
    
    # Balancing
    balancing:
      enabled: true
      interval_minutes: 15
      algorithm: equalize_pending_time  # equalize_count | equalize_pending_time | skill_weighted
      
      # Constraints
      constraints:
        max_reassignments_per_hour: 50
        preserve_context: true  # Avoid reassigning tasks agent has started
    
    # Overflow handling
    overflow:
      threshold_queue_depth: 100
      actions:
        - notify_supervisor
        - enable_ai_assistance
        - route_to_backup_team

  # Quality Assurance
  quality_assurance:
    # Sample reviews
    sampling:
      default_rate: 0.10  # 10% of completed tasks
      high_value_rate: 1.0  # 100% for high value
      new_agent_rate: 0.50  # 50% for agents in first 30 days
    
    # Review assignment
    reviewer_assignment:
      type: supervisor  # supervisor | peer | external
      round_robin: true
    
    # Calibration
    calibration_sessions:
      frequency: weekly
      participants:
        - role: supervisor
        - role: senior-analyst

  # Alerting Rules
  alerts:
    # Real-time alerts
    real_time:
      - name: "Queue Depth High"
        condition: "queue_depth > 50"
        severity: warning
        channels:
          - teams
          - email
        recipients:
          - on_duty_supervisor
      
      - name: "SLA Breach Imminent"
        condition: "sla_remaining_hours < 8 AND status != 'completed'"
        severity: critical
        channels:
          - teams
          - sms
        recipients:
          - assignee
          - supervisor
      
      - name: "Agent Inactive"
        condition: "agent_idle_minutes > 30 AND pending_tasks > 0"
        severity: info
        channels:
          - teams
        recipients:
          - agent
          - supervisor
    
    # Periodic alerts
    periodic:
      - name: "Daily Summary"
        schedule: "0 18 * * MON-FRI"
        type: summary
        recipients:
          - supervisor
          - manager
      
      - name: "Weekly Performance Report"
        schedule: "0 9 * * MON"
        type: performance_report
        recipients:
          - supervisor
          - manager
          - director

  # Agent Performance Tracking
  performance_tracking:
    metrics:
      - name: tasks_completed
        aggregation: count
        period: daily
      
      - name: average_handle_time
        aggregation: average
        period: daily
      
      - name: customer_satisfaction
        aggregation: average
        period: weekly
      
      - name: quality_score
        aggregation: average
        period: weekly
    
    goals:
      - metric: tasks_completed
        target: 20
        period: daily
      
      - metric: average_handle_time
        target_minutes: 30
        direction: below
      
      - metric: customer_satisfaction
        target: 4.5
        direction: above
    
    visibility:
      agents_see_own: true
      agents_see_team_aggregate: true
      agents_see_ranking: false  # Privacy consideration

  # AI Agent Supervision
  ai_supervision:
    # Review requirements
    review_policy:
      decisions_over_amount: 1000  # Human review required
      first_n_per_scenario: 10     # Review first 10 of each scenario type
      random_sample_rate: 0.05    # 5% random sampling
    
    # Escalation to human
    human_escalation:
      confidence_threshold: 0.7   # Escalate if AI confidence below 70%
      uncertainty_keywords:
        - "I'm not sure"
        - "This is unusual"
        - "Recommend human review"
    
    # AI performance monitoring
    monitoring:
      track_metrics:
        - accuracy
        - false_positive_rate
        - escalation_rate
        - customer_satisfaction
      
      alert_thresholds:
        accuracy_below: 0.90
        false_positive_above: 0.10
        escalation_rate_above: 0.30

  # Compliance and Audit
  compliance:
    # Mandatory documentation
    require_decision_rationale: true
    require_evidence_before_close: true
    
    # Four-eyes principle
    four_eyes:
      enabled: true
      threshold_amount: 10000
      approver_role: supervisor
    
    # Audit sampling
    audit_sampling:
      rate: 0.02  # 2% for external audit
      criteria:
        - random
        - high_value
        - customer_complaint
```

---

## Reconciliation Behavior

| Specification | Create | Update | Delete |
|---------------|--------|--------|--------|
| TaskQueueSpec | Create queue, configure allocation | Update algorithm, candidates, escalation | Verify no pending tasks, archive |
| WorkbenchSupervisionSpec | Configure supervision settings | Update rules, thresholds | Reset to defaults |

### Validation Rules

1. **Candidate Validation**: Referenced roles, groups, and users must exist in Cipher IAM
2. **Escalation Coherence**: Higher levels must have broader or equal candidate pools
3. **Schedule Validity**: Working hours must not have gaps in coverage (unless intentional)
4. **Alert Uniqueness**: Alert names must be unique within workbench

---

## Supervisor Workflow

```
┌──────────────────────────────────────────────────────────────────────┐
│                      Supervisor Workflow                              │
│                                                                       │
│  1. Receive Scenario Deployment Specification                         │
│     └── From Developer                                                │
│                              │                                        │
│                              ▼                                        │
│  2. Configure Task Queues                                             │
│     └── Allocation, escalation, candidates                            │
│                              │                                        │
│                              ▼                                        │
│  3. Configure Supervision Settings                                    │
│     └── Shifts, alerts, QA, workload                                  │
│                              │                                        │
│                              ▼                                        │
│  4. Commit to Git                                                     │
│     └── Version controlled configuration                              │
│                              │                                        │
│                              ▼                                        │
│  5. Operator Reconciles                                               │
│     └── Task Management updated                                       │
│                              │                                        │
│                              ▼                                        │
│  6. Ongoing Operations                                                │
│     └── Monitor, adjust, optimize                                     │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Runtime Adjustments

Supervisors can make some adjustments at runtime without going through GitOps:

| Adjustment | GitOps Required | Runtime Allowed |
|------------|-----------------|-----------------|
| Add/remove agent from queue | ✅ Preferred | ✅ Temporary |
| Change escalation thresholds | ✅ | ❌ |
| Modify allocation algorithm | ✅ | ❌ |
| Force reassign task | N/A | ✅ |
| Override SLA for single request | N/A | ✅ |
| Enable/disable AI assistance | ✅ Preferred | ✅ Temporary |
| Update shift schedule | ✅ | ❌ |

Runtime adjustments are audited and should be reconciled with GitOps specifications periodically.

---

## Related Documentation

- [Operators Overview](./README.md)
- [Developer Operators](./developer-operators.md) — Automation and Deployment specs
- [Task Management](../task-management/README.md)
- [Task Queues](../task-management/task-queues.md)
- [Task Allocation](../task-management/task-allocation.md)

---

*Supervisor Operators enable declarative configuration of operational settings while supporting necessary runtime flexibility for day-to-day operations.*

