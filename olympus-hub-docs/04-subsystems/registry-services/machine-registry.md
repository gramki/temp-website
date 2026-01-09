# Machine Registry

> **Status:** 🔴 Stub — Placeholder for expansion

The Machine Registry catalogs **Machines (systems) in the environment**—the information systems that manage business entities and produce signals. The registry operates at two levels: **Machine Definitions** (abstract templates) and **Machines** (concrete instances).

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Catalog abstract machine definitions and concrete machine instances |
| **Contents** | Machine Definitions with Tool Protocols; Machines with endpoints and policies |
| **Scope** | System-provided definitions + Tenant-specific instances |
| **Integration** | Tool Registry, Environment Registry, I/O Gateways, Workbenches |

---

## Two-Level Model

The Machine Registry maintains two distinct entity types:

```
┌─────────────────────────────────────────────────────────────────┐
│                    MACHINE DEFINITION                            │
│                    (Abstract Template)                           │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  temenos-core-banking v2.1                               │    │
│  │                                                          │    │
│  │  Tool Protocols:                                         │    │
│  │  ├── get-account (OpenAPI spec)                         │    │
│  │  ├── get-transaction (OpenAPI spec)                     │    │
│  │  ├── post-payment (OpenAPI spec)                        │    │
│  │  └── account-events (AsyncAPI spec)                     │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ instantiated as
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       MACHINE                                    │
│                  (Concrete Instance)                             │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  acme-core-banking (instance of temenos-core-banking)    │    │
│  │                                                          │    │
│  │  Endpoint: https://core.acme-bank.com/api/v2             │    │
│  │  Auth: OAuth2 → vault://secrets/acme/core-banking        │    │
│  │  Variables: { region: "us-east", tenant: "acme" }        │    │
│  │                                                          │    │
│  │  Tools (concrete):                                       │    │
│  │  ├── acme-get-account (rate-limit: 100/sec)             │    │
│  │  ├── acme-get-transaction (rate-limit: 500/sec)         │    │
│  │  └── acme-post-payment (requires-approval: true)        │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Machine Definition (Abstract)

A **Machine Definition** is an abstract template describing a type of machine without concrete connection details.

### Machine Definition Schema

```yaml
machine_definition:
  # Identity
  id: string
  name: string                    # e.g., "temenos-core-banking"
  version: string                 # e.g., "2.1.0"
  
  # Description
  display_name: string
  description: string
  vendor: string                  # e.g., "Temenos"
  
  # Type
  type: enum  # internal | external | saas | gateway
  
  # Capabilities (what this machine type can do)
  capabilities:
    produces_signals: boolean
    accepts_commands: boolean
    provides_data: boolean
  
  # Tool Protocols (abstract tools this machine supports)
  tool_protocols:
    - id: string
      name: string                # e.g., "get-account"
      description: string
      protocol_type: enum         # openapi | asyncapi | grpc | graphql
      specification: object       # The actual spec (OpenAPI, AsyncAPI, etc.)
      variables:                  # Placeholders in the spec
        - name: string
          description: string
          required: boolean
          default: string
  
  # Signal Schemas (if produces_signals)
  signal_schemas:
    - type: enum  # event | exception | observation
      schema: object
  
  # Metadata
  status: enum  # active | deprecated | retired
  documentation_url: string
```

### Example: Temenos Core Banking Definition

```yaml
machine_definition:
  id: "temenos-core-banking"
  name: "temenos-core-banking"
  version: "2.1.0"
  display_name: "Temenos T24 Core Banking"
  vendor: "Temenos"
  type: external
  
  capabilities:
    produces_signals: true
    accepts_commands: true
    provides_data: true
  
  tool_protocols:
    - id: "get-account"
      name: "Get Account Details"
      protocol_type: openapi
      specification:
        openapi: "3.0.0"
        paths:
          /accounts/{accountId}:
            get:
              parameters:
                - name: accountId
                  in: path
              servers:
                - url: "{{base_url}}"
      variables:
        - name: base_url
          description: "Base URL for the API"
          required: true
    
    - id: "post-payment"
      name: "Initiate Payment"
      protocol_type: openapi
      specification: { ... }
