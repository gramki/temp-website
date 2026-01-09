# ADR-0042: Scenario as Tool Granularity

| Property       | Value                                           |
|----------------|-------------------------------------------------|
| **Status**     | Accepted                                        |
| **Date**       | 2026-01-06                                      |
| **Category**   | Composite Patterns                              |
| **Deciders**   | Architecture Team                               |
| **Supersedes** | -                                               |

---

## Context

When exposing a Scenario as a Tool, we need to decide the granularity:

1. **Each HTTP Signal = One Tool** — A scenario with 5 signals becomes 5 tools
2. **Entire Scenario = One Tool** — A scenario becomes one tool with 5 operations

This affects:
- Tool discovery (how many tools to browse)
- Tool registry size
- API design
- Developer experience

---

## Decision

**An entire Scenario is exposed as one Tool, with each HTTP Signal type becoming an operation of that tool.**

### Example

```yaml
# Dispute Scenario exposed as ONE Tool with multiple operations
tool:
  name: dispute-resolution
  operations:
    - name: create          # From signal: dispute.submitted
    - name: add-evidence    # From signal: dispute.evidence.submitted
    - name: get-status      # From signal: dispute.status.query
```

### Rationale

| Benefit | Explanation |
|---------|-------------|
| **Prevents tool explosion** | 10 scenarios × 5 signals = 50 tools → 10 tools |
| **Logical grouping** | Related operations stay together |
| **Better discoverability** | Fewer tools to browse |
| **Cohesive interface** | Tool represents a capability, not an endpoint |
| **Versioning** | Tool version = Scenario version |

---

## Alternatives Considered

### 1. Each Signal = Separate Tool

Every HTTP signal type creates its own tool.

**Rejected because:**
- Tool registry becomes large and hard to navigate
- Related operations are scattered
- Redundant metadata across related tools
- Harder to understand what a scenario offers

### 2. Developer Chooses Per Signal

Let developer decide which signals become tools.

**Rejected because:**
- Inconsistent patterns across scenarios
- More configuration burden
- Still risks explosion if developers choose "all"
- Can be revisited based on adoption feedback

---

## Consequences

### Positive

1. **Manageable tool count** — Registry stays navigable
2. **Cohesive capabilities** — Related operations grouped logically
3. **Clear versioning** — Tool version tracks scenario version
4. **Simpler discovery** — Find the tool, then explore operations

### Negative

1. **Operation selection** — Caller must specify operation name
2. **Mixed schemas** — Different operations have different input/output
3. **Partial exposure** — Can't hide some operations (all or nothing)

### Risks

1. **Large operations list** — Scenarios with many signals have many operations
2. **Adoption feedback** — May need to revisit based on real usage

---

## Implementation Notes

### Tool Invocation

```python
# Invoke tool with operation
result = await tools.invoke(
    tool_id="dispute-ops/dispute-resolution",
    operation="create",  # Specifies which signal to trigger
    params={"customer_id": "C123", "transaction_id": "T456"}
)
```

### Operation Discovery

```python
# Get tool with operations
tool = await tools.get("dispute-ops/dispute-resolution")
for op in tool.operations:
    print(f"{op.name}: {op.description}")
```

---

## Related Decisions

- [ADR-0041: Standalone Tool as ToolInstance Variation](./0041-standalone-tool-variation.md)
- [ADR-0001: Signal Normalization](./0001-signal-normalization.md)

