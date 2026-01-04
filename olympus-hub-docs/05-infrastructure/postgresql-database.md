# PostgreSQL — Relational Database

> **Status:** 🔴 Stub — Placeholder for expansion

## Overview

**PostgreSQL** serves as the primary relational database for Olympus Hub's control plane and operational data stores, providing ACID-compliant transactional storage.

---

## Purpose in Olympus Hub

PostgreSQL stores:

- **System Metadata** — Hub configuration, schemas, definitions
- **Operational Data** — Request logs, task records, signal history
- **Control Plane State** — Workbench, Scenario, Trigger definitions
- **Audit Records** — Operational audit logs (via Cipher Audit Service)

---

## Database Topology

### System Databases

| Database | Purpose | Owner |
|----------|---------|-------|
| `hub_system` | Platform configuration | Hub Core |
| `hub_operations` | Operational data | Signal Exchange |
| `hub_audit` | Audit records | Cipher Audit |
| `temporal` | Temporal persistence | ChronoShift |

### Tenant Databases

Per-tenant databases for workbench isolation:

```
hub_tenant_<tenant_id>_<workbench_id>
```

---

## Schema Design Principles

### Multi-Tenancy

- **Database-per-Workbench** — Complete isolation
- **Row-Level Security** — Where shared databases are used
- **Tenant ID Column** — On all tenant-scoped tables

### Partitioning

Time-series data uses table partitioning:

```sql
CREATE TABLE hub_requests (
    request_id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ NOT NULL,
    ...
) PARTITION BY RANGE (created_at);
```

---

## Core Tables

### System Tables

| Table | Purpose |
|-------|---------|
| `tenants` | Tenant subscriptions |
| `workbenches` | Workbench definitions |
| `scenarios` | Scenario configurations |
| `triggers` | Trigger definitions |
| `applications` | Hub Application registry |

### Operational Tables

| Table | Purpose |
|-------|---------|
| `requests` | Request records |
| `request_updates` | Request update history |
| `tasks` | Task records |
| `task_assignments` | Task assignment history |
| `signals` | Signal log |

---

## High Availability

```
┌─────────────────────────────────────────────────────┐
│                PostgreSQL Cluster                    │
│                                                      │
│  ┌─────────────┐   ┌─────────────┐                  │
│  │   Primary   │──►│   Replica   │                  │
│  │   (RW)      │   │   (RO)      │                  │
│  └─────────────┘   └─────────────┘                  │
│         │                 │                          │
│         ▼                 ▼                          │
│  ┌─────────────────────────────────┐                │
│  │     Shared Storage (EBS)         │                │
│  └─────────────────────────────────┘                │
└─────────────────────────────────────────────────────┘
```

- **Streaming Replication** — Synchronous to replica
- **Automatic Failover** — Patroni/pg_auto_failover
- **Connection Pooling** — PgBouncer for connection management

---

## Backup Strategy

| Type | Frequency | Retention |
|------|-----------|-----------|
| Full Backup | Daily | 30 days |
| WAL Archiving | Continuous | 7 days |
| Point-in-Time Recovery | Available | 7 days |

---

## Performance Tuning

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| `shared_buffers` | 25% RAM | Memory allocation |
| `effective_cache_size` | 75% RAM | Query planner hints |
| `work_mem` | 256MB | Sort/hash operations |
| `maintenance_work_mem` | 1GB | Vacuum, index creation |

---

## Connection Management

- **PgBouncer** — Connection pooling
- **Pool Mode** — Transaction pooling
- **Max Connections** — 200 per service
- **Idle Timeout** — 10 minutes

---

## Monitoring

Metrics exported to Olympus Watch:

- `pg_stat_activity` — Active connections, queries
- `pg_stat_database` — Transaction rates, cache hit ratio
- `pg_stat_user_tables` — Table statistics
- `pg_replication_lag` — Replication delay

---

## Security

- **TLS** — Encrypted connections required
- **Role-Based Access** — Per-service database users
- **Row-Level Security** — Tenant data isolation
- **Audit Logging** — pgAudit extension

---

## Related Documentation

- [Storage Architecture](../07-data-architecture/storage-architecture.md) — Data architecture overview
- [Ganymede](./ganymede-rdbms.md) — Relational DBaaS for applications
- [Temporal Cluster](./temporal-cluster.md) — Temporal persistence

---

*Expand this document with schema designs, migration procedures, and operational runbooks.*

