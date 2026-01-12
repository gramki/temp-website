# Machines Produce Signals Through Signal Providers

> **Status:** 🟡 Draft — Work in progress  
> **Purpose:** Document how Machines emit signals through various Signal Providers (I/O Gateways)  
> **Target:** Machine Registry documentation enhancement

---

## Problem Statement

The current Machine Registry documentation indicates that Machines can produce signals (`capabilities.produces_signals: true`) and defines signal schemas, but it does **not** explain:

1. **How** Machines emit signals (what mechanism/protocol)
2. **Which** Signal Providers (I/O Gateways) Machines can use
3. **How** Machines are configured to emit through specific Signal Providers
4. **The flow** from Machine → Signal Provider → Signal Exchange

This creates a gap: developers understand Machines *can* produce signals, but not *how* to configure or use this capability.

---

## Core Concept

**Machines produce Signals** that are meant to be **perceived by Hub Scenarios/Applications** through Signal Providers.

Signal Providers are specialized Machines in the Hub Environment that:
- Accept signals from Domain Machines via protocol-specific interfaces (**Hub ingress**)
- Normalize signals to Signal Exchange format
- Forward signals to Signal Exchange for trigger evaluation

**Signal Flow:**
```
Domain Machine → Signal Provider (Hub Ingress) → Signal Exchange → Trigger → Scenario/Application
```

**Important Distinctions:**
- **Signal Emission (Machine → Hub)**: This document covers how Machines send signals into Hub
- **Signal Pulling (Hub → Machine)**: Hub can pull signals from Machines using signal-pulling applications (native Hub applications)
- **Sensory Tools**: Machines may also *receive* signals - this is covered in Tools documentation, not here

---

## Available Signal Providers

Machines can emit signals through the following Signal Providers:

| Signal Provider | Signal Type | Protocol | Use Case | Machine Interface |
|----------------|-------------|----------|----------|-------------------|
| **Atropos** | Event | Pub-Sub Event Bus | State changes, domain events | Publish to Event Bus Topic |
| **Heracles** | HTTP-Request | HTTP/REST/MCP | API calls, webhooks | HTTP POST/GET to Gateway |
| **Dia** | Batch-Request | SFTP/HTTP/WebDAV | File uploads, batch data | File upload to Gateway |
| **Cronus** | Exception, Observation | Publisher API | Business anomalies | API call to Publisher endpoint |
| **Kale** | Time-Signal | Scheduler | Scheduled triggers | (Managed by Kale, not direct) |

> **Note:** Kale is time-based and doesn't receive signals from Machines directly. Machines can trigger scheduled events through other providers.

---

## Signal Emission Patterns

### Pattern 1: Event-Based (Atropos)

**Flow:**
```
Domain Machine → Publish Event → Event Bus Topic → Atropos → Signal Exchange
```

**Machine Configuration:**
- Machine publishes events to Event Bus (Kafka, RabbitMQ, AWS EventBridge)
- Atropos subscribes to topics and consumes events
- Machine doesn't directly call Atropos; it publishes to the underlying event bus

**Example:**
```yaml
machine:
  id: "payment-switch"
  capabilities:
    produces_signals: true
  signal_config:
    provider: atropos
    event_bus:
      type: kafka
      topic: "payment.events"
      events:
        - "payment.authorized"
        - "payment.completed"
        - "payment.failed"
```

### Pattern 2: HTTP-Based (Heracles)

**Flow:**
```
Domain Machine → HTTP POST → Heracles → Signal Exchange
```

**Machine Configuration:**
- Machine makes HTTP calls to Heracles gateway endpoint
- Heracles receives HTTP request, normalizes to signal format
- Can be synchronous (request-response) or asynchronous (fire-and-forget)

**Example:**
```yaml
machine:
  id: "customer-portal"
  capabilities:
    produces_signals: true
  signal_config:
    provider: heracles
    endpoint: "https://gateway.olympus.tech/api/signals"
    method: POST
    auth:
      type: api_key
      credentials_ref: "vault://secrets/customer-portal/api-key"
    signals:
      - type: "dispute.filed"
        path: "/api/v1/disputes"
      - type: "account.inquiry"
        path: "/api/v1/accounts/{account_id}"
```

### Pattern 3: File-Based (Dia)

**Flow:**
```
Domain Machine → Upload File → Dia → Signal Exchange
```

**Machine Configuration:**
- Machine uploads files via SFTP, HTTP, or WebDAV
- Dia detects file arrival, processes file, emits signal
- Typically used for batch processing scenarios

**Example:**
```yaml
machine:
  id: "settlement-system"
  capabilities:
    produces_signals: true
  signal_config:
    provider: dia
    protocol: sftp
    endpoint: "sftp://dia.olympus.tech/inbound/settlements"
    file_pattern: "settlement_*.csv"
    signal_type: "settlement.file.arrived"
```

### Pattern 4: Exception-Based (Cronus)

**Flow:**
```
Domain Machine → API Call → Cronus → Signal Exchange
```

**Machine Configuration:**
- Machine calls Cronus Publisher API when business exceptions occur
- Cronus normalizes exception/observation to signal format
- Used for business-level anomalies, not system errors

**Example:**
```yaml
machine:
  id: "fraud-detection"
  capabilities:
    produces_signals: true
  signal_config:
    provider: cronus
    endpoint: "https://cronus.olympus.tech/api/v1/exceptions"
    signal_types:
      - type: "exception"
        category: "fraud.alert"
      - type: "observation"
        category: "risk.assessment"
```

---

## Machine Registry Schema Enhancement

### Proposed Addition to Machine Definition

