# ADR-0069: Agent Memory Storage Services

> **Status**: Accepted  
> **Date**: 2026-01-08  
> **Category**: memory-services

---

## Context

Hub's Agent Memory needs concrete storage services that:
1. Work with any agentic framework
2. Support session-scoped, isolated, encrypted storage
3. Enable both programmatic SDK and LLM-callable tool access
4. Handle different use cases (state, conversation, logs, documents)

### Requirements

- **No in-memory stores**: Hub runtimes don't guarantee VM affinity
- **Durable persistence**: Survive agent restarts within session
- **Multiple access patterns**: Key-value, append-only, RAG search
- **Compaction support**: Conversation history must respect token budgets
- **Document storage**: Files exchanged/referenced in session

---

## Decision

**Hub provides four storage services for Agent Memory:**

| Service | Purpose | Operations |
|---------|---------|------------|
| **Log Service** | Append-only session history | `append`, `get_last`, `rag_search` |
| **Conversation Service** | Chat history with compaction | `append`, `retrieve`, `compact` |
| **KV Store** | Entities, preferences, state | `put`, `get`, `delete`, `list` |
| **Document Service** | Files, images, PDFs | `store`, `retrieve`, `delete` |

### Service Characteristics

1. **Log Service**
   - Append-only (no update/delete)
   - RAG-enabled for semantic search
   - Use case: Session audit trail, searchable history

2. **Conversation Service**
   - Append-only with compaction
   - Configurable strategies: `sliding_window`, `summarization`, `token_budget`
   - Compaction is synchronous (before write)
   - Use case: Chat context within token limits

3. **KV Store**
   - Full CRUD operations
   - Logical store names for organization
   - Use case: Entities, preferences, workflow state

4. **Document Service**
   - Content-addressable URIs (hash-based)
   - Virus/malware scanning before persistence
   - Use case: Files referenced in conversation

### Access Patterns

All services support:
- **SDK access**: Direct programmatic API
- **Tool access**: LLM-callable save/recall operations

---

## Consequences

### Positive

1. **Generic primitives**: Work with any framework's idioms
2. **Separation of concerns**: Different services for different access patterns
3. **Token management**: Conversation compaction built-in
4. **Security**: Document scanning, encryption automatic

### Negative

1. **No automatic entity extraction**: KV Store is storage only
2. **No sophisticated decay**: Beyond compaction, left to frameworks
3. **No cross-service queries**: Each service is independent

### Neutral

1. Storage backend TBD (could be Europa, Callisto, or purpose-built)
2. RAG embeddings are Hub-provided (not developer-specified)

---

## Alternatives Rejected

### Single Unified Memory Store

- **Why rejected**: Different access patterns require different optimizations
- **Trade-off**: More services to learn, but each fits its use case

### ESPP-Named Services (Episodic Store, Semantic Store, etc.)

- **Why rejected**: Frameworks don't use ESPP; would create translation friction
- **Trade-off**: Less prescriptive, but more framework-compatible

### Pluggable Storage Backends

- **Why rejected**: Enterprise constraints require Hub-managed storage for security, isolation, compliance
- **Trade-off**: Less flexibility, but consistent guarantees

---

## Related Decisions

- [ADR-0067: Agent Memory Session Scope](./0067-agent-memory-session-scope.md) — Lifecycle constraints
- [ADR-0068: Framework-Native Idioms](./0068-agent-memory-framework-native-idioms.md) — Design philosophy

---

## References

- [Agent Memory Services](../04-subsystems/memory-services/agent-memory/README.md)
- [Storage Services](../04-subsystems/memory-services/agent-memory/storage-services.md)
- [Agent Memory SDK](../04-subsystems/memory-services/agent-memory/sdk.md)

