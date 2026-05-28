# Orchestrator Module Requirements

This document specifies detailed implementation requirements for the Foundry Orchestrator module.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Foundry Orchestrator                              │
│                                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│  │  Webhook    │  │  Workflow   │  │   Action    │  │    REST     │       │
│  │  Listener   │  │   Engine    │  │  Executor   │  │    API      │       │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘       │
│         │                │                │                │               │
│         └────────────────┴────────────────┴────────────────┘               │
│                                   │                                         │
│                          ┌────────┴────────┐                               │
│                          │   State Store   │                               │
│                          │   (Postgres)    │                               │
│                          └─────────────────┘                               │
└─────────────────────────────────────────────────────────────────────────────┘
         │                         │                         │
         ▼                         ▼                         ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│      Jira       │    │  Message Queue  │    │   Management    │
│  (REST + Hooks) │    │ (Kafka/RabbitMQ)│    │ (Metadata Svc)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   WO Runtime    │
                    └─────────────────┘
```

## Core Components

### State Store (Postgres)

Primary state persistence for workflow execution:

| Table | Purpose |
|-------|---------|
| `orchestration_items` | Current state of each orchestration item |
| `workflow_stages` | Current stage and pending handlers per item |
| `work_orders` | WO tracking with labels and groups |
| `wo_groups` | WO Group membership and completion tracking |
| `transition_history` | Audit log of all state transitions |
| `dlq_items` | Dead Letter Queue for failed actions |

Jira is the secondary store for work items; Orchestrator reads AND writes to Jira.

### Webhook Listener

Receives events from Jira via webhooks:

| Event | Trigger |
|-------|---------|
| `issue_created` | New orchestration item or WO created |
| `issue_updated` | Status change, field update |
| `issue_deleted` | Item deleted (rare) |

Webhook handler:
1. Validate webhook signature
2. Parse event payload
3. Match to orchestration item
4. Enqueue for workflow engine

### Workflow Engine

Evaluates workflow definitions and invokes handlers:

1. **Load workflow** — From Workbench > Workshop > Foundry (closest wins)
2. **Match handlers** — Find handlers where `when` matches the event
3. **Execute actions** — Run `then` actions sequentially
4. **Persist state** — Update stage, WO labels, completion status

### Action Executor

Executes workflow actions:

| Action | Implementation |
|--------|----------------|
| `create-work-order` | Jira REST API: create issue |
| `create-work-order-group` | Create multiple WOs atomically, track group |
| `create-user-task` | Jira REST API: create issue (User Task type) |
| `transition-orchestration-item` | Jira REST API: transition issue status |
| `invoke-governance-scenario` | Create governance WO, await verdict |
| `notify` | Send notification (email, Slack, etc.) |

### REST API

Exposes Orchestrator functionality to web console and IDE extensions.

---

## Jira Integration

### Bidirectional Communication

| Direction | Mechanism | Use |
|-----------|-----------|-----|
| Jira → Orchestrator | Webhooks | Event notification |
| Orchestrator → Jira | REST API | Create/update issues |

### Jira Attributes (Custom Fields)

| Attribute | Purpose |
|-----------|---------|
| `foundry-scenario` | Scenario identifier for the WO |
| `foundry-task-workspace` | Workspace Session instance ID |
| `foundry-workbench` | Workbench ID |
| `foundry-orchestration-item` | Parent orchestration item ID |
| `foundry-parent-wo` | Parent WO ID (for delegated tasks) |
| `foundry-wo-label` | WO label for workflow correlation |
| `foundry-wo-group` | WO Group label |

### Issue Types

| Type | Purpose |
|------|---------|
| `Product Intent` | Build Track orchestration item |
| `Release Intent` | Release batching orchestration item |
| `Discovery Case` | Discovery Track orchestration item |
| `Work Order` | Executable work unit |
| `User Task` | Manual intervention task |

---

## Workflow Engine Details

### Workflow Loading

```
1. Check Workbench: workflows/{orchestration-item-type}.yaml
2. If not found, check Workshop: workflows/{orchestration-item-type}.yaml
3. If not found, check Foundry: workflows/{orchestration-item-type}.yaml
4. If not found, error: no workflow defined
```

Workflow authoring permissions:
- **Foundry Admin** — Define Foundry-level workflows
- **Workshop Admin** — Define Workshop-level workflows (override Foundry)
- **Workbench Admin** — Define Workbench-level workflows (override Workshop)

### Event Matching

```python
def matches_handler(event, handler_when):
    if handler_when.event != event.type:
        return False
    for param, expected in handler_when.params.items():
        if event.params.get(param) != expected:
            return False
    return True
