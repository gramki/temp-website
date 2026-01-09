# ADR 0058: CAF Semantic Explainers in Content Schemas

**Status**: Accepted  
**Date**: 2026-01-07  
**Category**: caf

---

## Context

The Explanation Service needs to generate human-readable explanations from CAF records for different audiences (executive, technical, audit, customer). Without structured guidance, each record type would require custom explanation logic.

The question arose: where should explanation logic live, and how should it be standardized?

---

## Decision

**Every content schema registered with CAF includes a `semantic_explainer` section** that provides templates and metadata for generating explanations.

### Explainer Components

| Component | Purpose |
|-----------|---------|
| **Templates** | Parameterized narrative templates by audience |
| **Field Semantics** | Human-readable labels, descriptions, display formats |
| **Significance Rules** | What values are notable or concerning |
| **Relationships** | How to explain links to other records |
| **Counterfactual Hints** | What alternative scenarios to explain |

### Schema Structure

```yaml
semantic_explainer:
  templates:
    executive:
      summary: "A {{decision.action}} was made with {{decision.confidence | percent}} confidence."
    technical:
      summary: "Decision: {{decision.action}} (conf: {{decision.confidence}})"
    audit:
      summary: "{{record_id}}: {{decision.action}} @ {{timestamp}}"
    customer:
      summary: "We reviewed your case and {{decision.action | customer_friendly}}."
      
  field_semantics:
    decision.confidence:
      label: "Confidence"
      description: "Certainty level (0-100%)"
      display_format: "percentage"
      significance:
        low: { below: 0.5, label: "Low", style: "warning" }
        
  significance_rules:
    - condition: "decision.confidence < 0.5"
      level: "warning"
      message: "Low confidence decision"
      
  counterfactuals:
    - scenario: "higher_confidence"
      explanation: "With >80% confidence, this could auto-approve"
```

### API Endpoints

- `GET /v1/schemas/.../explainer` — Get explainer for a schema
- `POST /v1/schemas/explain` — Render explanation from schema + content

---

## Consequences

### Positive

- **Consistency**: All records of the same type get similar explanations
- **Declarative**: Explanation logic defined alongside schema, not in code
- **Multi-Audience**: Single definition serves all consumers
- **Evolvable**: Explainers can be updated without changing record data

### Negative

- **Schema Overhead**: Every schema needs explainer section
- **Template Limits**: Complex explanations may need LLM augmentation

### Neutral

- Explanation Service becomes a template renderer + optional LLM enhancer
- Schema Registry becomes the source of truth for explanation logic

---

## Related

- [Record Content Schema Registry](../04-subsystems/cognitive-audit-fabric/record-content-schema-registry.md) — Explainer in CRD
- [Explanation Service](../04-subsystems/cognitive-audit-fabric/explanation-service.md) — Explainer consumer


