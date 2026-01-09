# [Pattern Name]

<!-- 
Template: Composite Pattern Documentation
Purpose: Document patterns for composing Hub components
Instructions: 
  - Replace all [bracketed] text
  - Remove these comments
  - Include at least 2-3 automation approaches (not just AI)
  - Add to 09-composite-systems-and-patterns/README.md index
-->

## Overview

<!-- One paragraph summary of the pattern -->

[Pattern Name] enables [what it allows]. This pattern is useful when [primary use case].

### At a Glance

| Aspect | Description |
|--------|-------------|
| **Pattern Type** | [Composition / Integration / Delegation] |
| **Primary Actors** | [Who uses this pattern] |
| **Key Benefit** | [Main value proposition] |
| **Complexity** | [Low / Medium / High] |

---

## Why Use This Pattern?

<!-- The problems this pattern solves -->

### Problem Statement

[Description of the challenge or need this pattern addresses]

### Use Cases

1. **[Use Case 1]**: [Description]
2. **[Use Case 2]**: [Description]
3. **[Use Case 3]**: [Description]

### Benefits

- [Benefit 1]
- [Benefit 2]
- [Benefit 3]

### When NOT to Use

- [Scenario where this pattern is inappropriate]
- [Another scenario]

---

## How It Works

### Conceptual Model

```
┌─────────────────────────────────────────────────────────┐
│                     [Consumer]                           │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                  [Pattern Component]                     │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   Step 1    │───▶│   Step 2    │───▶│   Step 3    │  │
│  └─────────────┘    └─────────────┘    └─────────────┘  │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                    [Provider]                            │
└─────────────────────────────────────────────────────────┘
```

### Key Components

| Component | Role | Responsibility |
|-----------|------|----------------|
| [Component A] | [Role] | [What it does] |
| [Component B] | [Role] | [What it does] |
| [Component C] | [Role] | [What it does] |

### Interaction Flow

```
[Actor 1]                    [Pattern]                    [Actor 2]
    │                            │                            │
    │  1. [Action]               │                            │
    │───────────────────────────▶│                            │
    │                            │  2. [Action]               │
    │                            │───────────────────────────▶│
    │                            │                            │
    │                            │  3. [Response]             │
    │                            │◀───────────────────────────│
    │  4. [Result]               │                            │
    │◀───────────────────────────│                            │
```

---

## Automation Types

<!-- IMPORTANT: Include multiple automation approaches, not just AI -->

This pattern supports various automation approaches:

### Rule-Based Automation

[Description of how rules-based logic can implement this pattern]

```yaml
# Example rule-based configuration
rules:
  - condition: "[condition expression]"
    action: "[action to take]"
```

### Workflow-Based Automation

[Description of workflow approach]

### Image/Document Processing

[If applicable, how document/image processing fits]

### LLM/AI-Powered Automation

[Description of AI-based implementation]

---

## Implementation Examples

### Example 1: [Non-AI Example Name]

**Scenario:** [Description]

**Implementation approach:** [Brief description]

```yaml
# Configuration example
spec:
  automation_type: rule-based
  # ... configuration
```

```python
# Implementation snippet
def process(context):
    # Rule-based logic
    if context.condition:
        return action_a()
    return action_b()
```

---

### Example 2: [Another Non-AI Example]

**Scenario:** [Description]

**Implementation approach:** [Description]

```yaml
# Configuration
```

---

### Example 3: [AI-Powered Example]

**Scenario:** [Description]

**Implementation approach:** [Description]

```python
# AI implementation snippet
async def process_with_ai(context):
    response = await llm.analyze(context.data)
    return format_response(response)
```

---

## Step-by-Step Guide

### Prerequisites

- [Prerequisite 1]
- [Prerequisite 2]

### Step 1: [Setup Action]

[Detailed instructions]

```yaml
# Configuration
```

### Step 2: [Configuration Action]

[Detailed instructions]

### Step 3: [Deployment Action]

[Detailed instructions]

### Step 4: [Verification]

[How to verify the pattern is working]

---

## Operator Support

<!-- CRD and operator details -->

### CRD: [CRD Name]

```yaml
apiVersion: hub.olympus.io/v1
kind: [CRDKind]
metadata:
  name: [example-name]
  namespace: [namespace]
spec:
  # Key fields
  field_1: value
  field_2: value
```

### Key Fields

| Field | Required | Description |
|-------|----------|-------------|
| `field_1` | Yes | [Description] |
| `field_2` | No | [Description] |

### Reconciliation Behavior

[What the operator does when this CRD is applied]

---

## Best Practices

| Practice | Rationale |
|----------|-----------|
| [Do X] | [Why] |
| [Avoid Y] | [Why] |
| [Consider Z when...] | [Context] |

---

## Troubleshooting

### Issue: [Problem]

**Symptom:** [What you observe]

**Solution:** [How to fix]

---

### Issue: [Problem]

**Symptom:** [Observation]

**Solution:** [Fix]

---

## Related Patterns

- [Related Pattern 1](related-pattern.md) — [Relationship]
- [Related Pattern 2](related-pattern.md) — [Relationship]

## Related Documentation

- [ADR: Relevant Decision](../decision-logs/0000-decision.md)
- [Operator Documentation](../04-subsystems/operators/relevant.md)
- [Guide](../10-guides/relevant-guide.md)

