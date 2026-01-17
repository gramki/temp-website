# 0135. Machine Template Passthrough Pattern

## Status

Accepted

## Date

2026-01-17

## Context

Hub needs to expose Tool Registry tools via MCP without request lifecycle overhead. Some use cases require stateless tool invocation (e.g., account lookup, transaction validation) that don't need the full request lifecycle management provided by scenario-based templates.

The system needs a mechanism to:
- Expose Machine tools from Tool Registry via MCP
- Support stateless tool invocation (no request lifecycle)
- Reuse existing infrastructure (Tool Registry, HTTP Tool Calling Application)
- Maintain consistent access control model

### Constraints

- Must integrate with Tool Registry two-level model (Tool Protocols + Tools)
- Must support both Machine reference and explicit tool list
- Must avoid request lifecycle overhead for stateless operations
- Must maintain OPA-based access control

### Requirements

- Expose Tool Registry tools via MCP
- Stateless invocation (no requests, no sessions, no resources)
- MCP Router acts as gateway (authentication, protocol translation)
- Passthrough to HTTP Tool Calling Application

## Decision

We will support a **machine-template** that exposes Tool Registry tools via MCP with a **passthrough pattern** where MCP Router acts as a gateway.

### Key Points

- **machine-template exposes tools from Tool Registry**: Collection of tools (by Machine or explicit list)
- **MCP Router acts as gateway**: Authentication, protocol translation, passthrough (no request lifecycle)
- **Invocation via HTTP Tool Calling Application**: Native HTTP tool calling (stateless)
- **No request lifecycle**: No requests, no prompts, no resources, no sessions
- **Tool source options**: Machine reference OR explicit tool list
- **OPA policy controls access**: Same access control model as other templates

## Alternatives Considered

### Alternative 1: Scenario-Based Template with Minimal Request

**Description:** Use scenario-based template but create minimal requests for tool calls

**Pros:**
- Reuses existing template
- Consistent pattern

**Cons:**
- Unnecessary request lifecycle overhead
- Poor performance for stateless operations
- Complex for simple tool calls

**Why rejected:** Overhead of request lifecycle is unnecessary for stateless tool calls

---

### Alternative 2: Direct Tool Registry Integration

**Description:** MCP Router directly queries Tool Registry, bypasses HTTP Tool Calling Application

**Pros:**
- Direct integration
- No intermediate layer

**Cons:**
- Duplicates HTTP Tool Calling Application logic
- Inconsistent with Hub patterns
- Harder to maintain

**Why rejected:** HTTP Tool Calling Application already provides the right abstraction; reuse it

---

### Alternative 3: Separate Protocol for Tool Invocation

**Description:** New protocol/endpoint specifically for stateless tool invocation

**Pros:**
- Clear separation
- Optimized for stateless

**Cons:**
- Additional protocol to maintain
- Inconsistent with MCP pattern
- More complexity

**Why rejected:** MCP protocol already supports stateless tool calls; no need for separate protocol

## Consequences

### Positive

- **Performance**: No request lifecycle overhead for stateless operations
- **Reuse**: Leverages existing Tool Registry and HTTP Tool Calling Application
- **Consistency**: Same access control model (OPA) as other templates
- **Flexibility**: Supports both Machine reference and explicit tool list
- **Simplicity**: Stateless pattern is simpler for tool invocation

### Negative

- **No Request Lifecycle**: Cannot track tool invocations as requests
- **No Prompts**: Cannot provide guidance prompts for tools
- **No Resources**: Cannot subscribe to tool-related resources
- **No Sessions**: Stateless means no session management

### Neutral

- **Gateway Pattern**: MCP Router acts as gateway (not full MCP Server)
- **Tool Registry Dependency**: Requires Tool Registry for tool discovery

## Implementation Notes

- machine-template defined in [Machine Template](../../04-subsystems/mcp-channel/machine-template.md)
- Tool source options: `machine_ref` (all tools from Machine) OR `tools` (explicit list)
- MCP Router performs authentication, authorization, protocol translation
- HTTP Tool Calling Application handles actual tool invocation
- OPA policy structure same as other templates (C3 detail)

## Related Decisions

- [ADR-0131: MCP Server CRD Design](./0131-mcp-server-crd-design.md) — CRD structure
- [ADR-0132: MCP Template Kinds](./0132-mcp-template-kinds.md) — Template kinds
- [ADR-0023: HTTP Tool Calling Application](../0023-http-tool-calling-application.md) — HTTP tool invocation

## References

- [Machine Template](../../04-subsystems/mcp-channel/machine-template.md)
- [Tool Registry](../../04-subsystems/registry-services/tool-registry.md)
- [HTTP Tool Calling Application](../../04-subsystems/hub-native-utilities/http-tool-calling-application.md)