```yaml
machine_definition:
  # ... existing fields ...
  
  capabilities:
    produces_signals: boolean
  
  # NEW: Signal Emission Configuration
  signal_emission:
    # Which Signal Providers this machine type supports
    supported_providers:
      - atropos
      - heracles
      - dia
      - cronus
    
    # Default provider (if machine doesn't specify)
    default_provider: atropos
    
    # Signal schemas per provider (if different)
    provider_schemas:
      atropos:
        - type: event
          schema: { ... }
      heracles:
        - type: http_request
          schema: { ... }
```

### Proposed Addition to Machine Instance

```yaml
machine:
  # ... existing fields ...
  
  # Signal emission configuration (concrete)
  signal_emission:
    # Active provider for this instance
    provider: atropos  # atropos | heracles | dia | cronus
    
    # Provider-specific configuration
    config:
      # For Atropos
      event_bus:
        type: kafka
        topic: "payment.events"
        connection_ref: "vault://secrets/kafka-connection"
      
      # For Heracles
      # endpoint: "https://gateway.olympus.tech/api/signals"
      # auth: { ... }
      
      # For Dia
      # protocol: sftp
      # endpoint: "sftp://..."
      
      # For Cronus
      # endpoint: "https://cronus.olympus.tech/api/v1/exceptions"
    
    # Signal types this machine emits
    signal_types:
      - "payment.authorized"
      - "payment.completed"
      - "payment.failed"
```

---

## Integration Flow

### Complete Flow: Machine Emits Signal

```
┌─────────────────────────────────────────────────────────────────┐
│                    DOMAIN MACHINE                               │
│                   (e.g., Payment Switch)                        │
│                                                                  │
│  1. Business event occurs (payment authorized)                 │
│  2. Machine emits signal via configured provider                │
│     └─→ Provider: Atropos                                       │
│     └─→ Action: Publish to Kafka topic "payment.events"          │
└────────────────────────┬────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              SIGNAL PROVIDER (I/O Gateway)                      │
│                        ATROPOS                                   │
│                                                                  │
│  1. Consumes event from Event Bus                                │
│  2. Normalizes to Signal Exchange DTO format                     │
│  3. Forwards to Signal Exchange                                   │
└────────────────────────┬────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    SIGNAL EXCHANGE                               │
│                                                                  │
│  1. Receives normalized signal                                   │
│  2. Evaluates triggers                                           │
│  3. Creates/updates Request                                     │
│  4. Routes to Hub Application                                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Configuration Examples

### Example 1: Core Banking System (Atropos)

```yaml
machine:
  id: "acme-core-banking"
  definition_id: "temenos-core-banking"
  
  capabilities:
    produces_signals: true
  
  signal_emission:
    provider: atropos
    config:
      event_bus:
        type: kafka
        brokers: ["kafka.acme-bank.com:9092"]
        topic: "core-banking.events"
        auth:
          type: sasl_scram
          credentials_ref: "vault://secrets/kafka-sasl"
    
    signal_types:
      - "account.created"
      - "account.updated"
      - "transaction.posted"
      - "loan.approved"
```

### Example 2: Customer Portal (Heracles)

```yaml
machine:
  id: "customer-portal-api"
  definition_id: "custom-portal"
  
  capabilities:
    produces_signals: true
  
  signal_emission:
    provider: heracles
    config:
      endpoint: "https://gateway.olympus.tech/api/signals"
      method: POST
      auth:
        type: api_key
        credentials_ref: "vault://secrets/customer-portal/gateway-key"
      headers:
        X-Source: "customer-portal"
        X-Version: "2.1.0"
    
    signal_types:
      - "dispute.filed"
      - "account.inquiry"
      - "service.request"
```

### Example 3: Settlement System (Dia)

```yaml
machine:
  id: "settlement-processor"
  definition_id: "settlement-system"
  
  capabilities:
    produces_signals: true
  
  signal_emission:
    provider: dia
    config:
      protocol: sftp
      endpoint: "sftp://dia.olympus.tech/inbound/settlements"
      credentials_ref: "vault://secrets/settlement-sftp"
      file_pattern: "settlement_*.csv"
      signal_type: "settlement.file.arrived"
