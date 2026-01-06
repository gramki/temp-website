# ADR-0016: Typed Data Store CRDs Instead of Generic DataStore

## Status

**Accepted**

## Date

2026-01-06

## Context

Hub Applications require workbench-scoped storage for business domain entities. The Data Architecture defines three types of Application Data Stores:

| Store | Type | Platform | Use Cases |
|-------|------|----------|-----------|
| **Ganymede** | Relational DBaaS | PostgreSQL-compatible | Business entities, complex relationships, ACID transactions |
| **Callisto** | Key-Value Store | Distributed KV | Entity state, caching, fast lookups |
| **Europa** | Search/Analytics | OpenSearch (ELK) | Full-text search, log aggregation, analytics |

Each store type has fundamentally different:
- Configuration parameters (schema vs. collections vs. indices)
- Capacity planning (connections vs. memory vs. shards)
- Operational concerns (DDL migrations vs. TTL policies vs. retention)

## Decision

Create **separate typed CRDs** for each data store type rather than a single generic `DataStore` CRD:

| CRD | Purpose |
|-----|---------|
| `GanymedeStore` | Provisions PostgreSQL-compatible relational databases |
| `CallistoStore` | Provisions distributed key-value stores |
| `EuropaStore` | Provisions OpenSearch-based search/analytics services |

Each CRD has:
- Store-specific configuration schema
- Store-specific validation rules
- Store-specific reconciliation behavior
- Store-specific capacity and performance parameters

## Alternatives Considered

### Alternative 1: Generic DataStore CRD with Type Discriminator
```yaml
kind: DataStore
spec:
  type: ganymede  # or callisto, europa
  ganymede_config:  # optional, based on type
    ...
  callisto_config:  # optional, based on type
    ...
```

- **Pros**: Single CRD to manage, simpler operator
- **Cons**: Complex validation (conditional on type), larger CRD schema, less type safety

### Alternative 2: Inheritance-Based CRDs
```yaml
kind: GanymedeStore
# inherits from DataStore
```

- **Pros**: Shared base properties, type hierarchy
- **Cons**: Kubernetes CRDs don't support inheritance natively, complex operator logic

## Consequences

### Positive
- **Type Safety**: Each CRD has only relevant fields
- **Clear Validation**: Store-specific validation rules per CRD
- **Better Documentation**: Each CRD documented with store-specific examples
- **Specialized Operators**: Each store type can have specialized reconciliation

### Negative
- **More CRDs**: Three CRDs instead of one
- **Code Duplication**: Some common patterns repeated across CRDs
- **Migration Complexity**: If store types need to be changed, requires new CRD

### Neutral
- Aligns with Hub's Data Architecture naming (Ganymede, Callisto, Europa)
- Each CRD managed by Admin Operators

## Examples

### Ganymede (Relational)
```yaml
kind: GanymedeStore
spec:
  capacity:
    storage: 50Gi
    connections: 100
  schema:
    ddl_path: "./ddl/"
    auto_migrate: true
```

### Callisto (Key-Value)
```yaml
kind: CallistoStore
spec:
  capacity:
    memory: 8Gi
    max_keys: 10000000
  collections:
    - name: dispute-states
      ttl_seconds: 86400
```

### Europa (Search/Analytics)
```yaml
kind: EuropaStore
spec:
  capacity:
    storage: 100Gi
    shards: 3
  index_templates:
    - name: dispute-history
      retention_days: 365
```

## Related Decisions

- [ADR-0014: GitOps-Based Operator Model](./0014-gitops-operator-model.md)
- [ADR-0015: Persona-Based Operator Grouping](./0015-persona-based-operator-grouping.md)

