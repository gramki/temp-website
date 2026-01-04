# I/O Gateways (Signal Providers)

I/O Gateways are Machines in the Hub Environment that sense Signals from various protocols and channels, execute Workbench-defined Triggers, and create standardized Requests for Operations.

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
│        └─────────────┴──────┬──────┴─────────────┘              │
│                             ▼                                    │
│                    TRIGGER (Workbench-defined)                   │
│                             │                                    │
│                             ▼                                    │
│                         REQUEST                                  │
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

### 2. Trigger Execution
I/O Gateways execute Workbench-defined Triggers:

| Trigger Responsibility | Description |
|------------------------|-------------|
| **Filter** | Determine which incoming Signals should proceed |
| **Transform** | Convert protocol-specific format to/from Request/Response |
| **Access** | Enforce authorization rules at I/O boundary |
| **Bind** | Map protocol message → Request (input) and Response → protocol message (output) |

### 3. Request Creation
- Create standardized Requests from protocol-specific inputs
- Requests are channel-agnostic—Operations don't know their origin

### 4. Response Handling
- Receive Operation responses
- Transform back to protocol-specific format
- Deliver to originating channel

## Workbench Trigger Configuration

Triggers are defined in Workbench configurations, not in the I/O Gateways themselves. This allows:
- Same I/O Gateway to serve multiple Workbenches
- Workbench-specific filtering and transformation rules
- Centralized Trigger management in Workbench Studio

## Relationship to Other Subsystems

| Subsystem | Relationship |
|-----------|--------------|
| **Workbench Studio** | Defines Triggers that I/O Gateways execute |
| **Operations Center** | Receives Requests created by I/O Gateways |
| **Automation Runtimes** | Execute Operations on Requests |
| **Cipher IAM** | Provides authentication/authorization for I/O boundaries |

## Infrastructure Notes

For detailed infrastructure configuration (Kong, networking, security), see:
- [Heracles Gateway Infrastructure](../../05-infrastructure/heracles-gateway.md)
- [Traffic Management](../../05-infrastructure/traffic-management.md)

---

*Each I/O Gateway has its own detailed documentation linked above.*

