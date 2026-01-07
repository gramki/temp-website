# Memory Access Tools

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Related**: [Memory Services README](./README.md) | [Memory Query API](./memory-query-api.md) | [Seer Tool Catalog](../../../olympus-seer-docs/seer-design/subsystems/tool-catalog.md)

---

## Overview

**Memory Access Tools** are the primary interface for Hub agents and applications to read from enterprise memory. These tools encapsulate the Memory Query API into agent-friendly invocations with built-in authorization, context extraction, and result formatting.

### Key Principles

| Principle | Description |
|-----------|-------------|
| **Tool-Based Access** | All memory reads go through defined tools; no direct API access |
| **Authorization Embedded** | Each tool call carries agent/application identity for RBAC |
| **Context-Aware** | Tools automatically use current case/request context |
| **Result Formatting** | Results formatted for agent consumption (not raw API responses) |
| **Audit Trail** | All tool invocations are logged as part of agent traces |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          MEMORY ACCESS LAYER                                  │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐    │
│   │                        AGENT / APPLICATION                            │    │
│   │                                                                       │    │
│   │   Invokes memory tool:                                               │    │
│   │   memory.search_precedent("unauthorized wire transfer $50k")          │    │
│   └───────────────────────────────────┬───────────────────────────────────┘    │
│                                       │                                        │
│   ┌───────────────────────────────────▼───────────────────────────────────┐    │
│   │                     MEMORY TOOL EXECUTOR                               │    │
│   │                                                                        │    │
│   │   1. Extract caller identity (agent_id, scenario_id, request_id)      │    │
│   │   2. Validate permissions (memory:read, memory:search)                │    │
│   │   3. Build Memory Query API request                                    │    │
│   │   4. Execute query against Memory Query Service                        │    │
│   │   5. Format results for agent consumption                              │    │
│   │   6. Log tool invocation to agent trace                                │    │
│   └───────────────────────────────────┬───────────────────────────────────┘    │
│                                       │                                        │
│   ┌───────────────────────────────────▼───────────────────────────────────┐    │
│   │                     MEMORY QUERY SERVICE                               │    │
│   │                                                                        │    │
│   │   Executes query against OpenSearch (see memory-query-api.md)         │    │
│   └───────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Tool Catalog

### Enterprise Memory Tools

| Tool Name | Purpose | Memory Class |
|-----------|---------|--------------|
| `memory.search_precedent` | Find similar past cases | Episodic |
| `memory.get_case_history` | Get full case timeline | Episodic |
| `memory.query_decisions` | Query decisions by criteria | Episodic |
| `memory.get_handoff_context` | Get handoff context for case | Episodic |
| `memory.search_patterns` | Find semantic patterns | Semantic |
| `memory.get_entity_beliefs` | Get beliefs about an entity | Semantic |
| `memory.search_procedures` | Find relevant procedures | Procedural |
| `memory.get_preferences` | Get user/agent preferences | Preference |

---

## Tool Specifications

### memory.search_precedent

Find similar past cases based on semantic similarity to the current situation.

