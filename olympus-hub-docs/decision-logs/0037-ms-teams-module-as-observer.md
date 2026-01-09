# ADR-0037: MS Teams Module as Signal Exchange Observer

| Property       | Value                                           |
|----------------|-------------------------------------------------|
| **Status**     | Accepted                                        |
| **Date**       | 2026-01-06                                      |
| **Category**   | Integration                                     |
| **Deciders**   | Architecture Team                               |
| **Supersedes** | -                                               |

---

## Context

When Hub Applications update Requests (task assignments, status changes, decisions), the MS Teams module needs to be informed so it can:
- Add new assignees to chat groups
- Post update notifications
- Relay status changes

The question is: How should Signal Exchange notify the MS Teams module of these updates?

Options include:
1. Direct integration between Signal Exchange and MS Teams module
2. MS Teams module as a registered observer of Signal Exchange
3. Hub Application notifies MS Teams directly

---

## Decision

**The MS Teams module registers as an observer with Signal Exchange. Signal Exchange dispatches Request Updates to all registered observers (including MS Teams module). Signal Exchange operates at the Request level — it cannot direct updates to specific tasks or agents. The MS Teams module, as an observer, parses updates to determine which agents are affected.**

### Key Principles

1. **Signal Exchange dispatches to observers** — Not to agents or tasks directly
2. **Request-level granularity** — SX sends Request Updates, not agent-specific notifications
3. **Observer responsibility** — Each observer (like MS Teams) determines its own downstream actions
4. **Uniform pattern** — Same observer model for all interested modules

### Flow

```
Hub Application
       │
       │ Request Update (contains task/agent info)
       ▼
Signal Exchange
       │
       │ Dispatch to registered observers
       │ (Request-level, not agent/task-level)
       │
       ├─────────────────────┬──────────────────────────────
       │                     │
       ▼                     ▼
MS Teams Module         Other Observers
       │                 (Notification Service,
       │                  WebSocket, Webhook)
       │
       │ Parse update, determine affected agents
       ▼
Chat Group Actions
(Add members, post messages)
```

---

## Alternatives Considered

### 1. Direct Signal Exchange → MS Teams Integration

Signal Exchange has specific logic to notify MS Teams module.

**Rejected because:**
- Creates tight coupling between SX and Teams
- Each channel would need special handling
- Violates uniform observer pattern
- Harder to add new channels

### 2. Hub Application → MS Teams Directly

Applications notify MS Teams module themselves.

**Rejected because:**
- Every Hub Application needs Teams awareness
- Duplicates notification logic across applications
- Applications shouldn't know about channels
- Inconsistent behavior across applications

### 3. Task-Level Dispatch from Signal Exchange

Signal Exchange dispatches updates at task/agent granularity.

**Rejected because:**
- SX would need to understand task and agent models
- Increases SX complexity and coupling
- Different observers need different granularities
- Better for observers to handle their own logic

---

## Consequences

### Positive

1. **Loose coupling** — SX doesn't know about Teams specifics
2. **Uniform pattern** — All observers work the same way
3. **Extensible** — New channels just register as observers
4. **Clear responsibility** — Observer handles downstream logic
5. **Request-level simplicity** — SX stays focused on Requests

### Negative

1. **Observer parsing** — Each observer must parse update to extract relevant info
2. **Potential duplication** — Multiple observers may do similar parsing
3. **Agent determination** — Observer must map Request updates to affected agents
4. **All observers get all updates** — May receive updates they don't care about

### Risks

1. **Performance** — Many observers × many updates = high dispatch volume
2. **Filtering** — Observers need efficient filtering for relevant updates
3. **Consistency** — Different observers may interpret same update differently

---

## Implementation Notes

### Observer Registration

MS Teams module registers as an observer for:
- Scenarios with Teams integration enabled
- Specific update types (TASK_LIFECYCLE, DECISION, STATUS_CHANGE, etc.)

### Update Parsing

When MS Teams module receives a Request Update:
1. Extract update type and content
2. Determine affected agents (e.g., task assignee from TASK_LIFECYCLE)
3. Take appropriate action:
   - Add new assignees to chat group via Graph API
   - Post notification message
   - Update chat group metadata

### Multi-Channel Awareness

Agents in the Teams chat group may receive the same update through multiple channels (Teams + email + push). This is by design — channels are not mutually exclusive.

---

## Related Decisions

- [ADR-0019: Signal Exchange Observer Pattern](./0019-signal-exchange-observer-pattern.md)
- [ADR-0020: Request-Level Granularity](./0020-request-level-granularity.md)
- [ADR-0033: Chat Groups as Collaboration Surfaces](./0033-chat-groups-as-collaboration-surfaces.md)

