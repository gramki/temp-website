# Scenario Schema

This document specifies the canonical YAML schema for Scenario definitions in Foundry.

**This is the single source of truth for Scenario schema.** Other modules reference this document for the authoritative schema definition.

## Overview

A Scenario defines a unit of work that a Workspace can execute. Scenarios are stored in Work Catalog repositories at various levels (Platform, Foundry, Workshop, Workbench, User) and synced to the Metadata Service.

Scenarios have two scopes:
- **`workspace-ingress`** — External contract for the Workspace; invocable by Orchestrator via OI Workflows
- **`workspace-internal`** — Internal implementation detail; only invocable by Tasks within a Work Order

## Schema Version

```yaml
apiVersion: foundry/v1
kind: Scenario
```

## Full Schema

```yaml
apiVersion: foundry/v1
kind: Scenario
metadata:
  name: <scenario-name>              # Required: unique within workspace
  workspace: <workspace-type>        # Required: development, qa, etc.
  scope: <scope>                     # Required: workspace-ingress | workspace-internal
  version: <version-string>          # Optional: for tracking changes
  labels:                            # Optional: for filtering/organization
    track: build
    category: implementation
spec:
  description: <description>         # Required: human-readable description
  
  triggers:                          # Required: how scenario is invoked
    - manual                         # User-initiated
    - orchestrator: <event>          # Orchestrator workflow event (ingress only)
    - task: <task-pattern>           # Task invocation (internal only)
    - schedule: <cron>               # Time-based (future)
  
  inputs:                            # Optional: required inputs
    - name: <input-name>
      type: <type>                   # reference, string, number, boolean
      required: <boolean>
      description: <description>
  
  outputs:                           # Optional: expected outputs
    - name: <output-name>
      type: <type>
      description: <description>
  
  tasks:                             # Required: work to be done
    - name: <task-name>
      type: <agent|human>
      description: <description>
      skills:                        # For agent tasks
        - <skill-reference>
      dependencies:                  # Optional: task dependencies
        - <task-name>
      inputs:                        # Task-specific inputs
        - <input-mapping>
      outputs:                       # Task-specific outputs
        - <output-mapping>
  
  swarms:                            # Optional: referenced Swarms
    - <swarm-name>
  
  coordinator_agent:                 # Required if swarms specified
    ref: <swarm>/<agent>             # Always explicit: {swarm}/{trained-agent}
  
  guardrails:                        # Optional: execution constraints
    max_duration: <duration>
    max_cost: <amount>
    require_human_review: <boolean>
  
  success_criteria:                  # Optional: completion criteria
    - <criterion>
```

## Field Reference

### metadata

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Unique scenario identifier within workspace |
| `workspace` | string | Yes | Workspace type (development, qa, etc.) |
| `scope` | string | Yes | `workspace-ingress` or `workspace-internal` |
| `version` | string | No | Version for change tracking |
| `labels` | map | No | Key-value labels for filtering |

### metadata.scope

The `scope` field determines the scenario's visibility and invocation contract:

| Scope | Description | Invocable By | Use Case |
|-------|-------------|--------------|----------|
| `workspace-ingress` | External contract for the Workspace | Orchestrator (via OI Workflow), Manual trigger | Primary work types the Workspace accepts |
| `workspace-internal` | Internal implementation detail | Tasks within a Work Order (via Skills using Jira MCP) | Sub-work, helper scenarios, internal decomposition |

**`workspace-ingress`** scenarios:
- Form the public interface of a Workspace
- Referenced in OI Workflows by the `create-work-order` action
- Visible in "Available Scenarios" when browsing Work Catalogs
- Subject to stricter validation (OI→Scenario linkage checks)

**`workspace-internal`** scenarios:
- Not visible as Workspace contract
- Invoked programmatically by Tasks when they need to create sub-work
- Useful for breaking down complex work without exposing implementation details
- Can only be invoked from within an existing Work Order in the same Workspace

Example pattern:

```
OI Workflow creates WO → Scenario: implement-feature (workspace-ingress)
  └── Task uses Jira MCP to create sub-WO → Scenario: write-unit-tests (workspace-internal)
```

### spec.triggers

Triggers define how a scenario is invoked:

| Trigger Type | Format | Scope Restriction | Description |
|--------------|--------|-------------------|-------------|
| `manual` | `- manual` | Both | User can invoke from IDE or console |
| `orchestrator` | `- orchestrator: <event>` | `workspace-ingress` only | Workflow event triggers scenario |
| `task` | `- task: <pattern>` | `workspace-internal` only | Task can invoke via Jira MCP |
| `schedule` | `- schedule: "0 9 * * *"` | Both | Cron-based scheduling (future) |

Orchestrator events (for `workspace-ingress` scenarios):
- `psd-approved` — Product Specification approved
- `code-merged` — Code merged to main
- `tests-passed` — Test suite passed
- Custom events defined in workflow YAML

Task patterns (for `workspace-internal` scenarios):
- `*` — Any task can invoke
- `code-implementation:*` — Tasks using code-implementation skill
- `test-*` — Tasks matching pattern

### spec.inputs

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Input identifier |
| `type` | string | Yes | `reference`, `string`, `number`, `boolean` |
| `required` | boolean | No | Default: false |
| `description` | string | No | Human-readable description |

Reference types:
- `psdRef` — Reference to Product Specification Document
- `designRef` — Reference to design assets
- `codeRef` — Reference to code repository/branch
- `testRef` — Reference to test suite
- `woRef` — Reference to parent Work Order (for internal scenarios)

### spec.tasks

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Task identifier |
| `type` | string | Yes | `agent` or `human` |
| `description` | string | No | What the task does |
| `skills` | array | For agent | Skills required |
| `dependencies` | array | No | Tasks that must complete first |
| `inputs` | array | No | Input mappings for this task |
| `outputs` | array | No | Output mappings from this task |

### spec.swarms

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `swarms` | array | No | List of Swarm names referenced by this Scenario |

Swarms are organizational units containing Trained Agents. Scenarios reference Swarms rather than individual agents. See [Swarm concept](../../../agent-fabric/concepts/swarm.md).

### spec.coordinator_agent

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ref` | string | If swarms specified | Coordinator agent in `{swarm}/{trained-agent}` notation; always explicit |

The coordinator agent is always explicitly specified — it is not recommended or elected at runtime.

### spec.guardrails

| Field | Type | Description |
|-------|------|-------------|
| `max_duration` | duration | Maximum execution time (e.g., "4h") |
| `max_cost` | string | Maximum cost (e.g., "$50") |
| `require_human_review` | boolean | Require human approval before completion |

## Examples

### workspace-ingress Scenario (Development)

This scenario forms part of the Development Workspace's contract — Orchestrator can invoke it via OI Workflows.

```yaml
apiVersion: foundry/v1
kind: Scenario
metadata:
  name: implement-feature
  workspace: development
  scope: workspace-ingress
  labels:
    track: build
    category: implementation
spec:
  description: "Implement a feature from Product Specification"
  
  triggers:
    - manual
    - orchestrator: psd-approved
  
  inputs:
    - name: psdRef
      type: reference
      required: true
      description: "Reference to the Product Specification Document"
    - name: designRef
      type: reference
      required: false
      description: "Reference to UX design assets"
  
  outputs:
    - name: pullRequest
      type: reference
      description: "PR with implemented feature"
    - name: testCoverage
      type: number
      description: "Test coverage percentage"
  
  tasks:
    - name: analyze-requirements
      type: agent
      description: "Analyze PSD and create implementation plan"
      skills:
        - requirements-analysis
      inputs:
        - scenario.inputs.psdRef
      outputs:
        - implementationPlan
    
    - name: implement-code
      type: agent
      description: "Write code based on implementation plan"
      skills:
        - code-implementation
        - test-writing
      dependencies:
        - analyze-requirements
      outputs:
        - codeChanges
    
    - name: create-pr
      type: agent
      description: "Create pull request with changes"
      skills:
        - pr-authoring
      dependencies:
        - implement-code
      outputs:
        - scenario.outputs.pullRequest
    
    - name: review-pr
      type: human
      description: "Human reviews and approves PR"
      dependencies:
        - create-pr
  
  swarms:
    - build-swarm
    - review-swarm
  
  coordinator_agent:
    ref: build-swarm/feature-implementer
  
  guardrails:
    max_duration: 8h
    max_cost: "$100"
  
  success_criteria:
    - "PR created and approved"
    - "All tests pass"
    - "Coverage >= 80%"