```

---

## Resolved Design Decisions

### Multi-Provider Support

**Decision:** Machines can emit signals through multiple providers simultaneously. Hub does not deduplicate or acknowledge signals from multiple providers as the same or redundant. Each signal is processed independently.

**Example:** A Machine can send critical events via both Atropos (for real-time processing) and Heracles (for audit trail). Hub will process both signals separately.

### Provider Selection

**Decision:** Provider selection is the Machine's choice and is outside Hub's scope. Machines are represented in Hub, not defined in Hub (often external systems). The Machine decides which provider(s) to use based on its own logic and requirements.

### Signal Schema Validation

**Decision:** Signal schema validation occurs at the Signal Provider during normalization. Each provider validates according to its protocol requirements:
- **Webhook (Heracles)**: Validates against OpenAPI specification for POST request body
- **Atropos Inbox**: Validates CloudEvents v1.0 compliance
- **SFTP (Dia)**: Validates file format specification

### Hub Ingress Endpoints

**Decision:** Hub ingress endpoints are:
- **Scoped**: Subscription-scoped and per-workbench
- **Naming Pattern**: `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}`
- **Provisioning**: Provisioned by tenant admin or authorized developers as resources when required

### Authentication

**Decision:** Per-provider authentication mechanisms are used. Each Signal Provider has its own authentication requirements and mechanisms.

### Error Handling

**Decision:** Sound defaults for error handling will be implemented. Specific error handling strategies will be defined per provider and pull mechanism.

---

## Documentation Updates Needed

### 1. Machine Registry (`machine-registry.md`)

**Add Section:** "Signal Emission Configuration"
- Explain that Machines emit signals through Signal Providers
- Document `signal_emission` configuration schema
- Provide examples for each provider type
- Link to Signal Providers documentation

### 2. Signal Providers (`signal-providers/README.md`)

**Enhance Section:** "Architectural Role"
- Add explicit statement: "Machines emit signals through Signal Providers"
- Show Machine → Signal Provider flow diagram
- Clarify that Signal Providers are Machines themselves

### 3. Machine Definition Schema

**Update:** Add `signal_emission` fields to:
- Machine Definition schema
- Machine Instance schema
- Example configurations

### 4. Integration Guide

**Create:** "Configuring Machine Signal Emission" guide
- Step-by-step for each provider
- Common patterns
- Troubleshooting

---

## Related Documentation

- [Machine Registry](../04-subsystems/registry-services/machine-registry.md)
- [Signal Providers](../04-subsystems/signal-providers/README.md)
- [Atropos Event Bus](../04-subsystems/signal-providers/atropos-event-bus.md)
- [Heracles API Gateway](../04-subsystems/signal-providers/heracles-api-gateway.md)
- [Dia File Gateway](../04-subsystems/signal-providers/dia-file-gateway.md)
- [Cronus Business Exceptions](../04-subsystems/signal-providers/cronus-business-exceptions.md)
- [Signal Exchange](../04-subsystems/signal-exchange/README.md)

---

---

## Signal Provider Requirements & Hub Ingress Endpoints

> **Status:** 🟡 To Be Elaborated  
> **Purpose:** Capture requirements for signal emission configuration

### Core Concept: Signal Flow Direction

**Machine produces Signals** that are meant to be **perceived by Hub Scenarios/Applications** through Signal Providers.

```
Machine → Signal Provider (Hub Ingress) → Signal Exchange → Trigger → Scenario/Application
```

**Important Distinctions:**
- **Signal Emission (Machine → Hub)**: Machine sends signals into Hub (this document)
- **Signal Pulling (Hub → Machine)**: Hub pulls signals from Machine using signal-pulling applications
- **Sensory Tools (Machine receives)**: Machine's ability to receive signals (covered in Tools documentation, not here)

### Signal Provider Required

For each Machine that produces signals, we need to specify:
- **Which Signal Provider** the Machine will use to send signals into Hub
- **Signal Provider selection criteria** (when multiple providers are available)
- **Provider-specific configuration** requirements

### Hub Ingress Endpoints (Signal Provider Entry Points)

Each Signal Provider exposes **Hub ingress endpoints** where signals enter the Hub platform. These are the entry points into Hub, not into Machines.

| Signal Provider | Hub Ingress Endpoint Type | Endpoint Details | Status |
|----------------|---------------------------|------------------|--------|
| **Atropos** | Event Bus Topic | Topic name, broker endpoints | ⬜ To Document |
| **Heracles** | HTTP Endpoint | URL, path, method | ⬜ To Document |
| **Dia** | File Upload Endpoint | SFTP/HTTP/WebDAV endpoint | ⬜ To Document |
| **Cronus** | Publisher API Endpoint | API endpoint URL | ⬜ To Document |
| **Kale** | (N/A - time-based) | N/A | N/A |

**Questions to Resolve:**
- Are Hub ingress endpoints tenant-scoped or subscription-scoped?
- How are endpoints discovered/configured?
- What authentication is required at Hub ingress?
- Are endpoints per-workbench or shared?

### Signals Provided by Machine

For each Machine, we need to document:

1. **What signals** the Machine provides
   - Signal types (event names, categories)
   - Signal schemas (payload structure) - protocol-specific
   - Signal frequency/volume expectations

2. **Signal delivery capabilities per signal**
   - For each signal, specify: push and/or pull support
   - For each delivery method, specify: supported protocol(s)
   - For each protocol, provide: protocol-compliant signal schema

**Example Structure:**
```yaml
machine:
  id: "payment-switch"
  signal_emission:
    signals:
      - type: "payment.authorized"
        frequency: "high"  # thousands per hour
        
        # Push support
        push:
          protocols:
            - webhook
            - atropos_inbox
          schemas:
            webhook:
              # OpenAPI Spec POST Body with JSON Payload
              openapi_spec: { ... }
            atropos_inbox:
              # OpenAPI Schema in JSON format, CloudEvents compliant
              openapi_schema: { ... }
              cloudevents_compliant: true
        
        # Pull support (if applicable)
        pull:
          protocols:
            - rest_api
          schemas:
            rest_api:
              # Schema for REST API response
              schema: { ... }
      
      - type: "payment.completed"
        frequency: "high"
        push:
          protocols:
            - webhook
            - atropos_inbox
          schemas:
            webhook: { ... }
            atropos_inbox: { ... }
        pull:
          protocols: []  # No pull support
      
      - type: "payment.failed"
        frequency: "low"
        push:
          protocols:
            - webhook
          schemas:
            webhook: { ... }
        pull:
          protocols: []  # No pull support
