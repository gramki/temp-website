# Signal Exchange

> **Category:** Signal Architecture

---

## Overview

**Signal Exchange (SX)** is Hub's central routing and orchestration service. It receives normalized signals from I/O Gateways, evaluates triggers to determine which Scenarios should respond, creates and manages Requests, routes updates to Hub Applications, and notifies observers. SX connects signal ingestion to application execution.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Signals** (what's happening), **Triggers** (conditions that activate Scenarios), and **Scenarios** (operational requirements). However, it doesn't specify:
- How signals are routed to the right Scenario
- How trigger evaluation happens at runtime
- How updates flow between Applications and external systems
- How multiple observers (Notification Services, Task Management, MS Teams) receive updates

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Signal | Normalized Signal DTO | SX receives normalized signals |
| Trigger | Trigger Evaluator | SX evaluates trigger conditions |
| Scenario | Request + Hub Application | SX creates Requests and routes to Applications |
| (not covered) | Signal Exchange | Orchestrates the flow between all components |

### Gap This Fills

The ontology describes **what** should happen conceptually. Signal Exchange implements **how** it happens:
1. **Routing**: Which Application handles which signal?
2. **Stateful tracking**: How are request updates accumulated?
3. **Integration**: How do multiple subsystems stay synchronized?
4. **Reliability**: How are messages delivered reliably?

---

## Definition

**Signal Exchange** is the central data-plane service that:
- Receives normalized signals from I/O Gateways (which receive signals from Machines)
- Evaluates triggers to match signals to Scenarios
- Creates Requests and manages their lifecycle
- Routes request updates to Hub Applications
- Notifies registered observers of request events
- Provides reminder capabilities for time-based stimuli

### Machine Signal Emission

**Machines emit signals through Signal Providers (I/O Gateways)**, which serve as Hub ingress endpoints. Signal Providers:
- Receive signals from Machines (push model) or process signals from Hub-hosted topics (pull model)
- Validate signal schemas according to protocol requirements during normalization
- Normalize signals to Signal Exchange DTO format
- Forward normalized signals to Signal Exchange

**Multi-Provider Support:**
- Machines can emit signals through multiple providers simultaneously
- Hub does not deduplicate signals from multiple providers
- Each signal is processed independently

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | System-wide service; processes all signals across all subscriptions |
| **Lifecycle** | Always running; managed by platform SRE |
| **Ownership** | Platform-owned; not tenant-configurable |
| **Multiplicity** | Single logical service (distributed implementation) |

---

## Rationale

### Why This Design?

Signal Exchange follows the **observer pattern** and **centralized routing** principles:

1. **Centralized Routing**: All signals flow through SX, ensuring consistent trigger evaluation and request management
2. **Observer Integration**: Subsystems (Notification, Task Management, MS Teams) register as observers rather than being directly coupled
3. **Request-Level Granularity**: SX operates at Request level only — it doesn't route to individual tasks or agents (that's the Application's job)
4. **Decoupled Delivery**: Applications can receive updates via HTTP, Atropos (event bus), or OMS (outbound messaging)

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Direct signal routing to Applications** | No trigger evaluation; no request management |
| **Per-workbench SX instances** | Complexity; cross-workbench coordination issues |
| **Push-only model** | Unreliable; no store-and-forward |
| **SX routing to Tasks/Agents** | Violates separation of concerns; Application owns task management |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0001](../../decision-logs/0001-signal-normalization.md) | Normalize signal format between SPs and SX |
| [ADR-0003](../../decision-logs/0003-signal-exchange-responsibility-boundaries.md) | SX routes to Applications, not tasks or agents |
| [ADR-0019](../../decision-logs/0019-signal-exchange-observer-pattern.md) | Observer pattern for SX module integration |
| [ADR-0020](../../decision-logs/0020-request-level-granularity.md) | SX operates at Request level only |
| [ADR-0026](../../decision-logs/0026-signal-exchange-reminder-capability.md) | Built-in reminder capability |
| [ADR-0103](../../decision-logs/0103-machine-signal-emission.md) | Machine Signal Emission Through Signal Providers |

---

## Structure

### Core Components

```
Signal Exchange
├── Signal Intake
│   └── Receives normalized signals from I/O Gateways
│
├── Trigger Evaluator
│   └── Matches signals against registered triggers
│
├── Request Factory
│   └── Creates new Requests when triggers match
│
├── Application Router
│   └── Routes request updates to Hub Applications
│
├── Response Transformer
│   └── Transforms responses for I/O Gateways
│
├── Flow Controller
│   └── Store-and-forward, retry, deduplication
│
├── Reminder Service
│   └── Time-based reminder scheduling
│
└── Observer Notifier
    └── Broadcasts events to registered observers
```

### Message Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SIGNAL EXCHANGE FLOW                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   I/O Gateway                                                                │
│       │                                                                      │
│       │ Normalized Signal DTO                                                │
│       ▼                                                                      │
│   ┌──────────────┐                                                          │
│   │ Signal       │                                                          │
│   │ Intake       │                                                          │
│   └──────┬───────┘                                                          │
│          │                                                                   │
│          ▼                                                                   │
│   ┌──────────────┐     No Match                                             │
│   │ Trigger      │─────────────────▶ (logged, no action)                    │
│   │ Evaluator    │                                                          │
│   └──────┬───────┘                                                          │
│          │ Match                                                             │
│          ▼                                                                   │
│   ┌──────────────┐                                                          │
│   │ Request      │──────▶ Request Created                                   │
│   │ Factory      │                                                          │
│   └──────┬───────┘                                                          │
│          │                                                                   │
│          ▼                                                                   │
│   ┌──────────────┐              ┌──────────────┐                            │
│   │ Application  │─────────────▶│ Hub          │                            │
│   │ Router       │              │ Application  │                            │
│   └──────────────┘              └──────┬───────┘                            │
│          ▲                             │                                     │
│          │                             │ Request Update                      │
│          └─────────────────────────────┘                                     │
│          │                                                                   │
│          ▼                                                                   │
│   ┌──────────────┐                                                          │
│   │ Observer     │──────▶ Notification Services                             │
│   │ Notifier     │──────▶ Task Management                                   │
│   └──────────────┘──────▶ MS Teams Module                                   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Behavior

