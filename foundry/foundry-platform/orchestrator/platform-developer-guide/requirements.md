# Orchestrator Module Requirements

This document specifies detailed implementation requirements for the Foundry Orchestrator module.

## Key Concepts

This module implements several platform concepts. For definitions, see:

| Concept | Link |
|---------|------|
| Orchestration Item | [../../concepts/orchestration-item.md](../../concepts/orchestration-item.md) |
| Work Order | [../../concepts/work-order.md](../../concepts/work-order.md) |
| Scenario | [../../concepts/scenario.md](../../concepts/scenario.md) |
| Track | [../../concepts/track.md](../../concepts/track.md) |
| Governance | [../../concepts/governance.md](../../concepts/governance.md) |
| Work Catalog | [../../concepts/work-catalog.md](../../concepts/work-catalog.md) |

Module-specific concepts (internals):

| Concept | Link |
|---------|------|
| Workflow Engine | [../concepts/workflow-engine.md](../concepts/workflow-engine.md) |
| Action Executor | [../concepts/action-executor.md](../concepts/action-executor.md) |
| Work Order Group | [../concepts/work-order-group.md](../concepts/work-order-group.md) |
| Gate Enforcement | [../concepts/gate-enforcement.md](../concepts/gate-enforcement.md) |
| Dead Letter Queue | [../concepts/dead-letter-queue.md](../concepts/dead-letter-queue.md) |

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|---------------------------|
| **Track** | Routes orchestration items through Track-specific OI Workflows |
| **Workspace** | Creates Work Orders when items reach Workspaces |
| **Work Order** | Creates WOs via `create-work-order` action; does not execute them |
| **Governance** | Invokes Governance Scenarios at transition gates via `invoke-governance-scenario` |
| **Scenario** | References Scenarios in OI Workflow actions; delegates execution to WO Runtime |

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

**ORC-FR-0001:** The Webhook Listener SHALL validate the webhook signature before processing any event.

**ORC-FR-0002:** The Webhook Listener SHALL parse the event payload and match it to an orchestration item.

**ORC-FR-0003:** The Webhook Listener SHALL enqueue matched events for the Workflow Engine.

### Workflow Engine

Evaluates workflow definitions and invokes handlers:

**ORC-FR-0004:** The Workflow Engine SHALL load workflows using the Work Catalog resolution hierarchy: User (if active) > Workbench > Workshop > Foundry > Platform (closest scope wins). See [resolution algorithm](../../management/platform-developer-guide/work-catalog-management/resolution-algorithm.md).

**ORC-FR-0005:** The Workflow Engine SHALL match handlers where the `when` clause matches the event.

**ORC-FR-0006:** The Workflow Engine SHALL execute `then` actions sequentially within a handler.

**ORC-FR-0007:** The Workflow Engine SHALL persist state (stage, WO labels, completion status) after each handler execution.

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

**ORC-FR-0008:** The Workflow Engine SHALL check for workflows in the Work Catalog resolution order: User (if active), Workbench, Workshop, Foundry, Platform.

**ORC-FR-0009:** The Workflow Engine SHALL return an error if no workflow is defined at any level (including Platform defaults).

```
1. Check Workbench: workflows/{orchestration-item-type}.yaml
2. If not found, check Workshop: workflows/{orchestration-item-type}.yaml
3. If not found, check Foundry: workflows/{orchestration-item-type}.yaml
4. If not found, error: no workflow defined
```

Workflow authoring permissions:

**ORC-FR-0010:** Foundry Admins SHALL be able to define Foundry-level workflows.

**ORC-FR-0011:** Workshop Admins SHALL be able to define Workshop-level workflows that override Foundry workflows.

**ORC-FR-0012:** Workbench Admins SHALL be able to define Workbench-level workflows that override Workshop workflows.

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

**ORC-FR-0013:** After each handler execution, the Orchestrator SHALL update the `workflow_stages` table with the new stage if a transition occurred.

**ORC-FR-0014:** After each handler execution, the Orchestrator SHALL update the `work_orders` table with new WO labels.

**ORC-FR-0015:** After each handler execution, the Orchestrator SHALL insert a record into `transition_history`.

**ORC-FR-0016:** All state persistence operations SHALL be committed as a single transaction.

---

## Work Order Groups

### Creation

**ORC-FR-0017:** The `create-work-order-group` action SHALL create multiple WOs atomically in a single Jira batch request.

**ORC-FR-0018:** The Orchestrator SHALL record group membership in the `wo_groups` table.

**ORC-FR-0019:** The Orchestrator SHALL set the `foundry-wo-group` attribute on each WO in the group.

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

**ORC-FR-0020:** When a WO completes, if it belongs to a group, the Orchestrator SHALL update the group completion status.

**ORC-FR-0021:** The Orchestrator SHALL fire `work-order-group-completed` only when all WOs in the group have completed.

**ORC-FR-0022:** For individual WOs (not in a group), the Orchestrator SHALL fire `work-order-completed` on completion.

| Status | Meaning |
|--------|---------|
| `completed` | All WOs completed successfully |
| `partial` | Some completed, some failed/abandoned |
| `failed` | All WOs failed |

---

## Error Handling

### Retry Policy

