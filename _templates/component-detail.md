# [Component Name]

<!-- 
Template: Component Detail
Purpose: Detailed documentation for a specific component within a subsystem
Instructions: Replace all [bracketed] text and remove these comments
-->

## Overview

<!-- What is this component and what does it do? -->

[Component Name] is responsible for [primary responsibility]. It [key behavior description].

## Role in [Parent Subsystem]

<!-- How does this component fit into the larger subsystem? -->

```
[Parent Subsystem]
       │
       ├── [Other Component]
       │
       ├── [This Component] ◄── You are here
       │         │
       │         └── [Sub-component if any]
       │
       └── [Other Component]
```

## Responsibilities

<!-- What this component does -->

- [Responsibility 1]
- [Responsibility 2]
- [Responsibility 3]

## Non-Responsibilities

<!-- What this component explicitly does NOT do (clarifies boundaries) -->

- [Non-responsibility 1] — Handled by [Other Component]
- [Non-responsibility 2] — Out of scope

## Data Model

<!-- Key data structures this component works with -->

### [Entity Name]

```json
{
  "id": "string",
  "field_1": "type - description",
  "field_2": "type - description",
  "nested": {
    "field_3": "type - description"
  }
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | Unique identifier |
| `field_1` | string | Yes | [Description] |
| `field_2` | string | No | [Description] |

## Behavior

### [Operation/Flow 1]

<!-- Describe a key operation or flow -->

```
Step 1: [Description]
    │
    ▼
Step 2: [Description]
    │
    ▼
Step 3: [Description]
```

### [Operation/Flow 2]

<!-- Another key operation -->

## Interfaces

### API/Contract

<!-- If this component exposes an API or contract -->

| Operation | Input | Output | Description |
|-----------|-------|--------|-------------|
| [operation_name] | [Input type] | [Output type] | [What it does] |

### Events

<!-- If this component emits or consumes events -->

| Event | Direction | Description |
|-------|-----------|-------------|
| [event_name] | Emits | [When and what] |
| [event_name] | Consumes | [What triggers and response] |

## Configuration

<!-- Component-specific configuration -->

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| [setting] | [type] | [default] | [What it controls] |

## Error Handling

<!-- How errors are handled -->

| Error Scenario | Behavior | Recovery |
|----------------|----------|----------|
| [Scenario 1] | [What happens] | [How to recover] |
| [Scenario 2] | [What happens] | [How to recover] |

## Dependencies

<!-- What this component depends on -->

| Dependency | Type | Purpose |
|------------|------|---------|
| [Dependency 1] | [Internal/External] | [Why needed] |

## Examples

### Example 1: [Use Case Name]

```json
// Input
{
  "example": "input"
}

// Output
{
  "example": "output"
}
```

## Related Documentation

- [Parent Subsystem README](README.md)
- [Related Component](related-component.md)
- [ADR: Relevant Decision](../../decision-logs/0000-decision.md)

