# Signal Provider Interactions

> **Status:** 🟡 Draft — Needs review

This document details how Signal Providers interact with the Signal Exchange subsystem.

---

## Overview

Signal Exchange is a **message-oriented system** (similar to Atropos and OMS*) that handles the flow of signals between Signal Providers and Hub Applications.

> *OMS (Olympus Message System) is an in-house broker-less message exchange framework similar to ZeroMQ.

---

## Signal Provider Registration

Signal Providers must register with Signal Exchange before they can send or receive messages. Registration establishes the **contract** between the Signal Provider and Signal Exchange.

### Registration Payload

```json
{
  "signal_provider": {
    "id": "sp-temenos-core-banking",
    "name": "Temenos Core Banking",
    "type": "io_gateway",               // io_gateway | signal_source
    "version": "2.1.0"
  },
  
  "incoming_signal_schema": {
    "schema_type": "json_schema",       // json_schema | avro | protobuf
    "schema_version": "1.0",
    "schema": { /* JSON Schema for incoming signals */ }
  },
  
  "outgoing_message_schema": {
    "schema_type": "json_schema",
    "schema_version": "1.0",
    "schema": { /* JSON Schema for outgoing messages */ },
    "correlation": {
      "mode": "correlated",             // correlated | independent
      "correlation_field": "request_id"
    }
  },
  
  "acknowledgement": {
    "mode": "sync",                     // sync | async
    "timeout_ms": 5000,
    "retry_policy": {
      "max_attempts": 3,
      "backoff": "exponential"
    }
  },
  
  "notification": {
    "mechanism": "webhook",             // webhook | websocket | event_bus | poll
    "endpoint": "https://provider.example.com/callbacks",
    "auth": {
      "type": "oauth2",
      "token_endpoint": "..."
    }
  }
}
```

### Registration Components

| Component | Description |
|-----------|-------------|
| **signal_provider** | Provider identity and metadata |
| **incoming_signal_schema** | Schema for signals sent by this provider to Signal Exchange |
| **outgoing_message_schema** | Schema for messages Signal Exchange sends to this provider |
| **acknowledgement** | How Signal Exchange acknowledges receipt of incoming signals |
| **notification** | How Signal Exchange notifies this provider of Request updates |

---

## Schemas

### Incoming Signal DTO Schema

Defines the structure of signals that the Signal Provider sends to Signal Exchange:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "IncomingSignalDTO",
  "type": "object",
  "required": ["signal_header", "payload"],
  "properties": {
    "signal_header": {
      "type": "object",
      "required": ["signal_id", "signal_type", "timestamp"],
      "properties": {
        "signal_id": {
          "type": "string",
          "description": "Unique identifier for this signal"
        },
        "signal_type": {
          "type": "string",
          "description": "Type of signal (e.g., 'account_event', 'file_available')"
        },
        "timestamp": {
          "type": "string",
          "format": "date-time"
        },
        "correlation_id": {
          "type": "string",
          "description": "Optional correlation to existing request"
        },
        "idempotency_key": {
          "type": "string",
          "description": "Key for idempotent processing"
        }
      }
    },
    "payload": {
      "type": "object",
      "description": "Signal-specific payload (provider-defined)"
    },
    "metadata": {
      "type": "object",
      "properties": {
        "source_system": { "type": "string" },
        "source_event_id": { "type": "string" },
        "trace_id": { "type": "string" }
      }
    }
  }
}
```

### Outgoing Message DTO Schema

Defines the structure of messages Signal Exchange sends to the Signal Provider (for I/O Gateways that receive responses):

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "OutgoingMessageDTO",
  "type": "object",
  "required": ["message_header", "request_context", "payload"],
  "properties": {
    "message_header": {
      "type": "object",
      "required": ["message_id", "message_type", "timestamp"],
      "properties": {
        "message_id": {
          "type": "string",
          "description": "Unique identifier for this message"
        },
        "message_type": {
          "type": "string",
          "enum": ["RESPONSE", "UPDATE_NOTIFICATION"],
          "description": "Type of outgoing message"
        },
        "timestamp": {
          "type": "string",
          "format": "date-time"
        },
        "correlation_id": {
          "type": "string",
          "description": "Correlation to originating signal (if correlated)"
        }
      }
    },
    "request_context": {
      "type": "object",
      "required": ["request_id"],
      "properties": {
        "request_id": { "type": "string" },
        "workbench_id": { "type": "string" },
        "scenario_id": { "type": "string" },
        "request_status": {
          "type": "string",
          "enum": ["ACTIVE", "PENDING", "COMPLETED", "CANCELLED"]
        }
      },
      "description": "All outgoing messages are in context of a Request"
    },
    "request_update_envelope": {
      "type": "object",
      "description": "Standard request-update envelope data",
      "properties": {
        "update_type": { "type": "string" },
        "sequence": { "type": "integer" },
        "timestamp": { "type": "string", "format": "date-time" }
      }
    },
    "payload": {
      "type": "object",
      "description": "Response or notification payload (provider-defined)"
    }
  }
}
```

