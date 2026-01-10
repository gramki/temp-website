# 5.1 The Context Assembly Engine

The Context Assembly Engine is Seer's core subsystem for building reproducible, auditable reasoning contexts. It transforms the principles of context compilation (Part 1, Section 5.3) into a production-grade implementation.

## What the Engine Does

For every reasoning step, the Context Assembly Engine:

1. Receives a request with goal and constraints
2. Orchestrates retrieval from appropriate sources
3. Filters, deduplicates, and resolves conflicts
4. Allocates token budgets across sections
5. Assembles a structured context frame
6. Logs provenance for audit

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│               CONTEXT ASSEMBLY ENGINE                        │
│                                                              │
│   ┌───────────────────────────────────────────────────┐    │
│   │                  REQUEST HANDLER                   │    │
│   │   • Receives request with goal and constraints     │    │
│   │   • Identifies task type and required sources      │    │
│   └────────────────────────┬──────────────────────────┘    │
│                            │                                │
│   ┌────────────────────────▼──────────────────────────┐    │
│   │               SOURCE ORCHESTRATOR                  │    │
│   │                                                    │    │
│   │   ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────┐ │    │
│   │   │Knowledge │ │Enterprise│ │Operational│ │Agent │ │    │
│   │   │Services  │ │ Memory   │ │  Data    │ │Memory│ │    │
│   │   └────┬─────┘ └────┬─────┘ └────┬─────┘ └──┬───┘ │    │
│   │        └──────────┬─┴───────────┬┘          │     │    │
│   │                   │             │           │     │    │
│   └───────────────────┼─────────────┼───────────┼─────┘    │
│                       │             │           │          │
│   ┌───────────────────▼─────────────▼───────────▼─────┐    │
│   │              FILTER & CONFLICT RESOLVER           │    │
│   │   • Deduplication    • Access control             │    │
│   │   • Relevance filter • Precedence rules           │    │
│   └────────────────────────┬──────────────────────────┘    │
│                            │                                │
│   ┌────────────────────────▼──────────────────────────┐    │
│   │                 TOKEN BUDGET MANAGER              │    │
│   │   • Allocate by section • Truncation strategies   │    │
│   └────────────────────────┬──────────────────────────┘    │
│                            │                                │
│   ┌────────────────────────▼──────────────────────────┐    │
│   │                  FRAME ASSEMBLER                  │    │
│   │   • Structure output • Format sections            │    │
│   └────────────────────────┬──────────────────────────┘    │
│                            │                                │
│   ┌────────────────────────▼──────────────────────────┐    │
│   │                PROVENANCE LOGGER                  │    │
│   │   • Record inclusions • Record exclusions         │    │
│   │   • Version tracking  • Audit trail               │    │
│   └───────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## The Compilation Pipeline

### Step 1: Request Analysis

The engine receives a request and analyzes requirements:

```yaml
assembly_request:
  goal: "Decide refund eligibility for dispute case-12345"
  task_type: decision
  agent: dispute-analyst-tier1
  session: session-abc123
  constraints:
    max_tokens: 8000
    sources_required:
      - knowledge
      - enterprise_memory
      - operational_data
      - agent_memory
```

### Step 2: Source Selection

Based on task type, the engine determines which sources to query:

| Task Type | Knowledge | Enterprise Memory | Operational | Agent Memory |
|-----------|-----------|-------------------|-------------|--------------|
| Decision | Required | Required | Required | Optional |
| Information | Required | Optional | Required | Optional |
| Conversation | Optional | Optional | Optional | Required |
| Procedure | Required | Optional | Optional | Required |

### Step 3: Parallel Retrieval

The Source Orchestrator queries sources in parallel:

```python
results = await asyncio.gather(
    knowledge_service.retrieve(query, filters),
    enterprise_memory.retrieve_precedent(case_type),
    operational_data.get_current_state(entity_ids),
    agent_memory.get_session_context(session_id)
)
```

### Step 4: Filter and Resolve

Retrieved candidates are filtered and conflicts resolved:

```yaml
filter_results:
  total_candidates: 47
  after_dedup: 32
  after_relevance: 18
  after_access_control: 18
  
conflict_resolution:
  - conflict: "Refund limit policy vs. manager preference"
    resolution: "Enterprise Knowledge takes precedence"
    applied: knowledge_bank_policy
```

### Step 5: Budget Allocation

Token budget is allocated across sections:

```yaml
budget_allocation:
  total: 8000
  sections:
    constraints: 500 (fixed)
    goal: 200 (fixed)
    ground_truth_facts: 2500
    recent_episodes: 1500
    preferences: 300
    procedures: 1500
    working_state: 1500
```

### Step 6: Frame Assembly

The structured context frame is assembled:

```yaml
context_frame:
  constraints:
    - "Max refund without approval: $500"
    - "Tools allowed: [get_transaction, get_customer_history, approve_refund]"
    
  goal:
    objective: "Determine refund eligibility"
    required_output: "Decision with rationale"
    
  ground_truth_facts:
    - source: knowledge_bank
      content: "Dispute must be filed within 60 days"
      provenance: dispute-policy-v3.2
    - source: operational_data
      content: "Transaction amount: $450, Date: 2025-12-20"
      provenance: transaction-service
      
  recent_episodes:
    - source: enterprise_memory
      content: "Similar case approved (case-11234) - merchant error confirmed"
      provenance: decision-record-dr-xyz
      
  preferences:
    - source: agent_memory
      content: "Customer prefers email communication"
      
  procedures:
    - source: knowledge_bank
      content: "Step 1: Verify transaction details..."
      provenance: dispute-workflow-v2.1
      
  working_state:
    - extracted_entities: [txn-12345, cust-67890]
    - current_step: verify_eligibility
```

### Step 7: Provenance Logging

Everything is logged for audit:

```yaml
provenance_log:
  assembly_id: "ctx-assembly-789"
  timestamp: 2026-01-10T14:30:00Z
  
  sources_queried:
    - knowledge_bank: 3 queries, 12 chunks returned, 5 included
    - enterprise_memory: 2 queries, 8 records returned, 2 included
    - operational_data: 1 query, transaction details returned
    - agent_memory: session context, 4 entities
    
  exclusions:
    - item: "Outdated policy v2.1"
      reason: "Superseded by v3.2"
    - item: "Unrelated case precedent"
      reason: "Below relevance threshold"
      
  token_usage:
    allocated: 8000
    used: 7234
    
  frame_version: "ctx-frame-v1"
```

## Reproducibility

The engine enables exact reproduction of historical contexts:

```python
# Reproduce context for audit
historical_context = context_engine.reproduce(
    assembly_id="ctx-assembly-789"
)
# Returns: exact context frame as it was at decision time
```

This is essential for:
- Regulatory response ("What did the agent know?")
- Incident investigation ("Why did it decide that?")
- Model validation ("Are contexts consistent?")

---

**References:**
*   `olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md`
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-3-context-compilation.md`
*   `olympus-seer-docs/agentic-ai-concepts/agent-memory/context-building.md`
