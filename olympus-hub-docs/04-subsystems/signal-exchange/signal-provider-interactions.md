# Signal Provider Interactions

> **Status:** 🟡 Draft — Needs review

This document details how Signal Providers interact with the Signal Exchange subsystem.

---

## Overview

Signal Exchange is a **message-oriented system** (similar to Atropos and OMS*) that handles the flow of signals between Signal Providers and Hub Applications.

> *OMS (Olympus Message System) is an in-house broker-less message exchange framework similar to ZeroMQ.

---

## Normalized Signal Format

Signal Exchange uses a **single, normalized signal format** that all Signal Providers must align to, regardless of their transport protocol. I/O Gateways are responsible for transforming protocol-specific signals to this normalized format before sending to Signal Exchange.

### Normalized Signal DTO Structure

All signals sent to Signal Exchange must conform to this structure:

```json
{
  "signal_header": {
    "tenant_id": "acme-bank",              // Required: Tenant scope
    "subscription_id": "sub-prod-001",     // Required: Subscription scope
    "signal_id": "sig-12345",              // Required: Unique identifier for this signal
    "signal_type": "account_event",        // Required: Type of signal
    "timestamp": "2026-01-05T10:00:00Z",   // Required: Signal timestamp
    "correlation_id": "corr-67890",        // Optional: Correlation to existing request
    "idempotency_key": "idem-22222"        // Optional: Key for idempotent processing
  },
  "payload": {
    "content_type": "application/json",     // application/json | application/base64
    "data": {                               // Signal-specific payload data
      // Provider-defined payload structure
    }
  },
  "metadata": {                             // Optional: Additional metadata
    "source_system": "temenos-core",
    "source_event_id": "evt-99999",
    "trace_id": "trace-abc123"
  },
  "additional_fields": {                    // Optional: SP-specific additional fields
    // Signal Provider may add additional fields beyond the normalized structure
    // These are preserved but not processed by Signal Exchange
  }
}
```

### Alignment Requirements

- **Signal Providers must align to Signal Exchange's normalized DTO structure** — all required fields must be present and correctly formatted
- **Signal Providers may add additional data** — fields beyond the normalized structure are preserved but not processed by Signal Exchange
- **I/O Gateways handle transformation** — protocol-specific signals are transformed to normalized format by I/O Gateways before reaching Signal Exchange

---

## Signal Provider Registration

Signal Providers must register with Signal Exchange **per tenant subscription** before they can send or receive messages. Registration is a **formal document** that indicates:
- The Signal Provider can serve the specified tenant and subscription
- The service coordinates (endpoints, protocols) at which it will provide services for this subscription
- The attributes and fields the Signal Provider uses that map to Signal Exchange's normalized DTO
- Any additional fields the Signal Provider includes beyond the normalized structure
- The preferred interface (HTTP, Atropos, or OMS) for receiving updates from Signal Exchange

### Registration Payload

