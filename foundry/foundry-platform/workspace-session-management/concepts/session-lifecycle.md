# Session Lifecycle

Session lifecycle is the ordered progression of a Workspace Session through control-plane states. Session Management owns this progression: it persists state, enforces guards, delegates infrastructure work, and publishes events on every transition.

This module does **not** track Work Orders. Whether zero or many WOs attach to a session is invisible here; Orchestrator and WO Runtime coordinate that separately once a session is **Active**.

## State machine

```
Created → Starting → Active ⇄ Unhealthy → Stopping → Stopped → Archived → Deleted
                         ↑__________________|
                    (recovery / re-ack)
```

| State | Description |
|-------|-------------|
| **Created** | Session record allocated; provisioning not yet invoked |
| **Starting** | Provision request sent to Session Infrastructure; awaiting pod ready and WO Runtime liveness ack |
| **Active** | Session URL valid; WO Runtime acknowledged; heartbeats expected every 15s |
| **Unhealthy** | No heartbeat within liveness timeout (60s); recovery evaluation in progress |
| **Stopping** | Stop requested; WO Runtime draining; pod termination in flight |
| **Stopped** | Pod gone; session URL no longer serves live work; PVC retained per Infrastructure policy |
| **Archived** | Session moved to long-term retention; storage snapshotted per Infrastructure policy |
| **Deleted** | Session record and infrastructure resources reclaimed |

**Failed** is not a persistent terminal state in the public model: provisioning or unrecoverable infrastructure failures transition **Starting** → **Stopped** (or delete) with error metadata on the event, leaving Orchestrator to retry creation with a new session ID if needed.

## Who triggers transitions

| Transition | Typical trigger |
|------------|-----------------|
| Created → Starting | Session Management after accepting create request |
| Starting → Active | Session Management after Infrastructure `pod-ready` **and** WO Runtime `POST .../ack` |
| Active → Unhealthy | Session Management when liveness timeout (60s) expires without heartbeat |
| Unhealthy → Active | WO Runtime re-ack or resumed heartbeats within recovery window |
| Unhealthy → Stopped | Unrecoverable pod failure or recovery window exhausted |
| Active → Stopping | Admin force-stop, idle timeout, max lifetime, or heartbeat `command: stop` |
| Stopping → Stopped | WO Runtime shutdown ack **and** Infrastructure `pod-terminated` |
| Stopped → Active | Resume: new provision request (same session ID, new pod, rebind PVC) |
| Stopped → Archived | Admin or automated archive policy |
| Archived → Deleted | Admin or retention policy expiry |
| * → Deleted | Admin delete from any non-deleted state (runs stop/archive cleanup first) |

## Guard conditions

| Guard | Rule |
|-------|------|
| **Enter Active** | `session_url` set from Infrastructure **and** liveness ack received within ack deadline (30s after pod-ready notification) |
| **Enter Stopping** | Valid from Active, Unhealthy, or Starting (forced cancel) |
| **Enter Stopped** | Shutdown ack received or grace period elapsed; Infrastructure confirms pod termination |
| **Resume from Stopped** | Foundry policy allows resume; PVC still exists per Infrastructure |
| **Archive** | Only from Stopped (or forced from Active via stop-then-archive) |
| **Delete** | Archive complete, or forced delete with infrastructure cleanup |

## Timeouts and policies

| Policy | Default | Configurable by |
|--------|---------|-----------------|
| Liveness timeout | 60s without heartbeat | Foundry admin |
| Heartbeat interval | 15s (WO Runtime obligation) | Platform constant |
| Idle timeout | Foundry-specific | Foundry admin |
| Max session lifetime | Foundry-specific | Foundry admin |
| Stop grace period | 30s | Per stop request (admin API) |
| Ack deadline after pod-ready | 30s | Platform constant |

Idle timeout and max lifetime are evaluated against `last_heartbeat` and `created_at` respectively. When triggered, Session Management transitions **Active** → **Stopping** with reason `idle-timeout` or `max-lifetime`.

## Relationship to infrastructure lifecycle

Session Management state and Kubernetes pod state are related but not identical:

| Session state | Typical pod state |
|---------------|-------------------|
| Starting | Pod scheduling or init containers running |
| Active | Pod running; readiness probe passing |
| Unhealthy | Pod may still be running; WO Runtime not responding |
| Stopping | Pod terminating (preStop, drain) |
| Stopped | Pod deleted; PVC unbound but retained |

Session Infrastructure reports `pod-ready`, `pod-failed`, `pod-restarting`, and `pod-terminated`. Session Management reconciles these signals with WO Runtime heartbeats to decide **Active**, **Unhealthy**, or **Stopped**.

## Read next

- [session-events.md](session-events.md) — events emitted on each transition
- [session-identity.md](session-identity.md) — how sessions are keyed
- [../platform-developer-guide/session-state-machine.md](../platform-developer-guide/session-state-machine.md) — formal specification with side effects
