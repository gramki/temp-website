# Signal Exchange

> **Status:** 🟡 Draft — Under active development

The Signal Exchange is the **data plane** that handles the bidirectional flow of signals and responses between Signal Providers and Hub Applications. It is a **message-oriented system** (similar to Atropos and OMS*) that provides **flow control** and can operate as a **store-and-forward engine** when configured.

> *OMS (Olympus Message System) is an in-house broker-less message exchange framework similar to ZeroMQ.

---

## Overview

The Signal Exchange is responsible for:

| Function | Description |
|----------|-------------|
| **Inbound Routing** | Signal Provider → Trigger Evaluation → Request Creation/Update → Application Router → Hub Application |
| **Outbound Routing** | Hub Application Response → Response Transformation → I/O Gateway |
| **Async Update Capture** | Receive intermediate updates from long-running Applications |
| **Observer Notifications** | Dispatch Request Updates to registered observer modules (NOT to agents/tasks directly) |
| **Flow Control** | Rate limiting, back-pressure, throttling per Scenario |
| **Store-and-Forward** | Optional buffering and reliable delivery (configurable per Scenario) |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      SIGNAL EXCHANGE                              │
│                       (Data Plane)                               │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   SIGNAL INTAKE                          │    │
│  │          (From all Signal Providers)                     │    │
│  │                                                          │    │
│  │   • I/O Gateways (Atropos, Cronus, Heracles, Dia, Kale) │    │
│  │   • Other Signal Providers (input-only sources)         │    │
│  └─────────────────────────┬───────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │                 TRIGGER EVALUATOR                        │    │
│  │                                                          │    │
│  │   • Load trigger definitions from Workbench Management   │    │
│  │   • Match signals against trigger conditions             │    │
│  │   • Execute trigger transformations                      │    │
│  └─────────────────────────┼───────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │                  REQUEST FACTORY                         │    │
│  │                                                          │    │
│  │   • Create new Requests                                  │    │
│  │   • Update existing Requests (from subsequent signals)  │    │
│  │   • Manage Request-Application session binding          │    │
│  └─────────────────────────┼───────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │                APPLICATION ROUTER                        │    │
│  │                                                          │    │
│  │   • Route Requests to appropriate Hub Applications       │    │
│  │   • Route Request updates to active Application sessions │    │
│  │   • Handle Application selection based on Scenario       │    │
│  └─────────────────────────┼───────────────────────────────┘    │
│                            │                                     │
│                            ▼                                     │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   HUB APPLICATIONS                       │    │
│  │                                                          │    │
│  │   ┌─────────────┐ ┌─────────────┐ ┌─────────────────┐   │    │
│  │   │    File     │ │  Workflow   │ │   Seer Case     │   │    │
│  │   │    Apps     │ │    Apps     │ │  Orchestration  │   │    │
│  │   │  (Perseus)  │ │   (Rhea)    │ │     Agent       │   │    │
│  │   └─────────────┘ └─────────────┘ └─────────────────┘   │    │
│  │                                                          │    │
│  │   ┌─────────────┐ ┌─────────────────────────────────┐   │    │
│  │   │  Procedure  │ │   Durable Workflow              │   │    │
│  │   │    Apps     │ │        Apps                     │   │    │
│  │   │ (Atlantis)  │ │   (ChronoShift)                 │   │    │
│  │   └─────────────┘ └─────────────────────────────────┘   │    │
│  └─────────────────────────┬───────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │              RESPONSE TRANSFORMER                        │    │
│  │                                                          │    │
│  │   • Transform Application responses                      │    │
│  │   • Format for I/O Gateway protocols                    │    │
│  │   • Only for bidirectional Signal Providers             │    │
│  └─────────────────────────┬───────────────────────────────┘    │
│                            │                                     │
│                            ▼                                     │
│                   I/O GATEWAYS                                   │
│           (Bidirectional Signal Providers only)                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Signal Provider Interactions](./signal-provider-interactions.md) | Signal Provider registration, DTOs, filters, triggers | 🟡 Draft |
| [Message Envelope](./message-envelope.md) | Signal Exchange ↔ Hub Application DTOs | 🟡 Draft |
| [Trigger Evaluator](./trigger-evaluator.md) | Trigger matching and transformation | 🔴 Stub |
| [Request Factory](./request-factory.md) | Request creation and updates | 🔴 Stub |
| [Application Router](./application-router.md) | Routing to Hub Applications | 🔴 Stub |
| [Response Transformer](./response-transformer.md) | Response transformation for I/O Gateways | 🔴 Stub |
| [Flow Controller](./flow-controller.md) | Flow control and store-and-forward | 🔴 Stub |
| [Observer Notifications](./observer-notifications.md) | Request lifecycle notifications to observers | 🔴 Stub |