```json
{
  "registration": {
    "tenant_id": "acme-bank",              // Required: Tenant this registration serves
    "subscription_id": "sub-prod-001",     // Required: Subscription this registration serves
    "signal_provider": {
      "id": "sp-temenos-core-banking",
      "name": "Temenos Core Banking",
      "type": "io_gateway",                // io_gateway | signal_source
      "version": "2.1.0"
    },
    "service_coordinates": {
      "endpoint": "https://temenos.example.com/signals",
      "protocol": "https",
      "auth": {
        "type": "oauth2",
        "token_endpoint": "https://temenos.example.com/oauth/token"
      }
    }
  },
  
  "normalized_dto_mapping": {
    "description": "How this SP's attributes map to Signal Exchange's normalized DTO",
    "mappings": {
      "signal_header.tenant_id": "from: auth_context.tenant",
      "signal_header.subscription_id": "from: auth_context.subscription",
      "signal_header.signal_id": "from: event.id",
      "signal_header.signal_type": "from: event.type",
      "signal_header.timestamp": "from: event.timestamp",
      "payload.data": "from: event.payload"
    }
  },
  
  "additional_fields_schema": {
    "description": "Additional fields this SP includes beyond normalized DTO",
    "schema_type": "json_schema",
    "schema_version": "1.0",
    "schema": {
      "type": "object",
      "properties": {
        "protocol_metadata": {
          "type": "object",
          "description": "HTTP-specific metadata preserved for response routing"
        },
        "source_channel": {
          "type": "string",
          "description": "Original channel identifier (mobile-app, web-portal, etc.)"
        }
      }
    },
    "suggested_use": "These fields are preserved for use in response transformation back to protocol format"
  },
  
  "outgoing_message_schema": {
    "schema_type": "json_schema",
    "schema_version": "1.0",
    "schema": { /* JSON Schema for outgoing messages */ },
    "correlation": {
      "mode": "correlated",                // correlated | independent
      "correlation_field": "request_id"
    }
  },
  
  "acknowledgement": {
    "mode": "sync",                        // sync | async
    "timeout_ms": 5000,
    "retry_policy": {
      "max_attempts": 3,
      "backoff": "exponential"
    }
  },
  
  "update_delivery": {
    "interface": "http",                   // http | atropos | oms
    "configuration": {
      // For HTTP:
      "endpoint": "https://provider.example.com/updates",
      "method": "POST",
      "auth": {
        "type": "oauth2",
        "token_endpoint": "https://provider.example.com/oauth/token"
      }
      // For Atropos:
      // "topic": "sp-temenos-updates",
      // "subscription": "sp-temenos-sub"
      // For OMS:
      // "queue": "sp-temenos-queue",
      // "endpoint": "oms://provider.example.com/updates"
    }
  }
}
```

### Registration Components

| Component | Description |
|-----------|-------------|
| **registration** | Tenant/subscription scope, Signal Provider identity, and service coordinates |
| **normalized_dto_mapping** | How this SP's attributes map to Signal Exchange's normalized DTO fields |
| **additional_fields_schema** | Schema for additional fields beyond normalized DTO (preserved but not processed by SX) |
| **outgoing_message_schema** | Schema for messages Signal Exchange sends to this provider |
| **acknowledgement** | How Signal Exchange acknowledges receipt of incoming signals |
| **update_delivery** | Preferred interface (HTTP, Atropos, or OMS) and configuration for receiving Request updates from Signal Exchange |

> **Note:** Registration is **per tenant subscription**. A Signal Provider serving multiple tenants/subscriptions must register separately for each.

---

## Normalized Signal DTO Schema

This is the **standardized format** that Signal Exchange receives from all Signal Providers. I/O Gateways transform protocol-specific signals to this normalized format before sending to Signal Exchange.

