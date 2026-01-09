# Data Store Migrations

## Overview

When promoting artifacts that include data store changes, **Migration CRDs** define the schema and data transformations required at the destination. Migrations are executed as part of the deployment process.

---

## Key Principles

| Principle | Description |
|-----------|-------------|
| **Specification Only** | Only resource specifications and migrations are promoted, not data |
| **Ordered Execution** | Migrations execute in semantic version order |
| **Store-Specific** | Each data store type has its own migration CRD format |
| **Forward-Only** | Automatic rollback not supported; manual intervention required |

---

## What Gets Promoted

| Promoted | Not Promoted |
|----------|--------------|
| Data Store Resource Specification | Actual data content |
| Migration CRDs | Runtime state |
| DML Bundle references (OCI containers) | Connection credentials |

```
SOURCE WORKBENCH                       TARGET WORKBENCH
┌─────────────────────────┐           ┌─────────────────────────┐
│                         │           │                         │
│  Data Store Spec        │  ───────▶ │  Data Store Spec        │
│  ┌───────────────────┐  │  Promote  │  ┌───────────────────┐  │
│  │ ganymede-db.yaml  │  │           │  │ ganymede-db.yaml  │  │
│  └───────────────────┘  │           │  └───────────────────┘  │
│                         │           │                         │
│  Migrations             │  ───────▶ │  Migrations             │
│  ┌───────────────────┐  │  Promote  │  ┌───────────────────┐  │
│  │ v1.0.0-initial    │  │           │  │ v1.0.0-initial    │  │
│  │ v1.1.0-add-col    │  │           │  │ v1.1.0-add-col    │  │
│  │ v1.2.0-add-index  │  │           │  │ v1.2.0-add-index  │  │
│  └───────────────────┘  │           │  └───────────────────┘  │
│                         │           │           │              │
│  Data (local)           │  ✗ NOT    │           ▼              │
│  ┌───────────────────┐  │  promoted │  Execute migrations     │
│  │ [actual records]  │  │           │  at deployment time     │
│  └───────────────────┘  │           │                         │
│                         │           │                         │
└─────────────────────────┘           └─────────────────────────┘
```

---

## Migration Execution

### Ordering

Migrations execute in **semantic version order** (lowest version first):

```
Migrations in target:
├── v1.0.0-initial.yaml      ← Execute first
├── v1.1.0-add-category.yaml ← Execute second
├── v1.2.0-add-index.yaml    ← Execute third
└── v2.0.0-restructure.yaml  ← Execute fourth
```

### Execution During Deployment

```
Deployment Pipeline
       │
       ▼
┌──────────────────┐
│ Check Current    │
│ Migration State  │
└──────────────────┘
       │
       ▼
┌──────────────────┐
│ Determine        │
│ Pending          │
│ Migrations       │
└──────────────────┘
       │
       ▼
┌──────────────────┐
│ Execute          │
│ Migrations       │
│ (in order)       │
└──────────────────┘
       │
       ├─── Success ──▶ Continue Deployment
       │
       └─── Failure ──▶ Deployment Failed
                        (manual intervention)
```

### Migration State Tracking

Each workbench tracks which migrations have been applied:

```yaml
# Tracked per data store instance
migration_state:
  data_store: ganymede-dispute-db
  applied_migrations:
    - version: "1.0.0"
      applied_at: "2026-01-01T10:00:00Z"
    - version: "1.1.0"
      applied_at: "2026-01-05T14:30:00Z"
  pending_migrations:
    - version: "1.2.0"
```

---

## Data Store Specific Migrations

Each data store type has its own migration CRD contract:

### Ganymede (Relational DBaaS)

```yaml
apiVersion: hub.olympus.io/v1
kind: GanymedeMigration
metadata:
  name: dispute-db-v1-1-0
  namespace: acme-bank
spec:
  # Target data store
  data_store_ref: ganymede-dispute-db
  
  # Migration version (determines order)
  version: "1.1.0"
  
  # Migration description
  description: "Add dispute category column"
  
  # DDL operations
  ddl:
    up:
      - |
        ALTER TABLE disputes 
        ADD COLUMN category VARCHAR(50) DEFAULT 'general';
      - |
        CREATE INDEX idx_disputes_category 
        ON disputes(category);
    
    down:  # Optional: for manual rollback reference
      - "DROP INDEX idx_disputes_category;"
      - "ALTER TABLE disputes DROP COLUMN category;"
  
  # Optional: DML via OCI container
  dml:
    container:
      image: "registry.hub.acme.com/sub-001/migrations/dispute-seed:1.1.0"
      command: ["./run-dml.sh"]
    
  # Execution settings
  execution:
    timeout_seconds: 300
    transaction_mode: single  # single | per_statement
```