```

### Action Execution

Actions execute **sequentially** within a handler:

```python
def execute_handler(handler, context):
    for action in handler.then:
        result = execute_action(action, context)
        if result.failed:
            raise ActionFailedError(action, result)
        context.update(result.outputs)
```

### State Persistence

After each handler execution:
1. Update `workflow_stages` with new stage (if transitioned)
2. Update `work_orders` with new WO labels
3. Insert into `transition_history`
4. Commit transaction

---

## Work Order Groups

### Creation

`create-work-order-group` creates multiple WOs atomically:

```yaml
- action: create-work-order-group
  params:
    group-label: dev-and-qa-ready
    work-orders:
      - wo-label: dev-wo
        workspace: development
        scenario: implement-product-specification
      - wo-label: qa-plan-wo
        workspace: qa
        scenario: prepare-test-suite-for-product-specification
```

Implementation:
1. Create all WOs in single Jira batch request
2. Record group membership in `wo_groups` table
3. Set `foundry-wo-group` attribute on each WO

### Completion Tracking

```python
def on_wo_completed(wo):
    group = get_wo_group(wo)
    if group is None:
        # Individual WO, fire work-order-completed
        fire_event('work-order-completed', wo_label=wo.label)
    else:
        # Update group completion status
        update_group_completion(group, wo)
        if all_completed(group):
            fire_event('work-order-group-completed', group_label=group.label)
```

### Group Completion Status

| Status | Meaning |
|--------|---------|
| `completed` | All WOs completed successfully |
| `partial` | Some completed, some failed/abandoned |
| `failed` | All WOs failed |

---

## Error Handling

### Retry Policy

| Failure Type | Retry Strategy |
|--------------|----------------|
| Jira API timeout | Exponential backoff: 1s, 2s, 4s, 8s, 16s |
| Jira API 5xx | Exponential backoff with jitter |
| Jira API 4xx | No retry (client error) |
| Message queue failure | Retry with backoff |
| Database failure | Retry with backoff |

### Dead Letter Queue (DLQ)

After retries exhausted:

```python
def handle_action_failure(action, error, context):
    dlq_item = {
        'orchestration_item': context.item_id,
        'action': action,
        'error': str(error),
        'context': context.snapshot(),
        'created_at': now(),
        'status': 'pending'
    }
    insert_dlq(dlq_item)
    notify_admins(dlq_item)
```

DLQ items are resolved via admin console:
- **Retry** — Re-execute the action
- **Skip** — Mark as skipped, continue workflow
- **Abort** — Abort the orchestration item

---

## Timeout / SLA Management

### Timeout Configuration

Defaults cascade: Foundry > Workshop > Workbench > Per-stage

```yaml
# Foundry-level defaults
timeouts:
  default: 7d
  warning: 5d

# Per-stage override in workflow
stages:
  - name: in-development
    timeout: 14d
    warning: 10d
    handlers:
      - when:
          event: work-order-timeout
          params:
            wo-label: dev-wo
        then:
          - action: notify
            params:
              channel: workbench-managers
              template: wo-stalled
```

### Timeout Processing

Background job runs periodically:

```python
def check_timeouts():
    for wo in get_active_work_orders():
        if wo.age > wo.timeout:
            fire_event('work-order-timeout', wo_label=wo.label)
        elif wo.age > wo.warning and not wo.warning_sent:
            send_warning(wo)
            mark_warning_sent(wo)
```

---

## Governance Integration

### Invoking Governance

```yaml
- action: invoke-governance-scenario
  params:
    scenario: product-specification-review
    on-reject: soft-block  # or: hard-block
```

Implementation:
1. Create governance WO with scenario
2. Wait for governance verdict
3. If `approved` → continue
4. If `rejected` → apply configured behavior

### Block Behavior

| Mode | Behavior |
|------|----------|
| `hard-block` | Transition cannot proceed |
| `soft-block` | Transition requires manual override with justification |

Override recorded in `transition_history` with justification.

---

## Release Intent

Release Intent is a separate orchestration item type:

| Aspect | Detail |
|--------|--------|
| Type | `Release Intent` |
| Owner | Program Manager |
| Contains | List of tagged Product Intents |
| Milestones | `product-specification-development-start`, `development-started`, etc. |

### Milestone Events

When a Release Intent milestone is set:

```python
def on_release_intent_milestone(release_intent, milestone):
    for pi in get_tagged_pis(release_intent):
        if pi.status == 'ready-for-specification':
            fire_event(
                'release-intent-milestone-reached',
                milestone=milestone,
                orchestration_item=pi.id
            )
