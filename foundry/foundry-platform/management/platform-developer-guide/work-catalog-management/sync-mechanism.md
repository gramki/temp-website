# Work Catalog Sync Mechanism

This document specifies how Work Catalogs are synced from Git repositories to the Metadata Service registry.

## Overview

Work Catalogs are stored in Git repositories at multiple hierarchy levels. Changes to these repositories trigger sync to the Metadata Service, which serves as the runtime registry for OI Workflows and Scenarios.

```
┌─────────────────┐     webhook      ┌─────────────────┐     upsert      ┌─────────────────┐
│  Work Catalog   │ ───────────────▶ │   Sync Service  │ ───────────────▶│    Metadata     │
│   Repository    │                  │                 │                 │    Service      │
└─────────────────┘                  └─────────────────┘                 └─────────────────┘
       │                                     │                                   │
       │                                     │ validate                          │
       │                                     ▼                                   │
       │                             ┌─────────────────┐                         │
       │                             │  Work Catalog   │                         │
       │                             │   Management    │                         │
       │                             └─────────────────┘                         │
       │                                     │                                   │
       │                                     │ invalidate                        │
       │                                     ▼                                   │
       │                             ┌─────────────────┐                         │
       │                             │     Cache       │◀────────────────────────┘
       │                             │    (Redis)      │     read
       └─────────────────────────────┴─────────────────┘
```

## Repository Types

### Platform Defaults Repository

**Location:** Part of the Foundry codebase (`work-catalogues/platform-defaults/`)

**Sync trigger:** Foundry deployment/upgrade

**Structure:**

```
platform-defaults/
└── work-catalog/
    ├── build/
    │   └── product-intent/
    │       ├── workflow.yaml
    │       └── development/
    │           └── scenarios/
    │               └── implement-feature.yaml
    └── discovery/
        └── discovery-case/
            ├── workflow.yaml
            └── development/
                └── scenarios/
                    └── ...
```

### Foundry Work Catalog (embedded in Foundry Definition Repo)

**Location:** Embedded in Foundry Definition Repository (`foundry-{id}/`)

**Sync trigger:** Push to main branch (webhook)

**Structure:**

```
foundry-acme/
└── work-catalog/
    ├── build/
    │   └── product-intent/
    │       ├── workflow.yaml
    │       └── development/
    │           └── scenarios/
    │               └── implement-feature.yaml
    └── discovery/
        └── discovery-case/
            └── workflow.yaml
```

### Workshop Work Catalog (within Workshop Definition Repo)

**Location:** Workshop Definition Repository (`workshop-{id}/`)

**Sync trigger:** Push to main branch (webhook)

**Structure:**

```
workshop-ecommerce/
├── work-catalog/
│   └── build/
│       └── product-intent/
│           ├── workflow.yaml          # Workshop override
│           └── development/
│               └── scenarios/
│                   └── implement-feature.yaml
└── workbenches/
    └── checkout/
        └── work-catalog/
            └── build/
                └── product-intent/
                    └── development/
                        └── scenarios/
                            └── implement-feature.yaml  # Workbench override
```

### User Work Catalog Repository

**Location:** `user-work-catalog-{userId}/` (GitHub, private)

**Sync trigger:** Push to main branch (webhook) OR manual sync request

**Structure:**

```
user-work-catalog-alice/
└── work-catalog/
    └── build/
        └── product-intent/
            ├── workflow.yaml          # User's experimental workflow
            └── development/
                └── scenarios/
                    └── implement-feature.yaml  # User's experimental scenario
```

## Sync Flow

### Webhook Reception

```python
@app.post("/webhooks/github")
async def handle_github_webhook(request: Request):
    payload = await request.json()
    event_type = request.headers.get("X-GitHub-Event")
    
    if event_type != "push":
        return {"status": "ignored", "reason": "not a push event"}
    
    if payload["ref"] != "refs/heads/main":
        return {"status": "ignored", "reason": "not main branch"}
    
    repo_info = identify_repository(payload["repository"]["full_name"])
    if not repo_info:
        return {"status": "ignored", "reason": "unknown repository"}
    
    # Queue sync job
    sync_job = SyncJob(
        repo_type=repo_info.type,
        repo_id=repo_info.id,
        commit_sha=payload["after"],
        changed_files=extract_changed_files(payload["commits"])
    )
    await job_queue.enqueue(sync_job)
    
    return {"status": "queued", "job_id": sync_job.id}
```

### Sync Job Processing

