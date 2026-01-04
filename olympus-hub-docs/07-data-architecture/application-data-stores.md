# Application Data Stores

> **Status:** 🔴 Stub — Placeholder for expansion

Application Data Stores are workbench-scoped data stores that Hub Applications use to persist business domain entities. Unlike Operations Data (Hub-managed) and Cognitive Services (Memory/Knowledge), Application Data Stores are directly accessed and managed by applications.

---

## Overview

| Aspect | Description |
|--------|-------------|
| **Purpose** | Persist business domain entities for Hub Applications |
| **Scope** | Workbench-scoped |
| **Lifecycle** | Tied to Workbench Definition lifecycle |
| **Provisioning** | By Tenant Admins as part of workbench activation |
| **Access** | Direct access by Hub Applications |
| **Isolation** | Tenant-isolated |

---

## Available Services

| Service | Type | Platform | Use Cases |
|---------|------|----------|-----------|
| **Ganymede** | Relational DBaaS | PostgreSQL-compatible | Business entities, complex relationships, transactions, SQL queries |
| **Callisto** | Key-Value Store | Distributed KV | Entity state, caching, fast lookups, flexible schemas |
| **Europa** | Search/Analytics | OpenSearch (ELK) | Full-text search, log aggregation, metrics, analytics |

---

## Ganymede — Relational DBaaS

**Description:** Ganymede provides a complete solution for managing relational databases, offering Database as a Service (DBaaS) with provisioning, lifecycle management, DDL execution, and monitoring.

**When to use:**
- Business entities with complex relationships
- Transactional integrity requirements (ACID)
- Complex queries with joins and aggregations
- Referential integrity constraints
- Reporting and analytics on structured data

**Examples:**
- Transaction Dispute entity with state machine
- Customer profiles with relationships
- Order management with line items

**Reference:** [Ganymede Documentation](https://jupiter.olympus.tech/ganymede/)

---

## Callisto — Key-Value Store (Optional)

**Description:** Callisto is a key-value store that offers services to store and access any data with ease. It provides flexible, schema-less storage with fast access patterns.

**Note:** Callisto usage is **optional**. Not every application needs key-value storage. Developers choose to use Callisto based on their specific business logic requirements.

**When to use:**
- Fast entity lookups by key
- Caching entity state
- Session data (when application-specific session state is needed)
- Flexible/evolving schemas
- High-throughput, low-latency access

**Examples:**
- Dispute status cache for real-time UI
- Application-specific session state (e.g., wizard progress, temp calculations)
- Feature flags per entity

**Reference:** [Callisto Documentation](https://jupiter.olympus.tech/callisto/)

---

## Europa — Search and Analytics

**Description:** Europa is an ELK-as-a-Service platform built on OpenSearch (formerly Elasticsearch). It provides centralized search, log aggregation, and analytics capabilities.

**When to use:**
- Full-text search across entities
- Log aggregation and analysis
- Time-series data and metrics
- Analytics dashboards
- Audit trail searchability

**Examples:**
- Searchable dispute history
- Application logs and metrics
- Compliance audit logs
- Analytics on dispute resolution patterns

**Configuration:**
- 30 days retention for log indices
- 90 days retention for application indices
- Daily automated S3 snapshots

**Reference:** Europa internal documentation

---

## Lifecycle Integration

Application Data Stores are integrated into the Workbench Definition lifecycle:

### 1. Definition (Process Architect / Developer)

```yaml
workbench:
  id: "dispute-resolution"
  version: "1.2.0"
  
  application_data_stores:
    - name: "dispute_entities"
      type: "ganymede"
      ddl_path: "./ddl/v1.2/dispute-entities.sql"
      
    - name: "dispute_cache"
      type: "callisto"
      collection: "dispute-states"
      ttl_seconds: 3600
      
    - name: "dispute_search"
      type: "europa"
      index_template: "./indices/dispute-index.json"
      retention_days: 90
```

### 2. Provisioning (Tenant Admin)

When a workbench is activated:
1. Tenant Admin approves resource allocation
2. Hub provisions data stores via Olympus platform APIs
3. DDL is executed (Ganymede)
4. Collections/indices are created (Callisto/Europa)
5. Connection credentials are secured in Vault

### 3. Schema Evolution (Developer)

When workbench definition is updated:
1. New DDL migration files are added
2. Version increment triggers migration
3. Ganymede executes DDL migrations
4. Callisto/Europa configurations are updated
5. Rollback supported for failed migrations

### 4. Decommissioning

When a workbench is deactivated:
1. Data retention policies apply
2. Archives created per compliance requirements
3. Resources are deallocated

---

## Access Patterns

| Actor | Access |
|-------|--------|
| Hub Applications | Read/Write (via application code) |
| Developers | DDL management, debugging |
| Tenant Admins | Provisioning, monitoring |
| Platform Operators | Support, capacity management |

---

## Isolation

All Application Data Stores are tenant-isolated:

| Level | Mechanism |
|-------|-----------|
| **Tenant** | Separate namespaces/schemas per tenant |
| **Workbench** | Separate databases/collections/indices per workbench |
| **Network** | Private connectivity within tenant's network boundary |
| **Credentials** | Per-workbench credentials in Vault |

---

## When NOT to Use Application Data Stores

| Data Type | Use Instead | Reason |
|-----------|-------------|--------|
| Decisions, rationale | Enterprise Memory (via CAF) | Requires audit semantics |
| User preferences | User Memory | Requires decay/governance |
| Agent learning | Agent Memory | Requires Hub integration |
| Policies, rules | Knowledge Services | Requires curation workflow |
| Hub operational data | Operations Data (via Hub APIs) | Hub-managed lifecycle |

---

## Related Documentation

- [Storage Architecture](./storage-architecture.md) — Overall storage model and selection guide
- [Workbench Management](../04-subsystems/workbench-management/README.md) — Workbench lifecycle
- [Memory Services](../04-subsystems/memory-services/README.md) — Agent and Enterprise Memory
- [Knowledge Services](../04-subsystems/knowledge-services/README.md) — Knowledge Bank

---

*TODO: Detailed design — provisioning APIs, DDL migration patterns, monitoring, quota management*

