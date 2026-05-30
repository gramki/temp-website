# Sequence Diagrams

End-to-end time-ordered flows for platform developers implementing any participant.

## Session creation flow

```mermaid
sequenceDiagram
    participant ORC as Orchestrator
    participant WSM as Session Management
    participant WSI as Session Infrastructure
    participant K8S as Kubernetes
    participant WOR as WO Runtime

    ORC->>WSM: POST /sessions/create (user, workspace-type, workbench)
    WSM->>WSM: Create session record (state: Created)
    WSM->>WSI: POST /sessions/provision (session-id, foundry-id, ...)
    WSM->>WSM: Transition state: Starting
    WSI->>K8S: Create PVC, Pod, Service
    K8S-->>WSI: Pod scheduled
    K8S-->>K8S: Init containers run (workspace merge, admin overlay)
    K8S-->>K8S: Main container starts (Code Server + WO Runtime)
    K8S-->>WSI: Readiness probe passes
    WSI-->>WSM: Event: pod-ready (session-url)
    WSM->>WSM: Store session URL
    WOR->>WSM: POST /sessions/{id}/ack (liveness acknowledgment)
    WSM->>WSM: Transition state: Active
    WSM-->>ORC: Event: session-activated (session-id, session-url)
    ORC->>ORC: Assign WO (write to Jira)
    WOR->>WOR: Discover WO via polling/event
```

## Session stop flow

```mermaid
sequenceDiagram
    participant Admin as Foundry Admin
    participant WSM as Session Management
    participant WOR as WO Runtime
    participant WSI as Session Infrastructure
    participant K8S as Kubernetes

    Admin->>WSM: POST /sessions/{id}/stop
    WSM->>WSM: Transition state: Stopping
    WSM->>WOR: Stop command (drain active tasks)
    WOR->>WOR: Drain: finish current task, block new tasks
    WOR-->>WSM: Shutdown acknowledgment
    WSM->>WSI: DELETE /sessions/{id}/pod
    WSI->>K8S: Delete Pod (PVC retained)
    K8S-->>WSI: Pod terminated
    WSI-->>WSM: Event: pod-terminated
    WSM->>WSM: Transition state: Stopped
    WSM-->>Admin: Event: session-stopped
```

## Pod crash recovery flow

```mermaid
sequenceDiagram
    participant K8S as Kubernetes
    participant WSI as Session Infrastructure
    participant WSM as Session Management
    participant WOR as WO Runtime

    K8S->>K8S: Pod crashes (OOM, process exit, etc.)
    K8S->>K8S: Restart pod (restartPolicy: Always)
    K8S-->>WSI: Pod restarting event
    WSI-->>WSM: Event: pod-restarting (session-id)
    Note over WSM: Liveness timeout clock running (60s)
    K8S->>K8S: Init containers re-run
    K8S->>K8S: Main container starts
    WOR->>WSM: POST /sessions/{id}/ack (re-acknowledgment)
    WSM->>WSM: Reset liveness timer; remain Active
    Note over WSM: If ack does NOT arrive within 60s:
    WSM->>WSM: Transition: Active → Unhealthy
    WSM->>WSI: Query pod status via K8s API
    alt Pod running but WO Runtime unhealthy
        WSI-->>WSM: Pod exists, container running
        WSM->>WSM: Wait additional 30s for ack
    else Pod gone or CrashLoopBackOff
        WSI-->>WSM: Pod failed
        WSM->>WSM: Transition: Unhealthy → Stopped
    end
```

## Read Next

- [interface-contracts.md](interface-contracts.md) — API schemas
- [failure-modes.md](failure-modes.md) — recovery strategies
