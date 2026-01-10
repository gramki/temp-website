# 5.2 Source Orchestration

Source orchestration is the process of retrieving information from the four cognitive sources (Enterprise Knowledge, Enterprise Memory, Operational Data, Agent Memory) in a coordinated, governed manner. Each source answers a different cognitive question and requires different access patterns.

## The Four Sources in Practice

| Source | Question | Access Pattern | Governance |
|--------|----------|----------------|------------|
| **Enterprise Knowledge** | What is true/required? | Knowledge Services (RAG) | Version-controlled, approved |
| **Enterprise Memory** | What happened? | Memory Services query | Immutable, audited |
| **Operational Data** | What is current state? | Operational APIs/tools | Real-time, access-controlled |
| **Agent Memory** | What am I working with? | Agent Memory SDK | Session-scoped |

## Orchestration Flow

```
┌─────────────────────────────────────────────────────────────┐
│                 SOURCE ORCHESTRATOR                          │
│                                                              │
│   Request: "Decide refund eligibility for case-12345"        │
│                                                              │
│   ┌────────────────────────────────────────────────────┐    │
│   │              QUERY PLANNING                         │    │
│   │                                                     │    │
│   │   What sources are needed for this task?            │    │
│   │   What queries should be issued?                    │    │
│   │   What filters apply?                               │    │
│   └────────────────────────┬───────────────────────────┘    │
│                            │                                │
│         ┌──────────────────┼──────────────────┐             │
│         │                  │                  │             │
│         ▼                  ▼                  ▼             │
│   ┌───────────┐     ┌───────────┐     ┌───────────┐        │
│   │ KNOWLEDGE │     │  MEMORY   │     │OPERATIONAL│        │
│   │  QUERIES  │     │  QUERIES  │     │  QUERIES  │        │
│   └─────┬─────┘     └─────┬─────┘     └─────┬─────┘        │
│         │                 │                 │               │
│         ▼                 ▼                 ▼               │
│   ┌───────────┐     ┌───────────┐     ┌───────────┐        │
│   │ Knowledge │     │ Memory    │     │Operational│        │
│   │ Services  │     │ Services  │     │ APIs      │        │
│   └─────┬─────┘     └─────┬─────┘     └─────┬─────┘        │
│         │                 │                 │               │
│         └─────────────────┼─────────────────┘               │
│                           │                                 │
│   ┌───────────────────────▼────────────────────────────┐   │
│   │              RESULT AGGREGATION                     │   │
│   │                                                     │   │
│   │   Combine results, attach provenance                │   │
│   └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Source-Specific Patterns

### Enterprise Knowledge Retrieval

Querying authoritative policies and procedures:

```python
knowledge_results = await knowledge_service.retrieve(
    workbench="dispute-ops-prod",
    queries=[
        {
            "query": "refund eligibility policy",
            "filters": {"document_type": "policy"},
            "max_chunks": 5
        },
        {
            "query": "dispute resolution workflow",
            "filters": {"document_type": "procedure"},
            "max_chunks": 3
        }
    ]
)

# Results include provenance
for chunk in knowledge_results:
    print(f"Source: {chunk.document_id}, Version: {chunk.version}")
```

### Enterprise Memory Retrieval

Querying institutional experience:

```python
memory_results = await enterprise_memory.query(
    workbench="dispute-ops-prod",
    queries=[
        {
            "type": "precedent",
            "case_type": "merchant_dispute",
            "similarity_threshold": 0.8,
            "max_results": 3
        },
        {
            "type": "entity_history",
            "entity_ref": "cust-67890",
            "record_types": ["decision", "outcome"]
        }
    ]
)
```

### Operational Data Retrieval

Querying current system state via tools:

```python
operational_results = await operational_tools.invoke([
    {
        "tool": "get_transaction_details",
        "params": {"transaction_id": "txn-12345"}
    },
    {
        "tool": "get_customer_profile",
        "params": {"customer_id": "cust-67890"}
    }
])
```

### Agent Memory Retrieval

Querying session context:

```python
session_context = await agent_memory.get_context(
    session_id="session-abc123",
    include=[
        "conversation_history",
        "extracted_entities",
        "working_hypotheses",
        "tool_results"
    ]
)
```

## Parallel vs. Sequential

Source queries are parallelized when independent:

```python
# Independent queries - run in parallel
results = await asyncio.gather(
    knowledge_service.retrieve(...),
    enterprise_memory.query(...),
    operational_tools.invoke(...),
    agent_memory.get_context(...)
)

# Dependent queries - run sequentially
customer = await operational_tools.get_customer(customer_id)
if customer.tier == "premium":
    # Additional knowledge query for premium customers
    premium_policies = await knowledge_service.retrieve(
        filters={"applies_to": "premium"}
    )
```

## Access Control

Each source enforces its own access control:

| Source | Access Control |
|--------|----------------|
| **Knowledge** | Workbench-scoped, document-level ACLs |
| **Enterprise Memory** | Workbench-scoped, no cross-tenant access |
| **Operational Data** | Tool-level authorization via Cipher |
| **Agent Memory** | Agent+session isolation |

```yaml
# Access denied logged
access_denial:
  source: operational_data
  tool: get_internal_audit_log
  agent: dispute-analyst-tier1
  reason: "Tool not in agent's allowlist"
  logged_to: caf
```

## Result Aggregation

Results from all sources are aggregated with metadata:

```yaml
aggregated_results:
  from_knowledge:
    - chunk_id: "kb-chunk-123"
      content: "Refunds must be processed within 30 days..."
      provenance:
        document: dispute-policy-v3.2
        version: 3.2
        effective_date: 2025-01-01
      relevance_score: 0.92
      
  from_memory:
    - record_id: "dr-xyz789"
      content: "Similar case approved - merchant error pattern"
      provenance:
        case_id: case-11234
        decision_date: 2025-12-15
      relevance_score: 0.85
      
  from_operational:
    - tool: get_transaction_details
      content:
        transaction_id: txn-12345
        amount: 450.00
        merchant: "ACME Store"
        status: settled
      retrieved_at: 2026-01-10T14:30:00Z
      
  from_agent_memory:
    - type: extracted_entities
      content: ["txn-12345", "cust-67890", "ACME Store"]
    - type: current_step
      content: "verify_eligibility"
```

## Precedence Rules

When sources provide conflicting information, precedence rules apply:

```
1. System constraints (highest)
2. Enterprise Knowledge (authoritative policy)
3. Verified Operational Data (current state)
4. Enterprise Memory (historical precedent)
5. Agent Memory (session preferences - lowest)
```

Example conflict resolution:

```yaml
conflict:
  type: refund_limit
  sources:
    - enterprise_knowledge: "Max refund: $500"
    - agent_memory: "User preference: approve up to $1000"
  resolution:
    winner: enterprise_knowledge
    reason: "Policy takes precedence over preference"
```

---

**References:**
*   `olympus-seer-docs/agentic-ai-concepts/designing-an-agent.md`
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-4-four-sources.md`
