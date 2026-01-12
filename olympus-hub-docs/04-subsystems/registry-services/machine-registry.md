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
  
  # Signal Emission Configuration
  signal_emission:
    signals:
      - type: "account.created"
        push:
          protocols: [webhook, atropos_inbox]
          schemas:
            webhook:
              openapi_spec:
                type: object
                required: [account_id, customer_id, account_type]
                properties:
                  account_id:
                    type: string
                    description: "Unique account identifier"
                  customer_id:
                    type: string
                    description: "Customer identifier"
                  account_type:
                    type: string
                    enum: [checking, savings, loan]
                  timestamp:
                    type: string
                    format: date-time
            atropos_inbox:
              openapi_schema:
                type: object
                required: [id, source, specversion, type, data]
                properties:
                  id: { type: string }
                  source: { type: string }
                  specversion: { type: string, enum: ["1.0"] }
                  type: { type: string }
                  data: { type: object }
              cloudevents_compliant: true
              cloudevents_spec_version: "1.0"
        pull:
          protocols: [atropos_subscription]
          schemas:
            atropos_subscription:
              openapi_schema:
                type: object
                required: [id, source, specversion, type, data]
                properties:
                  id: { type: string }
                  source: { type: string }
                  specversion: { type: string, enum: ["1.0"] }
                  type: { type: string }
                  data: { type: object }
              cloudevents_compliant: true
      
      - type: "transaction.posted"
        push:
          protocols: [webhook, atropos_inbox]
          schemas:
            webhook:
              openapi_spec:
                type: object
                required: [transaction_id, account_id, amount]
                properties:
                  transaction_id: { type: string }
                  account_id: { type: string }
                  amount: { type: number }
                  currency: { type: string, default: "USD" }
                  timestamp: { type: string, format: date-time }
            atropos_inbox:
              openapi_schema:
                type: object
                required: [id, source, specversion, type, data]
                properties:
                  id: { type: string }
                  source: { type: string }
                  specversion: { type: string, enum: ["1.0"] }
                  type: { type: string }
                  data: { type: object }
              cloudevents_compliant: true
              cloudevents_spec_version: "1.0"
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
  
  # Signal Emission Configuration (concrete endpoints for this instance)
  signal_emission:
    push:
      webhook:
        endpoint: string          # Workbench-scoped Hub ingress endpoint
        auth:
          type: enum              # api_key | oauth2 | mtls
          credentials_ref: string # Vault path
      atropos_inbox:
        broker_endpoint: string   # Event bus broker endpoint
        topic: string             # Topic name
        auth:
          type: enum              # sasl_scram | oauth2 | mtls
          credentials_ref: string # Vault path
      sftp:
        server_endpoint: string    # Hub Dia SFTP server endpoint
        folder_path: string       # Target folder path
        auth:
          type: enum              # api_key | username_password
          credentials_ref: string # Vault path
        file_pattern: string      # Optional file naming pattern
    pull:
      atropos_subscription:
        machine_broker: string    # Machine-provided broker endpoint
        machine_topic: string     # Machine-provided topic name
        hub_topic: string         # Hub-hosted topic (auto-provisioned)
        auth:
          type: enum              # sasl_scram | oauth2 | mtls
          credentials_ref: string # Vault path
      kafka_connect:
        machine_broker: string    # Machine-provided Kafka broker endpoint
        machine_topic: string     # Machine-provided topic name
        hub_topic: string         # Hub-hosted topic (auto-provisioned)
        connect_config: object    # Kafka Connect connector configuration
        auth:
          type: enum              # sasl_scram | oauth2 | mtls
          credentials_ref: string # Vault path
      sftp:
        machine_sftp:
          endpoint: string        # Machine-provided SFTP server endpoint
          path: string            # Source path on Machine SFTP
          auth:
            type: enum            # username_password | api_key
            credentials_ref: string # Vault path
        hub_sftp:
          endpoint: string        # Hub Dia SFTP server endpoint
          path: string            # Target path on Hub Dia SFTP
          auth:
            type: enum            # api_key
            credentials_ref: string # Vault path
        polling:
          schedule: string         # Cron expression for polling schedule
          file_filters:
            - pattern: string     # File name pattern (glob)
              min_size: number    # Minimum file size in bytes
  
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
  
  # Signal Emission Configuration
  signal_emission:
    push:
      webhook:
        endpoint: "https://heracles.olympus.tech/api/workbenches/payment-ops/signals"
        auth:
          type: api_key
          credentials_ref: "vault://secrets/acme/core-banking/webhook-key"
      atropos_inbox:
        broker_endpoint: "kafka://kafka.olympus.tech:9092"
        topic: "acme-core-banking.events"
        auth:
          type: sasl_scram
          credentials_ref: "vault://secrets/acme/core-banking/kafka-auth"
    pull:
      atropos_subscription:
        machine_broker: "kafka://external-events.acme-bank.com:9092"
        machine_topic: "core-banking.events"
        hub_topic: "/hub/acme-bank/prod-subscription/payment-ops/atropos/acme-core-banking-events"
        auth:
          type: sasl_scram
          credentials_ref: "vault://secrets/acme/core-banking/external-kafka-auth"
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

## Signal Emission Configuration

Machines emit signals through **Signal Providers** (I/O Gateways), which serve as Hub ingress endpoints. Signal Providers normalize signals and forward them to Signal Exchange for trigger evaluation.

**Signal Flow:**
```
Machine → Signal Provider (Hub Ingress) → Signal Exchange → Trigger → Scenario/Application
```

### Push vs Pull Models

Machines can emit signals using two models:

1. **Push Model**: Machine actively sends signals to Hub ingress endpoints
   - **Webhook**: HTTP POST to Heracles gateway endpoint
   - **Atropos Inbox**: Publish events to Event Bus topic
   - **SFTP**: Upload files to Dia SFTP endpoint

2. **Pull Model**: Hub uses signal-pulling applications to retrieve signals from Machines
   - **Atropos Subscription**: Hub subscribes to Machine-provided Event Bus topic
   - **Kafka Connect**: Hub connects to Machine-provided Kafka via Kafka Connect
   - **SFTP**: Hub polls Machine SFTP and uploads to Hub Dia SFTP

### Hub Ingress Endpoints

Hub ingress endpoints are:
- **Scoped**: Subscription-scoped and per-workbench
- **Naming Pattern**: `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}`
- **Provisioning**: Provisioned by tenant admin or authorized developers as resources

### Schema Validation

Signal schema validation occurs at the Signal Provider during normalization:
- **Webhook (Heracles)**: Validates against OpenAPI specification for POST request body
- **Atropos Inbox**: Validates CloudEvents v1.0 compliance
- **SFTP (Dia)**: Validates file format specification

### Multi-Provider Support

Machines can emit signals through multiple providers simultaneously. Hub does not deduplicate signals from multiple providers—each signal is processed independently.

### Provider Selection

Provider selection is the Machine's choice and is outside Hub's scope. Machines are represented in Hub, not defined in Hub (often external systems).

For detailed configuration examples and protocol specifications, see:
- [Signal Providers](../signal-providers/README.md)
- [Machine Signal Emission Guide](../../10-guides/machine-signal-emission-guide.md)

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