```yaml
tool:
  name: memory.search_precedent
  description: >
    Search enterprise memory for similar past cases that can inform 
    the current decision. Returns cases ranked by similarity with 
    key decisions, outcomes, and lessons learned.
  
  # Permissions required
  permissions:
    - memory:read
    - memory:search
  
  # Input schema
  parameters:
    type: object
    required:
      - query
    properties:
      query:
        type: string
        description: >
          Natural language description of the current situation.
          Be specific about transaction type, amount, entity, and 
          circumstances for better matching.
        examples:
          - "Customer claims unauthorized international wire transfer of $50,000"
          - "Account holder disputes recurring subscription charge from unknown merchant"
      
      filters:
        type: object
        description: Optional structured filters to narrow results
        properties:
          time_range:
            type: object
            properties:
              from: { type: string, format: date-time }
              to: { type: string, format: date-time }
          outcome_types:
            type: array
            items: { type: string, enum: [approved, denied, partial, escalated] }
          entity_types:
            type: array
            items: { type: string }
        
      limit:
        type: integer
        default: 5
        minimum: 1
        maximum: 20
        description: Number of similar cases to return
      
      min_similarity:
        type: number
        default: 0.7
        minimum: 0.5
        maximum: 1.0
        description: Minimum similarity score (0-1)
  
  # Output schema
  returns:
    type: object
    properties:
      precedents:
        type: array
        items:
          type: object
          properties:
            case_id: { type: string }
            similarity_score: { type: number }
            summary: { type: string }
            relevance_factors: { type: array, items: { type: string } }
            key_decision:
              type: object
              properties:
                action: { type: string }
                rationale: { type: string }
                confidence: { type: number }
            outcome: { type: string }
            lessons: { type: array, items: { type: string } }
      
      query_context:
        type: object
        properties:
          query_id: { type: string }
          total_matches: { type: integer }
          search_scope: { type: string }

# Example invocation
example:
  input:
    query: "Customer claims unauthorized international wire transfer of $48,500 to first-time overseas recipient"
    filters:
      time_range:
        from: "2025-01-01T00:00:00Z"
      outcome_types: ["approved", "denied"]
    limit: 5
  
  output:
    precedents:
      - case_id: "case-55667788"
        similarity_score: 0.91
        summary: "Unauthorized international wire - Premium customer - $51,000"
        relevance_factors:
          - "Similar transaction amount ($51,000 vs $48,500)"
          - "Same transaction type (international wire)"
          - "Both involve first-time overseas recipients"
          - "Similar customer profile (long tenure, clean history)"
        key_decision:
          action: "approve_full_refund"
          rationale: "Pattern matched known fraud ring FR-2025-0034. Customer history clean with 8-year tenure. No prior disputes."
          confidence: 0.92
        outcome: "approved - full refund issued"
        lessons:
          - "Premium customers with clean history typically qualify for expedited resolution"
          - "Pattern match with known fraud ring is strong indicator"
      
      - case_id: "case-44556677"
        similarity_score: 0.85
        summary: "International wire fraud - $42,000 - denied initially then approved on appeal"
        relevance_factors:
          - "Similar transaction type and amount"
          - "Initial denial overturned on customer appeal"
        key_decision:
          action: "deny_initial"
          rationale: "Customer's recent travel to destination country raised suspicion of authorized transaction"
          confidence: 0.78
        outcome: "approved on appeal - customer provided travel denial documentation"
        lessons:
          - "Verify customer travel history before assuming unauthorized"
          - "Request documentation early to avoid appeal cycles"
    
    query_context:
      query_id: "qry-abc123"
      total_matches: 47
      search_scope: "fraud-ops workbench, episodic memory, last 12 months"
```

### memory.get_case_history

Retrieve complete case timeline with all related records.

```yaml
tool:
  name: memory.get_case_history
  description: >
    Retrieve the complete history of a case including all decisions, 
    evidence, outcomes, overrides, and handoffs in chronological order.
  
  permissions:
    - memory:read
  
  parameters:
    type: object
    required:
      - case_id
    properties:
      case_id:
        type: string
        description: The case ID to retrieve history for
      
      include:
        type: array
        items:
          type: string
          enum: [decisions, evidence, outcomes, overrides, handoffs, timeline]
        default: [decisions, outcomes, timeline]
        description: Which related records to include
      
      format:
        type: string
        enum: [timeline, grouped, full]
        default: timeline
        description: How to format the response
  
  returns:
    type: object
    properties:
      case:
        type: object
        properties:
          case_id: { type: string }
          status: { type: string }
          entity_type: { type: string }
          entity_id: { type: string }
          created_at: { type: string }
          resolved_at: { type: string }
      
      timeline:
        type: array
        items:
          type: object
          properties:
            timestamp: { type: string }
            event_type: { type: string }
            summary: { type: string }
            actor: { type: object }
            record_id: { type: string }
      
      summary:
        type: object
        properties:
          total_decisions: { type: integer }
          total_handoffs: { type: integer }
          duration_hours: { type: number }
          final_outcome: { type: string }

example:
  input:
    case_id: "case-12345678"
    include: ["decisions", "handoffs", "timeline"]
    format: "timeline"
  
  output:
    case:
      case_id: "case-12345678"
      status: "resolved"
      entity_type: "dispute"
      entity_id: "disp-78901"
      created_at: "2026-01-05T09:00:00Z"
      resolved_at: "2026-01-06T14:30:00Z"
    
    timeline:
      - timestamp: "2026-01-05T09:00:00Z"
        event_type: "case_created"
        summary: "Dispute case opened for unauthorized wire transfer"
        actor: { id: "system", type: "system" }
        record_id: "rec-001"
      
      - timestamp: "2026-01-05T09:05:00Z"
        event_type: "decision"
        summary: "Classified as high-priority fraud case"
        actor: { id: "agent-triage-001", type: "agent" }
        record_id: "dec-001"
      
      - timestamp: "2026-01-05T09:10:00Z"
        event_type: "handoff"
        summary: "Escalated to human analyst for high-value review"
        actor: { id: "agent-triage-001", type: "agent" }
        record_id: "hoff-001"
      
      - timestamp: "2026-01-06T14:30:00Z"
        event_type: "resolution"
        summary: "Full refund approved and processed"
        actor: { id: "user-jane", type: "human" }
        record_id: "dec-002"
    
    summary:
      total_decisions: 3
      total_handoffs: 1
      duration_hours: 29.5
      final_outcome: "approved"
```

