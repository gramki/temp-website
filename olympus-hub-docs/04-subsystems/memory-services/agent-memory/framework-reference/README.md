# Framework Reference — Agent Memory Patterns

> **Status**: 🟢 Reference  
> **Last Updated**: 2026-01-08  
> **Parent**: [Agent Memory Services](../README.md)

---

## Purpose

This folder contains reference documentation analyzing how popular agentic frameworks implement agent-level memory. This analysis informs Hub's Agent Memory design philosophy: **enable framework-native idioms without imposing Hub-specific semantics**.

---

## Documents

| Document | Description |
|----------|-------------|
| [Analysis](./analysis.md) | Detailed per-framework analysis with techniques, storage patterns, and observations |

---

## Executive Summary

### Key Finding: Frameworks Don't Enforce Memory Taxonomy

All analyzed frameworks allow memory type boundaries to blur:

| Framework | Memory Idiom | ESPP Enforcement |
|-----------|--------------|------------------|
| **LangChain** | Memory as chain component | ❌ None |
| **LangGraph** | Memory as typed state | ❌ None |
| **Semantic Kernel** | Memory as skill/plugin | 🟡 Collections only |
| **CrewAI** | Memory as shared crew context | 🟡 Short/Long-term only |
| **AutoGen** | Memory as conversation + teachability | ❌ None |
| **OpenAI Assistants** | Memory as managed threads | ❌ None |
| **AWS Strands** | Memory as state + messages + session | 🟡 via AgentCore |

**Implication for Hub**: ESPP taxonomy is valuable for Enterprise Memory governance (7+ year retention, cross-agent knowledge). For Agent Memory (session-scoped, ephemeral), enforcing taxonomy adds friction without governance benefit.

---

## Hub's Design Response

### Principle: Framework-Native Idiom Preservation

Hub's Agent Memory is designed to:

1. **Enable** — Provide storage infrastructure that works with any framework
2. **Not Conflict** — Avoid imposing patterns that clash with framework idioms
3. **Not Prescribe** — Let developers use their framework's native memory approaches
4. **Isolate** — Ensure enterprise-grade isolation without compromising flexibility

### What Hub Provides

| Capability | Description |
|------------|-------------|
| **Storage Services** | Log, Conversation, KV, Document — generic building blocks |
| **Persistence** | Durable stores that survive restarts |
| **Isolation** | Strict scoping per (tenant, workbench, scenario, request, agent) |
| **Encryption** | Application-layer with session-unique keys |
| **Compaction** | Built-in strategies (windowing, summarization) |
| **Tools** | Memory operations as callable tools |

### What Hub Leaves to Frameworks

| Capability | Rationale |
|------------|-----------|
| **Entity Extraction** | Domain-specific; frameworks already provide this |
| **Memory Classification** | Frameworks don't enforce; Hub shouldn't either |
| **Context Assembly** | Framework/Seer responsibility |
| **Decay Algorithms** | Beyond basic compaction, framework-specific |
| **Multi-Agent Sharing** | Request context for coordination; isolation preserved |

---

## Patterns Adopted from Frameworks

| Pattern | Source Framework | Hub Implementation |
|---------|-----------------|-------------------|
| **Typed State (JSON)** | LangGraph, Strands | JSON-serializable KV Store |
| **Memory as Tool** | Semantic Kernel | Save/recall operations as tools |
| **Session Persistence** | Strands | Durable stores, automatic persistence |
| **Conversation Compaction** | LangChain, Strands | Windowing, summarization strategies |
| **Namespace Scoping** | AgentCore | Strict multi-tenant isolation |

---

## Patterns Considered but Not Adopted

| Pattern | Source | Why Not Adopted |
|---------|--------|-----------------|
| **Automatic Entity Extraction** | LangChain, CrewAI | Domain-specific; requires LLM in storage layer |
| **Multi-Agent Memory Sharing** | CrewAI, Strands | Isolation is core; Request context serves coordination |
| **Pluggable Backends** | Strands | Enterprise constraints; Hub manages storage |
| **Cross-Session Memory** | Strands + AgentCore | Enterprise Memory serves this need |
| **ESPP Enforcement** | None (conceptual) | Frameworks don't enforce; adds friction |

---

## Framework Idiom Examples

### LangChain Style
```python
# Framework idiom: memory is a chain component
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=10)
chain = LLMChain(llm=llm, memory=memory)
```

**Hub equivalent**: Use Hub's Conversation Service with windowing.

### LangGraph Style
```python
# Framework idiom: memory is typed state
class AgentState(TypedDict):
    messages: list
    user_facts: dict
    preferences: dict
```

**Hub equivalent**: Use Hub's KV Store with logical store names (`"facts"`, `"preferences"`).

### Semantic Kernel Style
```python
# Framework idiom: memory is a skill
await kernel.memory.save_information("preferences", "User prefers dark mode")
result = await kernel.memory.search("preferences", "theme")
```

**Hub equivalent**: Use Hub's KV Store tools (`agent_memory.kv.save`, `agent_memory.kv.recall`).

### Strands Style
```python
# Framework idiom: memory is state + session
agent.state.set("preference", "concise")
session_manager = S3SessionManager(session_id="user-123")
```

**Hub equivalent**: Hub provides similar primitives; Strands agents can use Hub storage.

---

## Guidance for Developers

### Use Your Framework's Idioms

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│   Your Framework's Memory Patterns                                           │
│   (LangChain, LangGraph, Strands, custom, etc.)                             │
│                                                                              │
│       │                                                                      │
│       │  Use natively — Hub doesn't conflict                                │
│       ▼                                                                      │
│                                                                              │
│   Hub Agent Memory Services                                                  │
│   (Storage, Persistence, Isolation, Encryption)                             │
│                                                                              │
│       │                                                                      │
│       │  Provides infrastructure, not methodology                           │
│       ▼                                                                      │
│                                                                              │
│   Durable, Isolated, Encrypted Storage                                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### When to Use Enterprise Memory

| Use Case | Memory Type |
|----------|-------------|
| Session context, conversation history | Agent Memory |
| In-session user preferences | Agent Memory |
| Extracted entities for current session | Agent Memory |
| Temporary workflow state | Agent Memory |
| Cross-session preferences | ❌ Enterprise Memory |
| Audit trail, decisions | ❌ Enterprise Memory |
| Institutional knowledge | ❌ Enterprise Memory |
| Compliance records | ❌ Enterprise Memory |

---

## Related Documents

- [Agent Memory Services](../README.md) — Overview
- [Design Rationale](../design-rationale.md) — Trade-offs and decisions
- [Developer Guide](../../../../10-guides/agent-memory-developer-guide.md) — Best practices
- [Enterprise Memory](../../enterprise-memory/README.md) — Cross-session, governed memory

### Decision Logs

- [ADR-0068: Framework-Native Idioms](../../../../decision-logs/0068-agent-memory-framework-native-idioms.md) — No ESPP enforcement in Agent Memory

---

*Hub's Agent Memory enables framework-native development while providing enterprise-grade isolation and persistence.*

