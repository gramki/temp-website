# Storage

PersistentVolumeClaims for workspace persistence, ephemeral volumes for merge output, and volume lifecycle tied to session state.

## Volume model

Each session pod mounts three volumes:

| Volume | Type | Mount path | Lifecycle | Purpose |
|--------|------|------------|-----------|---------|
| `workspace-data` | PVC (ReadWriteOnce) | `/workspace` | Retained on stop; reclaimed on archive/delete | Git checkouts, build artifacts, local state |
| `merged-content` | emptyDir | `/workspace/.foundry` | Recreated every start | Workshop/Workbench merge output + admin overlay |
| `skill-cache` | emptyDir | `/opt/foundry/skills` | Recreated every start | Installed skills from Skill Registry |

The PVC is the only persistent storage. Init container output and skill cache are ephemeral — re-applied on every pod start.

## PVC specification

**WSI-FR-0009:** Session Infrastructure provisions a PVC per session and binds it to the pod on start.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: "pvc-session-{session-id}"
  namespace: "foundry-{foundry-id}-sessions"
  labels:
    foundry.io/session-id: "{session-id}"
    foundry.io/foundry-id: "{foundry-id}"
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: "{storage_class}"   # from workspace_infrastructure.kubernetes.storage_class
  resources:
    requests:
      storage: "20Gi"                   # default; configurable per Foundry (WSI-NFR-0006)
```

Foundry admin configures `storage_class` and `resource_defaults.storage_size` in Foundry settings. Validation module verifies the StorageClass exists before merge.

## Session state vs storage

| Session state | Pod | PVC | Snapshot |
|---------------|-----|-----|----------|
| **Starting** | Creating | Binding or rebinding | — |
| **Active** | Running | Bound to pod | — |
| **Stopping** | Terminating | Retained, unbound | — |
| **Stopped** | Deleted | Retained (unbound) | — |
| **Archived** | Deleted | Deleted after snapshot | Read-only snapshot retained |
| **Deleted** | — | Deleted | Snapshot deleted |

### Active

PVC is bound to the running pod. All user workspace files persist under `/workspace`.

### Stopped

Stop deletes the pod but **retains the PVC**. Resume creates a new pod with the same `claimName`; Kubernetes rebinds the existing PVC. Init containers re-run to refresh merge content and admin overlay.

### Archived

**WSI-FR-0010:** On archive, Session Infrastructure takes a volume snapshot, then deletes the PVC.

```
Archive request (Session Management → Session Infrastructure)
    │
    ├── Create VolumeSnapshot: snap-session-{session-id}
    │
    ├── Wait for snapshot Ready
    │
    ├── Delete PVC pvc-session-{session-id}
    │
    └── Emit session-infrastructure.storage-archived
```

Archived sessions expose read-only access via snapshot restore into a temporary pod (admin tooling — not automatic session resume).

### Deleted

Snapshot and PVC are both deleted. No recovery path.

## PVC naming and binding

PVC name is deterministic: `pvc-session-{session-id}`. One PVC per session for the lifetime of the session record.

| Scenario | Behavior |
|----------|----------|
| First start | Create PVC, bind to new pod |
| Stop | Delete pod; PVC remains |
| Resume | New pod, same PVC claimName |
| Crash restart | Same pod restarts; PVC stays bound |
| Archive | Snapshot → delete PVC |
| Provision failure (Pending) | Emit `pod-failed`; session cannot start until storage available |

ReadWriteOnce means a PVC can bind to only one pod at a time. Stop must complete pod deletion before resume can rebind.

## Ephemeral volumes

### merged-content

Written by init containers:

1. `workspace-merge` — Workshop/Workbench content, devcontainer config, scenarios
2. `admin-overlay` — Foundry admin additions from `workspace-infrastructure/<workspace>/`

Mounted read-only into the main container at `/workspace/.foundry`. Not stored on PVC — ensures Workshop and admin changes take effect on every start without stale overlay state.

### skill-cache

Populated by `workspace-merge` init container from Skill Registry. WO Runtime reads installed skills from `/opt/foundry/skills`. Recreated on every start to pick up skill version updates.

## Storage quotas

**WSI-NFR-0007:** Concurrent sessions per Foundry are limited by namespace ResourceQuota, including total storage:

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: session-storage-quota
  namespace: foundry-{foundry-id}-sessions
spec:
  hard:
    persistentvolumeclaims: "50"        # max concurrent session PVCs
    requests.storage: "1000Gi"          # total storage across all PVCs
```

Per-session default is 20Gi (WSI-NFR-0006). Foundry admin may increase per-session size up to quota limits.

## Related documentation

- [pod-lifecycle.md](pod-lifecycle.md) — Pod deletion retains PVC on stop
- [failure-modes.md](failure-modes.md) — PVC provision failure recovery
- [multi-tenant-isolation.md](multi-tenant-isolation.md) — Storage quota per namespace
- [requirements.md](requirements.md) — WSI-FR-0009, WSI-FR-0010, WSI-NFR-0006, WSI-NFR-0007
