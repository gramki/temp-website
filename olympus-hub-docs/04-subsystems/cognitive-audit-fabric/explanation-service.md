# Explanation Service

> **Status:** 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Related**: [CAF README](./README.md) | [Record Content Schema Registry](./record-content-schema-registry.md)

The Explanation Service generates **human-readable explanations** from CAF records using **semantic explainers** defined in the [Schema Registry](./record-content-schema-registry.md)—making enterprise memory legible and defensible.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Transform decision records into understandable narratives |
| **Consumers** | Auditors, compliance, customers, operations |
| **Input** | CAF records + semantic explainers from Schema Registry |
| **Output** | Structured explanations, narratives, counterfactuals |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           EXPLANATION SERVICE                                │
│                                                                              │
│   ┌───────────────────────────────────────────────────────────────────┐     │
│   │                     SCHEMA REGISTRY                                │     │
│   │                                                                    │     │
│   │   ContentSchema CRD ─────► Semantic Explainer                     │     │
│   │     • templates (by audience)                                      │     │
│   │     • field_semantics (labels, descriptions, significance)         │     │
│   │     • significance_rules (alerts)                                  │     │
│   │     • relationships (traversal)                                    │     │
│   │     • counterfactuals (hints)                                      │     │
│   │                                                                    │     │
│   └───────────────────────────────────────────────────────────────────┘     │
│                                    │                                         │
│                                    ▼                                         │
│   ┌───────────────────────────────────────────────────────────────────┐     │
│   │                    EXPLANATION ENGINE                              │     │
│   │                                                                    │     │
│   │   1. Resolve content type → schema → explainer                    │     │
│   │   2. Select audience template                                      │     │
│   │   3. Render template with record data                             │     │
│   │   4. Apply field semantics (labels, formatting)                    │     │
│   │   5. Evaluate significance rules (alerts)                         │     │
│   │   6. Traverse relationships (linked records)                       │     │
│   │   7. Generate counterfactuals (if requested)                       │     │
│   │                                                                    │     │
│   └───────────────────────────────────────────────────────────────────┘     │
│                                    │                                         │
│                                    ▼                                         │
│   ┌───────────────────────────────────────────────────────────────────┐     │
│   │                    EXPLANATION OUTPUT                              │     │
│   │                                                                    │     │
│   │   • Structured JSON (programmatic consumption)                     │     │
│   │   • Natural language narrative (human reading)                     │     │
│   │   • Compliance document (audit/regulatory)                         │     │
│   │   • Customer communication (dispute response)                      │     │
│   │                                                                    │     │
│   └───────────────────────────────────────────────────────────────────┘     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Semantic Explainer Integration

The Explanation Service relies on **semantic explainers** registered with each content schema. When explaining a record:

### 1. Schema Resolution

```python
def explain_record(record, audience):
    # 1. Get content type from record
    content_type = record.content_type.mime  # e.g., "application/vnd.olympus.caf.decision-record.v1+json"
    
    # 2. Resolve to schema
    schema = schema_registry.resolve_by_mime(content_type)
    
    # 3. Get semantic explainer
    explainer = schema_registry.get_explainer(schema.uri)
    
    # 4. Render explanation
    return render_explanation(record, explainer, audience)
```

### 2. Template Rendering

Templates use a Mustache-like syntax with filters:

| Syntax | Example | Description |
|--------|---------|-------------|
| `{{field}}` | `{{decision.action}}` | Direct field value |
| `{{field \| filter}}` | `{{confidence \| percent}}` | Apply filter |
| `{{array \| count}}` | `{{factors \| count}}` | Array length |
| `{{field \| json}}` | `{{factors \| json}}` | JSON format |
| `{{field \| customer_friendly}}` | `{{action \| customer_friendly}}` | Human-friendly |

**Built-in filters:**

| Filter | Description | Example |
|--------|-------------|---------|
| `percent` | Format as percentage | `0.87` → `87%` |
| `datetime` | Format timestamp | ISO → "Jan 7, 2026" |
| `count` | Array length | `[a,b,c]` → `3` |
| `json` | JSON stringify | Object → JSON string |
| `customer_friendly` | Customer language | `approve_refund` → `approve your refund` |
| `action_verb` | Action formatting | `approve_refund` → `Approve Refund` |
| `prose` | Sentence case | Technical → readable |
| `currency` | Currency format | `1000` → `$1,000.00` |

### 3. Field Semantics Application

For each field in the response:

```yaml
field_explanations:
  - field: "decision.confidence"
    label: "Confidence"              # From field_semantics.label
    description: "Certainty level"    # From field_semantics.description
    value: 0.87                       # Raw value
    formatted: "87%"                  # Formatted by display_format
    significance:                     # From significance rules
      level: "normal"
      message: null
```

