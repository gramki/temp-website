# I/O Gateways (Signal Providers)

I/O Gateways are Machines in the Hub Environment that sense Signals from various protocols and channels, forward them to Signal Exchange, and receive responses back to the originating channel. Signal Exchange executes Workbench-defined Triggers and creates standardized Requests for Hub Applications.

> **Olympus Academy References:**
> - [Atropos - Event Bus](https://atropos.olympus.tech/)
> - [Dia - Object/File Store](https://dia.olympus.tech/)
> - [Heracles - Traffic Management](https://heracles.olympus.tech/)
>
> **Note:** Cronus handles **Business Exceptions and Observations**—higher-order business anomalies, not system-level monitoring. Watch may optionally map system alerts to Cronus signals.

## Architectural Role

**Signal Providers (I/O Gateways) are Machines in the Hub Environment** that serve as Hub ingress endpoints. **Machines emit signals through Signal Providers**, which normalize signals and forward them to Signal Exchange.

**Signal Flow:**
```
Domain Machine → Signal Provider (Hub Ingress) → Signal Exchange → Trigger → Scenario/Application
```

### Complete Signal Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    DOMAIN MACHINES                               │
│              (e.g., Payment Switch, Core Banking)               │
│                                                                  │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  Machines emit signals via:                              │   │
│   │  • Push: Webhook, Atropos Inbox, SFTP                    │   │
│   │  • Pull: Atropos Subscription, Kafka Connect, SFTP Poll  │   │
│   └───────────────┬─────────────────────────────────────────┘   │
│                   │                                              │
│                   ▼                                              │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │         SIGNAL PROVIDERS (Hub Ingress Endpoints)         │   │
│   │              (I/O Gateways - Machines in Environment)    │   │
│   │                                                           │   │
│   │   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│   │   │ Atropos  │  │ Cronus   │  │ Heracles │  │   Dia    │ │
│   │   │ (Events) │  │(Obs/Exc) │  │(HTTP/API)│  │ (Files)  │ │
│   │   └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘ │
│   │        │             │             │             │       │
│   │        │ 1. Receive signals at Hub ingress endpoints      │
│   │        │ 2. Validate schema (per protocol)                 │
│   │        │ 3. Transform to normalized format                 │
│   │        └─────────────┴──────┬──────┴─────────────┘       │
│   └─────────────────────────────┼─────────────────────────────┘
│                                   ▼                            │
│                          SIGNAL EXCHANGE                       │
│                    (Normalized Signal DTO)                      │
│                                   │                            │
│                                   ▼                            │
│                    Trigger Evaluation → Request Creation        │
└─────────────────────────────────────────────────────────────────┘
```

**Key Points:**
- Signal Providers are Machines themselves in the Hub Environment
- Machines emit signals through Signal Providers (Hub ingress)
- Signal Providers validate schemas during normalization
- All signals are normalized to Signal Exchange format regardless of source protocol

## I/O Gateway Inventory

| Gateway | Signal Type | Protocol | Description | Status |
|---------|-------------|----------|-------------|--------|
| [Atropos](./atropos-event-bus.md) | Event | Pub-Sub Event Bus | State changes from Machines | 🟡 WIP |
| [Cronus](./cronus-business-exceptions.md) | Exception, Observation | Publisher API | Business-level anomalies | 🟡 WIP |
| [Heracles](./heracles-api-gateway.md) | HTTP-Request | HTTP/REST/MCP | API calls from users, apps, agents | 🟡 WIP |
| [Dia](./dia-file-gateway.md) | Batch-Request | SFTP/HTTP/WebDAV | File arrivals with batch data | 🟡 WIP |
| [Kale](./kale-scheduler.md) | Time-Signal | Scheduler | Scheduled triggers | 🟡 WIP |
| [MS Teams](./ms-teams-integration.md) | CHAT_MESSAGE | MS Teams Bot Framework | Copilot bots + chat collaboration | 🟡 WIP |

### Additional Documentation

**Dia (File Gateway):**
- [File Format Specification](./dia/file-format-specification.md) - Schema definition for CSV/TSV/fixed-width file formats with header/footer validation
- [Parser Requirements](./dia/parser-requirements.md) - Detailed requirements for implementing the file format parser

**Extensibility:** Signal types are tied to I/O Gateways. New gateways (e.g., GraphQL, gRPC, WebSocket) can introduce new signal types while the core flow remains stable: **Signal → Trigger → Request → Scenario → Operation**.

> **Note:** MS Teams Integration is more than a signal provider — it includes copilot bots, chat group orchestration, and direct services. See [MS Teams Integration](../ms-teams-integration/) for full documentation.

## Common Responsibilities

All I/O Gateways share these responsibilities:

### 1. Signal Sensing
- Listen for protocol-specific messages from the Environment
- Parse and validate incoming data
- Extract relevant metadata (source, timestamp, correlation IDs)

### 2. Transport & Security
I/O Gateways handle the transport layer, authentication, and access control for their scope:

| Responsibility | Description |
|----------------|-------------|
| **Transport Layer** | Manage protocol-specific communication (HTTP, event bus, file transfer, etc.) |
| **Authentication** | Authenticate incoming requests/signals at the I/O boundary |
| **Access Control** | Enforce authorization rules for their scope (additional controls may be enforced at subsequent subsystems) |
| **Communication Port** | Provide communication port and semantics to accept signals under a tenant's subscription |

### 3. Signal Normalization
I/O Gateways transform protocol-specific signals to Signal Exchange's normalized signal format:

- Transform from protocol-specific format → Signal Exchange's normalized DTO format
- Ensure all required fields (tenant_id, subscription_id, signal_id, etc.) are present
- Preserve protocol-specific metadata as additional fields (if needed)
- Align to Signal Exchange's DTO structure while maintaining extensibility

> **Note:** Signal Exchange receives signals in a single, normalized format regardless of the originating protocol. I/O Gateways are responsible for this transformation.

### 4. Signal Schema Validation

**Signal schema validation occurs at the Signal Provider during normalization.** Each provider validates according to its protocol requirements:

| Signal Provider | Validation Method |
|----------------|-------------------|
| **Heracles (Webhook)** | Validates against OpenAPI specification for POST request body |
| **Atropos Inbox** | Validates CloudEvents v1.0 compliance |
| **Dia (SFTP)** | Validates file format specification (CSV/TSV/Fixed-Width) |
| **Cronus** | Validates exception/observation schema |

Validation failures are handled according to provider-specific error handling policies.

### 5. Response Handling
- Receive responses from Signal Exchange (for bidirectional I/O Gateways)
- Transform normalized response format back to protocol-specific format
- Deliver to originating channel

---

## Hub Ingress Endpoints

**Hub ingress endpoints** are the entry points into the Hub platform where Machines send signals. These endpoints are exposed by Signal Providers and serve as the Hub's boundary for signal reception.

### Endpoint Characteristics

| Characteristic | Description |
|---------------|-------------|
| **Scoping** | Subscription-scoped and per-workbench |
| **Naming Pattern** | `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}` |
| **Provisioning** | Provisioned by tenant admin or authorized developers as resources when required |
| **Authentication** | Per-provider authentication mechanisms |

### Endpoint Provisioning

Hub ingress endpoints are provisioned as resources within a subscription and workbench context:

1. **Tenant Admin** can provision endpoints for any workbench in their tenant
2. **Authorized Developers** can provision endpoints for workbenches they have access to
3. Endpoints are tied to the workbench lifecycle
4. Endpoint configuration includes authentication credentials and access policies

### Example Endpoint Patterns

- **Heracles Webhook**: `https://heracles.olympus.tech/api/workbenches/{workbench-id}/signals`
- **Atropos Topic**: `/hub/{tenant}/{subscription}/{workbench-id}/atropos/{topic-name}`
- **Dia SFTP**: `sftp://dia.olympus.tech:22/inbound/{workbench-id}/{folder-path}`

For detailed configuration, see [Machine Registry](../registry-services/machine-registry.md) and [Machine Signal Emission Guide](../../10-guides/machine-signal-emission-guide.md).

## Workbench Trigger Configuration

Triggers are defined in Workbench Management and executed by Signal Exchange, not by I/O Gateways. This allows:
- Same I/O Gateway to serve multiple Workbenches
- Workbench-specific filtering and transformation rules
- Centralized Trigger management in Workbench Management
- I/O Gateways to focus on transport, security, and normalization

## Relationship to Other Subsystems

| Subsystem | Relationship |
|-----------|--------------|
| **Workbench Management** | Defines Triggers that Signal Exchange executes (not I/O Gateways) |
| **Signal Exchange** | Receives normalized signals from I/O Gateways, executes triggers, creates and routes Requests |
| **Automation Runtimes** | Execute Hub Applications on Requests |
| **Cipher IAM** | Provides authentication/authorization for I/O boundaries |

## Infrastructure Notes

For detailed infrastructure configuration (Kong, networking, security), see:
- [Heracles Gateway Infrastructure](../../05-infrastructure/heracles-gateway.md)
- [Traffic Management](../../05-infrastructure/traffic-management.md)

---

*Each I/O Gateway has its own detailed documentation linked above.*

