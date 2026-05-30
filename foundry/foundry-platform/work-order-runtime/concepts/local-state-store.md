# Local State Store

The Local State Store is the per-session SQLite database that maintains Work Order, task, agent, and context state within a Workspace Session.

## What it is

Each Workspace Session runs its own SQLite database for local state persistence. This provides:

- **Fast access** — No network latency for state queries during task scheduling
- **Session isolation** — State is scoped to the session owner
- **Persistence** — State survives workspace restarts
- **Offline capability** — Daemon can operate briefly during network partitions

The Local State Store is the source of truth for the WO Runtime Daemon during execution. Jira remains the system of record for Work Orders and Tasks — the local store is a cached, enriched view optimized for runtime operations.

## Where it lives

| Component | Location |
|-----------|----------|
| **Database file** | `~/.foundry/runtime/state.db` |
| **Backup** | Periodic backup to session storage |
| **Sync** | Two-way sync with Jira via MCP |

## Schema

### `work_orders` table

Cached Work Order metadata and state:

```sql
CREATE TABLE work_orders (
    id TEXT PRIMARY KEY,              -- WO-567
    jira_key TEXT NOT NULL,
    scenario TEXT NOT NULL,
    status TEXT NOT NULL,             -- in_progress, completed, failed
    orchestration_item TEXT,          -- PI-456
    attached_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    completed_at DATETIME
);
```

### `tasks` table

Task tree with dependencies and state:

```sql
CREATE TABLE tasks (
    id TEXT PRIMARY KEY,              -- TASK-890
    work_order_id TEXT NOT NULL REFERENCES work_orders(id),
    parent_task_id TEXT,
    scenario TEXT NOT NULL,
    state TEXT NOT NULL,              -- blocked, ready, in_progress, completed, failed, cancelled
    skilled_agent TEXT,
    dependencies TEXT,                -- JSON array of task IDs
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    started_at DATETIME,
    completed_at DATETIME,
    blocked_reason TEXT,
    retry_count INTEGER DEFAULT 0
);

CREATE INDEX idx_tasks_wo ON tasks(work_order_id);
CREATE INDEX idx_tasks_state ON tasks(state);
```

### `agents` table

Running agent processes:

```sql
CREATE TABLE agents (
    id TEXT PRIMARY KEY,              -- UUID
    task_id TEXT NOT NULL REFERENCES tasks(id),
    capable_agent TEXT NOT NULL,
    model TEXT NOT NULL,
    pid INTEGER,
    status TEXT NOT NULL,             -- starting, running, completed, failed
    delegation_token TEXT,
    started_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    completed_at DATETIME
);

CREATE INDEX idx_agents_task ON agents(task_id);
```

### `skill_versions` table

Installed skill versions:

```sql
CREATE TABLE skill_versions (
    name TEXT NOT NULL,
    version TEXT NOT NULL,
    installed_path TEXT NOT NULL,
    installed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(name, version)
);
```

### `context_cache` table

Cached knowledge context:

```sql
CREATE TABLE context_cache (
    key TEXT PRIMARY KEY,             -- "workshop:abc123" or "workbench:xyz789"
    content TEXT NOT NULL,            -- JSON blob
    fetched_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME
);
```

## Sync with Jira

The Local State Store syncs bidirectionally with Jira:

| Direction | Trigger | What syncs |
|-----------|---------|------------|
| Jira → Local | Poll cycle (5s) | New WOs, task state changes |
| Local → Jira | State change | Task status transitions |

### Conflict resolution

If Jira and local state diverge:

- **Task state** — Jira wins (human may have intervened via web UI)
- **Dependencies** — Jira wins (may have been modified externally)
- **Agent state** — Local wins (only daemon knows true agent status)

## Session lifecycle

| Event | State behavior |
|-------|----------------|
| Session start | Load existing state.db if present |
| Session stop | Persist final state, notify agents to stop |
| Session restart | Resume from persisted state |
| Session archive | State.db backed up, then deleted |

## Queries

Common queries used by daemon components:

```sql
-- Get ready tasks for scheduling
SELECT * FROM tasks 
WHERE state = 'ready' 
AND work_order_id IN (SELECT id FROM work_orders WHERE status = 'in_progress');

-- Get active agent count
SELECT COUNT(*) FROM agents WHERE status = 'running';

-- Check if WO is complete
SELECT COUNT(*) FROM tasks 
WHERE work_order_id = ? 
AND state NOT IN ('completed', 'cancelled');
```

## Related concepts

- [WO Runtime Daemon](wo-runtime-daemon.md) — Uses Local State Store for coordination
- [Task Manager](task-manager.md) — Reads/writes task state
- [Agent Spawner](agent-spawner.md) — Writes agent state
- [Context Compilation](context-compilation.md) — Uses context cache

## Further reading

- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Database schema requirements
- [../platform-developer-guide/task-execution.md](../platform-developer-guide/task-execution.md) — How state drives task scheduling
