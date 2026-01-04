# Ganymede — Relational DBaaS

> **Status:** 🔴 Stub — Placeholder for expansion

## Overview

**Ganymede** is Zeta's Relational Database-as-a-Service (DBaaS) offering, providing managed relational databases through the Olympus Platform. Hub uses Ganymede both internally for operational data and exposes it to Hub Applications for business entity storage.

---

## Purpose in Olympus Hub

Ganymede provides:

- **Hub Operational Data** — System metadata, request logs, task records, signal history
- **Control Plane State** — Workbench, Scenario, Trigger definitions
- **Application Data Storage** — Structured business entity persistence for Hub Applications
- **DDL Management** — Schema lifecycle integrated with Workbench definitions
- **Tenant Isolation** — Per-workbench database instances
- **Managed Operations** — Automated backups, scaling, and maintenance

---

## Hub Internal vs Application Usage

| Usage | Scope | Owner |
|-------|-------|-------|
| **Hub System Data** | Platform-wide | Hub Core |
| **Hub Operational Data** | Per-workbench | Signal Exchange, Request Management |
| **Application Data** | Per-workbench | Hub Applications |

Hub itself is a consumer of Ganymede — it does **not** directly manage PostgreSQL instances.

---

## When to Use Ganymede

| Use Case | Recommendation |
|----------|----------------|
| Business entities with relationships | ✅ Use Ganymede |
| Complex queries with joins | ✅ Use Ganymede |
| Transactional operations | ✅ Use Ganymede |
| Simple key-value lookups | ❌ Use Callisto |
| Full-text search | ❌ Use Europa |
| Session cache | ❌ Use Callisto |

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Ganymede Service                    │
│                                                      │
│  ┌─────────────┐   ┌─────────────┐                  │
│  │  Provisioner │   │  DDL Manager │                  │
│  └─────────────┘   └─────────────┘                  │
│                                                      │
│  ┌───────────────────────────────────────────────┐  │
│  │            Managed PostgreSQL Pool            │  │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐       │  │
│  │  │ Tenant A│  │ Tenant B│  │ Tenant C│       │  │
│  │  │  WB-1   │  │  WB-1   │  │  WB-2   │       │  │
│  │  └─────────┘  └─────────┘  └─────────┘       │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## Workbench Integration

### Provisioning

When a Workbench is created with Ganymede enabled:

1. Ganymede provisions a new database instance
2. Connection credentials generated and stored in Hub secrets
3. Database URL provided to Hub Applications

### DDL Lifecycle

Schema definitions are part of Workbench configuration:

```yaml
workbench:
  name: disputes
  application_data_stores:
    ganymede:
      enabled: true
      ddl:
        - version: 1
          script: |
            CREATE TABLE transaction_disputes (
              dispute_id UUID PRIMARY KEY,
              transaction_id UUID NOT NULL,
              status VARCHAR(50),
              amount DECIMAL(15,2),
              created_at TIMESTAMPTZ DEFAULT NOW()
            );
        - version: 2
          script: |
            ALTER TABLE transaction_disputes 
            ADD COLUMN resolution_notes TEXT;
```

---

## Example Usage

### Dispute Application

```python
# Hub Application accessing Ganymede
import psycopg2

def create_dispute(dispute_data):
    conn = get_ganymede_connection()  # From Hub environment
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO transaction_disputes 
            (dispute_id, transaction_id, status, amount)
            VALUES (%s, %s, %s, %s)
        """, (
            dispute_data['id'],
            dispute_data['transaction_id'],
            'OPENED',
            dispute_data['amount']
        ))
    conn.commit()
```

---

## Access Patterns

Hub Applications access Ganymede through:

- **Connection String** — Provided via environment variables
- **SDK** — Ganymede client SDK with connection pooling
- **ORM** — Compatible with SQLAlchemy, TypeORM, etc.

---

## Data Lifecycle

| Phase | Owner | Action |
|-------|-------|--------|
| Schema Creation | Workbench Admin | DDL in Workbench definition |
| Data Operations | Hub Application | DML via application code |
| Schema Migration | Workbench Admin | DDL version upgrade |
| Cleanup | Hub System | On workbench deletion |

---

## Tenant Isolation

- **Separate Databases** — Each workbench gets dedicated database
- **Network Isolation** — VPC-level separation
- **Credential Isolation** — Unique credentials per workbench
- **Resource Isolation** — Compute/storage quotas per tenant

---

## Monitoring

Ganymede exposes metrics to Olympus Watch:

- `ganymede_connections_active`
- `ganymede_query_duration_seconds`
- `ganymede_storage_bytes`
- `ganymede_transactions_per_second`

---

## Related Documentation

- [Application Data Stores](../07-data-architecture/application-data-stores.md) — Overview
- [Storage FAQ](../07-data-architecture/storage-faq.md) — Common questions
- [Callisto](./callisto-kv-store.md) — Key-Value alternative
- [Europa](./europa-opensearch.md) — Search/analytics alternative

---

## References

- [Olympus Academy: Ganymede](https://academy.olympus.tech/ganymede) — Full documentation

---

*Expand this document with detailed DDL management, migration procedures, and SDK usage.*

