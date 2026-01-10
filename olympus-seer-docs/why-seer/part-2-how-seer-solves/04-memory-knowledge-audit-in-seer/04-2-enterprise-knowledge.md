# 4.2 Enterprise Knowledge in Seer

Enterprise Knowledge is the authoritative source of organizational truth that grounds agent reasoning. Seer integrates with Hub's knowledge services to ensure agents operate from curated, versioned, and governed information sources.

## What Enterprise Knowledge Provides

Enterprise Knowledge answers the question: **"What is correct/required/true?"**

| Knowledge Type | Examples | Agent Use |
|---------------|----------|-----------|
| **Policies** | Dispute escalation rules, approval thresholds | Compliance constraints |
| **Procedures** | Standard operating procedures, playbooks | Guided workflows |
| **Reference data** | Product catalogs, fee schedules, entity definitions | Factual grounding |
| **Regulatory requirements** | Disclosures, hold periods, consent requirements | Mandatory actions |

## Knowledge Services Architecture

Hub's Knowledge Services provide the infrastructure for Enterprise Knowledge:

```
┌─────────────────────────────────────────────────────────────┐
│                   KNOWLEDGE SERVICES                         │
│                                                              │
│   ┌───────────────────┐    ┌───────────────────────────┐   │
│   │   KNOWLEDGE BANK  │    │   ETSL (Enterprise        │   │
│   │                   │    │   Temporal Semantic Layer)│   │
│   │   • Documents     │    │                           │   │
│   │   • Procedures    │    │   • Asserted facts        │   │
│   │   • RAG-indexed   │    │   • Business rules        │   │
│   │   • Versioned     │    │   • Time-aware validity   │   │
│   │                   │    │   • Authority-qualified   │   │
│   └───────────────────┘    └───────────────────────────┘   │
│                                                              │
│   ┌─────────────────────────────────────────────────────┐  │
│   │                  COMMON CAPABILITIES                  │  │
│   │                                                       │  │
│   │  • Semantic search (vector similarity)               │  │
│   │  • Symbolic filters (metadata, tags)                 │  │
│   │  • Provenance tracking                               │  │
│   │  • Access control (workbench-scoped)                 │  │
│   └─────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Knowledge Bank

The Knowledge Bank provides document-based knowledge for RAG (Retrieval-Augmented Generation):

*   **Documents:** Policies, procedures, guides, reference materials
*   **Indexing:** Vector embeddings for semantic search
*   **Versioning:** Full version history with effective dates
*   **Provenance:** Source attribution for retrieved content

### Agent Access Pattern

```python
# Agent retrieves knowledge via context compilation
knowledge = seer.context.retrieve_knowledge(
    query="What is the dispute escalation policy?",
    workbench="fraud-ops-prod",
    filters={"document_type": "policy"},
    max_chunks=5
)
# Returns: ranked chunks with provenance
```

## Enterprise Temporal Semantic Layer (ETSL)

ETSL provides structured, time-aware semantic knowledge:

*   **Asserted facts:** "Product X has fee Y" (valid from date A to date B)
*   **Business rules:** "Transactions over $10,000 require manager approval"
*   **Constraints:** "Customer cannot have more than 3 disputes per month"
*   **Temporal validity:** Facts have effective dates and can be superseded

### Why Temporal Matters

Enterprise knowledge changes over time:
- Fee schedules change quarterly
- Policies are updated
- Regulatory requirements evolve

ETSL tracks *when* facts are valid, enabling:
- Point-in-time queries ("What was the policy on January 1?")
- Audit reconstruction ("What rules applied when this decision was made?")
- Future-dated assertions ("New policy takes effect next month")

## Integration with Seer

### Context Compilation

Seer's Context Assembly Engine retrieves knowledge as part of context compilation:

```yaml
context_frame:
  constraints:
    - source: etsl
      content: "Max refund without approval: $500"
      
  ground_truth_facts:
    - source: knowledge_bank
      content: "Dispute must be filed within 60 days of transaction"
      provenance:
        document: "dispute-policy-v3.2"
        section: "Filing Requirements"
        retrieved_at: 2026-01-10T10:00:00Z
```

### Knowledge Precedence

Enterprise Knowledge takes precedence over other sources:

```
1. System constraints (highest) — Platform guardrails
2. Enterprise Knowledge         — Authoritative policy
3. Enterprise Memory            — Historical precedent
4. Agent Memory (lowest)        — Session preferences
```

An agent's session preferences cannot override enterprise policy.

## Governance

### Write Access

Enterprise Knowledge is write-protected:
- Only authorized governance processes can add/modify content
- Changes require approval workflows
- All modifications are versioned and audited

### Read Access

Agents access Enterprise Knowledge through governed tools:
- Scoped to workbench
- Retrieval is logged
- Provenance is attached to retrieved content

---

**References:**
*   `olympus-hub-docs/04-subsystems/knowledge-services/README.md`
*   `olympus-hub-docs/pontus/etsl/`
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-4-four-sources.md`
