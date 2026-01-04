# Europa — OpenSearch/ELK-as-a-Service

> **Status:** 🔴 Stub — Placeholder for expansion

## Overview

**Europa** is Zeta's managed OpenSearch service (formerly Elasticsearch), providing full-text search, analytics, and log aggregation capabilities for Hub Applications.

---

## Purpose in Olympus Hub

Europa provides:

- **Full-Text Search** — Natural language search across documents
- **Analytics** — Aggregations, metrics, and reporting
- **Log Aggregation** — Application and operational logs
- **Complex Queries** — Faceted search, filters, rankings

---

## When to Use Europa

| Use Case | Recommendation |
|----------|----------------|
| Full-text search | ✅ Use Europa |
| Log analytics | ✅ Use Europa |
| Complex aggregations | ✅ Use Europa |
| Faceted search | ✅ Use Europa |
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
| **Aggregations** | Metrics, buckets, pipelines |
| **Analyzers** | Standard, language-specific, custom |
| **Highlighting** | Search result highlighting |
| **Suggestions** | Autocomplete, did-you-mean |

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

## Related Documentation

- [Application Data Stores](../07-data-architecture/application-data-stores.md) — Overview
- [Storage FAQ](../07-data-architecture/storage-faq.md) — Common questions
- [Ganymede](./ganymede-rdbms.md) — Relational alternative
- [Callisto](./callisto-kv-store.md) — Key-Value alternative
- [Olympus Watch](./olympus-watch.md) — Log aggregation

---

## References

- [OpenSearch Documentation](https://opensearch.org/docs/latest/)
- [Olympus Academy: Europa](https://academy.olympus.tech/europa) — Full documentation

---

*Expand this document with mapping strategies, query optimization, and operational procedures.*

