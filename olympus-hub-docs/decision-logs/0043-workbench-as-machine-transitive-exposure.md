# ADR-0043: Workbench as Machine — Transitive Tool Exposure

| Property       | Value                                           |
|----------------|-------------------------------------------------|
| **Status**     | Accepted                                        |
| **Date**       | 2026-01-06                                      |
| **Category**   | Composite Patterns                              |
| **Deciders**   | Architecture Team                               |
| **Supersedes** | -                                               |

---

## Context

When a Workbench (WB-A) is exposed as a Machine, it can expose tools from:
1. Its own Scenarios (as tools)
2. Its own Standalone Tools (Hub Applications)
3. External machines it uses (Machine Tools)

The question is: Should WB-A be able to expose tools from external machines (Machine-X) as part of its Machine interface, allowing consumers (WB-B) to transitively access Machine-X's tools through WB-A?

```
WB-B ──> WB-A (as Machine) ──> Machine-X
```

---

## Decision

**Workbench-as-Machine supports transitive tool exposure. WB-A can include tools from machines it uses (Machine-X) in its exposed tool list, allowing WB-B to access Machine-X's tools through WB-A.**

### Key Points

1. **WB-B doesn't need direct access to Machine-X** — It only needs access to WB-A
2. **WB-A manages Machine-X credentials** — WB-B doesn't know about Machine-X's auth
3. **WB-A controls which tools to expose** — Not all of Machine-X's tools need to be exposed
4. **WB-A can add value** — Transform inputs, combine tools, add access control

---

## Alternatives Considered

### 1. No Transitive Exposure

WB-A can only expose its own tools (Scenarios, Standalone Tools).

**Rejected because:**
- WB-A often integrates multiple systems
- Consumers shouldn't need direct relationships with all systems
- Reduces WB-A's ability to act as a service aggregator
- Forces consumers to manage more machine relationships

### 2. Automatic Transitive Exposure

All machine tools used by WB-A are automatically exposed.

**Rejected because:**
- Security concern — exposes too much by default
- No control over what's exposed
- May expose tools consumers shouldn't access
- Explicit is better than implicit

---

## Consequences

### Positive

1. **Service aggregation** — WB-A can bundle related capabilities
2. **Simplified access** — Consumers access one machine instead of many
3. **Credential isolation** — Consumers don't need Machine-X credentials
4. **Controlled exposure** — WB-A decides what to expose
5. **Value-add opportunity** — WB-A can enhance transitive tools

### Negative

1. **Indirection** — Extra hop adds latency
2. **Dependency** — WB-B depends on WB-A's availability for Machine-X access
3. **Debug complexity** — Issues may be in WB-A, Machine-X, or between them

### Risks

1. **Over-exposure** — WB-A might expose too much from Machine-X
2. **Version drift** — Machine-X changes may break WB-A's exposure
3. **Performance** — Multiple hops accumulate latency

---

## Implementation Notes

### Transitive Tool Configuration

```yaml
# In WorkbenchAsMachine spec
exposed_tools:
  machine_tools:
    - tool_ref: core-banking/get-transaction
      exposed_name: get-transaction
      description: "Get transaction details"
      # Credentials resolved by WB-A at invocation time
```

### Invocation Flow

```
WB-B App → Direct Tool Dispatcher (WB-B) 
         → I/O Gateway (WB-A) 
         → Direct Tool Dispatcher (WB-A) 
         → Machine-X
```

### Credential Resolution

- WB-B uses its credentials to call WB-A
- WB-A uses its own credentials (or pass-through) to call Machine-X
- WB-B never sees Machine-X credentials

---

## Related Decisions

- [ADR-0040: Direct Tool Dispatcher](./0040-direct-tool-dispatcher.md)
- [ADR-0041: Standalone Tool as ToolInstance Variation](./0041-standalone-tool-variation.md)

