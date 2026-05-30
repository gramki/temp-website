# Session State Machine

Formal specification of the Workspace Session control-plane state machine implemented by Session Management.

## States

| State | Terminal? | User-visible session URL? |
|-------|-----------|---------------------------|
| `created` | No | No |
| `starting` | No | No (may be assigned internally when Infrastructure reports ready, before Active) |
| `active` | No | Yes |
| `unhealthy` | No | Yes (degraded; may fail health checks) |
| `stopping` | No | Yes (draining) |
| `stopped` | No | No (historical URL may be returned for admin UI) |
| `archived` | No | No |
| `deleted` | Yes | No |

## Transition table

| From | To | Trigger | Side effects |
|------|-----|---------|--------------|
| — | `created` | `POST /sessions` accepted | Insert record; emit `session-created` |
| `created` | `starting` | Automatic on create | Call Infrastructure provision; emit `session-starting` |
| `starting` | `active` | Infrastructure `pod-ready` **and** `POST .../ack` within ack deadline | Set `session_url`; start heartbeat clock; emit `session-activated` |
| `starting` | `stopped` | Provision failure or ack deadline missed | Emit `session-stopped` with error metadata; optional cleanup |
| `active` | `unhealthy` | No heartbeat for 60s | Emit `session-unhealthy`; query Infrastructure pod status |
| `unhealthy` | `active` | Heartbeat or re-ack within recovery window (30s additional) | Emit `session-activated` (or silent heal per policy) |
| `unhealthy` | `stopped` | Pod failed or recovery window exhausted | Initiate stop path |
| `active` | `stopping` | Admin stop, idle timeout, max lifetime, heartbeat `command: stop` | Send drain/stop to WO Runtime via heartbeat; emit `session-stopping` |
| `unhealthy` | `stopping` | Admin force-stop | Same as above |
| `stopping` | `stopped` | Shutdown ack + Infrastructure `pod-terminated` | Clear active URL; emit `session-stopped` |
| `stopped` | `starting` | Resume API | Re-provision pod; emit `session-starting` |
| `stopped` | `archived` | `POST .../archive` | Infrastructure archive PVC; emit `session-archived` |
| `archived` | `deleted` | `DELETE ...` or retention job | Infrastructure delete storage; purge record |
| `*` (non-deleted) | `stopping` → … → `deleted` | Admin delete | Force stop if needed; archive optional shortcut |

## Guards (detailed)

### Enter `active`

All must be true:

1. `session_url` populated from Infrastructure callback
2. `POST /api/v1/sessions/{id}/ack` received with valid pod identity
3. Current state is `starting` or `unhealthy` (re-activation)

### Enter `stopping`

Valid sources: `active`, `unhealthy`, `starting` (cancel during provision).

Stop reason recorded in metadata: `user-requested`, `admin-forced`, `idle-timeout`, `max-lifetime`, `provision-cancelled`.

### Enter `stopped`

Requires:

- WO Runtime `POST .../shutdown` **or** stop grace elapsed (default 30s, admin override)
- Infrastructure confirms pod termination

If shutdown reports `pending_tasks > 0`, still transition to `stopped`; metadata carries count for admin visibility (not WO identifiers).

## Timeout policies

### Liveness (WSSM-NFR-0004)

| Parameter | Value |
|-----------|-------|
| Heartbeat expected interval | 15s (WO Runtime obligation) |
| Unhealthy threshold | 60s since last heartbeat |
| Recovery window after unhealthy | 30s additional before forced stop |

On transition to `unhealthy`, Session Management queries Session Infrastructure for pod status via Kubernetes API:

- Pod running, container ready → wait recovery window for re-ack
- Pod `CrashLoopBackOff`, evicted, or missing → transition to `stopping` → `stopped`

### Idle timeout (WSSM-FR-0006)

Configurable per Foundry in Foundry settings (alongside `workspace_infrastructure`):

```yaml
session_management:
  idle_timeout_minutes: 120
  max_lifetime_hours: 24
```

Evaluated on each heartbeat: if `now - last_heartbeat_at > idle_timeout`, set heartbeat response `command: drain` then on next cycle `command: stop`, or transition directly to `stopping` per policy strictness.

### Max lifetime (WSSM-FR-0007)

Evaluated from `created_at`: if exceeded while `active`, transition to `stopping` with reason `max-lifetime`.

### Ack deadline

After Infrastructure `pod-ready`, if no ack within **30s**, transition `starting` → `stopped` (or `unhealthy` → retry once per Foundry policy).

## Side effects by state

| State | Infrastructure | WO Runtime | Message queue |
|-------|----------------|------------|---------------|
| `starting` | `POST` provision | — | `session-starting` |
| `active` | — | Expect heartbeats | `session-activated` |
| `stopping` | Pending terminate | `command: drain` then `stop` on heartbeat | `session-stopping` |
| `stopped` | Pod deleted, PVC retained | No heartbeats | `session-stopped` |
| `archived` | Snapshot + delete PVC | — | `session-archived` |
| `deleted` | Full reclaim | — | (audit only) |

## Concurrency

- One state transition per `session_id` at a time (row-level lock or optimistic versioning with `version` column)
- Heartbeats are idempotent: last-write-wins for `last_heartbeat_at` and resource metrics
- Duplicate Infrastructure `pod-ready` events are ignored if already `active`

## Persistence model (recommended)

| Column | Purpose |
|--------|---------|
| `session_id` | Primary key |
| `foundry_id`, `user_id`, `workspace_type`, `workbench_id` | Composite query key |
| `state` | Current enum |
| `session_url` | Nullable until activation |
| `created_at`, `activated_at`, `stopped_at`, `archived_at` | Lifecycle timestamps |
| `last_heartbeat_at` | Liveness |
| `stop_reason` | Last stop metadata |
| `version` | Optimistic locking |

No `work_order_id` column.

## Read next

- [session-api.md](session-api.md) — HTTP operations that drive transitions
- [interface-contracts.md](interface-contracts.md) — WO Runtime and Infrastructure payloads
- [requirements.md](requirements.md) — requirement IDs
- [../concepts/session-lifecycle.md](../concepts/session-lifecycle.md) — conceptual overview
