# 0134. MCP Directory Service for Collaborators

## Status

Accepted

## Date

2026-01-17

## Context

Hub needs a mechanism for discovering available MCP Servers. There are two distinct audiences:
1. **Collaborators** (Supervisors, Developers, Admins) who need to browse, manage, and configure MCP Servers
2. **MCP Clients** (AI agents) that need to connect to MCP Servers

The system needs to distinguish between these audiences and provide appropriate mechanisms for each.

### Constraints

- Must support multiple MCP Servers per workbench
- Must enable collaborators to discover and manage servers
- Must provide client configuration without exposing discovery complexity to clients
- Must respect access control (collaborators see servers they have access to)

### Requirements

- Directory service for collaborators to browse servers
- Client configuration injection (not self-discovery)
- Access control per collaborator role
- Support for all template kinds

## Decision

We will expose a **Directory Service for collaborators** (not MCP Clients), and **inject client configuration** based on directory information.

### Key Points

- **Directory for collaborators**: Exposed via tools (`list_mcp_servers`, `get_mcp_server_info`, `get_client_config`)
- **Clients are injected configuration**: MCP Clients do not discover servers; they are given configuration by the system
- **All template types included**: Directory includes all MCP Server template kinds
- **Access control**: Directory entries filtered by collaborator's workbench access and OPA policy

## Alternatives Considered

### Alternative 1: Client Self-Discovery

**Description:** MCP Clients discover servers by connecting to workbench endpoint

**Pros:**
- Clients can discover available servers
- Dynamic discovery

**Cons:**
- Clients must handle discovery complexity
- Security concerns (clients see all servers)
- No management interface for collaborators

**Why rejected:** Clients should not handle discovery; system should provide configuration

---

### Alternative 2: Unified Discovery for All

**Description:** Single discovery mechanism for both collaborators and clients

**Pros:**
- Single mechanism
- Simpler architecture

**Cons:**
- Different needs (management vs. connection)
- Security concerns (clients see management info)
- Poor separation of concerns

**Why rejected:** Collaborators and clients have different needs; separate mechanisms provide better security and UX

---

### Alternative 3: No Directory (Explicit Configuration Only)

**Description:** No directory service; all configuration explicit

**Pros:**
- Simple
- No discovery overhead

**Cons:**
- Poor collaborator experience
- Hard to manage multiple servers
- No visibility into available servers

**Why rejected:** Collaborators need directory for management; clients need injected configuration

## Consequences

### Positive

- **Clear Separation**: Collaborators use directory; clients get injected config
- **Security**: Clients don't see management information
- **Management**: Collaborators can browse and manage servers
- **Flexibility**: Injection mechanism can vary by client type
- **Access Control**: Directory respects access control per collaborator

### Negative

- **Two Mechanisms**: Directory for collaborators, injection for clients
- **Injection Complexity**: Need to support different client types

### Neutral

- **Directory Tools**: Tools for directory operations (list, get info, get config)
- **Client Configuration**: Configuration format depends on client type

## Implementation Notes

- Directory service defined in [Directory Service](../../04-subsystems/mcp-channel/directory-service.md)
- Directory tools: `list_mcp_servers`, `get_mcp_server_info`, `get_client_config`
- Client injection mechanism depends on client type (Cursor, Claude Desktop, custom)
- Directory entries filtered by workbench access and OPA policy

## Related Decisions

- [ADR-0131: MCP Server CRD Design](./0131-mcp-server-crd-design.md) — CRD structure
- [ADR-0132: MCP Template Kinds](./0132-mcp-template-kinds.md) — Template kinds

## References

- [Directory Service](../../04-subsystems/mcp-channel/directory-service.md)
- [MCP Server CRD](../../04-subsystems/mcp-channel/mcp-server-crd.md)
