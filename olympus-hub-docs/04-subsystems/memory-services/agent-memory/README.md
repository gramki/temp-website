# Agent Memory Services

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Parent**: [Memory Services](../README.md)

---

## Overview

**Agent Memory Services** provides Hub's implementation of agent-level memory for operational continuity and personalization. These stores capture recent interactions, learned preferences, and session context that help agents maintain continuity across conversations.

### Key Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Agent/session — scoped to individual agent or user |
| **Persistence** | Ephemeral — days to months depending on memory class |
| **Purpose** | Operational continuity, personalization, context |
| **Write Path** | Direct SDK access (not via Signal Exchange) |
| **Read Path** | SDK methods and Seer context assembly |
| **PII Policy** | **Permitted** — with appropriate consent and handling |

---

## Architecture

### Storage Backend

> **Note**: The storage backend for Agent Memory is **not yet finalized**. Options under consideration include managed key-value stores, document stores, or purpose-built memory services. This will be determined based on access patterns and scale requirements.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      AGENT MEMORY STORAGE                                     │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐    │
│   │                    STORAGE BACKEND (TBD)                             │    │
│   │                                                                      │    │
│   │   Requirements:                                                      │    │
│   │   • Low-latency reads (context assembly is time-sensitive)           │    │
│   │   • TTL support (automatic expiry for ephemeral data)                │    │
│   │   • Vector search capability (semantic retrieval)                    │    │
│   │   • Multi-tenant isolation                                           │    │
│   │   • Workbench scoping                                                │    │
│   │                                                                      │    │
│   │   Candidates:                                                        │    │
│   │   • Olympus Europa (OpenSearch) — if semantic search critical        │    │
│   │   • Olympus Callisto (Redis) — if latency critical                   │    │
│   │   • Purpose-built memory service — if specialized needs              │    │
│   └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Differences from Enterprise Memory

| Aspect | Enterprise Memory | Agent Memory |
|--------|-------------------|--------------|
| **Scope** | Organizational | Agent/User/Session |
| **Retention** | 7+ years | Days to months |
| **Write Path** | Via Signal Exchange | Direct SDK |
| **PII** | Prohibited | Permitted (with consent) |
| **Immutability** | Immutable records | Mutable (update/delete) |
| **Audit Requirements** | Full CAF compliance | Lightweight logging |
| **Primary Use** | Audit, precedent | Context, personalization |

---

## Write Path

Agent Memory supports **direct writes** via SDK — Signal Exchange routing is not required:

```
Agent (via Seer Runtime)
        │
        │ SDK method call
        ▼
Agent Memory SDK
        │
        │ Validation, scoping
        ▼
Agent Memory Service
        │
        │ TTL assignment, indexing
        ▼
Storage Backend
```

### Why Direct Writes?

| Reason | Justification |
|--------|---------------|
| **Latency** | Agent memory writes should be fast; async routing adds latency |
| **No Request Binding** | Agent memory isn't always tied to a Hub Request |
| **Simpler Model** | Session context doesn't need Signal Exchange complexity |
| **Mutability** | Agent memory can be updated/deleted; immutability not required |

---

## Read Path

Agent Memory is read via:

1. **SDK Methods** — Direct retrieval for agent code
2. **Seer Context Assembly** — Automatic inclusion in agent context

```python
# SDK method example
from hub.memory import agent_memory

# Write
await agent_memory.remember(
    agent_id="agent-support-001",
    memory_type="semantic",
    content={"user_prefers": "email", "timezone": "PST"},
    ttl_days=90
)

# Read
preferences = await agent_memory.recall(
    agent_id="agent-support-001",
    memory_type="semantic",
    query="user preferences"
)
```

---

## Memory Classes (ESPP)

Agent Memory implements the same ESPP taxonomy as Enterprise Memory, but with different semantics:

| Class | Purpose | Retention | Example |
|-------|---------|-----------|---------|
| **Episodic** | Recent interactions, session context | Session + 24h | Last 10 conversation turns |
| **Semantic** | Learned facts about user/context | 30 days | "User prefers email over phone" |
| **Procedural** | Task patterns, workflow customizations | Indefinite | "User always approves under $500" |
| **Preference** | Communication style, settings | 90 days | "Prefers concise responses" |

### Decay Model

Agent Memory supports **decay** — records lose relevance over time:

| Memory Class | Decay Model | Refresh Trigger |
|--------------|-------------|-----------------|
| **Episodic** | Time-based (linear) | N/A — expires automatically |
| **Semantic** | Usage-based | Re-accessed = TTL extended |
| **Procedural** | None | Explicit deletion |
| **Preference** | Usage-based | Re-confirmed = TTL extended |

---

## Promotion to Enterprise Memory

Agent Memory can **promote** to Enterprise Memory when patterns become institutional:

```
Agent Memory (observed pattern)
        │
        │ Pattern detected across sessions
        ▼
Enterprise Learning Services
        │
        │ Review, validation, governance
        ▼
Enterprise Memory (institutional knowledge)
```

See [Enterprise Learning Services](../../cognitive-audit-fabric/enterprise-learning-services.md) for promotion workflows.

---

## Provisioning

Agent Memory is provisioned as part of the Workbench specification:

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: fraud-ops-prod
  namespace: acme-bank
spec:
  memory_services:
    agent_memory:
      enabled: true
      
      defaults:
        retention:
          episodic_hours: 24
          semantic_days: 30
          procedural_days: -1      # Indefinite
          preference_days: 90
        
      storage:
        backend: tbd               # To be determined
        # backend: callisto       # If Redis
        # backend: europa         # If OpenSearch
```

---

## Seer Integration

Agent Memory integrates tightly with Seer:

| Integration Point | Description |
|-------------------|-------------|
| **Context Assembly** | Agent memory retrieved during context compilation |
| **Memory SDKs** | Seer provides SDKs that write to Hub Agent Memory |
| **Raw Agent Frameworks** | Can use own frameworks but storage in Hub |
| **Observability** | Memory operations traced as part of agent traces |

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Agent Memory SDK](./sdk.md) | SDK specification for agent memory operations | 🔴 Stub |
| [Retention & Decay](./retention-and-decay.md) | Retention policies and decay models | 🔴 Stub |
| [Context Assembly Integration](./context-assembly.md) | Integration with Seer context assembly | 🔴 Stub |

---

## Related Documents

- [Memory Services Overview](../README.md) — Parent subsystem
- [Enterprise Memory Services](../enterprise-memory/README.md) — Organizational memory
- [Shared Concepts](../shared/README.md) — ESPP taxonomy, common patterns
- [Seer Context Assembly](../../../../olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md)

---

## TODO

| Item | Priority | Notes |
|------|----------|-------|
| Storage backend decision | P1 | Evaluate latency vs search requirements |
| SDK specification | P1 | Define API surface |
| Decay algorithm | P2 | Time-based vs usage-based specifics |
| PII handling | P2 | Consent model, encryption requirements |

---

*TODO: Storage backend selection, SDK specification, decay algorithms, PII handling*

