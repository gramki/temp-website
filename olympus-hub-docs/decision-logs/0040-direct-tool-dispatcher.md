# ADR-0040: Direct Tool Dispatcher as Platform Utility

| Property       | Value                                           |
|----------------|-------------------------------------------------|
| **Status**     | Accepted                                        |
| **Date**       | 2026-01-06                                      |
| **Category**   | Hub Native Utilities                            |
| **Deciders**   | Architecture Team                               |
| **Supersedes** | -                                               |

---

## Context

Hub Applications need to invoke tools (external machine tools, standalone tools, decision tools) as part of their processing. Two paths exist:

1. **Via Signal Exchange** — Create a Request, trigger a Scenario, receive updates
2. **Direct Invocation** — Call the tool directly without SX/Request overhead

Many tool invocations are function-like (stateless, request-response) and don't need the full Request lifecycle. However, direct invocation still needs:
- Access control
- Credential management
- Observability
- Retry logic

---

## Decision

**Create a Direct Tool Dispatcher as a platform utility that routes tool invocations to target machines, handling credential resolution, access control, and observability. The dispatcher executes in the context of a (subscription, workbench) but is a shared platform component.**

### Key Characteristics

| Aspect | Decision |
|--------|----------|
| **Deployment** | Platform utility (shared), executes per (subscription, workbench) |
| **Credential Modes** | Pass-through, Configured, Escalation |
| **Access Control** | Enforced at dispatcher level; tool-level optional |
| **Observability** | Integrated with Olympus Watch |
| **Retry** | Dispatcher provides retry; tool defines config |

---

## Alternatives Considered

### 1. Application-Level Direct Calls

Each Hub Application manages its own HTTP calls to tools.

**Rejected because:**
- Duplicates credential management across applications
- No centralized access control
- Inconsistent observability
- Each application reinvents retry logic

### 2. Signal Exchange for All Invocations

Route all tool calls through Signal Exchange.

**Rejected because:**
- Unnecessary overhead for function-like operations
- Creates Requests that aren't needed
- Adds latency for simple calls
- SX is designed for operational scenarios, not function calls

### 3. Per-Tool Proxies

Each tool has its own proxy/gateway.

**Rejected because:**
- Complex to manage
- Duplicates functionality
- Inconsistent patterns
- More infrastructure to maintain

---

## Consequences

### Positive

1. **Optimal path** — Direct tool calls without SX overhead
2. **Centralized concerns** — Credentials, access, observability in one place
3. **Consistent pattern** — All tool invocations follow same model
4. **Flexible credentials** — Support for privilege escalation when needed
5. **Integrated observability** — All calls visible in Olympus Watch

### Negative

1. **Additional component** — One more thing to understand and configure
2. **Credential configuration** — Requires environment setup for tools
3. **Two paths** — Developers must choose between SX and direct invocation

### Risks

1. **Overuse** — Teams might bypass SX when they should use it
2. **Security** — Privilege escalation needs careful controls

---

## Related Decisions

- [ADR-0023: HTTP Tool Calling Application](./0023-http-tool-calling-application.md)
- [ADR-0041: Standalone Tool as ToolInstance Variation](./0041-standalone-tool-variation.md)
- [ADR-0042: Scenario as Tool Granularity](./0042-scenario-as-tool-granularity.md)