```

---

## Push Protocols & Signal Schemas

> **Status:** 🟡 To Be Elaborated  
> **Purpose:** Document push protocols and their signal schema requirements

### Push Protocol Options

Machines can push signals to Hub using the following protocols:

| Protocol | Signal Provider | Description | Status |
|----------|----------------|-------------|--------|
| **Webhook** | Heracles | HTTP Ingress Endpoint | ✅ Defined |
| **Atropos Inbox** | Atropos | Event Bus Topic | ✅ Defined |
| **SFTP** | Dia | File Upload | ⬜ TBD |

### Protocol 1: Webhook (HTTP Ingress Endpoint)

**Signal Provider:** Heracles  
**Direction:** Machine → HTTP POST → Heracles (Hub Ingress)

**Configuration:**
- **Endpoint**: Configured when configuring the Machine Instance
- **Endpoint Scope**: Unique to the Workbench instance
- **Method**: POST
- **Protocol**: HTTP/HTTPS

**Signal Schema Requirements:**
- **Format**: OpenAPI Spec POST Body with JSON Payload
- **Schema Location**: Defined in Machine Definition or Machine Instance
- **Compliance**: Must match OpenAPI specification for POST request body

**Example Configuration:**
```yaml
machine:
  id: "payment-switch"
  signal_emission:
    signals:
      - type: "payment.authorized"
        push:
          protocols:
            - webhook
          schemas:
            webhook:
              # OpenAPI Spec for POST request body
              openapi_spec:
                type: object
                required:
                  - payment_id
                  - amount
                  - customer_id
                properties:
                  payment_id:
                    type: string
                    description: "Unique payment identifier"
                  amount:
                    type: number
                    description: "Payment amount"
                  customer_id:
                    type: string
                    description: "Customer identifier"
                  timestamp:
                    type: string
                    format: date-time
                    description: "Payment authorization timestamp"
                  currency:
                    type: string
                    default: "USD"
    
    # Webhook endpoint configured in Machine Instance
    webhook_config:
      endpoint: "https://heracles.olympus.tech/api/workbenches/{workbench_id}/signals"  # Configured per Workbench
      method: POST
      auth:
        type: api_key
        credentials_ref: "vault://secrets/payment-switch/webhook-key"
```

**Machine Instance Configuration:**
```yaml
machine_instance:
  id: "acme-payment-switch"
  machine_id: "payment-switch"
  workbench_id: "payment-operations"
  
  signal_emission:
    webhook_endpoint: "https://heracles.olympus.tech/api/workbenches/payment-operations/signals"
    # Endpoint is unique to this Workbench instance
```

### Protocol 2: Atropos Inbox (Event Bus)

**Signal Provider:** Atropos  
**Direction:** Machine → Publish Event → Atropos Topic → Signal Exchange

**Configuration:**
- **Broker Endpoint**: Provided in Machine Instance configuration
- **Topic Name**: Provided in Machine Instance configuration
- **Protocol**: Event Bus (Kafka, RabbitMQ, AWS EventBridge, etc.)

**Signal Schema Requirements:**
- **Format**: OpenAPI Schema in JSON format
- **Compliance**: Must be compliant with [CloudEvents](https://cloudevents.io/) format
- **Schema Location**: Defined in Machine Definition

**CloudEvents Compliance:**
- Signal must conform to CloudEvents v1.0 specification
- Required attributes: `id`, `source`, `specversion`, `type`
- Optional attributes: `datacontenttype`, `data`, `time`, etc.

**Example Configuration:**
```yaml
machine:
  id: "payment-switch"
  signal_emission:
    signals:
      - type: "payment.authorized"
        push:
          protocols:
            - atropos_inbox
          schemas:
            atropos_inbox:
              # OpenAPI Schema in JSON format
              openapi_schema:
                type: object
                required:
                  - id
                  - source
                  - specversion
                  - type
                  - data
                properties:
                  id:
                    type: string
                    description: "CloudEvents event ID"
                    example: "550e8400-e29b-41d4-a716-446655440000"
                  source:
                    type: string
                    description: "CloudEvents source URI"
                    example: "payment-switch.acme.com"
                  specversion:
                    type: string
                    enum: ["1.0"]
                    description: "CloudEvents specification version"
                  type:
                    type: string
                    description: "CloudEvents event type"
                    example: "com.acme.payment.authorized"
                  datacontenttype:
                    type: string
                    default: "application/json"
                    description: "Content type of data attribute"
                  time:
                    type: string
                    format: date-time
                    description: "CloudEvents timestamp"
                  data:
                    type: object
                    description: "Event payload (CloudEvents data)"
                    properties:
                      payment_id:
                        type: string
                      amount:
                        type: number
                      customer_id:
                        type: string
              cloudevents_compliant: true
              cloudevents_spec_version: "1.0"
    
    # Atropos configuration in Machine Instance
    atropos_config:
      broker_endpoint: "kafka://kafka.olympus.tech:9092"  # Configured per Machine Instance
      topic: "payment.events"  # Configured per Machine Instance
```

**Machine Instance Configuration:**
```yaml
machine_instance:
  id: "acme-payment-switch"
  machine_id: "payment-switch"
  workbench_id: "payment-operations"
  
  signal_emission:
    atropos:
      broker_endpoint: "kafka://kafka.olympus.tech:9092"
      topic: "payment.events"
      auth:
        type: sasl_scram
        credentials_ref: "vault://secrets/payment-switch/kafka-auth"