```

---

## Machine (Concrete Instance)

A **Machine** is a concrete, data-plane usable instance of a Machine Definition with actual endpoints, policies, and variable bindings.

### Machine Schema

```yaml
machine:
  # Identity
  id: string
  name: string                    # e.g., "acme-core-banking"
  
  # Reference to Definition
  definition_id: string           # e.g., "temenos-core-banking"
  definition_version: string      # e.g., "2.1.0"
  
  # Environment
  environment_id: string          # Which Environment this machine is in
  
  # Connection (concrete endpoint details)
  connection:
    endpoint: string              # Actual URL
    protocol: string              # REST | SOAP | gRPC
    auth:
      type: enum                  # oauth2 | api_key | mtls | basic
      credentials_ref: string     # Vault path
  
  # Variable Bindings (replace placeholders in tool protocols)
  variables:
    base_url: string
    tenant_id: string
    region: string
    # ... other variables from definition
  
  # Access Policies (for this machine instance)
  access_policies:
    allowed_workbenches: array
    allowed_roles: array
    requires_approval: boolean
  
  # Tools (concrete tool instances)
  tools:
    - id: string                  # e.g., "acme-get-account"
      protocol_id: string         # Reference to tool_protocol in definition
      
      # Per-tool overrides
      variables: object           # Tool-specific variable overrides
      
      # Per-tool access policies
      access_policies:
        allowed_roles: array
        requires_approval: boolean
      
      # Flow control
      flow_control:
        rate_limit: number        # Requests per second
        burst_limit: number
        timeout_ms: number
        retry_policy: object
  
  # Metadata
  owner_team: string
  status: enum  # active | maintenance | deprecated
```

### Example: ACME Bank's Core Banking Instance

```yaml
machine:
  id: "acme-core-banking"
  name: "ACME Core Banking"
  definition_id: "temenos-core-banking"
  definition_version: "2.1.0"
  environment_id: "acme-core-banking-env"
  
  connection:
    endpoint: "https://core.acme-bank.com/api/v2"
    protocol: REST
    auth:
      type: oauth2
      credentials_ref: "vault://secrets/acme/core-banking/oauth"
  
  variables:
    base_url: "https://core.acme-bank.com/api/v2"
    tenant_id: "acme"
    region: "us-east-1"
  
  access_policies:
    allowed_workbenches: ["dispute-ops", "payment-ops"]
    allowed_roles: ["operator", "analyst"]
    requires_approval: false
  
  tools:
    - id: "acme-get-account"
      protocol_id: "get-account"
      access_policies:
        allowed_roles: ["operator", "analyst", "auditor"]
      flow_control:
        rate_limit: 100
        timeout_ms: 5000
    
    - id: "acme-post-payment"
      protocol_id: "post-payment"
      access_policies:
        requires_approval: true
        allowed_roles: ["operator"]
      flow_control:
        rate_limit: 10
        timeout_ms: 30000
```

---

## Definition vs Instance Comparison

| Aspect | Machine Definition | Machine (Instance) |
|--------|-------------------|-------------------|
| **Nature** | Abstract template | Concrete, usable |
| **Endpoints** | None (variables only) | Actual URLs |
| **Credentials** | None | Vault references |
| **Policies** | None | Access, flow control |
| **Tools** | Tool Protocols (specs) | Concrete Tools with overrides |
| **Scope** | System or Tenant | Tenant + Environment |
| **Versioned** | Yes (semantic) | References definition version |

---

## Tool Protocol to Tool Resolution

When a Workbench accesses a tool:

```
Workbench
    └── Machine (acme-core-banking)
            └── Tool (acme-get-account)
                    └── Tool Protocol (get-account from temenos-core-banking v2.1)
                            └── Specification with variables replaced
```

The final specification is computed by:
1. Start with Tool Protocol specification from Machine Definition
2. Apply Machine-level variable bindings
3. Apply Tool-level variable overrides
4. Apply Tool-level access policies and flow control

---

## Workbench Integration

Each Workbench defines:
- **Machines in Scope** — Which Machine instances are accessible
- **Tool Access** — Which Tools from those Machines are available
- **Signal Subscriptions** — Which Machine signals trigger scenarios

---

## Related Documentation

- [Registry Services Overview](./README.md)
- [Tool Registry](./tool-registry.md) — Complementary tool registration
- [Environment Registry](./environment-registry.md) — Connection contexts
- [I/O Gateways](../signal-providers/README.md) — Signal handling

---

*TODO: Detailed design — version compatibility, tool protocol validation, flow control implementation*

