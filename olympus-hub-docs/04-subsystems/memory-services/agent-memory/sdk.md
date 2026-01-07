# Agent Memory SDK

> **Status**: 🔴 Stub — Placeholder for expansion  
> **Last Updated**: 2026-01-07  
> **Parent**: [Agent Memory](./README.md)

---

## Overview

The **Agent Memory SDK** provides programmatic access to Agent Memory for Hub agents and applications. Unlike Enterprise Memory (which uses Memory Access Tools), Agent Memory supports direct SDK access for both reads and writes.

---

## API Surface (Conceptual)

```python
from hub.memory import agent_memory

# ============================================================
# WRITE OPERATIONS
# ============================================================

# Remember a fact (semantic memory)
await agent_memory.remember(
    agent_id="agent-support-001",
    memory_type="semantic",
    content={"user_prefers": "email", "timezone": "PST"},
    ttl_days=30
)

# Store session context (episodic memory)
await agent_memory.store_context(
    agent_id="agent-support-001",
    session_id="session-12345",
    context={
        "recent_turns": [...],
        "current_intent": "resolve_billing_issue"
    }
)

# ============================================================
# READ OPERATIONS
# ============================================================

# Recall by query (semantic search)
preferences = await agent_memory.recall(
    agent_id="agent-support-001",
    memory_type="semantic",
    query="user communication preferences"
)

# Get session context
context = await agent_memory.get_context(
    agent_id="agent-support-001",
    session_id="session-12345"
)

# ============================================================
# DELETE OPERATIONS
# ============================================================

# Forget specific memory
await agent_memory.forget(
    agent_id="agent-support-001",
    memory_id="mem-xyz789"
)

# Clear all memory for subject (data subject request)
await agent_memory.clear_subject(
    subject_id="user-john-doe",
    reason="gdpr_erasure_request"
)
```

---

## TODO

| Item | Priority | Notes |
|------|----------|-------|
| Define full API surface | P1 | All CRUD operations |
| Define scoping model | P1 | Agent vs session vs subject |
| Define authentication | P1 | How SDK authenticates |
| Define error handling | P2 | Error codes and recovery |
| Seer integration | P2 | How Seer runtime uses SDK |

---

*TODO: Full SDK specification pending storage backend decision*

