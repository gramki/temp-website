# I/O Gateways (Signal Providers)

I/O Gateways are Machines in the Hub Environment that sense Signals from various protocols and channels, forward them to Signal Exchange, and receive responses back to the originating channel. Signal Exchange executes Workbench-defined Triggers and creates standardized Requests for Hub Applications.

> **Olympus Academy References:**
> - [Atropos - Event Bus](https://atropos.olympus.tech/)
> - [Dia - Object/File Store](https://dia.olympus.tech/)
> - [Heracles - Traffic Management](https://heracles.olympus.tech/)
>
> **Note:** Cronus handles **Business Exceptions and Observations**—higher-order business anomalies, not system-level monitoring. Watch may optionally map system alerts to Cronus signals.

## Architectural Role

```
┌─────────────────────────────────────────────────────────────────┐
│                 I/O GATEWAYS (Machines in Environment)           │
│                                                                  │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│   │ Atropos  │  │ Cronus   │  │ Heracles │  │   Dia    │        │
│   │ (Events) │  │(Obs/Exc) │  │(HTTP/API)│  │ (Files)  │        │
│   └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘        │
│        │             │             │             │              │
│        │ 1. Sense protocol-specific signals                      │
│        │ 2. Transform to normalized format                      │
│        └─────────────┴──────┬──────┴─────────────┘              │
│                             ▼                                    │
│                    SIGNAL EXCHANGE                                │
│                    (Normalized Signal DTO)                        │
│                             │                                    │
│                             ▼                                    │
│                    Trigger Evaluation → Request Creation          │
└─────────────────────────────────────────────────────────────────┘
```

## I/O Gateway Inventory

| Gateway | Signal Type | Protocol | Description | Status |
|---------|-------------|----------|-------------|--------|
| [Atropos](./atropos-event-bus.md) | Event | Pub-Sub Event Bus | State changes from Machines | 🟡 WIP |
| [Cronus](./cronus-business-exceptions.md) | Exception, Observation | Publisher API | Business-level anomalies | 🟡 WIP |
| [Heracles](./heracles-api-gateway.md) | HTTP-Request | HTTP/REST/MCP | API calls from users, apps, agents | 🟡 WIP |
| [Dia](./dia-file-gateway.md) | Batch-Request | SFTP/HTTP/WebDAV | File arrivals with batch data | 🟡 WIP |
| [Kale](./kale-scheduler.md) | Time-Signal | Scheduler | Scheduled triggers | 🟡 WIP |
| [MS Teams](./ms-teams-integration.md) | CHAT_MESSAGE | MS Teams Bot Framework | Copilot bots + chat collaboration | 🟡 WIP |

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

### 4. Response Handling
- Receive responses from Signal Exchange (for bidirectional I/O Gateways)
- Transform normalized response format back to protocol-specific format
- Deliver to originating channel

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

