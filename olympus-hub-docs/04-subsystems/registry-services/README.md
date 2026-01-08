# Registry Services

> **Status:** 🔴 Stub — Placeholder for expansion

Registry Services maintain the **catalogs of capabilities, machines, environments, and tools** available within the Hub ecosystem. The Machine and Tool registries operate at **two levels**: abstract definitions (templates) and concrete instances (runtime-usable).

---

## Overview

Registries are essential for:
- **Discovery** — What capabilities are available?
- **Governance** — What is authorized for use?
- **Configuration** — How are capabilities configured?
- **Versioning** — Which versions are in use?

---

## Registry Inventory

| Registry | Description | Status |
|----------|-------------|--------|
| [Machine Registry](./machine-registry.md) | Machine Definitions & Machine Instances | 🔴 Stub |
| [Tool Registry](./tool-registry.md) | Tool Protocols (in Definitions) & Tool Instances | 🔴 Stub |
| [Environment Registry](./environment-registry.md) | Operational environments with endpoints & credentials | 🔴 Stub |

---

## Two-Level Model: Definitions vs Instances

The Machine and Tool registries use a two-level hierarchy:

```
┌─────────────────────────────────────────────────────────────────┐
│                     DEFINITIONS (Abstract)                       │
│                                                                  │
│  ┌───────────────────────────┐    ┌───────────────────────────┐ │
│  │    Machine Definition     │    │     Tool Protocol         │ │
│  │  (e.g., temenos-t24)      │───▶│  (e.g., get-account)      │ │
│  │                           │    │                           │ │
│  │  • Type, Vendor           │    │  • OpenAPI/AsyncAPI spec  │ │
│  │  • Capabilities           │    │  • Variables: {{base_url}}│ │
│  │  • Signal schemas         │    │  • Input/Output schemas   │ │
│  │  • No endpoints           │    │  • No concrete URLs       │ │
│  └───────────────────────────┘    └───────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                                │
                                │ instantiate
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                     INSTANCES (Concrete)                         │
│                                                                  │
│  ┌───────────────────────────┐    ┌───────────────────────────┐ │
│  │       Machine             │    │         Tool              │ │
│  │  (e.g., acme-core-banking)│───▶│  (e.g., acme-get-account) │ │
│  │                           │    │                           │ │
│  │  • Endpoint URL           │    │  • Bound to Machine       │ │
│  │  • Credentials (vault)    │    │  • Resolved variables     │ │
│  │  • Variable bindings      │    │  • Access policies        │ │
│  │  • Access policies        │    │  • Flow control           │ │
│  └───────────────────────────┘    └───────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

**Key Points:**
- **Machine Definitions** are abstract templates; **Machines** are concrete instances
- **Tool Protocols** are abstract specs (part of Machine Definitions); **Tools** are concrete instances (bound to Machines)
- Definitions can be platform-provided or tenant-created; Instances are always tenant-specific
- Variables in Definitions use `{{variable}}` syntax, resolved when creating Instances

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   REGISTRY SERVICES                              │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                 REGISTRY API LAYER                          ││
│  │        (CRUD, Discovery, Search, Versioning)                ││
│  └─────────────────────────┬───────────────────────────────────┘│
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────────┐│
│  │                 REGISTRIES                                  ││
│  │                                                             ││
│  │  ┌───────────────────────────────────────────────────────┐ ││
│  │  │              Machine Registry                         │ ││
│  │  │  • Machine Definitions (+ Tool Protocols)             │ ││
│  │  │  • Machines (instances)                               │ ││
│  │  └───────────────────────────────────────────────────────┘ ││
│  │  ┌───────────────────────────────────────────────────────┐ ││
│  │  │              Tool Registry                            │ ││
│  │  │  • Tools (bound to Machines)                          │ ││
│  │  │  • Standalone Tools (not machine-bound)               │ ││
│  │  └───────────────────────────────────────────────────────┘ ││
│  │  ┌───────────────────────────────────────────────────────┐ ││
│  │  │           Environment Registry                        │ ││
│  │  │  • Endpoints, credentials, event buses, file stores   │ ││
│  │  └───────────────────────────────────────────────────────┘ ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │              STORAGE (System & Tenant Spec)                 ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

---

## Storage Layers

Registries span two storage layers:

| Layer | Content | Ownership |
|-------|---------|-----------|
| **System Data** | Platform-provided Machine Definitions, Tool Protocols | Platform |
| **Tenant Spec** | Tenant Machine Definitions, Machines, Tools, Environments | Tenant |

---

## Common Registry Patterns

### Registration
- Schema validation
- Version assignment
- Approval workflow (if required)

### Discovery
- List/search by criteria
- Filter by scope (workbench, tenant)
- Permission-aware filtering

### Versioning
- Semantic versioning
- Compatibility declarations
- Deprecation lifecycle

### Access Control
- Who can register?
- Who can discover?
- Who can invoke/use?

---

## Tool Specification Requirements

### OPA Context Schema

Every Tool Specification **must define its OPA context schema**. This schema specifies what data is available to OPA policies when evaluating authority at the Tool Gateway.

```yaml
# Tool Specification
apiVersion: hub.olympus.io/v1
kind: ToolSpecification
metadata:
  name: refund-approve
