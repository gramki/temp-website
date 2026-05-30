# Agent Employment

Agent Employment is how a Builder invokes agents during work in a Workspace Session — associating each agent session with a Human Task, a workspace-local sub-task, or Personal Work.

## What it is

Agent employment is **not** configured when creating a manual task. The Create Task dialog captures title, description, parent placement, and dependencies only. Agents are employed **during execution**, when the builder needs help.

### Entry points

1. **From a Human Task tab** — `[+ Employ Agent]` spawns an agent pre-associated with that task. The agent inherits task and WO context from the [Knowledge Hierarchy](../../concepts/knowledge-hierarchy.md) (Foundry → Workshop → Workbench → WO → task instructions).

2. **From anywhere in the IDE** — Starting a general agent session (command palette, Capable Agent CLI, etc.) triggers the **task association prompt**: "Associate this agent session with:" listing in-progress Human Tasks and **Personal Work**. The system never auto-assigns to a pending Human Task.

The builder may always choose **Personal Work** for unstructured exploration. That routes the session to the [Personal Work](../../concepts/personal-work.md) WO (workspace-local, not synced to Jira).

### Multi-agent coordination

There is no formal sequential/parallel orchestration at the platform level. A builder may employ multiple agents on one Human Task over time; WO Runtime tracks each session independently (and may record each as a workspace-local child task for graph uniformity). Coordination is the builder's workflow.

Context provision (free text, files, code references) depends on what the employed **Capable Agent** supports — not a fixed IDE form at employment time.

### Quota and delegation

All employed agents use the builder's [Delegation](../../concepts/delegation.md) token and Access Gateway quota, whether under an orchestrated WO, a local task, or Personal Work.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **IDE** | `[+ Employ Agent]`, association prompt UI, opens Agent Output Tabs |
| **WO Runtime** | Spawns agents, associates sessions, records local tasks (WOR-FR-0036, WOR-FR-0037) |
| **Agent Fabric** | Skilled Agent resolution at spawn time (from task Scenario or default for Personal Work) |

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| Human–Agent Team | Builder is executor; agents are tools during Human Tasks |
| [Agent Model](../../concepts/agent-model.md) | Employment creates Employed Agent instances |
| [Task](../../concepts/task.md) | Sessions scoped to a task or Personal Work |

## Related concepts

- [Employed Agents Panel](employed-agents-panel.md) — Roster of all employed agents
- [Task Graph View](task-graph-view.md) — Graph navigation into tasks and sessions
- [Workspace-Local Tasks](../../work-order-runtime/concepts/workspace-local-tasks.md) — Local tracking for agent sessions
- [Personal Work](../../concepts/personal-work.md) — Fallback WO for unscoped agent use
- [Builder](builder.md) — Who employs agents

## Further reading

- [../platform-developer-guide/ux-requirements.md](../platform-developer-guide/ux-requirements.md) — IDE-UX-071 through IDE-UX-077, Frame 8
- [../../work-order-runtime/platform-developer-guide/ide-integration.md](../../work-order-runtime/platform-developer-guide/ide-integration.md) — Task Association Prompt protocol
