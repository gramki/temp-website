# Agent Memory (Hub Subsystem)

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08  
> **Parent**: [Memory Services](../README.md)

---

## Overview

**Agent Memory Services** provides Hub's infrastructure for agent-level memory persistence, isolation, retrieval, and lifecycle management. Unlike Enterprise Memory, Hub does not prescribe specific memory management approaches — it enables agents built on any framework to persist operational state with appropriate guardrails.

### Design Philosophy

Hub encourages **Raw Agents** to be built with any framework of choice. The agentic AI landscape is in its infancy with significant evolution expected before standards or best practices emerge. Hub therefore avoids opinionated approaches while advocating that agent developers recognize the distinction between Enterprise Memory and Agent Memory.

---

## Table of Contents

1. [Key Characteristics](#key-characteristics)
2. [Core Constraints](#core-constraints)
3. [Storage Services](#storage-services)
4. [Access Patterns](#access-patterns)
5. [RAG / Semantic Search Capabilities](#rag--semantic-search-capabilities)
6. [User Profile (Request Scoped)](#user-profile-request-scoped)
7. [Provisioning](#provisioning)
8. [Lifecycle Management](#lifecycle-management)
9. [Security Model](#security-model)
10. [What Hub Provides vs Framework Responsibility](#what-hub-provides-vs-framework-responsibility)
11. [Related Documents](#related-documents)

---

## Key Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Request/Session — all memory is bounded by session lifecycle |
| **Isolation** | Per (tenant, workbench, scenario, request, agent) |
| **Persistence** | Durable stores only — no in-memory stores |
| **Write Path** | Direct SDK access and tool invocation |
| **Read Path** | SDK methods, tools, and Seer context assembly |
| **PII Policy** | **Permitted** — within session scope (not cross-session) |
| **Encryption** | Application-layer encryption with agent+session unique keys |

---

## Core Constraints

### No In-Memory Stores

Hub Runtimes **do not ensure durable execution on the same VM**. Hub Sessions (Requests) are long-lived, and agents cannot expect in-memory stores to be reliably available across invocations.

| ❌ Not Supported | ✅ Required Approach |
|------------------|---------------------|
| In-memory dictionaries | Hub-provided storage services |
| Process-local caching | Request-scoped durable stores |
| VM affinity assumptions | Stateless agent execution |

### Session-Scoped Storage Only

All agent memory is bounded by the Request/Session lifecycle:

| Constraint | Rationale |
|------------|-----------|
| **Maximum lifetime = Session lifetime** | Prevents accidental enterprise memory patterns |
| **No user preferences beyond session** | Cross-session preferences require Enterprise Memory or business entity stores |
| **No cross-agent visibility** | Each agent's memory is isolated; no cross-talk |

### Strict Isolation

Every agent receives isolated storage scoped by:

```
tenant → workbench → scenario → request → agent
```

All read/write APIs operate **only within this scope** — agents cannot access higher scopes or other agents' memory.

---

## Storage Services

Hub provides four storage services for agent memory:

### 1. Log Service

**Purpose**: Append-only message log for session history

| Feature | Description |
|---------|-------------|
| **Operations** | Append, Retrieve (last N), RAG retrieval |
| **Use Cases** | Session history, conversation audit trail |
| **Compaction** | None — append-only |
| **Retrieval** | Last N messages, semantic search (RAG) |

### 2. Conversation Service

**Purpose**: Append-only message store with compaction strategies

| Feature | Description |
|---------|-------------|
| **Operations** | Append, Retrieve, Compact |
| **Use Cases** | Conversation context, token budget management |
| **Compaction** | Configurable per store and per agent |
| **Strategies** | LLM-based summarization, sliding window, token budget |

**Compaction Behavior**:
- Configured by developer in agent specification
- Can be tuned in deployment CRD
- **Synchronous** — executed before write operations
- Respects token budget constraints

### 3. Key-Value (KV) Service

**Purpose**: Structured key-value storage for entities and preferences

| Feature | Description |
|---------|-------------|
| **Operations** | Put, Get, Delete, List |
| **Use Cases** | Entity extraction, in-session preferences, state |
| **Store Names** | Logical names like "preferences", "merchant", etc. |
| **Naming Rules** | Pattern: `(a-zA-Z_-)+` (ASCII only, no PII in keys) |

**Logical Store Names**:

```python
# Named stores for business domain organization
kv_store.put("preferences", "theme", "dark")
kv_store.put("merchant", "id", "ACME-123")

# Default store (name = ".")
kv_store.put(".", "last_action", "approve")
```

### 4. Document Storage Service

**Purpose**: CLOB and BLOB storage for session documents

| Feature | Description |
|---------|-------------|
| **Operations** | Store, Retrieve, Delete |
| **Use Cases** | Documents exchanged/referenced in session |
| **Addressing** | Content-addressable URI (hash-based) |
| **Security** | Virus/malware scanning before persistence |

**Document References**:
- Documents are stored and assigned a unique URI
- URI is content-addressable (unique per content hash)
- Agents reference documents by URI in other services

---

## Access Patterns

All storage services are available through both SDK and tool interfaces:

### SDK Access (for Raw Agent Frameworks)

```python
from hub.agent_memory import kv_store, conversation, log_store, documents

# KV Store
await kv_store.put("preferences", "language", "en-US")
value = await kv_store.get("preferences", "language")

# Conversation
await conversation.append(message)
context = await conversation.retrieve(token_budget=4000)

# Log Store
await log_store.append(entry)
recent = await log_store.get_last(n=10)
relevant = await log_store.rag_search(query="user complaint")

# Documents
uri = await documents.store(content, content_type="application/pdf")
doc = await documents.retrieve(uri)
```

### Tool Access (for LLM-based Agents)

Each service exposes **save** and **recall** operations as tools:

| Tool | Operations | Description |
|------|------------|-------------|
| `agent_memory.kv` | `save`, `recall`, `delete` | Key-value operations |
| `agent_memory.conversation` | `save`, `recall` | Conversation context |
| `agent_memory.log` | `save`, `recall` | Session log |
| `agent_memory.documents` | `save`, `recall` | Document storage |

**Agent Training**: Agents are encouraged to incorporate memory management skills — understanding when to save vs recall, appropriate use of each service.

---

## Storage Architecture

Each Agent Memory service uses an appropriate Olympus platform service:

| Service | Storage Backend | Characteristics |
|---------|-----------------|-----------------|
| **KV Store** | Olympus Callisto (MongoDB) | Low-latency CRUD, document storage |
| **Log Service** | Olympus Europa (OpenSearch) + S3 | RAG-enabled, time-based tiering |
| **Conversation Service** | Olympus Europa (OpenSearch) + S3 | RAG-enabled, time-based tiering |
| **Document Storage** | Olympus Europa (OpenSearch) + S3 | Vector search, content-addressable |

### Tiered Storage

For Log and Conversation services, data is tiered based on time:

| Tier | Storage | Data Age | Access Pattern |
|------|---------|----------|----------------|
| **Hot** | Europa (OpenSearch) | Recent | Frequent read/write |
| **Cold** | S3 | Older | Archive, occasional access |

Tiering is time-based and configured per workbench.

---

## RAG / Semantic Search Capabilities

Log Service and Document Service support RAG-based semantic search:

| Aspect | Details |
|--------|---------|
| **Available On** | Log Service, Document Service (Conversation planned) |
| **Backing Store** | Olympus Europa (OpenSearch with k-NN plugin) |
| **Embeddings** | Hub framework-provided, synchronous on write (default) |
| **Async Option** | Configurable for async embedding generation |
| **Use Cases** | Semantic search over session history, document retrieval |
| **Limits** | Embedding count per session (configurable) |

> **Note**: RAG is a **capability of storage services**, not a separate fifth service.

---

## User Profile (Request Scoped)

User Profile is a **convenience wrapper** around KV Store for common user-related data patterns:

| Aspect | Details |
|--------|---------|
| **Implementation** | Uses KV Store with `"user_profile"` logical store name |
| **Scope** | Request/Session only (not cross-session) |
| **Schema** | Free-form (no enforced structure) |
| **Populated By** | Agent-supplied (not automatically from Hub identity) |

> **For cross-session user preferences**: Use Enterprise Memory or business entity stores.

---

## Provisioning

### Store Provisioning

| Level | Responsibility | Details |
|-------|----------------|---------|
| **Workbench** | Admin provisions stores | On developer request |
| **Agent Spec** | Developer declares requirements | Memory services needed |
| **Deployment** | Requirements mapped to stores | CRD configuration |

### Agent Specification

```yaml
apiVersion: seer.olympus.io/v1
kind: Agent
metadata:
  name: support-agent
spec:
  memory:
    services:
      - type: conversation
        compaction:
          strategy: summarization
          token_budget: 8000
      - type: kv
        stores:
          - preferences
          - customer
      - type: documents
```

### Deployment CRD

```yaml
apiVersion: hub.olympus.io/v1
kind: AgentDeployment
metadata:
  name: support-agent-prod
spec:
  agent_ref: support-agent
  memory_mapping:
    conversation:
      workbench_store: fraud-ops-conversation-store
      compaction:
        token_budget: 6000  # Override from spec
    kv:
      workbench_store: fraud-ops-kv-store
      quota_mb: 10
```

### Quotas

| Quota Type | Scope | Configurable By |
|------------|-------|-----------------|
| Storage size (MB) | Per agent per request | Deployment CRD |
| Document count | Per agent per request | Deployment CRD |
| Embedding count | Per agent per request | Deployment CRD |

---

## Lifecycle Management

### Retention

| Phase | Behavior |
|-------|----------|
| **Active Session** | Full read/write access |
| **Session Completed/Cancelled** | Memory retained for configured period |
| **Retention Expired** | Automatic deletion |

- Retention period configured **per store by tenant admin**
- Agents **cannot request early cleanup** (can override values)
- Supports debugging/audit during retention period

### No Cross-Request Memory

| Requirement | Path |
|-------------|------|
| Remember across sessions | Use Enterprise Memory |
| Persist business entities | Use operational data stores with entity semantics |
| User preferences (cross-session) | Use Enterprise Memory or business entity stores |

---

## Security Model

### Encryption

| Aspect | Implementation |
|--------|----------------|
| **Encryption Level** | Application layer (before persistence) |
| **Key Scope** | Unique per agent, per session |
| **Key Derivation** | From Workbench-scoped root key |
| **Values** | Encrypted; not logged; not retrievable outside session |

### Privacy

| Constraint | Enforcement |
|------------|-------------|
| Agent memory is agent-private | Scoped APIs enforce isolation |
| Values not logged | Application-layer encryption |
| Not retrievable outside session | Session-scoped keys |
| Store names: no PII | Validation on `(a-zA-Z_-)+` pattern |

---

## What Hub Provides vs Framework Responsibility

### Hub Provides

| Capability | Description |
|------------|-------------|
| Storage services | Log, Conversation, KV, Documents |
| Persistence | Durable stores with lifecycle management |
| Isolation | Strict scoping per agent per request |
| Encryption | Application-layer with session-unique keys |
| Tools | Save/recall operations as callable tools |
| SDK | Direct API access for Raw Agent frameworks |
| Quotas | Configurable limits per agent |
| Retention | Admin-configurable retention periods |

### Left to Agent Frameworks

| Capability | Notes |
|------------|-------|
| **Preference Learning** | Framework-specific algorithms |
| **Entity Extraction** | Framework-specific NLP/LLM approaches |
| **Provenance in Context Compilation** | How agent tracks memory sources |
| **Multi-agent Orchestration** | Sub-agent topology internal to Raw Agent |
| **Compaction Algorithms** | Beyond Hub-provided strategies |

### Multi-Agent Note

The **Request** is the shared context between agents in a Session. However, each agent could be a **compound agent** with an internal topology of sub-agents. Such sub-agents:
- Are not visible to Hub as agents
- Are out of Hub's purview
- Can access the memory of the Hub Agent that spawned them (if coded that way)

---

## Not Supported

| Feature | Rationale |
|---------|-----------|
| **Cross-talk between agents** | Isolation is a core principle |
| **In-memory stores** | No VM affinity guarantee |
| **Agent memory → Request updates** | No conflation with Enterprise Memory |
| **Multi-agent memory sharing** | Out of scope; use Request context |
| **Namespace-Scoped LTM Strategies** | LTM belongs to Enterprise Memory |
| **Cross-session memory** | Maximum lifespan = Request/Session |

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Agent Memory SDK](./sdk.md) | SDK and tool specification | 🟡 Draft |
| [Storage Services](./storage-services.md) | Log, Conversation, KV, Document services | 🟡 Draft |
| [Retention & Lifecycle](./retention-and-lifecycle.md) | Retention policies and lifecycle management | 🟡 Draft |
| [Design Rationale](./design-rationale.md) | Trade-offs and design decisions | 🟡 Draft |
| [Framework Reference](./framework-reference/README.md) | Industry framework analysis and patterns | 🟢 Reference |
| [Context Assembly Integration](./context-assembly.md) | Integration with Seer context assembly | 🔴 Stub |

---

## Related Documents

- [Memory Services Overview](../README.md) — Parent subsystem
- [Enterprise Memory Services](../enterprise-memory/README.md) — Organizational memory (cross-session)
- [Shared Concepts](../shared/README.md) — ESPP taxonomy, common patterns
- [Agent Memory Developer Guide](../../../10-guides/agent-memory-developer-guide.md) — **Best practices for developers**
- [Seer Context Assembly](../../../../olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md)

### Decision Logs

- [ADR-0067: Agent Memory Session Scope](../../../decision-logs/0067-agent-memory-session-scope.md) — Session lifecycle
- [ADR-0068: Framework-Native Idioms](../../../decision-logs/0068-agent-memory-framework-native-idioms.md) — No ESPP enforcement
- [ADR-0069: Storage Services](../../../decision-logs/0069-agent-memory-storage-services.md) — Four services
- [ADR-0070: Encryption and Isolation](../../../decision-logs/0070-agent-memory-encryption-isolation.md) — Security model
- [ADR-0071: Storage Backends](../../../decision-logs/0071-agent-memory-storage-backends.md) — Callisto + Europa + S3

---

## Key Differences from Enterprise Memory

| Aspect | Enterprise Memory | Agent Memory |
|--------|-------------------|--------------|
| **Scope** | Organizational, cross-agent | Agent/Session only |
| **Retention** | 7+ years | Session + retention period |
| **Write Path** | Via Signal Exchange | Direct SDK/tools |
| **PII** | Prohibited | Permitted (session scope) |
| **Immutability** | Immutable records | Mutable (update/delete) |
| **Audit Requirements** | Full CAF compliance | Encryption, no logging |
| **Cross-Session** | Yes | No |
| **Primary Use** | Audit, precedent, institutional learning | Context, personalization, state |

---

*Hub Agent Memory Services enable framework-agnostic agent memory with strict session scoping, encryption, and isolation.*