### 4. Significance Evaluation

```yaml
# In schema explainer:
significance_rules:
  - condition: "decision.confidence < 0.5"
    level: "warning"
    message: "Low confidence decision"

# In record being explained:
decision:
  confidence: 0.35

# Result:
significance_alerts:
  - level: "warning"
    message: "Low confidence decision"
    field: "decision.confidence"
    value: 0.35
```

---

## Explanation Types

### Decision Explanation
*"Why was this decision made?"*

```yaml
POST /v1/explainer/explain

Request:
{
  "record_type": "decision_record",
  "record_id": "dec-12345",
  "audience": "executive",
  "options": {
    "include_evidence": true,
    "include_significance": true,
    "include_relationships": true
  }
}

Response:
{
  "record_id": "dec-12345",
  "record_type": "decision_record",
  "audience": "executive",
  
  "narrative": {
    "summary": "A refund approval was made with 87% confidence.",
    "detail": "Based on 3 factors, the agent decided to approve the refund. The purchase was verified, the customer has no prior disputes, and the amount was reasonable."
  },
  
  "structured": {
    "decision": {
      "label": "Decision",
      "value": "Approve Refund",
      "confidence": "87%"
    },
    "factors": [
      { "factor": "Purchase Verified", "weight": "40%", "value": "✓ Confirmed" },
      { "factor": "No Prior Disputes", "weight": "30%", "value": "Clean history" },
      { "factor": "Amount Reasonable", "weight": "30%", "value": "$45.00" }
    ]
  },
  
  "significance_alerts": [],
  
  "evidence_summary": {
    "count": 4,
    "items": [
      { "type": "transaction_record", "summary": "Purchase on Dec 15" },
      { "type": "customer_history", "summary": "3 years, no disputes" }
    ]
  }
}
```

### Counterfactual Explanation
*"What would have happened if...?"*

```yaml
POST /v1/explainer/counterfactual

Request:
{
  "record_type": "decision_record",
  "record_id": "dec-12345",
  "audience": "technical",
  "scenarios": ["higher_confidence", "missing_factor"]
}

Response:
{
  "record_id": "dec-12345",
  "original_decision": "approve_refund",
  
  "counterfactuals": [
    {
      "scenario": "higher_confidence",
      "condition": "decision.confidence > 0.9",
      "current_value": 0.87,
      "threshold": 0.9,
      "explanation": "If confidence exceeded 90%, this could have been auto-approved without human review.",
      "outcome_change": "auto_approve (no review required)"
    },
    {
      "scenario": "missing_factor",
      "factor": "purchase_verified",
      "explanation": "Without purchase verification, confidence would drop to ~52%, likely triggering escalation.",
      "outcome_change": "escalate_to_senior"
    }
  ],
  
  "sensitivity_analysis": {
    "most_influential_factor": "purchase_verified",
    "decision_stability": "stable",
    "margin_to_flip": 0.23
  }
}
```

### Compliance Explanation
*"Can we prove this was reasonable?"*

```yaml
POST /v1/explainer/compliance

Request:
{
  "record_type": "decision_record",
  "record_id": "dec-12345",
  "format": "regulatory_audit",
  "include_full_evidence": true
}

Response:
{
  "record_id": "dec-12345",
  "audit_timestamp": "2026-01-07T15:00:00Z",
  
  "compliance_narrative": {
    "summary": "Decision record dec-12345 documents an automated refund approval made on January 7, 2026 at 14:30 UTC.",
    "decision_basis": "The decision was based on 3 weighted factors with a combined confidence of 87%.",
    "evidence_chain": "4 evidence items are linked to this decision, including transaction verification and customer history.",
    "policy_alignment": "Decision aligns with Refund Policy v2.3, Section 4.2 (automatic approval criteria).",
    "human_oversight": "No human override was applied. Decision was within autonomous authority bounds."
  },
  
  "evidence_manifest": [
    {
      "evidence_id": "evd-001",
      "type": "transaction_record",
      "captured_at": "2026-01-07T14:29:00Z",
      "hash": "sha256:abc123...",
      "retrieval_url": "/v1/evidence/evd-001"
    }
  ],
  
  "policy_references": [
    {
      "policy_id": "pol-refund-v23",
      "section": "4.2",
      "title": "Automatic Approval Criteria",
      "satisfied": true
    }
  ],
  
  "export_formats": ["pdf", "json", "xml"]
}
```

### Customer Explanation
*"Why did this happen to me?"*

