# Request Update

> **Category:** Request and Task

---

## Overview

A **Request Update** is an append-only entry in a Request's history that captures state changes, decisions, memos, and outcomes. Updates form the complete audit trail of a Request, enabling full reconstruction of what happened, when, and why.

---

## Ontology Context

### Relationship to Ontology

The ontology describes **Operation** as a runtime instance of work. Request Updates are the implementation of how operation state accumulates over time.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Operation state | Request Update | Updates capture state changes |
| (not covered) | Append-only history | Immutable audit trail |

### Gap This Fills

The ontology focuses on concepts. Request Update specifies:
1. **Update structure**: What does an update contain?
2. **Immutability**: How is audit trail preserved?
3. **Sequencing**: How are updates ordered?
4. **Types**: What kinds of updates exist?

---

## Definition

**Request Update** is an immutable record containing:
- Sequence number within the Request
- Update type and timestamp
- Payload with update-specific content
- Actor who created the update
- Optional status change

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Request-scoped; part of single Request |
| **Lifecycle** | Created on action; immutable thereafter |
| **Ownership** | Created by SX, applications, agents, or system |
| **Multiplicity** | Many updates per Request |

---

## Rationale

### Why This Design?

Append-only updates enable:
1. **Complete audit trail**: Nothing can be deleted or modified
2. **Event sourcing**: Reconstruct state at any point
3. **Compliance**: Full history for regulators
4. **Debugging**: See exactly what happened

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Mutable state only** | No history; no audit trail |
| **Overwrite updates** | Lost information; compliance issues |
| **External audit log** | Disconnected; sync issues |

---

## Structure

### Update Schema

```json
{
  "sequence": 5,
  "timestamp": "2026-01-06T10:30:00Z",
  "update_type": "APPLICATION_UPDATE",
  
  "actor": {
    "type": "application",           // application | agent | system | signal
    "id": "dispute-handler",
    "name": "Dispute Handler"
  },
  
  "status_change": {                  // Optional: if status changed
    "from": "CREATED",
    "to": "IN_PROGRESS",
    "reason": "Investigation started"
  },
  
  "payload": {
    "content_type": "application/json",
    "semantic_type": "com.hub.TaskCreated",
    "data": {
      "action": "task_created",
      "task_id": "task-001",
      "task_type": "investigate",
      "assignee": "agent-bob"
    }
  },
  
  "metadata": {
    "trace_id": "trace-xyz",
    "envelope_id": "env-123"
  }
}
```

### Update Types

| Type | Source | Purpose |
|------|--------|---------|
| **REQUEST_CREATED** | System | Initial request creation |
| **SIGNAL_RECEIVED** | Signal | External signal correlated to request |
| **APPLICATION_UPDATE** | Application | App processing result |
| **TASK_CREATED** | Application | Task delegated to agent |
| **TASK_COMPLETED** | Task Management | Task finished |
| **TASK_ESCALATED** | Task Management | Task escalated |
| **MEMO** | Agent/Application | Note or observation |
| **THOUGHT** | Agent | AI agent reasoning |
| **DECISION** | Application | Decision recorded |
| **COMPLETED** | Application | Request completed |
| **CANCELLED** | Agent/System | Request cancelled |
| **REMINDER_SET** | Application | Reminder scheduled |
| **REMINDER_TRIGGERED** | System | Reminder fired |
| **AUTHORITY_REQUEST** | Agent (Sidecar) | Agent requests delegation authority |
| **AUTHORITY_GRANTED** | Channel | Delegation granted, certificate attached |
| **AUTHORITY_DENIED** | Channel | Delegation denied or timeout |

### Delegation Update Types

The delegation-related update types enable request-scoped authority delegation:

| Update | Payload | Flow |
|--------|---------|------|
| **AUTHORITY_REQUEST** | `template`, `reason`, `timeout` | Agent → SX → Channel observers |
| **AUTHORITY_GRANTED** | `certificate_id`, `delegator`, `expires_at` | Channel → SX → Agent |
| **AUTHORITY_DENIED** | `reason` (user_denied/timeout) | Channel → SX → Agent |

