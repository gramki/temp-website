# CAF Integration for Native Utilities

> **Status:** 🔴 Stub — Placeholder for expansion

All Hub Native Utilities (Decision Tools, Prediction Tools) are **automatically CAF-compliant**. This document describes how the CAF Integration Layer ensures every invocation produces proper cognitive audit artifacts.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Automatic CAF compliance for all native utility invocations |
| **Approach** | Interception layer between Gateway and engines |
| **Outputs** | Decision records, evidence bundles, explanations |
| **Storage** | Enterprise Memory (via Memory Services) |

---

## Why Automatic CAF Integration?

Externalizing decisions and predictions to Native Utilities creates a natural audit point:

| Aspect | Benefit |
|--------|---------|
| **Single Interception Point** | All invocations pass through the Gateway |
| **Context is Explicit** | Inputs are the complete decision context |
| **Explanations Built-in** | Decision/prediction engines provide explanations |
| **Automatic, Not Optional** | Applications cannot bypass audit |

---

## CAF Artifacts Produced

Every native utility invocation produces:

### 1. Decision/Prediction Record

```yaml
decision_record:
  id: "DEC-123456"
  type: enum                    # decision | prediction
  
  # Identity
  tool_id: string               # Which tool was invoked
  tool_version: string          # Tool version used
  invocation_id: string         # Unique invocation ID
  
  # Context
  request_id: string            # Originating Hub Request
  session_id: string            # Session context
  actor_id: string              # Who/what triggered this (agent, automation)
  
  # Timing
  timestamp: datetime
  duration_ms: number
  
  # Inputs (context snapshot)
  inputs:
    data: object                # The input context provided
    sources:                    # Where inputs came from
      - source_type: enum       # knowledge | memory | signal | application
        source_ref: string      # Reference to source
  
  # Output
  output:
    result: object              # The decision/prediction result
    confidence: number          # 0.0-1.0 (for predictions)
  
  # Explanation
  explanation:
    type: enum                  # rule_trace | feature_importance | decision_path
    method: string              # SHAP, LIME, drools_audit, etc.
    details: object             # Engine-specific explanation
  
  # Metadata
  workbench_id: string
  tenant_id: string
```

### 2. Evidence Bundle

For significant decisions, an evidence bundle captures the state of information at decision time:

```yaml
evidence_bundle:
  id: "EVD-789012"
  decision_record_id: "DEC-123456"
  
  # Context at decision time
  knowledge_snapshot:
    - source: "policy://credit-policy-v2"
      relevant_sections: [...]
  
  memory_snapshot:
    - source: "enterprise-memory://customer/CUST-123"
      relevant_facts: [...]
  
  # Supporting artifacts
  artifacts:
    - type: "document"
      ref: "s3://evidence/income-verification.pdf"
    - type: "transaction_history"
      ref: "query://transactions?customer=CUST-123&range=90d"
  
  # Preservation metadata
  preserved_at: datetime
  retention_policy: string
```

### 3. Explanation Artifact

Detailed explanation stored for auditors:

```yaml
explanation_artifact:
  id: "EXP-345678"
  decision_record_id: "DEC-123456"
  
  # Human-readable summary
  summary: "Loan approved based on stable income (>1.5x loan amount) and positive credit history (score 720)"
  
  # Detailed explanation
  detailed:
    type: rule_trace
    format: json
    content: { ... }  # Full rule trace from engine
  
  # Counterfactual (what would change the decision)
  counterfactual:
    - "If income were below $30,000, decision would be DECLINE"
    - "If credit_score were below 650, decision would be REFER"
```

---