spec:
  # ... tool definition ...
  
  authority:
    # OPA context schema for this tool
    opaContextSchema:
      type: object
      properties:
        parameters:
          type: object
          description: Tool invocation parameters
          properties:
            amount:
              type: number
              description: Refund amount in cents
            case_id:
              type: string
            reason:
              type: string
        # Standard context (always available)
        agent:
          $ref: "#/definitions/AgentContext"
        access:
          $ref: "#/definitions/AccessContext"
        invocation:
          $ref: "#/definitions/InvocationContext"
    
    # Default OPA policy for this tool
    defaultPolicy: |
      package seer.authority.refund_approve
      
      default decision = "REJECT"
      
      decision = "ALLOW" {
        input.parameters.amount <= 10000
        input.agent.delegated_scopes[_] == "write:refunds"
      }
      
      reason = "Amount exceeds tool limit" {
        input.parameters.amount > 10000
      }
```

### Standard Context Definitions

These schemas are always available at the Tool Gateway:

```yaml
definitions:
  AgentContext:
    type: object
    description: Identity and authority of the invoking agent
    properties:
      agent_id:
        type: string
      training_spec:
        type: string
      employment_spec:
        type: string
      iam_role:
        type: string
      delegated_scopes:
        type: array
        items:
          type: string
      accountable_user:
        type: string
        description: IAM user or group accountable for this agent

  AccessContext:
    type: object
    description: Tenant and workbench context
    properties:
      tenant_id:
        type: string
      workbench_id:
        type: string
      scenario_id:
        type: string
      request_id:
        type: string

  InvocationContext:
    type: object
    description: Invocation metadata
    properties:
      timestamp:
        type: string
        format: date-time
      request_headers:
        type: object
        description: HTTP headers from invocation
      source_ip:
        type: string
```

### Policy Override Hierarchy

| Level | Scope | Override Behavior |
|-------|-------|-------------------|
| **Tool Specification** | Per-tool | Base policy |
| **Training Specification** | Per-agent type | Extends/overrides tool policy |
| **Employment Specification** | Per-deployment | **Final override** |

Employment policies always take precedence.

---

## Agent Registry (Special Case)

The Agent Registry is managed by **Cipher IAM**, not Hub Registry Services:

| Registry | Owner | Purpose |
|----------|-------|---------|
| **Agent Registry** | Cipher | Raw, Trained, Employed Agent identities |
| **AI Agent Registry** | Seer | AI Agent definitions and configurations |

Hub's role is to integrate with these registries for agent enrollment in Workbenches.

---

## Workbench Integration

Each Workbench can define:
- **Machine Access** — Which Machines are accessible from this workbench
- **Tool Access** — Which Tools (from those Machines or standalone) are available
- **Environment Binding** — Which Environments provide connection context

---

## Related Documentation

- [Hub Architecture](../../02-system-design/hub-architecture.md) — System context
- [Storage Architecture](../../07-data-architecture/storage-architecture.md) — Storage layers
- [Cipher IAM](../supporting-systems/cipher-iam.md) — Agent identity
- [Subscription Configuration Guide](../../10-guides/subscription-configuration-guide.md) — Setup guide

---

*TODO: Detailed design — registry schemas, versioning strategy, access control model*
