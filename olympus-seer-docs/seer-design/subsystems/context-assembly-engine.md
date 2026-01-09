# Context Assembly Engine

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08

## Overview

The Context Assembly Engine (CAE) constructs the **complete context** for each agent reasoning step, ensuring reproducibility and auditability.

Context is not a simple concatenation of inputs — it is a **compiled artifact** that brings together multiple sources, ranks relevance, manages token budgets, and preserves provenance.

**Key Design Point**: CAE is a **service that agents explicitly invoke** — it does not pre-compile context. Agents choose when and how to use CAE, and can augment the compiled context as needed.

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

## CAE API

### Base URL

```
https://seer-cae.olympus.io/v1
```

### Compile Context

```http
POST /compile
```

Main endpoint for context assembly.

**Request:**
```json
{
  "request_id": "req-abc123",
  "update_id": "upd-xyz789",
  "agent_id": "emp-fraud-analyst-001",
  
  "retrievers": [
    {
      "type": "memory.precedent",
      "query": "unauthorized transaction disputes",
      "limit": 5,
      "minScore": 0.7
    },
    {
      "type": "memory.case_history",
      "case_id": "case-12345"
    },
    {
      "type": "knowledge.search",
      "knowledge_base": "dispute-policies",
      "query": "chargeback eligibility criteria",
      "limit": 3
    },
    {
      "type": "agent_memory.conversation",
      "store": "case-dialog",
      "last_n": 10
    },
    {
      "type": "agent_memory.kv",
      "store": "case-entities",
      "keys": ["fraud_assessment", "customer_profile"]
    }
  ],
  
  "ranking": {
    "strategy": "relevance",
    "recencyBoost": 0.2,
    "sourceWeights": {
      "memory.precedent": 1.0,
      "knowledge.search": 0.8,
      "agent_memory": 0.9
    }
  },
  
  "tokenBudget": {
    "total": 8000,
    "allocation": {
      "precedents": 2000,
      "case_history": 1500,
      "policies": 2000,
      "conversation": 1500,
      "entities": 500,
      "reserve": 500
    }
  },
  
  "options": {
    "includeProvenance": true,
    "cache": true,
    "summarizeOverflow": true
  }
}
```

**Response:**
```json
{
  "compilationId": "cmp-123e4567",
  "timestamp": "2026-01-08T14:30:00Z",
  
  "context": {
    "precedents": [
      {
        "case_id": "case-2025-12345",
        "outcome": "approved",
        "similarity_score": 0.92,
        "summary": "Similar velocity pattern, approved after merchant verification",
        "provenance": {
          "source": "enterprise_memory.episodic",
          "retrieved_at": "2026-01-08T14:30:00.100Z",
          "record_id": "ep-rec-789"
        }
      }
    ],
    "case_history": [...],
    "policies": [...],
    "conversation": [...],
    "entities": {...}
  },
  
  "metadata": {
    "tokenCount": 7200,
    "budgetRemaining": 800,
    "compilationTimeMs": 250,
    "retrievalStats": {
      "sources_queried": 5,
      "records_retrieved": 28,
      "records_included": 15,
      "records_truncated": 8,
      "records_excluded": 5
    }
  },
  
  "provenance": [
    {
      "source": "enterprise_memory.episodic",
      "query": "unauthorized transaction disputes",
      "records_returned": 5,
      "latency_ms": 45
    },
    {
      "source": "knowledge_bank.dispute-policies",
      "query": "chargeback eligibility criteria",
      "chunks_returned": 3,
      "latency_ms": 80
    }
  ],
  
  "asText": "## Precedents\n\n### Case 2025-12345 (Similarity: 0.92)\n...",
  
  "asDict": {
    "precedents": [...],
    "policies": [...],
    "conversation": [...]
  }
}
```

### Retriever Types

| Type | Source | Description |
|------|--------|-------------|
| `memory.precedent` | Enterprise Memory (Episodic) | Similar past cases |
| `memory.case_history` | Enterprise Memory (Episodic) | Current case records |
| `memory.patterns` | Enterprise Memory (Semantic) | Learned patterns |
| `memory.procedures` | Enterprise Memory (Procedural) | Known procedures |
| `memory.preferences` | Enterprise Memory (Preference) | User/agent preferences |
| `knowledge.search` | Knowledge Bank | Policy documents (RAG) |
| `knowledge.rules` | Knowledge Bank | Structured rules |
| `agent_memory.conversation` | Agent Memory | Session conversation |
| `agent_memory.log` | Agent Memory | Session audit log |
| `agent_memory.kv` | Agent Memory | Key-value entities |
| `agent_memory.documents` | Agent Memory | Session documents |
| `request.context` | Hub Request | Current request updates |

---

## Ranking Algorithms

### Relevance Ranking

Default ranking strategy combining multiple signals:

```
score = (semantic_score * 0.6) + (recency_score * 0.2) + (source_weight * 0.2)
```

**Configuration:**
```json
{
  "ranking": {
    "strategy": "relevance",
    "recencyBoost": 0.2,
    "recencyDecay": "exponential",
    "recencyHalfLife": 86400,
    "sourceWeights": {
      "memory.precedent": 1.0,
      "memory.case_history": 1.2,
      "knowledge.search": 0.8
    }
  }
}
```

### Priority Ranking

Fixed priority ordering:

```json
{
  "ranking": {
    "strategy": "priority",
    "order": [
      "request.context",
      "agent_memory.conversation",
      "memory.case_history",
      "memory.precedent",
      "knowledge.search"
    ]
  }
}
```

### Custom Ranking

Agent-defined ranking function:

```json
{
  "ranking": {
    "strategy": "custom",
    "rankerRef": "fraud-case-ranker-v1"
  }
}
```

---

## Token Budgeting

