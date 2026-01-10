# 4.3 Enterprise Memory in Seer

Enterprise Memory captures the organization's experiential record—what happened, what was decided, and what was learned. It provides the foundation for institutional learning and regulatory-grade audit.

## What Enterprise Memory Captures

Enterprise Memory answers the question: **"What happened and why?"**

| Record Type | What It Captures | Purpose |
|-------------|-----------------|---------|
| **Decision Records** | Agent decisions with rationale | Audit, precedent, learning |
| **Outcome Records** | Results of decisions | Feedback, evaluation |
| **Override Records** | Human interventions and reasons | Audit, improvement |
| **Hypothesis Records** | Patterns observed across cases | Institutional learning |
| **Case Records** | Case lifecycle and state | Case continuity |

## Enterprise Memory Architecture

Hub's Enterprise Memory uses the ESPP taxonomy (Episodic, Semantic, Procedural, Preference):

```
┌─────────────────────────────────────────────────────────────┐
│                   ENTERPRISE MEMORY                          │
│                                                              │
│   ┌─────────────────┐    ┌─────────────────────────────┐   │
│   │    EPISODIC     │    │        SEMANTIC             │   │
│   │                 │    │                             │   │
│   │  • Decisions    │    │  • Patterns (hypotheses)    │   │
│   │  • Outcomes     │    │  • Entity beliefs           │   │
│   │  • Overrides    │    │  • Learned constraints      │   │
│   │  • Handoffs     │    │  • Relationship beliefs     │   │
│   └─────────────────┘    └─────────────────────────────┘   │
│                                                              │
│   ┌─────────────────┐    ┌─────────────────────────────┐   │
│   │   PROCEDURAL    │    │        PREFERENCE           │   │
│   │                 │    │                             │   │
│   │  • Learned      │    │  • User preferences         │   │
│   │    skills       │    │  • Agent behaviors          │   │
│   │  • Procedures   │    │  • Interaction patterns     │   │
│   │  • Action seqs  │    │                             │   │
│   └─────────────────┘    └─────────────────────────────┘   │
│                                                              │
│   Storage: Olympus Europa (OpenSearch)                       │
│   Retention: 7+ years │ PII: Prohibited │ Immutable          │
└─────────────────────────────────────────────────────────────┘
```

## Writing to Enterprise Memory

Agents write to Enterprise Memory via the Signal Exchange, not directly:

```
Agent Decision
     │
     ▼
Signal Exchange (routing)
     │
     ├──→ Episodic Store (decision record)
     │
     └──→ CAF (audit cataloging)
```

### Why Indirect Write?

*   **Governance:** Signal Exchange enforces write policies
*   **Routing:** Records are classified and routed appropriately
*   **Audit:** All writes are logged and attributed
*   **Consistency:** Standard format and validation

### Decision Record Example

```yaml
decision_record:
  record_id: "dr-a1b2c3d4"
  case_id: "case-12345"
  
  decision:
    type: refund_approved
    value: 450
    
  rationale:
    summary: "Approved based on clear merchant error and customer history"
    factors:
      - factor: merchant_error_confirmed
        weight: high
        evidence_ref: evidence-789
      - factor: customer_dispute_history
        weight: medium
        evidence_ref: evidence-790
        
  context_snapshot_ref: "cs-xyz789"
  
  agent:
    employment_spec: dispute-analyst-tier1-acme-production
    identity: dispute-analyst-tier1
    
  delegator:
    principal: manager@acme.com
    delegation_id: del-456
    
  hub_metadata:
    tenant_id: acme
    workbench_id: dispute-ops-prod
    created_at: 2026-01-10T14:30:00Z
    content_hash: sha256:abc123...
```

## Reading from Enterprise Memory

Agents read Enterprise Memory for precedent and context:

```python
# Retrieve similar past decisions
precedents = seer.memory.retrieve_precedent(
    case_type="merchant_dispute",
    customer_segment="retail",
    similarity_threshold=0.8,
    max_results=5
)
```

### Use Cases

| Use Case | What Agent Retrieves |
|----------|---------------------|
| **Precedent lookup** | Similar past decisions and outcomes |
| **Customer history** | Prior interactions (via entity references) |
| **Pattern detection** | Recurring issues or behaviors |
| **Outcome prediction** | What happened in similar situations |

## Key Governance Properties

### Immutability

Records cannot be modified after creation:
- Errors corrected via new amendment records
- Original record preserved with correction reference
- Full audit trail maintained

### No PII

Enterprise Memory uses entity references, not direct PII:
- `customer-id: cust-12345` instead of name/email
- Enables 7+ year retention without privacy conflicts
- Supports right-to-erasure (reference is deleted, memory preserved)

### Long Retention

Episodic records retained 7+ years:
- Regulatory compliance (OCC, EU AI Act, Fair Lending)
- Audit and legal discovery
- Institutional learning over time

---

**References:**
*   `olympus-hub-docs/04-subsystems/memory-services/enterprise-memory/README.md`
*   `olympus-hub-docs/04-subsystems/memory-services/shared/espp-taxonomy.md`
*   `olympus-seer-docs/why-seer/part-1-background/03-memory-requirements/03-3-org-vs-op-memory.md`
