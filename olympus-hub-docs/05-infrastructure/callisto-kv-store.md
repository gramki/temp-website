# Callisto — Key-Value Store

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-08

## Overview

**Callisto** is Zeta's managed Key-Value Store service built on **MongoDB**, providing high-performance, low-latency data access for Hub Applications that need simple key-based lookups or session state storage.

---

## Purpose in Olympus Hub

Callisto provides:

- **Entity State Cache** — Fast access to entity snapshots
- **Session State** — Application-specific session data
- **Configuration Cache** — Runtime configuration storage
- **Materialized Views** — Denormalized data for fast reads
- **Agent Memory KV Store** — Session-scoped key-value storage for AI agents

---

## When to Use Callisto

| Use Case | Recommendation |
|----------|----------------|
| Simple key-value lookups | ✅ Use Callisto |
| Session state persistence | ✅ Use Callisto |
| Entity state cache | ✅ Use Callisto |
| **Agent Memory KV Store** | ✅ Use Callisto |
| Structured queries | ❌ Use Ganymede |
| Full-text search | ❌ Use Europa |
| Complex relationships | ❌ Use Ganymede |
| Semantic/vector search | ❌ Use Europa |

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Callisto Service                    │
│                                                      │
│  ┌─────────────┐   ┌─────────────┐                  │
│  │  Provisioner │   │  Key Router  │                  │
│  └─────────────┘   └─────────────┘                  │
│                                                      │
│  ┌───────────────────────────────────────────────┐  │
│  │           Distributed KV Cluster              │  │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐       │  │
│  │  │ Node 1  │  │ Node 2  │  │ Node 3  │       │  │
│  │  └─────────┘  └─────────┘  └─────────┘       │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## Data Model

### Key Structure

Keys follow a hierarchical pattern:

```
<tenant>/<workbench>/<namespace>/<entity-type>/<entity-id>
```

Example:
```
acme/disputes/dispute-app/transaction-dispute/disp-12345
```

### Value Format

Values can be:
- **JSON** — Structured documents
- **Binary** — Serialized objects
- **String** — Simple text values

---

## Workbench Integration

### Provisioning

```yaml
workbench:
  name: disputes
  application_data_stores:
    callisto:
      enabled: true
      namespaces:
        - dispute-cache
        - session-state
```

### Access

Hub Applications access Callisto via SDK:

```python
from callisto import CallistoClient

client = CallistoClient.from_environment()

# Store entity state
client.put(
    namespace="dispute-cache",
    key=f"dispute/{dispute_id}",
    value=dispute_state,
    ttl=3600  # Optional TTL
)

# Retrieve entity state
dispute = client.get(
    namespace="dispute-cache",
    key=f"dispute/{dispute_id}"
)
```

---

## Example Usage

### Entity State Cache

```python
# Cache dispute entity for fast access
def cache_dispute_state(dispute):
    callisto.put(
        namespace="dispute-cache",
        key=f"dispute/{dispute.id}",
        value={
            "status": dispute.status,
            "amount": dispute.amount,
            "last_updated": dispute.updated_at.isoformat()
        }
    )

# Retrieve cached state
def get_dispute_state(dispute_id):
    return callisto.get(
        namespace="dispute-cache",
        key=f"dispute/{dispute_id}"
    )
```

### Session State

```python
# Store session-specific data
def save_session_context(request_id, context):
    callisto.put(
        namespace="session-state",
        key=f"request/{request_id}/context",
        value=context,
        ttl=86400  # 24 hours
    )
```

---

## Features

| Feature | Description |
|---------|-------------|
| **TTL** | Optional expiration for keys |
| **Atomic Operations** | CAS (Compare-and-Swap) |
| **Batch Operations** | Multi-get, multi-put |
| **Prefix Scan** | List keys by prefix |

---

## Performance Characteristics

| Metric | Target |
|--------|--------|
| Read Latency (p99) | < 5ms |
| Write Latency (p99) | < 10ms |
| Throughput | 100K ops/sec per node |

---

## Tenant Isolation

- **Namespace Isolation** — Each workbench gets isolated namespaces
- **Key Prefix** — Tenant/workbench prefix enforced
- **Access Control** — Credentials scoped to workbench
- **Quota Management** — Storage limits per workbench

---

## Monitoring

Callisto exposes metrics to Olympus Watch:

- `callisto_operations_total` — Operation count by type
- `callisto_latency_seconds` — Operation latency
- `callisto_storage_bytes` — Storage usage
- `callisto_cache_hit_ratio` — Cache effectiveness

---

## Agent Memory Services

Callisto serves as the storage backend for **Agent Memory KV Store**:

### Requirements

| Requirement | Expectation |
|-------------|-------------|
| **Isolation** | Per (tenant, workbench, scenario, request, agent) |
| **Encryption** | Values encrypted at application layer before storage |
| **TTL** | Automatic cleanup after session + retention period |
| **Logical Stores** | Multiple stores per agent (e.g., `preferences`, `entities`) |
| **Quota** | Storage limits per agent/request (configurable) |

### Key Pattern for Agent Memory

```
<tenant>/<workbench>/<scenario>/<request_id>/<agent_id>/<store_name>/<key>
```

### Operations

| Operation | Description | Latency Target |
|-----------|-------------|----------------|
| `put(store, key, value)` | Store encrypted value | < 10ms |
| `get(store, key)` | Retrieve and return (encrypted) | < 5ms |
| `delete(store, key)` | Remove key | < 10ms |
| `list(store)` | List keys in store | < 20ms |

### Lifecycle Integration

- **Provisioning**: Stores auto-provisioned on first access
- **Cleanup**: TTL-based expiration (session + retention period)
- **Monitoring**: Metrics to Olympus Watch per agent/request

See [Agent Memory Services](../04-subsystems/memory-services/agent-memory/README.md) for full specification.

---

## Related Documentation

- [Application Data Stores](../07-data-architecture/application-data-stores.md) — Overview
- [Storage FAQ](../07-data-architecture/storage-faq.md) — Common questions
- [Ganymede](./ganymede-rdbms.md) — Relational alternative
- [Europa](./europa-opensearch.md) — Search/analytics alternative
- [Agent Memory Services](../04-subsystems/memory-services/agent-memory/README.md) — KV Store use case
- [Agent Memory Storage Services](../04-subsystems/memory-services/agent-memory/storage-services.md) — Detailed specification
- [ADR-0071: Agent Memory Storage Backends](../decision-logs/0071-agent-memory-storage-backends.md) — Storage decisions

---

## References

- [Olympus Academy: Callisto](https://academy.olympus.tech/callisto) — Full documentation
- [MongoDB Documentation](https://docs.mongodb.com/) — Underlying technology

