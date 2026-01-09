# ADR-0031: Application Data Stores are Optional (Not Mandated)

## Status

**Accepted**

## Date

2026-01-06

## Context

Hub provides Application Data Stores (Ganymede, Callisto, Europa) for Hub Applications to persist business domain entities. The question is whether these stores should be:
1. **Mandated** — Every workbench must have them
2. **Optional** — Available when needed, but not required

Some Hub Applications may:
- Only orchestrate requests without needing domain storage
- Use external systems for all data persistence
- Be simple transformations that don't maintain state

Mandating data stores for all applications would create unnecessary overhead.

## Decision

**Application Data Stores are optional — Hub provides the capability but does NOT mandate its use.**

### Key Principles

| Principle | Description |
|-----------|-------------|
| **Developer Choice** | How an application is built and whether it uses these stores is the developer's decision |
| **No Default Provisioning** | Data stores are not automatically provisioned; must be explicitly requested |
| **Per-Store Selection** | Developers can choose which stores to use (e.g., only Ganymede, or only Callisto) |
| **Admin Enablement** | Tenant Admin must approve provisioning |

### When to Use

| Store | Use When |
|-------|----------|
| **Ganymede** | Complex relationships, transactions, SQL queries, joins |
| **Callisto** | Fast lookups, entity state, caching, flexible schemas |
| **Europa** | Full-text search, log aggregation, time-series, analytics |

### When NOT to Use

| Scenario | Alternative |
|----------|-------------|
| Decisions, rationale | Enterprise Memory (via CAF) |
| User preferences | User Memory |
| Agent learning | Agent Memory |
| Policies, rules | Knowledge Services |
| Hub operational data | Operations Data (via Hub APIs) |

## Alternatives Considered

### Alternative 1: Mandatory Data Stores
Every workbench automatically gets all three data stores.

- **Pros**: Consistent, no decision overhead
- **Cons**: Wasted resources, unnecessary complexity for simple applications

### Alternative 2: Mandatory Ganymede Only
Relational store is always available; others optional.

- **Pros**: Common use case covered
- **Cons**: Still wasteful for applications that don't need it

## Consequences

### Positive
- **Resource Efficiency**: Only provision what's needed
- **Simpler Workbenches**: Simple applications don't carry data store overhead
- **Developer Autonomy**: Developers choose based on actual needs
- **Cost Control**: Tenants only pay for what they use

### Negative
- **Decision Burden**: Developers must decide what they need
- **Later Provisioning**: May need to add stores later if requirements change
- **Inconsistency**: Different workbenches have different data store configurations

### Neutral
- Provisioning can be done at any time (initial or later)
- DDL migrations supported for adding/evolving stores

## Provisioning Flow

1. **Define** — Developer specifies required stores in Workbench Definition (optional section)
2. **Request** — Tenant Admin reviews and approves provisioning
3. **Provision** — Hub provisions requested stores
4. **Access** — Applications receive connection credentials

```yaml
# Workbench Definition — Application Data Stores (all optional)
workbench:
  id: "dispute-resolution"
  
  application_data_stores:        # Entire section is optional
    - name: "dispute_entities"    # Optional: Ganymede
      type: "ganymede"
      ddl_path: "./ddl/dispute-entities.sql"
      
    - name: "dispute_cache"       # Optional: Callisto
      type: "callisto"
      collection: "dispute-states"
      
    - name: "dispute_search"      # Optional: Europa
      type: "europa"
      index_template: "./indices/dispute-index.json"
```

## Examples

### Simple Orchestration Application (No Data Stores)
An application that receives signals, makes decisions using Knowledge Services, and creates tasks — no domain storage needed.

### Full-Featured Application (All Data Stores)
A dispute resolution application with:
- Ganymede for Dispute entities
- Callisto for status caching
- Europa for search and analytics

### Search-Only Application (Europa Only)
A reporting application that aggregates data in Europa for dashboards — no relational or key-value storage needed.

## Related Decisions

- [ADR-0016: Typed Data Store CRDs](./0016-typed-data-store-crds.md)
- [ADR-0030: Workbench-Scoped Data Stores](./0030-workbench-scoped-data-stores.md)
- [ADR-0028: Data Classification](./0028-data-classification.md)

