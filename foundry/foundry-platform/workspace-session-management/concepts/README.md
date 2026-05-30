# Workspace Session Management Concepts

This folder contains module-specific concept definitions for Workspace Session Management. These concepts describe control-plane session lifecycle — state, events, and identity — without reference to Work Orders.

## How to use these concepts

- **Module-scoped.** These concepts explain Session Management behavior and invariants.
- **Link to platform concepts.** For what a Workspace Session *is*, see [../../concepts/workspace-session.md](../../concepts/workspace-session.md).
- **Link to infrastructure.** For pods, URLs, and storage, see [../../workspace-session-infrastructure/](../../workspace-session-infrastructure/).
- **No Work Order semantics.** Orchestrator and WO Runtime own WO assignment and execution; this module only knows that a session is Active or not.

## Concept index

| Concept | Definition |
|---------|------------|
| [Session lifecycle](session-lifecycle.md) | State machine, transitions, triggers, and guard conditions |
| [Session events](session-events.md) | Event types, envelope, consumers, delivery semantics |
| [Session identity](session-identity.md) | How sessions are keyed, addressed, and distinguished |

## Relationship to platform concepts

| Platform concept | Session Management realization |
|------------------|-------------------------------|
| [Workspace Session](../../concepts/workspace-session.md) | Lifecycle source of truth; URL registry after activation |
| [Workspace](../../concepts/workspace.md) | `workspace_type` dimension on every session record |

## Read next

- [session-lifecycle.md](session-lifecycle.md) — state machine overview
- [../README.md](../README.md) — module scope and architecture
- [../../concepts/workspace-session.md](../../concepts/workspace-session.md) — platform-wide definition