### memory.get_handoff_context

Get handoff context for continuing work on a case.

```yaml
tool:
  name: memory.get_handoff_context
  description: >
    Retrieve the handoff context for a case, including current state, 
    actions taken, open items, and recommendations from the previous agent.
    Use this when starting work on a case that was handed off.
  
  permissions:
    - memory:read
  
  parameters:
    type: object
    required:
      - case_id
    properties:
      case_id:
        type: string
        description: The case ID to get handoff context for
      
      latest_only:
        type: boolean
        default: true
        description: Return only the most recent handoff (true) or all handoffs (false)
  
  returns:
    type: object
    properties:
      handoff:
        type: object
        properties:
          handoff_id: { type: string }
          from_agent: { type: object }
          to_agent: { type: object }
          handoff_reason: { type: string }
          timestamp: { type: string }
          
          current_state:
            type: object
            properties:
              status: { type: string }
              summary: { type: string }
              key_facts: { type: array, items: { type: string } }
              working_hypothesis: { type: string }
          
          actions_taken: { type: array, items: { type: string } }
          
          open_items:
            type: object
            properties:
              pending_actions: { type: array }
              awaiting_response: { type: array }
              unanswered_questions: { type: array }
          
          recommendations:
            type: object
            properties:
              suggested_next_steps: { type: array }
              areas_of_concern: { type: array }
              relevant_precedent: { type: array }
          
          sla_status:
            type: object
            properties:
              deadline: { type: string }
              time_remaining: { type: string }
              sla_risk: { type: string }
```

### memory.search_patterns

Search semantic memory for patterns and hypotheses.

```yaml
tool:
  name: memory.search_patterns
  description: >
    Search semantic memory for learned patterns, hypotheses, and 
    constraints that may be relevant to the current situation.
  
  permissions:
    - memory:read
    - memory:search
  
  parameters:
    type: object
    required:
      - query
    properties:
      query:
        type: string
        description: Description of the situation or pattern you're looking for
      
      pattern_types:
        type: array
        items:
          type: string
          enum: [hypothesis, pattern_summary, learned_constraint, entity_belief]
        default: [hypothesis, pattern_summary]
      
      min_confidence:
        type: number
        default: 0.7
        minimum: 0.5
        maximum: 1.0
      
      limit:
        type: integer
        default: 10
  
  returns:
    type: object
    properties:
      patterns:
        type: array
        items:
          type: object
          properties:
            pattern_id: { type: string }
            pattern_type: { type: string }
            description: { type: string }
            confidence: { type: number }
            evidence_count: { type: integer }
            conditions: { type: array, items: { type: string } }
            implications: { type: array, items: { type: string } }
            last_validated: { type: string }
```

### memory.get_entity_beliefs

Get semantic beliefs about a specific entity.

```yaml
tool:
  name: memory.get_entity_beliefs
  description: >
    Retrieve learned beliefs and inferred attributes about a specific entity 
    (customer, account, merchant, etc.) from semantic memory.
  
  permissions:
    - memory:read
  
  parameters:
    type: object
    required:
      - entity_type
      - entity_id
    properties:
      entity_type:
        type: string
        description: Type of entity (customer, account, merchant, etc.)
      
      entity_id:
        type: string
        description: Unique identifier for the entity
      
      belief_types:
        type: array
        items:
          type: string
          enum: [attribute, behavior, relationship, risk]
        description: Types of beliefs to retrieve
      
      min_confidence:
        type: number
        default: 0.6
  
  returns:
    type: object
    properties:
      entity:
        type: object
        properties:
          entity_type: { type: string }
          entity_id: { type: string }
      
      beliefs:
        type: array
        items:
          type: object
          properties:
            belief_id: { type: string }
            belief_type: { type: string }
            attribute: { type: string }
            value: { type: string }
            confidence: { type: number }
            evidence_summary: { type: string }
            last_updated: { type: string }
      
      relationships:
        type: array
        items:
          type: object
          properties:
            related_entity_type: { type: string }
            related_entity_id: { type: string }
            relationship_type: { type: string }
            confidence: { type: number }
```

---

## Authentication & Authorization

### Identity Extraction

When a tool is invoked, the Memory Tool Executor extracts caller identity from the execution context:

