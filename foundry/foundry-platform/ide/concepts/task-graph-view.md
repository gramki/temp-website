# Task Graph View

The Task Graph View is an editor-tab visualization of a Work Order's task tree — a **folder-tree** layout (like the VS Code Explorer) showing parent-child structure, status, and navigation into agent output. Dependencies are shown inline or as badges, not as a separate graph layout.

## What it is

When a builder selects a Work Order from the sidebar, the IDE opens a tab with:

1. **WO Detail** (top, collapsible and resizable) — Metadata aligned with the Foundry Web App WO detail page: ID, title, status, Scenario, parent OI, track, workspace, assignment, description, acceptance criteria.
2. **Task Tree** (bottom) — Indented, expandable tree of all tasks for that WO, including [workspace-local](../../work-order-runtime/concepts/workspace-local-tasks.md) tasks.

Each tree row shows:

- Expand/collapse chevron when the task has children
- Status icon (checkmark, spinner, circle, blocked, waiting-for-input accent)
- Task ID and title on one line (truncated with tooltip when long)
- Secondary columns or trailing text: `[Agent]` / `[Human]`, agent name, duration
- Dependency hint when blocked — e.g. `blocked on TASK-892` in muted text (not drawn as graph edges)

**Synced tasks** use standard row styling. **Local-only tasks** use greyed or light typography so builders see the sync boundary while keeping the same tree structure.

Rows are clickable:

- Agent task or agent session under a Human Task → opens **Agent Output Tab**
- Human Task in progress → opens Human Task workspace tab (with [+ Employ Agent] affordance)

The tree is built from WO Runtime payload (WOR-FR-0039): flat or nested nodes with `parentTaskId`, `dependencies`, `syncScope`, and agent summary fields. The IDE renders parent-child as indentation; cross-task dependencies do not change indent level.

## Tree layout conventions

| Element | Behavior |
|---------|----------|
| **Root** | WO root task at depth 0 |
| **Indent** | One level per parent-child link |
| **Expand/collapse** | Per node with children; remember state per WO tab in `workspaceState` |
| **Sort** | Siblings ordered by creation or stable task ID (implementation choice) |
| **+ Add Task** | Toolbar action; new row attaches under selected parent in the tree picker |

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **IDE** | Tree view rendering, expand/collapse, collapse/resize of WO detail, click navigation |
| **WO Runtime** | Authoritative task tree (parent-child + dependencies) including local tasks |
| **Web App** | WO detail content model (IDE embeds or mirrors) |

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Task](../../concepts/task.md) | Rows are tasks; parent-child is tree structure; dependencies are metadata |
| [Work Order](../../concepts/work-order.md) | Tree is scoped to one WO per tab |
| [IDE](../../ace/concepts.md#ide) | Task tree is the execution monitor for builders |

## Related concepts

- [Employed Agents Panel](employed-agents-panel.md) — Session-wide agent list; same output tabs on click
- [Agent Employment](agent-employment.md) — Creating agent sessions from Human Task nodes
- [Workspace Views](workspace-views.md) — Workspace-type framing around the IDE shell

## Further reading

- [../platform-developer-guide/ux-requirements.md](../platform-developer-guide/ux-requirements.md) — IDE-UX-023 through IDE-UX-032
- [../../work-order-runtime/platform-developer-guide/task-execution.md](../../work-order-runtime/platform-developer-guide/task-execution.md) — DAG and state machine