```

### Protocol 3: SFTP (Files)

**Signal Provider:** Dia  
**Direction:** Machine → Upload File → Dia SFTP Endpoint → Signal Exchange

**Configuration:**
- **SFTP Server Endpoint**: Hub Dia SFTP server endpoint (configured in Machine Instance)
- **Folder Path**: Target folder path on Hub Dia SFTP server (configured in Machine Instance)
- **File Format**: Format specification for expected files (defined in Machine Definition, references [File Format Specification](../../04-subsystems/signal-providers/dia/file-format-specification.md))

**Signal Schema Requirements:**
- **Format Specification**: Files must conform to the file format specification defined in Machine Definition
- **Format Specification Reference**: See [File Format Specification](../../04-subsystems/signal-providers/dia/file-format-specification.md) for complete schema definition
- **Supported Formats**: CSV, TSV, Fixed-Width
- **Schema Location**: Defined in Machine Definition as `file_format_spec`

**Example Configuration:**
```yaml
machine:
  id: "settlement-file-system"
  signal_emission:
    signals:
      - type: "settlement.file.ready"
        push:
          protocols:
            - sftp
          schemas:
            sftp:
              # File format specification
              file_format_spec:
                # Reference to file format specification
                # See: 04-subsystems/signal-providers/dia/file-format-specification.md
                name: "settlement-file-v1"
                format: "csv"
                encoding: "utf-8"
                dialect:
                  delimiter: ","
                  quote: '"'
                structure:
                  header:
                    rows: 1
                    validation:
                      required: true
                      fields:
                        - name: "file_type"
                          position: 0
                          type: "string"
                          constraints:
                            enum: ["SETTLEMENT"]
                        - name: "file_date"
                          position: 1
                          type: "date"
                          format: "%Y-%m-%d"
                        - name: "batch_id"
                          position: 2
                          type: "string"
                  body:
                    startRow: 2
                    schema:
                      fields:
                        - name: "transaction_id"
                          position: 0
                          type: "string"
                        - name: "amount"
                          position: 1
                          type: "decimal"
                        - name: "status"
                          position: 2
                          type: "string"
                  footer:
                    rows: 1
                    validation:
                      required: true
                      extract:
                        record_count:
                          from: "TOTAL,(?P<count>\\d+)"
                          type: "integer"
                integrity:
                  checks:
                    - type: "row_count"
                      min_rows: 3
                output:
                  format: "json"
                  perRow: true
                  includeMetadata: true

machine_instance:
  id: "acme-settlement-files"
  machine_id: "settlement-file-system"
  workbench_id: "settlement-operations"
  
  signal_emission:
    sftp:
      # Hub Dia SFTP server endpoint
      server_endpoint: "sftp://dia.olympus.tech:22"
      
      # Target folder path on Hub Dia SFTP server
      folder_path: "/inbound/settlements/{workbench_id}"  # Workbench-scoped path
      
      # Authentication for Hub Dia SFTP
      auth:
        type: api_key
        credentials_ref: "vault://secrets/settlement-files/dia-sftp-key"
      
      # File naming pattern (optional)
      file_pattern: "settlement_*.csv"
```

**Flow:**
1. Machine uploads file to Hub Dia SFTP server: `sftp://dia.olympus.tech:22`
2. Machine uploads to folder path: `/inbound/settlements/settlement-operations`
3. Hub Dia detects file arrival
4. Hub Dia parses file according to file format specification
5. Hub Dia emits signals to Signal Exchange (one signal per row, if `perRow: true`)
6. Signal Exchange processes as normal push signals

**File Format Specification:**
The file format specification follows the schema defined in [File Format Specification](../../04-subsystems/signal-providers/dia/file-format-specification.md), which supports:
- **Format Types**: CSV, TSV, Fixed-Width
- **Structure**: Header, Body, Footer sections
- **Validation**: Pattern matching, field validation, cross-validation
- **Integrity Checks**: File size, hash, row count, column count
- **Output**: JSON per-row format with metadata

---

## Signal Schema Compliance

### CloudEvents Format (for Atropos Inbox)

When using Atropos Inbox protocol, signals must comply with [CloudEvents v1.0 specification](https://cloudevents.io/).

**Required Attributes:**
- `id`: Unique identifier for the event
- `source`: URI identifying the event producer
- `specversion`: CloudEvents specification version (must be "1.0")
- `type`: Type of event (e.g., "com.acme.payment.authorized")

**Optional Attributes:**
- `datacontenttype`: Content type of the `data` attribute (default: "application/json")
- `dataschema`: URI of the schema that `data` adheres to
- `subject`: Subject of the event
- `time`: Timestamp when the event occurred
- `data`: Event payload (must conform to `datacontenttype`)

**Example CloudEvents-Compliant Signal:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "source": "payment-switch.acme.com",
  "specversion": "1.0",
  "type": "com.acme.payment.authorized",
  "datacontenttype": "application/json",
  "time": "2026-01-15T10:30:00Z",
  "data": {
    "payment_id": "pay_12345",
    "amount": 100.50,
    "customer_id": "cust_67890",
    "currency": "USD"
  }
}
```

### OpenAPI Specification (for Webhook)

When using Webhook protocol, signals must conform to OpenAPI specification for POST request body.

**Requirements:**
- JSON payload structure defined in OpenAPI schema
- Schema must be included in Machine Definition
- Request body validation against schema at Hub ingress (Heracles)

---

## Push vs Pull Model: Machine Signal Delivery to Hub

> **Status:** 🟡 To Be Elaborated  
> **Purpose:** Determine signal delivery model(s) for Machine → Hub flow

### Question: Push or Pull?

**How do Machines deliver signals into Hub?**

- **Option A: Machine Pushes to Hub Ingress (Push Model)**
  - Machine actively sends signals to Hub ingress endpoint (Signal Provider)
  - Machine controls when signals are sent
  - Signal Provider receives and processes immediately
  - Machine must know Hub ingress endpoint and authentication
  
- **Option B: Hub Pulls from Machine (Pull Model)**
  - Hub uses **signal-pulling applications** to retrieve signals from Machine
  - Hub controls polling frequency and timing
  - Machine exposes endpoint/interface for Hub to query
  - Machine doesn't need to know Hub details
  
- **Option C: Both (Hybrid)**
  - Machine can push critical/real-time signals to Hub ingress
  - Hub can pull batch/historical signals from Machine
  - Different signal types use different mechanisms

### If Pull Model: Machine Endpoints for Hub to Query

If Hub **pulls** signals from Machines using signal-pulling applications, we need to document:

1. **Machine endpoints/interfaces that Hub can query:**
   - **REST API**: Machine exposes REST endpoint for signal querying
   - **GraphQL**: Machine exposes GraphQL endpoint
   - **Event Bus**: Machine publishes to event bus, Hub subscribes
   - **Database Query**: Machine exposes database access (read-only)
   - **File Location**: Machine writes to file location, Hub polls
   - **Webhook Registration**: Machine accepts webhook registrations (reverse pull)
   - **gRPC**: Machine exposes gRPC service
   - **Message Queue**: Machine publishes to queue, Hub consumes

2. **Machine endpoint characteristics:**
   - What endpoint does Machine expose for Hub to query?
   - Authentication/authorization for Hub access
   - Rate limiting and throttling
   - Pagination for large result sets
   - Filtering capabilities (by time, type, etc.)

**Example Pull Configuration:**
```yaml
machine:
  id: "legacy-system"
  signal_emission:
    delivery_mechanism: pull  # Hub pulls from Machine
    
    # Machine endpoint that Hub will query
    machine_endpoint:
      type: rest_api
      url: "https://legacy-system.acme.com/api/v1/signals"
      method: GET
      auth:
        type: oauth2
        credentials_ref: "vault://secrets/hub-to-machine-oauth"
      
      query_parameters:
        - since: timestamp  # Get signals since this time
        - signal_type: string  # Filter by signal type
        - limit: integer  # Pagination limit
      
      # Hub will use signal-pulling application to query this endpoint
      # Hub controls polling frequency, not Machine