```yaml
POST /v1/explainer/customer

Request:
{
  "record_type": "decision_record",
  "record_id": "dec-12345",
  "language": "en",
  "options": {
    "include_next_steps": true,
    "personalization": {
      "customer_name": "Sarah"
    }
  }
}

Response:
{
  "record_id": "dec-12345",
  
  "customer_narrative": {
    "greeting": "Hi Sarah,",
    "summary": "Good news! We've reviewed your refund request and approved it.",
    "explanation": "We verified your purchase from December 15 and confirmed the issue you reported. Since you're a valued customer with a great history, we've processed this quickly.",
    "outcome": "Your refund of $45.00 will appear in your account within 3-5 business days.",
    "closing": "Thank you for your patience."
  },
  
  "next_steps": [
    {
      "action": "wait_for_refund",
      "description": "Your refund will arrive in 3-5 business days",
      "timeline": "2026-01-12"
    },
    {
      "action": "contact_support",
      "description": "If you don't see the refund by then, contact us",
      "link": "/support"
    }
  ],
  
  "tone": "positive",
  "reading_level": "grade_8"
}
```

---

## Case Explanation (Multi-Record)

Explain an entire case by traversing from `case_id`:

```yaml
POST /v1/explainer/case

Request:
{
  "case_id": "case-12345",
  "audience": "executive",
  "depth": "summary"  # summary | detailed | full
}

Response:
{
  "case_id": "case-12345",
  "case_type": "fraud_investigation",
  "status": "resolved",
  
  "timeline_narrative": [
    {
      "timestamp": "2026-01-07T10:00:00Z",
      "event": "Case opened",
      "explanation": "Customer disputed $450 charge from MerchantCo"
    },
    {
      "timestamp": "2026-01-07T10:05:00Z",
      "event": "Investigation started",
      "explanation": "Fraud investigator agent began analysis"
    },
    {
      "timestamp": "2026-01-07T10:15:00Z",
      "event": "Decision made",
      "explanation": "Agent approved refund with 87% confidence",
      "record_ref": "dec-12345"
    },
    {
      "timestamp": "2026-01-07T10:16:00Z",
      "event": "Case resolved",
      "explanation": "Refund processed, customer notified"
    }
  ],
  
  "key_decisions": [
    {
      "record_id": "dec-12345",
      "summary": "Approve refund with 87% confidence",
      "factors_count": 3,
      "evidence_count": 4
    }
  ],
  
  "outcome": {
    "resolution": "refund_approved",
    "customer_impact": "positive",
    "time_to_resolution": "PT16M"
  }
}
```

---

## API Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/explainer/explain` | POST | Explain a single record |
| `/v1/explainer/counterfactual` | POST | Generate counterfactual analysis |
| `/v1/explainer/compliance` | POST | Generate compliance-ready explanation |
| `/v1/explainer/customer` | POST | Generate customer-facing explanation |
| `/v1/explainer/case` | POST | Explain entire case |
| `/v1/explainer/batch` | POST | Explain multiple records |
| `/v1/explainer/export` | POST | Export explanation in document format |

---

## Audience Mapping

| Audience | Template Key | Characteristics |
|----------|--------------|-----------------|
| `executive` | High-level summary, key metrics | Business language, outcome-focused |
| `technical` | Detailed with raw values | Technical terminology, full data |
| `audit` | Compliance-formatted | Regulatory language, evidence chain |
| `customer` | Plain language, empathetic | Simple words, actionable |
| `operational` | Action-oriented | What to do next, context |

---

## LLM Integration (Optional)

For enhanced narrative generation, the Explanation Service can optionally use LLM:

```yaml
POST /v1/explainer/explain
{
  "record_id": "dec-12345",
  "audience": "customer",
  "options": {
    "use_llm": true,
    "llm_config": {
      "style": "empathetic",
      "tone": "positive",
      "max_tokens": 500
    }
  }
}
```

The LLM receives:
1. Rendered template (from semantic explainer)
2. Structured data
3. Audience guidelines

And produces polished natural language.

---

## Explanation Quality Metrics

| Metric | Description |
|--------|-------------|
| **Completeness** | All required elements present |
| **Accuracy** | Faithful to decision record |
| **Clarity** | Understandable to target audience |
| **Actionability** | Includes next steps where appropriate |
| **Consistency** | Similar records get similar explanations |

---

## TODO

| Item | Description | Priority |
|------|-------------|----------|
| Define counterfactual algorithms | How to compute minimal flip conditions | P1 |
| Define LLM prompt templates | Standardized prompts for narrative polish | P1 |
| Define explanation caching | Cache computed explanations | P2 |
| Define multi-language support | i18n for customer explanations | P2 |
| Define explanation versioning | Track explanation changes over time | P2 |

---

## Related Documentation

- [CAF Overview](./README.md)
- [Record Content Schema Registry](./record-content-schema-registry.md) — Source of semantic explainers
- [Decision Records](./episodic-memory-store/decision-records.md)
- [Evidence Bundles](./episodic-memory-store/evidence-bundles.md)