### How It Works

**Inbound Flow (Signal → Application):**
```
1. I/O Gateway normalizes protocol-specific signal to DTO
2. SX Signal Intake receives normalized signal
3. Trigger Evaluator matches signal against registered triggers
4. If match: Request Factory creates Request (or correlates to existing)
5. Application Router delivers Request to Hub Application
6. Application processes and returns update
7. Observer Notifier broadcasts to registered observers
```

**Outbound Flow (Application → Signal Provider):**
```
1. Hub Application sends Request Update to SX
2. SX appends update to Request history
3. Observer Notifier broadcasts to observers
4. If Signal Provider registered for updates: SX delivers via configured interface
```

**Reminder Flow:**
```
1. Hub Application sends REMIND request with schedule
2. SX Reminder Service schedules reminder
3. At scheduled time: SX sends REMINDER_NOTIFICATION to Application
4. Application handles reminder (e.g., escalate, take alternate path)
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| I/O Gateways | ← inbound | Receive normalized signals |
| Hub Applications | ↔ bidirectional | Route requests, receive updates |
| Notification Services | → outbound | Observer: request events |
| Task Management | → outbound | Observer: task-relevant events |
| MS Teams Module | → outbound | Observer: collaboration events |
| Workbench Management | ← config | Trigger and Scenario definitions |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Request-level only** | SX doesn't route to tasks or agents — only to Applications |
| **Normalized format** | All incoming signals must use normalized DTO |
| **Idempotent delivery** | Signals with idempotency keys are deduplicated |
| **Ordered per request** | Updates within a request are sequence-numbered |
| **Observer isolation** | Observer failures don't affect core routing |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Single routing point** | Consistent trigger evaluation and request management |
| ✅ **Observer decoupling** | Subsystems integrate without tight coupling |
| ✅ **Reliable delivery** | Store-and-forward with retries |
| ✅ **Audit trail** | All signals and updates logged |
| ✅ **Built-in reminders** | Applications don't need external schedulers |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Single point of failure** | Distributed implementation; high availability |
| ⚠️ **Latency overhead** | Optimized routing; async processing |
| ⚠️ **Complexity** | Clear component separation; extensive logging |

---

## Examples

### Example 1: Dispute Filing Signal

```json
// Normalized Signal DTO from Heracles Gateway
{
  "signal_header": {
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001",
    "signal_id": "sig-12345",
    "signal_type": "dispute.filed",
    "timestamp": "2026-01-06T10:00:00Z"
  },
  "payload": {
    "content_type": "application/json",
    "data": {
      "customer_id": "CUST-001",
      "transaction_id": "TXN-99999",
      "amount": 500.00,
      "reason": "unauthorized_charge"
    }
  }
}
```

### Example 2: Reminder Request

```json
// Application sends REMIND update to SX
{
  "update": { "update_type": "REMIND", "sequence": 10 },
  "payload": {
    "reminder": {
      "reminder_schedule_id": "rem-doc-upload-48h",
      "kind": "document_upload_timeout",
      "schedule": {
        "type": "once",
        "when": "2026-01-08T10:00:00Z"
      },
      "reminder_payload": {
        "content_type": "application/json",
        "data": {
          "message": "Customer has not uploaded documents",
          "task_id": "task-abc"
        }
      }
    }
  }
}
```

---

## Implementation Notes

### For Developers

- Your Hub Application receives Request Updates from SX — not raw signals
- Always include sequence numbers when sending updates
- Use reminders instead of external schedulers for time-based logic
- SX handles deduplication via idempotency keys — provide them for reliability

### For Operators

- Monitor SX health via Olympus Watch
- Check trigger evaluation metrics for misconfigurations
- Observer failures are logged but don't block core flow
- Reminder Service has its own metrics and alerting

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [I/O Gateway](./io-gateway.md) | Sends normalized signals to SX |
| [Hub Application](./hub-application.md) | Receives routed requests from SX |
| [Request Lifecycle](./request-lifecycle.md) | SX manages request state |
| [Normalized Signal Format](./normalized-signal-format.md) | DTO structure SX expects |
| [Observer Pattern](./observer-pattern.md) | How subsystems integrate with SX |
| [Reminder Capability](./reminder-capability.md) | SX built-in time-based stimuli |

---

## References

- [Signal Exchange Subsystem](../../04-subsystems/signal-exchange/README.md)
- [Message Envelope](../../04-subsystems/signal-exchange/message-envelope.md)
- [Trigger Evaluator](../../04-subsystems/signal-exchange/trigger-evaluator.md)
- [ADR-0001: Signal Normalization](../../decision-logs/0001-signal-normalization.md)
- [ADR-0003: Responsibility Boundaries](../../decision-logs/0003-signal-exchange-responsibility-boundaries.md)

