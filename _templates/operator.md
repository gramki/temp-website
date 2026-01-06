# [Operator Name]

<!-- 
Template: Operator Documentation
Purpose: Document Hub operators and their CRDs
Instructions: 
  - Replace all [bracketed] text
  - Remove these comments
  - Include complete CRD examples
  - Document reconciliation behavior
-->

## Overview

The **[Operator Name]** manages [what resources/configurations] for [which persona/scope].

### Scope

| Attribute | Value |
|-----------|-------|
| **Persona** | [Admin / Developer / Supervisor / etc.] |
| **Domain** | [Publisher / Tenant] |
| **Namespace** | [System / Tenant / Workbench] |

### Managed Resources

| CRD | Purpose |
|-----|---------|
| `[CRDKind1]` | [Brief description] |
| `[CRDKind2]` | [Brief description] |

---

## [CRDKind1]

### Purpose

[What this CRD represents and when to use it]

### Specification

```yaml
apiVersion: hub.olympus.io/v1
kind: [CRDKind1]
metadata:
  name: [example-name]
  namespace: [namespace]
  labels:
    [label-key]: [label-value]
spec:
  # Required fields
  required_field_1: "value"
  required_field_2: "value"
  
  # Optional fields
  optional_field: "value"
  
  # Nested configuration
  nested_config:
    field_a: "value"
    field_b: "value"
  
  # Array fields
  items:
    - name: "item-1"
      property: "value"
    - name: "item-2"
      property: "value"
status:
  # Status fields (managed by operator)
  state: [Pending | Active | Failed | ...]
  message: "Status message"
  last_reconciled: "2026-01-06T10:00:00Z"
```

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `spec.required_field_1` | string | Yes | [Description] |
| `spec.required_field_2` | string | Yes | [Description] |
| `spec.optional_field` | string | No | [Description, default value] |
| `spec.nested_config.field_a` | string | No | [Description] |
| `spec.items[]` | array | No | [Description] |
| `spec.items[].name` | string | Yes (per item) | [Description] |

### Validation Rules

- [Validation rule 1]
- [Validation rule 2]
- [Field X must be unique within namespace]

### Reconciliation Behavior

When this CRD is applied, the operator:

1. [Step 1 of reconciliation]
2. [Step 2]
3. [Step 3]

**On Update:**
- [What happens on update]

**On Delete:**
- [What happens on delete, cleanup behavior]

### Example: [Use Case Name]

```yaml
apiVersion: hub.olympus.io/v1
kind: [CRDKind1]
metadata:
  name: example-use-case
  namespace: acme-bank
spec:
  required_field_1: "example-value"
  required_field_2: "another-value"
  nested_config:
    field_a: "configured"
```

---

## [CRDKind2]

### Purpose

[Description]

### Specification

```yaml
apiVersion: hub.olympus.io/v1
kind: [CRDKind2]
metadata:
  name: [example-name]
spec:
  # Fields
```

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `spec.field` | type | Yes/No | Description |

### Reconciliation Behavior

[Description]

---

## Dependencies

<!-- What this operator depends on -->

| Dependency | Type | Description |
|------------|------|-------------|
| [Other Operator] | Operator | [Why needed] |
| [External Service] | Service | [Why needed] |

## Integration Points

<!-- How this operator integrates with other systems -->

### Inputs

| Source | Data/Event | Description |
|--------|------------|-------------|
| [Source] | [What] | [Description] |

### Outputs

| Target | Data/Event | Description |
|--------|------------|-------------|
| [Target] | [What] | [Description] |

---

## Troubleshooting

### Issue: [Problem]

**Symptom:** [What you observe]

**Cause:** [Why it happens]

**Solution:** [How to fix]

---

## Related Documentation

- [Operator Subsystem Overview](../operators/README.md)
- [CRD Reference](../operators/crd-reference.md)
- [ADR: Related Decision](../../decision-logs/0000-decision.md)

