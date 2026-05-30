# `foundry workspace` CLI

Local, in-session CLI that talks to WO Runtime only — not to Session Management or the management plane.

## Prerequisites

- Active Workspace Session (WO Runtime running on port 9090 inside pod)
- CLI installed in session container (ships with base image)

## Commands

### `foundry workspace status`

Show session-local status: active WOs, agents, resource usage.

```bash
foundry workspace status
# Session: sess-abc123
# Active WOs: 2
# Active agents: 1
# WO Runtime: healthy
```

### `foundry workspace tasks`

List tasks in the current session's task tree.

```bash
foundry workspace tasks --wo WO-1234
```

### `foundry workspace wo list`

List Work Orders attached to this session.

```bash
foundry workspace wo list
```

### `foundry workspace agent spawn`

Spawn an agent for a task (delegates to WO Runtime).

```bash
foundry workspace agent spawn --task TASK-5678
```

### `foundry workspace agent logs`

Tail agent output.

```bash
foundry workspace agent logs --agent agent-001 --follow
```

## Architecture note

The CLI is a **user/local interface** to WO Runtime. It does not create sessions, change session lifecycle, or communicate with Session Management. Session lifecycle is managed by the control plane; WO Runtime is the in-session worker.

→ [../../work-order-runtime/concepts/management-plane-interface.md](../../work-order-runtime/concepts/management-plane-interface.md) — WO Runtime dual interface

## Read next

- [../../work-order-runtime/user-guide/README.md](../../work-order-runtime/user-guide/README.md) — WO execution from builder perspective
- [../../ide/user-guide/workspace-sessions.md](../../ide/user-guide/workspace-sessions.md) — IDE session usage
