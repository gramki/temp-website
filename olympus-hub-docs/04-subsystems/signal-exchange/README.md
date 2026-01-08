# Signal Exchange

> **Status:** 🟡 Draft — Under active development

The Signal Exchange is the **data plane** that handles the bidirectional flow of signals and responses between Signal Providers and Hub Applications. It is a **message-oriented system** (similar to Atropos and OMS*) that provides **flow control** and can operate as a **store-and-forward engine** when configured.

> *OMS (Olympus Message System) is an in-house broker-less message exchange framework similar to ZeroMQ.

---

## Overview

The Signal Exchange is responsible for:

| Function | Description |
|----------|-------------|
| **Inbound Routing** | Normalized Signal → Trigger Evaluation → Request Creation/Update → Application Router → Hub Application |
| **Outbound Routing** | Hub Application Response → Response Transformation → I/O Gateway |
| **Request Update Capture** | Receive intermediate updates (REQUEST_UPDATE) from long-running Applications |
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
│  │     (Normalized Signal DTO from all Signal Providers)     │    │
│  │                                                          │    │
│  │   • I/O Gateways (Atropos, Cronus, Heracles, Dia, Kale) │    │
│  │   • Other Signal Providers (input-only sources)         │    │
│  │                                                          │    │
│  │   All signals arrive in Signal Exchange's normalized     │    │
│  │   DTO format, regardless of originating protocol         │    │
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
│  │   • Transform from normalized format to I/O Gateway     │    │
│  │     protocol format                                     │    │
│  │   • Only for bidirectional Signal Providers (io_gateway)│    │
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
| [Reminder Capability](./reminder-capability.md) | Time-based reminder scheduling and notifications | 🟡 Draft |
| [Memory Record Routing](./memory-record-routing.md) | Routing memory records from Request Updates to memory stores | 🟡 Draft |
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
| **I/O Gateway** | Bidirectional Signal Provider (type: `io_gateway`) | Yes — receives responses |
| **Signal Provider** | May be input-only (type: `signal_source`) | No — fire-and-forget |

All I/O Gateways are Signal Providers, but not all Signal Providers are I/O Gateways. The `io_gateway` type indicates a bidirectional provider that receives responses, while `signal_source` indicates an input-only provider that does not receive responses.

### Request as Application Session

A **Request** represents a potentially long-running session for a Hub Application:
- Initial signal creates the Request
- Subsequent signals can update the Request
- The Application processes the Request over its lifetime
- The Request tracks the full interaction history

### Request Hierarchy (Parent-Child Requests)

When a Hub Application invokes another Scenario **within the same workbench** (as tool or agent), a **child request** is created:

| Aspect | Behavior |
|--------|----------|
| **Context Inheritance** | Child can access parent context via reference |
| **Lifecycle Cascade** | Child is completed/cancelled when parent completes/cancels |
| **Observer Isolation** | Observers see only their specific request's updates |
| **Depth Limit** | Configurable per workbench (default: 5) |

**Cross-workbench invocations** do NOT create parent-child relationships — invoker must explicitly forward context.

→ **Details:** [Request Hierarchy](../request-management/request-hierarchy.md)

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
1. Signal Provider sends signal in normalized DTO format to Signal Exchange
   (I/O Gateways transform protocol-specific signals to normalized format)
2. Signal Intake receives normalized signal
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

> **Note:** Signal Exchange executes triggers and creates/manages requests. Signal Providers only forward signals in normalized format; they do not execute triggers or create requests.

### Outbound Flow (Application → I/O Gateway)

```
1. Hub Application produces response
2. Response Transformer:
   a. Transforms response to I/O Gateway protocol
   b. Applies output mappings from trigger definition
3. I/O Gateway delivers response to originator
```

### Request Update Flow (Application → Observers)

Long-running Applications (workflows, durable workflows, case management) can send intermediate updates via `REQUEST_UPDATE` messages:

```
1. Hub Application sends REQUEST_UPDATE to Signal Exchange
2. Signal Exchange captures update:
   a. Updates Request state (if state change)
   b. Records update details in Request history
   c. Extracts memory_records and routes to memory stores (see below)
3. Signal Exchange dispatches to registered observers:
   a. Identifies registered observer MODULES for this Request
   b. Formats notification per observer's subscription
   c. Delivers to observer modules (NOT to agents/tasks directly)
4. Observer modules receive notification and determine user-level actions
```

