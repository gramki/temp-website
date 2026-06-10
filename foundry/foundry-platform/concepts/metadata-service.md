# Metadata Service

The Metadata Service is the central configuration store for the Foundry Platform — holding all Foundry, Workshop, Workbench, Workspace, and Scenario configuration and providing query APIs for platform consumers.

## What it is

The Metadata Service is the authoritative runtime source for platform configuration. While configuration is authored in Git repositories (Foundry Definition Repo, Workshop Definition Repo), the Metadata Service is what platform modules query at runtime.

The service provides four core capabilities:

| Capability | Description |
|------------|-------------|
| **Configuration Store** | Foundry, Workshop, Workbench, Workspace, Scenario, Skill configs |
| **ID Generation** | Unique IDs for orchestration items (PI-123, WO-456, DC-789) |
| **Commit Tracking** | Track commits to Intent, Design, Code repositories |
| **Query APIs** | REST APIs for consumers to fetch configuration |

Configuration hierarchy stored:

```
Foundry
└── Workshop
    └── Workbench
        └── Workspace
            └── Scenario
```

The data flow:

```
1. Author creates PR against Definition Repo
2. Validation Module validates PR content
3. PR merges to main
4. Workshop Sync Service receives webhook
5. Sync Service updates Metadata Service
6. Consumers query Metadata Service
```

**Key design decision:** Consumers (Orchestrator, WO Runtime, Web App) query Metadata Service, never reading Git directly. This provides:

- Consistent, validated configuration
- Fast queries without Git overhead
- Cache invalidation via Atropos (`/{foundry-id}/foundry.management.metadata-changed`)
- Central audit point

ID generation supports multiple types:

| Type | Prefix | Example |
|------|--------|---------|
| `product-intent` | PI | PI-456 |
| `release-intent` | RI | RI-78 |
| `work-order` | WO | WO-1234 |
| `discovery-case` | DC | DC-89 |
| `run-case` | RC | RC-45 |

Sequences are scoped per Workbench, monotonically increasing.

Artifact registration returns canonical `artifactUri` per [../../foundry-work-plan/phase-1/repository-contracts.md](../../foundry-work-plan/phase-1/repository-contracts.md).

## Where it lives in Foundry

| Module | Interaction |
|--------|-------------|
| **Workshop Sync** | Writes configuration to Metadata Service |
| **Validation Module** | Validates before Sync writes |
| **Orchestrator** | Queries for OI Workflows, Workbench config |
| **WO Runtime** | Queries for Scenarios, Skills, Workspace config |
| **Web App** | Queries for display and user actions |
| **Agent Fabric** | Queries for Raw Agent, Skill registry config |

Architecture:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Metadata Service                                   │
│                                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │     ID      │  │   Commit    │  │   Config    │  │    Query    │        │
│  │  Generator  │  │  Tracker    │  │    Store    │  │    APIs     │        │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘        │
│         └────────────────┴────────────────┴────────────────┘               │
│                                   │                                         │
│                          ┌────────┴────────┐                               │
│                          │    Database     │                               │
│                          │   (Postgres)    │                               │
│                          └─────────────────┘                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

## ACE/UPIM alignment

The Metadata Service is a **Foundry Platform implementation concern**, not an ACE or UPIM entity. It operationalizes:

| ACE/UPIM Concept | Metadata Service Realization |
|------------------|------------------------------|
| Workshop configuration | Stored and queryable |
| Workbench configuration | Stored and queryable |
| Scenario definitions | Stored after validation |
| Skill definitions | Stored after validation |
| Orchestration item IDs | Generated with unique sequences |

The service is the runtime bridge between Git-based configuration authoring and module consumption.

## Related concepts

- [Containment Hierarchy](containment-hierarchy.md) — Configuration structure stored
- [Work Catalog](work-catalog.md) — Scenarios stored in Metadata Service
- [Knowledge Hierarchy](knowledge-hierarchy.md) — Knowledge served through Metadata Service
- [Scenario](scenario.md) — Definitions served by Metadata Service
- [Skill](skill.md) — Definitions served by Metadata Service

## Further reading

- [../management/platform-developer-guide/services/metadata-service.md](../management/platform-developer-guide/services/metadata-service.md) — Full specification
- [../management/platform-developer-guide/services/README.md](../management/platform-developer-guide/services/README.md) — Services overview
- [../management/platform-developer-guide/services/workshop-sync.md](../management/platform-developer-guide/services/workshop-sync.md) — How config reaches Metadata Service
- [../management/platform-developer-guide/validation/README.md](../management/platform-developer-guide/validation/README.md) — Validation before storage
