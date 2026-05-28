# Metadata Service

The Metadata Service is the central configuration store for Foundry. It holds all Foundry, Workshop, Workbench, Workspace, and Scenario configuration, and provides query APIs for platform consumers.

## Purpose

- Store and serve platform configuration
- Generate unique IDs for orchestration items
- Track commits across repositories
- Provide query APIs for Orchestrator, WO Runtime, and Web App

## Scope

| Capability | Description |
|------------|-------------|
| **ID Generation** | Unique IDs for PI, WO, RI, DC, RC |
| **Commit Tracking** | Track commits to Intent, Design, Code repos |
| **Config Store** | Foundry, Workshop, Workbench, Workspace, Scenario configs |
| **Query APIs** | REST APIs for consumers to fetch configuration |

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Metadata Service                                   │
│                                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │     ID      │  │   Commit    │  │   Config    │  │    Query    │        │
│  │  Generator  │  │  Tracker    │  │    Store    │  │    APIs     │        │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘        │
│         │                │                │                │               │
│         └────────────────┴────────────────┴────────────────┘               │
│                                   │                                         │
│                          ┌────────┴────────┐                               │
│                          │    Database     │                               │
│                          │   (Postgres)    │                               │
│                          └─────────────────┘                               │
└─────────────────────────────────────────────────────────────────────────────┘
         ▲                         ▲                         ▲
         │ writes                  │ queries                 │ queries
         │                         │                         │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Workshop Sync  │    │   Orchestrator  │    │   WO Runtime    │
│    Service      │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## ID Generation

### Supported Types

| Type | Prefix | Example | Consumers |
|------|--------|---------|-----------|
| `product-intent` | `PI` | `PI-456` | IDE extensions, Orchestrator |
| `release-intent` | `RI` | `RI-78` | Web console, Orchestrator |
| `work-order` | `WO` | `WO-1234` | Orchestrator |
| `discovery-case` | `DC` | `DC-89` | IDE extensions, Orchestrator |
| `run-case` | `RC` | `RC-45` | IDE extensions, Orchestrator |

### API

```
POST /api/v1/ids/{type}
Response: { "id": "PI-456" }
```

### Sequence Management

- Sequences are scoped per Workbench
- Monotonically increasing integers
- Gap-free not guaranteed (failed transactions may consume IDs)
- IDs are unique within a Workbench

## Commit Tracking

### Tracked Repositories

| Repository | Tracking |
|------------|----------|
| Intent Repository | All commits to main |
| Design Repository | All commits to main |
| Code Repositories | All commits to main (multiple repos) |

### API

```
GET /api/v1/commits?workbench={id}&repo_type=intent&since={timestamp}
Response: { commits: [{ sha, message, author, timestamp, files }] }
```

## Config Store

### Hierarchy

```
Foundry
└── Workshop
    └── Workbench
        └── Workspace
            └── Scenario
```

### Stored Configuration

| Entity | Key Fields | Source |
|--------|------------|--------|
| **Foundry** | id, name, settings | Foundry setup |
| **Workshop** | id, foundry_id, name, settings | Workshop Sync |
| **Workbench** | id, workshop_id, name, integrations, team | Workshop Sync |
| **Workspace** | id, workbench_id, type, devcontainer, hooks | Workshop Sync |
| **Scenario** | id, workspace_id, name, spec, triggers | Workshop Sync |
| **Skill** | id, workspace_id, name, version, spec | Workshop Sync |

### Effective Config Resolution

Workbench config overrides Workshop defaults:

```
GET /api/v1/config/effective/workspace/{id}
Response: {
  "workspace": { ... merged config ... },
  "scenarios": [ ... merged scenarios ... ],
  "skills": [ ... merged skills ... ]
}
```

## Query APIs

### Foundry/Workshop/Workbench

```
GET /api/v1/foundry
GET /api/v1/workshops
GET /api/v1/workshops/{id}
GET /api/v1/workbenches
GET /api/v1/workbenches/{id}
```

### Workspaces

```
GET /api/v1/workspaces?workbench={id}
GET /api/v1/workspaces/{id}
GET /api/v1/workspaces/{id}/scenarios
GET /api/v1/workspaces/{id}/skills
```

### Scenarios

```
GET /api/v1/scenarios/{id}
GET /api/v1/scenarios?workspace={id}&trigger={trigger_type}
```

### Skills

```
GET /api/v1/skills/{id}
GET /api/v1/skills?workspace={id}
```

## Caching

### Client-Side Caching

Consumers (WO Runtime, Orchestrator) should cache locally:

| Cache Strategy | Use Case |
|----------------|----------|
| **Session cache** | WO Runtime caches at session start |
| **TTL cache** | Web App caches with short TTL |
| **Event-driven invalidation** | Subscribe to change events |

### Cache Invalidation

Metadata Service publishes change events:

```
Topic: metadata.changes
Event: {
  "type": "workspace.updated",
  "workspace_id": "ws-123",
  "timestamp": "2026-05-28T10:00:00Z"
}
```

Consumers can subscribe to invalidate local caches.

## Data Model

### Tables (Postgres)

| Table | Purpose |
|-------|---------|
| `foundries` | Foundry instances |
| `workshops` | Workshops per Foundry |
| `workbenches` | Workbenches per Workshop |
| `workspaces` | Workspaces per Workbench |
| `scenarios` | Scenarios per Workspace |
| `skills` | Skills per Workspace |
| `id_sequences` | ID sequence tracking |
| `commits` | Commit history |

### Indexes

- `workbenches.workshop_id`
- `workspaces.workbench_id`
- `scenarios.workspace_id`
- `commits.(workbench_id, repo_type, timestamp)`

## Error Handling

| Error | HTTP Status | Handling |
|-------|-------------|----------|
| Entity not found | 404 | Return clear error message |
| Invalid query params | 400 | Return validation errors |
| Database unavailable | 503 | Retry, then fail |
| Sequence exhausted | 500 | Alert, manual intervention |

## Observability

| Metric | Description |
|--------|-------------|
| `metadata_queries_total` | Total queries by endpoint |
| `metadata_query_duration_ms` | Query latency |
| `metadata_ids_generated` | IDs generated by type |
| `metadata_cache_invalidations` | Cache invalidation events |

## Read Next

- [workshop-sync.md](workshop-sync.md) — How config gets into Metadata Service
- [workshop-validation.md](workshop-validation.md) — How config is validated
- [../scenario-management/README.md](../scenario-management/README.md) — Scenario-specific logic
