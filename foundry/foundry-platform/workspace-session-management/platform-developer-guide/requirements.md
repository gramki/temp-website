# Workspace Session Management Requirements

This document specifies implementation requirements for the Workspace Session Management module.

**Scope boundary:** Session Management owns control-plane session lifecycle only. It does not model Work Orders, assignment, Jira, or task execution.

## Key concepts

| Concept | Link |
|---------|------|
| Workspace Session | [../../concepts/workspace-session.md](../../concepts/workspace-session.md) |
| Workspace | [../../concepts/workspace.md](../../concepts/workspace.md) |

Module-specific concepts:

| Concept | Link |
|---------|------|
| Session lifecycle | [../concepts/session-lifecycle.md](../concepts/session-lifecycle.md) |
| Session events | [../concepts/session-events.md](../concepts/session-events.md) |
| Session identity | [../concepts/session-identity.md](../concepts/session-identity.md) |

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|----------------------------|
| **Workspace Session** | Lifecycle source of truth, session URL registry, event stream |
| **Workspace** | Every session is scoped to a `workspace_type` within a Workbench |

## Architecture overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    Workspace Session Management (standalone)                 │
│                                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │  Session API │  │ State Machine│  │   Event      │  │ Session Store│   │
│  │  (REST)      │  │              │  │  Publisher   │  │ (PostgreSQL) │   │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────────────┘   │
│         └─────────────────┴─────────────────┘                               │
└───────────────┬───────────────────────────────┬─────────────────────────────┘
                │                               │
                ▼                               ▼
     ┌──────────────────────┐        ┌──────────────────────┐
     │ Session Infrastructure│        │ Message queue         │
     │ (provision / terminate)│        │ (session events)      │
     └──────────────────────┘        └──────────────────────┘
                ▲
                │ ack / heartbeat / shutdown
     ┌──────────┴──────────┐
     │   WO Runtime (pod)   │
     └─────────────────────┘
                ▲
                │ create / query
     ┌──────────┴──────────┐
     │     Orchestrator     │
     └─────────────────────┘