> **Note:** In Signal Exchange ↔ Hub Application interactions, **Async Update and Request Update are the same concept**. Both use `REQUEST_UPDATE` message type.

### Memory Record Routing (Application → Memory Stores)

**Critical Design Decision:** All enterprise episodic memory writes flow through Signal Exchange. Applications and agents do not directly access memory store write APIs.

**Schema Validation:** Signal Exchange validates all memory records against registered schemas. Valid records are routed to memory stores; invalid records are retained in request history (marked invalid) but NOT written to memory stores. See [Memory Record Routing](./memory-record-routing.md) for details.

**Cognitive Applications:** Applications that regularly emit memory records should be modeled as [Cognitive Applications](../../02-system-design/implementation-concepts/cognitive-application.md).

```
1. Hub Application attaches memory_records to REQUEST_UPDATE
   (decision_records, evidence_bundles, handoff_context, etc.)
2. Signal Exchange extracts memory_records from update payload
3. For each memory record:
   a. Validates against CAF schema
   b. Enriches with hub_metadata (tenant, workbench, scenario, request_id)
   c. Determines target Atropos topic based on memory_class and Scenario config
   d. Publishes to Atropos topic
4. Memory Store Writer Service consumes from Atropos and indexes in OpenSearch
```

See [Memory Record Routing](./memory-record-routing.md) for full specification.

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
| **Hub Applications** | Request dispatch, response handling | HTTP, Atropos, or OMS (per Application Runtime preference) |
| **Workbench Management** | Trigger definitions, Scenario → Application mappings | Internal |
| **Request Management** | Request state, storage, entity binding | Internal |
| **CAF** | Decision records for routing decisions | Internal |

### Interface Separation

| Interface | Protocol | Use Case |
|-----------|----------|----------|
| **Signal Exchange** | Message (Atropos/OMS) | Create or update Hub Requests |
| **Request Lifecycle** | HTTP REST | Lifecycle enquiry, status checks, cancellation |

> **Note:** Signal Providers use the **Signal Exchange** message interface for interactions that create or update Requests. For **lifecycle and enquiry** operations, Signal Providers can use the **Request Lifecycle** module's HTTP interface.

### Delivery Interfaces

Signal Exchange uses multiple transport interfaces for delivering messages. The same transport options (HTTP, Atropos, OMS) are available for both **Application Runtimes** and **Signal Providers**.

| Interface | Protocol | Characteristics |
|-----------|----------|-----------------|
| **HTTP** | HTTP/REST | Synchronous request-response, standard REST API |
| **Atropos** | Event Bus | Pub-sub messaging, asynchronous delivery |
| **OMS** | Message (Olympus Message System) | Broker-less messaging, asynchronous delivery |

#### Application Runtime Delivery

Signal Exchange delivers messages to Application Runtimes over their preferred interface:

**Key Characteristics:**
- **Interface Selection**: Each Application Runtime specifies its preferred interface(s) during registration/configuration
- **Bidirectional**: Signal Exchange both delivers messages to Applications and accepts updates from Applications on any of these interfaces
- **Out-of-Order Delivery**: Messages may arrive out of order — Application Runtimes must handle ordering if required
- **Deduplication**: Deduplication is the responsibility of the recipient (Application Runtime), not Signal Exchange
- **Idempotency**: Application Runtimes should design their message handlers to be idempotent

#### Signal Provider Update Delivery

Signal Providers register their preferred interface for receiving Request updates from Signal Exchange:

**Key Characteristics:**
- **Interface Selection**: Each Signal Provider specifies its preferred interface (HTTP, Atropos, or OMS) during registration in the `update_delivery` configuration
- **Same Transport Options**: Signal Providers have access to the same transport options (HTTP, Atropos, OMS) as Application Runtimes
- **Observer Updates**: Signal Providers that initiate Requests are automatically registered as observers and receive updates via their configured interface
- **Out-of-Order Delivery**: Messages may arrive out of order — Signal Providers must handle ordering if required
- **Deduplication**: Deduplication is the responsibility of the recipient (Signal Provider), not Signal Exchange
- **Idempotency**: Signal Providers should design their update handlers to be idempotent

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

