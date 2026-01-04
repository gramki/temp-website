# Tool Registry

> **Status:** 🔴 Stub — Placeholder for expansion

The Tool Registry is the **catalog of tools available for agent and automation use** within Hub—a critical integration point for Seer.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Catalog tools with schemas, permissions, and providers |
| **Consumers** | AI Agents (via Seer), Automation Runtimes, Human Agents |
| **Scope** | System-provided + Tenant-registered tools |
| **Integration** | MCP Orchestrator, Seer Context Assembly |

---

## Why Tool Registry Matters

From the Seer integration requirements:
> *"Tool & Action Framework :: Tool Registry of Hub"*

Agents need:
- To discover what tools are available
- To understand tool schemas and capabilities
- To have authorized access to tools
- To invoke tools within their authority

---

## Tool Registration Schema

```yaml
tool:
  # Identity
  id: string
  name: string
  namespace: string
  version: string
  
  # Description
  display_name: string
  description: string
  documentation_url: string
  
  # Schema
  input_schema: json_schema
  output_schema: json_schema
  
  # Provider
  provider:
    type: enum  # http | grpc | mcp | internal
    endpoint: string
    auth_method: string
  
  # Access Control
  access_control:
    discoverability: policy  # who can see this tool
    invocation: policy       # who can invoke this tool
  
  # Metadata
  tags: array
  category: string
  status: enum  # active | deprecated | suspended
  
  # Operational
  timeout_ms: number
  retry_policy: object
  rate_limit: object
```

---

## Tool Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Data Access** | Retrieve business entity data | Get customer, Get transaction |
| **Action Execution** | Perform business actions | Create case, Send notification |
| **Integration** | External system integration | Call API, Query database |
| **Computation** | Calculations and transformations | Calculate risk, Format report |
| **Communication** | Messaging and notification | Send email, Post to channel |

---

## Tool Lifecycle

```
[Registered] → [Active] → [Deprecated] → [Retired]
                   │
                   └─→ [Suspended] (temporary)
```

---

## Access Control Model

### Discoverability
Who can see this tool in discovery:
- All agents in tenant
- Specific workbenches
- Specific roles

### Invocation Authorization
Who can invoke this tool:
- Role-based access
- Delegation-based (Employed Agent authority)
- Scope-based (workbench, entity type)

---

## MCP Orchestrator Integration

From the MCP Orchestrator design:

| MCP Concept | Tool Registry Role |
|-------------|-------------------|
| **Tool Registration** | Registered with Tool Registry |
| **Tool Discovery** | MCP Orchestrator queries Tool Registry |
| **Access Control** | OPA policies reference Tool Registry |
| **Template Variables** | Tool specs support Mustache templates |

---

## Workbench Tool Access

Each Workbench defines:
- **Available Tools** — Subset of registry accessible in workbench
- **Default Tools** — Tools always available
- **Restricted Tools** — Tools requiring elevated access

---

## API Operations

| Operation | Description |
|-----------|-------------|
| `register` | Register a new tool |
| `update` | Update tool configuration |
| `deprecate` | Mark tool as deprecated |
| `discover` | List available tools (permission-filtered) |
| `get` | Get tool details |
| `invoke` | Invoke a tool (via appropriate gateway) |

---

## Related Documentation

- [Registry Services Overview](./README.md)
- [MCP Orchestrator](../../05-infrastructure/mcp-orchestrator.md)
- [Heracles Gateway](../../05-infrastructure/heracles-gateway.md)

---

*TODO: Detailed design — OPA policy integration, MCP tool specification, template variables*

