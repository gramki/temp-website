# Session API

REST API for Workspace Session lifecycle. Base path: `/api/v1`. All requests require Foundry-scoped authentication; `foundry_id` is taken from the token or explicit parameter on admin routes.

Session Management does not expose Work Order endpoints.

## Orchestrator and builder APIs

### Create session

```
POST /api/v1/sessions
```

**Request:**

```yaml
user_id: string
workspace_type: string    # product-specification | ux-design | development | qa | release | governance
workbench_id: string
foundry_id: string
instance_id: string | null  # optional, for multi-session mode
```

**Response (201):**

```yaml
session_id: string
state: "created" | "starting"   # may advance synchronously to starting
```

**Behavior:**

1. Persist record (`created`)
2. Emit `session-created`
3. Transition to `starting`, call Session Infrastructure provision
4. Emit `session-starting`

Idempotency: optional header `Idempotency-Key` for safe retries.

### Query sessions

```
GET /api/v1/sessions?user={user-id}&workspace_type={type}&workbench={id}&state={state}
```

**Response:**

```yaml
sessions:
  - session_id: string
    session_url: string | null
    state: string
    created_at: ISO8601
    last_heartbeat: ISO8601 | null
    workbench_id: string
    workspace_type: string
```

**Filters:**

| Parameter | Description |
|-----------|-------------|
| `user` | Required for builder-scoped queries |
| `workspace_type` | Optional |
| `workbench` | Optional |
| `state` | Optional (`active`, `stopped`, etc.) |
| `foundry_id` | From auth context |

**Performance:** WSSM-NFR-0001 — p95 under 200ms for typical Foundry session counts.

### Get session

```
GET /api/v1/sessions/{session-id}
```

Returns full session record including state, URLs, timestamps, and last heartbeat metrics summary (counts only, no WO IDs).

### Stop session (orchestrator / user)

```
POST /api/v1/sessions/{session-id}/stop
```

**Request:**

```yaml
reason: "user-requested" | "admin-forced" | "idle-timeout" | "max-lifetime"
grace_period_seconds: int   # default 30
```

Transitions `active` or `unhealthy` → `stopping`. See state machine for completion.

## WO Runtime APIs (in-pod)

Called from the session pod over HTTPS to the management-plane endpoint (cluster-external).

### Liveness acknowledgment

```
POST /api/v1/sessions/{session-id}/ack
```

**Request:**

```yaml
wo_runtime_version: string
pod_ip: string
api_port: int    # default 9090
```

**Response:**

```yaml
state: "active"
session_url: string
```

Transitions `starting` → `active` when Infrastructure has already reported pod ready.

### Heartbeat

```
POST /api/v1/sessions/{session-id}/heartbeat
```

**Request:**

```yaml
active_wos: int          # count only
active_agents: int
cpu_usage_pct: float
memory_usage_pct: float
```

**Response:**

```yaml
command: null | "stop" | "drain"
```

**Interval:** every 15s while Active (WOR obligation).

Session Management updates `last_heartbeat_at` and evaluates idle/max-lifetime policies. Piggyback `command` to avoid separate push channel.

**Throughput:** WSSM-NFR-0005 — sustain 1000 heartbeats/second per Foundry.

### Shutdown acknowledgment

```
POST /api/v1/sessions/{session-id}/shutdown
```

**Request:**

```yaml
reason: "user-requested" | "admin-forced" | "idle-timeout" | "max-lifetime" | "drain-complete"
pending_tasks: int
```

Called after drain completes. Allows `stopping` → `stopped` once Infrastructure confirms pod termination.

## Admin APIs

### Force stop

```
POST /api/v1/sessions/{session-id}/stop
```

Same as builder stop with `reason: admin-forced` and configurable `grace_period_seconds`.

### Archive

```
POST /api/v1/sessions/{session-id}/archive
```

Requires `stopped` (or triggers stop-then-archive). Transitions to `archived`; delegates PVC snapshot to Infrastructure.

### Delete

```
DELETE /api/v1/sessions/{session-id}
```

Terminal cleanup: `archived` → `deleted` or forced path from lower states.

### List sessions (admin)

```
GET /api/v1/admin/sessions?foundry={id}&state={state}&user={id}&page=1&limit=50
```

Paginated admin view across users and workbenches.

## Event publication contract

Every successful state transition commits to the database, then publishes to the session topic via outbox:

| Transition | Event type |
|------------|------------|
| → created | `session-created` |
| → starting | `session-starting` |
| → active | `session-activated` |
| → unhealthy | `session-unhealthy` |
| → stopping | `session-stopping` |
| → stopped | `session-stopped` |
| → archived | `session-archived` |

Envelope: [interface-contracts.md](interface-contracts.md).

**Latency:** WSSM-NFR-0002 — under 500ms from DB commit to message availability.

## Error responses

| Code | Condition |
|------|-----------|
| 404 | Unknown `session-id` |
| 409 | Invalid state transition (e.g. archive while active) |
| 422 | Missing required fields |
| 503 | Infrastructure provision unavailable (retryable) |

## Authentication

| Caller | Auth model |
|--------|------------|
| Orchestrator | Service account; Foundry scope |
| WO Runtime | Session bootstrap token injected by Infrastructure at pod start |
| Admin | Foundry admin role |

## Read next

- [interface-contracts.md](interface-contracts.md) — full YAML schemas
- [session-state-machine.md](session-state-machine.md) — transition rules
- [requirements.md](requirements.md) — WSSM-FR/NFR mapping
