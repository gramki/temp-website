# OI Workflow Schema

This document specifies the canonical YAML schema for Orchestration Item (OI) Workflows in Foundry.

**This is the single source of truth for OI Workflow schema.** For authoring guidance, see [Authoring OI Workflows](../../../work-catalogues/user-guide/authoring-oi-workflows.md). For runtime execution details, see [How the Orchestrator Consumes OI Workflows](../../../orchestrator/user-guide/orchestration-item-workflow.md).

## Overview

Each Orchestration Item type (Product Intent, Release Intent, Discovery Case, etc.) has a workflow that defines:

- **Stages** — Named states the item progresses through
- **Handlers** — Event-driven logic that executes actions
- **Actions** — Operations like creating Work Orders or transitioning stages

Workflows are defined at Platform, Foundry, Workshop, Workbench, or User level. The closest definition wins (User > Workbench > Workshop > Foundry > Platform). See [resolution-algorithm.md](resolution-algorithm.md).

## Schema Version

```yaml
apiVersion: foundry/v1
kind: OIWorkflow
```

## Full Schema

```yaml
apiVersion: foundry/v1
kind: OIWorkflow
metadata:
  name: <workflow-name>                # Required: unique identifier
  orchestrationItem: <item-type>       # Required: product-intent, discovery-case, etc.
  version: <version-string>            # Optional: for tracking changes
  labels:                              # Optional: for filtering/organization
    track: build
spec:
  stages:
    - name: <stage-name>
      timeout: <duration>              # Optional: override default timeout
      on-enter:                        # Optional: actions on stage entry
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
| `apiVersion` | string | Yes | Schema version (e.g., `foundry/v1`) |
| `kind` | string | Yes | Must be `OIWorkflow` |
| `metadata` | object | Yes | Workflow metadata |
| `spec` | object | Yes | Workflow specification |

## Metadata Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Unique workflow identifier |
| `orchestrationItem` | string | Yes | Type of OI (e.g., `product-intent`, `discovery-case`) |
| `version` | string | No | Version for change tracking |
| `labels` | map | No | Key-value labels for filtering |

### Orchestration Item Types

| Type | Track | Description |
|------|-------|-------------|
| `product-intent` | Build | New product capability to build |
| `discovery-case` | Discovery | Research or exploration initiative |
| `run-case` | Run | Operational task or incident |
| `customer-release-intent` | Win | Customer-facing release |
| `evolve-case` | Evolve | Improvement or modernization |
| `governance-ritual` | Governance | Compliance or audit process |

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
| `start` | Initial stage; OI enters here on creation |
| `end` | Terminal stage; OI is complete |

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

Creates a Work Order in the target Workspace. The `scenario` must reference a `workspace-ingress` Scenario from the effective Work Catalog.

```yaml
- action: create-work-order
  params:
    wo-label: <label>
    workspace: <workspace-type>
    scenario: <scenario-name>          # Must be workspace-ingress scope
    assignee: <user-selector>          # Optional
    priority: <priority>               # Optional
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `wo-label` | string | Yes | Unique label within the OI |
| `workspace` | string | Yes | Target workspace type |
| `scenario` | string | Yes | Scenario to execute (must be `workspace-ingress`) |
| `assignee` | string | No | User selector (see below) |
| `priority` | string | No | `critical`, `high`, `normal`, `low` |

**Validation:** The referenced `scenario` must exist in the effective Work Catalog at the same scope as this workflow and have `scope: workspace-ingress`.

### create-work-order-group

Creates multiple Work Orders atomically with collective completion tracking.

```yaml
- action: create-work-order-group
  params:
    group-label: <label>
    work-orders:
      - wo-label: <label>
        workspace: <workspace-type>
        scenario: <scenario-name>
      - wo-label: <label>
        workspace: <workspace-type>
        scenario: <scenario-name>
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `group-label` | string | Yes | Unique group label within the OI |
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
| `task-label` | string | Yes | Unique label within the OI |
| `title` | string | Yes | Task title |
| `description` | string | No | Task description |
| `assignee` | string | Yes | User selector |

### transition-orchestration-item

Transitions the OI to a new stage.

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
    scenario: <governance-scenario-name>
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
    recipients: <recipient-selector>   # Optional
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
  - action: create-work-order           # 1. Executes first
    params: ...
  - action: notify                      # 2. Executes after WO created
    params: ...
  - action: transition-orchestration-item  # 3. Executes last
    params: ...
```

If any action fails, subsequent actions do not execute and the item enters the DLQ.

## Variable Substitution

Actions can reference variables from the orchestration context:

| Variable | Description |
|----------|-------------|
| `${orchestration-item.id}` | Current OI ID |
| `${orchestration-item.title}` | OI title |
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
| `author` | Original OI author |
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

1. Via Web Console: Navigate to OI → Actions → Transition
2. Via API: `POST /api/v1/orchestration-items/{id}/transition`

Manual transitions bypass workflow handlers but are logged in `transition_history`.

## Validation Rules

| Rule | Description |
|------|-------------|
| Schema conformance | YAML matches `foundry/v1` OIWorkflow schema |
| Stage uniqueness | Stage names are unique within workflow |
| Stage references valid | `to-stage` references existing stage |
| `start` stage exists | Workflow has a `start` stage |
| `end` stage exists | Workflow has an `end` stage |
| Scenario references valid | `create-work-order.scenario` exists in effective catalog with `scope: workspace-ingress` |
| No orphan stages | All stages are reachable from `start` |
| No handler cycles | Handler transitions don't create infinite loops |

→ See [validation-rules.md](validation-rules.md) for comprehensive validation specification.

## Complete Example

```yaml
apiVersion: foundry/v1
kind: OIWorkflow
metadata:
  name: product-intent-workflow
  orchestrationItem: product-intent
  version: "1.0"
  labels:
    track: build
spec:
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
                scenario: prepare-test-suite
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
            wo-label: release-wo
            workspace: release
            scenario: prepare-customer-release
      handlers:
        - when:
            event: work-order-completed
            params:
              wo-label: release-wo
              status: success
          then:
            - action: invoke-governance-scenario
              params:
                scenario: release-package-review
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
            event: user-task-completed
            params:
              task-label: close-pi
          then:
            - action: transition-orchestration-item
              params:
                to-stage: end

    - name: end
      # Terminal stage - no handlers
```

## Read Next

- [README.md](README.md) — Work Catalog Management overview
- [scenario-schema.md](scenario-schema.md) — Scenario YAML schema
- [resolution-algorithm.md](resolution-algorithm.md) — Hierarchy resolution
- [validation-rules.md](validation-rules.md) — Validation specification
- [../../../orchestrator/README.md](../../../orchestrator/README.md) — Orchestrator module (consumer)
- [../../../work-catalogues/platform-defaults/](../../../work-catalogues/platform-defaults/) — Platform default workflows
