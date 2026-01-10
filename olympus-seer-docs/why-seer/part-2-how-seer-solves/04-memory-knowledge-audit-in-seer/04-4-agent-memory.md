# 4.4 Agent Memory in Seer

Agent Memory supports an agent's immediate operational needs within a session. Unlike Enterprise Memory, it is ephemeral, session-scoped, and designed for the practical requirements of in-flight agent operations.

## What Agent Memory Supports

Agent Memory answers the question: **"What does the agent need to work with right now?"**

| Memory Type | Examples | Retention |
|-------------|----------|-----------|
| **Conversation history** | Recent turns, user statements | Session + 48 hours |
| **Session state** | Extracted entities, current step | Session + 24 hours |
| **Working hypotheses** | Agent's current understanding | Session only |
| **Tool results** | Recent API responses, lookups | Session + 72 hours |
| **Preferences** | User's stated preferences | Session + 90 days |

## Agent Memory Architecture

Hub's Agent Memory provides four storage services:

```
┌─────────────────────────────────────────────────────────────┐
│                      AGENT MEMORY                            │
│                                                              │
│   ┌─────────────────┐    ┌─────────────────────────────┐   │
│   │   KV STORE      │    │      LOG SERVICE            │   │
│   │                 │    │                             │   │
│   │  • Key-value    │    │  • Append-only events       │   │
│   │  • Fast CRUD    │    │  • RAG searchable           │   │
│   │  • Session      │    │  • Time-ordered             │   │
│   │    state        │    │                             │   │
│   └─────────────────┘    └─────────────────────────────┘   │
│                                                              │
│   ┌─────────────────┐    ┌─────────────────────────────┐   │
│   │ CONVERSATION    │    │    DOCUMENT STORE           │   │
│   │   SERVICE       │    │                             │   │
│   │                 │    │  • Larger documents         │   │
│   │  • Turn-based   │    │  • Vector indexed           │   │
│   │  • Compaction   │    │  • Content-addressable      │   │
│   │  • Summaries    │    │                             │   │
│   └─────────────────┘    └─────────────────────────────┘   │
│                                                              │
│   Isolation: (tenant, workbench, scenario, request, agent)   │
│   Retention: Session + configured period                     │
│   PII: Permitted (within session scope)                      │
│   Encryption: Agent+session unique keys                      │
└─────────────────────────────────────────────────────────────┘
```

## Storage Services

### KV Store

Fast key-value storage for session state:

```python
# Store session state
agent_memory.kv.set("current_step", "verify_merchant")
agent_memory.kv.set("extracted_entities", {
    "transaction_id": "txn-12345",
    "merchant": "ACME Store",
    "amount": 450.00
})

# Retrieve later
current_step = agent_memory.kv.get("current_step")
```

### Log Service

Append-only event log with RAG search:

```python
# Log events
agent_memory.log.append({
    "event": "tool_invocation",
    "tool": "get_transaction_details",
    "result_summary": "Transaction found, merchant error confirmed"
})

# Search logs
relevant = agent_memory.log.search(
    query="merchant error",
    limit=5
)
```

### Conversation Service

Manages conversation history with compaction:

```python
# Automatic turn management
agent_memory.conversation.add_turn(
    role="user",
    content="I want to dispute this charge"
)
agent_memory.conversation.add_turn(
    role="assistant",
    content="I'd be happy to help. Can you tell me which transaction?"
)

# Compaction for long conversations
agent_memory.conversation.compact(
    strategy="summarization",
    token_budget=4000
)
```

### Document Store

Vector-indexed storage for larger content:

```python
# Store document for later retrieval
agent_memory.documents.store(
    content=transaction_history,
    metadata={"type": "transaction_history", "customer": "cust-12345"}
)

# Semantic search
relevant_docs = agent_memory.documents.search(
    query="prior disputes with this merchant",
    limit=3
)
```

## Key Differences from Enterprise Memory

| Aspect | Agent Memory | Enterprise Memory |
|--------|--------------|-------------------|
| **Scope** | Session/request | Organizational |
| **Retention** | Hours to days | 7+ years |
| **PII** | Permitted | Prohibited |
| **Mutability** | Update/delete allowed | Immutable |
| **Write path** | Direct SDK access | Via Signal Exchange |
| **ESPP enforcement** | Optional | Required |
| **Isolation** | Per-agent, per-session | Workbench-scoped |

## PII Handling

Agent Memory can contain PII because:
- Session scope limits exposure window
- Encryption with agent+session unique keys
- Short retention enables erasure compliance
- Isolated storage prevents cross-session leakage

```yaml
agent_memory_config:
  pii_handling:
    permitted: true
    encryption: aes-256-gcm
    key_scope: agent_session
    retention_max: 72h
```

## Integration with Context Assembly

Seer's Context Assembly Engine retrieves from Agent Memory:

```yaml
context_frame:
  working_state:
    - source: agent_memory/kv
      key: current_step
      value: verify_merchant
      
  recent_episodes:
    - source: agent_memory/log
      summary: "Tool call to get_transaction returned merchant error"
      timestamp: 2026-01-10T14:28:00Z
      
  conversation_context:
    - source: agent_memory/conversation
      turns: 4
      summary: "Customer disputing $450 charge at ACME Store"
```

## Promotion to Enterprise Memory

Agent Memory content can be promoted to Enterprise Memory through explicit action:

1. Agent identifies cross-session value
2. Developer writes to Signal Exchange
3. Record enters Enterprise Memory with proper governance

```python
# Promote significant finding to Enterprise Memory
if decision.is_significant:
    signal_exchange.emit(
        record_type="decision_record",
        content=decision.to_enterprise_format(),
        case_id=case_id
    )
```

---

**References:**
*   `olympus-hub-docs/04-subsystems/memory-services/agent-memory/README.md`
*   `olympus-hub-docs/04-subsystems/memory-services/agent-memory/storage-services.md`
*   `olympus-seer-docs/agentic-ai-concepts/agent-memory/agent-memory-management.md`
