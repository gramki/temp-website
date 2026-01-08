# Agent Memory Storage Services

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08  
> **Parent**: [Agent Memory Services](./README.md)

---

## Overview

Hub provides four storage services for agent memory, each designed for specific use cases while maintaining strict session scoping, encryption, and isolation.

### Storage Backend Summary

| Service | Backend | Tiering |
|---------|---------|---------|
| **Log Service** | Olympus Europa (OpenSearch) | S3 (time-based) |
| **Conversation Service** | Olympus Europa (OpenSearch) | S3 (time-based) |
| **KV Store** | Olympus Callisto (MongoDB) | None |
| **Document Storage** | Olympus Europa (OpenSearch) | S3 |

---

## 1. Log Service

**Purpose**: Append-only message log for session history and audit trail.

**Storage**: Olympus Europa (OpenSearch) with S3 tiered storage.

### Operations

| Operation | Description |
|-----------|-------------|
| `append(entry)` | Add entry to log |
| `get_last(n)` | Retrieve last N entries |
| `rag_search(query, limit)` | Semantic search over log entries |

### SDK Interface

```python
from hub.agent_memory import log_store

# Append an entry
await log_store.append({
    "type": "user_message",
    "content": "I need help with my account",
    "timestamp": "2026-01-08T10:30:00Z"
})

# Get last N entries
recent = await log_store.get_last(n=10)

# Semantic search
relevant = await log_store.rag_search(
    query="customer complaints about billing",
    limit=5
)
```

### Tool Interface

| Tool | Parameters |
|------|------------|
| `agent_memory.log.save` | `entry: object` |
| `agent_memory.log.recall` | `mode: "last_n" | "rag"`, `n?: int`, `query?: string`, `limit?: int` |

### Characteristics

| Aspect | Value |
|--------|-------|
| **Mutability** | Append-only (no update/delete) |
| **Compaction** | None |
| **RAG Support** | Yes (Hub-provided embeddings) |
| **Ordering** | Timestamp-ordered |

---

## 2. Conversation Service

**Purpose**: Append-only message store with configurable compaction strategies for token budget management.

**Storage**: Olympus Europa (OpenSearch) with S3 tiered storage.

### Operations

| Operation | Description |
|-----------|-------------|
| `append(message)` | Add message to conversation |
| `retrieve(token_budget)` | Get messages within token budget |
| `compact()` | Manually trigger compaction |

### SDK Interface

```python
from hub.agent_memory import conversation

# Append a message
await conversation.append({
    "role": "user",
    "content": "What's my account balance?"
})

# Retrieve within token budget
context = await conversation.retrieve(token_budget=4000)

# Manual compaction (usually automatic)
await conversation.compact()
```

### Tool Interface

| Tool | Parameters |
|------|------------|
| `agent_memory.conversation.save` | `message: object` |
| `agent_memory.conversation.recall` | `token_budget: int` |

### Compaction Strategies

| Strategy | Description |
|----------|-------------|
| `sliding_window` | Keep last N messages, discard oldest |
| `summarization` | LLM-based summarization of older messages |
| `token_budget` | Hybrid: recent messages + summarized history |

### Configuration

```yaml
# In agent specification
memory:
  services:
    - type: conversation
      compaction:
        strategy: summarization
        token_budget: 8000
        preserve_recent: 5  # Always keep last 5 messages
```

### Compaction Behavior

| Aspect | Behavior |
|--------|----------|
| **Trigger** | Synchronous, before write |
| **Configuration** | Developer in spec, tunable in deployment CRD |
| **Token Counting** | Hub-provided tokenizer |

---

## 3. Key-Value (KV) Service

**Purpose**: Structured key-value storage for entities, preferences, and state.

**Storage**: Olympus Callisto (MongoDB) — low-latency CRUD operations.

### Operations

| Operation | Description |
|-----------|-------------|
| `put(store, key, value)` | Store a value |
| `get(store, key)` | Retrieve a value |
| `delete(store, key)` | Remove a value |
| `list(store)` | List all keys in a store |

### SDK Interface

```python
from hub.agent_memory import kv_store

# Named stores for organization
await kv_store.put("preferences", "language", "en-US")
await kv_store.put("preferences", "timezone", "America/Los_Angeles")
await kv_store.put("customer", "segment", "premium")

# Retrieve
language = await kv_store.get("preferences", "language")

# Delete
await kv_store.delete("preferences", "timezone")

# List keys
keys = await kv_store.list("preferences")

# Default store (name = ".")
await kv_store.put(".", "last_action", "approve")
value = await kv_store.get(".", "last_action")
```

### Tool Interface

| Tool | Parameters |
|------|------------|
| `agent_memory.kv.save` | `store?: string`, `key: string`, `value: any` |
| `agent_memory.kv.recall` | `store?: string`, `key: string` |
| `agent_memory.kv.delete` | `store?: string`, `key: string` |

### Logical Store Names