```python
async def process_sync_job(job: SyncJob):
    """Process a work catalog sync job."""
    
    # 1. Fetch changed files from repository
    files = await fetch_files_from_repo(
        job.repo_id,
        job.commit_sha,
        job.changed_files
    )
    
    # 2. Categorize files
    oi_workflows = [f for f in files if is_oi_workflow(f)]
    scenarios = [f for f in files if is_scenario(f)]
    
    # 3. Validate all artifacts
    validation_results = []
    for workflow in oi_workflows:
        result = await validate_oi_workflow(workflow, job)
        validation_results.append(result)
    
    for scenario in scenarios:
        result = await validate_scenario(scenario, job)
        validation_results.append(result)
    
    # 4. Check for validation failures
    failures = [r for r in validation_results if not r.valid]
    if failures:
        await notify_sync_failure(job, failures)
        raise SyncValidationError(failures)
    
    # 5. Upsert to Metadata Service
    for workflow in oi_workflows:
        await upsert_oi_workflow(workflow, job)
    
    for scenario in scenarios:
        await upsert_scenario(scenario, job)
    
    # 6. Handle deletions
    deleted_files = [f for f in job.changed_files if f.status == "deleted"]
    for deleted in deleted_files:
        await delete_artifact(deleted, job)
    
    # 7. Invalidate caches
    await invalidate_caches(job)
    
    # 8. Emit sync complete event
    await emit_event("catalog.synced", {
        "repo_type": job.repo_type,
        "repo_id": job.repo_id,
        "commit_sha": job.commit_sha,
        "artifacts_synced": len(oi_workflows) + len(scenarios),
        "artifacts_deleted": len(deleted_files)
    })
```

### Metadata Service Upsert

```python
async def upsert_scenario(scenario: ParsedScenario, job: SyncJob):
    """Upsert a scenario to Metadata Service."""
    
    scope = determine_scope(job.repo_type)  # foundry, workshop, workbench, user
    scope_id = determine_scope_id(job, scenario)
    
    await metadata_service.upsert_scenario(
        scope=scope,
        scope_id=scope_id,
        workspace_type=scenario.metadata.workspace,
        name=scenario.metadata.name,
        api_version=scenario.api_version,
        spec=scenario.spec,
        source={
            "repository": job.repo_id,
            "path": scenario.source_path,
            "commit_sha": job.commit_sha
        }
    )
```

## File Detection

### OI Workflow Detection

```python
def is_oi_workflow(file: RepoFile) -> bool:
    """Check if file is an OI Workflow definition."""
    
    # Path pattern: work-catalog/{track}/{oi-type}/workflow.yaml
    if not re.match(r"(.*\/)?work-catalog\/[^\/]+\/[^\/]+\/workflow\.ya?ml$", file.path):
        return False
    
    # Content check: kind: OIWorkflow
    try:
        content = yaml.safe_load(file.content)
        return content.get("kind") == "OIWorkflow"
    except:
        return False
```

### Scenario Detection

```python
def is_scenario(file: RepoFile) -> bool:
    """Check if file is a Scenario definition."""
    
    # Path pattern: work-catalog/{track}/{oi-type}/{workspace}/scenarios/*.yaml
    if not re.match(r"(.*\/)?work-catalog\/[^\/]+\/[^\/]+\/[^\/]+\/scenarios\/[^\/]+\.ya?ml$", file.path):
        return False
    
    # Content check: kind: Scenario
    try:
        content = yaml.safe_load(file.content)
        return content.get("kind") == "Scenario"
    except:
        return False
```

## Validation During Sync

All artifacts are validated before being stored:

```python
async def validate_scenario(scenario: ParsedScenario, job: SyncJob) -> ValidationResult:
    """Validate scenario during sync."""
    
    context = build_validation_context(job)
    
    result = await work_catalog_management.validate(
        type="scenario",
        yaml=scenario.raw_content,
        context=context
    )
    
    if not result.valid:
        return ValidationResult(
            valid=False,
            artifact_name=scenario.metadata.name,
            artifact_path=scenario.source_path,
            errors=result.errors
        )
    
    return ValidationResult(valid=True, artifact_name=scenario.metadata.name)
```

## Cache Invalidation

After successful sync, relevant caches are invalidated:

```python
async def invalidate_caches(job: SyncJob):
    """Invalidate caches affected by the sync."""
    
    if job.repo_type == "platform":
        # Platform change affects all caches
        await cache.invalidate_pattern("effective-catalog:*")
        await cache.invalidate_pattern("resolve:*")
    
    elif job.repo_type == "foundry":
        foundry_id = job.repo_id.split("-")[0]
        # Foundry change affects all workshops/workbenches in foundry
        await cache.invalidate_pattern(f"effective-catalog:{foundry_id}:*")
        await cache.invalidate_pattern(f"resolve:{foundry_id}:*")
    
    elif job.repo_type == "workshop":
        # Workshop change affects all workbenches in workshop
        workshop_id = extract_workshop_id(job)
        await cache.invalidate_pattern(f"effective-catalog:*:{workshop_id}:*")
        await cache.invalidate_pattern(f"resolve:*:{workshop_id}:*")
    
    elif job.repo_type == "workbench":
        # Workbench change affects only that workbench
        workbench_id = extract_workbench_id(job)
        await cache.invalidate_pattern(f"effective-catalog:*:*:{workbench_id}*")
        await cache.invalidate_pattern(f"resolve:*:*:{workbench_id}*")
    
    elif job.repo_type == "user":
        # User change affects only user's active sessions
        user_id = extract_user_id(job)
        await cache.invalidate_pattern(f"effective-catalog:*:*:*:{user_id}")
        await cache.invalidate_pattern(f"resolve:*:*:*:{user_id}")
```

## Failure Handling

### Validation Failure

When artifacts fail validation during sync:

1. **Block the sync** — Invalid artifacts are not stored
2. **Notify stakeholders** — Send notification with validation errors
3. **Log for debugging** — Record full validation context
4. **Leave existing artifacts** — Previous valid version remains active

```python
async def notify_sync_failure(job: SyncJob, failures: List[ValidationResult]):
    """Notify stakeholders of sync failure."""
    
    await notification_service.send(
        channel="workbench-admins",
        template="sync-validation-failed",
        data={
            "repository": job.repo_id,
            "commit_sha": job.commit_sha,
            "failures": [
                {
                    "artifact": f.artifact_name,
                    "path": f.artifact_path,
                    "errors": f.errors
                }
                for f in failures
            ]
        }
    )
```

### Partial Sync

If some artifacts fail validation, the sync can proceed partially:

```python
# Configuration option
PARTIAL_SYNC_ENABLED = True

if PARTIAL_SYNC_ENABLED:
    # Sync valid artifacts, skip invalid ones
    valid_artifacts = [a for a in artifacts if a.validation.valid]
    for artifact in valid_artifacts:
        await upsert_artifact(artifact, job)
    
    # Notify about skipped artifacts
    if failures:
        await notify_partial_sync(job, valid_artifacts, failures)
```

## Manual Sync

Users can trigger manual sync for their personal catalog:

```http
POST /api/v1/users/{user_id}/work-catalog/sync
Authorization: Bearer <user-token>

{
  "foundry_id": "acme"
}
```

```python
@app.post("/api/v1/users/{user_id}/work-catalog/sync")
async def manual_user_catalog_sync(user_id: str, request: SyncRequest):
    """Manually trigger sync of user's work catalog."""
    
    # Verify user owns this catalog
    if request.user.id != user_id:
        raise ForbiddenError("Can only sync own catalog")
    
    # Get user's work catalog repo
    repo = await get_user_catalog_repo(user_id, request.foundry_id)
    if not repo:
        raise NotFoundError("User work catalog not found")
    
    # Queue sync job
    job = SyncJob(
        repo_type="user",
        repo_id=repo.full_name,
        commit_sha=await get_latest_commit(repo),
        changed_files=None,  # Full sync
        triggered_by=user_id
    )
    await job_queue.enqueue(job, priority="high")
    
    return {"status": "queued", "job_id": job.id}
```

## Sync Status API

```http
GET /api/v1/work-catalog/sync-status
  ?repo_type=workshop
  &repo_id=ecommerce
```

**Response:**

```json
{
  "repository": "acme/ecommerce-workshop-definition",
  "last_sync": {
    "commit_sha": "abc123",
    "synced_at": "2026-05-28T10:30:00Z",
    "artifacts_synced": 12,
    "status": "success"
  },
  "pending_sync": null
}
```

## Monitoring

### Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `work_catalog_sync_total` | Counter | Sync jobs by status (success/failure) |
| `work_catalog_sync_duration_ms` | Histogram | Sync job duration |
| `work_catalog_sync_artifacts_total` | Counter | Artifacts synced by type |
| `work_catalog_validation_failures_total` | Counter | Validation failures during sync |

### Alerts

| Alert | Condition | Severity |
|-------|-----------|----------|
| Sync failure rate high | >5% failures in 1h | Warning |
| Sync backlog growing | >100 pending jobs | Warning |
| Sync latency high | p99 >5min | Warning |

## Read Next

- [README.md](README.md) — Work Catalog Management overview
- [validation-rules.md](validation-rules.md) — Validation specification
- [events-and-caching.md](events-and-caching.md) — Events and caching
- [../services/workshop-sync.md](../services/workshop-sync.md) — Workshop Sync Service details
