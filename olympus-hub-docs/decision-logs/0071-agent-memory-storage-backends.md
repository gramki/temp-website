# ADR-0071: Agent Memory Storage Backends

> **Status**: Accepted  
> **Date**: 2026-01-08  
> **Category**: memory-services

---

## Context

Agent Memory Services requires storage backends for four services:
1. **KV Store** — Key-value operations for entities, preferences, state
2. **Log Service** — Append-only session history with RAG search
3. **Conversation Service** — Chat context with compaction and RAG
4. **Document Storage** — Files and BLOBs with vector search

### Considerations

1. **Access Patterns**: KV needs low-latency CRUD; Log/Conversation/Documents need search
2. **Session Scope**: All storage is ephemeral (session + retention period)
3. **RAG Requirements**: Log, Conversation, and Documents need semantic search
4. **Cost Efficiency**: Session data should tier to cheaper storage over time
5. **Platform Consistency**: Use Olympus platform services where possible

### Olympus Platform Services

| Service | Technology | Strengths |
|---------|-----------|-----------|
| **Olympus Callisto** | MongoDB | Low-latency CRUD, document model, indexing |
| **Olympus Europa** | OpenSearch | Full-text search, k-NN vectors, aggregations |
| **S3** | Object Storage | Cost-effective archival, durability |

---

## Decision

**Mixed backend strategy** — use the right Olympus service for each access pattern:

| Service | Primary Backend | Tiered Storage | Rationale |
|---------|----------------|----------------|-----------|
| **KV Store** | Olympus Callisto (MongoDB) | None | Low-latency CRUD, document model fits KV |
| **Log Service** | Olympus Europa (OpenSearch) | S3 (time-based) | RAG search, archival to S3 |
| **Conversation Service** | Olympus Europa (OpenSearch) | S3 (time-based) | RAG search, compaction, archival |
| **Document Storage** | Olympus Europa (OpenSearch) | S3 (content) | Vector search, S3 for BLOBs |

### Tiered Storage Model

For Log and Conversation services:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        TIERED STORAGE                                        │
│                                                                               │
│   ┌───────────────────────────────────┐                                      │
│   │        HOT TIER                   │                                      │
│   │     Olympus Europa                │ ◄── Recent data (configurable age)  │
│   │   (OpenSearch + k-NN)             │                                      │
│   └───────────────┬───────────────────┘                                      │
│                   │                                                          │
│                   │ Time-based cutoff                                        │
│                   ▼                                                          │
│   ┌───────────────────────────────────┐                                      │
│   │        COLD TIER                  │                                      │
│   │          S3                       │ ◄── Older data (archived)            │
│   │   (Cost-effective archive)        │                                      │
│   └───────────────────────────────────┘                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Embedding Generation

| Aspect | Configuration |
|--------|---------------|
| **Default** | Synchronous on write |
| **Optional** | Async (configurable per workbench) |
| **Model** | Hub framework-provided (Olympus embedding service) |

---

## Consequences

### Positive

1. **Optimized for access patterns**: KV gets low-latency MongoDB; search services get OpenSearch
2. **Cost efficiency**: Time-based tiering moves old data to cheaper S3
3. **RAG-enabled**: Europa's k-NN plugin provides vector search
4. **Platform consistency**: Uses existing Olympus services (no new infrastructure)
5. **Session-appropriate**: Ephemeral data with automatic cleanup

### Negative

1. **Mixed backends**: Two different services to manage (Callisto + Europa)
2. **Tiering complexity**: Time-based cutoff requires configuration and monitoring
3. **Sync embedding latency**: Default synchronous embeddings add write latency

### Mitigations

| Risk | Mitigation |
|------|------------|
| Mixed backend complexity | Unified SDK abstracts storage details |
| Tiering configuration | Sensible defaults; admin tunable |
| Embedding latency | Async option available; embedding cached |

---

## Alternatives Considered

### Single Backend (Europa Only)

- **Pros**: Simpler, single service
- **Cons**: OpenSearch is overkill for simple KV; higher latency for CRUD
- **Why rejected**: KV access pattern benefits from MongoDB's low-latency

### Single Backend (Callisto Only)

- **Pros**: Simpler, single service
- **Cons**: MongoDB lacks native vector search; would need separate embedding service
- **Why rejected**: RAG is core requirement for Log/Conversation/Documents

### Purpose-Built Service

- **Pros**: Optimized for exact requirements
- **Cons**: New infrastructure; development/ops overhead
- **Why rejected**: Olympus services meet requirements; no need to build new

---

## Configuration

### Workbench CRD

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
spec:
  memory_services:
    agent_memory:
      kv_store:
        backend: callisto
        cluster_ref: callisto-prod
      log_store:
        backend: europa
        cluster_ref: europa-prod
        tiering:
          hot_retention_hours: 24
          cold_storage: s3
      conversation_store:
        backend: europa
        cluster_ref: europa-prod
        tiering:
          hot_retention_hours: 12
          cold_storage: s3
      document_store:
        backend: europa
        cluster_ref: europa-prod
        content_storage: s3
      embedding:
        mode: sync  # or 'async'
```

---

## Related Decisions

- [ADR-0067: Agent Memory Session Scope](./0067-agent-memory-session-scope.md) — Session lifecycle
- [ADR-0069: Agent Memory Storage Services](./0069-agent-memory-storage-services.md) — Four services design

---

## References

- [Agent Memory Services](../04-subsystems/memory-services/agent-memory/README.md)
- [Storage Services](../04-subsystems/memory-services/agent-memory/storage-services.md)
- [Memory Services Overview](../04-subsystems/memory-services/README.md)