```

### Milestone Auto-Tracking

| Milestone | Auto-set when |
|-----------|---------------|
| `development-started` | First tagged PI enters Development |
| `development-completed` | All tagged PIs complete Development |
| `qa-started` | First tagged PI enters QA |
| `qa-completed` | All tagged PIs complete QA |
| `product-specification-completed` | All tagged PIs complete Specification |

---

## Authorization

### Workflow Authoring

| Role | Scope | Permissions |
|------|-------|-------------|
| Foundry Admin | Foundry | Create/update Foundry workflows |
| Workshop Admin | Workshop | Create/update Workshop workflows |
| Workbench Admin | Workbench | Create/update Workbench workflows |

### Manual Stage Transitions

| Role | Permission |
|------|------------|
| Workbench Manager | Manually transition orchestration items in their Workbench |
| Program Manager | Manually transition Release Intents and associated PIs |

### API Authentication

| Client | Auth Method |
|--------|-------------|
| Web Console | User JWT token |
| IDE Extension | User JWT token |
| WO Runtime | Service account token |
| Jira Webhooks | Webhook secret signature |

---

## API Specification

### Orchestration Items

```
GET /api/v1/orchestration-items/{id}
Response: { id, type, status, stage, workbench, created_at, updated_at }

GET /api/v1/orchestration-items/{id}/history
Response: [ { timestamp, from_stage, to_stage, trigger, actor } ]

POST /api/v1/orchestration-items/{id}/transition
Body: { target_stage, justification }
Response: { success, new_stage }

GET /api/v1/orchestration-items?workbench={id}&status={status}
Response: [ { id, type, status, stage, ... } ]
```

### Work Orders

```
GET /api/v1/work-orders?orchestration-item={id}
Response: [ { id, label, scenario, status, assignee, ... } ]

GET /api/v1/work-orders/{id}
Response: { id, label, scenario, status, assignee, group, parent_wo, ... }
```

### Workflows

```
GET /api/v1/workflows/{type}?workbench={id}
Response: { effective_workflow, source_level }

POST /api/v1/workflows
Body: { type, level, scope_id, workflow_yaml }
Response: { success, workflow_id }
```

### DLQ

```
GET /api/v1/dlq?workbench={id}
Response: [ { id, orchestration_item, action, error, created_at, status } ]

POST /api/v1/dlq/{id}/retry
Response: { success }

POST /api/v1/dlq/{id}/skip
Body: { justification }
Response: { success }
```

---

## Scalability

### Partitioning

Multiple Orchestrator instances, partitioned by Workbench:

```
Instance 1: Workbenches A, B, C
Instance 2: Workbenches D, E, F
Instance 3: Workbenches G, H, I
```

Partition assignment via consistent hashing on Workbench ID.

### Message Queue Topics

| Topic | Content |
|-------|---------|
| `orchestrator.events.{workbench}` | Inbound events for partition |
| `orchestrator.wo-runtime` | Outbound to WO Runtime |
| `orchestrator.dlq` | Dead letter items |

---

## Observability

### Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `orchestrator_wo_created_total` | Counter | WOs created |
| `orchestrator_wo_completed_total` | Counter | WOs completed (by status) |
| `orchestrator_stage_duration_seconds` | Histogram | Time spent in each stage |
| `orchestrator_dlq_depth` | Gauge | Items in DLQ |
| `orchestrator_webhook_latency_seconds` | Histogram | Webhook processing time |

### Logging

Structured JSON logs with:
- `correlation_id` — Traces across Orchestrator, Jira, WO Runtime
- `orchestration_item_id`
- `work_order_id`
- `action`
- `result`

### Tracing

OpenTelemetry spans for:
- Webhook processing
- Workflow evaluation
- Action execution
- Jira API calls
- Message queue publish

---

## External Dependencies

| Dependency | Integration | Failure Mode |
|------------|-------------|--------------|
| Jira | REST API + Webhooks | Retry with backoff |
| Management (Metadata Service) | REST API | Retry with backoff |
| Message Queue | Kafka/RabbitMQ | Retry with backoff |
| Postgres | Connection pool | Retry with backoff |

---

## Open Implementation Questions

- Exact Jira custom field IDs and project configuration
- Message queue topic naming convention
- Service account provisioning process
- Webhook secret rotation procedure
- Database migration strategy for schema changes
- Monitoring and alerting thresholds

## Read Next

- [orchestration-item-workflow.md](orchestration-item-workflow.md) — Workflow YAML schema
- [sample-pi-workflow.yaml](sample-pi-workflow.yaml) — Complete PI workflow example
- [pi-journey.md](pi-journey.md) — End-to-end PI walkthrough