These follow the REMIND pattern — updates are routed through Signal Exchange to observer modules (Channels), which handle user interaction and respond with grant/deny.

→ See [Request-Scoped Delegation](./request-scoped-delegation.md) for details.

---

## Behavior

### How Updates Accumulate

```
Request created (seq 1)
    │
    ├── Signal received → Update (seq 2)
    │
    ├── App processes → Update (seq 3)
    │
    ├── Task created → Update (seq 4)
    │
    ├── Agent adds memo → Update (seq 5)
    │
    ├── Task completed → Update (seq 6)
    │
    ├── Another signal → Update (seq 7)
    │
    └── Request completed → Update (seq 8)
```

### Sequence Guarantees

```
Sequence invariants:
├── Starts at 1
├── Monotonically increasing
├── No gaps (1, 2, 3... not 1, 3, 4)
├── Assigned by SX on receipt
└── Concurrent updates get ordered sequence
```

### Actor Types

| Actor Type | Examples |
|------------|----------|
| **application** | Hub Application processing request |
| **agent** | Human or AI agent working on task |
| **system** | Platform (SX, Task Management) |
| **signal** | External signal provider |

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Request | ↑ belongs to | Updates are part of Request |
| Signal Exchange | ← created by | SX assigns sequence, stores |
| Hub Application | ← created by | Apps send updates |
| Agent | ← created by | Agents add memos, complete tasks |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Immutable** | Updates cannot be modified after creation |
| **Append-only** | Updates cannot be deleted |
| **Sequenced** | Every update has unique sequence number |
| **Timestamped** | Every update has creation timestamp |
| **Typed** | Every update has known type |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Complete history** | Nothing lost |
| ✅ **Audit compliance** | Regulator-friendly |
| ✅ **Debuggable** | Full trace of events |
| ✅ **Reconstructable** | State at any point in time |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Storage growth** | Archival policies for completed requests |
| ⚠️ **Query complexity** | Indexed current state view |

---

## Examples

### Example 1: Complete Request History

```json
{
  "request_id": "req-dispute-001",
  "updates": [
    {
      "sequence": 1,
      "update_type": "REQUEST_CREATED",
      "actor": { "type": "signal", "id": "core-banking" },
      "payload": { "data": { "amount": 500, "reason": "unauthorized" } }
    },
    {
      "sequence": 2,
      "update_type": "APPLICATION_UPDATE",
      "actor": { "type": "application", "id": "dispute-handler" },
      "status_change": { "to": "IN_PROGRESS" },
      "payload": { "data": { "action": "processing_started" } }
    },
    {
      "sequence": 3,
      "update_type": "TASK_CREATED",
      "actor": { "type": "application", "id": "dispute-handler" },
      "payload": { "data": { "task_id": "task-001", "type": "investigate" } }
    },
    {
      "sequence": 4,
      "update_type": "MEMO",
      "actor": { "type": "agent", "id": "agent-bob" },
      "payload": { "data": { "note": "Reviewed transaction history" } }
    },
    {
      "sequence": 5,
      "update_type": "TASK_COMPLETED",
      "actor": { "type": "agent", "id": "agent-bob" },
      "payload": { "data": { "outcome": "charge_is_unauthorized" } }
    },
    {
      "sequence": 6,
      "update_type": "COMPLETED",
      "actor": { "type": "application", "id": "dispute-handler" },
      "status_change": { "to": "COMPLETED" },
      "payload": { "data": { "resolution": "refund_issued" } }
    }
  ]
}
```

---

## Implementation Notes

### For Developers

- Include meaningful payload data for debugging
- Use appropriate update_type for clarity
- Include actor information consistently
- Add semantic_type for domain-specific typing

### For Operators

- Monitor update volume per request
- Archive completed request updates per policy
- Index updates for efficient queries

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Request Lifecycle](./request-lifecycle.md) | Updates drive Request state |
| [Message Envelope](./message-envelope.md) | Envelopes become updates |
| [Signal Exchange](./signal-exchange.md) | SX manages updates |

---

## References

- [Request Management Subsystem](../../04-subsystems/request-management/README.md)
- [Request Lifecycle](../../04-subsystems/request-management/request-lifecycle.md)