### Outgoing Message Correlation

| Mode | Description |
|------|-------------|
| **Correlated** | Outgoing message correlates to a specific incoming signal (e.g., synchronous request-response) |
| **Independent** | Outgoing message is an async notification not tied to a specific signal (e.g., Request status update) |

> **Key Principle:** All outgoing messages are in context of a **Request** and contain standard **request-update envelope data** as the schema supports.

### Outgoing Message DTO Carries Request Mutations

The **Outgoing Message DTO** is how Signal Providers receive **all Request mutations**:

| Mutation Type | Description | Example |
|---------------|-------------|---------|
| **Status Change** | Request status transitions (ACTIVE, PENDING, COMPLETED, CANCELLED) | Request moved to PENDING awaiting documents |
| **Task Lifecycle** | Task created, picked, acted upon, escalated | Task assigned to agent-123 |
| **Decision** | Decision records with evidence references | Dispute validity determined |
| **Thought** | Reasoning or rationale comments | Agent explains prioritization logic |
| **Memo** | Scoped notes for future reference | Customer preference noted |
| **Memory Update** | Subject/Org/Session memory updates | Customer preference stored |
| **Progress** | Progress indicators | 60% complete |
| **Milestone** | Significant checkpoints | Document verification complete |
| **Error** | Recoverable errors or warnings | Document unreadable |

These are delivered via the `request_update_envelope` and `payload` fields in the Outgoing Message DTO.

---

## Signal Acknowledgement

Signal Exchange acknowledges receipt of incoming signals:

```json
{
  "acknowledgement": {
    "signal_id": "sig-12345",
    "status": "ACCEPTED",               // ACCEPTED | REJECTED | DUPLICATE
    "timestamp": "2026-01-05T10:00:00Z",
    "request_id": "req-67890",          // If signal created/updated a request
    "correlation_id": "corr-11111",
    "rejection_reason": null            // Populated if REJECTED
  }
}
```

| Status | Description |
|--------|-------------|
| **ACCEPTED** | Signal accepted for processing |
| **REJECTED** | Signal rejected (validation failure, policy violation) |
| **DUPLICATE** | Signal was already processed (idempotency check) |

---

## Automatic Observer Registration

Signal Providers that **initiate a Request** are automatically registered as **observers** of that Request:

| Aspect | Description |
|--------|-------------|
| **Automatic Registration** | No explicit subscription required |
| **Scope** | Observer of the specific Request they initiated |
| **Notification Mechanism** | Uses the `notification` configuration from registration |
| **Lifecycle** | Observation ends when Request reaches terminal state |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AUTOMATIC OBSERVER REGISTRATION                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Signal Provider (Heracles)                                                  │
│       │                                                                      │
│       │ 1. Sends Signal                                                      │
│       ▼                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      SIGNAL EXCHANGE                                 │    │
│  │                                                                      │    │
│  │   2. Creates Request (req-12345)                                    │    │
│  │   3. Auto-registers Heracles as Observer of req-12345               │    │
│  │                                                                      │    │
│  └───────────────────────────────────┬─────────────────────────────────┘    │
│                                      │                                       │
│       ┌──────────────────────────────┼──────────────────────────────────┐   │
│       │                              │                                   │   │
│       │                              ▼                                   │   │
│       │  ┌─────────────────────────────────────────────────────────┐    │   │
│       │  │              OBSERVER REGISTRY                          │    │   │
│       │  │                                                          │    │   │
│       │  │  Request: req-12345                                     │    │   │
│       │  │  Observers:                                             │    │   │
│       │  │    - Heracles (originating signal provider) ◀──────────┼────┘   │
│       │  │    - MS Teams Module (if configured)                    │        │
│       │  │    - Neutrino (if configured)                          │        │   │
│       │  │                                                          │        │
│       │  └─────────────────────────────────────────────────────────┘        │
│       │                                                                      │
│       │  4. On any Request mutation, Signal Exchange notifies observers    │
│       │                                                                      │
│       └──────────────────────────────────────────────────────────────────────┘
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Signal Definitions and Triggers

