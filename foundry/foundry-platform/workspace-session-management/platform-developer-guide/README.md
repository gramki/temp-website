# Workspace Session Management — Foundry Platform developer guide

This guide contains implementation specifications for engineers building **Workspace Session Management** — the control-plane service for Workspace Session lifecycle.

## Implementation overview

Session Management is a standalone service (separate container, own schema) that shares a PostgreSQL instance with Management but does not use foreign key constraints to Management tables. It exposes a REST API for Orchestrator, WO Runtime, and admins; delegates provisioning to Session Infrastructure; and publishes session lifecycle events to **Atropos** (HTTP callbacks to subscribers).

**This service has no Work Order domain model.** Do not add WO tables, assignment logic, or Jira coupling here.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|----------------------------|
| [Workspace Session](../../concepts/workspace-session.md) | Lifecycle source of truth and session URL registry |
| [Workspace](../../concepts/workspace.md) | `workspace_type` on every session |

## Specification index

| Document | Scope |
|----------|-------|
| [session-state-machine.md](session-state-machine.md) | Formal states, guards, side effects, timeout policies |
| [session-api.md](session-api.md) | REST API: create, query, stop, archive, delete; event publication |
| [interface-contracts.md](interface-contracts.md) | Schemas for Orchestrator, WO Runtime, Infrastructure, Admin |
| [requirements.md](requirements.md) | WSSM-FR-0001–0010, WSSM-NFR-0001–0005 |
| [design-discussions/standalone-vs-subsystem.md](design-discussions/standalone-vs-subsystem.md) | Deployment decision: standalone vs Management subsystem |

## Dependencies

| Module | Integration |
|--------|-------------|
| [Workspace Session Infrastructure](../workspace-session-infrastructure/README.md) | Provision and terminate pods; pod-ready / pod-failed events |
| [Orchestrator](../../orchestrator/README.md) | Create and query sessions; subscribe to `session-activated` |
| [Work Order Runtime](../../work-order-runtime/README.md) | Ack, heartbeat, shutdown; receive stop/drain via heartbeat |
| [Management](../../management/README.md) | Foundry settings for idle timeout and max lifetime |

## Related documentation

- [Module README](../README.md) — scope, boundaries, architecture
- [User guide](../user-guide/) — admin operations
- [Concepts](../concepts/) — lifecycle, events, identity
- [Foundry Platform README](../../README.md) — platform module map
