# Context Assembly

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-11

## Overview

Context Assembly is the process of constructing the **complete context** for each agent reasoning step, ensuring reproducibility and auditability.

Context is not a simple concatenation of inputs — it is a **compiled artifact** that brings together multiple sources, ranks relevance, manages token budgets, and preserves provenance.

**Key Design Point**: Context assembly is a **service that agents explicitly invoke** — it does not pre-compile context. Agents choose when and how to use it, and can augment the compiled context as needed.

---

## The Three-Source Model

Agent decision context draws from three distinct sources, each serving a different cognitive purpose:

| Source | What the Agent Asks | Nature | Owned By |
|--------|---------------------|--------|----------|
| **Enterprise Knowledge** | *"What should I do?"* | Normative — rules, policies, facts | Hub (Knowledge Services) |
| **Enterprise Memory** | *"What has been done?"* | Historical — precedent, outcomes, exceptions | Hub (Memory Services) |
| **Agent Memory** | *"What have I been doing?"* | Operational — session state, recent interactions | Hub (Memory Services), accessed via Seer SDK |

### Why All Three Matter

| Without... | The Agent Cannot... |
|------------|---------------------|
| Enterprise Knowledge | Know what is permitted, required, or true |
| Enterprise Memory | Recognize precedent, learn from outcomes, continue handoffs |
| Agent Memory | Maintain session continuity, recall recent interactions |

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
| **Context Sources** | Enterprise Knowledge, Enterprise Memory, Agent Memory |
| **Retrieval Orchestration** | Coordinates retrieval from memory, knowledge, and APIs |
| **Context Ranking** | Prioritizes information by relevance to the current task |
| **Context Truncation** | Manages context size within model token limits |
| **Context Logging** | Records assembled context for audit and reproducibility |
| **Reproducibility** | Same inputs and retrieval state produce same context |

---

## Related

- `subsystems/context-compiler/README.md` - Context Compiler subsystem implementation
- `subsystems/seer-agent-sdk/README.md` - SDK APIs for context assembly
- `olympus-hub-docs/04-subsystems/memory-services/README.md` - Hub Memory Services
- `olympus-hub-docs/04-subsystems/knowledge-services/README.md` - Hub Knowledge Services

---

*For detailed implementation, see `subsystems/context-assembly-engine.md` (to be migrated to `subsystems/context-compiler/`).*
