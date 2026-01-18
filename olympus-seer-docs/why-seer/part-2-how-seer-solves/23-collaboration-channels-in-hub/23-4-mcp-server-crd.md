# 23.4 MCP Server CRD Design

Hub enables AI agents and assistants to interact with Hub capabilities via the Model Context Protocol (MCP). The MCP Server CRD design enables developers to publish multiple MCP Servers per workbench, allowing segregation by functional boundaries, privilege boundaries, or business needs. This design addresses the collaboration channel requirements established in Section 5.15.1, enabling persona-specific access with fine-grained control.

## Purpose of This Section

This section explains how Hub implements MCP Servers as Custom Resource Definitions (CRDs) with template-based persona inference. It describes how multiple MCP Servers per workbench enable fine-grained access control, how template kinds imply persona and capabilities, and how OPA-based access control provides enterprise-grade security.

MCP Server CRDs extend the multi-channel access capabilities described in Section 23.3, providing a structured mechanism for exposing Hub capabilities to AI assistants (ChatGPT, Claude, Gemini) and other MCP clients.

## Core Concepts & Definitions

### MCP Server as CRD

An **MCP Server** is a workbench-scoped Custom Resource Definition that exposes Hub capabilities via the Model Context Protocol. Each MCP Server:

- **Exposes scenarios, tools, and resources** to MCP clients
- **Uses template kind** to imply persona and default capabilities
- **Controls access** via OPA-based policies
- **Supports multiple servers per workbench** for segregation

MCP Servers follow Hub's CRD-based configuration pattern, enabling versioning, GitOps workflows, and lifecycle management.

### Template Kind Implies Persona

The **template kind** (e.g., `business-user-template`, `supervisor-template`) implies the persona and capabilities without requiring an explicit persona field:

```yaml
apiVersion: hub.olympus.io/v1
kind: business-user-template  # Template kind implies persona
metadata:
  name: payments-mcp-server
spec:
  # No explicit persona field - template kind implies it
  exposed_scenarios:
    - scenario_ref: bill-payment
```

This design provides:
- **Type safety**: Template kind is part of CRD kind, enabling compile-time validation
- **Default capabilities**: Each template kind has sensible defaults for tools, resources, and sessions
- **Clear intent**: Template kind clearly indicates persona and capabilities

### Scenarios Automatically Include Requests

When scenarios are included in an MCP Server specification, corresponding requests are automatically included. There is no need to specify `request_type` separately:

```yaml
exposed_scenarios:
  - scenario_ref: bill-payment  # Automatically includes bill-payment requests
```

This design simplifies configuration and ensures consistency between scenarios and their request types.

### OPA-Based Access Control

MCP Servers use **OPA-based access control** via the `access_policy` field. The policy evaluates:

- **Access token claims**: User identity, roles, scopes
- **Delegation templates**: For request-scoped delegation
- **User profile**: Workbench membership, permissions
- **Request context**: For request-scoped operations

OPA policies provide fine-grained authorization that aligns with Hub's existing access control model.

## Conceptual Models / Frameworks

### Template Kind Taxonomy

Hub supports **seven template kinds** organized into two categories:

**Scenario-Based Templates** (Request Lifecycle):
- `business-user-template`: Business Customer, Employee, System — request initiation and participation
- `supervisor-template`: Supervisor — queue management, SLAs, directability
- `agent-template`: Agent (Human/AI) — task processing, knowledge access
- `creator-template`: Process Architect, Developer — scenario design, feedback management
- `admin-template`: Administrator — subscription and resource management
- `auditor-template`: Auditor — compliance and investigation capabilities

**Tool-Based Templates** (Passthrough):
- `machine-template`: Expose Machine tools via MCP — stateless tool invocation, no request lifecycle

### Multiple Servers per Workbench Pattern

Multiple MCP Servers per workbench enable segregation:

```
Workbench: payments-workbench
    ├── MCP Server: payments-customer-mcp (business-user-template)
    │   └── Exposes: customer-facing scenarios
    ├── MCP Server: payments-operations-mcp (supervisor-template)
    │   └── Exposes: operations management scenarios
    └── MCP Server: payments-tools-mcp (machine-template)
        └── Exposes: payment processing tools (stateless)
```

This pattern enables:
- **Functional segregation**: Different servers for different functional areas
- **Privilege segregation**: Read-only servers vs. write-capable servers
- **Business segregation**: Customer-facing vs. internal operations

### MCP Directory Service

The **MCP Directory Service** enables collaborators to discover available MCP Servers:

- **Directory tools**: `list_mcp_servers`, `get_mcp_server_info`, `get_client_config`
- **Access control**: Directory entries filtered by collaborator's workbench access and OPA policy
- **Client configuration injection**: MCP Clients receive configuration from the system (not self-discovery)

The directory service separates management (for collaborators) from connection (for MCP clients), providing appropriate mechanisms for each audience.

## Systemic and Enterprise Considerations

### Multiple Servers for Functional/Privilege Boundaries

Organizations can create multiple MCP Servers per workbench to segregate:

