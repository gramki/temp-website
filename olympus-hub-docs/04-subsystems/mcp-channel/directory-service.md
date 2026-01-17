# Directory Service

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-17

The Directory Service exposes a catalog of available MCP Servers for **collaborators** (not MCP Clients). MCP Clients are injected with server configuration based on directory information.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Enable collaborators to discover and manage MCP Servers |
| **Audience** | Collaborators (Supervisors, Developers, Admins) — NOT MCP Clients |
| **Client Configuration** | MCP Clients are injected configuration (not self-discovered) |
| **Scope** | Workbench-scoped (except admin-template which is tenant-scoped) |

---

## Purpose

**Directory is for collaborators, not MCP Clients:**

- **Collaborators** use directory to browse, manage, and configure MCP Servers
- **MCP Clients** are given configuration by the system (injected, not discovered)
- Directory provides visibility and management capabilities for Hub personas

---

## Directory Tools

| Tool | Description | Available To |
|------|-------------|-------------|
| `list_mcp_servers` | List all MCP Servers accessible to the collaborator | All Collaborators |
| `get_mcp_server_info` | Get details about a specific MCP Server | All Collaborators |
| `get_client_config` | Generate client configuration for an MCP Server | All Collaborators |

---

## Directory Entry Structure

### Entry Format

```json
{
  "servers": [
    {
      "name": "payments-mcp-server",
      "display_name": "Payments MCP Server",
      "workbench": "payments-workbench",
      "template_kind": "business-user-template",
      "version": "1.0.0",
      "scenarios": ["bill-payment", "recurring-payment"],
      "endpoint": "mcp://hub.acme.io/payments/payments-mcp-server",
      "status": "provisioned",
      "tools_count": 15,
      "prompts_count": 3
    },
    {
      "name": "core-banking-mcp",
      "display_name": "Core Banking Tools",
      "workbench": "payments-workbench",
      "template_kind": "machine-template",
      "version": "1.0.0",
      "machine_ref": "acme-core-banking",
      "tools_count": 8,
      "endpoint": "mcp://hub.acme.io/payments/core-banking-mcp",
      "status": "provisioned"
    }
  ]
}
```

### Entry Fields

| Field | Description | Example |
|-------|-------------|---------|
| `name` | MCP Server name (from CRD) | `payments-mcp-server` |
| `display_name` | Human-readable display name | `Payments MCP Server` |
| `workbench` | Workbench ID | `payments-workbench` |
| `template_kind` | Template kind | `business-user-template` |
| `version` | Server version | `1.0.0` |
| `scenarios` | Exposed scenarios (scenario-based templates) | `["bill-payment", "recurring-payment"]` |
| `machine_ref` | Machine reference (machine-template) | `acme-core-banking` |
| `endpoint` | MCP endpoint URL | `mcp://hub.acme.io/payments/payments-mcp-server` |
| `status` | Provisioning status | `provisioned` |
| `tools_count` | Number of tools exposed | `15` |
| `prompts_count` | Number of prompt templates (scenario-based) | `3` |

---

## Client Injection

**MCP Clients are injected configuration:**

- Clients do not discover servers themselves
- System provides client configuration based on directory information
- Injection mechanism depends on client type:
  - **Cursor**: Configuration file or environment variable
  - **Claude Desktop**: Configuration in settings
  - **Custom clients**: API or configuration service

**Injection Flow:**
```
1. Collaborator uses directory to identify MCP Server
2. Collaborator generates client configuration via get_client_config tool
3. Configuration provided to client (file, API, etc.)
4. Client connects using provided configuration
```

---

## Access Control

Directory entries are filtered by:

- **Workbench Access**: Collaborator must have access to workbench
- **OPA Policy**: Directory queries evaluated against collaborator's access token
- **Template Kind**: Collaborator sees servers for their persona/template kind

**Example:**
- Supervisor sees `supervisor-template` servers in their workbench
- Developer sees `creator-template` servers in their workbench
- Admin sees all servers (tenant-scoped)

---

## Directory Operations

### List MCP Servers

```json
{
  "method": "tools/call",
  "params": {
    "name": "list_mcp_servers",
    "arguments": {
      "workbench": "payments-workbench",
      "template_kind": "business-user-template"  // optional filter
    }
  }
}
```

**Response:**
```json
{
  "servers": [
    {
      "name": "payments-mcp-server",
      "display_name": "Payments MCP Server",
      "workbench": "payments-workbench",
      "template_kind": "business-user-template",
      "version": "1.0.0",
      "scenarios": ["bill-payment", "recurring-payment"],
      "endpoint": "mcp://hub.acme.io/payments/payments-mcp-server",
      "status": "provisioned"
    }
  ]
}
```

### Get MCP Server Info

```json
{
  "method": "tools/call",
  "params": {
    "name": "get_mcp_server_info",
    "arguments": {
      "server_name": "payments-mcp-server",
      "workbench": "payments-workbench"
    }
  }
}
```

**Response:**
```json
{
  "name": "payments-mcp-server",
  "display_name": "Payments MCP Server",
  "description": "MCP server for payment-related request operations",
  "workbench": "payments-workbench",
  "template_kind": "business-user-template",
  "version": "1.0.0",
  "scenarios": ["bill-payment", "recurring-payment"],
  "tools": [
    {
      "name": "create_service_request",
      "description": "Create a new service request"
    },
    // ... more tools
  ],
  "prompts": [
    {
      "name": "how_to_initiate_request",
      "description": "Guidance on how to initiate a request"
    },
    // ... more prompts
  ],
  "endpoint": "mcp://hub.acme.io/payments/payments-mcp-server",
  "status": "provisioned",
  "provisioned_at": "2026-01-17T10:30:00Z"
}
```

### Get Client Configuration

```json
{
  "method": "tools/call",
  "params": {
    "name": "get_client_config",
    "arguments": {
      "server_name": "payments-mcp-server",
      "workbench": "payments-workbench",
      "client_type": "cursor"  // cursor | claude | custom
    }
  }
}
```

**Response:**
```json
{
  "client_config": {
    "mcpServers": {
      "payments-mcp-server": {
        "url": "mcp://hub.acme.io/payments/payments-mcp-server",
        "auth": {
          "type": "oauth2",
          "authorization_endpoint": "https://hub.acme.io/oauth/authorize",
          "token_endpoint": "https://hub.acme.io/oauth/token"
        }
      }
    }
  }
}
```

---

## Related Documentation

- [MCP Server CRD](./mcp-server-crd.md) — Server configuration
- [MCP Operator](./mcp-operator.md) — Endpoint provisioning
- [ADR-0134](../../decision-logs/0134-mcp-directory-service.md) — MCP Directory Service

---

*TODO: C3-level details — exact directory API, client configuration formats, injection mechanisms*
