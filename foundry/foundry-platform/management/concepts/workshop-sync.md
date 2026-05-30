# Workshop Sync

Workshop Sync is the service that processes changes from Foundry, Workshop, and User Work Catalog definition repositories and populates the Metadata Service with validated configuration — the pipeline that turns Git commits into runtime-queryable config.

## What it is

Workshop Sync bridges the gap between configuration-as-code (stored in Git) and configuration-at-runtime (served by Metadata Service). When an admin merges changes to a definition repository, Workshop Sync ensures those changes propagate to where runtime modules can use them.

The sync process:

1. **Receive** — GitHub webhook on merge/push to main
2. **Identify** — Map repository to Workshop/Foundry/User
3. **Fetch** — Get changed files from the commit
4. **Parse** — Extract YAML content from each file
5. **Transform** — Convert to Metadata Service format
6. **Write** — Upsert to Metadata Service
7. **Invalidate** — Trigger cache invalidation for affected scopes

File patterns determine processing:

| File Pattern | Processing |
|--------------|------------|
| `foundry.yaml` | Update Foundry config |
| `workshop.yaml` | Update Workshop config |
| `workbenches/{wb}/workbench.yaml` | Update Workbench config |
| `work-catalog/**` | Update Work Catalog |
| `domain/**`, `practices/**` | Update knowledge indexes |

When Workshop and Workbench define the same config:

```
Effective Config = Workshop Base + Workbench Overrides
```

Workshop Sync computes this effective config before writing to Metadata Service.

Sync operations are idempotent:
- Same commit SHA processed twice produces same result
- Metadata Service uses upsert semantics
- Sync ID prevents duplicate processing

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Workshop Sync Service** | Webhook handling, file processing, sync orchestration |
| **Metadata Service** | Destination for synced configuration |
| **Validation Module** | Re-validates during sync (safety net) |
| **GitHub App** | Receives push events |

Sync flow:

```
Foundry Repo │ Workshop Repo │ User Work Catalog Repo
    (Git)    │     (Git)     │         (Git)
       │            │                  │
       └────────────┴──────────────────┘
                    │ merge/push to main (webhook)
                    ▼
┌──────────────────────────────────────────────────────────┐
│                  Workshop Sync Service                    │
│                                                          │
│  1. Receive GitHub push webhook                          │
│  2. Identify Workshop from repo                          │
│  3. Fetch changed files from commit                      │
│  4. Parse, transform, write to Metadata Service          │
│  5. Trigger cache invalidation                           │
└──────────────────────────────────────────────────────────┘
                    │
                    ▼
            Metadata Service
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Repositories](../../concepts/repositories.md) | Sync propagates from definition repos |
| Configuration | Git-based configuration synced to runtime |

Workshop Sync operationalizes the principle that Git is the source of truth for configuration. Rather than requiring runtime modules to read directly from Git (slow, complex), sync maintains a runtime-optimized copy in Metadata Service.

## Related concepts

- [Validation Module](validation-module.md) — Validates config before and during sync
- [Declarative Provisioning](declarative-provisioning.md) — Creates repos that sync monitors
- [Work Catalog Resolution](work-catalog-resolution.md) — Consumes synced catalog content
- [Metadata Service](../../concepts/metadata-service.md) — Destination for synced config

## Further reading

- [../platform-developer-guide/services/workshop-sync.md](../platform-developer-guide/services/workshop-sync.md) — Sync service specification
- [../platform-developer-guide/services/metadata-service.md](../platform-developer-guide/services/metadata-service.md) — Metadata Service details
- [../platform-developer-guide/workshop-repository.md](../platform-developer-guide/workshop-repository.md) — Workshop repo structure