> **Note:** All signals are scoped to a **Tenant** and **Subscription**. These are required in the signal header.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "NormalizedSignalDTO",
  "type": "object",
  "required": ["signal_header", "payload"],
  "properties": {
    "signal_header": {
      "type": "object",
      "required": ["tenant_id", "subscription_id", "signal_id", "signal_type", "timestamp"],
      "properties": {
        "tenant_id": {
          "type": "string",
          "description": "Tenant scope for this signal (required)"
        },
        "subscription_id": {
          "type": "string",
          "description": "Subscription scope for this signal (required)"
        },
        "signal_id": {
          "type": "string",
          "description": "Unique identifier for this signal (required)"
        },
        "signal_type": {
          "type": "string",
          "description": "Type of signal (e.g., 'account_event', 'file_available') (required)"
        },
        "timestamp": {
          "type": "string",
          "format": "date-time",
          "description": "Signal timestamp (required)"
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
      "required": ["content_type", "data"],
      "properties": {
        "content_type": {
          "type": "string",
          "enum": ["application/json", "application/base64"],
          "description": "Content type of payload data"
        },
        "data": {
          "description": "Signal-specific payload data (provider-defined structure)"
        }
      }
    },
    "metadata": {
      "type": "object",
      "properties": {
        "source_system": { "type": "string" },
        "source_event_id": { "type": "string" },
        "trace_id": { "type": "string" }
      },
      "description": "Optional metadata for tracing and debugging"
    },
    "additional_fields": {
      "type": "object",
      "description": "Optional additional fields beyond normalized structure. These are preserved but not processed by Signal Exchange. Signal Providers should document these in their registration's additional_fields_schema."
    }
  }
}
```

> **Key Points:**
> - Signal Providers **must align** to this normalized structure — all required fields must be present
> - Signal Providers **may add additional fields** beyond this structure — these are preserved but not processed by Signal Exchange
> - I/O Gateways are responsible for transforming protocol-specific signals to this normalized format
> - The `additional_fields` section allows SPs to include protocol-specific or provider-specific data that may be needed for response transformation

### Outgoing Message DTO Schema

Defines the structure of messages Signal Exchange sends to the Signal Provider (for I/O Gateways that receive responses).

> **Note:** All outgoing messages include **Tenant** and **Subscription** scope in the message header.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "OutgoingMessageDTO",
  "type": "object",
  "required": ["message_header", "request_context", "payload"],
  "properties": {
    "message_header": {
      "type": "object",
      "required": ["tenant_id", "subscription_id", "message_id", "message_type", "timestamp"],
      "properties": {
        "tenant_id": {
          "type": "string",
          "description": "Tenant scope for this message"
        },
        "subscription_id": {
          "type": "string",
          "description": "Subscription scope for this message"
        },
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

Signal Exchange acknowledges receipt of incoming signals. The acknowledgement mechanism depends on the registration configuration:

### Synchronous Acknowledgement

When `acknowledgement.mode: sync` is configured, Signal Exchange sends an immediate response over the same message channel (request-response pattern):

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

> **Note:** Even in a message-oriented system, synchronous acknowledgement uses a request-response pattern over the same channel. The Signal Provider sends a signal and waits for the acknowledgement response before proceeding.

### Asynchronous Acknowledgement

When `acknowledgement.mode: async` is configured, Signal Exchange sends acknowledgement via the configured `update_delivery` interface (HTTP, Atropos, or OMS). The Signal Provider does not wait for acknowledgement.

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
| **Update Delivery** | Uses the `update_delivery` interface configuration from registration (HTTP, Atropos, or OMS) |
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

> **Note:** The transformation from Normalized Signal DTO to internal Request handling is managed within Signal Exchange. The **Request Mutation DTO** described below is an **internal artifact** — it is NOT exchanged between Signal Provider and Signal Exchange. Signal Providers receive Request updates via the **Outgoing Message DTO**.

### Signal Definition

A **Signal Definition** is a **filter** defined using the Normalized Signal DTO structure:

```yaml
signal_definition:
  id: "sig-def-account-overdraft"
  name: "Account Overdraft Signal"
  signal_provider_id: "sp-temenos-core-banking"
  
  # Filter on Normalized Signal DTO fields
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

A **Trigger** is a **code/low-code artifact** that translates the Normalized Signal DTO to a **Request Mutation DTO** (Request Initiation or Update message):

```yaml
trigger:
  id: "trg-overdraft-dispute"
  name: "Overdraft Dispute Trigger"
  signal_definition_id: "sig-def-account-overdraft"
  
  action: create_or_update              # create_new | update_existing | create_or_update
  
  # Correlation key for finding existing Request
  correlation:
    key_expression: "payload.account_id"
    
  # Transformation from Normalized Signal DTO → Request Mutation DTO
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
1. Extracting data from the Normalized Signal DTO
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
| **Update Delivery** | HTTP, Atropos, or OMS (per SP preference) | Outgoing updates to registered observers (Signal Providers and observer modules) |
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
│       │ 1. Normalized Signal (Normalized Signal DTO)                         │
│       │    (I/O Gateways transform protocol-specific → normalized format)    │
│       ▼                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      SIGNAL EXCHANGE                                 │    │
│  │                                                                      │    │
│  │   2. Validate against Normalized Signal DTO Schema                   │    │
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


