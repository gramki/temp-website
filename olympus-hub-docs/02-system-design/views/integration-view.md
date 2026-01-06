# Integration View

> **How Hub connects to external systems**

---

## Audience

- Enterprise Architects
- Integration Architects
- Solution Architects

---

## Overview

This view shows how Olympus Hub integrates with external systems — both as a consumer of external capabilities and as a provider of operational services. It covers the Machine abstraction, I/O patterns, and cross-workbench communication.

---

## Integration Patterns

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         INTEGRATION PATTERNS                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   INBOUND (Hub as Receiver)          OUTBOUND (Hub as Caller)                │
│   ─────────────────────────          ───────────────────────                 │
│                                                                              │
│   External systems send signals       Hub calls external systems             │
│   to Hub via I/O Gateways            via Machines and Tools                  │
│                                                                              │
│   ┌───────────────────────┐          ┌───────────────────────┐              │
│   │ HTTP Webhooks         │          │ Machine: Core Banking │              │
│   │ → Heracles Gateway    │          │   → get_transaction   │              │
│   └───────────────────────┘          │   → initiate_refund   │              │
│                                      └───────────────────────┘              │
│   ┌───────────────────────┐                                                 │
│   │ Kafka Events          │          ┌───────────────────────┐              │
│   │ → Atropos Gateway     │          │ Machine: Email        │              │
│   └───────────────────────┘          │   → send_notification │              │
│                                      └───────────────────────┘              │
│   ┌───────────────────────┐                                                 │
│   │ File Uploads          │          ┌───────────────────────┐              │
│   │ → Dia Gateway         │          │ Machine: CRM          │              │
│   └───────────────────────┘          │   → get_customer      │              │
│                                      │   → update_case       │              │
│                                      └───────────────────────┘              │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## The Machine Abstraction

External systems are modeled as **Machines** — sources of commands (tools) that agents can invoke.

### Machine Definition

```yaml
apiVersion: hub.olympus.io/v1
kind: MachineDefinition
metadata:
  name: core-banking-system
spec:
  display_name: "Core Banking System"
  version: "1.0.0"
  
  # Transport configuration
  transport:
    type: http
    base_url: "https://core.{{environment}}.acme.com/api"
    auth:
      type: oauth2
      token_url: "https://auth.acme.com/token"
  
  # Available commands
  commands:
    - name: get_transaction
      description: "Retrieve transaction details"
      input_schema: { /* JSON Schema */ }
      output_schema: { /* JSON Schema */ }
      
    - name: initiate_refund
      description: "Initiate a refund"
      input_schema: { /* JSON Schema */ }
      output_schema: { /* JSON Schema */ }
```

### Machine Instance (Per Environment)

```yaml
apiVersion: hub.olympus.io/v1
kind: MachineInstance
metadata:
  name: core-banking-prod
spec:
  definition_ref: core-banking-system
  workbench_ref: dispute-ops-prod
  
  # Environment-specific configuration
  endpoint: "https://core.prod.acme.com/api"
  credentials_ref: core-banking-prod-creds
```

---

## I/O Gateway Integration

### Inbound Signal Patterns

| Pattern | Gateway | Protocol | Use Case |
|---------|---------|----------|----------|
| **Webhook** | Heracles | HTTP POST | Real-time notifications |
| **Event Stream** | Atropos | Kafka | CDC, event-driven |
| **File Drop** | Dia | S3/SFTP | Batch uploads |
| **Scheduled** | Kale | Cron | Periodic jobs |
| **Exception** | Cronus | API | Business exceptions |

### Signal Provider Registration

```yaml
apiVersion: hub.olympus.io/v1
kind: SignalProviderSpec
metadata:
  name: core-banking-webhooks
spec:
  gateway: heracles
  
  inbound:
    path: "/signals/core-banking"
    methods: ["POST"]
    auth:
      type: bearer
      validate_with: cipher-iam
    signal_type_mapping:
      "transaction.completed": "txn-completed"
      "transaction.failed": "txn-failed"
      
  outbound:
    endpoint: "https://core.acme.com/hub-updates"
    method: "POST"
    auth:
      type: oauth2
```

---

## Cross-Workbench Integration

### Workbench as Machine

One workbench can expose its capabilities as a Machine to other workbenches:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CROSS-WORKBENCH INTEGRATION                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   Workbench A                              Workbench B                       │
│   (Payments)                               (Disputes)                        │
│                                                                              │
│   ┌─────────────────────┐                 ┌─────────────────────────────┐   │
│   │                     │                 │                              │   │
│   │ Exposes scenarios   │                 │ Consumes via Machine         │   │
│   │ as Machine          │◀────────────────│                              │   │
│   │                     │                 │ Machine: payments-workbench  │   │
│   │ • process_refund    │                 │   → process_refund           │   │
│   │ • verify_payment    │                 │   → verify_payment           │   │
│   │                     │                 │                              │   │
│   └─────────────────────┘                 └─────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Scenario as Tool

Scenarios can be exposed as callable tools for AI agents:

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioToolSpec
metadata:
  name: dispute-investigation-tool
spec:
  scenario_ref: standard-dispute
  
  tool_interface:
    name: investigate_dispute
    description: "Investigate a customer dispute"
    input_schema:
      type: object
      properties:
        transaction_id: { type: string }
        customer_id: { type: string }
        reason: { type: string }
```

---

## Enterprise System Integration

### Common Integration Points

| System Type | Integration Pattern | Hub Component |
|-------------|---------------------|---------------|
| **ERP** | API/Events | Machine + Atropos |
| **CRM** | API | Machine |
| **Core Banking** | API/Events | Machine + Atropos |
| **Email/SMS** | API | Machine (Notification) |
| **Document Management** | API/Files | Machine + Dia |
| **Identity Provider** | SAML/OIDC | Cipher IAM |

### Integration Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ENTERPRISE INTEGRATION ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                         ENTERPRISE SYSTEMS                                   │
│                                                                              │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐          │
│   │   ERP   │  │   CRM   │  │ Banking │  │  Email  │  │   DMS   │          │
│   └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘          │
│        │            │            │            │            │                │
│        └────────────┴─────┬──────┴────────────┴────────────┘                │
│                           │                                                  │
│                           ▼                                                  │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                      INTEGRATION LAYER                               │   │
│   │                                                                      │   │
│   │   Machine Definitions    Signal Providers    Credentials Vault       │   │
│   │   (Tool schemas)         (Webhook configs)   (Secure storage)        │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                           │                                                  │
│                           ▼                                                  │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                      OLYMPUS HUB                                     │   │
│   │                                                                      │   │
│   │   I/O Gateways    Signal Exchange    Workbenches    Automation       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Authentication Patterns

| Pattern | Use Case | Mechanism |
|---------|----------|-----------|
| **OAuth 2.0** | API access to external systems | Client credentials flow |
| **API Key** | Simple integrations | Secure header |
| **mTLS** | High-security integrations | Mutual TLS |
| **SPIFFE** | Service-to-service | Workload identity |

---

## Related Documentation

- [I/O Gateway](../implementation-concepts/io-gateway.md)
- [Workbench as Machine](../implementation-concepts/workbench-as-machine.md)
- [Scenario as Tool](../implementation-concepts/scenario-as-tool.md)
- [Signal Flow](../signal-flow.md)

