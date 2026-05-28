# Workshop Sync Service

The Workshop Sync Service processes changes from Workshop Definition Repositories and populates the Metadata Service with validated configuration.

## Purpose

- Receive GitHub webhooks on merge to main
- Process changed files and extract configuration
- Write validated config to Metadata Service
- Support explicit sync triggers for recovery/refresh

## How It Works

```
┌─────────────────┐
│   Workshop Repo │
│      (Git)      │
└────────┬────────┘
         │ merge to main
         │ (webhook)
         ▼
┌─────────────────────────────────────────────────────────────┐
│                  Workshop Sync Service                       │
│                                                             │
│  1. Receive GitHub push webhook                             │
│  2. Identify Workshop from repo                             │
│  3. Fetch changed files from commit                         │
│  4. For each changed file:                                  │
│     - Parse YAML content                                    │
│     - Transform to Metadata Service format                  │
│     - Write to Metadata Service                             │
│  5. Trigger cache invalidation                              │
│                                                             │
└──────────────────────────┬──────────────────────────────────┘
                           │ writes
                           ▼
                  ┌─────────────────┐
                  │Metadata Service │
                  └─────────────────┘
```

## Sync Process

### Webhook Processing

```
1. Receive push event from GitHub
2. Validate webhook signature (HMAC)
3. Extract:
   - Repository (maps to Workshop)
   - Commit SHA
   - Changed files list
4. Queue sync job
```

### File Processing

| File Pattern | Processing |
|--------------|------------|
| `workbenches/{wb}/workbench.yaml` | Update Workbench config |
| `workbenches/{wb}/integrations.yaml` | Update integrations |
| `workbenches/{wb}/team.yaml` | Update team roster |
| `workbenches/{wb}/workspaces/{ws}/*.yaml` | Update Workspace config |
| `workbenches/{wb}/workspaces/{ws}/scenarios/*.yaml` | Update Scenario registry |
| `workbenches/{wb}/workspaces/{ws}/skills/*` | Update Skill references |
| `workspaces/{ws}/*` | Update Workshop-level Workspace defaults |

### Conflict Resolution

When Workshop and Workbench define the same config:

```
Effective Config = Workshop Base + Workbench Overrides
```

The Sync Service computes the effective config and stores it in Metadata Service.

## Explicit Sync Trigger

For recovery or manual refresh:

```
POST /api/v1/sync/trigger
Body: {
  "workshop_id": "ws-retail",
  "full_sync": true  // false = only changed since last sync
}
Response: {
  "sync_id": "sync-123",
  "status": "queued"
}
```

Use cases:
- Recovery after Metadata Service restore
- Initial sync for new Workshop
- Force refresh after schema migration

## Sync States

| State | Description |
|-------|-------------|
| `queued` | Sync job created, waiting for worker |
| `processing` | Worker processing changes |
| `completed` | All changes written to Metadata Service |
| `failed` | Error during sync (see error details) |
| `partial` | Some files synced, others failed |

## Error Handling

### Transient Errors

| Error | Handling |
|-------|----------|
| Metadata Service unavailable | Retry with exponential backoff |
| GitHub API rate limited | Wait and retry |
| Network timeout | Retry up to 3 times |

### Permanent Errors

| Error | Handling |
|-------|----------|
| Invalid YAML (should be caught by validation) | Log error, skip file, alert |
| Unknown file type | Log warning, skip file |
| Schema mismatch | Log error, skip file, alert |

Failed files are recorded and can be manually re-synced after fixing.

## Idempotency

Sync operations are idempotent:
- Same commit SHA processed twice produces same result
- Metadata Service uses upsert semantics
- Sync ID prevents duplicate processing

## API

### Webhook Endpoint

```
POST /api/v1/webhooks/github
Headers: X-Hub-Signature-256: sha256=...
Body: (GitHub push event payload)
```

### Sync Status

```
GET /api/v1/sync/{sync_id}
Response: {
  "sync_id": "sync-123",
  "workshop_id": "ws-retail",
  "status": "completed",
  "commit_sha": "abc123",
  "files_processed": 12,
  "files_failed": 0,
  "started_at": "2026-05-28T10:00:00Z",
  "completed_at": "2026-05-28T10:00:05Z"
}
```

### List Recent Syncs

```
GET /api/v1/sync?workshop_id={id}&limit=10
Response: { syncs: [...] }
```

## Observability

| Metric | Description |
|--------|-------------|
| `sync_jobs_total` | Total sync jobs processed |
| `sync_duration_seconds` | Time to complete sync |
| `sync_files_processed` | Files processed per sync |
| `sync_errors_total` | Sync errors by type |
| `webhook_received_total` | Webhooks received |

## Read Next

- [workshop-validation.md](workshop-validation.md) — What validates before sync
- [metadata-service.md](metadata-service.md) — Where sync writes to
- [../workshop-repository.md](../workshop-repository.md) — Workshop repo structure
