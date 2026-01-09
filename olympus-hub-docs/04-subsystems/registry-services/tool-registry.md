# Tool Registry

> **Status:** 🔴 Stub — Placeholder for expansion

The Tool Registry is the **catalog of tools available for agent and automation use** within Hub—a critical integration point for Seer. The registry operates at two levels: **Tool Protocols** (abstract specifications) and **Tools** (concrete, invocable instances).

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Catalog tool protocols and concrete tool instances |
| **Consumers** | AI Agents (via Seer), Automation Runtimes, Human Agents |
| **Scope** | Tool Protocols in Machine Definitions + Concrete Tools bound to Machines |
| **Integration** | Machine Registry, MCP Router, Seer Context Assembly |

---

## Two-Level Model

The Tool Registry works in conjunction with the Machine Registry to provide a complete tool resolution model:

```
┌─────────────────────────────────────────────────────────────────┐
│                    TOOL PROTOCOL                                 │
│                 (Abstract Specification)                         │
│                                                                  │
│  Part of Machine Definition                                      │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  get-account (OpenAPI Specification)                     │    │
│  │                                                          │    │
│  │  - Path: /accounts/{{accountId}}                        │    │
│  │  - Method: GET                                           │    │
│  │  - Server: {{base_url}}                                  │    │
│  │  - Input Schema: { accountId: string }                   │    │
│  │  - Output Schema: { account: AccountDetails }            │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ instantiated via Machine
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         TOOL                                     │
│                   (Concrete Instance)                            │
│                                                                  │
│  Bound to a Machine (acme-core-banking)                         │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  acme-get-account                                        │    │
│  │                                                          │    │
│  │  Protocol: get-account                                   │    │
│  │  Machine: acme-core-banking                              │    │
│  │  Variables: { base_url: "https://core.acme.com/api" }    │    │
│  │                                                          │    │
│  │  Access Policies:                                        │    │
│  │  - Allowed Roles: [operator, analyst]                    │    │
│  │  - Requires Approval: false                              │    │
│  │                                                          │    │
│  │  Flow Control:                                           │    │
│  │  - Rate Limit: 100/sec                                   │    │
│  │  - Timeout: 5000ms                                       │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Tool Protocol (Abstract Specification)

A **Tool Protocol** is an abstract tool specification that is integral to a Machine Definition. It describes *what* a tool does without *how* to invoke it concretely.

### Tool Protocol Schema

```yaml
tool_protocol:
  # Identity
  id: string                      # e.g., "get-account"
  name: string
  
  # Description
  display_name: string
  description: string
  documentation_url: string
  
  # Protocol Type & Specification
  protocol_type: enum             # openapi | asyncapi | grpc | graphql | mcp
  specification: object           # The actual protocol spec
  
  # Variables (placeholders in the specification)
  variables:
    - name: string
      description: string
      required: boolean
      default: string
  
  # Schema (derived from specification or explicit)
  input_schema: json_schema
  output_schema: json_schema
  
  # Classification
  category: enum                  # data_access | action | query | notification
  tags: array
  
  # Machine Definition Reference
  machine_definition_id: string
  machine_definition_version: string
```

### Protocol Types

| Protocol Type | Specification Format | Use Case |
|---------------|---------------------|----------|
| **openapi** | OpenAPI 3.x | REST API tools |
| **asyncapi** | AsyncAPI 2.x | Event/message tools |
| **grpc** | Protocol Buffers | High-performance RPC |
| **graphql** | GraphQL SDL | GraphQL queries/mutations |
| **mcp** | MCP Tool Schema | Native MCP tools |

---

## Tool (Concrete Instance)

A **Tool** is a concrete, invocable instance derived from a Tool Protocol and bound to a specific Machine. It has resolved endpoints, credentials, and policies.

### Tool Schema

```yaml
tool:
  # Identity
  id: string                      # e.g., "acme-get-account"
  name: string
  namespace: string               # Typically machine namespace
  
  # References
  protocol_id: string             # Reference to tool_protocol
  machine_id: string              # Reference to concrete Machine
  
  # Variable Overrides (tool-specific, on top of machine variables)
  variables: object
  
  # Access Control
  access_control:
    discoverability:
      allowed_workbenches: array
      allowed_roles: array
    invocation:
      allowed_roles: array
      requires_approval: boolean
      approval_workflow: string   # Workflow to run if approval needed
      delegatable: boolean        # Can be delegated to agents
  
  # Flow Control
  flow_control:
    rate_limit: number            # Requests per second
    burst_limit: number           # Max burst
    concurrency_limit: number     # Max concurrent calls
    timeout_ms: number
    retry_policy:
      max_attempts: number
      backoff: enum               # linear | exponential
  
  # Metadata
  status: enum                    # active | deprecated | suspended
  owner_team: string
