# Orchestration Item Workflow Guide

This document provides an authoring guide and reference for OI Workflow definitions. For the canonical YAML schema, see [../management/work-catalog-management/oi-workflow-schema.md](../management/work-catalog-management/oi-workflow-schema.md).

## Overview

Each orchestration item type (Product Intent, Release Intent, Discovery Case, etc.) has a workflow that defines:

- **Stages** — Named states the item progresses through
- **Handlers** — Event-driven logic that executes actions
- **Actions** — Operations like creating Work Orders or transitioning stages

Workflows are sourced from the **Work Catalog** with hierarchical resolution: Platform → Foundry → Workshop → Workbench → User. The closest definition wins.

**Audience:** This guide is for platform admins and foundry admins who author or customize OI Workflows. Builders typically interact with workflows indirectly through Work Orders.

**Schema reference:** [../management/work-catalog-management/oi-workflow-schema.md](../management/work-catalog-management/oi-workflow-schema.md)
**Platform defaults:** [../work-catalogues/platform-defaults/](../work-catalogues/platform-defaults/)

## Schema Structure

```yaml
orchestration-item: <type>
version: <version>
stages:
  - name: <stage-name>
    timeout: <duration>  # optional
    on-enter:            # optional
      - <action>
    handlers:
      - when:
          event: <event-type>
          params:
            <param>: <value>
        then:
          - <action>
```

## Top-Level Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `orchestration-item` | string | Yes | Type of orchestration item (e.g., `product-intent`) |
| `version` | string | Yes | Schema version (e.g., `1.0`) |
| `stages` | array | Yes | List of stage definitions |

## Stage Definition

```yaml
stages:
  - name: <stage-name>
    timeout: <duration>
    on-enter:
      - <action>
    handlers:
      - <handler>
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Unique stage identifier |
| `timeout` | duration | No | Override default timeout for this stage |
| `on-enter` | array | No | Actions to execute when entering stage |
| `handlers` | array | No | Event handlers for this stage |

### Special Stages

| Stage | Purpose |
|-------|---------|
| `start` | Initial stage; orchestration item enters here on creation |
| `end` | Terminal stage; orchestration item is complete |

## Handler Definition

```yaml
handlers:
  - when:
      event: <event-type>
      params:
        <param>: <value>
    then:
      - <action>
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `when` | object | Yes | Event matching criteria |
| `then` | array | Yes | Actions to execute when matched |

### When Clause

```yaml
when:
  event: <event-type>
  params:
    <param>: <value>
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `event` | string | Yes | Event type to match |
| `params` | object | No | Additional criteria for matching |

## Event Types

| Event | Description | Params |
|-------|-------------|--------|
| `orchestration-item-created` | Item was created | — |
| `release-intent-milestone-reached` | Release Intent reached a milestone | `milestone` |
| `work-order-completed` | A Work Order completed | `wo-label`, `status` |
| `work-order-group-completed` | All WOs in a group completed | `group-label`, `status` |
| `user-task-completed` | A User Task was completed | `task-label` |
| `work-order-timeout` | A Work Order exceeded its timeout | `wo-label` |
| `governance-completed` | Governance scenario completed | `scenario`, `verdict` |

### Event Parameter Matching

```yaml
when:
  event: work-order-completed
  params:
    wo-label: dev-wo
    status: success
```

Matches only when:
- Event type is `work-order-completed`
- The WO label is `dev-wo`
- The status is `success`

Multiple handlers can match the same event (all execute).

## Action Types

### create-work-order

Creates a Work Order in the target Workspace.

```yaml
- action: create-work-order
  params:
    wo-label: <label>
    workspace: <workspace-type>
    scenario: <scenario-id>
    assignee: <user-selector>  # optional
    priority: <priority>       # optional
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `wo-label` | string | Yes | Unique label within the orchestration item |
| `workspace` | string | Yes | Target workspace type |
| `scenario` | string | Yes | Scenario to execute |
| `assignee` | string | No | User selector (see below) |
| `priority` | string | No | `critical`, `high`, `normal`, `low` |

### create-work-order-group

Creates multiple Work Orders atomically with collective completion tracking.