---

## Key Concepts

### Signal Providers vs I/O Gateways

| Type | Description | Response Path |
|------|-------------|---------------|
| **I/O Gateway** | Bidirectional Signal Provider | Yes — receives responses |
| **Signal Provider** | May be input-only | No — fire-and-forget |

All I/O Gateways are Signal Providers, but not all Signal Providers are I/O Gateways.

### Request as Application Session

A **Request** represents a potentially long-running session for a Hub Application:
- Initial signal creates the Request
- Subsequent signals can update the Request
- The Application processes the Request over its lifetime
- The Request tracks the full interaction history

### Message Dispatch vs Request Status

Signal Exchange tracks two distinct state machines:

| Concern | Scope | States |
|---------|-------|--------|
| **Message Dispatch** | Per message (initiation, update) | CREATED → DISPATCHED → ACKNOWLEDGED/FAILED |
| **Request Status** | The request as a whole | ACTIVE → PENDING → COMPLETED/CANCELLED |

> **Note:** Escalation is a **Task** concern, not a Request concern. See [Task Management](../task-management/README.md).

### Standard Message Envelope

Signal Exchange enforces a **standard envelope** for all Application communication:
- Application-specific payloads are embedded within the envelope
- Applications return **Request Status** (business state) and **Response Status** (semantic outcome)
- Response Status includes user-reportable codes and messages

See [Message Envelope](./message-envelope.md) for details.

### Hub Application

A **Hub Application** is the automation artifact that corresponds to a Scenario. Each Automation Runtime provides specialized Hub Application types:

| Automation Runtime | Hub Application Type(s) |
|-------------------|------------------------|
| **Atlantis** | Procedure Apps, Decision Apps, Prediction Apps |
| **Perseus** | File Apps, Map-Reduce Apps, Complex Event Apps |
| **Rhea** | Workflow Apps |
| **ChronoShift** | Durable Workflow Apps |
| **Seer** | Seer Case Orchestration Agent |

### Flow Control

The Signal Exchange provides flow control capabilities to manage signal throughput:

| Capability | Description |
|------------|-------------|
| **Rate Limiting** | Limit signals per second/minute to protect downstream Applications |
| **Back-Pressure** | Slow down Signal Providers when Applications are overwhelmed |
| **Throttling** | Per-Scenario throttling based on Application capacity |
| **Priority Queuing** | Prioritize high-priority signals over low-priority ones |

### Store-and-Forward Mode

When configured for a Scenario, Signal Exchange operates as a **store-and-forward engine**:

| Aspect | Description |
|--------|-------------|
| **Durability** | Signals are persisted before acknowledgment |
| **Guaranteed Delivery** | Signals are retried until successfully delivered |
| **Ordering** | Optional ordering guarantees (FIFO, priority-based) |
| **Batching** | Signals can be batched for efficient delivery |
| **Dead-Letter Handling** | Failed signals routed to dead-letter queue after retries |

Store-and-forward is configured per Scenario in Workbench Management:

```yaml
scenario:
  id: "high-volume-payments"
  flow_control:
    mode: store_and_forward    # direct | store_and_forward
    rate_limit: 1000/s
    priority: high
    ordering: fifo
    retry_policy:
      max_attempts: 5
      backoff: exponential
    dead_letter:
      enabled: true
      queue: "payments-dlq"
```

---

## Runtime Flow

### Inbound Flow (Signal → Application)