```

**Note:** The Machine endpoint above is what the Machine exposes. Hub uses a **signal-pulling application** (native Hub application) to query this endpoint and deliver signals to Signal Providers.

---

## Pull Mechanisms: Converting Pull to Push Semantics

> **Status:** 🟡 To Be Elaborated  
> **Purpose:** Document pull mechanisms that convert to push semantics via Hub-hosted topics/endpoints

### Core Concept: Pull-to-Push Conversion

All pull mechanisms follow a **pull-to-push conversion pattern**:
1. Hub pulls signals from Machine-provided endpoints/topics
2. Hub routes pulled signals to **Hub-hosted topics/endpoints**
3. Signals are then processed as push semantics (from Hub-hosted resources)
4. This ensures consistent signal processing regardless of original delivery method

**Flow Pattern:**
```
Machine (provides endpoint/topic) → Hub Pulls → Hub-Hosted Topic/Endpoint → Signal Provider → Signal Exchange
```

### Pull Mechanism 1: Listening/Subscribing to Atropos Topic

**Protocol:** Atropos Event Bus Subscription  
**Signal Provider:** Atropos  
**Direction:** Hub subscribes to Machine-provided topic → Hub-hosted topic → Signal Exchange

**Configuration:**
- **Machine-provided**: Broker endpoint and topic name (configured in Machine Instance)
- **Hub-hosted**: Hub creates/manages a topic for queuing pulled messages
- **Conversion**: All messages read from Machine topic are queued to Hub-hosted topic for dispatch

**Signal Schema:**
- **Same as Atropos Push event**: CloudEvents-compliant OpenAPI Schema
- **Format**: OpenAPI Schema in JSON format, compliant with CloudEvents v1.0

**Example Configuration:**
```yaml
machine:
  id: "external-payment-system"
  signal_emission:
    signals:
      - type: "payment.authorized"
        pull:
          protocols:
            - atropos_subscription
          schemas:
            atropos_subscription:
              # Same schema as Atropos Push
              openapi_schema:
                type: object
                required: ["id", "source", "specversion", "type", "data"]
                properties:
                  id: { type: string }
                  source: { type: string }
                  specversion: { type: string, enum: ["1.0"] }
                  type: { type: string }
                  data: { type: object }
              cloudevents_compliant: true

machine_instance:
  id: "acme-external-payment"
  machine_id: "external-payment-system"
  workbench_id: "payment-operations"
  
  signal_emission:
    pull:
      atropos_subscription:
        # Machine-provided endpoint and topic
        broker_endpoint: "kafka://external-payment.acme.com:9092"
        topic: "payment.events"
        auth:
          type: sasl_scram
          credentials_ref: "vault://secrets/external-payment/kafka-auth"
        
        # Hub-hosted topic (configured, dedicated to machine instance)
        # Hub will queue messages here for dispatch
        # Pattern: /hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}
        hub_topic: "/hub/acme-bank/prod-subscription/payment-operations/atropos/external-payment-events"
```

**Flow:**
1. Hub subscribes to Machine-provided topic: `payment.events` at `kafka://external-payment.acme.com:9092`
2. Hub reads messages from Machine topic
3. Hub queues messages to Hub-hosted topic: `hub.payment-operations.external-payment.events`
4. Hub-hosted topic dispatches to Signal Exchange (push semantics)
5. Signal Exchange processes as normal push signals

### Pull Mechanism 2: Kafka Connect Endpoint

**Protocol:** Kafka Connect Protocol  
**Signal Provider:** Atropos (via Kafka Connect)  
**Direction:** Hub connects to Machine-provided Kafka → Hub-hosted topic → Signal Exchange

**Configuration:**
- **Machine-provided**: Broker endpoint and topic name (configured in Machine Instance)
- **Protocol**: Kafka Connect protocol
- **Hub-hosted**: Hub creates/manages a topic for queuing pulled messages
- **Conversion**: Messages converted to push semantics using Hub-hosted topic

**Signal Schema:**
- **Same as Atropos Push event**: CloudEvents-compliant OpenAPI Schema
- **Format**: OpenAPI Schema in JSON format, compliant with CloudEvents v1.0