## Integration Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                Hub Application                                   │
│                      │                                           │
│                      │ invoke("credit-decision", context)        │
│                      ▼                                           │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │              Native Utility Gateway                         ││
│  │                                                             ││
│  │  1. Validate request                                        ││
│  │  2. Resolve tool                                            ││
│  │  3. Check access                                            ││
│  │  4. Generate invocation_id                                  ││
│  └─────────────────────────────┬───────────────────────────────┘│
│                                │                                 │
│  ┌─────────────────────────────┼───────────────────────────────┐│
│  │         CAF Integration Layer (Pre-Invoke)                  ││
│  │                                                             ││
│  │  1. Capture context snapshot                                ││
│  │  2. Record input sources                                    ││
│  │  3. Start timing                                            ││
│  └─────────────────────────────┬───────────────────────────────┘│
│                                │                                 │
│                                ▼                                 │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │    Decision Engine / Prediction Engine                      ││
│  │                                                             ││
│  │    Execute logic, produce result + explanation              ││
│  └─────────────────────────────┬───────────────────────────────┘│
│                                │                                 │
│  ┌─────────────────────────────┼───────────────────────────────┐│
│  │         CAF Integration Layer (Post-Invoke)                 ││
│  │                                                             ││
│  │  1. Capture result                                          ││
│  │  2. Capture explanation from engine                         ││
│  │  3. Generate decision record                                ││
│  │  4. Create evidence bundle (if configured)                  ││
│  │  5. Store explanation artifact                              ││
│  │  6. Write to Enterprise Memory (via Memory Services)        ││
│  │  7. Generate audit_ref                                      ││
│  └─────────────────────────────┬───────────────────────────────┘│
│                                │                                 │
│                                ▼                                 │
│                    Return response + caf_audit                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Configuration Options

### Per-Tool CAF Configuration

```yaml
caf_config:
  # Explanation detail level
  explanation_level: enum
    # minimal: Just result + basic trace
    # standard: Result + explanation + top factors
    # detailed: Full trace + counterfactual + evidence bundle
  
  # Context capture depth
  context_capture: enum
    # inputs_only: Just the input data
    # inputs_and_sources: Input data + source references
    # full: Inputs + sources + snapshots of source data
  
  # Evidence bundling
  evidence_bundling:
    enabled: boolean
    threshold: enum           # always | significant_only | never
    significant_criteria: object  # What makes a decision "significant"
  
  # Retention
  retention_policy: string    # Reference to retention policy
```

### Example: High-Stakes Decision

```yaml
tool:
  id: "loan-approval-decision"
  caf_config:
    explanation_level: detailed
    context_capture: full
    evidence_bundling:
      enabled: true
      threshold: always
    retention_policy: "7-year-regulatory"
```

### Example: Routine Prediction

```yaml
tool:
  id: "transaction-risk-score"
  caf_config:
    explanation_level: minimal
    context_capture: inputs_only
    evidence_bundling:
      enabled: false
    retention_policy: "90-day-operational"
```

---

## Storage in Enterprise Memory

CAF artifacts are stored in Enterprise Memory via Memory Services:

```yaml
enterprise_memory_structure:
  semantic_memory:
    decisions:
      - decision_record
      - evidence_bundle
      - explanation_artifact
  
  # Indexed for retrieval
  indexes:
    - by_request: request_id → [decision_records]
    - by_tool: tool_id → [decision_records]
    - by_time: timestamp → [decision_records]
    - by_subject: subject_id → [decision_records]  # e.g., customer
```

---

## Audit Access Patterns

### 1. Request-Centric Audit

"Show me all decisions made for this Request"

```
GET /memory/enterprise/decisions?request_id=REQ-456

Returns: [DEC-123, DEC-124, ...]  with full records
```

### 2. Tool-Centric Audit

"Show me all invocations of this decision tool today"

```
GET /memory/enterprise/decisions?tool_id=loan-approval&date=today

Returns: Aggregated view with statistics
```

### 3. Subject-Centric Audit

"Show me all decisions made about this customer"

```
GET /memory/enterprise/decisions?subject_type=customer&subject_id=CUST-123

Returns: Cross-request decision history
```

### 4. Explanation Retrieval

"Explain why this decision was made"

```
GET /caf/explain/DEC-123456

Returns: Human-readable explanation + counterfactual
```

---

## Compliance Benefits

| Regulatory Requirement | How Native Utilities Help |
|------------------------|--------------------------|
| **Explainability** | Built-in explanations from decision/prediction engines |
| **Reproducibility** | Stateless tools + captured context = reproducible |
| **Audit Trail** | Every invocation logged to Enterprise Memory |
| **Evidence Preservation** | Evidence bundles capture decision-time state |
| **Right to Explanation** | Explanation artifacts ready for customer requests |

---

## Related Documentation

- [Hub Native Utilities](./README.md) — Overview
- [Decision Tools](./decision-tools.md) — Rule-based decisions
- [Prediction Tools](./prediction-tools.md) — ML predictions
- [Cognitive Audit Fabric](../cognitive-audit-fabric/README.md) — CAF requirements
- [Enterprise Memory](../memory-services/hub-enterprise-memory.md) — Storage

---

*TODO: Detailed design — explanation generation, evidence bundling rules, retention enforcement*

