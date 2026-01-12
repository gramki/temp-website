# Context Assembly for Seer Agents

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-12  
> **Parent**: [Seer-Hub Integration](./README.md)

---

## Overview

The **Context Compilation Service** (formerly Context Assembly Engine/CAE) is a Seer service that compiles relevant context for agent reasoning. Unlike pre-compiled context delivery, the service is **agent-initiated** — the Raw Agent explicitly invokes it via SDK or API to assemble context as needed.

---

## Context Compilation Service Invocation Model

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      AGENT-INITIATED CONTEXT COMPILATION                       │
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
│   │ 3. Invokes      │────────────────────────┐                               │
│   │    Context      │                         │                               │
│   │    Compilation  │                         │                               │
│   │    Service      │                         │                               │
│   └─────────────────┘                         │                               │
│                                               ▼                               │
│                                      ┌─────────────────┐                     │
│                                      │ Context         │                     │
│                                      │ Compilation     │                     │
│                                      │ Service         │                     │
│                                      │                 │                     │
│                                      │ 1. Matches      │                     │
│                                      │    Training Spec│                     │
│                                      │    selectors    │                     │
│                                      │ 2. Retrieves    │                     │
│                                      │    from 4       │                     │
│                                      │    sources      │                     │
│                                      │ 3. Incorporates  │                     │
│                                      │    tools        │                     │
│                                      │ 4. Ranks &      │                     │
│                                      │    filters      │                     │
│                                      │ 5. Truncates    │                     │
│                                      │    to budget    │                     │
│                                      │ 6. Returns      │                     │
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

### Key Design Points

> **Context Compilation Service is explicitly invoked by the Raw Agent.** The agent chooses when to invoke compilation, and the service automatically applies Training Spec retriever configurations based on the incoming request update metadata. Agents can augment the compiled context as needed.

---

## Context Compilation Service SDK Usage

### Basic Invocation (Automatic Retriever Selection)

The Context Compilation Service automatically selects retrievers based on Training Spec selector criteria matching request update metadata. Agents only need to provide `request_id` and `update_id`:

```python
from seer_sdk import ContextCompiler

compiler = ContextCompiler.from_environment()

# Compile context for current request update
# Retrievers are automatically selected from Training Spec
# based on update metadata (updateType, taskType, contextKeys, etc.)
context = compiler.compile(
    request_id=invocation.request.request_id,
    update_id=invocation.update.update_id
)

print(context.precedents)    # Similar past cases
print(context.case_history)  # Current case context
print(context.policies)      # Relevant policies
print(context.request_context)  # Request hierarchy context
```

### With Optional Overrides

Agents can optionally override token budgets or disable caching:

```python
context = compiler.compile(
    request_id=request.id,
    update_id=update.id,
    token_budget_override=10000,  # Override total budget
    cache=False  # Force fresh retrieval
)
```

**Note**: Retrievers are automatically selected from Training Spec retriever configurations. The service:
1. Loads Training Spec retriever configurations with selectors
2. Matches request update metadata against selector criteria
3. Merges all matching configurations
4. Executes retrievers automatically

---

## Four-Source Compilation

The Context Compilation Service assembles context from four distinct sources:

| Source | What the Agent Asks | Nature | Owned By |
|--------|---------------------|--------|----------|
| **Enterprise Knowledge** | *"What should I do?"* | Normative — rules, policies, facts | Hub (Knowledge Services) |
| **Enterprise Memory** | *"What has been done?"* | Historical — precedent, outcomes, exceptions | Hub (Memory Services) |
| **Agent Memory** | *"What have I been doing?"* | Operational — session state, recent interactions | Hub (Memory Services) |
| **Hub Request Context** | *"What is the request context chain?"* | Hierarchical — current request + all ancestors | Hub (Request Management) |

### Request Hierarchy Integration

The service traverses the request hierarchy/ancestry topology to access context from all requestors in the ancestry chain:

```
Root Request (depth=0)
├── Child Request (depth=1)
│   └── Grandchild Request (depth=2) ← Current Request
```

**Ancestry Traversal**:
- Retrieves context from current request
- Traverses up the hierarchy to root request
- Accesses context records from each ancestor request
- Applies goal and role-based filtering to determine which ancestor contexts are relevant

**Goal and Role-Based Filtering**:
- Agent goal (from Training Spec) determines which ancestor contexts align with the agent's purpose
- Agent role (from Training Spec) determines which ancestor contexts are within the agent's responsibility scope
- Only relevant ancestor contexts are included in compilation
- Filtering prevents information overload and ensures context relevance

### Tool-Aware Compilation

The service incorporates available tools (from Training/Employment Specs) into context constraints and uses tool capabilities to influence context retrieval and ranking:

- Loads tool bindings from Employment Spec
- Loads tool metadata (capabilities, schemas) from Tool Registry
- Includes tool allowlist in context constraints section
- Tool capabilities influence context retrieval (e.g., if a tool can query a database, reduce redundant context about that data)

---

## Compilation Pipeline

