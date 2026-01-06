# ADR-0041: Standalone Tool as ToolInstance Variation

| Property       | Value                                           |
|----------------|-------------------------------------------------|
| **Status**     | Accepted                                        |
| **Date**       | 2026-01-06                                      |
| **Category**   | Operators                                       |
| **Deciders**   | Architecture Team                               |
| **Supersedes** | -                                               |

---

## Context

Hub Applications can be exposed as directly invocable tools (Standalone Tools). The question is how to register these:

1. Create a new `StandaloneToolSpec` CRD
2. Extend the existing `ToolInstance` CRD with a flag indicating the workbench is the machine

A Standalone Tool differs from external machine tools only in that:
- The "machine" is the workbench itself
- No external machine endpoint needed
- Tool is hosted by a Hub Application within the workbench

---

## Decision

**Use the existing `ToolInstance` CRD with `machine.type: standalone` to indicate the workbench hosts the tool. This avoids CRD proliferation while maintaining clear semantics.**

```yaml
apiVersion: hub.olympus.io/v1
kind: ToolInstance
metadata:
  name: fraud-detection-tool
spec:
  tool:
    name: fraud-detection-tool
    version: "1.0.0"
  
  # Standalone indicator
  machine:
    type: standalone           # Key: workbench is the machine
  
  # Application that implements the tool
  application_ref: fraud-detection-app
  
  # Rest of tool configuration...
```

---

## Alternatives Considered

### 1. New StandaloneToolSpec CRD

Create a dedicated CRD for standalone tools.

**Rejected because:**
- Conceptually, a standalone tool IS a tool instance
- Most fields would duplicate ToolInstance
- Adds CRD maintenance burden
- Confuses developers with similar CRDs

### 2. Flag in HubApplicationSpec

Add a `expose_as_tool` section in HubApplicationSpec.

**Rejected because:**
- Mixes application and tool concerns
- Tool registration should be explicit
- Harder to manage independently
- Doesn't integrate with Tool Registry naturally

---

## Consequences

### Positive

1. **Single CRD** — All tools use ToolInstance
2. **Clear semantics** — `machine.type: standalone` is explicit
3. **Tool Registry consistency** — All tools registered the same way
4. **Developer familiarity** — Same patterns for all tool types

### Negative

1. **Conditional fields** — Some fields only apply to standalone tools
2. **Validation complexity** — Need different validation rules per type

---

## Implementation Notes

### Machine Type Values

| Type | Description |
|------|-------------|
| `external` | Tool hosted on external machine (default) |
| `standalone` | Tool hosted by Hub Application in workbench |

### Required Fields by Type

| Field | External | Standalone |
|-------|----------|------------|
| `machine.machine_ref` | Required | Not used |
| `application_ref` | Not used | Required |

---

## Related Decisions

- [ADR-0040: Direct Tool Dispatcher](./0040-direct-tool-dispatcher.md)
- [ADR-0016: Typed Data Store CRDs](./0016-typed-data-store-crds.md)

