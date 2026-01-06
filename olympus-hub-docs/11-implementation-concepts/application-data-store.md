# Application Data Store

> **Category:** Data Architecture

---

## Overview

**Application Data Stores** are workbench-scoped storage services that Hub Applications use for structured data, key-value access, and search. Hub provides three data store types — Ganymede (relational), Callisto (key-value), and Europa (search/analytics) — each optimized for specific access patterns.

---

## Ontology Context

### Relationship to Ontology

The ontology describes knowledge and memory but doesn't detail transactional data storage for applications. Application Data Stores are implementation-level storage for Hub Application state.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| (not covered) | Application Data Store | Transactional storage for apps |
| Knowledge Base | Knowledge Bank (separate) | Different purpose |

### Gap This Fills

The ontology focuses on semantic knowledge. Application Data Stores address:
1. **Transactional data**: Order records, customer data, etc.
2. **Access patterns**: SQL vs key-value vs search
3. **Multi-tenancy**: Data isolation per workbench
4. **Migrations**: Schema evolution and data promotion

---

## Definition

**Application Data Store** is a workbench-scoped storage service that:
- Provides structured data storage for Hub Applications
- Is isolated per workbench (no cross-workbench access)
- Supports migrations during promotion
- Integrates with Hub observability

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-level; one per workbench per type |
| **Lifecycle** | Created by Admin; used by Applications |
| **Ownership** | Admin provisions; Developer uses |
| **Multiplicity** | Multiple stores per workbench possible |

---

## Rationale

### Why This Design?

Purpose-built stores enable:
1. **Right tool for job**: Different patterns for different needs
2. **Managed infrastructure**: Hub handles provisioning
3. **Promotion support**: Migrations move with artifacts
4. **Isolation**: Workbench data boundaries

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Single store type** | Inefficient for varied patterns |
| **External databases** | Complex; inconsistent integration |
| **Shared across workbenches** | Isolation concerns |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0030](../decision-logs/0030-three-tier-data-architecture.md) | Three-tier data architecture |
| [ADR-0031](../decision-logs/0031-data-store-per-workbench-isolation.md) | Per-workbench data isolation |

---

## Structure

### Data Store Types

| Store | Type | Use Cases |
|-------|------|-----------|
| **Ganymede** | Relational (PostgreSQL) | Structured data, transactions, complex queries |
| **Callisto** | Key-Value (Redis) | Session state, caches, counters |
| **Europa** | Search (Elasticsearch) | Full-text search, analytics, logs |

### Ganymede (Relational)

```yaml
apiVersion: hub.olympus.io/v1
kind: GanymedeStore
metadata:
  name: dispute-data
  namespace: acme-bank
spec:
  workbench_ref: dispute-ops-prod
  
  size: medium          # small | medium | large
  
  # Schema managed via migrations
  migration_ref: dispute-schema-v2
  
  # Connection pooling
  pool:
    min_connections: 5
    max_connections: 20
```

### Callisto (Key-Value)

```yaml
apiVersion: hub.olympus.io/v1
kind: CallistoStore
metadata:
  name: dispute-cache
  namespace: acme-bank
spec:
  workbench_ref: dispute-ops-prod
  
  size: small
  
  # TTL defaults
  default_ttl_seconds: 3600
  
  # Persistence
  persistence:
    enabled: true
    snapshot_interval_minutes: 15
```

### Europa (Search)

```yaml
apiVersion: hub.olympus.io/v1
kind: EuropaStore
metadata:
  name: dispute-search
  namespace: acme-bank
spec:
  workbench_ref: dispute-ops-prod
  
  size: medium
  
  # Index configuration
  indices:
    - name: disputes
      shards: 3
      replicas: 1
```

---

## Behavior

### How Applications Use Stores

```python
# Hub Application accessing data stores
class DisputeHandler(HubApplication):
    async def handle_request(self, update):
        # Relational query via Ganymede
        customer = await self.ganymede.query(
            "SELECT * FROM customers WHERE id = $1",
            [update.payload.customer_id]
        )
        
        # Cache lookup via Callisto
        cached_tier = await self.callisto.get(
            f"customer_tier:{update.payload.customer_id}"
        )
        
        # Full-text search via Europa
        similar_cases = await self.europa.search(
            index="disputes",
            query={
                "match": {
                    "description": update.payload.dispute_reason
                }
            }
        )
```

### Migration During Promotion

```
Promotion with data store changes:

1. Scenario includes migration CRD
2. Promotion copies migration to target
3. Target workbench runs migration:
   ├── Schema changes (DDL)
   └── Seed data (DML from OCI container)
4. Application uses new schema
```

### Data Isolation

```
Workbench A cannot access Workbench B data:
├── Separate database/schema per workbench
├── Credentials scoped to workbench
├── No cross-workbench queries
└── Promotion copies schemas, not data
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Hub Application | ← used by | Apps query stores |
| Migration CRD | → applied by | Schema changes |
| Olympus Watch | → logged | Query metrics |
| Promotion | → migrated | Schema migrations promoted |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Workbench isolation** | No cross-workbench data access |
| **Migration versioning** | Migrations use semver |
| **Forward only** | Migrations don't roll back data |
| **Size limits** | Quotas per store type |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Purpose-built** | Right tool for each pattern |
| ✅ **Managed** | Hub handles infrastructure |
| ✅ **Promotion-aware** | Migrations included in promotion |
| ✅ **Observable** | Integrated with Olympus Watch |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **No cross-workbench** | By design; use APIs for sharing |
| ⚠️ **Migration complexity** | Tooling and testing support |

---

## Examples

### Example 1: Creating Tables in Ganymede

```sql
-- Migration: 1.0.0
CREATE TABLE disputes (
    id UUID PRIMARY KEY,
    customer_id VARCHAR(50) NOT NULL,
    transaction_id VARCHAR(50) NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_disputes_customer ON disputes(customer_id);
CREATE INDEX idx_disputes_status ON disputes(status);
```

### Example 2: Caching with Callisto

```python
async def get_customer_tier(self, customer_id: str) -> str:
    # Try cache first
    cached = await self.callisto.get(f"tier:{customer_id}")
    if cached:
        return cached
    
    # Query source
    tier = await self.external_crm.get_tier(customer_id)
    
    # Cache for 1 hour
    await self.callisto.set(
        f"tier:{customer_id}", 
        tier, 
        ttl=3600
    )
    return tier
```

---

## Implementation Notes

### For Developers

- Use Ganymede for structured, queryable data
- Use Callisto for caching and session state
- Use Europa for search and analytics
- Write idempotent migrations

### For Operators

- Monitor store capacity and performance
- Manage backup schedules
- Review migration execution logs

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Memory Services](./memory-services.md) | Different purpose: cognitive vs transactional |
| [Knowledge Bank](./knowledge-bank.md) | Different purpose: semantic vs structured |
| [Promotion](./promotion.md) | Migrations promoted with artifacts |

---

## References

- [Data Architecture](../02-system-design/data-architecture.md)
- [ADR-0030: Three-Tier Data Architecture](../decision-logs/0030-three-tier-data-architecture.md)