```
┌──────────────────────────────────────────────────────────────────────────────┐
│              CONTEXT COMPILATION SERVICE PIPELINE                             │
│                                                                               │
│   ┌─────────────────┐                                                        │
│   │ 0. SELECTOR      │                                                        │
│   │    MATCHING      │                                                        │
│   │                 │                                                        │
│   │ Match request   │                                                        │
│   │ update metadata │                                                        │
│   │ against Training│                                                        │
│   │ Spec selectors  │                                                        │
│   │ Merge matching  │                                                        │
│   │ configs         │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ 1. RETRIEVAL    │                                                        │
│   │                 │                                                        │
│   │ From 4 sources: │                                                        │
│   │ • Enterprise    │                                                        │
│   │   Knowledge     │                                                        │
│   │ • Enterprise     │                                                        │
│   │   Memory        │                                                        │
│   │ • Agent Memory   │                                                        │
│   │ • Request        │                                                        │
│   │   Hierarchy     │                                                        │
│   │ Execute each     │                                                        │
│   │ retriever in     │                                                        │
│   │ parallel         │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ 2. TOOL          │                                                        │
│   │    INTEGRATION   │                                                        │
│   │                 │                                                        │
│   │ Incorporate     │                                                        │
│   │ tools into      │                                                        │
│   │ constraints     │                                                        │
│   │ Use tool        │                                                        │
│   │ capabilities to │                                                        │
│   │ influence       │                                                        │
│   │ retrieval       │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ 3. RANKING       │                                                        │
│   │                 │                                                        │
│   │ Score by:       │                                                        │
│   │ • Relevance     │                                                        │
│   │ • Recency       │                                                        │
│   │ • Source weight │                                                        │
│   │ • Goal/role     │                                                        │
│   │   filtering     │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ 4. FILTERING     │                                                        │
│   │                 │                                                        │
│   │ Remove:         │                                                        │
│   │ • Duplicates    │                                                        │
│   │ • Below threshold                                                        │
│   │ • Irrelevant    │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ 5. TRUNCATION    │                                                        │
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
│   │ 6. PROVENANCE    │                                                        │
│   │                 │                                                        │
│   │ Attach source   │                                                        │
│   │ metadata:       │                                                        │
│   │ • Source ID     │                                                        │
│   │ • Retrieval time│                                                        │
│   │ • Confidence    │                                                        │
│   │ • Version info  │                                                        │
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
# Get Context Compilation Service-compiled context
context = compiler.compile(
    request_id=request.id,
    update_id=update.id
)

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

## When to Use Context Compilation Service

| Scenario | Use Service? | Rationale |
|----------|--------------|-----------|
| **New case received** | ✅ Yes | Need precedents, policies, request hierarchy |
| **Simple acknowledgment** | ❌ No | No reasoning needed |
| **User asks question** | ✅ Yes | May need policy lookup, case history |
| **Tool result received** | Maybe | Depends on next action |
| **Generating final decision** | ✅ Yes | Need full context from all sources |

### Agent Training Guidance

```
# In system prompt
When you receive a request update:
1. Assess if you need additional context
2. If reasoning required, invoke Context Compilation Service
   (retrievers are automatically selected from Training Spec)
3. Augment with session-specific information
4. Proceed with response generation
```

---

## Performance Considerations

| Aspect | Guidance |
|--------|----------|
| **Parallel retrieval** | Service retrieves from sources in parallel |
| **Caching** | Service caches recent retrievals per request |
| **Token budget** | Training Spec defines budgets; can override if needed |
| **Automatic selection** | Retrievers automatically selected based on update metadata |

### Caching

```python
# First call - full retrieval
context1 = compiler.compile(
    request_id=req.id,
    update_id=update.id
)

# Second call (same request) - may use cache
context2 = compiler.compile(
    request_id=req.id,
    update_id=update.id
)

# Force fresh retrieval
context3 = compiler.compile(
    request_id=req.id,
    update_id=update.id,
    cache=False
)
```

---

## Traceability

Every Context Compilation Service invocation is traced:

| Trace Field | Description |
|-------------|-------------|
| `compilation_id` | Unique compilation call ID |
| `request_id` | Hub Request |
| `update_id` | Request update that triggered compilation |
| `agent_id` | Invoking agent |
| `retrievers` | Retrievers selected and executed |
| `token_count` | Tokens returned |
| `sources` | Source provenance with version info |
| `selector_matches` | Which Training Spec selectors matched |

Traces stored in agent observability logs and can be correlated with Hub request history.

---

## Related Documentation

- [Context Compilation Service](../subsystems/context-compiler/compilation-service.md) — Full context compilation service design with automatic retriever selection, request hierarchy integration, and tool-aware compilation
- [Memory Integration](./memory-integration.md) — Agent Memory as context source
- [Enterprise Memory Access Tools](../../../olympus-hub-docs/04-subsystems/memory-services/enterprise-memory/access-tools.md) — Memory retrieval
- [Knowledge Services](../../../olympus-hub-docs/04-subsystems/knowledge-services/README.md) — Policy retrieval
- [Hub Request Hierarchy](../../../olympus-hub-docs/04-subsystems/request-management/request-hierarchy.md) — Request hierarchy and context inheritance

---

*Context Compilation Service provides agent-initiated context compilation with automatic retriever selection from Training Spec, retrieving from four sources: Enterprise Knowledge, Enterprise Memory, Agent Memory, and Hub Request Context (including request hierarchy traversal).*

