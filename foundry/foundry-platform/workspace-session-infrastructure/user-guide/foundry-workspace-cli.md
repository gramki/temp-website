# Foundry Workspace CLI

Reference for the `foundry workspace` command-line interface — available inside active Workspace Sessions.

## Overview

The `foundry workspace` CLI runs locally inside the session pod. It communicates with WO Runtime only (port 9090) — not with Session Management or the Orchestrator directly.

Use it from the integrated terminal in Code Server to inspect session status, manage tasks, spawn agents, and list Work Orders.

## Prerequisites

- Active Workspace Session (Session Management state: Active)
- WO Runtime running (started automatically by supervisord)
- CLI pre-installed in the platform base image at `/usr/local/bin/foundry`

## Global options

```
foundry workspace [command] [options]

Global flags:
  --json          Output as JSON
  --quiet         Suppress non-essential output
  --timeout SEC   Request timeout (default: 30)
```

## Commands

### status

Show current session and WO Runtime status.

```
foundry workspace status
```

**Output:**

```
Session ID:     sess-abc123
Workspace type: development
Workbench:      workbench-456
WO Runtime:     v1.2.3 (healthy)
Active WOs:     2
Active agents:  1
CPU usage:      34%
Memory usage:   52%
```

With `--json`:

```json
{
  "session_id": "sess-abc123",
  "workspace_type": "development",
  "workbench_id": "workbench-456",
  "wo_runtime_version": "1.2.3",
  "healthy": true,
  "active_wos": 2,
  "active_agents": 1,
  "cpu_usage_pct": 34.0,
  "memory_usage_pct": 52.0
}
```

### tasks

List or inspect tasks in the current session.

```
foundry workspace tasks list
foundry workspace tasks show TASK-890
foundry workspace tasks logs TASK-890 [--follow]
```

| Subcommand | Description |
|------------|-------------|
| `list` | All tasks in active Work Orders |
| `show TASK-ID` | Task details, state, dependencies |
| `logs TASK-ID` | Agent output for the task; `--follow` streams live |

**Task states:** `pending`, `ready`, `running`, `completed`, `failed`, `blocked`

### agent

Spawn and manage Capable Agents.

```
foundry workspace agent spawn --task TASK-890 [--agent codex] [--skill skill-name]
foundry workspace agent list
foundry workspace agent logs AGENT-ID [--follow]
foundry workspace agent stop AGENT-ID
```

| Subcommand | Description |
|------------|-------------|
| `spawn` | Start an agent for a task; defaults to Workbench-preferred agent |
| `list` | Running and recently completed agents |
| `logs` | Agent stdout/stderr |
| `stop` | Terminate a running agent |

**Example:**

```
foundry workspace agent spawn --task TASK-890 --agent codex --skill implement-feature
Agent spawned: agent-xyz789
  Task:    TASK-890
  Agent:   codex
  Skill:   implement-feature
  State:   running
```

If the preferred agent is unavailable, WO Runtime tries fallback agents configured for the Workbench.

### wo

List and inspect Work Orders assigned to this session.

```
foundry workspace wo list
foundry workspace wo show WO-1234
```

| Subcommand | Description |
|------------|-------------|
| `list` | Work Orders assigned to the session owner |
| `show WO-ID` | WO details, task tree summary, completion status |

**Example:**

```
foundry workspace wo list

ID        TITLE                          STATE      TASKS
WO-1234   Implement login flow           active     8/12 complete
WO-1235   Add password reset             active     2/5 complete
```

## Environment variables

The CLI reads these from the session pod environment (set by Session Infrastructure):

| Variable | Description |
|----------|-------------|
| `FOUNDRY_SESSION_ID` | Current session identifier |
| `FOUNDRY_WORKSPACE_TYPE` | Workspace type (e.g. `development`) |
| `FOUNDRY_WORKBENCH_ID` | Workbench identifier |
| `FOUNDRY_WO_RUNTIME_URL` | WO Runtime API endpoint (default: `http://localhost:9090`) |

## Error handling

| Exit code | Meaning |
|-----------|---------|
| 0 | Success |
| 1 | General error |
| 2 | WO Runtime unreachable |
| 3 | Resource not found (task, agent, WO) |
| 4 | Agent spawn failed (quota, skill missing) |

If WO Runtime is unreachable, check session health:

```
foundry workspace status
# If unhealthy, the session may be restarting — wait and retry
```

## What the CLI does not do

| Action | Use instead |
|--------|-------------|
| Create or stop sessions | Session Management (admin API or Web console) |
| Configure cluster settings | Foundry settings (`workspace_infrastructure`) |
| Customize workspace images | Foundry Definition Repo overlay — see [customizing-workspace-images.md](customizing-workspace-images.md) |
| Assign Work Orders | Orchestrator (automatic) |

## Related documentation

- [../../work-order-runtime/user-guide/work-order-lifecycle.md](../../work-order-runtime/user-guide/work-order-lifecycle.md) — Work Order flow
- [../../work-order-runtime/concepts/wo-runtime-daemon.md](../../work-order-runtime/concepts/wo-runtime-daemon.md) — WO Runtime internals
- [customizing-workspace-images.md](customizing-workspace-images.md) — Admin overlay guide