- **Functional boundaries**: Payments vs. Disputes vs. Onboarding
- **Privilege boundaries**: Read-only vs. write-capable servers
- **Business needs**: Customer-facing vs. internal operations

This segregation enables fine-grained access control and reduces the risk of over-exposure.

### OPA Policy Management

OPA policies for MCP Servers must be:

- **Maintainable**: Policies should be versioned and managed via GitOps
- **Testable**: Policies should be testable independently of server deployment
- **Auditable**: Policy changes should be tracked and reviewed

Organizations should establish governance processes for MCP Server access policies, similar to other access control policies.

### Discovery via Directory Service

The MCP Directory Service provides:

- **Collaborator management**: Browse, configure, and manage MCP Servers
- **Client configuration**: Inject configuration into MCP clients (not self-discovery)
- **Access control**: Filter directory entries by collaborator permissions

Organizations should establish processes for managing MCP Server discovery and client configuration.

### Template Kind Maintenance

Template kinds must be maintained as Hub capabilities evolve:

- **New capabilities**: Template kinds may need updates when new Hub capabilities are added
- **Persona changes**: Template kinds may need updates when persona capabilities change
- **Backward compatibility**: Template kind changes must maintain backward compatibility

Organizations should monitor template kind evolution and update MCP Server configurations accordingly.

## Common Misconceptions & Failure Modes

### Misconception 1: One Server per Workbench per Persona

**Misconception**: Each workbench should have one MCP Server per persona.

**Reality**: Multiple MCP Servers per workbench enable fine-grained segregation. A workbench can have multiple servers for the same persona, each exposing different scenarios or capabilities.

**Failure mode**: Organizations create overly broad servers that expose too many capabilities, increasing security risk and reducing flexibility.

### Misconception 2: Template Kind Is Just a Label

**Misconception**: Template kind is just a label; capabilities are fully configurable.

**Reality**: Template kind implies default capabilities, persona, and validation rules. While capabilities can be customized, the template kind provides sensible defaults and type safety.

**Failure mode**: Organizations ignore template kind defaults and configure capabilities from scratch, missing the benefits of template-based design.

### Misconception 3: All Scenarios Must Be Exposed

**Misconception**: MCP Servers must expose all scenarios in a workbench.

**Reality**: MCP Servers selectively expose scenarios via `exposed_scenarios`. Organizations can create multiple servers, each exposing different subsets of scenarios.

**Failure mode**: Organizations expose all scenarios in a single server, increasing security risk and reducing flexibility.

### Misconception 4: MCP Clients Discover Servers

**Misconception**: MCP Clients discover available servers by connecting to a workbench endpoint.

**Reality**: MCP Clients receive configuration from the system (injected configuration). The directory service is for collaborators to manage servers, not for clients to discover them.

**Failure mode**: Organizations design client discovery mechanisms, increasing complexity and security risk.

## Practical Implications

### When to Create Multiple Servers

Organizations should create multiple MCP Servers when:

- **Functional segregation needed**: Different functional areas require different access patterns
- **Privilege segregation needed**: Read-only vs. write-capable access requires separate servers
- **Business segregation needed**: Customer-facing vs. internal operations require separate servers
- **Template kind mismatch**: Different template kinds are needed for different use cases

### Template Kind Selection

Organizations should select template kinds that:

- **Match persona needs**: Select template kinds that match the intended persona's needs
- **Provide appropriate defaults**: Leverage template defaults rather than configuring from scratch
- **Enable required capabilities**: Ensure template kind supports required tools and resources

Template kind selection directly impacts server capabilities and access control.

### OPA Policy Design

Organizations should design OPA policies that:

- **Align with workbench access**: Policies should align with workbench-level access control
- **Support delegation**: Policies should support request-scoped delegation when applicable
- **Maintain auditability**: Policy decisions should be auditable

OPA policy design directly impacts security and compliance.

### Client Configuration Management

Organizations should establish processes for:

- **Client onboarding**: How MCP clients receive initial configuration
- **Configuration updates**: How configuration changes are propagated to clients
- **Access revocation**: How client access is revoked when needed

Client configuration management ensures that MCP clients have appropriate access without exposing discovery complexity.

## Cross-References

- **Section 5.15.1 (Channel Diversity Needs)**: Establishes the need for multiple access channels, including MCP
- **Section 1.9 (Persona-Specific Desks)**: Describes persona-specific experiences that MCP Servers extend
- **Section 8 (Identity & Authority)**: OPA access control uses identity and authority models
- **Section 23.3 (Multi-Channel Access)**: MCP Server is one of multiple collaboration channels

---

**References:**
*   `olympus-hub-docs/decision-logs/0131-mcp-server-crd-design.md` — Architectural decision record
*   `olympus-hub-docs/decision-logs/0132-mcp-template-kinds.md` — Template kind definitions
*   `olympus-hub-docs/decision-logs/0134-mcp-directory-service.md` — Directory service design
*   `olympus-hub-docs/04-subsystems/mcp-channel/mcp-server-crd.md` — Complete CRD specification
*   `olympus-hub-docs/04-subsystems/mcp-channel/README.md` — MCP Channel subsystem overview