**ORC-NFR-0001:** For Jira API timeouts, the Orchestrator SHALL retry with exponential backoff (1s, 2s, 4s, 8s, 16s).

**ORC-NFR-0002:** For Jira API 5xx errors, the Orchestrator SHALL retry with exponential backoff and jitter.

**ORC-FR-0023:** For Jira API 4xx errors, the Orchestrator SHALL NOT retry (client error).

**ORC-NFR-0003:** For message queue and database failures, the Orchestrator SHALL retry with exponential backoff.

| Failure Type | Retry Strategy |
|--------------|----------------|
| Jira API timeout | Exponential backoff: 1s, 2s, 4s, 8s, 16s |
| Jira API 5xx | Exponential backoff with jitter |
| Jira API 4xx | No retry (client error) |
| Message queue failure | Retry with backoff |
| Database failure | Retry with backoff |

### Dead Letter Queue (DLQ)

**ORC-FR-0024:** After retries are exhausted, the Orchestrator SHALL insert the failed action into the DLQ with full context.

**ORC-FR-0025:** The Orchestrator SHALL notify admins when an item enters the DLQ.

**ORC-FR-0026:** The admin console SHALL support Retry, Skip, and Abort operations on DLQ items.

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

---

## Timeout / SLA Management

### Timeout Configuration

**ORC-FR-0027:** Timeout defaults SHALL cascade: Foundry > Workshop > Workbench > Per-stage (closest scope wins).

**ORC-FR-0028:** A background job SHALL periodically check for timed-out Work Orders.

**ORC-FR-0029:** When a WO exceeds its timeout, the Orchestrator SHALL fire `work-order-timeout` event.

**ORC-FR-0030:** When a WO exceeds its warning threshold and no warning has been sent, the Orchestrator SHALL send a warning notification.

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

**ORC-FR-0031:** The `invoke-governance-scenario` action SHALL create a governance WO and wait for the verdict.

**ORC-FR-0032:** On governance approval, the workflow SHALL continue to the next action.

**ORC-FR-0033:** On governance rejection with `hard-block`, the transition SHALL NOT proceed.

**ORC-FR-0034:** On governance rejection with `soft-block`, the transition SHALL require manual override with justification.

**ORC-FR-0035:** Manual overrides SHALL be recorded in `transition_history` with justification.

```yaml
- action: invoke-governance-scenario
  params:
    scenario: product-specification-review
    on-reject: soft-block  # or: hard-block
```

| Mode | Behavior |
|------|----------|
| `hard-block` | Transition cannot proceed |
| `soft-block` | Transition requires manual override with justification |

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

**ORC-FR-0036:** When a Release Intent milestone is set, the Orchestrator SHALL fire `release-intent-milestone-reached` for each tagged PI in `ready-for-specification` status.

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

**ORC-FR-0037:** The Orchestrator SHALL auto-set `development-started` when the first tagged PI enters Development.

**ORC-FR-0038:** The Orchestrator SHALL auto-set `development-completed` when all tagged PIs complete Development.

**ORC-FR-0039:** The Orchestrator SHALL auto-set `qa-started` when the first tagged PI enters QA.

**ORC-FR-0040:** The Orchestrator SHALL auto-set `qa-completed` when all tagged PIs complete QA.

**ORC-FR-0041:** The Orchestrator SHALL auto-set `product-specification-completed` when all tagged PIs complete Specification.

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

**ORC-FR-0042:** Foundry Admins SHALL have permission to create/update Foundry workflows.

**ORC-FR-0043:** Workshop Admins SHALL have permission to create/update Workshop workflows.

**ORC-FR-0044:** Workbench Admins SHALL have permission to create/update Workbench workflows.

| Role | Scope | Permissions |
|------|-------|-------------|
| Foundry Admin | Foundry | Create/update Foundry workflows |
| Workshop Admin | Workshop | Create/update Workshop workflows |
| Workbench Admin | Workbench | Create/update Workbench workflows |

### Manual Stage Transitions

**ORC-FR-0045:** Workbench Managers SHALL be able to manually transition orchestration items in their Workbench.

**ORC-FR-0046:** Program Managers SHALL be able to manually transition Release Intents and associated PIs.

| Role | Permission |
|------|------------|
| Workbench Manager | Manually transition orchestration items in their Workbench |
| Program Manager | Manually transition Release Intents and associated PIs |

### API Authentication

**ORC-NFR-0004:** Web Console and IDE Extension SHALL authenticate via User JWT token.

**ORC-NFR-0005:** WO Runtime SHALL authenticate via Service account token.

**ORC-NFR-0006:** Jira Webhooks SHALL authenticate via Webhook secret signature.

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

**ORC-NFR-0007:** The Orchestrator SHALL support multiple instances partitioned by Workbench.

**ORC-NFR-0008:** Partition assignment SHALL use consistent hashing on Workbench ID.

```
Instance 1: Workbenches A, B, C
Instance 2: Workbenches D, E, F
Instance 3: Workbenches G, H, I
```

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
- [workflow.yaml](..//work-catalogues/platform-defaults/work-catalog/build/product-intent/workflow.yaml) — Complete PI workflow example
- [product-intent-journey.md](product-intent-journey.md) — End-to-end PI walkthrough
