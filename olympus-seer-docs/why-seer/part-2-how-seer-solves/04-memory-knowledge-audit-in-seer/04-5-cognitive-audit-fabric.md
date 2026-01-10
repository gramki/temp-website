# 4.5 The Cognitive Audit Fabric

The Cognitive Audit Fabric (CAF) is Hub's control plane for memory governance, audit, and explainability. CAF doesn't store memory—it governs how memory is captured, linked, explained, and audited.

## What CAF Provides

CAF answers the question: **"Can we prove this decision was reasonable?"**

| Capability | What It Enables |
|------------|-----------------|
| **Decision journaling** | Capture what was decided and why |
| **Evidence bundling** | Package context available at decision time |
| **Explanation generation** | Produce human-readable rationales |
| **Audit replay** | Reconstruct decision conditions |
| **Policy enforcement** | Govern memory access and retention |

## CAF Architecture

CAF is a control plane that orchestrates memory governance:

```
┌─────────────────────────────────────────────────────────────┐
│               COGNITIVE AUDIT FABRIC (CAF)                   │
│                                                              │
│   ┌─────────────────┐    ┌─────────────────────────────┐   │
│   │  POLICY ENGINE  │    │     AUDIT LOGGER            │   │
│   │                 │    │                             │   │
│   │  • Memory       │    │  • Operation logging        │   │
│   │    policies     │    │  • Access logging           │   │
│   │  • Access       │    │  • Policy decision          │   │
│   │    policies     │    │    logging                  │   │
│   └─────────────────┘    └─────────────────────────────┘   │
│                                                              │
│   ┌─────────────────┐    ┌─────────────────────────────┐   │
│   │   RETENTION     │    │    EXPLANATION              │   │
│   │    MANAGER      │    │      SERVICE                │   │
│   │                 │    │                             │   │
│   │  • Expiration   │    │  • Multi-audience           │   │
│   │  • Deletion     │    │    explanations             │   │
│   │  • Legal hold   │    │  • Semantic explainers      │   │
│   │  • Archive      │    │  • Template rendering       │   │
│   └─────────────────┘    └─────────────────────────────┘   │
│                                                              │
│   ┌─────────────────────────────────────────────────────┐  │
│   │              ENTERPRISE LEARNING SERVICES            │  │
│   │                                                       │  │
│   │  • Pattern detection in episodic memory              │  │
│   │  • Promotion orchestration (Episodic → Semantic)     │  │
│   │  • Knowledge promotion (Semantic → ETSL)             │  │
│   │  • Governance gates for promotions                   │  │
│   └─────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Decision Journaling

Every significant agent decision creates a decision record:

```yaml
decision_record:
  record_id: "dr-a1b2c3d4"
  case_id: "case-12345"
  
  decision:
    type: refund_approved
    value: 450
    alternatives_considered:
      - type: partial_refund
        value: 225
        rejected_reason: "Clear merchant error warrants full refund"
      - type: escalate
        rejected_reason: "Within agent authority ceiling"
        
  rationale:
    summary: "Full refund approved due to confirmed merchant error"
    factors:
      - factor: merchant_error_confirmed
        weight: 0.9
      - factor: customer_history_positive
        weight: 0.7
        
  context_snapshot_ref: "cs-xyz789"
```

## Evidence Bundling

Evidence bundles capture what the agent knew at decision time:

```yaml
evidence_bundle:
  bundle_id: "eb-xyz789"
  decision_record_ref: "dr-a1b2c3d4"
  
  contents:
    knowledge_retrieved:
      - source: knowledge_bank
        document: "dispute-policy-v3.2"
        chunks_retrieved: 3
        
    memory_consulted:
      - source: enterprise_memory
        type: precedent_lookup
        records_returned: 2
        
    operational_data:
      - source: transaction_service
        query: "get_transaction_details(txn-12345)"
        response_summary: "Merchant error flag: true"
        
    agent_memory:
      - conversation_turns: 4
        entities_extracted: ["txn-12345", "cust-67890"]
```

## Explanation Service

CAF's Explanation Service generates audience-appropriate explanations:

### Multi-Audience Output

From the same underlying records, CAF generates:

**Customer Explanation:**
> We've approved your dispute for the $450 charge at ACME Store. Our review confirmed the merchant charged you incorrectly. The full amount will be credited within 3-5 business days.

**Operator Explanation:**
> Decision: REFUND_APPROVED | Amount: $450.00 | Case: case-12345
> Factors: merchant_error_confirmed (0.9), customer_history_positive (0.7)
> Agent: dispute-analyst-tier1 | Authority: within $500 ceiling
> Context: 3 knowledge chunks, 2 precedents, 1 API response

**Regulator Explanation:**
> Decision ID: dr-a1b2c3d4 | Timestamp: 2026-01-10T14:30:00Z
> Decision Type: Refund Approval | Value: USD 450.00
> Agent Identity: dispute-analyst-tier1 (Employment: dispute-analyst-acme-production)
> Delegating Authority: manager@acme.com (Delegation: del-456)
> 
> Evidence Package: eb-xyz789
> - Policy consulted: dispute-policy-v3.2, sections 4.2, 4.3, 4.7
> - Precedent cases: case-11234 (similar, approved), case-11189 (similar, approved)
> - Operational verification: Transaction service confirmed merchant_error=true
> 
> Rationale: Agent determined full refund appropriate per policy section 4.2
> (merchant error, customer in good standing). Decision within delegated authority
> ceiling of $500. No escalation triggers met.

### Semantic Explainers

Explanation generation uses semantic explainers:

```yaml
explainer:
  name: refund_decision_explainer
  applies_to: decision_record
  
  audiences:
    customer:
      template: "We've {{outcome}} your dispute for {{amount}}..."
      tone: empathetic
      detail_level: summary
      
    operator:
      template: "Decision: {{decision_type}} | Amount: {{amount}}..."
      tone: technical
      detail_level: operational
      
    regulator:
      template: "Decision ID: {{record_id}} | Timestamp: {{created_at}}..."
      tone: formal
      detail_level: complete
```

## Policy Enforcement

CAF enforces policies on all cognitive operations:

```yaml
caf_policy:
  memory:
    enterprise_memory:
      retention_days: 2555  # 7 years
      pii_detection: enabled
      access_logging: full
      
    agent_memory:
      retention_days: 90
      access_logging: summary
      
  access:
    cross_scope_access: deny
    admin_access: audit_required
    bulk_export: approval_required
    
  audit:
    log_level: full
    retention_years: 7
    immutable: true
```

## Audit Replay

CAF enables reconstruction of past decisions:

```python
# Reconstruct decision conditions
replay = caf.replay_decision(
    decision_record_id="dr-a1b2c3d4"
)

# Returns:
# - Context snapshot at decision time
# - Evidence bundle (what was known)
# - Policy version that applied
# - Agent version and configuration
# - Delegation chain in effect
```

This enables:
- Regulatory response ("Show me what the agent knew when it decided X")
- Root cause analysis ("Why did the agent make this unusual decision?")
- Model validation ("Are agents deciding consistently?")

---

**References:**
*   `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/README.md`
*   `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/explanation-service.md`
*   `olympus-seer-docs/why-seer/part-1-background/04-audit-requirements/04-3-cognitive-audit-fabric.md`