> **Note:** The transformation from Incoming Signal DTO to internal Request handling is managed within Signal Exchange. The **Request Mutation DTO** described below is an **internal artifact** — it is NOT exchanged between Signal Provider and Signal Exchange. Signal Providers receive Request updates via the **Outgoing Message DTO**.

### Signal Definition

A **Signal Definition** is a **filter** defined using the Signal Provider's Incoming Signal DTO:

```yaml
signal_definition:
  id: "sig-def-account-overdraft"
  name: "Account Overdraft Signal"
  signal_provider_id: "sp-temenos-core-banking"
  
  # Filter on Incoming Signal DTO fields
  filter:
    signal_type: "account_event"
    payload:
      event_type: "OVERDRAFT"
      severity:
        $in: ["HIGH", "CRITICAL"]
      amount:
        $gt: 1000
```

### Trigger Definition

A **Trigger** is a **code/low-code artifact** that translates the Incoming Signal DTO to a **Request Mutation DTO** (Request Initiation or Update message):

```yaml
trigger:
  id: "trg-overdraft-dispute"
  name: "Overdraft Dispute Trigger"
  signal_definition_id: "sig-def-account-overdraft"
  
  action: create_or_update              # create_new | update_existing | create_or_update
  
  # Correlation key for finding existing Request
  correlation:
    key_expression: "payload.account_id"
    
  # Transformation from Incoming Signal DTO → Request Mutation DTO
  transformation:
    type: low_code                      # low_code | code
    
    # For low_code transformations
    mapping:
      request_type: "BusinessRequest"
      scenario_id: "overdraft-resolution"
      
      payload_mapping:
        account_id: "$.payload.account_id"
        overdraft_amount: "$.payload.amount"
        overdraft_date: "$.signal_header.timestamp"
        severity: "$.payload.severity"
        
    # For code transformations
    # code_ref: "trigger-handlers/overdraft-handler"
```

---

## Supported Payload Types

Signal Exchange only supports **two payload types**:

| Type | Description | Use Case |
|------|-------------|----------|
| **JSON** | Structured JSON payload | Default for all structured data |
| **Base64** | Base64-encoded binary data | Files, images, encrypted content |

The Trigger is responsible for:
1. Extracting data from the Incoming Signal DTO
2. Transforming it to the expected format
3. Packing it into the Request Mutation DTO

---

## Request Mutation DTO (Internal)

> **Scope:** The Request Mutation DTO is an **internal artifact** within Signal Exchange. It flows from **Trigger Evaluator → Request Factory**. It is NOT exchanged with Signal Providers.

The **Request Mutation DTO** is the standard internal message format that Triggers produce. This is used for both Request Initiation and Request Updates.

### Request Initiation DTO

```json
{
  "mutation_type": "INITIATION",
  
  "signal_context": {
    "signal_id": "sig-12345",
    "signal_provider_id": "sp-temenos-core-banking",
    "trigger_id": "trg-overdraft-dispute",
    "received_at": "2026-01-05T10:00:00Z"
  },
  
  "request": {
    "request_type": "BusinessRequest",
    "workbench_id": "dispute-ops",
    "scenario_id": "overdraft-resolution",
    "priority": "high",
    "subject": {
      "type": "customer",
      "id": "cust-67890"
    }
  },
  
  "correlation": {
    "correlation_id": "corr-11111",
    "idempotency_key": "idem-22222"
  },
  
  "payload": {
    "content_type": "application/json",  // application/json | application/base64
    "data": {
      "account_id": "acc-99999",
      "overdraft_amount": 1500.00,
      "overdraft_date": "2026-01-05",
      "severity": "HIGH"
    }
  }
}
```

### Request Update DTO

