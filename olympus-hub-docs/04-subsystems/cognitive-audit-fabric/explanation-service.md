# Explanation Service

> **Status:** 🔴 Stub — Placeholder for expansion

The Explanation Service generates **human-readable explanations** from decision records and evidence bundles—making enterprise memory legible and defensible.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Transform decision records into understandable narratives |
| **Consumers** | Auditors, compliance, customers, operations |
| **Input** | Decision records, evidence bundles, context |
| **Output** | Structured explanations, narratives, counterfactuals |

---

## Explanation Types

### Decision Explanation
*"Why was this decision made?"*
- Summarizes factors and reasoning
- Links to supporting evidence
- Appropriate for the audience

### Counterfactual Explanation
*"What would have happened if...?"*
- Shows alternative outcomes under different inputs
- Identifies key factors that would change the decision
- Supports dispute resolution

### Compliance Explanation
*"Can we prove this was reasonable?"*
- Meets regulatory requirements
- Structured for audit consumption
- Links to policy and precedent

### Customer Explanation
*"Why did this happen to me?"*
- Plain language summary
- Appropriate level of detail
- Actionable next steps

---

## Explanation Assembly

```
┌─────────────────────────────────────────────────────────────────┐
│                  EXPLANATION SERVICE                             │
│                                                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │  Decision   │  │  Evidence   │  │  Explanation            │  │
│  │  Records    │→ │  Bundles    │→ │  Templates              │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
│                                            │                     │
│                                            ▼                     │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                  NARRATIVE ASSEMBLER                     │    │
│  │                                                          │    │
│  │  • Selects appropriate template                          │    │
│  │  • Extracts relevant facts                               │    │
│  │  • Applies audience-appropriate language                 │    │
│  │  • Generates structured output                           │    │
│  └─────────────────────────────────────────────────────────┘    │
│                            │                                     │
│                            ▼                                     │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                  EXPLANATION OUTPUT                      │    │
│  │                                                          │    │
│  │  • Structured JSON                                       │    │
│  │  • Natural language narrative                            │    │
│  │  • Compliance-formatted document                         │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Template System

| Template Type | Use Case | Audience |
|---------------|----------|----------|
| **Regulatory** | Audit requests, compliance reviews | Auditors, regulators |
| **Operational** | Case investigation, dispute handling | Operations teams |
| **Customer** | Dispute responses, decision notifications | End customers |
| **Technical** | Model debugging, agent review | AI engineers |

---

## Counterfactual Generation

```
Given:
  - Decision record D
  - Input factors F1, F2, F3, ...

Counterfactual:
  - "If F2 had been X instead of Y, the decision would have been Z"
  - Identifies minimal changes to flip decision
  - Shows factor sensitivity
```

---

## Explanation Quality Metrics

| Metric | Description |
|--------|-------------|
| **Completeness** | All required elements present |
| **Accuracy** | Faithful to decision record |
| **Clarity** | Understandable to target audience |
| **Actionability** | Includes next steps where appropriate |

---

## API Operations

| Operation | Description |
|-----------|-------------|
| `explain` | Generate explanation for a decision |
| `counterfactual` | Generate counterfactual analysis |
| `batch_explain` | Explain multiple related decisions |
| `export` | Export explanation in compliance format |

---

## Related Documentation

- [CAF Overview](./README.md)
- [Decision Records](./decision-records.md)
- [Evidence Bundles](./evidence-bundles.md)

---

*TODO: Detailed design — template language, LLM integration for narrative, counterfactual algorithms*

