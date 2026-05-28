# Work Order Runtime Requirements

This document specifies detailed implementation requirements for the Work Order Runtime module.

## Architecture Overview

```
┌───────────────────────────────────────────────────────────────────────────────┐
│                        Workspace Session (Coder)                               │
│                                                                                │
│  ┌──────────────────────────────────────────────────────────────────────────┐ │
│  │                         WO Runtime Daemon                                 │ │
│  │                                                                           │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │ │
│  │  │ Jira Poller │  │    Task     │  │   Agent     │  │ Completion  │     │ │
│  │  │   (MCP)     │  │   Manager   │  │   Spawner   │  │  Reporter   │     │ │
│  │  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘     │ │
│  │         │                │                │                │            │ │
│  │         └────────────────┴────────────────┴────────────────┘            │ │
│  │                                │                                         │ │
│  │                         ┌──────┴──────┐                                 │ │
│  │                         │ Local State │                                 │ │
│  │                         │  (SQLite)   │                                 │ │
│  │                         └─────────────┘                                 │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
│                                                                                │
│  ┌──────────────────────────────────────────────────────────────────────────┐ │
│  │                    Employed Agent Processes                               │ │
│  │                                                                           │ │
│  │    ┌───────────────┐   ┌───────────────┐   ┌───────────────┐            │ │
│  │    │   Agent 1     │   │   Agent 2     │   │   Agent N     │            │ │
│  │    │  (TASK-890)   │   │  (TASK-891)   │   │  (TASK-...)   │            │ │
│  │    └───────┬───────┘   └───────┬───────┘   └───────┬───────┘            │ │
│  │            │                   │                   │                     │ │
│  │            └───────────────────┴───────────────────┘                     │ │
│  │                                │                                         │ │
│  │                     Gateway Policy Layer                                 │ │
│  │                      (for model calls)                                   │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┬───────────────────────────────┘
                                                  │
         ┌────────────────────────────────────────┼────────────────────────────────┐
         │                                        │                                │
         ▼                                        ▼                                ▼
┌─────────────────┐               ┌─────────────────────┐              ┌─────────────────┐
│   Jira (MCP)    │               │    Orchestrator     │              │  Agent Fabric   │
│ (system of      │               │   (completion       │              │ (skills, quota) │
│  record)        │               │    notifications)   │              │                 │
└─────────────────┘               └─────────────────────┘              └─────────────────┘
```

## Core Components

### WO Runtime Daemon

| Aspect | Detail |
|--------|--------|
| Responsibility | Coordinate all WO/task execution within a Workspace Session |
| Lifecycle | Starts with workspace, runs continuously, stops with workspace |
| Input | Assigned WOs from Jira, scenario definitions from Metadata Service |
| Output | Task state changes, completion notifications |
| Dependencies | Jira MCP, Metadata Service, Agent Fabric |

### Jira Poller

| Aspect | Detail |
|--------|--------|
| Responsibility | Poll for assigned Work Orders and tasks |
| Polling interval | 5 seconds (configurable) |
| Input | Session owner identity |
| Output | List of assigned WOs and task tree updates |
| Dependencies | Jira MCP Server |

### Task Manager

| Aspect | Detail |
|--------|--------|
| Responsibility | Manage task tree, dependencies, state transitions |
| Input | Task events (created, updated, completed) |
| Output | Ready tasks for scheduling, state transitions |
| Dependencies | Local SQLite state, Jira MCP |

### Agent Spawner

| Aspect | Detail |
|--------|--------|
| Responsibility | Prepare harness and spawn Employed Agents |
| Input | Ready tasks with Skilled Agent definitions |
| Output | Running agent processes |
| Dependencies | Skill Registry, Metadata Service, Gateway Policy |

### Completion Reporter

| Aspect | Detail |
|--------|--------|
| Responsibility | Notify Orchestrator when WOs complete |
| Input | WO completion events |
| Output | Messages to Orchestrator via message queue |
| Dependencies | Message Queue (Kafka/RabbitMQ) |

---

## Database Schema

### Local State (SQLite per Session)

| Table | Purpose |
|-------|---------|
| `work_orders` | Cached WO metadata and state |
| `tasks` | Task tree with dependencies and state |
| `agents` | Running agent processes |
| `skill_versions` | Installed skill versions |
| `context_cache` | Cached knowledge context |

**Key columns:**