```yaml
- action: create-work-order-group
  params:
    group-label: <label>
    work-orders:
      - wo-label: <label>
        workspace: <workspace-type>
        scenario: <scenario-id>
      - wo-label: <label>
        workspace: <workspace-type>
        scenario: <scenario-id>
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `group-label` | string | Yes | Unique group label within the orchestration item |
| `work-orders` | array | Yes | List of WOs to create |

### create-user-task

Creates a manual intervention task.

```yaml
- action: create-user-task
  params:
    task-label: <label>
    title: <title>
    description: <description>
    assignee: <user-selector>
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `task-label` | string | Yes | Unique label within the orchestration item |
| `title` | string | Yes | Task title |
| `description` | string | No | Task description |
| `assignee` | string | Yes | User selector |

### transition-orchestration-item

Transitions the orchestration item to a new stage.

```yaml
- action: transition-orchestration-item
  params:
    to-stage: <stage-name>
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `to-stage` | string | Yes | Target stage name |

### invoke-governance-scenario

Invokes a governance scenario and awaits the verdict.

```yaml
- action: invoke-governance-scenario
  params:
    scenario: <governance-scenario-id>
    on-reject: <soft-block|hard-block>
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `scenario` | string | Yes | Governance scenario to invoke |
| `on-reject` | string | Yes | `soft-block` (allows override) or `hard-block` |

### notify

Sends a notification.

```yaml
- action: notify
  params:
    channel: <channel>
    template: <template-id>
    recipients: <recipient-selector>  # optional
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `channel` | string | Yes | Notification channel (e.g., `workbench-managers`, `email`, `slack`) |
| `template` | string | Yes | Notification template ID |
| `recipients` | string | No | Override default recipients |

### transition-release-intent-milestone

Transitions a Release Intent to a milestone.

```yaml
- action: transition-release-intent-milestone
  params:
    milestone: <milestone-name>
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `milestone` | string | Yes | Target milestone |

## Action Execution Order

Actions within a handler execute **sequentially**:

```yaml
then:
  - action: create-work-order      # 1. Executes first
    params: ...
  - action: notify                 # 2. Executes after WO created
    params: ...
  - action: transition-orchestration-item  # 3. Executes last
    params: ...
```

If any action fails, subsequent actions do not execute and the item enters the DLQ.

## Variable Substitution

Actions can reference variables from the orchestration context:

| Variable | Description |
|----------|-------------|
| `${orchestration-item.id}` | Current orchestration item ID |
| `${orchestration-item.title}` | Orchestration item title |
| `${orchestration-item.author}` | Original author |
| `${orchestration-item.workbench}` | Workbench ID |
| `${release-intent.id}` | Associated Release Intent ID |
| `${event.wo-label}` | WO label from the triggering event |
| `${event.status}` | Status from the triggering event |

Example:

```yaml
- action: notify
  params:
    template: wo-completed
    message: "Work Order ${event.wo-label} completed with status ${event.status}"
```

## User Selectors

User selectors determine who receives a WO or task:

| Selector | Description |
|----------|-------------|
| `auto` | Auto-assign based on skills, capacity, affinity |
| `author` | Original orchestration item author |
| `previous-wo-assignee` | Assignee of the previous WO |
| `workbench-queue` | Queue for team pickup |
| `role:<role-name>` | Assign to user with role |

## On-Enter Actions

Actions in `on-enter` execute when the stage is entered (regardless of trigger):

```yaml
stages:
  - name: in-development
    on-enter:
      - action: notify
        params:
          channel: dev-team
          template: dev-started
    handlers:
      - ...
```

## Timeout Handling

### Stage-Level Timeout

```yaml
stages:
  - name: in-development
    timeout: 14d
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
          - action: create-user-task
            params:
              task-label: escalation-task
              title: "Development WO stalled"
              assignee: workbench-queue
```

### Timeout Event

`work-order-timeout` fires when a WO exceeds its timeout. The handler can escalate, reassign, or notify.

## Manual Stage Transitions

Workbench Managers and Program Managers can manually transition stages:

1. Via Web Console: Navigate to orchestration item → Actions → Transition
2. Via API: `POST /api/v1/orchestration-items/{id}/transition`

Manual transitions bypass workflow handlers but are logged in `transition_history`.

## Workflow Hierarchy (Work Catalog Resolution)