| Aspect | Rules |
|--------|-------|
| **Pattern** | `(a-zA-Z_-)+` (ASCII only) |
| **No PII** | Store names must not contain PII |
| **Default** | `"."` when no store name provided |
| **Scope** | Local to agent (not shared across agents) |

### Example Store Organization

| Store Name | Use Case |
|------------|----------|
| `preferences` | User in-session preferences |
| `customer` | Customer entity attributes |
| `merchant` | Merchant entity attributes |
| `workflow` | Workflow state variables |
| `entities` | Extracted entities |

---

## 4. Document Storage Service

**Purpose**: CLOB and BLOB storage for documents referenced or exchanged in session.

**Storage**: Olympus Europa (OpenSearch) with S3 for content storage — vector search enabled.

### Operations

| Operation | Description |
|-----------|-------------|
| `store(content, content_type)` | Store document, returns URI |
| `retrieve(uri)` | Retrieve document by URI |
| `delete(uri)` | Remove document |
| `list()` | List all stored document URIs |

### SDK Interface

```python
from hub.agent_memory import documents

# Store a document
uri = await documents.store(
    content=pdf_bytes,
    content_type="application/pdf",
    metadata={"filename": "statement.pdf"}
)

# Retrieve
doc = await documents.retrieve(uri)
content = doc.content
content_type = doc.content_type

# Delete
await documents.delete(uri)

# List all
uris = await documents.list()
```

### Tool Interface

| Tool | Parameters |
|------|------------|
| `agent_memory.documents.save` | `content: bytes`, `content_type: string`, `metadata?: object` |
| `agent_memory.documents.recall` | `uri: string` |
| `agent_memory.documents.delete` | `uri: string` |

### URI Characteristics

| Aspect | Details |
|--------|---------|
| **Format** | Content-addressable (hash-based) |
| **Uniqueness** | Unique per content hash |
| **Referencing** | Use URI in other services (conversation, kv) |

### Security

| Aspect | Implementation |
|--------|----------------|
| **Virus Scan** | Before persistence |
| **Malware Scan** | Before persistence |
| **Content Validation** | Type-specific validation |

### Limits

| Limit | Scope | Configurable |
|-------|-------|--------------|
| Document size | Per document | Deployment CRD |
| Document count | Per agent per request | Deployment CRD |
| Total storage | Per agent per request | Deployment CRD |

---

## Common Patterns

### All Services

| Pattern | Details |
|---------|---------|
| **Isolation** | Per (tenant, workbench, scenario, request, agent) |
| **Encryption** | Application-layer, agent+session unique keys |
| **Access** | SDK and Tool interfaces |
| **Scope** | Request/Session only |

### Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `QuotaExceeded` | Storage limit reached | Delete old data or increase quota |
| `StoreNotFound` | Logical store not declared | Add to agent specification |
| `KeyNotFound` | Key doesn't exist | Handle gracefully |
| `InvalidStoreName` | Name violates pattern | Use valid ASCII pattern |

---

## RAG / Semantic Search Support

RAG is a **capability of certain storage services**, not a separate service.

### Availability by Service

| Service | RAG Support | Notes |
|---------|-------------|-------|
| Log Service | ✅ Available | Semantic search over log entries |
| Conversation Service | 🟡 Planned | Not yet implemented |
| KV Service | ❌ Not Applicable | Key-value lookup only |
| Document Storage | ✅ Available | Semantic search over document content |

### Embedding Generation

| Aspect | Details |
|--------|---------|
| **Provider** | Hub framework-provided (not developer-specified) |
| **Model** | Platform-configured |
| **Limits** | Embedding count per session (configurable per workbench) |

### RAG Query Examples

```python
# Search over log entries
log_results = await log_store.rag_search(
    query="customer complained about billing",
    limit=5,
    min_score=0.7
)

# Search over stored documents
doc_results = await documents.rag_search(
    query="dispute resolution policy",
    limit=5,
    min_score=0.7
)

for result in doc_results:
    print(f"URI: {result.uri}, Score: {result.score}")
```

---

## Related Documents

- [Agent Memory Services](./README.md) — Overview
- [Agent Memory SDK](./sdk.md) — Complete SDK specification
- [Retention & Lifecycle](./retention-and-lifecycle.md) — Retention policies
- [Context Assembly Integration](./context-assembly.md) — Seer integration
- [Design Rationale](./design-rationale.md) — Why these four services

### Infrastructure

- [Olympus Callisto](../../../../olympus-hub-docs/05-infrastructure/callisto-kv-store.md) — MongoDB-based KV Store
- [Olympus Europa](../../../../olympus-hub-docs/05-infrastructure/europa-opensearch.md) — OpenSearch with k-NN and S3 tiering
- [ADR-0071: Storage Backends](../../../decision-logs/0071-agent-memory-storage-backends.md) — Storage layer decisions

---

*Storage services provide the building blocks for agent memory with strict session scoping and encryption.*

