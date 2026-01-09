# Request Lifecycle

> **Status:** 🟡 Draft

Request Lifecycle defines the **states, transitions, and update patterns** for Requests as they flow through Operations.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Define request business states and transitions |
| **States** | ACTIVE, PENDING, COMPLETED, CANCELLED |
| **Updates** | From Hub Applications (sync response or async update) |

---

## Request Status vs Message Dispatch

Signal Exchange tracks two distinct concerns:

| Concern | Scope | States |
|---------|-------|--------|
| **Message Dispatch** | Per message (initiation, update) | CREATED → DISPATCHED → ACKNOWLEDGED/FAILED |
| **Request Status** | The request as a whole | ACTIVE → PENDING → COMPLETED/CANCELLED |

> **Note:** Escalation is a **Task** concern, not a Request concern. Tasks within a request's processing flow can be escalated. See [Task Management](../task-management/README.md).

---

## Request Status States

```
[ACTIVE] ←→ [PENDING] → [COMPLETED]
    │                        │
    └────────────────────────┴─→ [CANCELLED]
```

---

## State Definitions

| Status | Description |
|--------|-------------|
| **ACTIVE** | Request is being actively processed by Hub Application |
| **PENDING** | Waiting for external input, event, or human action |
| **COMPLETED** | Request finished (success or failure indicated in response_status) |
| **CANCELLED** | Request terminated without completion |

---

## State Transitions

### Valid Transitions

| From | To | Trigger |
|------|----|---------|
| (initial) | ACTIVE | First message acknowledged by Application |
| ACTIVE | PENDING | Application awaiting input/event |
| PENDING | ACTIVE | Input received, processing resumes |
| ACTIVE | COMPLETED | Application finished processing |
| ACTIVE | CANCELLED | Request terminated |
| PENDING | CANCELLED | Request terminated while waiting |

### Terminal States

- **COMPLETED** — cannot transition further
- **CANCELLED** — cannot transition further

### Lifecycle Cascade (Parent-Child Requests)

When a request has child requests (from same-workbench scenario invocations), terminal state transitions **cascade** to all descendants:

| Parent Transition | Descendant Behavior |
|-------------------|---------------------|
| → `COMPLETED` | All descendants marked `COMPLETED` with reason `PARENT_COMPLETED` |
| → `CANCELLED` | All descendants marked `CANCELLED` with reason `PARENT_CANCELLED` |

Non-terminal transitions (`ACTIVE` ↔ `PENDING`) do **not** cascade.

→ **Details:** [Request Hierarchy](./request-hierarchy.md)

---

## Request Updates

Updates to a Request can come from multiple sources and are delivered via the Signal Exchange.

### Update Sources

| Source | Mechanism | Example |
|--------|-----------|---------|
| **Signal Providers** | New signal → REQUEST_UPDATE message | Customer uploads document |
| **Hub Applications** | ASYNC_UPDATE message | Workflow step completed |
| **Human Agents** | Via Ops Center or task completion | Manager approves action |
| **External Systems** | Callback → signal → update | Payment gateway confirms |

### Update Types

| Type | Description |
|------|-------------|
| **Request Status Change** | Status transition (ACTIVE → PENDING, etc.) |
| **Task Lifecycle** | Task created, assigned, acted upon, completed |
| **Decision** | Decision record with optional evidence reference |
| **Thought** | Reasoning or rationale comment |
| **Memo** | Semi-structured note for future reference |
| **Memory Update** | Subject, Org, or Session memory changes |

---

## Update Type Details

### Task Lifecycle Updates

Captures the full lifecycle of tasks within a request:

| Event | Description |
|-------|-------------|
| **Task Created** | Task created and assigned to a queue |
| **Task Picked** | Agent (human or AI) picked the task |
| **Task Acted** | Action performed on the task |
| **Task Status Change** | Status transition (e.g., In-Progress → Completed) |
| **Task Escalated** | Task elevated to higher authority |

```json
{
  "update_type": "TASK_LIFECYCLE",
  "task": {
    "id": "task-12345",
    "queue_id": "dispute-review-queue",
    "event": "PICKED",
    "agent_id": "agent-67890",
    "agent_type": "human",
    "previous_status": "QUEUED",
    "current_status": "IN_PROGRESS",
    "timestamp": "2026-01-04T10:30:00Z"
  }
}
```

### Decision

A Decision record capturing what was decided, with optional reference to an evidence bundle:

| Field | Description |
|-------|-------------|
| **decision_id** | Unique decision identifier |
| **decision_type** | Type of decision (approval, rejection, classification, etc.) |
| **outcome** | The decision made |
| **rationale** | Explanation for the decision |
| **evidence_ref** | Optional reference to evidence bundle (may be persisted out-of-band) |
| **decidedBy** | Agent who made the decision |

```json
{
  "update_type": "DECISION",
  "decision": {
    "id": "dec-99999",
    "type": "DISPUTE_VALIDITY",
    "outcome": "VALID",
    "rationale": "Documentation supports customer claim",
    "evidence_ref": "evidence://caf/bundles/evb-88888",
    "decided_by": {
      "agent_id": "agent-67890",
      "agent_type": "ai"
    },
    "timestamp": "2026-01-04T10:35:00Z"
  }
}
```

### Thought

A comment by any agent (human or AI) or the system explaining reasoning or rationale:

