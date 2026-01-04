# Context Assembly Engine

> **Status:** Placeholder — Design in progress

## Overview

The Context Assembly Engine constructs the **complete context** for each agent reasoning step, ensuring reproducibility and auditability.

Context is not a simple concatenation of inputs — it is a **compiled artifact** that brings together multiple sources, ranks relevance, manages token budgets, and preserves provenance.

---

## The Three-Source Model

Agent decision context draws from three distinct sources, each serving a different cognitive purpose:

| Source | What the Agent Asks | Nature | Owned By |
|--------|---------------------|--------|----------|
| **Enterprise Knowledge** | *"What should I do?"* | Normative — rules, policies, facts | Hub (Knowledge Integration) |
| **Enterprise Memory** | *"What has been done?"* | Historical — precedent, outcomes, exceptions | Hub (Memory System) |
| **Agent Memory** | *"What have I been doing?"* | Operational — session state, recent interactions | Seer (Agent Runtime) |

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
│  (Hub - RAG)  │     │ (Hub - Memory)  │     │ (Seer Runtime)  │
└───────────────┘     └─────────────────┘     └─────────────────┘
```

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

## Key Principles

- Context is **compiled**, not concatenated
- Every element in context is intentionally included
- Each element has a **source, timestamp, and provenance**
- Context assembly is **inspectable and reproducible**
- Enterprise Memory is a **first-class context source**, not an afterthought

---

## SDK Approach

Seer provides SDKs for use in building Raw Agents. The SDK handles:

### Agent Memory Retrieval
- Episodic memory (recent interactions)
- Semantic memory (learned facts)
- Preference memory (user/context preferences)
- Procedural memory (workflows, skills)

### Enterprise Memory Retrieval
- Decision records (what was decided and why)
- Exception and override history
- Outcome records (what happened after decisions)
- Handoff context (prior agent/human actions on this case)

### Enterprise Knowledge Retrieval
- Policy and rule retrieval (RAG)
- Reference data lookup
- Domain-specific knowledge graphs

### Context Management
- Token budgeting and truncation
- Relevance ranking
- Source attribution

---

## Dependencies

| System | Relationship |
|--------|--------------|
| **Hub Memory System** | Source for Enterprise Memory and Agent Memory persistence |
| **Hub Knowledge Integration** | Source for Enterprise Knowledge (RAG) |
| **Model Gateway** | Token limits inform context truncation |
| **Cognitive Audit Fabric** | Context snapshots feed audit records |

---

## Related

- [Introduction](../introduction.md)
- [Agent Memory Management](../../agentic-ai-concepts/agent-memory-management.md)
- [Knowledge vs Memory vs Context vs Session](../../agentic-ai-concepts/knowledge-memory-context-session.md)
- [Enterprise Knowledge vs Memory vs Agent Memory](../../agentic-ai-concepts/enprise-knowledge-memory-other-data.md)

---

*TODO: Detailed design — retrieval APIs, ranking algorithms, token budgeting strategies, caching*