```

### workspace-internal Scenario (Development)

This scenario is internal to the Development Workspace — Tasks can invoke it to create sub-work, but Orchestrator cannot reference it.

```yaml
apiVersion: foundry/v1
kind: Scenario
metadata:
  name: write-unit-tests
  workspace: development
  scope: workspace-internal
  labels:
    category: testing
spec:
  description: "Write unit tests for a specific component"
  
  triggers:
    - task: code-implementation:*    # Tasks using code-implementation skill can invoke
  
  inputs:
    - name: woRef
      type: reference
      required: true
      description: "Reference to parent Work Order"
    - name: componentPath
      type: string
      required: true
      description: "Path to component to test"
  
  outputs:
    - name: testFiles
      type: reference
      description: "Created test files"
    - name: coverage
      type: number
      description: "Coverage percentage for component"
  
  tasks:
    - name: analyze-component
      type: agent
      description: "Analyze component for testable units"
      skills:
        - code-analysis
      inputs:
        - scenario.inputs.componentPath
    
    - name: write-tests
      type: agent
      description: "Write unit tests"
      skills:
        - test-writing
      dependencies:
        - analyze-component
      outputs:
        - scenario.outputs.testFiles
        - scenario.outputs.coverage
  
  guardrails:
    max_duration: 2h
```

### QA Scenario (workspace-ingress)

```yaml
apiVersion: foundry/v1
kind: Scenario
metadata:
  name: execute-test-suite
  workspace: qa
  scope: workspace-ingress
spec:
  description: "Execute test suite against deployed feature"
  
  triggers:
    - orchestrator: feature-deployed
  
  inputs:
    - name: deploymentRef
      type: reference
      required: true
    - name: testSuiteRef
      type: reference
      required: true
  
  outputs:
    - name: testResults
      type: reference
    - name: passRate
      type: number
  
  tasks:
    - name: run-automated-tests
      type: agent
      skills:
        - test-execution
      outputs:
        - automatedResults
    
    - name: run-manual-tests
      type: human
      description: "Execute manual test cases"
      dependencies:
        - run-automated-tests
      outputs:
        - manualResults
    
    - name: compile-results
      type: agent
      skills:
        - test-reporting
      dependencies:
        - run-manual-tests
      outputs:
        - scenario.outputs.testResults
        - scenario.outputs.passRate
  
  guardrails:
    max_duration: 4h
```

## Validation Rules

| Rule | Error |
|------|-------|
| `name` must be unique in workspace | "Duplicate scenario name: {name}" |
| `workspace` must be valid type | "Unknown workspace type: {type}" |
| `scope` must be `workspace-ingress` or `workspace-internal` | "Invalid scope: {scope}" |
| `triggers` must have at least one | "Scenario must have at least one trigger" |
| `orchestrator` trigger only for `workspace-ingress` | "Orchestrator trigger not allowed for workspace-internal scope" |
| `task` trigger only for `workspace-internal` | "Task trigger not allowed for workspace-ingress scope" |
| `tasks` must have at least one | "Scenario must have at least one task" |
| Task `dependencies` must reference existing tasks | "Unknown task dependency: {name}" |
| Agent tasks must have `skills` | "Agent task missing skills: {name}" |
| `swarms` entries must reference visible Swarms | "Unknown Swarm: {name}" |
| `coordinator_agent.ref` must be a valid `{swarm}/{agent}` in a referenced Swarm | "Unknown coordinator agent: {ref}" |
| `coordinator_agent` required if `swarms` specified | "Coordinator agent required when swarms are referenced" |
| No circular dependencies in tasks | "Circular dependency detected: {path}" |

→ See [validation-rules.md](validation-rules.md) for comprehensive validation specification.

## Schema Evolution

When schema changes:

1. Increment `apiVersion` for breaking changes (e.g., `foundry/v2`)
2. Support both versions during migration period
3. Provide migration tooling for existing scenarios

Non-breaking additions (new optional fields) don't require version bump.

## Read Next

- [README.md](README.md) — Work Catalog Management overview
- [oi-workflow-schema.md](oi-workflow-schema.md) — OI Workflow YAML schema
- [resolution-algorithm.md](resolution-algorithm.md) — Hierarchy resolution
- [validation-rules.md](validation-rules.md) — Validation specification
- [../../work-order-runtime/README.md](../../work-order-runtime/README.md) — How WO Runtime executes scenarios
