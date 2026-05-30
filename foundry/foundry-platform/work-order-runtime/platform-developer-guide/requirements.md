# Work Order Runtime Requirements

This document specifies detailed implementation requirements for the Work Order Runtime module.

## Key Concepts

This module implements several platform concepts. For definitions, see:

| Concept | Link |
|---------|------|
| Work Order | [../../concepts/work-order.md](../../concepts/work-order.md) |
| Task | [../../concepts/task.md](../../concepts/task.md) |
| Scenario | [../../concepts/scenario.md](../../concepts/scenario.md) |
| Workspace Session | [../../concepts/workspace-session.md](../../concepts/workspace-session.md) |
| Agent Model | [../../concepts/agent-model.md](../../concepts/agent-model.md) |
| Delegation | [../../concepts/delegation.md](../../concepts/delegation.md) |
| Knowledge Hierarchy | [../../concepts/knowledge-hierarchy.md](../../concepts/knowledge-hierarchy.md) |

Module-specific concepts (internals):

| Concept | Link |
|---------|------|
| WO Runtime Daemon | [../concepts/wo-runtime-daemon.md](../concepts/wo-runtime-daemon.md) |
| Task Manager | [../concepts/task-manager.md](../concepts/task-manager.md) |
| Agent Spawner | [../concepts/agent-spawner.md](../concepts/agent-spawner.md) |
| Context Compilation | [../concepts/context-compilation.md](../concepts/context-compilation.md) |
| Completion Reporter | [../concepts/completion-reporter.md](../concepts/completion-reporter.md) |
| Local State Store | [../concepts/local-state-store.md](../concepts/local-state-store.md) |
| Management Plane Interface | [../concepts/management-plane-interface.md](../concepts/management-plane-interface.md) |

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|---------------------------|
| **Workspace** | Runs within Workspace Sessions (Coder/K8s environments); does not create sessions |
| **Work Order** | Attaches, schedules, and executes WOs within sessions |
| **Task** | Manages task trees with dependencies and state transitions |
| **Agent** | Spawns Employed Agents (runtime instances of Skilled Agents) |
| **Scenario** | Reads Scenario definitions to determine task execution and agent assignment |
| **Delegation** | Generates and provides Delegation Tokens to Employed Agents |

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

**WOR-FR-0001:** The WO Runtime Daemon SHALL coordinate all WO/task execution within a Workspace Session.

**WOR-FR-0002:** The WO Runtime Daemon SHALL start with the workspace container, run continuously, and stop when the session stops. WO Runtime does not create sessions — it boots inside a pod provisioned by Session Infrastructure and acknowledges liveness to Session Management.

| Aspect | Detail |
|--------|--------|
| Responsibility | Coordinate all WO/task execution within a Workspace Session |
| Lifecycle | Starts with workspace, runs continuously, stops with workspace |
| Input | Assigned WOs from Jira, scenario definitions from Metadata Service |
| Output | Task state changes, completion notifications |
| Dependencies | Jira MCP, Metadata Service, Agent Fabric |

### Jira Poller

**WOR-FR-0003:** The Jira Poller SHALL poll for assigned Work Orders and tasks.

**WOR-FR-0004:** The default polling interval SHALL be 5 seconds (configurable).

| Aspect | Detail |
|--------|--------|
| Responsibility | Poll for assigned Work Orders and tasks |
| Polling interval | 5 seconds (configurable) |
| Input | Session owner identity |
| Output | List of assigned WOs and task tree updates |
| Dependencies | Jira MCP Server |

### Task Manager

**WOR-FR-0005:** The Task Manager SHALL manage task tree, dependencies, and state transitions.

**WOR-FR-0006:** The Task Manager SHALL identify ready tasks (dependencies met) for scheduling.

| Aspect | Detail |
|--------|--------|
| Responsibility | Manage task tree, dependencies, state transitions |
| Input | Task events (created, updated, completed) |
| Output | Ready tasks for scheduling, state transitions |
| Dependencies | Local SQLite state, Jira MCP |

### Agent Spawner

**WOR-FR-0007:** The Agent Spawner SHALL prepare harness and spawn Employed Agents for ready tasks.

**WOR-FR-0008:** The Agent Spawner SHALL select a Capable Agent with fallback support.

| Aspect | Detail |
|--------|--------|
| Responsibility | Prepare harness and spawn Employed Agents |
| Input | Ready tasks with Skilled Agent definitions |
| Output | Running agent processes |
| Dependencies | Skill Registry, Metadata Service, Gateway Policy |

### Completion Reporter

**WOR-FR-0009:** The Completion Reporter SHALL notify the Orchestrator when WOs reach terminal state.

**WOR-FR-0010:** The Completion Reporter SHALL send `work-order-completed`, `work-order-failed`, or `task-blocked` messages via message queue.

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

**WOR-FR-0011:** Jira integration SHALL use MCP (Model Context Protocol) for bidirectional communication.