```sql
CREATE TABLE work_orders (
    id TEXT PRIMARY KEY,          -- WO-567
    jira_key TEXT NOT NULL,
    scenario TEXT NOT NULL,
    status TEXT NOT NULL,         -- in_progress, completed, failed
    orchestration_item TEXT,      -- PI-456
    attached_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    completed_at DATETIME
);

CREATE TABLE tasks (
    id TEXT PRIMARY KEY,          -- TASK-890
    work_order_id TEXT NOT NULL REFERENCES work_orders(id),
    parent_task_id TEXT,
    scenario TEXT NOT NULL,
    state TEXT NOT NULL,          -- blocked, ready, in_progress, completed, failed, cancelled
    skilled_agent TEXT,
    dependencies TEXT,            -- JSON array of task IDs
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    started_at DATETIME,
    completed_at DATETIME
);

CREATE TABLE agents (
    id TEXT PRIMARY KEY,          -- UUID
    task_id TEXT NOT NULL REFERENCES tasks(id),
    capable_agent TEXT NOT NULL,
    model TEXT NOT NULL,
    pid INTEGER,
    status TEXT NOT NULL,         -- starting, running, completed, failed
    delegation_token TEXT,
    started_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    completed_at DATETIME
);

CREATE TABLE skill_versions (
    name TEXT NOT NULL,
    version TEXT NOT NULL,
    installed_path TEXT NOT NULL,
    installed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(name, version)
);

CREATE INDEX idx_tasks_wo ON tasks(work_order_id);
CREATE INDEX idx_tasks_state ON tasks(state);
CREATE INDEX idx_agents_task ON agents(task_id);
```

---

## Integration Details

### Jira MCP Integration

| Aspect | Detail |
|--------|--------|
| Integration type | MCP (Model Context Protocol) |
| Direction | Bidirectional |
| Authentication | Session owner's Jira credentials (via delegation) |

**MCP Tools:**

| Tool | Purpose | Frequency |
|------|---------|-----------|
| `jira_search` | Query assigned WOs | Every poll (5s) |
| `jira_get_issue` | Get task details | On task tree build |
| `jira_create_issue` | Create sub-tasks | During agent execution |
| `jira_update_issue` | Update task fields | On state change |
| `jira_transition_issue` | Move task state | On state change |

**Jira Custom Fields:**

| Field ID | Field Name | Purpose |
|----------|------------|---------|
| `customfield_10100` | `foundry-scenario` | Scenario identifier |
| `customfield_10101` | `foundry-work-order` | Parent WO reference |
| `customfield_10102` | `foundry-workspace` | Workspace type |
| `customfield_10103` | `foundry-task-workspace` | Session instance ID |
| `customfield_10104` | `dependencies` | Task dependency list |

### Metadata Service Integration

| Aspect | Detail |
|--------|--------|
| Integration type | REST API |
| Direction | Query only |
| Caching | Session-scoped cache with 5-minute TTL |

**Queries:**

| Query | Frequency |
|-------|-----------|
| Get Scenario definition | Once per unique scenario per session |
| Get Workspace configuration | Once at session start |
| Get effective Skilled Agents | Once per unique scenario |

### Agent Fabric Integration

| Aspect | Detail |
|--------|--------|
| Integration type | REST API |
| Direction | Query + usage reporting |

**Interactions:**

| Operation | Purpose |
|-----------|---------|
| Resolve skill versions | At session start |
| Get agent recommendations | Before spawning |
| Report usage | After task completion |

### Orchestrator Integration

| Aspect | Detail |
|--------|--------|
| Integration type | Message Queue |
| Direction | Outbound only |

**Messages:**

| Message | When |
|---------|------|
| `work-order-completed` | WO reaches terminal state |
| `work-order-failed` | WO fails with no retry |
| `task-blocked` | Task enters recoverable failure |

---

## Processing Logic

### Work Order Attachment

```python
def attach_work_order(wo_id: str):
    # 1. Fetch WO details from Jira
    wo = jira_mcp.get_issue(wo_id)
    
    # 2. Store in local state
    db.insert("work_orders", {
        "id": wo.id,
        "jira_key": wo.key,
        "scenario": wo.fields.foundry_scenario,
        "orchestration_item": wo.fields.foundry_orchestration_item,
        "status": "in_progress"
    })
    
    # 3. Build task tree
    build_task_tree(wo_id)
    
    # 4. Start task scheduling
    schedule_ready_tasks()
```

### Task Tree Building

```python
def build_task_tree(wo_id: str):
    # Query all tasks under this WO from Jira
    tasks = jira_mcp.search(f"'foundry-work-order' = '{wo_id}'")
    
    for task in tasks:
        db.upsert("tasks", {
            "id": task.key,
            "work_order_id": wo_id,
            "parent_task_id": task.fields.parent,
            "scenario": task.fields.foundry_scenario,
            "state": compute_state(task),
            "dependencies": task.fields.dependencies
        })
```

