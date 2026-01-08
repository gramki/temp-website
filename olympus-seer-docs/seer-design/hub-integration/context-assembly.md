# Context Assembly for Seer Agents

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08  
> **Parent**: [Seer-Hub Integration](./README.md)

---

## Overview

The **Context Assembly Engine (CAE)** is a Seer service that compiles relevant context for agent reasoning. Unlike pre-compiled context delivery, CAE is **agent-initiated** — the Raw Agent explicitly invokes CAE via SDK or API to assemble context as needed.

---

## CAE Invocation Model

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      AGENT-INITIATED CONTEXT ASSEMBLY                         │
│                                                                               │
│   ┌─────────────────┐                                                        │
│   │ Request Update  │                                                        │
│   │ arrives         │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ Raw Agent       │                                                        │
│   │                 │                                                        │
│   │ 1. Receives     │                                                        │
│   │    update       │                                                        │
│   │ 2. Decides to   │                                                        │
│   │    compile      │                                                        │
│   │    context      │                                                        │
│   │ 3. Invokes CAE  │────────────────────────┐                               │
│   │                 │                         │                               │
│   └─────────────────┘                         │                               │
│                                               ▼                               │
│                                      ┌─────────────────┐                     │
│                                      │ Context Assembly│                     │
│                                      │ Engine (CAE)    │                     │
│                                      │                 │                     │
│                                      │ 1. Retrieves    │                     │
│                                      │    from sources │                     │
│                                      │ 2. Ranks &      │                     │
│                                      │    filters      │                     │
│                                      │ 3. Truncates    │                     │
│                                      │    to budget    │                     │
│                                      │ 4. Returns      │                     │
│                                      │    context      │                     │
│                                      └────────┬────────┘                     │
│                                               │                               │
│            ┌──────────────────────────────────┘                              │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ Raw Agent       │                                                        │
│   │                 │                                                        │
│   │ 4. Receives     │                                                        │
│   │    context      │                                                        │
│   │ 5. May augment  │                                                        │
│   │    further      │                                                        │
│   │ 6. Proceeds     │                                                        │
│   │    with task    │                                                        │
│   └─────────────────┘                                                        │
│                                                                               │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Key Design Point

> **CAE is a service that needs to be explicitly invoked by the Raw Agent.** The agent chooses when and how to use CAE, and can augment the compiled context as needed.

---

## CAE SDK Usage

### Basic Invocation

```python
from seer_sdk import ContextAssemblyEngine

cae = ContextAssemblyEngine.from_environment()

# Compile context for current request update
context = cae.compile(
    request_id=invocation.request.request_id,
    update_id=invocation.update.update_id,
    token_budget=8000
)

print(context.precedents)    # Similar past cases
print(context.case_history)  # Current case context
print(context.policies)      # Relevant policies
```

### With Specific Retrievers

```python
context = cae.compile(
    request_id=request.id,
    update_id=update.id,
    retrievers=[
        # Enterprise Memory - Precedents
        {
            "type": "memory.precedent",
            "query": "unauthorized transaction disputes",
            "limit": 5
        },
        # Enterprise Memory - Case History
        {
            "type": "memory.case_history",
            "case_id": case.id
        },
        # Knowledge Bank - Policies
        {
            "type": "knowledge.search",
            "knowledge_base": "dispute-policies",
            "query": "chargeback eligibility",
            "limit": 3
        },
        # Agent Memory - Session Context
        {
            "type": "agent_memory.log",
            "store": "session-audit",
            "query": "recent actions",
            "limit": 10
        }
    ],
    ranking={
        "strategy": "relevance",
        "recency_boost": 0.2
    },
    token_budget=8000
)
```

---

## Context Sources

CAE can retrieve from multiple Hub sources:

| Source | Type | Description |
|--------|------|-------------|
| **Enterprise Memory** | `memory.precedent` | Similar past cases (Episodic) |
| **Enterprise Memory** | `memory.case_history` | Current case records (Episodic) |
| **Enterprise Memory** | `memory.patterns` | Learned patterns (Semantic) |
| **Enterprise Memory** | `memory.procedures` | Known procedures (Procedural) |
| **Knowledge Bank** | `knowledge.search` | Policy documents, guidelines |
| **Agent Memory** | `agent_memory.*` | Session-scoped context |
| **Request Context** | `request.context` | Current request updates |

---

