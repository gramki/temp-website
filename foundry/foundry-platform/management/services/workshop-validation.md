# Workshop Validation Service

The Workshop Validation Service validates pull requests against Workshop Definition Repositories and controls what can be merged to the main branch.

## Purpose

- Validate PR content against schemas before merge
- Ensure referential integrity (skills, scenarios, configs)
- Gate merges — only this service can merge to main
- Provide fast feedback to authors on validation errors

## How It Works

```
┌─────────────────┐
│   Workshop Repo │
│      (Git)      │
└────────┬────────┘
         │ PR opened
         ▼
┌─────────────────────────────────────────────────────────────┐
│              Workshop Validation Service                     │
│                                                             │
│  1. Receive GitHub check run trigger                        │
│  2. Fetch PR diff                                           │
│  3. For each changed file:                                  │
│     - Identify file type (workbench.yaml, scenario, etc.)   │
│     - Load appropriate schema                               │
│     - Validate structure                                    │
│     - Validate references                                   │
│  4. Report results as GitHub check                          │
│  5. If all pass, merge PR                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
         │
         │ check status
         ▼
┌─────────────────┐
│   PR Status     │
│  (pass/fail)    │
└─────────────────┘
```

## Validation Rules

### Schema Validation

| File Type | Schema | Required Fields |
|-----------|--------|-----------------|
| `workbench.yaml` | WorkbenchConfig | name, workshop, metadata |
| `workspace.yaml` | WorkspaceConfig | name, workbench |
| `scenarios/*.yaml` | ScenarioConfig | name, workspace, spec.tasks |
| `skills/*/skill.yaml` | SkillConfig | name, version, spec |
| `integrations.yaml` | IntegrationsConfig | (all optional) |
| `team.yaml` | TeamConfig | members |

### Reference Validation

| Reference Type | Validation |
|----------------|------------|
| Skill references in scenarios | Skill folder must exist |
| Workspace references | Workspace folder must exist |
| Workbench references | Workbench must be registered in Foundry |
| External tool IDs | Format validation only (actual validation at runtime) |

### Permission Validation

| Operation | Required Permission |
|-----------|---------------------|
| Modify workbench.yaml | Workbench Admin |
| Modify scenarios | Workspace Admin or Workbench Admin |
| Modify skills | Workspace Admin or Workbench Admin |
| Modify team.yaml | Workbench Admin |

## GitHub Integration

### Check Run Configuration

```yaml
name: foundry-workshop-validation
trigger:
  - pull_request:
      branches: [main]
      paths:
        - 'workbenches/**'
        - 'workspaces/**'
        - '*.yaml'
```

### Merge Control

The Validation Service is the **only entity** with merge permission on Workshop repos:

1. Branch protection rules require the `foundry-workshop-validation` check to pass
2. Direct pushes to main are disabled
3. The Validation Service uses a GitHub App token to perform the merge

This ensures no invalid configuration reaches main.

## Error Handling

### Validation Errors

Errors are reported as GitHub check annotations:

```
❌ workbenches/checkout/scenarios/create-feature.yaml
   Line 15: Invalid skill reference 'code-review' - skill folder not found
   Line 23: Missing required field 'spec.outputs'
```

### Service Errors

| Error | Handling |
|-------|----------|
| GitHub API unavailable | Retry with exponential backoff |
| Schema not found | Fail validation with clear error |
| Timeout | Fail check, allow re-run |

## API

### Trigger Validation (Internal)

```
POST /api/v1/validation/trigger
Body: { repo, pr_number }
Response: { validation_id, status: "pending" }
```

### Get Validation Status

```
GET /api/v1/validation/{validation_id}
Response: { status, errors[], warnings[] }
```

## Observability

| Metric | Description |
|--------|-------------|
| `validation_requests_total` | Total validation requests |
| `validation_pass_rate` | Percentage of validations that pass |
| `validation_duration_seconds` | Time to complete validation |
| `validation_errors_by_type` | Errors grouped by type |

## Read Next

- [workshop-sync.md](workshop-sync.md) — What happens after merge
- [metadata-service.md](metadata-service.md) — Where validated config ends up
- [../work-catalog-management/scenario-schema.md](../work-catalog-management/scenario-schema.md) — Scenario schema details
