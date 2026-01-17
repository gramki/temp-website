# 0131. MCP Server CRD Design

## Status

Accepted

## Date

2026-01-17

## Context

Hub needs to enable AI agents and assistants to interact with Hub capabilities via the Model Context Protocol (MCP). Developers should be able to publish multiple MCP Servers per workbench to segregate functional boundaries, privilege boundaries, or business needs.

The system needs a mechanism to:
- Define what Hub capabilities are exposed via MCP
- Control access per MCP Server
- Support different personas with different capabilities
- Enable multiple MCP Servers per workbench

### Constraints

- Must align with Hub's CRD-based configuration pattern
- Must support persona-scoped access (like REST Channels)
- Must enable segregation by functional/privilege boundaries
- Must integrate with existing OPA-based access control

### Requirements

- Developers can create multiple MCP Servers per workbench
- Each MCP Server can expose different scenarios/tools
- Access control via OPA policies
- Template-based approach to imply persona and capabilities

## Decision

We will use **Custom Resource Definitions (CRDs)** for MCP Servers with **template kinds** that imply persona and capabilities.

### Key Points

- **MCP Server is a CRD**: Defined as Kubernetes CRD, scoped to workbench
- **Template kind implies persona**: No explicit persona field; template kind (e.g., `business-user-template`) implies persona
- **Scenarios automatically include requests**: When scenarios are included, corresponding requests are automatically included (no need to specify request_type)
- **OPA-based access control**: Access limited via OPA policies using access token claims, scopes, delegation-templates

## Alternatives Considered

### Alternative 1: One MCP Server per Workbench per Persona

**Description:** Simple one-to-one mapping

**Pros:**
- Simple, straightforward
- Easy to discover

**Cons:**
- Cannot segregate by functional/privilege boundaries
- All scenarios in workbench exposed in one server
- Does not meet requirement for multiple servers

**Why rejected:** Does not support requirement for multiple MCP Servers per workbench

---

### Alternative 2: MCP Server as Configuration in Workbench Management

**Description:** MCP Server configuration stored in Workbench Management, not as CRD

**Pros:**
- Centralized configuration
- No new resource type

**Cons:**
- Less flexible than CRD
- Harder to version and manage
- Does not align with Hub's CRD pattern

**Why rejected:** CRD pattern provides better versioning, lifecycle management, and GitOps integration

---

### Alternative 3: Explicit Persona Field

**Description:** CRD with explicit `persona` field instead of template kind

**Pros:**
- Explicit persona declaration
- Easier to understand

**Cons:**
- Redundant with template kind
- More fields to maintain
- Less type-safe

**Why rejected:** Template kind already implies persona; explicit field would be redundant

## Consequences

### Positive

- **Flexibility**: Multiple MCP Servers per workbench enable fine-grained control
- **Consistency**: Aligns with Hub's CRD-based configuration pattern
- **Versioning**: CRDs support versioning and GitOps workflows
- **Type Safety**: Template kinds provide compile-time type safety
- **Access Control**: OPA-based policies provide fine-grained authorization

### Negative

- **Complexity**: Additional resource type to manage
- **Discovery**: Need directory service for collaborators to discover servers
- **Operator Overhead**: MCP Operator needed to provision endpoints

### Neutral

- **Template Kinds**: Need to define and maintain template kinds for each persona
- **OPA Policies**: Need to define OPA policy structure (C3 detail)

## Implementation Notes

- CRD structure defined in [MCP Server CRD](../../04-subsystems/mcp-channel/mcp-server-crd.md)
- Template kinds defined in [ADR-0132](./0132-mcp-template-kinds.md)
- MCP Operator provisions endpoints based on CRDs
- OPA policy structure to be defined at C3 level

## Related Decisions

- [ADR-0132: MCP Template Kinds](./0132-mcp-template-kinds.md) — Template kind definitions
- [ADR-0134: MCP Directory Service](./0134-mcp-directory-service.md) — Server discovery mechanism

## References

- [MCP Channel Subsystem](../../04-subsystems/mcp-channel/README.md)
- [MCP Server CRD](../../04-subsystems/mcp-channel/mcp-server-crd.md)
