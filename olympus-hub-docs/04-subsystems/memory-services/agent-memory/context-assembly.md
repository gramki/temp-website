# Context Assembly Integration

> **Status**: 🔴 Stub — Placeholder for expansion  
> **Last Updated**: 2026-01-07  
> **Parent**: [Agent Memory](./README.md)

---

## Overview

This document describes how **Agent Memory integrates with Seer Context Assembly** — the process by which relevant memory is retrieved and included in an agent's context during processing.

---

## Integration Points

| Integration | Description |
|-------------|-------------|
| **Automatic Retrieval** | Context assembly automatically retrieves relevant agent memory |
| **Memory Selection** | Selects memories based on recency, relevance, and memory class |
| **Context Budget** | Memory competes for space in limited context window |
| **Semantic Matching** | Uses embeddings to find relevant semantic/procedural memories |

---

## Context Assembly Flow

```
Agent Turn Start
        │
        ▼
Seer Context Assembly Engine
        │
        ├── Retrieve Episodic Memory (recent turns, session context)
        ├── Retrieve Semantic Memory (relevant facts about user/context)
        ├── Retrieve Procedural Memory (relevant skills/procedures)
        └── Retrieve Preference Memory (user/agent preferences)
        │
        ▼
Context Compilation
        │
        ▼
Agent Processing
```

---

## TODO

| Item | Priority | Notes |
|------|----------|-------|
| Define memory retrieval strategy | P1 | How memories are selected |
| Define context budget allocation | P2 | How much space for memory vs other context |
| Define relevance scoring | P2 | How relevance is calculated |

---

## Related Documents

- [Agent Memory README](./README.md)
- [Seer Context Assembly Engine](../../../../olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md)

---

*TODO: Detailed integration specification pending Seer context assembly design*

