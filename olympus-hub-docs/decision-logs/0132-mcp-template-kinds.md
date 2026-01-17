# 0132. MCP Template Kinds

## Status

Accepted

## Date

2026-01-17

## Context

Hub needs to support different persona-scoped MCP access with different capabilities. Each persona has different needs:
- Business users need request initiation and participation
- Supervisors need queue management and agent oversight
- Agents need task processing and knowledge access
- Developers need scenario design and feedback management
- Administrators need subscription and resource management
- Auditors need compliance and investigation capabilities

Additionally, there is a need to expose Tool Registry tools via MCP without request lifecycle overhead.

### Constraints

- Must support persona-scoped access
- Must align with existing Hub persona model
- Must enable different capabilities per persona
- Must support both request lifecycle and stateless tool invocation

### Requirements

- Different template kinds for different personas
- Each template kind implies default tools, resources, and capabilities
- Support for stateless tool exposure (machine-template)
- Template kind is part of CRD kind (type-safe)

## Decision

We will support **seven template kinds** organized into two categories:

### Scenario-Based Templates (Request Lifecycle)

- `business-user-template` — Business Customer, Employee, System
- `supervisor-template` — Supervisor
- `agent-template` — Agent (Human/AI)
- `creator-template` — Process Architect, Developer
- `admin-template` — Administrator
- `auditor-template` — Auditor

### Tool-Based Templates (Passthrough)

- `machine-template` — Expose Machine tools via MCP

### Key Points

- **Template kind is part of CRD kind**: `kind: business-user-template` (not `kind: MCPServer` with `spec.persona`)
- **Template implies capabilities**: Each template kind has default tools, resources, and capabilities
- **Scenario-based templates**: Full request lifecycle, prompts, resources, sessions
- **machine-template**: Stateless tool invocation, no request lifecycle

## Alternatives Considered

### Alternative 1: Single CRD Kind with Persona Field

**Description:** `kind: MCPServer` with `spec.persona: BusinessUser`

**Pros:**
- Single CRD kind
- Explicit persona declaration

**Cons:**
- Less type-safe
- Harder to validate
- Redundant with template capabilities

**Why rejected:** Template kind provides better type safety and clearer intent

---

### Alternative 2: Separate CRD per Persona

**Description:** `BusinessUserMCPServer`, `SupervisorMCPServer`, etc.

**Pros:**
- Very explicit
- Strong type safety

**Cons:**
- Too many CRD kinds
- Harder to maintain
- Less flexible

**Why rejected:** Template kind pattern provides good balance of type safety and flexibility

---

### Alternative 3: No Template Kinds (Generic CRD)

**Description:** Single generic CRD with all capabilities configurable

**Pros:**
- Maximum flexibility
- Single CRD kind

**Cons:**
- Too complex
- Hard to validate
- No default capabilities
- Poor developer experience

**Why rejected:** Template kinds provide better developer experience and validation

## Consequences

### Positive

- **Type Safety**: Template kinds provide compile-time type safety
- **Default Capabilities**: Each template has sensible defaults
- **Clear Intent**: Template kind clearly indicates persona and capabilities
- **Flexibility**: Supports both request lifecycle and stateless patterns
- **Developer Experience**: Easier to understand and configure

### Negative

- **Multiple CRD Kinds**: Seven template kinds to maintain
- **Template Maintenance**: Need to keep templates aligned with persona capabilities

### Neutral

- **CRD Validation**: Each template kind can have its own validation rules
- **Operator Complexity**: MCP Operator must handle all template kinds

## Implementation Notes

- Template kinds defined in [MCP Server CRD](../../04-subsystems/mcp-channel/mcp-server-crd.md)
- machine-template has dedicated document: [Machine Template](../../04-subsystems/mcp-channel/machine-template.md)
- Each template kind implies default tools, resources, and capabilities
- OPA policies can be template-specific

## Related Decisions

- [ADR-0131: MCP Server CRD Design](./0131-mcp-server-crd-design.md) — CRD structure
- [ADR-0135: Machine Template Passthrough Pattern](./0135-machine-template-passthrough.md) — machine-template design

## References

- [MCP Server CRD](../../04-subsystems/mcp-channel/mcp-server-crd.md)
- [Machine Template](../../04-subsystems/mcp-channel/machine-template.md)