**Example Configuration:**
```yaml
machine:
  id: "legacy-kafka-system"
  signal_emission:
    signals:
      - type: "transaction.completed"
        pull:
          protocols:
            - kafka_connect
          schemas:
            kafka_connect:
              # Same schema as Atropos Push
              openapi_schema:
                type: object
                required: ["id", "source", "specversion", "type", "data"]
                properties:
                  id: { type: string }
                  source: { type: string }
                  specversion: { type: string, enum: ["1.0"] }
                  type: { type: string }
                  data: { type: object }
              cloudevents_compliant: true

machine_instance:
  id: "acme-legacy-kafka"
  machine_id: "legacy-kafka-system"
  workbench_id: "transaction-operations"
  
  signal_emission:
    pull:
      kafka_connect:
        # Machine-provided Kafka endpoint and topic
        broker_endpoint: "kafka://legacy-system.acme.com:9092"
        topic: "transactions"
        auth:
          type: sasl_scram
          credentials_ref: "vault://secrets/legacy-kafka/auth"
        
        # Kafka Connect specific configuration
        connect_config:
          connector_class: "io.confluent.connect.kafka.KafkaSourceConnector"
          # Additional Kafka Connect properties
        
        # Hub-hosted topic (configured, dedicated to machine instance)
        # Pattern: /hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}
        hub_topic: "/hub/acme-bank/prod-subscription/transaction-operations/atropos/legacy-kafka-transactions"
```

**Flow:**
1. Hub uses Kafka Connect to connect to Machine-provided Kafka: `kafka://legacy-system.acme.com:9092`
2. Hub reads messages from Machine topic: `transactions`
3. Hub queues messages to Hub-hosted topic: `hub.transaction-operations.legacy-kafka.transactions`
4. Hub-hosted topic dispatches to Signal Exchange (push semantics)
5. Signal Exchange processes as normal push signals

### Pull Mechanism 3: SFTP Endpoints

**Protocol:** SFTP File Transfer  
**Signal Provider:** Dia  
**Direction:** Hub pulls files from Machine SFTP → Hub Dia SFTP endpoint → Signal Exchange

**Configuration:**
- **Machine-provided**: SFTP server endpoint and credentials (configured in Machine Instance)
- **Hub-provided**: Hub Dia SFTP endpoint for receiving files
- **Conversion**: Files pulled from Machine SFTP are uploaded to Hub Dia SFTP endpoint (push semantics)

**Signal Schema:**
- **TBD**: To be defined (similar to SFTP Push protocol)

**Example Configuration:**
```yaml
machine:
  id: "batch-file-system"
  signal_emission:
    signals:
      - type: "settlement.file.ready"
        pull:
          protocols:
            - sftp
          schemas:
            sftp:
              # TBD - To be defined
              schema: { ... }

machine_instance:
  id: "acme-batch-file"
  machine_id: "batch-file-system"
  workbench_id: "settlement-operations"
  
  signal_emission:
    pull:
      sftp:
        # Machine-provided SFTP server
        machine_sftp:
          endpoint: "sftp://batch-files.acme.com:22"
          path: "/outbound/settlements"
          auth:
            type: username_password
            credentials_ref: "vault://secrets/batch-file/sftp-auth"
        
        # Hub Dia SFTP endpoint (configured, subscription-scoped, per-workbench)
        # Pattern: /hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}
        hub_sftp:
          endpoint: "sftp://dia.olympus.tech:22"  # Hub-provided
          path: "/inbound/settlements/{workbench_id}"  # Workbench-scoped
          auth:
            type: api_key
            credentials_ref: "vault://secrets/hub-dia/sftp-key"
        
        # Polling configuration
        polling:
          schedule: "0 */5 * * * *"  # Every 5 minutes (cron format)
          file_filters:
            - pattern: "settlement_*.csv"
              min_size: 1024  # Minimum file size in bytes
```

**Flow:**
1. Hub connects to Machine-provided SFTP: `sftp://batch-files.acme.com:22`
2. Hub polls Machine SFTP path: `/outbound/settlements` according to configured schedule
3. Hub applies file filters during poll (pattern matching, size checks)
4. Hub reads file fully from Machine SFTP
5. Hub uploads pulled file to Hub Dia SFTP endpoint: `sftp://dia.olympus.tech:22/inbound/settlements/payment-operations` (immediately after full read)
6. Hub Dia SFTP endpoint processes file arrival (push semantics, validates file format)
7. Signal Exchange processes as normal push signals

**Note:** The pull mechanism does not validate files. File validation happens at the Hub Dia SFTP push endpoint according to the file format specification.

---

## Questions for Clarification

### General Pull-to-Push Conversion

**Resolved Decisions:**

1. **Hub-Hosted Topic/Endpoint Naming:**
   - **Pattern**: `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}`
   - **Configuration**: Topics/endpoints are configured (not auto-generated)
   - **Scoping**: Topics are dedicated to machine instance

2. **Automatic Conversion:**
   - **Decision**: Pull-to-push conversion is automatic when endpoints are appropriately provisioned and specified
   - Signal-pulling applications handle the conversion automatically

3. **Error Handling:**
   - **Decision**: Sound defaults for error handling will be implemented
   - Specific error handling strategies will be defined per provider and pull mechanism

### Atropos Subscription Pull

**Resolved Decisions:**

4. **Subscription Management:**
   - **Decision**: The signal-pulling application registers as a subscriber with the configured credentials
   - **Decision**: Atropos manages all subscription aspects (consumer groups, offsets, etc.)
   - **Decision**: Subscriber only needs to acknowledge processed messages

5. **Hub-Hosted Topic:**
   - **Decision**: Topic is dedicated to machine instance
   - **Decision**: Topic is auto-provisioned with machine instance
   - **Decision**: Tenant admin manages the topic lifecycle