### Allocation Strategies

**Fixed Allocation:**
```json
{
  "tokenBudget": {
    "total": 8000,
    "allocation": {
      "precedents": 2000,
      "case_history": 1500,
      "policies": 2000,
      "conversation": 1500,
      "reserve": 1000
    }
  }
}
```

**Proportional Allocation:**
```json
{
  "tokenBudget": {
    "total": 8000,
    "strategy": "proportional",
    "weights": {
      "precedents": 2,
      "case_history": 1.5,
      "policies": 2,
      "conversation": 1.5
    },
    "reserve": 1000
  }
}
```

**Dynamic Allocation:**
```json
{
  "tokenBudget": {
    "total": 8000,
    "strategy": "dynamic",
    "priorities": ["request.context", "agent_memory", "memory", "knowledge"],
    "reserve": 1000
  }
}
```

### Overflow Handling

When content exceeds allocated budget:

| Strategy | Description |
|----------|-------------|
| `truncate` | Cut off at budget limit |
| `summarize` | LLM-based summarization |
| `compress` | Remove low-value content |
| `paginate` | Return first page, indicate more available |

```json
{
  "tokenBudget": {
    "total": 8000,
    "overflow": {
      "strategy": "summarize",
      "summarizer": "gpt-4o-mini",
      "targetRatio": 0.5
    }
  }
}
```

---

## SDK

### Python SDK

```python
from seer_sdk import ContextAssemblyEngine

cae = ContextAssemblyEngine.from_environment()

# Basic compilation
context = cae.compile(
    request_id="req-abc123",
    update_id="upd-xyz789",
    token_budget=8000
)

# With specific retrievers
context = cae.compile(
    request_id="req-abc123",
    retrievers=[
        cae.retrievers.memory_precedent(
            query="unauthorized transaction",
            limit=5
        ),
        cae.retrievers.knowledge_search(
            knowledge_base="dispute-policies",
            query="chargeback rules",
            limit=3
        ),
        cae.retrievers.agent_memory_conversation(
            store="case-dialog",
            last_n=10
        )
    ],
    ranking=cae.ranking.relevance(recency_boost=0.2),
    token_budget=8000
)

# Access compiled context
print(context.precedents)
print(context.as_text)
print(context.metadata.token_count)

# Check provenance
for source in context.provenance:
    print(f"{source.type}: {source.records_returned} records in {source.latency_ms}ms")
```

### Async Compilation

```python
import asyncio
from seer_sdk import ContextAssemblyEngine

cae = ContextAssemblyEngine.from_environment()

async def compile_context():
    context = await cae.compile_async(
        request_id="req-abc123",
        retrievers=[...],
        token_budget=8000
    )
    return context

context = asyncio.run(compile_context())
```

### Caching

```python
# First call - full retrieval
context1 = cae.compile(request_id="req-abc123", ...)

# Second call - may use cache (same request)
context2 = cae.compile(request_id="req-abc123", ...)

# Force fresh retrieval
context3 = cae.compile(request_id="req-abc123", ..., cache=False)

# Clear cache for request
cae.cache.invalidate(request_id="req-abc123")
```

---

## Hub Memory Integration

### Enterprise Memory Access

CAE uses Hub Memory Access Tools under the hood:

| CAE Retriever | Hub Memory Tool |
|---------------|-----------------|
| `memory.precedent` | `memory.search_precedent` |
| `memory.case_history` | `memory.get_case_history` |
| `memory.patterns` | `memory.get_patterns` |

### Agent Memory Access

CAE accesses Agent Memory via SDK:

```python
# CAE internally calls:
from hub_memory_sdk import AgentMemory

memory = AgentMemory.from_environment()
conversation = memory.conversation.get_last("case-dialog", n=10)
entities = memory.kv.get_many("case-entities", ["fraud_assessment", "customer_profile"])
```

### Knowledge Bank Access

CAE uses Hub Knowledge Bank API:

```python
# CAE internally calls:
from hub_knowledge_sdk import KnowledgeBank

kb = KnowledgeBank.from_environment()
chunks = kb.search(
    knowledge_base="dispute-policies",
    query="chargeback eligibility",
    top_k=3
)
```

---

## Observability

### Metrics

| Metric | Description |
|--------|-------------|
| `cae_compile_duration_seconds` | Context compilation time |
| `cae_retrieval_duration_seconds` | Per-source retrieval time |
| `cae_tokens_used` | Tokens in compiled context |
| `cae_records_retrieved` | Records retrieved per source |
| `cae_cache_hit_rate` | Cache effectiveness |

### Tracing

Every compilation includes trace context:

```json
{
  "traceId": "trace-abc123",
  "spanId": "span-cae-001",
  "parentSpanId": "span-agent-001",
  "operation": "context.compile",
  "duration": 250,
  "spans": [
    {"name": "retrieve.memory.precedent", "duration": 45},
    {"name": "retrieve.knowledge.search", "duration": 80},
    {"name": "rank", "duration": 20},
    {"name": "truncate", "duration": 15},
    {"name": "format", "duration": 10}
  ]
}
```

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
- [Context Assembly in Hub Integration](../hub-integration/context-assembly.md) — Agent invocation patterns
- [Agent Memory Management](../../agentic-ai-concepts/agent-memory/agent-memory-management.md)
- [Knowledge vs Memory vs Context vs Session](../../agentic-ai-concepts/agent-memory/knowledge-memory-context-session.md)
- [Enterprise Knowledge vs Memory vs Agent Memory](../../agentic-ai-concepts/enterprise-knowledge-memory-other-data.md)
- [Hub Memory Services](../../../olympus-hub-docs/04-subsystems/memory-services/README.md)
- [Hub Knowledge Services](../../../olympus-hub-docs/04-subsystems/knowledge-services/README.md)

