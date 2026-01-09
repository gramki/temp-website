# Context Assembly Integration

> **Status**: 🔴 Stub — Placeholder for expansion  
> **Last Updated**: 2026-01-08  
> **Parent**: [Agent Memory](./README.md)

---

## Overview

This document describes how **Agent Memory integrates with Seer Context Assembly** — the process by which relevant memory is retrieved and included in an agent's context during processing.

> **Note**: Hub Agent Memory does **not** enforce ESPP (Episodic-Semantic-Procedural-Preference) taxonomy. Memory is organized by storage service (Log, Conversation, KV, Documents), not by memory class. See [Design Rationale](./design-rationale.md#framework-native-idiom-preservation).

---

## Integration Points

| Integration | Description |
|-------------|-------------|
| **Automatic Retrieval** | Context assembly retrieves from agent memory services |
| **Memory Selection** | Selects based on recency, relevance, and token budget |
| **Context Budget** | Memory competes for space in limited context window |
| **Semantic Matching** | Uses embeddings for RAG retrieval (Log, Documents) |

---

## Context Assembly Flow

```
Agent Turn Start
        │
        ▼
Seer Context Assembly Engine
        │
        ├── Retrieve Conversation History (token budget)
        ├── Retrieve Relevant Log Entries (RAG search)
        ├── Retrieve Stored Entities (KV Store)
        └── Retrieve Referenced Documents (if needed)
        │
        ▼
Context Compilation
        │
        ▼
Agent Processing
```

---

## Storage Service Integration

| Service | Context Assembly Use |
|---------|---------------------|
| **Conversation** | Token-budgeted recent messages + summary |
| **Log Store** | RAG search for relevant past entries |
| **KV Store** | Direct retrieval of stored entities/preferences |
| **Documents** | RAG search or direct URI retrieval |

---

## TODO

| Item | Priority | Notes |
|------|----------|-------|
| Define memory retrieval strategy | P1 | How services are queried |
| Define context budget allocation | P2 | How much space for each service |
| Define relevance scoring | P2 | How RAG results are ranked |

---

## Related Documents

- [Agent Memory README](./README.md)
- [Storage Services](./storage-services.md)
- [Seer Context Assembly Engine](../../../../olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md)

---

*TODO: Detailed integration specification pending Seer context assembly design*