### Task Scheduling

```python
def schedule_ready_tasks():
    while True:
        # Get ready tasks (dependencies met, not yet started)
        ready_tasks = db.query("tasks", state="ready")
        
        for task in ready_tasks:
            if can_start_task(task):
                start_task(task)
        
        sleep(SCHEDULE_INTERVAL)  # 1 second

def can_start_task(task) -> bool:
    # Check concurrent task limit
    active_count = db.count("tasks", state="in_progress")
    return active_count < MAX_CONCURRENT_TASKS
```

### Agent Spawning

```python
def start_task(task: Task):
    # 1. Get Skilled Agent definition
    scenario = metadata_service.get_scenario(task.scenario)
    skilled_agent = scenario.skilled_agent
    
    if not skilled_agent:
        # Human task - mark ready in Jira, show in UI
        mark_human_task_ready(task)
        return
    
    # 2. Select Capable Agent (with fallback)
    capable_agent, model = select_capable_agent(skilled_agent)
    
    # 3. Prepare harness
    harness = prepare_harness(task, skilled_agent, capable_agent, model)
    
    # 4. Spawn agent process
    pid = spawn_agent(capable_agent, harness)
    
    # 5. Record in local state
    db.insert("agents", {
        "id": uuid(),
        "task_id": task.id,
        "capable_agent": capable_agent.id,
        "model": model,
        "pid": pid,
        "status": "running",
        "delegation_token": harness.delegation_token
    })
    
    # 6. Update task state
    db.update("tasks", task.id, state="in_progress")
    jira_mcp.transition_issue(task.id, "In Progress")
```

### Harness Preparation

```python
def prepare_harness(task, skilled_agent, capable_agent, model) -> Harness:
    # Environment variables
    env = {
        "FOUNDRY_WORKBENCH_ID": session.workbench_id,
        "FOUNDRY_WORKSPACE_TYPE": session.workspace_type,
        "FOUNDRY_SESSION_ID": session.id,
        "FOUNDRY_SESSION_OWNER": session.owner,
        "FOUNDRY_WORK_ORDER": task.work_order_id,
        "FOUNDRY_TASK_KEY": task.id,
        "FOUNDRY_SCENARIO": task.scenario,
        "FOUNDRY_AGENT_TYPE": capable_agent.id,
        "FOUNDRY_AGENT_MODEL": model,
        "FOUNDRY_ACCESS_GATEWAY_URL": gateway_url
    }
    
    # MCP connectors
    mcps = configure_mcps(task, session)
    
    # Skills (already installed at session start)
    skills = get_installed_skills(skilled_agent.skills)
    
    # Knowledge context
    context = merge_knowledge_context(
        workshop_knowledge=session.workshop_knowledge,
        workbench_knowledge=session.workbench_knowledge,
        wo_context=get_wo_context(task.work_order_id)
    )
    
    # Delegation token
    token = generate_delegation_token(
        session_owner=session.owner,
        session_id=session.id,
        workbench_id=session.workbench_id,
        work_order=task.work_order_id,
        task=task.id,
        granted_models=[model]
    )
    
    return Harness(env=env, mcps=mcps, skills=skills, context=context, token=token)
```

---

## Error Handling

### Retry Policy

| Failure Type | Strategy |
|--------------|----------|
| Jira MCP timeout | Retry immediately, up to 3 times |
| Metadata Service unavailable | Use cached value, retry in background |
| Agent spawn failure | Try fallback agent, then recoverable failure |
| Agent crash | Retry task up to 2 times |
| Model rate limited | Pause task, retry when quota resets |

### Recoverable Failures

| Failure | State | Resume Trigger |
|---------|-------|----------------|
| Quota exhausted | `blocked` | Quota refreshes |
| Agent disabled | `blocked` | Agent re-enabled |
| All fallbacks failed | `blocked` | Any option restored |
| Model unavailable | `blocked` | Model becomes available |

### Task Failure Flow

```python
def handle_task_failure(task: Task, error: Error):
    if error.is_recoverable:
        # Pause task, await external resolution
        db.update("tasks", task.id, state="blocked", blocked_reason=error.reason)
        jira_mcp.update_issue(task.id, status="Blocked", blocked_reason=error.reason)
        notify_session_owner(task, error)
    
    elif task.retry_count < MAX_RETRIES:
        # Retry task
        db.update("tasks", task.id, retry_count=task.retry_count + 1, state="ready")
        schedule_ready_tasks()
    
    else:
        # Permanent failure
        db.update("tasks", task.id, state="failed")
        jira_mcp.transition_issue(task.id, "Failed")
        check_wo_completion(task.work_order_id)
```