```

## Functional requirements

### Session creation and provisioning

**WSSM-FR-0001:** Session Management SHALL create a session record on request from Orchestrator or Foundry Admin and delegate pod provisioning to Workspace Session Infrastructure.

| Aspect | Detail |
|--------|--------|
| Trigger | `POST /api/v1/sessions` |
| Initial state | `created`, then automatic transition to `starting` |
| Delegation | `POST /api/v1/sessions/provision` to Session Infrastructure |
| Validation | Required fields: `user_id`, `workspace_type`, `workbench_id`, `foundry_id` |
| Work Orders | Not referenced |

### State tracking

**WSSM-FR-0002:** Session Management SHALL track session state transitions and persist the current state for every session.

| Aspect | Detail |
|--------|--------|
| States | `created`, `starting`, `active`, `unhealthy`, `stopping`, `stopped`, `archived`, `deleted` |
| Authority | Session Management is the sole writer of session state |
| Concurrency | One transition per `session_id` at a time (row lock or optimistic `version`) |
| Specification | [session-state-machine.md](session-state-machine.md) |

### Liveness acknowledgment

**WSSM-FR-0003:** Session Management SHALL accept a liveness acknowledgment from WO Runtime and transition the session to `active` when Infrastructure has reported pod ready and ack is received within the ack deadline.

| Aspect | Detail |
|--------|--------|
| Endpoint | `POST /api/v1/sessions/{session-id}/ack` |
| Preconditions | `session_url` set from Infrastructure `pod-ready`; state `starting` or `unhealthy` |
| Post-transition | Start heartbeat clock; emit `session-activated` |
| Ack deadline | 30 seconds after `pod-ready` (see state machine) |

### Event publication

**WSSM-FR-0004:** Session Management SHALL publish a session event on every state transition.

| Aspect | Detail |
|--------|--------|
| Events | `session-created`, `session-starting`, `session-activated`, `session-unhealthy`, `session-stopping`, `session-stopped`, `session-archived` |
| Envelope | Shared schema per [interface-contracts.md](interface-contracts.md) |
| Delivery | At-least-once via message queue; partition key `session_id` |
| Latency | See WSSM-NFR-0002 |

### Session query

**WSSM-FR-0005:** Session Management SHALL expose query APIs to list and filter sessions by user, workspace type, workbench, and state.

| Aspect | Detail |
|--------|--------|
| Orchestrator API | `GET /api/v1/sessions?user=&workspace_type=&workbench=&state=` |
| Admin API | `GET /api/v1/admin/sessions?foundry=&state=&page=&limit=` |
| Response fields | `session_id`, `session_url`, `state`, timestamps, `last_heartbeat` where applicable |
| Work Orders | Not included in query results |

### Idle timeout

**WSSM-FR-0006:** Session Management SHALL enforce a configurable idle timeout and stop sessions with no heartbeat activity beyond the threshold.

| Aspect | Detail |
|--------|--------|
| Configuration | `session_management.idle_timeout_minutes` in Foundry settings |
| Evaluation | On each heartbeat: compare `now - last_heartbeat_at` |
| Stop path | Heartbeat `command: drain` then `stop`, or direct transition to `stopping` |
| Stop reason | `idle-timeout` in metadata |

### Max session lifetime

**WSSM-FR-0007:** Session Management SHALL enforce a configurable maximum session lifetime and stop sessions that exceed the limit while `active`.

| Aspect | Detail |
|--------|--------|
| Configuration | `session_management.max_lifetime_hours` in Foundry settings |
| Evaluation | From `created_at` while state is `active` |
| Stop reason | `max-lifetime` in metadata |

### Admin force-stop

**WSSM-FR-0008:** Session Management SHALL accept force-stop from Foundry Admin, send stop/drain commands to WO Runtime, and drive the session through `stopping` to `stopped`.

| Aspect | Detail |
|--------|--------|
| Endpoint | `POST /api/v1/sessions/{session-id}/stop` |
| Parameters | `reason`, `grace_period_seconds` (default 30) |
| WO Runtime | Stop/drain via heartbeat response or dedicated command channel |
| Infrastructure | `DELETE /api/v1/sessions/{id}/pod` after shutdown ack or grace elapsed |

### Session URL registry

**WSSM-FR-0009:** Session Management SHALL store the session URL received from Session Infrastructure and expose it via query API from `session-activated` onward.

| Aspect | Detail |
|--------|--------|
| Source | `session-infrastructure.pod-ready` event payload |
| Storage | `session_url` column on session record |
| Visibility | Populated in API responses and event envelope when active |
| Cleared | On transition to `stopped` (historical URL optional for admin UI) |

### Unhealthy detection and recovery

**WSSM-FR-0010:** Session Management SHALL detect unhealthy sessions when the liveness timeout is exceeded, query Infrastructure for pod status, and attempt recovery before marking the session `stopped`.

| Aspect | Detail |
|--------|--------|
| Unhealthy threshold | 60 seconds since last heartbeat (WSSM-NFR-0004) |
| Recovery window | 30 seconds additional after `unhealthy` |
| Infrastructure query | Pod running → wait for re-ack; pod failed/missing → `stopping` → `stopped` |
| Events | Emit `session-unhealthy`; emit `session-stopped` on failure |

## Non-functional requirements

### Query latency

**WSSM-NFR-0001:** Session state query responses SHALL complete within 200ms at P95 under normal load (single Foundry, indexed filters on `foundry_id`, `user_id`, `workbench_id`, `state`).

| Aspect | Detail |
|--------|--------|
| Scope | `GET /api/v1/sessions` and `GET /api/v1/admin/sessions` |
| Indexing | Composite index on query dimensions |
| Excludes | Heartbeat write path (separate SLO) |

### Event publication latency

**WSSM-NFR-0002:** Event publication SHALL occur within 500ms of the state transition commit (P95).

| Aspect | Detail |
|--------|--------|
| Pattern | Transactional outbox in session schema recommended |
| Consumers | Orchestrator, Web console, metrics |

### Scale

**WSSM-NFR-0003:** Session Management SHALL support at least 10,000 concurrent session records per Foundry without degrading query or heartbeat SLOs.

| Aspect | Detail |
|--------|--------|
| Record types | All non-deleted states count toward capacity planning |
| Horizontal scaling | Stateless API replicas; shared PostgreSQL; partition-friendly event topic |

### Liveness timeout

**WSSM-NFR-0004:** If no heartbeat is received within 60 seconds of the last heartbeat, Session Management SHALL mark the session `unhealthy`.

| Aspect | Detail |
|--------|--------|
| Expected interval | WO Runtime sends heartbeat every 15s |
| Margin | 4 missed heartbeats before unhealthy |
| Recovery | Per WSSM-FR-0010 |

### Heartbeat ingestion throughput

**WSSM-NFR-0005:** Session Management SHALL sustain ingestion of at least 1,000 heartbeats per second per Foundry without backpressure or dropped updates.

| Aspect | Detail |
|--------|--------|
| Load model | ~15s interval × N active sessions; 10k sessions ≈ 667/s |
| Design | Async write path; batch optional; idempotent `last_heartbeat_at` updates |
| Deployment | Standalone service with independent scaling ([standalone-vs-subsystem.md](design-discussions/standalone-vs-subsystem.md)) |

## Deployment requirements

| Requirement | Detail |
|-------------|--------|
| Service model | Standalone container in management namespace |
| Database | Shared PostgreSQL instance; dedicated schema; no FK to Management tables |
| References | `foundry_id`, `workbench_id`, `user_id` as plain columns |
| Message queue | Dedicated producer connection for session events |

## Out of scope (explicit)

| Concern | Owner module |
|---------|--------------|
| Work Order assignment or discovery | Orchestrator, WO Runtime |
| Kubernetes pod / PVC / ingress | Workspace Session Infrastructure |
| Workshop content and devcontainer merge | Management, Session Infrastructure |
| Cluster endpoint configuration | Foundry admin settings → Session Infrastructure |

## Traceability

| Document | Requirement coverage |
|----------|---------------------|
| [session-state-machine.md](session-state-machine.md) | WSSM-FR-0002, WSSM-FR-0003, WSSM-FR-0006, WSSM-FR-0007, WSSM-FR-0010, WSSM-NFR-0004 |
| [session-api.md](session-api.md) | WSSM-FR-0001, WSSM-FR-0005, WSSM-FR-0008, WSSM-FR-0009 |
| [interface-contracts.md](interface-contracts.md) | WSSM-FR-0004, integration schemas |
| [design-discussions/standalone-vs-subsystem.md](design-discussions/standalone-vs-subsystem.md) | WSSM-NFR-0003, WSSM-NFR-0005 |

## Read next

- [session-state-machine.md](session-state-machine.md) — formal transitions and timeouts
- [session-api.md](session-api.md) — REST operations
- [interface-contracts.md](interface-contracts.md) — consumer schemas
- [../user-guide/managing-sessions.md](../user-guide/managing-sessions.md) — admin operations
