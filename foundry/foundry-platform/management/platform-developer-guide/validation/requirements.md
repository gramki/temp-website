# Validation Module — Requirements

Implementation requirements for the Validation module.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|---------------------------|
| **Workshop** | Validates Workshop definition repos; gates PR merges |
| **Scenario** | Delegates Work Catalog validation (OI Workflows, Scenarios) to Work Catalog Management |
| **Repositories** | Validates Knowledge (Domain, Practices) content in definition repos |

## Functional requirements

### PR validation (definition repos)

**VAL-FR-0001:** The Validation module SHALL validate all changed files in PRs against Foundry and Workshop definition repos.

**VAL-FR-0002:** The Validation module SHALL report results as GitHub check `foundry-validation`.

**VAL-FR-0003:** The Validation module SHALL block merge when validation fails.

**VAL-FR-0004:** The Validation module SHALL perform merge via GitHub App token when validation passes and PR is approved.

**VAL-FR-0005:** The Validation module SHALL support Foundry definition repo (`foundry-{id}/`) in addition to Workshop repos.

### Push validation (user catalog repos)

**VAL-FR-0006:** The Validation module SHALL validate on push to main for `user-work-catalog-{userId}/` repos.

**VAL-FR-0007:** The Validation module SHALL report validation status but NOT block push for user catalog repos.

**VAL-FR-0008:** The Validation module SHALL trigger sync on successful validation.

### Platform release validation

**VAL-FR-0009:** The Validation module SHALL validate all content under `platform-defaults/work-catalog/` before Foundry deployment/upgrade.

**VAL-FR-0010:** The Validation module SHALL block release if platform defaults fail validation.

### Sync validation (safety net)

**VAL-FR-0011:** The Validation module SHALL re-apply validation rules during Sync before Metadata Service write.

**VAL-FR-0012:** The Validation module SHALL abort sync and notify on validation failure.

### Hierarchy-aware Work Catalog validation

**VAL-FR-0013:** The Validation module SHALL load parent effective catalog when validating Work Catalog changes.

**VAL-FR-0014:** The Validation module SHALL resolve OI→Scenario references against PR files plus parent catalog.

**VAL-FR-0015:** The Validation module SHALL validate cross-artifact rules within multi-file PRs.

## Triggers

| Repository type | Git event | Validation mode | Merge gate |
|-----------------|-----------|-----------------|------------|
| `foundry-{id}/` | `pull_request` | Full | Yes |
| `workshop-{id}/` | `pull_request` | Full | Yes |
| `user-work-catalog-{userId}/` | `push` to main | Full | No |
| Platform defaults | Release pipeline | Full | Yes (release) |

### Path filters (PR triggers)

```yaml
paths:
  - 'work-catalog/**'
  - 'workbenches/**'
  - 'workspaces/**'
  - 'domain/**'
  - 'practices/**'
  - 'foundry.yaml'
  - 'workshop.yaml'
  - '*.yaml'
```

## APIs

### Validation orchestrator

```
POST /api/v1/validation/trigger
Body: { repo, pr_number?, commit_sha?, event_type: "pull_request" | "push" }
Response: { validation_id, status: "pending" }
```

```
GET /api/v1/validation/{validation_id}
Response: { status, errors[], warnings[], conclusion: "success" | "failure" }
```

### Work Catalog delegation

Work Catalog validation delegates to Work Catalog Management:

```
POST /api/v1/work-catalog/validate
Body: { type: "oi-workflow" | "scenario", yaml: "...", context: { foundry_id, workshop_id?, workbench_id?, user_id?, pr_files? } }
Response: { valid, errors[], warnings[] }
```

→ [../work-catalog-management/apis.md](../work-catalog-management/apis.md) for full Work Catalog Management API spec

## Permission matrix

**VAL-FR-0016:** Modifying `foundry.yaml` SHALL require Foundry Admin permission.

**VAL-FR-0017:** Modifying `workshop.yaml` and workshop `work-catalog/**` SHALL require Workshop Admin permission.

**VAL-FR-0018:** Modifying `workbench.yaml` and `team.yaml` SHALL require Workbench Manager permission.

**VAL-FR-0019:** Modifying `workbenches/{wb}/work-catalog/**` SHALL require Workbench Manager or Workshop Admin permission.

**VAL-FR-0020:** Modifying `domain/` and `practices/` at Foundry level SHALL require Foundry Admin permission.

**VAL-FR-0021:** Modifying `domain/` and `practices/` at Workshop/Workbench level SHALL require Workshop Admin or Workbench Manager permission.

**VAL-FR-0022:** Pushing to user work catalog repo SHALL require repo owner (user) permission.

| Operation | Required permission |
|-----------|---------------------|
| Modify `foundry.yaml` | Foundry Admin |
| Modify `workshop.yaml`, workshop `work-catalog/**` | Workshop Admin |
| Modify `workbench.yaml`, `team.yaml` | Workbench Manager |
| Modify `workbenches/{wb}/work-catalog/**` | Workbench Manager or Workshop Admin |
| Modify `domain/`, `practices/` at Foundry level | Foundry Admin |
| Modify `domain/`, `practices/` at Workshop/Workbench level | Workshop Admin or Workbench Manager |
| Push to user work catalog repo | Repo owner (user) |

## Observability

| Metric | Type | Description |
|--------|------|-------------|
| `validation_requests_total` | Counter | Total validation requests by repo type |
| `validation_pass_rate` | Gauge | Percentage passing by repo type |
| `validation_duration_seconds` | Histogram | Time to complete validation |
| `validation_errors_by_type` | Counter | Errors grouped by validator and rule ID |

## Error handling

**VAL-NFR-0001:** When GitHub API is unavailable, the Validation module SHALL retry with exponential backoff.

**VAL-FR-0023:** When schema is not found, the Validation module SHALL fail validation with a clear error.

**VAL-FR-0024:** When Work Catalog Management is unavailable, the Validation module SHALL fail validation and NOT merge.

**VAL-NFR-0002:** On timeout, the Validation module SHALL fail the check but allow re-run.

**VAL-FR-0025:** On partial PR failure, the Validation module SHALL report all errors and block merge.

| Error | Handling |
|-------|----------|
| GitHub API unavailable | Retry with exponential backoff |
| Schema not found | Fail validation with clear error |
| Work Catalog Management unavailable | Fail validation; do not merge |
| Timeout | Fail check; allow re-run |
| Partial PR failure | Report all errors; block merge |

## Read Next

- [README.md](README.md) — Module overview and architecture
- [../services/workshop-validation.md](../services/workshop-validation.md) — GitHub integration
- [../work-catalog-management/validation-rules.md](../work-catalog-management/validation-rules.md) — Work Catalog rules