### Callisto (Key-Value Store)

```yaml
apiVersion: hub.olympus.io/v1
kind: CallistoMigration
metadata:
  name: cache-v1-0-0
  namespace: acme-bank
spec:
  data_store_ref: callisto-dispute-cache
  version: "1.0.0"
  description: "Initialize cache key patterns"
  
  # Callisto-specific operations
  operations:
    - type: create_key_pattern
      pattern: "dispute:{dispute_id}:status"
      ttl_seconds: 3600
    
    - type: create_key_pattern
      pattern: "user:{user_id}:disputes"
      ttl_seconds: 7200
```

### Europa (Search/Analytics)

```yaml
apiVersion: hub.olympus.io/v1
kind: EuropaMigration
metadata:
  name: search-v1-0-0
  namespace: acme-bank
spec:
  data_store_ref: europa-dispute-search
  version: "1.0.0"
  description: "Create dispute search index"
  
  # Europa-specific operations
  operations:
    - type: create_index
      index_name: disputes
      mappings:
        properties:
          dispute_id:
            type: keyword
          customer_name:
            type: text
            analyzer: standard
          amount:
            type: float
          created_at:
            type: date
```

---

## DML Bundles

For complex data seeding or transformation, migrations can reference **OCI containers** containing data bundles:

### Use Cases

| Use Case | Example |
|----------|---------|
| **Seed Data** | Reference data, lookup tables |
| **Data Transformation** | Complex ETL scripts |
| **Test Data** | Fixtures for testing environments |

### DML Container Structure

```
dml-container/
├── Dockerfile
├── run-dml.sh          # Entry point
├── data/
│   ├── categories.csv
│   └── lookup-codes.json
└── scripts/
    └── import.py
```

### Container Execution

```yaml
dml:
  container:
    image: "registry.hub.acme.com/sub-001/migrations/seed-data:1.0.0"
    command: ["./run-dml.sh"]
    env:
      - name: TARGET_DB
        value_from:
          secret_ref: db-connection
    resources:
      memory: 512Mi
      cpu: 500m
```

### Who Builds DML Containers?

| Actor | Responsibility |
|-------|----------------|
| **Developer** | Create and build DML containers |
| **CI System** | Build and push to snapshot registry |
| **Promotion** | Copy to production registry with scenario |

---

## Failure Handling

### Migration Failure

| Scenario | Behavior |
|----------|----------|
| DDL fails | Deployment marked as FAILED |
| DML fails | Deployment marked as FAILED |
| Timeout | Deployment marked as FAILED |
| Partial completion | State recorded; manual fix required |

### Recovery Process

```
Migration Failure
       │
       ▼
┌──────────────────┐
│ Deployment       │
│ Marked FAILED    │
└──────────────────┘
       │
       ▼
┌──────────────────┐
│ Admin/Developer  │
│ Investigates     │
└──────────────────┘
       │
       ├─── Fix migration script ──▶ Re-promote with fixed version
       │
       └─── Manual database fix ──▶ Mark migration as applied
                                    └──▶ Retry deployment
```

### No Automatic Rollback

> **Important:** Data store migrations do not automatically rollback. The `down` scripts in migrations are for **documentation and manual reference only**.

---

## Best Practices

### DO

| Practice | Rationale |
|----------|-----------|
| **Backward-compatible changes** | Allows staged rollout |
| **Small, incremental migrations** | Easier to debug failures |
| **Test migrations in DEV/STAGING** | Catch issues before PROD |
| **Include rollback scripts (docs)** | Enables manual recovery |
| **Version DML containers with migrations** | Ensures consistency |

### DON'T

| Anti-pattern | Issue |
|--------------|-------|
| Large monolithic migrations | Hard to debug, long execution |
| Data-dependent DDL | May fail on different data |
| Assumptions about data state | Different per environment |
| Skip versioning | Execution order undefined |

---

## Migration CRD Placement

Migrations are stored with their associated Scenario:

```
workbenches/
└── dispute-ops-dev/
    └── scenarios/
        └── standard-dispute/
            └── migrations/
                ├── v1.0.0-initial.yaml
                ├── v1.1.0-add-category.yaml
                └── v1.2.0-add-index.yaml
```

### Shared Data Store Migrations

For subscription-scoped data stores, migrations go in `_shared/`:

```
_shared/
└── data-stores/
    └── ganymede-shared-db/
        ├── data-store.yaml
        └── migrations/
            ├── v1.0.0-initial.yaml
            └── v1.1.0-schema-update.yaml
```

---

## Related Documentation

- [Promotion Model](./promotion-model.md) — How migrations are promoted
- [Data Architecture](../../03-architecture/data-architecture.md) — Data store concepts
- [Admin Operators](../operators/admin-operators.md) — Data store CRDs


