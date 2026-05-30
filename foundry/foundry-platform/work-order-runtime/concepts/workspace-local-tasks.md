# Workspace-Local Tasks

Workspace-Local Tasks are tasks that exist only within a Workspace Session — stored in the [Local State Store](local-state-store.md), shown in the IDE task graph, and not synced to Jira or the work repository.

## What it is

The task tree for a [Work Order](../../concepts/work-order.md) normally mirrors Jira: Scenario-generated tasks, agent-created sub-tasks, and human-completed work all sync to the Workbench project. Builders also create work that should not leave the session:

- **Manual Human Tasks** — Tasks the builder adds to the graph (title, description, parent, dependencies) without a Scenario ingress contract.
- **Agent sessions under Human Tasks** — When a builder employs agents while executing a Human Task, each session can be recorded as a workspace-local child task for tracking and graph uniformity (WO Runtime may create hidden sub-tasks internally).
- **Tasks under [Personal Work](../../concepts/personal-work.md)** — Ad-hoc agent usage associated with the session-local Personal Work WO.

Workspace-local tasks use `sync_scope = 'local'` in the Local State Store. They participate in the same DAG model (parent-child, dependencies, state machine) as synced tasks, but the Task Manager does not push them to Jira.

| Aspect | Synced task | Workspace-local task |
|--------|-------------|----------------------|
| **System of record** | Jira | Local State Store |
| **Visible in IDE graph** | Yes | Yes (greyed/light styling) |
| **Orchestrator visibility** | Yes | No |
| **Agent employment** | Per Scenario / Task Manager | Builder-initiated during Human Task or Personal Work |

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Task Manager** | Creates local tasks on builder request; resolves dependencies; does not sync to Jira |
| **Local State Store** | Authoritative store for `sync_scope = 'local'` rows |
| **Agent Spawner** | Spawns agents for local tasks using standard harness flow |
| **IDE** | Renders local nodes in the [Task Graph View](../../ide/concepts/task-graph-view.md) with distinct styling |

## Manual task creation

Builders create manual tasks from the IDE:

- **"+ Add Task"** in the task graph view, or **right-click WO → Create Task** in the sidebar.
- Fields: title, description, parent task (anywhere in the tree), optional dependencies.
- **No agent configuration at creation** — Skilled Agent, model, and I/O mode are chosen when the builder employs agents during execution.
- **[Create]** — Adds task as pending/blocked per dependencies.
- **[Create & Start]** — Adds task and transitions to In-Progress immediately; **manual Human Tasks may start with partially completed dependencies** — the builder assumes coordination responsibility.

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Task](../../concepts/task.md) | Local tasks are still Tasks in the session graph; they are not exported to UPIM work repository |
| [Work Order](../../concepts/work-order.md) | Local tasks attach under assigned WOs or Personal Work |
| Human–Agent Team | Human Tasks are the primary manual creation path; agents are employed as tools during execution |

## Related concepts

- [Task Manager](task-manager.md) — Schedules and state-transitions local tasks
- [Local State Store](local-state-store.md) — `sync_scope` and schema
- [Personal Work](../../concepts/personal-work.md) — Local-only WO for unstructured agent use
- [Agent Employment](../../ide/concepts/agent-employment.md) — Employing agents during Human Tasks

## Further reading

- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — WOR-FR-0034 through WOR-FR-0043
- [../platform-developer-guide/task-execution.md](../platform-developer-guide/task-execution.md) — Task state machine
- [../../ide/platform-developer-guide/ux-requirements.md](../../ide/platform-developer-guide/ux-requirements.md) — Manual task creation UX
