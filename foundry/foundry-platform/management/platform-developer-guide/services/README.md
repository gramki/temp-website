# Management Services

The Management module provides several services that work together to manage Foundry, Workshop, and Work Catalog configuration and make it available to the platform.

## Service Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Management Module Services                          │
│                                                                             │
│  ┌─────────────────────┐     ┌─────────────────────┐                       │
│  │  Validation Module  │     │   Workshop Sync     │                       │
│  │  foundry-validation │     │     Service         │                       │
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
| **Validation Module** | Pre-publish gate for Foundry-scope config; PR merge control on definition repos | [../validation/README.md](../validation/README.md) |
| **Workshop Sync** | Processes git webhooks, populates Metadata Service | [workshop-sync.md](workshop-sync.md) |
| **Metadata Service** | Central config store, ID generation, query APIs | [metadata-service.md](metadata-service.md) |

## Data Flow

### Configuration Changes (Definition repos)

```
1. Author creates PR against Foundry or Workshop Definition Repo
2. Validation Module validates PR content (foundry-validation check)
   - Schema validation (YAML structure)
   - Reference validation (skills, scenarios exist)
   - Permission checks
3. If valid, Validation Module merges to main
4. GitHub webhook fires on merge
5. Workshop Sync Service receives webhook
6. Sync Service processes changes:
   - Parses modified files (work-catalog/**, domain/**, etc.)
   - Re-validates as safety net
   - Updates Metadata Service
7. Metadata Service notifies interested parties (cache invalidation)
```

### User Work Catalog Changes

```
1. Author pushes directly to main (user-work-catalog-{userId}/)
2. Validation Module validates on push (foundry-validation check; report only)
3. GitHub webhook fires on push
4. Workshop Sync Service processes work-catalog/** changes
5. Metadata Service updated
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
| PR validation | GitHub check `foundry-validation` triggers Validation Module |
| Merge control | Only Validation Module has merge permission on definition repos |
| Webhook handling | GitHub webhooks route to Sync Service |

## Read Next

- [../validation/README.md](../validation/README.md) — Validation module (pre-publish gate)
- [workshop-validation.md](workshop-validation.md) — GitHub integration appendix
- [workshop-sync.md](workshop-sync.md) — Webhook processing and sync
- [metadata-service.md](metadata-service.md) — Central config store
- [../work-catalog-management/README.md](../work-catalog-management/README.md) — Work Catalog Management (schemas, resolution, validation)
