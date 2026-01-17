# MCP Operator

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-17

The MCP Operator is a Kubernetes operator that watches MCP Server CRDs and provisions endpoints at the MCP Channel platform service. It bridges the gap between workbench-scoped configuration (CRDs) and platform infrastructure (MCP Channel).

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Provision MCP Server endpoints based on CRD configuration |
| **Scope** | Kubernetes operator pattern |
| **Lifecycle** | Watch CRDs → Provision/Deprovision endpoints |
| **Integration** | MCP Channel platform service, Tool Registry (for machine-template) |

---

## Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **CRD Watch** | Watch for MCP Server CRD create/update/delete events |
| **Endpoint Provisioning** | Create endpoints at MCP Channel for each MCP Server |
| **Tool Registration** | Register tools from Tool Registry (for machine-template) |
| **Endpoint Deprovisioning** | Remove endpoints when CRDs are deleted |
| **Status Updates** | Update CRD status with provisioning state |

---

## Operator Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                    MCP OPERATOR                                 │
│                                                                 │
│  1. Watch MCP Server CRDs (all template kinds)                 │
│     │                                                           │
│  2. On CREATE/UPDATE:                                           │
│     ├─▶ Validate CRD                                           │
│     ├─▶ Resolve tool source (for machine-template)             │
│     ├─▶ Query Tool Registry (if machine-template)               │
│     ├─▶ Provision endpoint at MCP Channel                       │
│     └─▶ Update CRD status                                       │
│                                                                 │
│  3. On DELETE:                                                  │
│     ├─▶ Deprovision endpoint                                    │
│     └─▶ Cleanup resources                                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Endpoint Provisioning Flow

### Scenario-Based Templates

For scenario-based templates (business-user-template, supervisor-template, etc.):

```
1. Operator detects CRD create/update
2. Validate CRD structure
3. Extract exposed scenarios
4. Provision endpoint at MCP Channel:
   - Endpoint path: /mcp/{workbench}/{server-name}
   - Register tools (from template defaults + scenarios)
   - Register prompt templates
   - Register resource types
   - Configure session settings
5. Update CRD status: Provisioned
```

### Machine Template

For `machine-template`:

```
1. Operator detects CRD create/update
2. Validate CRD structure
3. Resolve tool source:
   - If machine_ref: Query Tool Registry for all tools from Machine
   - If tools list: Query Tool Registry for specific tools
4. Validate tools exist and are accessible
5. Provision endpoint at MCP Channel:
   - Endpoint path: /mcp/{workbench}/{server-name}
   - Register tools from Tool Registry
   - Configure passthrough routing to HTTP Tool Calling Application
6. Update CRD status: Provisioned
```

---

## CRD Status

The operator updates CRD status to reflect provisioning state:

```yaml
status:
  phase: Provisioned  # Provisioning | Provisioned | Failed
  endpoint: /mcp/payments-workbench/payments-mcp-server
  tools_count: 15
  last_provisioned: "2026-01-17T10:30:00Z"
  conditions:
    - type: EndpointReady
      status: "True"
      lastTransitionTime: "2026-01-17T10:30:00Z"
    - type: ToolsRegistered
      status: "True"
      lastTransitionTime: "2026-01-17T10:30:05Z"
```

---

## Integration Points

### MCP Channel Platform Service

The operator provisions endpoints at the MCP Channel platform service:

- **Endpoint Registration**: Register endpoint path and configuration
- **Tool Catalog**: Register tools, prompts, resources per endpoint
- **Access Policy**: Configure OPA policy evaluation per endpoint
- **Session Configuration**: Configure session settings (for scenario-based templates)

### Tool Registry

For `machine-template`, the operator queries Tool Registry:

- **Tool Discovery**: Query tools by Machine ID or explicit tool list
- **Tool Resolution**: Resolve tool endpoints, authentication, flow control
- **Tool Registration**: Register tools with MCP Router for passthrough

### Kubernetes API

The operator watches Kubernetes API for CRD events:

- **CRD Watch**: Watch all MCP Server template kinds
- **Status Updates**: Update CRD status subresource
- **Event Logging**: Log provisioning events for observability

---

## Error Handling

| Error Condition | Operator Behavior |
|----------------|-------------------|
| **Invalid CRD** | Mark status as Failed, log validation errors |
| **Tool Not Found** | Mark status as Failed (for machine-template) |
| **Endpoint Provisioning Failure** | Retry with exponential backoff, mark Failed after max retries |
| **Tool Registry Unavailable** | Retry, mark status as Provisioning until resolved |

---

## Observability

The operator provides:

- **CRD Status**: Current provisioning state per CRD
- **Event Logs**: Kubernetes events for CRD lifecycle
- **Metrics**: Provisioning success/failure rates, endpoint counts
- **Traces**: End-to-end provisioning flow traces

---

## Related Documentation

- [MCP Server CRD](./mcp-server-crd.md) — CRD specification
- [Machine Template](./machine-template.md) — Tool Registry integration
- [MCP Channel README](./README.md) — Subsystem overview
- [Tool Registry](../registry-services/tool-registry.md) — Tool discovery

---

*TODO: C3-level details — exact endpoint provisioning API, retry policies, reconciliation logic*
