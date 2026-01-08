# Europa — OpenSearch/ELK-as-a-Service

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-08

## Overview

**Europa** is Zeta's managed OpenSearch service (AWS OpenSearch with vector support), providing full-text search, analytics, vector/semantic search, and log aggregation capabilities for Hub Applications.

---

## Purpose in Olympus Hub

Europa provides:

- **Full-Text Search** — Natural language search across documents
- **Vector/Semantic Search** — k-NN plugin for embedding-based similarity search
- **Analytics** — Aggregations, metrics, and reporting
- **Log Aggregation** — Application and operational logs
- **Complex Queries** — Faceted search, filters, rankings
- **Enterprise Memory** — Episodic, Semantic, Procedural, Preference memory stores
- **Agent Memory** — Log, Conversation, and Document storage with RAG

---

## When to Use Europa

| Use Case | Recommendation |
|----------|----------------|
| Full-text search | ✅ Use Europa |
| Log analytics | ✅ Use Europa |
| Complex aggregations | ✅ Use Europa |
| Faceted search | ✅ Use Europa |
| **Vector/semantic search (RAG)** | ✅ Use Europa (k-NN) |
| **Enterprise Memory stores** | ✅ Use Europa |
| **Agent Memory Log/Conversation/Docs** | ✅ Use Europa + S3 |
| Simple key-value | ❌ Use Callisto |
| Transactional data | ❌ Use Ganymede |
| Primary data store | ❌ Use Ganymede |

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                   Europa Service                     │
│                                                      │
│  ┌─────────────┐   ┌─────────────┐                  │
│  │  Provisioner │   │ Index Mgmt  │                  │
│  └─────────────┘   └─────────────┘                  │
│                                                      │
│  ┌───────────────────────────────────────────────┐  │
│  │           OpenSearch Cluster                  │  │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐       │  │
│  │  │ Master  │  │  Data   │  │  Data   │       │  │
│  │  │  Node   │  │  Node   │  │  Node   │       │  │
│  │  └─────────┘  └─────────┘  └─────────┘       │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## Workbench Integration

### Provisioning

```yaml
workbench:
  name: disputes
  application_data_stores:
    europa:
      enabled: true
      indices:
        - name: dispute-documents
          mappings:
            properties:
              dispute_id: { type: keyword }
              description: { type: text, analyzer: standard }
              amount: { type: float }
              status: { type: keyword }
              created_at: { type: date }
```

### Access

Hub Applications access Europa via SDK:

```python
from europa import EuropaClient

client = EuropaClient.from_environment()

# Index a document
client.index(
    index="dispute-documents",
    id=dispute_id,
    document={
        "dispute_id": dispute_id,
        "description": dispute.description,
        "amount": dispute.amount,
        "status": dispute.status,
        "created_at": dispute.created_at
    }
)

# Search documents
results = client.search(
    index="dispute-documents",
    query={
        "bool": {
            "must": [
                {"match": {"description": "unauthorized transaction"}},
                {"term": {"status": "OPEN"}}
            ]
        }
    }
)
```

---

## Example Usage

### Full-Text Search

```python
# Search disputes by description
def search_disputes(query_text, status_filter=None):
    query = {
        "bool": {
            "must": [
                {"match": {"description": query_text}}
            ]
        }
    }
    
    if status_filter:
        query["bool"]["filter"] = [
            {"term": {"status": status_filter}}
        ]
    
    return europa.search(
        index="dispute-documents",
        query=query,
        size=50
    )
```

### Analytics Aggregations

```python
# Aggregate dispute amounts by status
def dispute_summary():
    return europa.search(
        index="dispute-documents",
        size=0,
        aggs={
            "by_status": {
                "terms": {"field": "status"},
                "aggs": {
                    "total_amount": {"sum": {"field": "amount"}},
                    "avg_amount": {"avg": {"field": "amount"}}
                }
            }
        }
    )
```

---

## Index Management

### Index Lifecycle

- **Creation** — Indices created from Workbench definition
- **Mapping Updates** — Via Workbench configuration changes
- **Reindexing** — Automated for breaking changes
- **Deletion** — On workbench cleanup

### Index Naming

```
<tenant>-<workbench>-<index-name>-<version>
```

Example: `acme-disputes-dispute-documents-v1`

---

## Features

| Feature | Description |
|---------|-------------|
| **Full-Text Search** | Natural language query parsing |
| **Vector Search (k-NN)** | Embedding-based similarity search for RAG |
| **Aggregations** | Metrics, buckets, pipelines |
| **Analyzers** | Standard, language-specific, custom |
| **Highlighting** | Search result highlighting |
| **Suggestions** | Autocomplete, did-you-mean |
| **Tiered Storage** | Hot (OpenSearch) + Cold (S3) with time-based cutoff |

---

## Vector Search (k-NN)

Europa supports semantic/vector search via OpenSearch k-NN plugin:

### Configuration

```yaml
indices:
  - name: agent-session-logs
    settings:
      index.knn: true
    mappings:
      properties:
        content:
          type: text
        embedding:
          type: knn_vector
          dimension: 1536  # Model-specific
          method:
            name: hnsw
            engine: nmslib
            parameters:
              ef_construction: 128
              m: 16
```

