# Authoring OI Workflows

This guide covers how to create and edit Orchestration Item (OI) Workflows.

## Audience

OI Workflow authoring is typically performed by:

| Role | Scope |
|------|-------|
| Platform Admins | Platform-default workflows shipped with product |
| Foundry Admins | Organization-wide workflow customizations |
| Workshop Admins | Team-specific workflow overrides (rare) |

Builders and Workbench Managers typically consume OI Workflows rather than author them.

## What is an OI Workflow?

An OI Workflow is a state machine that defines how an Orchestration Item (like a Product Intent) progresses through its lifecycle:

- **Stages** — Named states the OI can be in
- **Events** — Triggers that cause transitions (task completed, milestone reached, timeout)
- **Actions** — What happens at transitions (create Work Orders, invoke governance, notify)

## Workflow Structure

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
    timeout: 14d
    on-enter:
      - action: create-user-task
        params:
          task-label: draft-approval
          title: "Review PI: ${orchestration-item.title}"
          assignee: role:product-owner
    handlers:
      - when:
          event: user-task-completed
          params:
            task-label: draft-approval
        then:
          - action: transition-orchestration-item
            params:
              to-stage: ready-for-specification
```

## Creating an OI Workflow

### File Location

Place workflow files in the Work Catalog at:
```
work-catalog/<track>/<oi-type>/workflow.yaml
```

For example:
- Platform default: `platform-defaults/work-catalog/build/product-intent/workflow.yaml`
- Foundry override: `foundry-{id}/work-catalog/build/product-intent/workflow.yaml`

### Using the IDE

1. Navigate to the OI folder in Work Catalog Explorer
2. Right-click > "New OI Workflow" (or create `workflow.yaml` directly)
3. Use the workflow schema for autocomplete and validation

### Workflow Components

#### Stages

Define the states the OI can be in:

```yaml
stages:
  - name: draft-ready
    timeout: 14d          # Optional: how long before timeout event
    on-enter:             # Optional: actions when entering this stage
      - action: notify
        params:
          channel: product-owners
          template: pi-draft-ready
    handlers:             # Event handlers for this stage
      - when: ...
        then: ...
```

Standard stage names for Product Intent:
- `start` → `draft-ready` → `ready-for-specification` → `in-specification` → `specified` → `in-development` → `in-qa` → `ready-for-release` → `released` → `end`

#### Events

Events trigger handler execution:

| Event | Description | Parameters |
|-------|-------------|------------|
| `orchestration-item-created` | OI was created | — |
| `user-task-completed` | A user task was completed | `task-label` |
| `work-order-completed` | A Work Order finished | `wo-label`, `status` |
| `work-order-group-completed` | All WOs in a group finished | `group-label`, `status` |
| `work-order-timeout` | A Work Order or stage timed out | `wo-label` (optional) |
| `release-intent-milestone-reached` | Release milestone reached | `milestone` |

#### Actions

Actions are executed when events match:

| Action | Description | Parameters |
|--------|-------------|------------|
| `transition-orchestration-item` | Move OI to new stage | `to-stage` |
| `create-work-order` | Create a Work Order | `wo-label`, `workspace`, `scenario`, `assignee`, `priority` |
| `create-work-order-group` | Create parallel Work Orders | `group-label`, `work-orders[]` |
| `create-user-task` | Create a human task | `task-label`, `title`, `description`, `assignee` |
| `invoke-governance-scenario` | Run a governance check | `scenario`, `on-reject` |
| `notify` | Send notification | `channel`, `template` |

### Work Order Creation

Creating a Work Order links the OI to a Scenario:

```yaml
- action: create-work-order
  params:
    wo-label: dev-wo                    # Reference label for handlers
    workspace: development              # Target workspace
    scenario: implement-feature         # Scenario to execute
    assignee: auto                      # 'auto' or specific user/role
    priority: normal                    # low, normal, high, critical
```

The `scenario` must be a `workspace-ingress` scenario in the target workspace.

### Work Order Groups (Parallel Execution)

Execute multiple Work Orders in parallel:

```yaml
- action: create-work-order-group
  params:
    group-label: dev-and-qa-prep
    work-orders:
      - wo-label: dev-wo
        workspace: development
        scenario: implement-product-specification
        priority: normal
      - wo-label: qa-prep-wo
        workspace: qa
        scenario: prepare-test-suite
        priority: normal
```

Handle group completion:

```yaml
handlers:
  - when:
      event: work-order-group-completed
      params:
        group-label: dev-and-qa-prep
        status: completed              # all succeeded
    then:
      - action: transition-orchestration-item
        params:
          to-stage: in-qa

  - when:
      event: work-order-group-completed
      params:
        group-label: dev-and-qa-prep
        status: partial                # some failed
    then:
      - action: create-user-task
        params:
          task-label: group-failure-review
          title: "Some work orders failed"
          assignee: workbench-queue
```

### Governance Gates

Invoke governance scenarios at transitions:

```yaml
- action: invoke-governance-scenario
  params:
    scenario: code-review-gate
    on-reject: soft-block            # or 'hard-block'