| Field | Description |
|-------|-------------|
| **thought_id** | Unique thought identifier |
| **author** | Agent or system that authored the thought |
| **content** | The reasoning or rationale text |
| **context** | What the thought relates to (task, decision, action) |

```json
{
  "update_type": "THOUGHT",
  "thought": {
    "id": "thot-77777",
    "author": {
      "agent_id": "seer-agent-01",
      "agent_type": "ai"
    },
    "content": "Customer has a history of valid disputes. Prioritizing based on loyalty tier.",
    "context": {
      "relates_to": "task-12345",
      "context_type": "task_assignment"
    },
    "timestamp": "2026-01-04T10:32:00Z"
  }
}
```

### Memo

A semi-structured or unstructured note meant for future reference. Memos are scoped and have visibility restrictions.

| Field | Description |
|-------|-------------|
| **memo_id** | Unique memo identifier |
| **scope** | Target scope: `request`, `subject`, or `object` |
| **scope_id** | ID of the scoped entity |
| **content** | The memo content |
| **visibility** | Access restrictions |
| **retention** | Retention policy |

**Scope Types:**
- **Request** — Memo associated with this specific request
- **Subject** — Memo associated with the subject (e.g., customer) of the request
- **Object** — Memo associated with the object (e.g., account, transaction) of the request

**Visibility Levels:**
- **Author** — Only visible to the memo author
- **Team** — Visible to agents working on this request
- **Role** — Visible to agents with specified roles

```json
{
  "update_type": "MEMO",
  "memo": {
    "id": "memo-66666",
    "scope": "subject",
    "scope_id": "customer-12345",
    "author": {
      "agent_id": "human-agent-99",
      "agent_type": "human"
    },
    "content": {
      "title": "Preferred Resolution Method",
      "body": "Customer prefers phone callbacks over email. Best times: 2-4 PM EST.",
      "tags": ["preference", "contact"]
    },
    "visibility": {
      "level": "role",
      "roles": ["dispute_agent", "customer_service"]
    },
    "retention": {
      "policy": "subject_lifetime",
      "expires_at": null
    },
    "timestamp": "2026-01-04T10:40:00Z"
  }
}
```

> **Note:** Memos are NOT Memory Updates. Memo retention and access follows different semantics. Memos are request-context notes; Memory Updates are persistent knowledge.

### Memory Update

Updates to persistent memory stores. Applies to Subject Memory, Org Memory, and Session Memory (NOT Agent Memory).

| Memory Type | Description |
|-------------|-------------|
| **Subject Memory** | Preferences and context about the subject (customer) |
| **Org Memory** | Organizational knowledge and institutional learning |
| **Session Memory** | Session-scoped context for the current interaction |

> **Agent Memory** is managed by Seer's Context Assembly Engine, not through Request updates.

```json
{
  "update_type": "MEMORY_UPDATE",
  "memory": {
    "type": "subject",
    "subject_id": "customer-12345",
    "operation": "upsert",
    "entries": [
      {
        "key": "preferred_contact_method",
        "value": "phone",
        "source": "request-12345",
        "confidence": 0.95
      },
      {
        "key": "dispute_history_summary",
        "value": "3 disputes in 2 years, all resolved favorably",
        "source": "request-12345"
      }
    ],
    "timestamp": "2026-01-04T10:45:00Z"
  }
}
```

---

## Memo vs Memory: Key Differences

| Aspect | Memo | Memory Update |
|--------|------|---------------|
| **Purpose** | Note for future reference in context | Persistent knowledge/preference |
| **Retention** | Request/subject/object lifetime, policy-based | Long-term persistence |
| **Access** | Visibility restrictions (author, team, role) | Based on memory type and scope |
| **Structure** | Semi-structured, free-form allowed | Structured key-value or semantic |
| **Scope** | Request, Subject, or Object | Subject, Org, or Session |
| **Use Case** | "Remember this for later in this case" | "This is a learned preference" |

---

## Request as Session Boundary

The request defines a session boundary for:
- Scope storage (request-local data)
- Agent memory scope
- Audit trail
- Participant context

---

## Trigger Updates

From Todo notes:
> *"Trigger can update Applications; I/O Gateway for MS Teams -> Signals -> Trigger -> (New Case or Action in an existing Case)"*

Triggers can:
- Create new requests
- Update existing requests
- Add actions to existing operations

---

## Hub Tracking

From Todo notes:
> *"Hub tracks the complete request lifecycle"*

Hub maintains:
- Full state history
- All updates with timestamps
- Participant actions
- Linked entities and decisions

---

## Integration with Signal Exchange

Signal Exchange is responsible for:
1. Tracking message dispatch state (per message)
2. Tracking request status (per request)
3. Dispatching observer notifications on status changes

See [Signal Exchange Message Envelope](../signal-exchange/message-envelope.md) for envelope structure.

---

## Related Documentation

- [Request Management Overview](./README.md)
- [Request Hierarchy](./request-hierarchy.md) — Parent-child requests, context inheritance, lifecycle cascade
- [Request Storage](./request-storage.md)
- [Signal Exchange - Message Envelope](../signal-exchange/message-envelope.md)
- [Signal Exchange - Observer Notifications](../signal-exchange/observer-notifications.md)
- [Task Management](../task-management/README.md) — Task states including escalation

---

*TODO: Detailed design — event sourcing, history retention, status change policies*