```

### Example: Concrete Tool

```yaml
tool:
  id: "acme-get-account"
  name: "Get ACME Account"
  namespace: "acme-core-banking"
  
  protocol_id: "get-account"
  machine_id: "acme-core-banking"
  
  variables:
    # Override if different from machine-level
    response_format: "detailed"
  
  access_control:
    discoverability:
      allowed_workbenches: ["dispute-ops", "payment-ops"]
      allowed_roles: ["operator", "analyst", "auditor"]
    invocation:
      allowed_roles: ["operator", "analyst"]
      requires_approval: false
      delegatable: true
  
  flow_control:
    rate_limit: 100
    timeout_ms: 5000
    retry_policy:
      max_attempts: 3
      backoff: exponential
  
  status: active
```

---

## Standalone Tools

Not all tools are bound to external Machines. Hub also supports **standalone tools** for:
- Internal Hub utilities
- Computation tools
- Notification services
- Custom tenant tools

Standalone tools follow the same schema but with `machine_id: null` and an explicit provider:

```yaml
tool:
  id: "calculate-risk-score"
  name: "Calculate Risk Score"
  namespace: "hub-utilities"
  
  machine_id: null                # Not bound to a machine
  protocol_id: null               # Self-contained
  
  provider:
    type: enum                    # http | grpc | mcp | internal
    endpoint: string
    auth_method: string
  
  # Full specification inline
  input_schema: json_schema
  output_schema: json_schema
  
  # ... access_control, flow_control ...
```

---

## Tool Resolution

When an agent or automation requests a tool:

```
                    Tool Request: "acme-get-account"
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      Tool Registry                           │
│                                                              │
│  1. Lookup Tool by ID                                        │
│  2. Verify access (workbench, role, delegation)              │
│  3. Fetch Machine (for connection details)                   │
│  4. Fetch Tool Protocol (for specification)                  │
│  5. Resolve variables (machine + tool overrides)             │
│  6. Apply flow control policies                              │
│  7. Return resolved Tool Invocation Context                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    Resolved Invocation Context:
                    - Endpoint: https://core.acme.com/api/accounts/{id}
                    - Auth: OAuth2 (token from vault)
                    - Rate Limit: 100/sec
                    - Timeout: 5000ms
```

---

## Tool Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Data Access** | Retrieve business entity data | Get customer, Get transaction |
| **Action** | Perform business actions | Create case, Initiate payment |
| **Query** | Search and filter data | Search transactions, List accounts |
| **Notification** | Send communications | Send email, Push notification |
| **Computation** | Calculations and transformations | Calculate risk, Format report |

---

## Tool Lifecycle

```
[Registered] → [Active] → [Deprecated] → [Retired]
                   │
                   └─→ [Suspended] (temporary, e.g., outage)
```

### Lifecycle Events

| Event | Trigger | Effect |
|-------|---------|--------|
| **Registered** | Tool created | Not yet available |
| **Activated** | Admin approval | Available for use |
| **Deprecated** | Version superseded | Warning on use |
| **Suspended** | Operational issue | Temporarily unavailable |
| **Retired** | End of life | Permanently unavailable |

---

## MCP Router Integration

The Tool Registry integrates with MCP Router for agent tool access:

| MCP Concept | Tool Registry Role |
|-------------|-------------------|
| **Tool List** | Registry provides filtered tool catalog |
| **Tool Schema** | Protocol specification served as MCP schema |
| **Access Control** | OPA policies reference Tool Registry permissions |
| **Template Variables** | Mustache templates resolved from tool/machine variables |
| **Invocation** | MCP Router routes to Machine endpoint |

---

## Workbench Tool Access

Each Workbench defines:
- **Available Tools** — Subset of registry accessible in workbench
- **Default Tools** — Tools always available for scenarios
- **Restricted Tools** — Tools requiring elevated access or approval

---

## API Operations

| Operation | Description |
|-----------|-------------|
| `register_protocol` | Register a tool protocol (via Machine Definition) |
| `register_tool` | Register a concrete tool instance |
| `update_tool` | Update tool configuration |
| `deprecate` | Mark tool as deprecated |
| `suspend` | Temporarily suspend tool |
| `discover` | List available tools (permission-filtered) |
| `get` | Get tool details with resolved specification |
| `resolve` | Get invocation context for a tool |

---

## Related Documentation

- [Registry Services Overview](./README.md)
- [Machine Registry](./machine-registry.md) — Machine definitions and instances
- [MCP Router](../../05-infrastructure/mcp-orchestrator.md)
- [Heracles Gateway](../../05-infrastructure/heracles-gateway.md)

---

*TODO: Detailed design — OPA policy integration, MCP tool specification mapping, template variable resolution*

