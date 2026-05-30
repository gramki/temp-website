# Workspace Session Management user guide

This guide covers administrative tasks for Foundry Admins who monitor Workspace Sessions, enforce policies, and intervene when sessions misbehave.

Session Management is the control plane for session lifecycle. It does not assign or track Work Orders — that remains Orchestrator and WO Runtime responsibility after a session becomes active.

## Audience

| Role | Primary interest |
|------|------------------|
| Foundry Admins | View sessions, force-stop, idle timeout and max lifetime, archive |
| Platform operators | Capacity and health visibility across active sessions |

## Guide contents

| Document | Description |
|----------|-------------|
| [managing-sessions.md](managing-sessions.md) | View sessions, force-stop, policy configuration, archive |

## Quick start paths

**"I need to see who has active sessions and stop one"**
→ [managing-sessions.md](managing-sessions.md) — Viewing and force-stopping sessions

**"Sessions are running too long or sitting idle"**
→ [managing-sessions.md](managing-sessions.md) — Idle timeout and max lifetime

**"I need to retain session evidence after stop"**
→ [managing-sessions.md](managing-sessions.md) — Archive policies

## Prerequisites

Before sessions can be created and managed:

1. **Foundry admin** configures `workspace_infrastructure` (Kubernetes cluster, ingress, storage) — see [Workspace Session Infrastructure](../../workspace-session-infrastructure/README.md) and [Management foundry settings](../../management/user-guide/foundry-settings.md).
2. **Session policies** (`session_management` block) are set in the Foundry Definition Repo and validated by Management.
3. **Orchestrator** or admin APIs create sessions; builders do not call Session Management directly.

## Related documentation

- [Module README](../README.md) — scope, boundaries, architecture
- [Foundry Platform developer guide](../platform-developer-guide/) — APIs, state machine, requirements
- [IDE user guide](../../ide/user-guide/workspace-sessions.md) — builder experience inside an active session
- [Work Order Runtime user guide](../../work-order-runtime/user-guide/) — in-session execution (separate from session lifecycle)