```yaml
caller_context:
  # From agent execution context
  agent_id: "agent-fraud-triage-001"
  agent_type: "seer_agent"
  
  # From request context
  request_id: "req-12345"
  case_id: "case-67890"
  
  # From workbench context
  workbench_id: "wb-fraud-ops"
  scenario_id: "fraud-dispute-resolution"
  
  # From authentication
  tenant_id: "tenant-acme-bank"
  subscription_id: "sub-fraud-premium"
  
  # Effective permissions (from agent role)
  permissions:
    - memory:read
    - memory:search
```

### Permission Checks

| Permission | Required For |
|------------|--------------|
| `memory:read` | All memory access tools |
| `memory:search` | Semantic search tools (`search_precedent`, `search_patterns`) |
| `memory:explain` | Explanation generation |
| `memory:admin` | Retention management, bulk operations |

### Workbench Scoping

All tool invocations are automatically scoped to the caller's workbench. Agents cannot access memory from other workbenches.

---

## SDK Integration

### Seer Agent SDK

For Seer-managed agents, memory tools are available through the standard tool interface:

```python
from seer.tools import memory

# Search for precedent
precedents = await memory.search_precedent(
    query="Customer claims unauthorized wire transfer of $48,500",
    filters={"outcome_types": ["approved", "denied"]},
    limit=5
)

# Get case history
history = await memory.get_case_history(
    case_id="case-12345",
    include=["decisions", "handoffs", "timeline"]
)

# Get handoff context for current case
handoff = await memory.get_handoff_context(
    case_id=context.case_id,
    latest_only=True
)

# Search patterns
patterns = await memory.search_patterns(
    query="weekend international wire transfers",
    min_confidence=0.75
)
```

### Direct API Access

For applications not using the Seer SDK, memory tools can be invoked via the Tool Execution API:

```yaml
POST /v1/tools/execute

Request:
{
  "tool_name": "memory.search_precedent",
  "parameters": {
    "query": "Customer claims unauthorized wire transfer",
    "limit": 5
  },
  "context": {
    "request_id": "req-12345",
    "case_id": "case-67890"
  }
}

Response:
{
  "tool_name": "memory.search_precedent",
  "execution_id": "exec-abc123",
  "status": "success",
  "result": {
    "precedents": [...],
    "query_context": {...}
  },
  "execution_metadata": {
    "latency_ms": 245,
    "tokens_used": 0
  }
}
```

---

## Audit & Observability

### Tool Invocation Logging

All memory tool invocations are logged as part of the agent trace:

```yaml
tool_invocation:
  invocation_id: "inv-xyz789"
  tool_name: "memory.search_precedent"
  agent_id: "agent-fraud-triage-001"
  request_id: "req-12345"
  timestamp: "2026-01-07T15:30:00Z"
  
  input:
    query: "unauthorized wire transfer $48,500"
    filters: { outcome_types: ["approved"] }
    limit: 5
  
  output:
    result_count: 5
    top_similarity: 0.91
  
  execution:
    latency_ms: 245
    cache_hit: false
    query_id: "qry-abc123"
```

### Metrics

| Metric | Description |
|--------|-------------|
| `memory.tool.invocations` | Count of tool invocations by tool name |
| `memory.tool.latency` | Latency histogram by tool name |
| `memory.tool.errors` | Error count by tool name and error type |
| `memory.search.similarity` | Similarity score distribution |
| `memory.search.result_count` | Result count distribution |

---

## Error Handling

### Error Responses

```yaml
error_response:
  tool_name: "memory.search_precedent"
  status: "error"
  error:
    code: "INSUFFICIENT_PERMISSIONS"
    message: "Agent does not have memory:search permission"
    details:
      required_permission: "memory:search"
      agent_permissions: ["memory:read"]
    
    # Suggested action for agent
    suggestion: "Request elevated permissions or use memory.get_case_history for specific case lookup"
```

### Error Codes

| Code | Description | Agent Action |
|------|-------------|--------------|
| `INSUFFICIENT_PERMISSIONS` | Missing required permission | Escalate or use alternative tool |
| `CASE_NOT_FOUND` | Case ID not in memory | Verify case ID, check scope |
| `QUERY_TIMEOUT` | Search took too long | Narrow filters, reduce limit |
| `NO_RESULTS` | No matches found | Broaden search, reduce min_similarity |
| `RATE_LIMITED` | Too many requests | Wait and retry |

---

## Related Documents

- [Memory Services README](./README.md) — Architecture overview
- [Memory Query API](./memory-query-api.md) — Query API specification
- [CAF Episodic Memory Store](../cognitive-audit-fabric/episodic-memory-store/README.md) — Record schemas
- [Seer Tool Catalog](../../../olympus-seer-docs/seer-design/subsystems/tool-catalog.md) — Tool framework

---

*TODO: Additional tools for procedural/preference memory, batch operations, cross-memory queries*