```json
{
  "mutation_type": "UPDATE",
  
  "signal_context": {
    "signal_id": "sig-23456",
    "signal_provider_id": "sp-temenos-core-banking",
    "trigger_id": "trg-overdraft-update",
    "received_at": "2026-01-05T14:00:00Z"
  },
  
  "target_request": {
    "request_id": "req-12345",
    "correlation_id": "corr-11111"
  },
  
  "update": {
    "update_reason": "SIGNAL_UPDATE",
    "update_source": "temenos-core-banking"
  },
  
  "payload": {
    "content_type": "application/json",
    "data": {
      "repayment_received": true,
      "repayment_amount": 500.00,
      "repayment_date": "2026-01-05"
    }
  }
}
```

---

## Interface Summary

### Signal Exchange Interfaces

| Interface | Protocol | Use Case |
|-----------|----------|----------|
| **Signal Intake** | Message (Atropos/OMS) | Incoming signals from Signal Providers |
| **Observer Notification** | Webhook/WebSocket/Event | Outgoing updates to registered observers |
| **Sync Response** | Message (Atropos/OMS) | Immediate response for bidirectional gateways |

### Request Lifecycle Module Interface

Signal Providers can also contact the **Request Lifecycle Module** over **HTTP** for:

| Use Case | HTTP Method | Endpoint |
|----------|-------------|----------|
| **Request Status** | GET | `/requests/{request_id}` |
| **Request History** | GET | `/requests/{request_id}/history` |
| **Request Search** | POST | `/requests/search` |
| **Cancel Request** | POST | `/requests/{request_id}/cancel` |

> **Note:** The HTTP interface is for **lifecycle and enquiry** use cases. For interactions that **create or update** Hub Requests, Signal Providers must use the **Signal Exchange** message interface.

---

## Message Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SIGNAL PROVIDER → SIGNAL EXCHANGE FLOW                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  SIGNAL PROVIDER                                                             │
│       │                                                                      │
│       │ 1. Incoming Signal (Incoming Signal DTO)                            │
│       ▼                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      SIGNAL EXCHANGE                                 │    │
│  │                                                                      │    │
│  │   2. Validate against registered Incoming Signal Schema             │    │
│  │   3. Send Acknowledgement to Signal Provider                        │    │
│  │   4. Match against Signal Definitions (filter)                       │    │
│  │   5. Execute Trigger (transformation)                                │    │
│  │   6. Produce Request Mutation DTO                                    │    │
│  │                                                                      │    │
│  │   ┌─────────────────────────────────────────────────────────────┐   │    │
│  │   │               REQUEST FACTORY                                │   │    │
│  │   │   7. Create new Request OR Update existing Request          │   │    │
│  │   │   8. Register originating Signal Provider as Observer       │   │    │
│  │   └───────────────────────────────────┬─────────────────────────┘   │    │
│  │                                       │                              │    │
│  │   ┌───────────────────────────────────┼─────────────────────────┐   │    │
│  │   │            APPLICATION ROUTER     │                          │   │    │
│  │   │   9. Route to Hub Application     │                          │   │    │
│  │   └───────────────────────────────────┼─────────────────────────┘   │    │
│  │                                       │                              │    │
│  └───────────────────────────────────────┼──────────────────────────────┘    │
│                                          │                                   │
│                                          ▼                                   │
│                               HUB APPLICATION                                │
│                                          │                                   │
│                                          │ 10. Response                      │
│                                          ▼                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      SIGNAL EXCHANGE                                 │    │
│  │                                                                      │    │
│  │   11. Update Request status                                         │    │
│  │   12. Notify registered Observers (Outgoing Message DTO)            │    │
│  │   13. For I/O Gateways: Transform and send response                 │    │
│  │                                                                      │    │
│  └───────────────────────────────────────┬──────────────────────────────┘    │
│                                          │                                   │
│                                          ▼                                   │
│                            SIGNAL PROVIDER (Observer)                        │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Related Documentation

- [Signal Exchange Overview](./README.md)
- [Message Envelope](./message-envelope.md) — Signal Exchange ↔ Hub Application DTOs
- [Trigger Evaluator](./trigger-evaluator.md)
- [Request Factory](./request-factory.md)
- [Observer Notifications](./observer-notifications.md)
- [Signal Providers](../signal-providers/README.md)

---

*TODO: Detailed design — schema registry integration, transformation DSL, error handling strategies*