```
1. Signal arrives from Signal Provider
2. Signal Intake receives and normalizes signal
3. Trigger Evaluator:
   a. Loads trigger definitions (from Workbench Management)
   b. Matches signal against trigger conditions
   c. Executes trigger transformation
4. Request Factory:
   a. Creates new Request OR
   b. Updates existing Request (for ongoing sessions)
5. Application Router:
   a. Determines target Hub Application from Scenario
   b. Routes Request to Application
6. Hub Application begins processing
```

### Outbound Flow (Application → I/O Gateway)

```
1. Hub Application produces response
2. Response Transformer:
   a. Transforms response to I/O Gateway protocol
   b. Applies output mappings from trigger definition
3. I/O Gateway delivers response to originator
```

### Async Update Flow (Application → Observers)

Long-running Applications (workflows, durable workflows, case management) can send intermediate updates:

```
1. Hub Application sends async update to Signal Exchange
2. Signal Exchange captures update:
   a. Updates Request state (if state change)
   b. Records update details in Request history
3. Signal Exchange dispatches to registered observers:
   a. Identifies registered observer MODULES for this Request
   b. Formats notification per observer's subscription
   c. Delivers to observer modules (NOT to agents/tasks directly)
4. Observer modules receive notification and determine user-level actions
```

**Critical Principle:**
- Signal Exchange dispatches Request Updates to **observer modules** (e.g., MS Teams module, Neutrino, Ops Center)
- Signal Exchange does NOT dispatch to individual agents, tasks, or users
- Signal Exchange operates at the **Request level** only — it cannot attribute updates to specific tasks or agents
- Observer modules parse update content to determine which users/agents to notify

### Observer Notification Patterns

| Pattern | Description |
|---------|-------------|
| **Push** | Immediate dispatch to observer module via webhook, WebSocket, or event |
| **Pull** | Observer module polls for status (Signal Exchange caches latest) |
| **Batch** | Updates aggregated and delivered to observer module periodically |

> **Note:** These patterns describe how Signal Exchange delivers to observer **modules** (like MS Teams integration, Neutrino, dashboards). User-level notification logic is the responsibility of each observer module.

---

## Integration Points

| Component | Integration | Protocol |
|-----------|-------------|----------|
| **Signal Providers** | Signal intake, observer notifications | Message (Atropos/OMS) |
| **I/O Gateways** | Signal intake + response delivery | Message (Atropos/OMS) |
| **Hub Applications** | Request dispatch, response handling | Message (Atropos/OMS) |
| **Workbench Management** | Trigger definitions, Scenario → Application mappings | Internal |
| **Request Management** | Request state, storage, entity binding | Internal |
| **CAF** | Decision records for routing decisions | Internal |

### Interface Separation

| Interface | Protocol | Use Case |
|-----------|----------|----------|
| **Signal Exchange** | Message (Atropos/OMS) | Create or update Hub Requests |
| **Request Lifecycle** | HTTP REST | Lifecycle enquiry, status checks, cancellation |

> **Note:** Signal Providers use the **Signal Exchange** message interface for interactions that create or update Requests. For **lifecycle and enquiry** operations, Signal Providers can use the **Request Lifecycle** module's HTTP interface.

See [Signal Provider Interactions](./signal-provider-interactions.md) for details.

---

## Operational Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Stateless (Direct Mode)** | In direct mode, Signal Exchange is stateless; state is in Requests |
| **Stateful (Store-and-Forward)** | In store-and-forward mode, signals are buffered durably |
| **Scalable** | Horizontally scalable for high signal volume |
| **Observable** | Full tracing of signal → request → application flow |
| **Idempotent** | Duplicate signals handled via idempotency keys |
| **Back-Pressure Aware** | Propagates back-pressure to Signal Providers |

---

## Related Documentation

- [Workbench Management](../workbench-management/README.md) — Control plane for trigger definitions
- [Signal Providers](../signal-providers/README.md) — Signal sources
- [Automation Runtimes](../automation-runtimes/README.md) — Hub Application hosts
- [Hub Architecture](../../02-system-design/hub-architecture.md) — System context

---

*TODO: Detailed design — trigger evaluation algorithms, routing strategies, response transformation, observability*

