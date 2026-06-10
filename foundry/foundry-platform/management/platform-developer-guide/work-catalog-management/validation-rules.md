# Work Catalog Validation Rules

This document specifies the comprehensive validation rules applied to OI Workflows and Scenarios during PR checks (via the Validation module) and sync operations.

## Overview

Validation occurs at two points:
1. **PR Validation** — Before merge, blocking invalid changes
2. **Sync Validation** — During sync to Metadata Service, as a safety net

Both stages apply the same rules; PR validation prevents most issues before they reach sync.

## Validation Layers

```
┌─────────────────────────────────────────────────────────────────────┐
│                      Validation Pipeline                             │
│                                                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │   YAML      │  │   Schema    │  │  Reference  │  │  Semantic   │ │
│  │  Parsing    │──│  Validation │──│  Validation │──│  Validation │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘ │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

| Layer | Purpose | Fails Fast |
|-------|---------|------------|
| YAML Parsing | Syntax correctness | Yes |
| Schema Validation | Structure conformance | Yes |
| Reference Validation | Cross-references exist | No (collects all errors) |
| Semantic Validation | Business logic rules | No (collects all errors) |

---

## OI Workflow Validation Rules

### Schema Rules

| Rule ID | Rule | Severity | Message |
|---------|------|----------|---------|
| OI-001 | `apiVersion` is `foundry/v1` | Error | "Unsupported apiVersion: {value}" |
| OI-002 | `kind` is `OIWorkflow` | Error | "Expected kind: OIWorkflow, got: {value}" |
| OI-003 | `metadata.name` is present and non-empty | Error | "Missing required field: metadata.name" |
| OI-004 | `metadata.orchestrationItem` is valid type | Error | "Unknown orchestration item type: {value}" |
| OI-005 | `spec.stages` is non-empty array | Error | "Workflow must have at least one stage" |
| OI-006 | Stage `name` is unique within workflow | Error | "Duplicate stage name: {name}" |

### Structural Rules

| Rule ID | Rule | Severity | Message |
|---------|------|----------|---------|
| OI-010 | Workflow has `start` stage | Error | "Workflow must have a 'start' stage" |
| OI-011 | Workflow has `end` stage | Error | "Workflow must have an 'end' stage" |
| OI-012 | `transition-orchestration-item.to-stage` references valid stage | Error | "Unknown stage: {stage}" |
| OI-013 | All stages reachable from `start` | Warning | "Unreachable stage: {stage}" |
| OI-014 | `end` stage has no handlers | Warning | "Terminal stage should not have handlers" |
| OI-015 | No handler transition cycles that could loop infinitely | Error | "Potential infinite loop: {path}" |

### Reference Rules

| Rule ID | Rule | Severity | Message |
|---------|------|----------|---------|
| OI-020 | `create-work-order.scenario` exists in effective catalog | Error | "Scenario not found: {scenario}" |
| OI-021 | Referenced scenario has `scope: workspace-ingress` | Error | "Scenario '{scenario}' is workspace-internal, cannot be invoked by Orchestrator" |
| OI-022 | `create-work-order.workspace` matches scenario's workspace | Error | "Workspace mismatch: action specifies {action_ws}, scenario is {scenario_ws}" |
| OI-023 | `invoke-governance-scenario.scenario` exists | Error | "Governance scenario not found: {scenario}" |
| OI-024 | `wo-label` is unique within workflow | Error | "Duplicate wo-label: {label}" |
| OI-025 | `group-label` is unique within workflow | Error | "Duplicate group-label: {label}" |
| OI-026 | `task-label` is unique within workflow | Error | "Duplicate task-label: {label}" |

### Event Rules

| Rule ID | Rule | Severity | Message |
|---------|------|----------|---------|
| OI-030 | `when.event` is recognized event type | Error | "Unknown event type: {event}" |
| OI-031 | Event params match expected params for event type | Warning | "Unexpected param '{param}' for event '{event}'" |
| OI-032 | `work-order-completed.wo-label` references created WO | Warning | "No WO with label '{label}' created in workflow" |

---

## Scenario Validation Rules

### Schema Rules

| Rule ID | Rule | Severity | Message |
|---------|------|----------|---------|
| SC-001 | `apiVersion` is `foundry/v1` | Error | "Unsupported apiVersion: {value}" |
| SC-002 | `kind` is `Scenario` | Error | "Expected kind: Scenario, got: {value}" |
| SC-003 | `metadata.name` is present and non-empty | Error | "Missing required field: metadata.name" |
| SC-004 | `metadata.workspace` is valid workspace type | Error | "Unknown workspace type: {value}" |
| SC-005 | `metadata.scope` is `workspace-ingress` or `workspace-internal` | Error | "Invalid scope: {value}. Must be 'workspace-ingress' or 'workspace-internal'" |
| SC-006 | `spec.description` is present | Error | "Missing required field: spec.description" |
| SC-007 | `spec.triggers` is non-empty array | Error | "Scenario must have at least one trigger" |
| SC-008 | `spec.tasks` is non-empty array | Error | "Scenario must have at least one task" |

### Scope Rules

| Rule ID | Rule | Severity | Message |
|---------|------|----------|---------|
| SC-010 | `workspace-ingress` scenarios can have `orchestrator` trigger | OK | — |
| SC-011 | `workspace-internal` scenarios cannot have `orchestrator` trigger | Error | "Orchestrator trigger not allowed for workspace-internal scope" |
| SC-012 | `workspace-internal` scenarios can have `task` trigger | OK | — |
| SC-013 | `workspace-ingress` scenarios cannot have `task` trigger | Error | "Task trigger not allowed for workspace-ingress scope" |
| SC-014 | `manual` trigger allowed for both scopes | OK | — |

### Task Rules

| Rule ID | Rule | Severity | Message |
|---------|------|----------|---------|
| SC-020 | Task `name` is unique within scenario | Error | "Duplicate task name: {name}" |
| SC-021 | Task `type` is `agent` or `human` | Error | "Unknown task type: {type}" |
| SC-022 | Agent tasks have non-empty `skills` array | Error | "Agent task missing skills: {task}" |
| SC-023 | Task `dependencies` reference existing tasks | Error | "Unknown task dependency: {dep}" |
| SC-024 | No circular dependencies in tasks | Error | "Circular dependency detected: {path}" |
| SC-025 | At least one task has no dependencies (entry point) | Error | "All tasks have dependencies - no entry point" |

### Reference Rules

| Rule ID | Rule | Severity | Message |
|---------|------|----------|---------|
| SC-030 | Skill references exist in Skill Registry | Error | "Unknown skill: {skill}" |
| SC-031 | `trained_agent.ref` exists in Trained Agent registry | Error | "Unknown Trained Agent: {ref}" |
| SC-032 | `trained_agent.ref` has required skills | Warning | "Trained Agent '{ref}' missing skill: {skill}" |
| SC-033 | Input `type: reference` uses valid reference type | Warning | "Unknown reference type: {type}" |

### Guardrail Rules

| Rule ID | Rule | Severity | Message |
|---------|------|----------|---------|
| SC-040 | `guardrails.max_duration` is valid duration | Error | "Invalid duration: {value}" |
| SC-041 | `guardrails.max_cost` is valid cost string | Error | "Invalid cost: {value}" |
| SC-042 | `guardrails.max_duration` > 0 | Warning | "Zero duration may cause immediate timeout" |

---

## Cross-Artifact Validation

When validating a PR with multiple files, additional cross-artifact rules apply:

| Rule ID | Rule | Severity | Message |
|---------|------|----------|---------|
| CA-001 | OI Workflow's scenario references resolve within same PR or existing catalog | Error | "Scenario '{scenario}' not found in PR or catalog" |
| CA-002 | Deleted scenario is not referenced by OI Workflows | Error | "Cannot delete scenario '{scenario}': referenced by workflow '{workflow}'" |
| CA-003 | Renamed scenario has corresponding OI Workflow updates | Warning | "Scenario '{old}' renamed to '{new}' but workflow references not updated" |

---

## Validation Context

Validation requires context to resolve references:

```python
@dataclass
class ValidationContext:
    foundry_id: str
    workshop_id: Optional[str] = None
    workbench_id: Optional[str] = None
    user_id: Optional[str] = None
    
    # For PR validation: files in the same PR
    pr_files: List[ParsedFile] = field(default_factory=list)
    
    # For reference resolution
    effective_catalog: Optional[EffectiveCatalog] = None