---

## Authorization

### Session Scope

| Resource | Scope |
|----------|-------|
| Work Orders | Only WOs assigned to session owner |
| Tasks | Only tasks in attached WOs |
| Agents | Only agents spawned in this session |

### Delegation Token Scope

| Permission | Scope |
|------------|-------|
| Model access | Only models in `granted_models` |
| Jira access | Session owner's permissions |
| Repository access | Session workspace checkout |

---

## API Specification

### WO Runtime Daemon API (Internal)

```
# Health check
GET /health
Response: { status: "healthy", session_id, uptime_seconds }

# List attached WOs
GET /work-orders
Response: { work_orders: [{ id, scenario, status, tasks_count }] }

# Get task tree
GET /work-orders/{wo_id}/tasks
Response: { tasks: [{ id, state, scenario, dependencies }] }

# Manual task action
POST /tasks/{task_id}/action
Body: { action: "retry" | "cancel" | "complete" }
Response: { success: true }
```

### VS Code Extension API

```
# Get work orders panel data
GET /api/panel/work-orders
Response: { work_orders: [...], grouped_by_status: {...} }

# Get agent chat tabs
GET /api/panel/agents
Response: { agents: [{ id, task, status, capable_agent }] }

# Start task manually
POST /api/tasks/{task_id}/start
Response: { success: true, agent_id }
```

---

## Scalability

### Per-Session Limits

| Limit | Default | Configurable |
|-------|---------|--------------|
| Max attached WOs | 20 | Yes |
| Max concurrent agents | 10 | Yes |
| Max tasks per WO | 500 | Yes |
| Task tree depth | 5 | Yes |

### Resource Constraints

| Resource | Constraint |
|----------|------------|
| Memory per session | Coder workspace limits |
| CPU per agent | Capped at 2 cores |
| Disk for skills | 1GB max skill cache |

### Session Scaling

- One WO Runtime daemon per Workspace Session
- Sessions are user-scoped (not shared)
- Horizontal scaling by user count, not WO count

---

## Observability

### Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `wo_runtime_wos_attached` | Gauge | Currently attached WOs |
| `wo_runtime_tasks_total` | Counter | Tasks by state |
| `wo_runtime_agents_active` | Gauge | Currently running agents |
| `wo_runtime_task_duration_seconds` | Histogram | Task execution time |
| `wo_runtime_agent_spawn_duration_seconds` | Histogram | Agent spawn time |
| `wo_runtime_jira_poll_duration_seconds` | Histogram | Jira polling latency |
| `wo_runtime_failures_total` | Counter | Failures by type |

### Logging

Structured JSON logs with:

| Field | Description |
|-------|-------------|
| `session_id` | Workspace Session ID |
| `session_owner` | User identity |
| `work_order` | WO ID if applicable |
| `task` | Task ID if applicable |
| `operation` | `poll`, `spawn`, `complete`, `fail` |
| `duration_ms` | Operation duration |

### Tracing

OpenTelemetry spans for:
- Jira polling cycles
- Task tree building
- Agent harness preparation
- Agent spawn
- Task completion handling
- WO completion reporting

---

## External Dependencies

| Dependency | Integration | Failure Mode |
|------------|-------------|--------------|
| Jira (via MCP) | System of record | Retry with backoff, then pause session |
| Metadata Service | Scenario definitions | Use cache, retry in background |
| Agent Fabric | Skills, recommendations | Use cache, degrade to defaults |
| Orchestrator (MQ) | Completion notifications | Queue locally, retry delivery |
| Gateway Policy | Model access | Fail task, try fallback |

---

## Open Implementation Questions

- Exact Jira custom field IDs and project configuration per Workbench
- Coder workspace template customization for WO Runtime daemon
- Agent process isolation model (containers vs processes)
- Session persistence on Coder workspace stop/restart
- Knowledge context refresh policy
- Agent crash detection and recovery timing
- IDE extension communication protocol (WebSocket vs polling)

## Read Next

- [end-to-end-work-order-flow.md](end-to-end-work-order-flow.md) — Full WO lifecycle walkthrough
- [task-execution.md](task-execution.md) — Task tree and state machine
- [agent-spawning.md](agent-spawning.md) — Harness preparation details
- [ide-integration.md](ide-integration.md) — VS Code plugin architecture
- [../agent-fabric/requirements.md](../agent-fabric/requirements.md) — Agent infrastructure
