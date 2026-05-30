# Managing Workspace Sessions

This guide explains how Foundry Admins view Workspace Sessions, intervene when needed, and configure lifecycle policies. Session Management tracks whether an environment exists and is healthy — not what Work Orders run inside it.

## Session lifecycle (admin view)

| State | What it means for admins |
|-------|--------------------------|
| **Starting** | Pod is provisioning; session URL not yet usable |
| **Active** | Builder can open the session URL; WO Runtime is heartbeating |
| **Unhealthy** | Heartbeats missed; recovery may be in progress |
| **Stopping** | Drain in progress; URL may still respond briefly |
| **Stopped** | Pod removed; workspace data retained on storage (resume possible) |
| **Archived** | Long-term retention snapshot; not interactive |
| **Deleted** | Record and storage reclaimed |

A session becomes **Active** only after the pod is ready and WO Runtime sends a liveness acknowledgment. Pod readiness alone is not sufficient.

## Viewing sessions

### Foundry Web console

When integrated, the Foundry admin console lists sessions for your Foundry with filters:

- **State** — e.g. active, unhealthy, stopped
- **User** — who owns the session
- **Workbench** — which Workbench context
- **Workspace type** — product-specification, development, qa, etc.

Each row typically shows: session ID, state, user, workbench, workspace type, created time, last heartbeat, and session URL (when active).

### Admin API

For automation or scripting, use the admin list endpoint documented in [interface-contracts.md](../platform-developer-guide/interface-contracts.md):

```
GET /api/v1/admin/sessions?foundry={foundry-id}&state=active&page=1&limit=50
```

Paginate with `page` and `limit`. Filter by `state` to focus on active or unhealthy sessions during incidents.

## Force-stopping a session

Use force-stop when a session must end immediately — runaway resource use, policy violation, or user offboarding.

### Console

1. Open **Sessions** (or equivalent) for your Foundry.
2. Select the session (must be `active`, `unhealthy`, or `starting`).
3. Choose **Stop** / **Force stop**.
4. Confirm; optional grace period (default 30 seconds).

### API

```
POST /api/v1/sessions/{session-id}/stop
```

```yaml
reason: "admin-forced"
grace_period_seconds: 30   # optional
```

**What happens:**

1. Session transitions to **Stopping**; event `session-stopping` is published.
2. Session Management signals WO Runtime to **drain** then **stop** (via heartbeat command).
3. After shutdown acknowledgment or grace elapsed, Session Infrastructure terminates the pod (PVC retained per infrastructure policy).
4. Session becomes **Stopped**; event `session-stopped` is published.

Stopping a session does not cancel Work Orders in Jira — Orchestrator and WO Runtime handle work separately. Admins stop the **environment**, not individual tasks.

## Configuring idle timeout

Idle timeout ends sessions that receive no heartbeats from WO Runtime for longer than the configured period. Heartbeats arrive every 15 seconds while the session is healthy; idle timeout is evaluated against `last_heartbeat_at`, not IDE keyboard activity.

### Foundry settings

Add or update in your Foundry Definition Repo (`foundry.yaml`):

```yaml
session_management:
  idle_timeout_minutes: 120
  max_lifetime_hours: 24
  allow_multiple_active: false
```

| Setting | Purpose | Typical values |
|---------|---------|----------------|
| `idle_timeout_minutes` | Stop session after this many minutes without heartbeat | 60–480 (team policy) |
| `max_lifetime_hours` | Hard cap from session creation while active | 8–24 |
| `allow_multiple_active` | Whether one user may have multiple active sessions for same (workbench, workspace type) | `false` for cost control |

Settings are validated by Management and synced to Metadata Service. Session Management reads them at runtime.

### Strict vs graceful idle stop

Implementation may either:

- Return `command: drain` on heartbeat, then `command: stop` on the next cycle, or
- Transition directly to **Stopping** when idle threshold is exceeded.

Both paths emit `session-stopping` with reason `idle-timeout`. Builders see the session URL become unavailable after drain completes.

## Configuring max session lifetime

`max_lifetime_hours` prevents indefinitely long **Active** sessions (e.g. forgotten environments left running overnight).

- Clock starts at `created_at`.
- When exceeded while **Active**, Session Management initiates stop with reason `max-lifetime`.
- Admins can still force-stop earlier if needed.

Combine with idle timeout: idle catches abandoned sessions; max lifetime caps wall-clock duration even with steady heartbeats.

## Archiving stopped sessions

Archive moves a **Stopped** session into long-term retention without keeping a live pod.

### When to archive

- Compliance or audit retention after work completed
- Freeing active session quota while keeping storage snapshot
- Standard housekeeping for sessions stopped more than N days (retention job)

### Console / API

```
POST /api/v1/sessions/{session-id}/archive
```

**Prerequisites:** Session should be **Stopped**. Implementations may support stop-then-archive in one flow.

**Effects:**

- Session state → **Archived**
- Session Infrastructure snapshots PVC and removes live volume per infrastructure policy
- Event `session-archived` published
- Session URL no longer available

### Deleting archived sessions

Full removal uses delete APIs or retention jobs (implementation-specific). **Deleted** is terminal: record and infrastructure reclaimed.

## Policies and multi-session behavior

| Policy | Admin intent |
|--------|----------------|
| `allow_multiple_active: false` | One active session per (user, workbench, workspace type) — reduces duplicate environments |
| Short idle timeout | Cost control for ephemeral dev sessions |
| Long max lifetime | Workshops or pair sessions that legitimately run all day |

Orchestrator creates sessions when assigning work; admins tune policies so creation and teardown match organizational cost and security posture.

## Troubleshooting

| Symptom | Likely cause | Admin action |
|---------|--------------|--------------|
| Stuck in **Starting** | Image pull, PVC, or cluster issue | Check Infrastructure events; see infrastructure module docs |
| **Unhealthy** then **Stopped** | WO Runtime not heartbeating; pod crash | Review session events; force-stop if hung in Stopping |
| Session stopped but user expects URL | Idle or max lifetime fired | Adjust `session_management` settings; user starts new session via normal flow |
| Active session, no Work Order progress | Not a Session Management issue | WO assignment is Orchestrator / Jira — session can be healthy without WOs |

## What admins do not configure here

| Concern | Where to configure |
|---------|-------------------|
| Kubernetes cluster, ingress, TLS | `workspace_infrastructure` in Foundry settings → Session Infrastructure |
| Container image layers | Session Infrastructure user guide |
| Work Order assignment | Orchestrator |
| IDE extensions in session | Session Infrastructure image / admin overlay |

## Related documentation

- [../platform-developer-guide/session-state-machine.md](../platform-developer-guide/session-state-machine.md) — formal states and timeouts
- [../platform-developer-guide/interface-contracts.md](../platform-developer-guide/interface-contracts.md) — admin API schemas
- [../../management/user-guide/foundry-settings.md](../../management/user-guide/foundry-settings.md) — Foundry settings reference
- [../../workspace-session-infrastructure/README.md](../../workspace-session-infrastructure/README.md) — pod and URL provisioning
