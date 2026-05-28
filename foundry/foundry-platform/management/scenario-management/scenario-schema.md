# Scenario Schema

This document specifies the YAML schema for scenario definitions in Foundry.

## Overview

A Scenario defines a unit of work that a Workspace can execute. Scenarios are stored in Workshop Definition Repositories and synced to the Metadata Service.

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
  name: <scenario-name>           # Required: unique within workspace
  workspace: <workspace-type>     # Required: development, qa, etc.
  version: <version-string>       # Optional: for tracking changes
  labels:                         # Optional: for filtering/organization
    track: build
    category: implementation
spec:
  description: <description>      # Required: human-readable description
  
  triggers:                       # Required: how scenario is invoked
    - manual                      # User-initiated
    - orchestrator: <event>       # Orchestrator workflow event
    - schedule: <cron>            # Time-based (future)
  
  inputs:                         # Optional: required inputs
    - name: <input-name>
      type: <type>                # reference, string, number, boolean
      required: <boolean>
      description: <description>
  
  outputs:                        # Optional: expected outputs
    - name: <output-name>
      type: <type>
      description: <description>
  
  tasks:                          # Required: work to be done
    - name: <task-name>
      type: <agent|human>
      description: <description>
      skills:                     # For agent tasks
        - <skill-reference>
      dependencies:               # Optional: task dependencies
        - <task-name>
      inputs:                     # Task-specific inputs
        - <input-mapping>
      outputs:                    # Task-specific outputs
        - <output-mapping>
  
  skilled_agent:                  # Optional: preferred Skilled Agent
    ref: <skilled-agent-id>
    fallback: auto                # auto | fail | specific-agent
  
  guardrails:                     # Optional: execution constraints
    max_duration: <duration>
    max_cost: <amount>
    require_human_review: <boolean>
  
  success_criteria:               # Optional: completion criteria
    - <criterion>
```

## Field Reference

### metadata

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Unique scenario identifier within workspace |
| `workspace` | string | Yes | Workspace type (development, qa, etc.) |
| `version` | string | No | Version for change tracking |
| `labels` | map | No | Key-value labels for filtering |

### spec.triggers

Triggers define how a scenario is invoked:

| Trigger Type | Format | Description |
|--------------|--------|-------------|
| `manual` | `- manual` | User can invoke from IDE or console |
| `orchestrator` | `- orchestrator: <event>` | Workflow event triggers scenario |
| `schedule` | `- schedule: "0 9 * * *"` | Cron-based scheduling (future) |

Orchestrator events:
- `psd-approved` — Product Specification approved
- `code-merged` — Code merged to main
- `tests-passed` — Test suite passed
- Custom events defined in workflow YAML

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

### spec.skilled_agent

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ref` | string | No | Preferred Skilled Agent ID |
| `fallback` | string | No | `auto` (recommend), `fail`, or specific agent ID |

### spec.guardrails

| Field | Type | Description |
|-------|------|-------------|
| `max_duration` | duration | Maximum execution time (e.g., "4h") |
| `max_cost` | string | Maximum cost (e.g., "$50") |
| `require_human_review` | boolean | Require human approval before completion |

## Examples

### Development Scenario

```yaml
apiVersion: foundry/v1
kind: Scenario
metadata:
  name: implement-feature
  workspace: development
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
  
  skilled_agent:
    ref: sa-full-stack-dev
    fallback: auto
  
  guardrails:
    max_duration: 8h
    max_cost: "$100"
  
  success_criteria:
    - "PR created and approved"
    - "All tests pass"
    - "Coverage >= 80%"
```

### QA Scenario

```yaml
apiVersion: foundry/v1
kind: Scenario
metadata:
  name: execute-test-suite
  workspace: qa
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
| `triggers` must have at least one | "Scenario must have at least one trigger" |
| `tasks` must have at least one | "Scenario must have at least one task" |
| Task `dependencies` must reference existing tasks | "Unknown task dependency: {name}" |
| Agent tasks must have `skills` | "Agent task missing skills: {name}" |
| `skilled_agent.ref` must exist if specified | "Unknown Skilled Agent: {ref}" |
| No circular dependencies in tasks | "Circular dependency detected: {path}" |

## Schema Evolution

When schema changes:

1. Increment `apiVersion` for breaking changes (e.g., `foundry/v2`)
2. Support both versions during migration period
3. Provide migration tooling for existing scenarios

Non-breaking additions (new optional fields) don't require version bump.

## Read Next

- [README.md](README.md) — Scenario Management overview
- [../services/workshop-validation.md](../services/workshop-validation.md) — How scenarios are validated
- [../../orchestrator/orchestration-item-workflow.md](../../orchestrator/orchestration-item-workflow.md) — How orchestrator triggers scenarios