**WOR-FR-0012:** Jira authentication SHALL use the session owner's Jira credentials via delegation.

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

**WOR-FR-0013:** Metadata Service queries SHALL be cached with a session-scoped 5-minute TTL.

**WOR-FR-0014:** The WO Runtime SHALL query Scenario definitions once per unique scenario per session.

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

**WOR-NFR-0001:** For Jira MCP timeouts, the WO Runtime SHALL retry immediately up to 3 times.

**WOR-NFR-0002:** When Metadata Service is unavailable, the WO Runtime SHALL use cached values and retry in background.

**WOR-FR-0015:** On agent spawn failure, the WO Runtime SHALL try fallback agents before entering recoverable failure.

**WOR-FR-0016:** On agent crash, the WO Runtime SHALL retry the task up to 2 times.

**WOR-FR-0017:** When model is rate limited, the WO Runtime SHALL pause the task and retry when quota resets.

| Failure Type | Strategy |
|--------------|----------|
| Jira MCP timeout | Retry immediately, up to 3 times |
| Metadata Service unavailable | Use cached value, retry in background |
| Agent spawn failure | Try fallback agent, then recoverable failure |
| Agent crash | Retry task up to 2 times |
| Model rate limited | Pause task, retry when quota resets |

### Recoverable Failures

**WOR-FR-0018:** When quota is exhausted, the task SHALL enter `blocked` state and resume when quota refreshes.

**WOR-FR-0019:** When an agent is disabled, the task SHALL enter `blocked` state and resume when agent is re-enabled.

**WOR-FR-0020:** When all fallback agents fail, the task SHALL enter `blocked` state and resume when any option is restored.

**WOR-FR-0021:** When a model is unavailable, the task SHALL enter `blocked` state and resume when model becomes available.

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

**WOR-NFR-0003:** Work Orders visible to a session SHALL be limited to WOs assigned to the session owner.

**WOR-NFR-0004:** Tasks visible to a session SHALL be limited to tasks in attached WOs.

**WOR-NFR-0005:** Agents visible to a session SHALL be limited to agents spawned in that session.

| Resource | Scope |
|----------|-------|
| Work Orders | Only WOs assigned to session owner |
| Tasks | Only tasks in attached WOs |
| Agents | Only agents spawned in this session |

### Delegation Token Scope

**WOR-NFR-0006:** Delegation tokens SHALL grant model access only to models in `granted_models`.

**WOR-NFR-0007:** Delegation tokens SHALL grant Jira access at session owner's permission level.

**WOR-NFR-0008:** Delegation tokens SHALL grant repository access only to session workspace checkout.

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

**WOR-NFR-0009:** The default maximum attached WOs per session SHALL be 20 (configurable).

**WOR-NFR-0010:** The default maximum concurrent agents per session SHALL be 10 (configurable).

**WOR-NFR-0011:** The default maximum tasks per WO SHALL be 500 (configurable).

**WOR-NFR-0012:** The default maximum task tree depth SHALL be 5 (configurable).

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

---

## Management Plane Interface

WO Runtime communicates with [Workspace Session Management](../../workspace-session-management/README.md) as an in-session worker. See [../concepts/management-plane-interface.md](../concepts/management-plane-interface.md).

**WOR-FR-0030:** On boot, WO Runtime SHALL send liveness acknowledgment to Session Management within 30 seconds.

**WOR-FR-0031:** WO Runtime SHALL send heartbeat to Session Management every 15 seconds while the session is Active.

**WOR-FR-0032:** On receiving stop or drain command (via heartbeat response or explicit API), WO Runtime SHALL drain active tasks within the configured grace period, then send shutdown acknowledgment.

**WOR-FR-0033:** WO Runtime SHALL expose `GET /health` for Kubernetes readiness and liveness probes.

| Aspect | Detail |
|--------|--------|
| Liveness ack endpoint | Session Management `POST /api/v1/sessions/{id}/ack` |
| Heartbeat interval | 15 seconds |
| Grace period on stop | Configurable; default 30 seconds |
| Health probe | `/health` returns `{ status, session_id, uptime_seconds }` |

---

## Open Implementation Questions

- Exact Jira custom field IDs and project configuration per Workbench
- Coder workspace template customization for WO Runtime daemon (owned by Session Infrastructure)
- Session persistence on stop/restart (owned by Session Management + Session Infrastructure)
- Knowledge context refresh policy
- Agent crash detection and recovery timing
- IDE extension communication protocol (WebSocket vs polling)

## Read Next

- [../user-guide/work-order-lifecycle.md](../user-guide/work-order-lifecycle.md) — Full WO lifecycle walkthrough
- [task-execution.md](task-execution.md) — Task tree and state machine
- [agent-spawning.md](agent-spawning.md) — Harness preparation details
- [ide-integration.md](ide-integration.md) — VS Code plugin architecture
- [../agent-fabric/platform-developer-guide/requirements.md](..//agent-fabric/platform-developer-guide/requirements.md) — Agent infrastructure