## Compilation Pipeline

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      CAE COMPILATION PIPELINE                                 │
│                                                                               │
│   ┌─────────────────┐                                                        │
│   │ 1. RETRIEVAL    │                                                        │
│   │                 │                                                        │
│   │ Execute each    │                                                        │
│   │ retriever in    │                                                        │
│   │ parallel        │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ 2. RANKING      │                                                        │
│   │                 │                                                        │
│   │ Score by:       │                                                        │
│   │ • Relevance     │                                                        │
│   │ • Recency       │                                                        │
│   │ • Source weight │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ 3. FILTERING    │                                                        │
│   │                 │                                                        │
│   │ Remove:         │                                                        │
│   │ • Duplicates    │                                                        │
│   │ • Below threshold                                                        │
│   │ • Irrelevant    │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ 4. TRUNCATION   │                                                        │
│   │                 │                                                        │
│   │ Fit to token    │                                                        │
│   │ budget:         │                                                        │
│   │ • Prioritize    │                                                        │
│   │ • Summarize     │                                                        │
│   │ • Trim          │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ 5. PROVENANCE   │                                                        │
│   │                 │                                                        │
│   │ Attach source   │                                                        │
│   │ metadata:       │                                                        │
│   │ • Source ID     │                                                        │
│   │ • Retrieval time│                                                        │
│   │ • Confidence    │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ COMPILED        │                                                        │
│   │ CONTEXT         │                                                        │
│   └─────────────────┘                                                        │
│                                                                               │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Response Structure

```python
@dataclass
class CompiledContext:
    # Compiled content by source type
    precedents: List[PrecedentRecord]
    case_history: List[EpisodicRecord]
    policies: List[PolicyChunk]
    session_context: List[SessionEntry]
    
    # Metadata
    token_count: int
    budget_remaining: int
    compilation_time_ms: int
    
    # Provenance
    sources: List[SourceMetadata]
    
    # Raw text (for direct LLM injection)
    as_text: str
    
    # Structured (for agent processing)
    as_dict: Dict[str, Any]
```

### Example Response

```json
{
  "precedents": [
    {
      "case_id": "case-2025-12345",
      "outcome": "approved",
      "similarity_score": 0.92,
      "summary": "Similar velocity pattern, approved after merchant verification"
    }
  ],
  "case_history": [
    {
      "record_type": "decision",
      "timestamp": "2026-01-08T14:00:00Z",
      "decision": "escalate_for_review",
      "rationale": "High transaction amount"
    }
  ],
  "policies": [
    {
      "source": "dispute-policies/chargeback-rules.md",
      "chunk": "Transactions over $5000 require manager approval...",
      "relevance_score": 0.88
    }
  ],
  "token_count": 3200,
  "budget_remaining": 4800
}
```

---

## Agent Augmentation

After receiving compiled context, agents can augment:

```python
# Get CAE-compiled context
context = cae.compile(request_id=request.id, ...)

# Agent-specific augmentation
augmented_context = {
    **context.as_dict,
    
    # Add agent-specific reasoning
    "current_hypothesis": analyze_patterns(context.precedents),
    
    # Add tool results
    "transaction_data": get_transaction_details(case.transaction_id),
    
    # Add session state
    "conversation_summary": memory.conversation.get_summary("case-dialog")
}

# Use augmented context for LLM
response = llm.complete(
    system_prompt=training.system_prompt,
    context=augmented_context,
    user_message=update.payload.message
)
```

---

## When to Use CAE

| Scenario | Use CAE? | Rationale |
|----------|----------|-----------|
| **New case received** | ✅ Yes | Need precedents, policies |
| **Simple acknowledgment** | ❌ No | No reasoning needed |
| **User asks question** | ✅ Yes | May need policy lookup |
| **Tool result received** | Maybe | Depends on next action |
| **Generating final decision** | ✅ Yes | Need full context |

### Agent Training Guidance

```
# In system prompt
When you receive a request update:
1. Assess if you need additional context
2. If reasoning required, invoke CAE with relevant retrievers
3. Augment with session-specific information
4. Proceed with response generation
```

---

## Performance Considerations

| Aspect | Guidance |
|--------|----------|
| **Parallel retrieval** | CAE retrieves from sources in parallel |
| **Caching** | CAE caches recent retrievals per request |
| **Token budget** | Set appropriate budget to avoid over-retrieval |
| **Selective retrieval** | Only request sources you need |

### Caching

```python
# First call - full retrieval
context1 = cae.compile(request_id=req.id, retrievers=[...])

# Second call (same request) - may use cache
context2 = cae.compile(request_id=req.id, retrievers=[...])

# Force fresh retrieval
context3 = cae.compile(request_id=req.id, retrievers=[...], cache=False)
```

---

## Traceability

Every CAE invocation is traced:

| Trace Field | Description |
|-------------|-------------|
| `cae_invocation_id` | Unique CAE call ID |
| `request_id` | Hub Request |
| `agent_id` | Invoking agent |
| `retrievers` | Sources queried |
| `token_count` | Tokens returned |
| `sources` | Source provenance |

Traces stored in agent observability logs and can be correlated with Hub request history.

---

## Related Documentation

- [Context Assembly Engine](../subsystems/context-assembly-engine.md) — Full CAE design
- [Memory Integration](./memory-integration.md) — Agent Memory as CAE source
- [Enterprise Memory Access Tools](../../../olympus-hub-docs/04-subsystems/memory-services/enterprise-memory/access-tools.md) — Memory retrieval
- [Knowledge Bank](../../../olympus-hub-docs/04-subsystems/knowledge-bank/README.md) — Policy retrieval

---

*Context Assembly Engine provides agent-initiated context compilation, retrieving from Hub's memory and knowledge services.*

