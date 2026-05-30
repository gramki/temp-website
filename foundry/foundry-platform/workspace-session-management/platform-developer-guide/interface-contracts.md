# Interface Contracts

API and event schemas between Workspace Session Management and its consumers: Orchestrator, WO Runtime, Session Infrastructure, and Foundry Admin.

Session Management does not define Work Order schemas. Any `active_wos` field is an opaque integer count for observability.

## Orchestrator → Session Management

### Query available sessions

```
GET /api/v1/sessions?user={user-id}&workspace_type={type}&workbench={id}&state=active
```

**Response:**

```yaml
sessions:
  - session_id: string
      session_url: string
      state: "active"
      created_at: ISO8601
      last_heartbeat: ISO8601
```

### Create session

```
POST /api/v1/sessions
```

**Request:**

```yaml
user_id: string
workspace_type: string
workbench_id: string
foundry_id: string
```

**Response:**

```yaml
session_id: string
state: "created"
```

Orchestrator should subscribe to `session-activated` before assigning Work Orders (Orchestrator responsibility, not Session Management).

---

## WO Runtime → Session Management

### Liveness acknowledgment (on boot)

```
POST /api/v1/sessions/{session-id}/ack
```

**Request:**

```yaml
wo_runtime_version: string
pod_ip: string
api_port: 9090
```

**Response:**

```yaml
state: "active"
session_url: string
```

### Heartbeat (every 15s)

```
POST /api/v1/sessions/{session-id}/heartbeat
```

**Request:**

```yaml
active_wos: int
active_agents: int
cpu_usage_pct: float
memory_usage_pct: float
```

**Response:**

```yaml
command: null | "stop" | "drain"
```

Management plane may piggyback stop/drain commands on heartbeat responses.

### Shutdown acknowledgment

```
POST /api/v1/sessions/{session-id}/shutdown
```

**Request:**

```yaml
reason: "user-requested" | "admin-forced" | "idle-timeout" | "max-lifetime" | "drain-complete"
pending_tasks: int
```

**Response:**

```yaml
state: "stopping" | "stopped"
```

---

## Session Management → consumers (message queue)

All session events share this envelope:

```yaml
event:
  type: "session-created" | "session-starting" | "session-activated" | "session-unhealthy" | "session-stopping" | "session-stopped" | "session-archived"
  session_id: string
  foundry_id: string
  user_id: string
  workspace_type: string
  workbench_id: string
  session_url: string | null   # populated from session-activated onward
  timestamp: ISO8601
  metadata: object
```

**Topic:** `foundry.sessions.{foundry_id}` (partition key: `session_id`)

**Consumers:**

| Consumer | Events used |
|----------|-------------|
| Orchestrator | `session-activated`, `session-stopped`, `session-unhealthy` |
| Web console | All (read-only) |
| Metrics | All |

---

## Admin → Session Management

### Force stop

```
POST /api/v1/sessions/{session-id}/stop
```

**Request:**

```yaml
reason: "admin-forced"
grace_period_seconds: int   # default 30
```

### Archive

```
POST /api/v1/sessions/{session-id}/archive
```

No body required. Session must be `stopped` unless implementation supports stop-then-archive.

### List all sessions (admin view)

```
GET /api/v1/admin/sessions?foundry={id}&state=active&page=1&limit=50
```

**Response:**

```yaml
sessions: [...]
page: int
limit: int
total: int
```

---

## Session Management ↔ Session Infrastructure

### Provision request (Session Management → Infrastructure)

```
POST /api/v1/sessions/provision
```

**Request:**

```yaml
session_id: string
user_id: string
workspace_type: "product-specification" | "ux-design" | "development" | "qa" | "release" | "governance"
workbench_id: string
foundry_id: string
```

**Response (synchronous acknowledgment):**

```yaml
status: "accepted" | "failed"
error: string | null
```

Full URL returned asynchronously via event.

### Terminate pod (Session Management → Infrastructure)

```
DELETE /api/v1/sessions/{session-id}/pod
```

Retains PVC per Infrastructure policy.

### Infrastructure → Session Management (events)

**Pod ready:**

```yaml
# Event: session-infrastructure.pod-ready
payload:
  session_id: string
  session_url: string
  pod_ip: string
  node_name: string
  ready_at: ISO8601
```

**Pod failed:**

```yaml
# Event: session-infrastructure.pod-failed
payload:
  session_id: string
  reason: "ImagePullBackOff" | "CrashLoopBackOff" | "Evicted" | "OOMKilled" | "NodeLost"
  message: string
  failed_at: ISO8601
```

**Pod terminated:**

```yaml
# Event: session-infrastructure.pod-terminated
payload:
  session_id: string
  terminated_at: ISO8601
```

**Pod restarting:**

```yaml
# Event: session-infrastructure.pod-restarting
payload:
  session_id: string
  restarted_at: ISO8601
```

---

## Foundry settings (admin configuration)

Session policies are configured in Foundry Definition Repo / Metadata Service:

```yaml
session_management:
  idle_timeout_minutes: 120
  max_lifetime_hours: 24
  allow_multiple_active: false
```

Validated by Management Validation module; read by Session Management at runtime.

## Read next

- [session-api.md](session-api.md) — operational guide to endpoints
- [../../workspace-session-infrastructure/platform-developer-guide/interface-contracts.md](../../workspace-session-infrastructure/platform-developer-guide/interface-contracts.md) — Infrastructure-side mirror (when published)
- [../README.md](../README.md) — module architecture
