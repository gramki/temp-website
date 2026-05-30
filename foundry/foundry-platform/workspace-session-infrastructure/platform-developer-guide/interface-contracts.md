# Interface Contracts

API and event schemas between Workspace Session Infrastructure and Session Management.

Session Infrastructure does not expose APIs to Orchestrator or WO Runtime directly. All consumers interact through Session Management except WO Runtime's health endpoint (Kubernetes probe) and management-plane HTTPS endpoints.

## Session Management → Session Infrastructure

### Provision request

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
pod_name: string | null        # set when accepted
namespace: string | null
error: string | null
```

Full session URL is returned asynchronously via event when pod readiness probe passes.

### Terminate pod

```
DELETE /api/v1/sessions/{session-id}/pod
```

Retains PVC. Init containers re-run on next start.

**Response:**

```yaml
status: "terminating" | "not_found"
```

### Archive storage

```
POST /api/v1/sessions/{session-id}/archive-storage
```

Triggers volume snapshot and PVC deletion (WSI-FR-0010).

**Response:**

```yaml
status: "archiving" | "archived" | "failed"
snapshot_name: string | null
error: string | null
```

### Query pod status

```
GET /api/v1/sessions/{session-id}/pod
```

Used by Session Management during unhealthy recovery.

**Response:**

```yaml
session_id: string
pod_name: string
namespace: string
phase: "Pending" | "Running" | "Succeeded" | "Failed" | "Unknown"
ready: boolean
container_state: "running" | "waiting" | "terminated"
restart_count: int
node_name: string | null
```

---

## Session Infrastructure → Session Management (events)

Events are published to the message queue topic `foundry.session-infrastructure.{foundry_id}` (partition key: `session_id`).

### Pod ready

```yaml
# Event: session-infrastructure.pod-ready
payload:
  session_id: string
  session_url: string          # https://{session-id}.sessions.{ingress-domain}
  pod_ip: string
  node_name: string
  ready_at: ISO8601
```

Session Management stores the URL and waits for WO Runtime liveness ack before transitioning to Active.

### Pod failed

```yaml
# Event: session-infrastructure.pod-failed
payload:
  session_id: string
  reason: "ImagePullBackOff" | "CrashLoopBackOff" | "Evicted" | "OOMKilled" | "NodeLost" | "ProvisionTimeout" | "StoragePending"
  message: string
  failed_at: ISO8601
```

### Pod terminated

```yaml
# Event: session-infrastructure.pod-terminated
payload:
  session_id: string
  terminated_at: ISO8601
```

Emitted after graceful or forced pod deletion on stop.

### Pod restarting

```yaml
# Event: session-infrastructure.pod-restarting
payload:
  session_id: string
  restart_count: int
  restarted_at: ISO8601
```

Emitted when K8s restarts a pod (crash, OOM). Session Management resets liveness timeout clock.

### Storage archived

```yaml
# Event: session-infrastructure.storage-archived
payload:
  session_id: string
  snapshot_name: string
  archived_at: ISO8601
```

---

## Metadata Service (read-only)

Session Infrastructure reads Foundry configuration at provision time:

```
GET /api/v1/foundries/{foundry-id}/settings/workspace_infrastructure
```

**Response:** See [foundry-management-integration.md](foundry-management-integration.md) for schema.

Configuration is cached per Foundry with invalidation on Metadata Service change events.

---

## Indirect interfaces

Session Infrastructure does not call these directly but the session pod depends on them:

| Consumer | Interface | Purpose |
|----------|-----------|---------|
| WO Runtime | `GET /health:9090` | Kubernetes readiness/liveness probes |
| WO Runtime | Session Management ack/heartbeat | Liveness protocol (in-pod, not WSI) |
| Coder | REST API | Workspace create/stop |
| Kubernetes | API server | Pod, PVC, Service, NetworkPolicy CRUD |

---

## Error handling

| HTTP status | Meaning | Session Management action |
|-------------|---------|--------------------------|
| 202 Accepted | Provision queued | Transition to Starting |
| 400 Bad Request | Invalid workspace type or missing foundry config | Mark Failed |
| 409 Conflict | Pod already exists for session | Query status |
| 503 Service Unavailable | Cluster unreachable | Retry with backoff |
| 507 Insufficient Storage | Quota or StorageClass failure | Mark Failed; alert admin |

---

## Read next

- [../../workspace-session-management/platform-developer-guide/interface-contracts.md](../../workspace-session-management/platform-developer-guide/interface-contracts.md) — Session Management-side mirror
- [sequence-diagrams.md](sequence-diagrams.md) — End-to-end flows
- [failure-modes.md](failure-modes.md) — Failure recovery per event type