### Kafka Connect Pull

**Resolved Decisions:**

6. **Kafka Connect Integration:**
   - **Decision**: Hub runs Kafka Connect connectors internally
   - **Decision**: Connectors are provisioned with machine instance
   - **Decision**: Connector lifecycle is tied to machine instance lifecycle

7. **Schema Compatibility:**
   - **Decision**: Schema transformation is kept as TBD in documentation
   - **Note**: Transformation should be possible but not specified at this stage

### SFTP Pull

**Resolved Decisions:**

8. **File Polling:**
   - **Decision**: Polling schedule is specified in the pull configuration
   - **Decision**: Hub polls on a configurable schedule
   - **Decision**: File filters are applied during poll

9. **File Processing:**
   - **Decision**: Files are pushed immediately after full read completion
   - **Decision**: Processing of pushed files follows the push endpoint configuration

10. **SFTP Pull Validation:**
    - **Decision**: Pull mechanism does not validate files
    - **Decision**: Pull mechanism reads file fully, then pushes to Hub Dia SFTP
    - **Note**: File validation happens at the push endpoint (Hub Dia SFTP)

### Authentication & Authorization

11. **Machine Endpoint Access:**
    - How are credentials for Machine-provided endpoints managed?
    - Are credentials per-Machine Instance or shared?
    - How are credentials rotated?

12. **Hub Endpoint Access:**
    - Who can access Hub-hosted topics/endpoints?
    - Are they workbench-scoped or tenant-scoped?

---

## Signal-Pulling Applications (Native Hub Applications)

> **Status:** 🟡 To Be Elaborated  
> **Purpose:** List essential native Hub applications that pull signals from Machines

Signal-pulling applications are **native Hub applications** that:
- Run within Hub infrastructure
- **Pull signals from Machines** (when Machine doesn't support push or uses pull model)
- Act as **sensors** that sense the Machine's state/events
- Deliver pulled signals to **Signal Providers** (Hub ingress)
- Handle various pull mechanisms and protocols

**Flow:**
```
Machine → [Signal-Pulling Application] → Signal Provider (Hub Ingress) → Signal Exchange
```

**Note:** These are different from **Sensory Tools** of Machines. Sensory Tools are Machine capabilities to *receive* signals (covered in Tools documentation). Signal-pulling applications are Hub applications that *retrieve* signals from Machines.

### Essential Signal-Pulling Applications

We should list and document native Hub applications that support a wide range of application signal pull scenarios:

| Application | Pull Mechanism | Use Case | Status |
|-------------|---------------|----------|--------|
| **REST API Poller** | REST API polling | Machines with REST endpoints | ⬜ To Document |
| **Database Poller** | Database query polling | Machines with database access | ⬜ To Document |
| **File Watcher** | File system polling | Machines that write files | ⬜ To Document |
| **Message Queue Consumer** | Queue consumption | Machines that publish to queues | ⬜ To Document |
| **Webhook Receiver** | Webhook registration | Machines that support webhooks | ⬜ To Document |
| **GraphQL Query** | GraphQL query polling | Machines with GraphQL APIs | ⬜ To Document |
| **gRPC Client** | gRPC service calls | Machines with gRPC services | ⬜ To Document |
| **Event Bus Subscriber** | Event bus subscription | Machines on event buses | ⬜ To Document |
| **SFTP Poller** | SFTP file polling | Machines that upload via SFTP | ⬜ To Document |
| **Change Data Capture (CDC)** | Database CDC | Real-time database change capture | ⬜ To Document |

### Application Characteristics

Each signal-pulling application should support:
- **Configurable polling intervals**
- **Filtering and transformation** of pulled signals
- **Error handling and retry logic**
- **Rate limiting** to avoid overwhelming source Machines
- **Signal normalization** to Signal Exchange format
- **Observability** (metrics, logs, traces)

### Example: REST API Poller Application

```yaml
application:
  type: signal_puller_rest_api
  name: "legacy-system-signal-puller"
  
  config:
    # Source: Machine endpoint to pull from
    source:
      machine_id: "legacy-system"
      endpoint: "https://legacy-system.acme.com/api/v1/signals"  # Machine endpoint
      auth:
        type: oauth2
        credentials_ref: "vault://secrets/hub-to-machine-oauth"
    
    # Hub-controlled polling
    polling:
      interval: "5m"
      batch_size: 100
      timeout: "30s"
    
    # Filtering
    filtering:
      signal_types:
        - "payment.authorized"
        - "payment.completed"
      since: "2026-01-01T00:00:00Z"
    
    # Transformation: Machine format → Signal Exchange format
    transformation:
      mapping:
        signal_type: "$.event.type"
        payload: "$.event.data"
    
    # Target: Deliver to Signal Provider (Hub ingress)
    target:
      signal_provider: atropos  # Hub ingress endpoint
      topic: "legacy-system.events"
```

**Flow:**
1. Signal-pulling application queries Machine endpoint
2. Application transforms Machine format to Signal Exchange format
3. Application delivers to Signal Provider (Hub ingress)
4. Signal Provider forwards to Signal Exchange

---

## Next Steps

1. ✅ Document current understanding (this scratchpad)
2. ⬜ **Elaborate Signal Provider Requirements & Ingress Endpoints** (this section)
3. ⬜ **Resolve Push vs Pull model** (architecture decision)
4. ⬜ **Design signal-pulling applications** (if pull model adopted)
5. ⬜ Resolve key questions with architecture team
6. ⬜ Design `signal_emission` schema
7. ⬜ Update Machine Registry documentation
8. ⬜ Create configuration guide
9. ⬜ Add examples to each Signal Provider documentation
