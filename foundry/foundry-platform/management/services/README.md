# Management Services

The Management module provides several services that work together to manage Workshop configuration and make it available to the platform.

## Service Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Management Module Services                          │
│                                                                             │
│  ┌─────────────────────┐     ┌─────────────────────┐                       │
│  │ Workshop Validation │     │   Workshop Sync     │                       │
│  │      Service        │     │     Service         │                       │
│  └──────────┬──────────┘     └──────────┬──────────┘                       │
│             │                           │                                   │
│             │ validates                 │ writes                            │
│             ▼                           ▼                                   │
│  ┌──────────────────────────────────────────────────────────────┐          │
│  │                      Metadata Service                         │          │
│  │  (Central config store for Foundry/Workshop/Workbench)       │          │
│  └──────────────────────────────────────────────────────────────┘          │
│                                    │                                        │
└────────────────────────────────────┼────────────────────────────────────────┘
                                     │ queries
           ┌─────────────────────────┼─────────────────────────┐
           │                         │                         │
           ▼                         ▼                         ▼
    ┌────────────┐            ┌────────────┐            ┌────────────┐
    │Orchestrator│            │ WO Runtime │            │  Web App   │
    └────────────┘            └────────────┘            └────────────┘
```

## Services

| Service | Purpose | Documentation |
|---------|---------|---------------|
| **Workshop Validation** | Validates PRs against Workshop repo, gates merges | [workshop-validation.md](workshop-validation.md) |
| **Workshop Sync** | Processes git webhooks, populates Metadata Service | [workshop-sync.md](workshop-sync.md) |
| **Metadata Service** | Central config store, ID generation, query APIs | [metadata-service.md](metadata-service.md) |

## Data Flow

### Configuration Changes

```
1. Author creates PR against Workshop Definition Repo
2. Workshop Validation Service validates PR content
   - Schema validation (YAML structure)
   - Reference validation (skills, scenarios exist)
   - Permission checks
3. If valid, Validation Service merges to main
4. GitHub webhook fires on merge
5. Workshop Sync Service receives webhook
6. Sync Service processes changes:
   - Parses modified files
   - Validates against current state
   - Updates Metadata Service
7. Metadata Service notifies interested parties (cache invalidation)
```

### Configuration Queries

```
1. Consumer (Orchestrator, WO Runtime, Web App) needs config
2. Consumer queries Metadata Service API
3. Metadata Service returns config from its store
4. Consumer caches locally if appropriate
```

## Integration with GitHub

Foundry operates as a **GitHub App** registered in the organization:

| Capability | Implementation |
|------------|----------------|
| Repo creation | Foundry creates Workshop repos via GitHub API |
| PR validation | GitHub check runs trigger Validation Service |
| Merge control | Only Validation Service has merge permission |
| Webhook handling | GitHub webhooks route to Sync Service |

## Read Next

- [workshop-validation.md](workshop-validation.md) — PR validation and merge gating
- [workshop-sync.md](workshop-sync.md) — Webhook processing and sync
- [metadata-service.md](metadata-service.md) — Central config store
- [../work-catalog-management/README.md](../work-catalog-management/README.md) — Work Catalog Management (schemas, resolution, validation)