### Query

```python
# Semantic search
results = europa.search(
    index="agent-session-logs",
    query={
        "knn": {
            "embedding": {
                "vector": query_embedding,
                "k": 10
            }
        }
    }
)
```

### Embedding Generation

| Aspect | Configuration |
|--------|---------------|
| **Default** | Synchronous on write |
| **Async Option** | Configurable per workbench |
| **Model** | Hub framework-provided (Olympus embedding service) |

---

## Performance Characteristics

| Metric | Target |
|--------|--------|
| Search Latency (p99) | < 100ms |
| Indexing Latency | < 1s (async) |
| Query Throughput | 1K queries/sec per node |

---

## Tenant Isolation

- **Index Isolation** — Separate indices per workbench
- **Index Prefix** — Tenant/workbench prefix enforced
- **Access Control** — Credentials scoped to indices
- **Resource Quotas** — Storage and query limits

---

## Monitoring

Europa exposes metrics to Olympus Watch:

- `europa_search_latency_seconds` — Query latency
- `europa_index_rate` — Documents indexed per second
- `europa_storage_bytes` — Index storage usage
- `europa_query_count` — Queries per index

---

## Tiered Storage (S3)

For long-running sessions and archival, Europa integrates with S3 for tiered storage:

### Configuration

```yaml
tiered_storage:
  enabled: true
  hot_tier:
    storage: opensearch
    retention_hours: 24  # Configurable per workbench
  cold_tier:
    storage: s3
    bucket: olympus-europa-cold-{tenant}
    lifecycle:
      transition_days: 1
      expiration_days: 30  # Session + retention period
```

### Tiering Model

```
┌─────────────────────────────────────────────────────────────────┐
│                      TIERED STORAGE                              │
│                                                                   │
│   ┌─────────────────────────────┐                                │
│   │        HOT TIER             │ ◄── Recent data               │
│   │   OpenSearch (Europa)       │     (configurable hours)       │
│   │   - Fast query access       │                                │
│   │   - k-NN vector search      │                                │
│   └──────────────┬──────────────┘                                │
│                  │ Time-based cutoff                             │
│                  ▼                                                │
│   ┌─────────────────────────────┐                                │
│   │        COLD TIER            │ ◄── Older data                │
│   │         S3                  │     (archived)                 │
│   │   - Cost-effective          │                                │
│   │   - Compliance retention    │                                │
│   └─────────────────────────────┘                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## Memory Services Integration

Europa serves as the storage backend for Hub Memory Services:

### Enterprise Memory

| Memory Class | Index Pattern | Features |
|--------------|---------------|----------|
| **Episodic** | `{tenant}_{workbench}_episodic_{type}` | Immutable, 7+ year retention |
| **Semantic** | `{tenant}_{workbench}_semantic_{type}` | Evidence-grounded beliefs |
| **Procedural** | `{tenant}_{workbench}_procedural_{type}` | Learned skills and procedures |
| **Preference** | `{tenant}_{workbench}_preference_{type}` | User and agent preferences |

### Agent Memory

| Service | Storage | Features |
|---------|---------|----------|
| **Log Service** | Europa + S3 tiered | Append-only, RAG search |
| **Conversation Service** | Europa + S3 tiered | Compaction, token budgets |
| **Document Storage** | Europa + S3 | Vector search, content-addressable |

### Agent Memory Requirements

| Requirement | Expectation |
|-------------|-------------|
| **Isolation** | Per (tenant, workbench, scenario, request, agent) |
| **Encryption** | Values encrypted at application layer |
| **Embeddings** | Synchronous on write (default), async optional |
| **TTL** | Session + retention period (configurable) |
| **Tiering** | Time-based hot/cold transition |

### Agent Memory Index Pattern

```
{tenant}_{workbench}_{scenario}_{request_id}_{agent_id}_{service}
```

---

## Related Documentation

- [Application Data Stores](../07-data-architecture/application-data-stores.md) — Overview
- [Storage FAQ](../07-data-architecture/storage-faq.md) — Common questions
- [Ganymede](./ganymede-rdbms.md) — Relational alternative
- [Callisto](./callisto-kv-store.md) — Key-Value alternative
- [Olympus Watch](./olympus-watch.md) — Log aggregation
- [Memory Services](../04-subsystems/memory-services/README.md) — Hub Memory Services overview
- [Enterprise Memory](../04-subsystems/memory-services/enterprise-memory/README.md) — Organizational memory
- [Agent Memory](../04-subsystems/memory-services/agent-memory/README.md) — Session-scoped agent memory
- [Agent Memory Storage Services](../04-subsystems/memory-services/agent-memory/storage-services.md) — Detailed specification
- [ADR-0071: Agent Memory Storage Backends](../decision-logs/0071-agent-memory-storage-backends.md) — Storage decisions

---

## References

- [OpenSearch Documentation](https://opensearch.org/docs/latest/)
- [OpenSearch k-NN Plugin](https://opensearch.org/docs/latest/search-plugins/knn/index/) — Vector search
- [Olympus Academy: Europa](https://academy.olympus.tech/europa) — Full documentation