OI Workflows are resolved from the Work Catalog hierarchy:

```
Platform Default                    ← work-catalogues/platform-defaults/
└── Foundry Catalog                 ← foundry-{id}/work-catalog/
    └── Workshop Catalog            ← workshop-{id}/work-catalog/
        └── Workbench Catalog       ← workbench settings
            └── User Catalog        ← user-work-catalog-{id}/ (if activated)
```

Resolution order:
1. Check User catalog (if user catalog is activated for the session)
2. Check Workbench-level catalog
3. Check Workshop-level catalog
4. Check Foundry-level catalog
5. Check Platform defaults

Workflows at a lower level **replace** (not merge with) parent workflows.

For full resolution algorithm details, see [../management/work-catalog-management/resolution-algorithm.md](../management/work-catalog-management/resolution-algorithm.md).

## Complete Example

```yaml
orchestration-item: product-intent
version: "1.0"
stages:
  - name: start
    handlers:
      - when:
          event: orchestration-item-created
        then:
          - action: transition-orchestration-item
            params:
              to-stage: draft-ready

  - name: draft-ready
    handlers:
      - when:
          event: user-task-completed
          params:
            task-label: draft-approval
        then:
          - action: transition-orchestration-item
            params:
              to-stage: ready-for-specification
    on-enter:
      - action: create-user-task
        params:
          task-label: draft-approval
          title: "Review and approve PI draft"
          assignee: role:product-owner

  - name: ready-for-specification
    timeout: 30d
    handlers:
      - when:
          event: release-intent-milestone-reached
          params:
            milestone: product-specification-development-start
        then:
          - action: create-work-order
            params:
              wo-label: spec-wo
              workspace: product-specification
              scenario: create-product-specification
          - action: transition-orchestration-item
            params:
              to-stage: in-specification

  - name: in-specification
    handlers:
      - when:
          event: work-order-completed
          params:
            wo-label: spec-wo
            status: success
        then:
          - action: invoke-governance-scenario
            params:
              scenario: product-specification-review
              on-reject: soft-block
          - action: transition-orchestration-item
            params:
              to-stage: specified

  - name: specified
    on-enter:
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
    handlers:
      - when:
          event: work-order-group-completed
          params:
            group-label: dev-and-qa-ready
            status: completed
        then:
          - action: invoke-governance-scenario
            params:
              scenario: test-plan-review
              on-reject: soft-block
          - action: transition-orchestration-item
            params:
              to-stage: in-qa

  - name: in-qa
    on-enter:
      - action: create-work-order
        params:
          wo-label: qa-wo
          workspace: qa
          scenario: test-developed-feature
    handlers:
      - when:
          event: work-order-completed
          params:
            wo-label: qa-wo
            status: success
        then:
          - action: invoke-governance-scenario
            params:
              scenario: test-coverage-review
              on-reject: soft-block
          - action: transition-orchestration-item
            params:
              to-stage: ready-for-release

  - name: ready-for-release
    on-enter:
      - action: create-work-order
        params:
          wo-label: accept-wo
          workspace: release
          scenario: accept-completed-product-intent
    handlers:
      - when:
          event: work-order-completed
          params:
            wo-label: accept-wo
            status: success
        then:
          - action: create-work-order
            params:
              wo-label: release-wo
              workspace: release
              scenario: prepare-customer-release
      - when:
          event: work-order-completed
          params:
            wo-label: release-wo
            status: success
        then:
          - action: invoke-governance-scenario
            params:
              scenario: customer-release-package-review
              on-reject: hard-block
          - action: transition-orchestration-item
            params:
              to-stage: released

  - name: released
    on-enter:
      - action: notify
        params:
          channel: workbench-managers
          template: pi-released
    handlers:
      - when:
          event: orchestration-item-created  # placeholder for any final event
        then:
          - action: transition-orchestration-item
            params:
              to-stage: end

  - name: end
    # Terminal stage - no handlers
```

## Read Next

- [orchestrator-requirements.md](orchestrator-requirements.md) — Orchestrator module requirements
- [workflow.yaml](../work-catalogues/platform-defaults/build/product-intent/workflow.yaml) — Complete PI workflow example
- [pi-journey.md](pi-journey.md) — End-to-end PI walkthrough
