# Hub Agent Memory

> **Status:** 🔴 Stub — Placeholder for expansion

Hub Agent Memory provides **persistence and management for Agent Memory**—the operational, scoped memory used by agents to maintain continuity and adapt behavior.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Memory Types** | Episodic, Semantic, Preference, Procedural |
| **Scope** | Agent/Session |
| **Persistence** | Ephemeral (configurable retention) |
| **Purpose** | Operational continuity, personalization |

---

## The Question Agent Memory Answers

> *"Given what I have experienced, how should I act now?"*

---

## Memory Categories

### Episodic Memory
Recent interactions, events, and experiences:
- Chat history and conversation turns
- Tool calls and results
- Decisions made in current session
- Errors encountered

### Semantic Memory
Facts promoted from experience:
- Learned facts about the user/context
- Patterns recognized over time
- Preferences inferred from behavior

### Preference Memory
Stated or learned preferences:
- Communication style preferences
- Timezone and locale
- Notification preferences
- Decision delegation preferences

### Procedural Memory
Workflows, skills, and procedures:
- Task execution patterns
- Custom workflows learned
- Tool usage patterns
- Escalation triggers

---

## Storage Model

```
┌─────────────────────────────────────────────────────────────────┐
│                    AGENT MEMORY STORE                            │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                  MEMORY RECORD                           │    │
│  │                                                          │    │
│  │  tenant_id: string                                       │    │
│  │  agent_id: string                                        │    │
│  │  session_id: string (optional)                           │    │
│  │  memory_type: enum (episodic|semantic|preference|proc)   │    │
│  │  content: structured/unstructured                        │    │
│  │  embedding: vector (for semantic search)                 │    │
│  │  timestamp: datetime                                     │    │
│  │  ttl: duration (for decay)                               │    │
│  │  metadata: key-value                                     │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Retention & Decay

| Memory Type | Default Retention | Decay Model |
|-------------|-------------------|-------------|
| **Episodic** | Session + 24h | Time-based decay |
| **Semantic** | 30 days | Usage-based refresh |
| **Preference** | 90 days | Explicit or usage-based |
| **Procedural** | Indefinite | Explicit deletion |

---

## API Operations

| Operation | Description |
|-----------|-------------|
| `write` | Store a memory record |
| `read` | Retrieve specific memory by ID |
| `query` | Query memories by type, time range, metadata |
| `search` | Semantic search across memories |
| `delete` | Explicit memory deletion |
| `promote` | Promote to Enterprise Memory |

---

## Scoping

| Scope | Description | Use Case |
|-------|-------------|----------|
| **Session** | Ephemeral, single conversation | Chat context |
| **Agent** | Persists across sessions | Learned preferences |
| **Agent+Subject** | Agent's memory of specific subject | Customer interaction history |

---

## Seer Integration

| Integration | Description |
|-------------|-------------|
| **Memory SDKs** | Seer provides SDKs that write to Hub Agent Memory |
| **Context Assembly** | Retrieved during context compilation |
| **Raw Agent Frameworks** | Can use own frameworks but storage in Hub |

---

## Related Documentation

- [Memory Services Overview](./README.md)
- [Hub Enterprise Memory](./hub-enterprise-memory.md)
- [Seer Context Assembly](../../../olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md)

---

*TODO: Detailed design — storage backends, embedding strategy, decay algorithms, promotion rules*

