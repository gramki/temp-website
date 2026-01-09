# ADR-0030: Application Data Stores are Workbench-Scoped (Not Runtime-Scoped)

## Status

**Accepted**

## Date

2026-01-06

## Context

Hub Applications run on different Automation Runtimes:
- **Atlantis** — Container runtime
- **Perseus** — Batch/ETL runtime
- **Rhea** — BPMN workflow runtime
- **ChronoShift** — Durable workflow runtime (Temporal)
- **Seer** — AI Agent runtime

Each runtime has internal storage needs (workflow state, batch metadata, agent context). The question is: how should Application Data Stores (Ganymede, Callisto, Europa) be scoped?

Options:
1. Per-runtime (each application has its own stores)
2. Per-workbench (all applications in a workbench share stores)

## Decision

**Application Data Stores are workbench-scoped, not runtime-scoped.**

### Key Principles

| Principle | Description |
|-----------|-------------|
| **Runtime-Agnostic Access** | All Hub Applications can access Application Data Stores regardless of their Automation Runtime |
| **Admin-Enabled** | Access to data stores must be enabled by Tenant Admin during workbench provisioning |
| **Optional Service** | Hub provides the capability; applications choose whether to use it |
| **Developer Choice** | How an application is built and whether it uses these stores is the developer's decision |
| **Workbench-Scoped** | Stores are shared across all applications within a workbench |

### Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                 WORKBENCH: Dispute Resolution                           │
├────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  HUB APPLICATIONS (different runtimes, same data stores)               │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐        │
│  │  Filing Agent   │  │ Document Proc   │  │  Final Review   │        │
│  │  (Seer)         │  │  (Perseus)      │  │   (Rhea)        │        │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘        │
│           │                    │                    │                  │
│           └────────────────────┼────────────────────┘                  │
│                                │                                       │
│                                ▼                                       │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │                APPLICATION DATA STORES                          │  │
│  │  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐           │  │
│  │  │  Ganymede   │   │  Callisto   │   │   Europa    │           │  │
│  │  │  (Entities) │   │  (Cache)    │   │  (Search)   │           │  │
│  │  └─────────────┘   └─────────────┘   └─────────────┘           │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                         │
└────────────────────────────────────────────────────────────────────────┘
```

### Runtime Internal Storage (Separate Concern)

Each Automation Runtime has its **own internal storage** for runtime-specific needs:
- Rhea/ChronoShift: Workflow state, execution history
- Perseus: Batch job metadata, processing state
- Seer: Agent context, conversation history

These internal storage choices are **engineering decisions for each runtime** and are documented in their respective project documentation, not in Hub's architecture documentation.

## Alternatives Considered

### Alternative 1: Per-Runtime Data Stores
Each application gets its own isolated data stores.

- **Pros**: Complete isolation, no contention
- **Cons**: Cannot share business entities across applications in same workbench, data duplication, complex synchronization

### Alternative 2: Tenant-Scoped Data Stores
All workbenches in a tenant share the same data stores.

- **Pros**: Maximum sharing
- **Cons**: Too broad, blurs workbench isolation, security concerns

## Consequences

### Positive
- **Entity Sharing**: Multiple applications can access same business entities (e.g., Dispute entity)
- **No Duplication**: Single source of truth for domain data within workbench
- **Runtime Flexibility**: Can use best runtime for each application without data silos
- **Simpler Architecture**: Fewer data stores to provision and manage

### Negative
- **Contention**: Multiple applications accessing same tables/collections
- **Schema Coordination**: DDL changes affect all applications in workbench
- **Access Control**: Must manage access within workbench

### Neutral
- Workbench-scoped isolation provides security boundary
- Cross-workbench access requires explicit configuration

## Example: Dispute Resolution Workbench

| Application | Runtime | Accesses |
|-------------|---------|----------|
| Dispute Filing Agent | Seer | Ganymede (Dispute entity), Callisto (status cache) |
| Document Processing | Perseus | Ganymede (Dispute entity), Europa (document index) |
| Final Review Workflow | Rhea | Ganymede (Dispute entity) |

All three applications share access to the same Ganymede database where the Dispute entity is stored.

## Related Decisions

- [ADR-0016: Typed Data Store CRDs](./0016-typed-data-store-crds.md)
- [ADR-0027: Four-Layer Storage Model](./0027-four-layer-storage-model.md)
- [ADR-0031: Optional Application Data Stores](./0031-optional-data-stores.md)