```

| Rejection Mode | Behavior |
|----------------|----------|
| `soft-block` | Log warning, allow transition (can be overridden) |
| `hard-block` | Block transition, require resolution |

### Timeout Handling

Set stage timeouts and handle them:

```yaml
- name: in-specification
  timeout: 21d
  handlers:
    - when:
        event: work-order-timeout
        params:
          wo-label: spec-wo
      then:
        - action: notify
          params:
            channel: workbench-managers
            template: wo-stalled
        - action: create-user-task
          params:
            task-label: timeout-escalation
            title: "Specification work stalled"
            assignee: workbench-queue
```

### Variable Substitution

Use OI context in action parameters:

```yaml
- action: create-user-task
  params:
    title: "Review PI: ${orchestration-item.title}"
    description: |
      PI ID: ${orchestration-item.id}
      Author: ${orchestration-item.author}
```

Available variables:
- `${orchestration-item.id}` — OI identifier
- `${orchestration-item.title}` — OI title
- `${orchestration-item.author}` — Who created the OI
- `${orchestration-item.priority}` — OI priority
- `${orchestration-item.stage}` — Current stage name

## Validation

### Real-Time Validation

The IDE validates as you type:

- Schema conformance
- Stage name consistency (transitions reference valid stages)
- Event/action parameter validity
- Scenario references (workspace-ingress scenarios must exist)

### Full Validation

```bash
foundry workflow validate ./workflow.yaml
```

Validates:
- All transition targets exist as stages
- Referenced scenarios exist and are `workspace-ingress`
- No orphan stages (unreachable from start)
- Terminal stage exists (no handlers)

## Best Practices

### Stage Design

- Keep stages coarse-grained — major milestones, not micro-states
- Use descriptive names: `in-specification`, not `state-2`
- Always have `start` and `end` stages
- Consider timeout at each stage

### Event Handling

- Handle both success and failure cases for Work Orders
- Provide timeout handlers for long-running stages
- Use specific `wo-label` in handlers to avoid ambiguity

### Governance Integration

- Place governance gates at key transitions (not every transition)
- Use `soft-block` for advisory checks, `hard-block` for compliance
- Document what each governance scenario checks

### Work Order Design

- Use meaningful `wo-label` names for traceability
- Match `scenario` to workspace capabilities
- Set appropriate `priority` based on OI urgency

## Event transport (Atropos)

Workflow handlers react to **semantic event names** (e.g. `work-order-completed`, `user-task-completed`). At runtime, modules publish these on **Atropos** at tenant-first paths:

```
/{foundry-id}/foundry.{module}.{event-semantic-name}
```

Examples:

| Semantic event | Atropos path (example) | Publisher |
|----------------|------------------------|-----------|
| `orchestration-item-created` | `/foundry-zeta/foundry.orchestrator.orchestration-item-created` | Orchestrator (after Work Repository webhook) |
| `work-order-completed` | `/foundry-zeta/foundry.wo-runtime.work-order-completed` | WO Runtime |
| `user-task-completed` | Internal workflow event (from Jira webhook) | Orchestrator |

Handler `when.event` values use the **semantic name**, not the full Atropos path. Envelope fields (`foundryId`, `workshopId`, `workbenchId`, `correlationId`) are defined in [event-contracts.md](../../../foundry-work-plan/phase-1/event-contracts.md).

## Example: Complete Product Intent Workflow

See [platform-defaults/work-catalog/build/product-intent/workflow.yaml](../platform-defaults/work-catalog/build/product-intent/workflow.yaml) for a complete example demonstrating:

- Full lifecycle from draft to release
- Parallel Work Order groups
- Governance gates at transitions
- Timeout handling and escalation
- QA failure loops with retry

## Next Steps

After creating an OI Workflow:

1. **Validate** — Run full validation before publishing
2. **Test** — Use dry-run mode to simulate transitions
3. **Publish** — Follow the [publishing workflow](publishing-workflow.md)
4. **Monitor** — Watch OI progression in the Orchestration Dashboard

## Related

- [OI Workflow Schema](../../management/platform-developer-guide/work-catalog-management/oi-workflow-schema.md) — canonical YAML schema reference
- [How the Orchestrator Consumes OI Workflows](../../orchestrator/user-guide/orchestration-item-workflow.md) — runtime execution model
- [Work Catalog Resolution Algorithm](../../management/platform-developer-guide/work-catalog-management/resolution-algorithm.md) — hierarchy resolution (Platform → Foundry → Workshop → Workbench → User)
- [Orchestrator Concepts](../../orchestrator/README.md) — module boundaries and architecture

## Troubleshooting

| Symptom | Likely cause | What to do |
|---------|--------------|------------|
| Workflow validation fails | Invalid stage reference or missing required fields | Run `foundry workflow validate` and check error details |
| Stage transition not firing | Handler `when` clause not matching the event | Verify `event` and `params` match the actual event payload |
| Work Order not created | Referenced scenario missing or not `workspace-ingress` | Check scenario exists in effective Work Catalog with correct scope |
| Timeout not firing | Timeout duration not set on stage | Add `timeout: <duration>` to stage definition |

See [troubleshooting.md](troubleshooting.md) for additional common issues.
