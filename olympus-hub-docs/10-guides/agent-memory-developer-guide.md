# Agent Memory Developer Guide

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08  
> **Audience**: Developers building agents on Hub

---

## Overview

This guide helps developers effectively use Hub's Agent Memory Services. The key principle: **use your framework's idioms; Hub provides storage, not methodology**.

---

## Table of Contents

1. [Core Philosophy](#core-philosophy)
2. [Quick Start](#quick-start)
3. [Storage Services](#storage-services)
4. [Best Practices](#best-practices)
5. [Common Patterns](#common-patterns)
6. [What NOT to Do](#what-not-to-do)
7. [When to Use Enterprise Memory](#when-to-use-enterprise-memory)
8. [Framework-Specific Examples](#framework-specific-examples)

---

## Core Philosophy

### Hub Enables, Doesn't Prescribe

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│   Your Framework (LangChain, LangGraph, Strands, etc.)                       │
│                                                                              │
│       │  Write memory code in your framework's natural style                │
│       ▼                                                                      │
│                                                                              │
│   Hub Agent Memory Services                                                  │
│                                                                              │
│       • Provides: Persistence, Isolation, Encryption                        │
│       • Does NOT provide: Memory classification, Learning algorithms        │
│       ▼                                                                      │
│                                                                              │
│   Durable, Isolated, Encrypted, Session-Scoped Storage                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Key Points

| Principle | What It Means |
|-----------|---------------|
| **Use framework idioms** | If LangChain uses dictionaries, use dictionaries |
| **No ESPP enforcement** | Hub doesn't require you to classify memory as "Episodic" or "Semantic" |
| **Session-scoped** | All agent memory is bounded by the Request/Session |
| **Isolation guaranteed** | Your agent's memory is private; other agents can't see it |
| **Encryption automatic** | All values encrypted; you don't need to handle this |

---

## Quick Start

### 1. Use the SDK

```python
from hub.agent_memory import kv_store, conversation, log_store, documents

# Store a preference (framework-native style)
await kv_store.put("preferences", "language", "en-US")

# Get it back
lang = await kv_store.get("preferences", "language")
```

### 2. Or Use Tools (for LLM-based agents)

```python
# Your agent can invoke these tools
# agent_memory.kv.save(store="preferences", key="language", value="en-US")
# agent_memory.kv.recall(store="preferences", key="language")
```

### 3. That's It

No configuration needed. No memory classification required. Storage is automatically:
- Persisted (survives restarts)
- Isolated (your agent only)
- Encrypted (you don't see this)
- Session-scoped (cleaned up when session ends)

---

## Storage Services

Hub provides four storage services. Use whichever fits your use case:

| Service | Use Case | Operations |
|---------|----------|------------|
| **KV Store** | Entities, preferences, state | `put`, `get`, `delete`, `list` |
| **Conversation** | Chat history with compaction | `append`, `retrieve`, `compact` |
| **Log Store** | Session audit trail, RAG | `append`, `get_last`, `rag_search` |
| **Documents** | Files, images, PDFs | `store`, `retrieve`, `delete` |

### Choosing a Service

| You Want To... | Use |
|----------------|-----|
| Store key-value pairs | KV Store |
| Track conversation history | Conversation Service |
| Keep an append-only log | Log Store |
| Store files/documents | Document Service |
| Search over past content | Log Store (RAG) or Documents (RAG) |

---

## Best Practices

### 1. Use Logical Store Names

Organize your KV Store with domain-relevant names:

```python
# Good: Business-relevant names
await kv_store.put("customer", "segment", "premium")
await kv_store.put("preferences", "notification_channel", "email")
await kv_store.put("workflow", "current_step", "verification")

# Avoid: Generic or unclear names
await kv_store.put("data", "key1", value)  # What is this?
```

### 2. Configure Conversation Compaction

Don't let conversation history grow unbounded:

```yaml
# In agent specification
memory:
  services:
    - type: conversation
      compaction:
        strategy: summarization  # or sliding_window
        token_budget: 8000
        preserve_recent: 5  # Always keep last 5 messages
```

### 3. Use RAG for Relevant Retrieval

When you need context-relevant information:

```python
# Search log entries semantically
relevant = await log_store.rag_search(
    query="customer complaints about billing",
    limit=5
)

# Search documents
docs = await documents.rag_search(
    query="refund policy",
    limit=3
)
```

### 4. Let Framework Handle Entity Extraction

Hub doesn't extract entities automatically. Use your framework's capabilities:

```python
# LangChain example
from langchain.memory import EntityMemory

# CrewAI example (automatic)
# Entities extracted automatically by CrewAI

# Then store in Hub
for entity_type, entity_value in extracted_entities.items():
    await kv_store.put("entities", entity_type, entity_value)
```

---

## Common Patterns

### Pattern 1: Session State

```python
# Store workflow state
await kv_store.put("workflow", "step", "review")
await kv_store.put("workflow", "approved_by", None)
await kv_store.put("workflow", "pending_items", ["item1", "item2"])

# Retrieve state
current_step = await kv_store.get("workflow", "step")
```

### Pattern 2: User Context

```python
# Store user context learned during session
await kv_store.put("user", "timezone", "America/Los_Angeles")
await kv_store.put("user", "prefers_concise", True)
await kv_store.put("user", "language", "en-US")
```

### Pattern 3: Conversation with Token Budget

```python
# Append messages
await conversation.append({"role": "user", "content": user_message})
await conversation.append({"role": "assistant", "content": response})

# Retrieve within budget for next LLM call
context = await conversation.retrieve(token_budget=4000)
```

### Pattern 4: Document Reference

```python
# User uploads a document
uri = await documents.store(
    content=pdf_bytes,
    content_type="application/pdf",
    metadata={"filename": "contract.pdf"}
)

# Reference in conversation
await conversation.append({
    "role": "user",
    "content": f"Please review this document: {uri}",
    "metadata": {"document_uri": uri}
})
```

### Pattern 5: Context Assembly

```python
async def get_context_for_llm(token_budget: int = 4000):
    """Assemble context from multiple sources."""
    
    # Allocate budget
    conv_budget = int(token_budget * 0.6)  # 60% for conversation
    other_budget = token_budget - conv_budget
    
    # Get conversation history
    messages = await conversation.retrieve(token_budget=conv_budget)
    
    # Get relevant log entries
    log_entries = await log_store.get_last(n=5)
    
    # Get user preferences
    prefs = {
        "timezone": await kv_store.get("user", "timezone"),
        "language": await kv_store.get("user", "language"),
    }
    
    return {
        "messages": messages,
        "recent_log": log_entries,
        "user_preferences": prefs
    }
```

---

## What NOT to Do

### ❌ Don't Store Cross-Session Data

Agent Memory is session-scoped. It will be deleted after the session.

```python
# Wrong: Expecting this to persist across sessions
await kv_store.put("user", "lifetime_value", 50000)  # Will be lost!

# Right: Use Enterprise Memory for cross-session data
# (via Signal Exchange and Cognitive Application)
```

### ❌ Don't Rely on In-Memory State

Hub runtimes don't guarantee VM affinity. Use Hub storage.

```python
# Wrong: In-memory dictionary
self.preferences = {"theme": "dark"}  # May be lost on restart

# Right: Hub storage
await kv_store.put("preferences", "theme", "dark")  # Persisted
```

### ❌ Don't Over-Classify

You don't need to classify memory as "Episodic" or "Semantic."

```python
# Unnecessary: Trying to enforce ESPP in agent memory
await kv_store.put("episodic", "last_action", "approve")
await kv_store.put("semantic", "user_fact", "prefers email")
await kv_store.put("preference", "theme", "dark")

# Better: Use domain-relevant names
await kv_store.put("workflow", "last_action", "approve")
await kv_store.put("user", "contact_preference", "email")
await kv_store.put("settings", "theme", "dark")
```

### ❌ Don't Store PII in Store Names

Store names are validated but not encrypted in metadata.

```python
# Wrong: PII in store name
await kv_store.put("john.doe@email.com", "preference", value)

# Right: Generic store name, PII only in values
await kv_store.put("user", "email", "john.doe@email.com")  # Value is encrypted
```

---

## When to Use Enterprise Memory

| Scenario | Memory Type | Why |
|----------|-------------|-----|
| Session conversation | Agent Memory | Ephemeral, session-scoped |
| In-session preferences | Agent Memory | Will be re-learned next session |
| Temporary workflow state | Agent Memory | Session lifecycle |
| **Cross-session preferences** | **Enterprise Memory** | Must persist |
| **Audit trail** | **Enterprise Memory** | Compliance requirement |
| **Institutional knowledge** | **Enterprise Memory** | Cross-agent sharing |
| **Regulatory records** | **Enterprise Memory** | Long-term retention |

### How to Write to Enterprise Memory

Enterprise Memory writes go through Signal Exchange, not direct SDK:

```python
# This is done by your Hub Application (Cognitive Application)
# Not by the agent directly

# Application attaches memory records to request updates
request_update = {
    "status": "ACTIVE",
    "memory_records": [
        {
            "memory_class": "semantic",
            "record_type": "UserPreference",
            "content": {
                "subject_type": "user",
                "subject_id": "user-123",
                "preference_key": "contact_method",
                "preference_value": "email"
            }
        }
    ]
}
```

---

## Framework-Specific Examples

### LangChain

```python
# LangChain uses memory as a chain component
# Hub provides the storage backend

from hub.agent_memory import kv_store, conversation

# Store entity facts (like EntityMemory)
async def store_entity(entity_type: str, entity_value: dict):
    await kv_store.put("entities", entity_type, entity_value)

# Custom memory class using Hub storage
class HubConversationMemory:
    async def add_message(self, role: str, content: str):
        await conversation.append({"role": role, "content": content})
    
    async def get_messages(self, token_budget: int = 4000):
        return await conversation.retrieve(token_budget=token_budget)
```

### LangGraph

```python
# LangGraph uses typed state
# Hub provides persistence for that state

from typing import TypedDict
from hub.agent_memory import kv_store

class AgentState(TypedDict):
    messages: list
    user_facts: dict
    preferences: dict

# Save state to Hub
async def save_state(state: AgentState):
    await kv_store.put("state", "messages", state["messages"])
    await kv_store.put("state", "user_facts", state["user_facts"])
    await kv_store.put("state", "preferences", state["preferences"])

# Restore state from Hub
async def restore_state() -> AgentState:
    return {
        "messages": await kv_store.get("state", "messages") or [],
        "user_facts": await kv_store.get("state", "user_facts") or {},
        "preferences": await kv_store.get("state", "preferences") or {},
    }
```

### Strands

```python
# Strands has its own state model
# Hub provides the persistence backend

from strands import Agent

# Strands agent with Hub storage integration
# The session manager can be configured to use Hub storage

# For Strands agents running in Hub:
# - agent.state maps to Hub KV Store
# - agent.messages maps to Hub Conversation Service
# - Session persistence is handled by Hub
```

---

## Summary

| Do | Don't |
|----|-------|
| Use your framework's idioms | Force Hub-specific patterns |
| Use logical store names | Over-classify with ESPP |
| Configure conversation compaction | Let history grow unbounded |
| Use RAG for relevant retrieval | Load all history into context |
| Understand session scope | Expect cross-session persistence |
| Use Enterprise Memory for audit | Store compliance data in agent memory |

---

## Related Documentation

- [Agent Memory Services](../04-subsystems/memory-services/agent-memory/README.md) — Technical reference
- [Agent Memory SDK](../04-subsystems/memory-services/agent-memory/sdk.md) — API specification
- [Storage Services](../04-subsystems/memory-services/agent-memory/storage-services.md) — Service details
- [Design Rationale](../04-subsystems/memory-services/agent-memory/design-rationale.md) — Why these decisions
- [Framework Analysis](../04-subsystems/memory-services/agent-memory/framework-reference/README.md) — Industry context
- [ESPP Taxonomy](../04-subsystems/memory-services/shared/espp-taxonomy.md) — Memory type concepts
- [Enterprise Memory](../04-subsystems/memory-services/enterprise-memory/README.md) — Cross-session memory

---

*Use your framework's idioms. Hub provides storage, not methodology.*

