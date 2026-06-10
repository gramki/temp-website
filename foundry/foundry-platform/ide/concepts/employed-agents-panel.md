# Employed Agents Panel

The Employed Agents Panel is the right-side VS Code view that lists every agent session employed in the current Workspace Session, across all Work Orders and Personal Work.

## What it is

Previously, agent interaction was surfaced as ad-hoc chat tabs. The Employed Agents Panel centralizes **who is working, on what, and in what state** — while full conversation and terminal output open in editor tabs when the builder selects an entry.

The panel shows all employed agents in the session. Filters can narrow the list to a single Work Order; default is session-wide.

Each entry is a multi-line ("fat") row:

| Field | Purpose |
|-------|---------|
| Status badge | `WAITING FOR INPUT`, `WORKING`, `COMPLETED`, `FAILED`, `QUEUED` |
| WO > Task breadcrumb | e.g. `WO-1234 › TASK-892` or Personal Work |
| Task title | Human-readable task name |
| Trained Agent | Label from manifest (Raw Agent / model) |
| Duration | Elapsed time |
| Status snippet | For waiting agents — e.g. "Approve PR?" |

Status indicators must clearly distinguish agents waiting for builder input from those working autonomously.

Panel controls:

- **Search** — Filter by task title, WO ID, agent name
- **Sort** — By status, duration, WO, recency
- **Filter** — By WO, by status, by executor context

Clicking an entry opens the agent's **Agent Output Tab** in the main editor (live or read-only per session state).

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **IDE** | Renders the panel; handles search/sort/filter UX |
| **WO Runtime** | Pushes `AgentSessionEvent` updates (WOR-FR-0038) |
| **Agent Fabric** | Trained Agent labels and Raw Agent metadata |

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| **Agent** | Employed Agents are runtime instances; the panel is the session-wide roster |
| Human–Agent Team | Builder monitors and responds to agents from one surface |
| [Work Order](../../concepts/work-order.md) | Entries are grouped/filtered by WO |

## Related concepts

- [Agent Employment](agent-employment.md) — How agents are started and associated with tasks
- [Task Graph View](task-graph-view.md) — Alternative navigation into the same output tabs
- [Builder](builder.md) — Primary user of the panel

## Further reading

- [../platform-developer-guide/ux-requirements.md](../platform-developer-guide/ux-requirements.md) — IDE-UX-016 through IDE-UX-022
- [../../work-order-runtime/platform-developer-guide/ide-integration.md](../../work-order-runtime/platform-developer-guide/ide-integration.md) — Employed Agents Panel data flow
