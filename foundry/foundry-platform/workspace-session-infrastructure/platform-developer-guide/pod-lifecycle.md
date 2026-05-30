# Pod Lifecycle

Pod creation, health probes, graceful shutdown, eviction handling, and resource limits for session pods.

## Pod creation sequence

When Session Infrastructure receives a provision request:

1. Ensure namespace `foundry-{foundry-id}-sessions` exists (create if not — WSI-FR-0007)
2. Create PVC `pvc-session-{session-id}` if not exists (Stopped resume reuses existing PVC)
3. Submit pod spec to Coder Kubernetes provider (or direct K8s API)
4. Watch pod events until readiness probe passes or failure timeout
5. Emit `session-infrastructure.pod-ready` or `session-infrastructure.pod-failed`

## Pod spec

Single container with init containers — no sidecars:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: "session-{session-id}"
  namespace: "foundry-{foundry-id}-sessions"
  labels:
    foundry.io/session-id: "{session-id}"
    foundry.io/user: "{user-id}"
    foundry.io/workspace-type: "development"
    foundry.io/workbench: "{workbench-id}"
    foundry.io/foundry-id: "{foundry-id}"
spec:
  restartPolicy: Always
  serviceAccountName: "session-pod-sa"
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  initContainers:
    - name: workspace-merge
      image: "registry.foundry.example.com/workspace-init:v1.2.3"
      env:
        - name: FOUNDRY_WORKBENCH_ID
          value: "{workbench-id}"
        - name: FOUNDRY_WORKSPACE_TYPE
          value: "development"
      volumeMounts:
        - name: merged-content
          mountPath: /merged-content
        - name: skill-cache
          mountPath: /skill-cache
    - name: admin-overlay
      image: "registry.foundry.example.com/workspace-init:v1.2.3"
      env:
        - name: FOUNDRY_ID
          value: "{foundry-id}"
        - name: FOUNDRY_WORKSPACE_TYPE
          value: "development"
      volumeMounts:
        - name: merged-content
          mountPath: /merged-content
  containers:
    - name: workspace
      image: "registry.foundry.example.com/workspace:v1.2.3"
      command: ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
      ports:
        - containerPort: 8080
          name: code-server
        - containerPort: 9090
          name: wo-runtime
      env:
        - name: FOUNDRY_SESSION_ID
          value: "{session-id}"
        - name: FOUNDRY_WORKSPACE_TYPE
          value: "development"
      readinessProbe:
        httpGet:
          path: /health
          port: 9090
        initialDelaySeconds: 10
        periodSeconds: 5
        failureThreshold: 6
      livenessProbe:
        httpGet:
          path: /health
          port: 9090
        initialDelaySeconds: 30
        periodSeconds: 15
        failureThreshold: 3
      lifecycle:
        preStop:
          exec:
            command: ["/opt/foundry/graceful-shutdown.sh"]
      resources:
        requests:
          cpu: "2"
          memory: "4Gi"
        limits:
          cpu: "4"
          memory: "8Gi"
      volumeMounts:
        - name: workspace-data
          mountPath: /workspace
        - name: merged-content
          mountPath: /workspace/.foundry
          readOnly: true
        - name: skill-cache
          mountPath: /opt/foundry/skills
          readOnly: true
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: ["ALL"]
  volumes:
    - name: workspace-data
      persistentVolumeClaim:
        claimName: "pvc-session-{session-id}"
    - name: merged-content
      emptyDir: {}
    - name: skill-cache
      emptyDir: {}
```

## Health probes

| Probe | Endpoint | Semantics |
|-------|----------|-----------|
| **readiness** | WO Runtime `GET /health:9090` | Session ready — triggers pod-ready event and URL activation |
| **liveness** | WO Runtime `GET /health:9090` | Hung daemon detection — K8s restarts container |

Readiness uses WO Runtime rather than Code Server because session activation (liveness ack to Session Management) requires WO Runtime to be running. Code Server may start before WO Runtime finishes skill installation.

**WSI-NFR-0001:** Pod must pass readiness within 90 seconds of provision request.

## Graceful shutdown

When Session Management requests stop:

1. Session Infrastructure sends pod delete (or Coder workspace stop)
2. K8s sends SIGTERM; `preStop` hook runs `/opt/foundry/graceful-shutdown.sh`
3. Hook signals supervisord → WO Runtime drains active tasks (coordinated with Session Management stop command)
4. WO Runtime sends shutdown ack to Session Management
5. supervisord stops code-server and wo-runtime
6. K8s waits `terminationGracePeriodSeconds: 30` then SIGKILL

**WSI-NFR-0004:** Eviction and manual stop both use the 30-second grace period.

## Eviction handling

When a node evicts a pod due to resource pressure:

| Event | Session Infrastructure action |
|-------|------------------------------|
| Pod `Evicted` | Emit `session-infrastructure.pod-failed` with reason `Evicted` |
| Pod restarting (OOM) | Emit `session-infrastructure.pod-restarting`; watch for re-ack |
| CrashLoopBackOff | Emit `pod-failed` after threshold; Session Management marks Failed |

Session Infrastructure watches pod events via K8s informer scoped to the Foundry namespace.

## Resource limits

Per workspace type defaults (overridable in Foundry settings):

| Workspace type | CPU request | CPU limit | Memory request | Memory limit |
|----------------|-------------|-----------|----------------|--------------|
| product-specification | 1 | 2 | 2Gi | 4Gi |
| ux-design | 2 | 4 | 4Gi | 8Gi |
| development | 2 | 4 | 4Gi | 8Gi |
| qa | 2 | 4 | 4Gi | 8Gi |
| release | 2 | 4 | 4Gi | 8Gi |
| governance | 1 | 2 | 2Gi | 4Gi |

**WSI-FR-0012:** Limits applied per workspace type and Foundry quota. Namespace ResourceQuota caps total concurrent resources.

## Pod deletion on stop

Stop deletes the pod but **retains the PVC**:

```
DELETE pod/session-{session-id}  →  PVC pvc-session-{session-id} retained
```

Resume creates a new pod with the same PVC claimName. Init containers re-run on every start.

## Related documentation

- [storage.md](storage.md) — PVC bind and retain semantics
- [failure-modes.md](failure-modes.md) — Crash and eviction recovery
- [sequence-diagrams.md](sequence-diagrams.md) — Stop and crash recovery flows
- [requirements.md](requirements.md) — WSI-FR-0001, WSI-FR-0012, WSI-NFR-0001, WSI-NFR-0004