```

### Context Building

```python
def build_validation_context(job: ValidationJob) -> ValidationContext:
    """Build validation context for a job."""
    
    # Determine scope from repository
    scope = determine_repo_scope(job.repository)
    
    # Load effective catalog at parent level
    # (e.g., for workbench validation, load workshop-level effective catalog)
    parent_catalog = load_parent_effective_catalog(scope)
    
    # Parse all files in the PR/commit
    pr_files = [parse_file(f) for f in job.changed_files]
    
    return ValidationContext(
        foundry_id=scope.foundry_id,
        workshop_id=scope.workshop_id,
        workbench_id=scope.workbench_id,
        user_id=scope.user_id,
        pr_files=pr_files,
        effective_catalog=parent_catalog
    )
```

---

## Validation API Integration

### Request

```http
POST /api/v1/work-catalog/validate
Content-Type: application/json

{
  "type": "scenario",
  "yaml": "apiVersion: foundry/v1\nkind: Scenario\n...",
  "context": {
    "foundry_id": "acme",
    "workshop_id": "ecommerce",
    "workbench_id": "checkout"
  }
}
```

### Response (with errors)

```json
{
  "valid": false,
  "errors": [
    {
      "rule_id": "SC-005",
      "severity": "error",
      "message": "Invalid scope: external. Must be 'workspace-ingress' or 'workspace-internal'",
      "path": "$.metadata.scope",
      "line": 6,
      "column": 10
    },
    {
      "rule_id": "SC-030",
      "severity": "error",
      "message": "Unknown skill: advanced-coding",
      "path": "$.spec.tasks[0].skills[0]",
      "line": 25
    }
  ],
  "warnings": [
    {
      "rule_id": "SC-042",
      "severity": "warning",
      "message": "Zero duration may cause immediate timeout",
      "path": "$.spec.guardrails.max_duration",
      "line": 40
    }
  ]
}
```

---

## Validation module integration

The Validation module invokes Work Catalog Management validation rules when Work Catalog files change. Results are reported as a GitHub check named `foundry-validation`.

### GitHub Check Integration

When a PR touches Work Catalog paths, the Validation module:

1. Identifies changed files under `work-catalog/**` or `workbenches/*/work-catalog/**`
2. Calls `POST /api/v1/work-catalog/validate` for each artifact
3. Reports results to GitHub as the `foundry-validation` check

### Validation Output Format

```
❌ work-catalog/build/product-intent/development/scenarios/implement-feature.yaml
   Line 6: [SC-005] Invalid scope: external. Must be 'workspace-ingress' or 'workspace-internal'
   Line 25: [SC-030] Unknown skill: advanced-coding

⚠️ work-catalog/build/product-intent/workflow.yaml
   Line 45: [OI-013] Unreachable stage: legacy-approval

✅ work-catalog/build/product-intent/qa/scenarios/execute-test-suite.yaml

Summary: 1 file failed, 1 file with warnings, 1 file passed
```

---

## Error Severity Levels

| Severity | Behavior | Use Case |
|----------|----------|----------|
| Error | Blocks merge/sync | Schema violations, broken references |
| Warning | Allows merge, logged | Best practice violations, suspicious patterns |
| Info | Informational only | Suggestions, deprecation notices |

---

## Custom Validation Rules

Foundries can define custom validation rules via configuration:

```yaml
# foundry-config/validation-rules.yaml
custom_rules:
  - id: CUSTOM-001
    type: scenario
    severity: error
    check: |
      $.spec.guardrails.max_duration <= "4h"
    message: "Scenarios in this Foundry must have max_duration <= 4h"
  
  - id: CUSTOM-002
    type: oi-workflow
    severity: warning
    check: |
      $.spec.stages[*].handlers[?(@.when.event == "work-order-timeout")]
    message: "Consider adding timeout handlers to all stages"
```

---

## Read Next

- [README.md](README.md) — Work Catalog Management overview
- [oi-workflow-schema.md](oi-workflow-schema.md) — OI Workflow schema
- [scenario-schema.md](scenario-schema.md) — Scenario schema
- [sync-mechanism.md](sync-mechanism.md) — Sync and validation flow
