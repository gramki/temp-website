# Session Events

Session events are the management-plane notification stream for Workspace Session lifecycle. Every state transition in Session Management produces an event so downstream modules — especially Orchestrator — can react without polling the session API.

Session Management publishes events; it does not consume Work Order events. The event stream is session-scoped only.

## Event types

| Event | Emitted when | Typical consumers |
|-------|--------------|-------------------|
| `session-created` | Record persisted (state: Created) | Audit, observability |
| `session-starting` | Provision request issued (state: Starting) | Observability |
| `session-activated` | Transition to Active (URL + liveness ack) | **Orchestrator** (WO assignment), web console |
| `session-unhealthy` | Transition to Unhealthy | Orchestrator (hold assignment), alerting |
| `session-stopping` | Transition to Stopping | Observability |
| `session-stopped` | Transition to Stopped | Orchestrator, admin dashboards |
| `session-archived` | Transition to Archived | Retention workflows |

There is no `session-deleted` event in the standard stream: deletion is terminal and may be modeled as `session-stopped` with `metadata.deleted: true` or a separate admin-only audit channel. Implementations may add `session-deleted` if audit requirements demand it.

## Event envelope

All session events share one envelope schema (see [../platform-developer-guide/interface-contracts.md](../platform-developer-guide/interface-contracts.md)):

```yaml
event:
  type: string          # one of the types above
  session_id: string
  foundry_id: string
  user_id: string
  workspace_type: string
  workbench_id: string
  session_url: string | null   # from session-activated onward
  timestamp: ISO8601
  metadata: object             # transition-specific (reason, error, policy)
```

**Metadata examples:**

| Event | Typical metadata |
|-------|------------------|
| `session-starting` | `{ "provision_request_id": "..." }` |
| `session-activated` | `{ "wo_runtime_version": "...", "pod_ip": "..." }` |
| `session-unhealthy` | `{ "reason": "liveness-timeout", "last_heartbeat": "..." }` |
| `session-stopping` | `{ "reason": "admin-forced" | "idle-timeout" | "max-lifetime" }` |
| `session-stopped` | `{ "pending_tasks": 0 }` — opaque count from WO Runtime shutdown ack; not WO IDs |
| `session-archived` | `{ "archive_policy": "manual" | "scheduled" }` |

## Consumers

### Orchestrator

Orchestrator is the primary consumer for coordination:

- Subscribes to `session-activated` before assigning Work Orders to a newly created session
- May treat `session-unhealthy` and `session-stopped` as signals to pause or cancel pending assignment (WO logic stays in Orchestrator)

Session Management does not wait for Orchestrator acknowledgment of events.

### WO Runtime

WO Runtime does not consume session events. It uses the session API (ack, heartbeat, shutdown). Events are for management-plane and Orchestrator subscribers.

### Foundry admin / observability

Admin dashboards and metrics pipelines subscribe to the full event stream for session counts, failure rates, and policy triggers.

## Delivery semantics

| Property | Guarantee |
|----------|-----------|
| **Ordering per session** | Events for a given `session_id` are published in state-machine order |
| **Cross-session ordering** | Not guaranteed |
| **At-least-once delivery** | Yes; consumers must be idempotent |
| **Latency** | Target under 500ms from state commit (WSSM-NFR-0002) |
| **Durability** | Events written to the message queue after DB commit (outbox pattern recommended) |

Duplicate delivery may occur on retry. Consumers should key idempotency on `(session_id, type, timestamp)` or a monotonic `sequence` field if added to metadata.

## Infrastructure events (inbound)

Session Management also **consumes** infrastructure events from Session Infrastructure (not published on the public session topic):

| Infrastructure event | Session Management action |
|------------------------|---------------------------|
| `session-infrastructure.pod-ready` | Store URL; wait for WO Runtime ack |
| `session-infrastructure.pod-failed` | Fail or Unhealthy → Stopped depending on state |
| `session-infrastructure.pod-restarting` | Extend liveness window if Active |
| `session-infrastructure.pod-terminated` | Confirm Stopping → Stopped |

These are internal integration events; they do not replace the public `session-*` envelope for platform consumers.

## Read next

- [session-lifecycle.md](session-lifecycle.md) — which transitions emit which events
- [../platform-developer-guide/interface-contracts.md](../platform-developer-guide/interface-contracts.md) — full schemas
- [../platform-developer-guide/session-api.md](../platform-developer-guide/session-api.md) — REST API alongside events
