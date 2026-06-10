# WO Runtime Daemon

The WO Runtime Daemon is the long-running process within each Workspace Session that coordinates Work Order execution — polling for assigned WOs, scheduling tasks, spawning agents, and reporting completion.

## What it is

Every Workspace Session runs a WO Runtime Daemon. The daemon is the execution coordinator for that session, responsible for:

1. **Polling** — Querying Jira (via MCP) for Work Orders assigned to the session owner
2. **Task tree management** — Building and maintaining the task tree for each attached WO
3. **Scheduling** — Identifying ready tasks across **all attached WOs in parallel**; tasks wait only when blocked (dependencies, `blocked` state, or agent concurrency limits)
4. **Agent spawning** — Preparing harnesses and spawning Employed Agents for agent tasks
5. **Human task surfacing** — Making tasks without Trained Agents visible in the IDE
6. **Completion tracking** — Detecting task completion and updating state
7. **Notification** — Reporting WO completion to the Orchestrator via Atropos (`/{foundry-id}/foundry.wo-runtime.*`)

The daemon runs continuously while the Workspace Session is active. It starts when the Coder workspace starts and stops when the workspace stops. Session state persists across workspace restarts via the Local State Store.

The daemon does not execute tasks directly — it coordinates. Agent processes run separately within the same workspace, and humans interact with tasks through the IDE Work Orders panel.

## Where it lives

| Component | Location |
|-----------|----------|
| **Daemon process** | Runs within Coder workspace container |
| **Configuration** | Session settings from Metadata Service |
| **State** | Local SQLite database (see [Local State Store](local-state-store.md)) |
| **Jira access** | Via Jira MCP Server |
| **Agent processes** | Sibling processes within same container |

## Daemon lifecycle

| Phase | Description |
|-------|-------------|
| **Startup** | Daemon starts when Coder workspace activates |
| **Authentication** | Authenticates to Jira MCP using session owner credentials |
| **Initial sync** | Builds task trees for already-attached WOs |
| **Poll loop** | Queries for new WOs every 5 seconds (configurable) |
| **Execution loop** | Schedules ready tasks, monitors completion |
| **Shutdown** | Persists state, notifies running agents, stops with workspace |

## Daemon architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         WO Runtime Daemon                                    │
│                                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │   Jira Poller   │  │  Task Manager   │  │  Agent Spawner  │             │
│  │                 │  │                 │  │                 │             │
│  │  • Poll for WOs │  │  • Build tree   │  │  • Prepare      │             │
│  │  • Track status │  │  • Track deps   │  │    harness      │             │
│  │  • Update Jira  │  │  • Schedule     │  │  • Spawn agent  │             │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘             │
│           │                    │                    │                       │
│           └────────────────────┴────────────────────┘                       │
│                                │                                            │
│                    ┌───────────┴───────────┐                               │
│                    │  Completion Reporter  │──────▶ Orchestrator (MQ)      │
│                    └───────────────────────┘                               │
│                                │                                            │
│                    ┌───────────┴───────────┐                               │
│                    │   Local State Store   │                               │
│                    │       (SQLite)        │                               │
│                    └───────────────────────┘                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Coordination with other components

| Component | Interaction |
|-----------|-------------|
| **Jira MCP** | Poll for WOs, update task status, create sub-tasks |
| **Agent Fabric** | Fetch skill versions, get agent recommendations |
| **Metadata Service** | Get Scenario definitions, Workspace configuration |
| **Orchestrator** | Receive WO assignments (via Jira), report completion (via MQ) |
| **IDE Extension** | Expose Work Orders panel, agent chat tabs |

## Daemon configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `poll_interval` | 5s | How often to poll Jira for WO updates |
| `max_concurrent_agents` | 10 | Maximum parallel agent processes |
| `max_attached_wos` | 20 | Maximum WOs attached to session |
| `metadata_cache_ttl` | 5min | How long to cache Scenario definitions |

## Related concepts

- [Task Manager](task-manager.md) — Manages task trees and dependencies
- [Agent Spawner](agent-spawner.md) — Spawns agents for ready tasks
- [Completion Reporter](completion-reporter.md) — Notifies Orchestrator
- [Local State Store](local-state-store.md) — Persists daemon state
- [Work Order](../../concepts/work-order.md) — What the daemon executes
- [Workspace Session](../../concepts/workspace-session.md) — Where the daemon runs

## Further reading

- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Daemon requirements (WOR-FR-0001, WOR-FR-0002)
- [../user-guide/work-order-lifecycle.md](../user-guide/work-order-lifecycle.md) — Full WO lifecycle
