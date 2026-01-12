# Context Assembly

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-11

## Overview

Context Assembly is the process of constructing the **complete context** for each agent reasoning step, ensuring reproducibility and auditability.

Context is not a simple concatenation of inputs — it is a **compiled artifact** that brings together multiple sources, ranks relevance, manages token budgets, and preserves provenance.

**Key Design Point**: Context assembly is a **service that agents explicitly invoke** — it does not pre-compile context. Agents choose when and how to use it, and can augment the compiled context as needed.

---

## The Four-Source Model

Agent decision context draws from four distinct sources, each serving a different cognitive purpose:

| Source | What the Agent Asks | Nature | Owned By |
|--------|---------------------|--------|----------|
| **Enterprise Knowledge** | *"What should I do?"* | Normative — rules, policies, facts | Hub (Knowledge Services) |
| **Enterprise Memory** | *"What has been done?"* | Historical — precedent, outcomes, exceptions | Hub (Memory Services) |
| **Agent Memory** | *"What have I been doing?"* | Operational — session state, recent interactions | Hub (Memory Services) |
| **Hub Request Context** | *"What is the request context chain?"* | Hierarchical — current request + all ancestors | Hub (Request Management) |

### Why All Four Matter

| Without... | The Agent Cannot... |
|------------|---------------------|
| Enterprise Knowledge | Know what is permitted, required, or true |
| Enterprise Memory | Recognize precedent, learn from outcomes, continue handoffs |
| Agent Memory | Maintain session continuity, recall recent interactions |
| Hub Request Context | Access ancestor request context, understand request hierarchy |

### Retrieval Flow

```
                    ┌─────────────────────────┐
                    │   Context Assembly      │
                    │        Engine           │
                    └───────────┬─────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
        ▼                       ▼                       ▼
┌───────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Enterprise   │     │   Enterprise    │     │     Agent       │
│   Knowledge   │     │     Memory      │     │     Memory      │
│  (Hub - RAG)  │     │ (Hub - Memory)  │     │  (Hub - Memory) │
└───────────────┘     └─────────────────┘     └─────────────────┘
```

---

## Key Principles

- Context is **compiled**, not concatenated
- Every element in context is intentionally included
- Each element has a **source, timestamp, and provenance**
- Context assembly is **inspectable and reproducible**
- Enterprise Memory is a **first-class context source**, not an afterthought

---

## Scope

| Capability | Description |
|------------|-------------|
| **Context Sources** | Enterprise Knowledge, Enterprise Memory, Agent Memory, Hub Request Context |
| **Request Hierarchy Integration** | Ancestry topology traversal, goal and role-based filtering |
| **Request-Update-Based Retriever Configuration** | Automatic retriever selection based on Training Spec selectors |
| **Tool-Aware Compilation** | Incorporation of available tools into context constraints |
| **Retrieval Orchestration** | Coordinates retrieval from memory, knowledge, request context, and APIs |
| **Context Ranking** | Prioritizes information by relevance to the current task |
| **Context Truncation** | Manages context size within model token limits |
| **Context Logging** | Records assembled context for audit and reproducibility |
| **Reproducibility** | Same inputs and retrieval state produce same context |

---

## Related

- [Context Compiler: Compilation Service](../subsystems/context-compiler/compilation-service.md) — Detailed context compilation service design
- [Context Compiler: README](../subsystems/context-compiler/README.md) — Context Compiler subsystem overview
- [Seer Agent SDK: Context Compiler APIs](../subsystems/seer-agent-sdk/python-sdk/context-compiler-apis.md) — Python SDK APIs
- [Seer Agent SDK: Context Compiler APIs](../subsystems/seer-agent-sdk/java-sdk/context-compiler-apis.md) — Java SDK APIs
- [Hub Memory Services](../../../olympus-hub-docs/04-subsystems/memory-services/README.md) — Enterprise Memory and Agent Memory
- [Hub Knowledge Services](../../../olympus-hub-docs/04-subsystems/knowledge-services/README.md) — Enterprise Knowledge
- [Hub Request Hierarchy](../../../olympus-hub-docs/04-subsystems/request-management/request-hierarchy.md) — Request hierarchy and context inheritance

---

*For detailed implementation, see [Context Compiler: Compilation Service](../subsystems/context-compiler/compilation-service.md).*
