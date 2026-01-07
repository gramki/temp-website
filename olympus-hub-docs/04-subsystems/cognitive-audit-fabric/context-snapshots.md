# Context Snapshots

> **Status:** 🔴 Stub — Placeholder for expansion

Context Snapshots capture the **compiled context provided to an agent for any turn**—enabling observability, debugging, and reproducibility. Unlike EvidenceBundles (which are decision-specific), Context Snapshots are captured for **every agent turn**.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Capture what information agents received for each turn |
| **Timing** | Written at every agent turn (before reasoning) |
| **Scope** | All agent turns, not just decision points |
| **Relationship** | EvidenceBundles reference ContextSnapshots for decision turns |
| **Storage** | Enterprise Memory (via Memory Services) |
| **CAF Role** | Schema, retention policies, replay support |

---

## Why Context Snapshots Matter

Without context snapshots:
- Cannot debug why an agent behaved a certain way
- Cannot reproduce agent behavior for testing
- Cannot verify context assembly correctness
- Cannot measure context quality over time

---

## Context Snapshot vs Evidence Bundle

| Aspect | Context Snapshot | Evidence Bundle |
|--------|------------------|-----------------|
| **When Created** | Every agent turn | Decision points only |
| **Purpose** | Observability, debugging | Audit, compliance |
| **Content** | Compiled context frame | Context + model I/O + evidence |
| **Retention** | Shorter (days-weeks) | Longer (years) |
| **Linkage** | May have no decision | Always has DecisionRecord |

**Relationship:** EvidenceBundle contains a reference to the ContextSnapshot at decision time.

---

## Context Snapshot Schema

```yaml
context_snapshot:
  # Identity
  id: uuid                         # Unique identifier (UUID v4)
  timestamp: datetime
  case_id: uuid                    # Universal binding ID (UUID v4, = hub request_id when Hub-originated)
  
  # Hub Metadata (optional - populated when captured within Hub context)
  hub_metadata:
    tenant_id: string              # Tenant identifier
    subscription_id: string        # Subscription within tenant
    workbench_id: string           # Workbench where agent is operating
    scenario_id: string            # Scenario governing this turn
    request_id: string             # Hub Request this turn belongs to
    parent_request_id: string      # Parent request if nested (optional)
  
  # Agent & Session
  agent_id: uuid                   # Agent receiving this context
  agent_version: string            # Version of agent
  session_id: uuid                 # Session grouping (for replay traversal)
  turn_number: integer             # Order within session (for temporal traversal)
  
  # Context Frame (matches Context Assembly Engine output)
  context_frame:
    content_type:
      mime: string                 # e.g., "application/vnd.olympus.seer.context-frame.v1+json"
      schema: olympus.seer.context-frame
      schema_version: string
      
    # Section 1: Constraints
    constraints:
      tool_allowlist: array        # Allowed tools
      safety_rules: array          # Active guardrails
      escalation_rules: array      # When to escalate
      policy_constraints: array    # Active policies
    
    # Section 2: Goal
    goal:
      objective: text              # Current turn objective
      definition_of_done: text     # What constitutes success
      parent_goal: string          # Higher-level goal if nested
    
    # Section 3: Ground Truth Facts (from OLTP)
    facts:
      - source: string             # Where fact came from
        source_timestamp: datetime # When fact was retrieved
        content: object            # The fact itself
        content_content_type:      # Type of this specific fact
          mime: string             # e.g., "application/vnd.zeta.core.account.v3+json"
          schema: string
          schema_version: string
        confidence: number         # Data quality confidence
    
    # Section 4: Precedent (from Enterprise Memory)
    precedent:
      - record_type: string        # Type of memory record
        record_id: string          # Reference to full record
        summary: text              # Summarized for context
        relevance_score: number    # Why included
    
    # Section 5: Procedures (from Knowledge + Agent Memory)
    procedures:
      applicable_sops: array       # SOPs that apply
      applicable_sops_content_type:
        mime: string               # e.g., "application/vnd.olympus.hub.sop.v1+json"
        schema: string
        schema_version: string
      agent_procedures: array      # Agent's procedural memory
      workflow_state: object       # Current workflow position
    
    # Section 6: Working State (from Agent Memory)
    working_state:
      tool_outputs: array          # Results from prior tool calls
      tool_outputs_content_type:
        mime: string               # Default type; items may override
        schema: string
        schema_version: string
      pending_actions: array       # Actions awaiting completion
      session_variables: object    # Session-scoped state
      prior_turns: array           # Summary of prior turns
  
  # Compilation Metadata
  compilation:
    compiler_version: string       # Context Assembly Engine version
    token_budget: integer          # Budget for this turn
    tokens_used: integer           # Actual tokens
    truncation_applied: boolean    # Whether context was truncated
    sections_truncated: array      # Which sections were cut
    
  # Retrieval Log
  retrieval_log:
    knowledge_queries: array       # RAG queries executed
    memory_queries: array          # Memory queries executed
    facts_retrieved: integer       # Number of facts pulled
    facts_included: integer        # Number after filtering
    retrieval_latency_ms: integer
    
  # Provenance
  provenance:
    sources: array                 # All sources contributing to context
    source_versions: object        # Version of each source
    hash: string                   # Deterministic hash of context
  
  # Metadata & Links
  tags: array
  linked_records:
    evidence_bundle_id: uuid       # → EvidenceBundle if this turn resulted in decision
    decision_record_id: uuid       # → DecisionRecord if decision was made
```

---

## Capture Triggers

Context Snapshots are captured:

| Trigger | Description |
|---------|-------------|
| **Agent Turn Start** | Before agent reasoning begins |
| **Context Recompilation** | When context is refreshed mid-turn |
| **Debugging Mode** | Enhanced capture for troubleshooting |

---

## Retention Tiers

| Tier | Retention | Use Case |
|------|-----------|----------|
| **Hot** | 7 days | Active debugging, recent analysis |
| **Warm** | 30 days | Investigation of recent issues |
| **Archived** | Varies | Only if linked to EvidenceBundle |

---

## Hash for Reproducibility

The context hash enables:

| Use Case | How Hash Helps |
|----------|----------------|
| **Replay** | Same hash → expect same behavior |
| **Comparison** | Different hash → investigate what changed |
| **Caching** | Same hash → reuse reasoning |
| **Audit** | Prove context was identical |

---

## Query Patterns

| Query | Use Case |
|-------|----------|
| By session | All contexts in a session |
| By agent | Contexts for a specific agent |
| By request | Contexts for a Hub Request |
| By hash | Find identical contexts |
| By anomaly | Contexts with unusual patterns |

---

## Debugging Integration

Context Snapshots feed into:

| Consumer | Use Case |
|----------|----------|
| **Agent Debugger** | Step-through reasoning |
| **Context Quality Dashboard** | Monitor context assembly |
| **Regression Testing** | Compare context across versions |
| **Prompt Engineering** | Analyze what context was provided |

---

## Related Documentation

- [CAF Overview](./README.md)
- [Evidence Bundles](./evidence-bundles.md)
- [Seer Context Assembly Engine](../../../olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md)

---

*TODO: Detailed design — hash algorithm, storage optimization, debugging UI integration*

