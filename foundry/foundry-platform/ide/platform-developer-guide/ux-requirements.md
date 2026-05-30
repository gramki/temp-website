# IDE UX Requirements

This document captures UX decisions and mockup requirements for the Foundry IDE, based on design discussions. These inform the Figma mockups and eventual implementation.

## Base Interface

- **IDE-UX-001:** The Foundry IDE SHALL use VS Code (Code Server) as the base interface.
- **IDE-UX-002:** The IDE experience SHALL resemble GitHub Codespaces — per-builder, per-Workspace sessions accessed via browser.

## Overall Layout

- **IDE-UX-003:** The IDE layout SHALL follow standard VS Code structure: Title Bar, Activity Bar (left icons), Sidebar, Editor Area, Bottom Panel, Status Bar.
- **IDE-UX-004:** The right panel SHALL be the Employed Agents Panel (not a chat panel). All agent interaction happens in editor tabs.
- **IDE-UX-005:** Agent chat and terminal output SHALL open as editor tabs, not as fixed panels. Users can pull tabs into separate windows.

## Title Bar

- **IDE-UX-006:** Title bar SHALL show macOS-style window chrome with Foundry branding: "Foundry IDE — {Workspace Type} Workspace — {branch name}".

## Activity Bar

- **IDE-UX-007:** Activity bar SHALL include standard VS Code icons plus a dedicated "Work Orders" icon.
- **IDE-UX-008:** The Work Orders icon SHALL have a highlight/active indicator (blue left border) when selected.

## Sidebar — Work Orders Panel

- **IDE-UX-009:** The sidebar SHALL show assigned Work Orders as a tree view with task trees underneath.
- **IDE-UX-010:** Each WO entry SHALL show: WO ID (as a link), status badge, and title.
- **IDE-UX-011:** Task tree entries SHALL show: status icon (checkmark, spinner, circle, blocked), task title, and [Agent]/[Human] type indicator.
- **IDE-UX-012:** Status badges SHALL use color coding: green = completed, amber = in-progress, gray = pending/blocked, red = failed.
- **IDE-UX-013:** Clicking a WO SHALL open a "WO Detail + Task Graph" tab in the editor area.
- **IDE-UX-014:** Personal Work SHALL appear in the sidebar with a "local only" visual indicator, distinguished from synced WOs.

## Sidebar — Context Panel

- **IDE-UX-015:** Below the Work Orders tree, a "CONTEXT" section SHALL display pre-loaded product context: Product, Module, OI, Workbench.

## Employed Agents Panel (Right)

- **IDE-UX-016:** The right panel SHALL show a list of ALL employed agents across all WOs in the workspace session.
- **IDE-UX-017:** The panel SHALL support searching, sorting, and filtering controls (by WO, by status, by agent type).
- **IDE-UX-018:** Filters can narrow to a single WO; default shows all agents.
- **IDE-UX-019:** Each agent entry SHALL be multi-line ("fat entry") showing:
  - Status badge: WAITING FOR INPUT (amber/pulsing) / WORKING (green) / COMPLETED (checkmark) / FAILED (red) / QUEUED (gray)
  - WO ID > Task ID (breadcrumb)
  - Task title
  - Skilled Agent name (Capable Agent / Model)
  - Duration
  - For WAITING state: snippet of what the agent is waiting on
- **IDE-UX-020:** A clear visual indicator SHALL distinguish agents waiting for user input from agents that are working autonomously.
- **IDE-UX-021:** Clicking an agent entry SHALL open its output tab in the main editor.
- **IDE-UX-022:** Multi-agent tasks SHALL show each agent as a separate entry with a "(1/N)" indicator.

## WO Detail + Task Graph Tab (Frame 2)

- **IDE-UX-023:** Clicking a WO opens an editor tab with the WO detail page.
- **IDE-UX-024:** The editor area SHALL be horizontally split: top = WO Detail, bottom = Task Execution Graph.
- **IDE-UX-025:** The WO Detail section SHALL be collapsible (collapse/expand toggle) and resizable (drag handle between sections).
- **IDE-UX-026:** WO Detail (top half) SHALL mirror the web app's WO detail page:
  - WO ID + Title + Status badge
  - Scenario name
  - Parent Orchestration Item (e.g., PI-89 "Secure Login")
  - Track + Workspace type
  - Assigned to
  - Description / Acceptance criteria
  - Context links (OI, Workbench, related PRs)
- **IDE-UX-027:** Task Execution Tree (bottom half) SHALL render tasks as a **folder-style tree** (indented rows with expand/collapse), similar to the VS Code Explorer — not a node-and-arrow DAG layout.
- **IDE-UX-028:** Each tree row SHALL show: expand/collapse chevron (if children), status icon, Task ID + title, `[Agent]` / `[Human]` indicator, optional agent name, duration.
- **IDE-UX-029:** Task tree status colors: green = completed, amber = in-progress, gray = pending/blocked, red = failed, pulsing/accent for "waiting for input".
- **IDE-UX-030:** Task tree rows SHALL be clickable — clicking opens the agent output tab or Human Task tab for that task.
- **IDE-UX-031:** Workspace-local tasks (not synced to Jira) SHALL appear in the tree with greyed/light font — clearly distinguishable from synced tasks while keeping the same tree structure.
- **IDE-UX-032:** Cross-task **dependencies** SHALL be shown inline (e.g. muted `blocked on TASK-892`) or as a badge on the row — not as arrows between tree nodes.

## Agent Output Tabs — Live (Chat Mode)

- **IDE-UX-033:** Live agent output SHALL open as an editor tab with: task header bar + full chat transcript + input field.
- **IDE-UX-034:** Task header bar SHALL show: Task ID, title, status badge, WO breadcrumb, Skilled Agent (Capable Agent / Model), skills used, start time, dependencies, and action buttons ([Back to Graph] [Pause] [Cancel]).
- **IDE-UX-035:** Live chat tabs SHALL have a green left-border or banner: "LIVE — you can send messages".
- **IDE-UX-036:** Chat transcript SHALL show chronological messages with sender label, timestamp, and message content.
- **IDE-UX-037:** Agent approval prompts SHALL render inline with action buttons (e.g., [Approve] [Reject] [Ask question]).
- **IDE-UX-038:** An active input field SHALL appear at the bottom for sending messages to the agent.

## Agent Output Tabs — Live (Terminal Mode)

- **IDE-UX-039:** Live terminal output SHALL open as an editor tab with: task header bar + monospace terminal output + cursor prompt.
- **IDE-UX-040:** Terminal content SHALL use a monospace font (JetBrains Mono or equivalent).
- **IDE-UX-041:** Terminal tabs SHALL have a green left-border or banner indicating live/interactive state.

## Agent Output Tabs — Completed (Read-Only)

- **IDE-UX-042:** Completed agent output SHALL open as a read-only editor tab.
- **IDE-UX-043:** Completed tabs SHALL have a muted/gray left-border or banner: "COMPLETED — read-only transcript".
- **IDE-UX-044:** No input field SHALL appear at the bottom for completed transcripts.
- **IDE-UX-045:** Completed tabs SHALL have a slightly dimmer background for the transcript area.
- **IDE-UX-046:** An "Artifacts produced" section SHALL appear at the bottom listing files/outputs created by the agent.
- **IDE-UX-047:** Action buttons for completed tabs: [Back to Graph] [Re-run] [View Artifacts]. "View Artifacts" opens produced files in the editor.
- **IDE-UX-048:** Completed terminal logs SHALL support [Search log] [Copy all] [Download] actions.

## Agent Output Tabs — Failed

- **IDE-UX-049:** Failed agent output SHALL display a red banner with error summary at the top of the transcript.
- **IDE-UX-050:** Action buttons for failed tabs: [Back to Graph] [Retry] [Escalate to Human] [Cancel].
- **IDE-UX-051:** The error summary SHALL include: what the agent attempted, the failure reason, and relevant context.

## Manual Task Creation (Frame 7)

- **IDE-UX-052:** Builders SHALL be able to create tasks via: (a) "+ Add Task" button in the Task Graph view, (b) right-click WO in sidebar > "Create Task".
- **IDE-UX-053:** Task creation SHALL use a modal dialog with the following fields:
  - Work Order (fixed to current WO)
  - Title (required)
  - Description
  - Parent Task (tree picker — where to attach in the graph, parent-child relationship)
  - Depends on (multi-select from existing tasks in the WO)
- **IDE-UX-054:** Manual tasks can be placed anywhere in the tree, including under Scenario-generated tasks. The parent-child placement is a structural relationship, not a dependency.
- **IDE-UX-055:** Agent selection, model override, and I/O mode SHALL NOT be part of the task creation dialog. Agents are employed during task execution, not at creation time.
- **IDE-UX-056:** A "Description" field SHALL accept free-text task instructions. The method of providing richer context (file attachments, code references, drag-drop) depends on the Capable Agent employed later.
- **IDE-UX-057:** Two submit actions: [Create] (adds to graph as pending) and [Create & Start] (adds to graph AND immediately transitions to In-Progress — builder is picking it up now).
- **IDE-UX-058:** "Create & Start" SHALL work even with partially completed dependencies. Manual Human Tasks are not blocked by unmet dependencies — the builder takes responsibility for coordination.

## Agent Employment During Execution

- **IDE-UX-071:** Builders SHALL be able to employ agents during a Human Task via two entry points:
  - (a) From within the Human Task's editor tab: "[+ Employ Agent]" button spawns an agent pre-associated with that task, inheriting its context.
  - (b) From anywhere in the IDE (e.g., opening a new agent session, command palette): the system prompts the builder to associate the session with a task.
- **IDE-UX-072:** When starting an agent session from outside a task context, the system SHALL prompt: "Associate this agent session with:" showing a picker listing active Human Tasks and "Personal Work" as a fallback.
- **IDE-UX-073:** The system SHALL NOT auto-assign agent sessions to pending Human Tasks. It SHALL always prompt the builder to choose.
- **IDE-UX-074:** The builder can always choose "Personal Work" for ad-hoc exploration not tied to any specific task.
- **IDE-UX-075:** Each employed agent session is tracked independently under the parent Human Task. There is no formal sequential/parallel orchestration — multi-agent coordination is the builder's workflow.
- **IDE-UX-076:** Agent sessions employed within a Human Task are workspace-local (not synced to Jira). They appear in the task graph with the local-only visual treatment (greyed/light).
- **IDE-UX-077:** The Employed Agents Panel (right) shows all active agent sessions regardless of whether they were started from within a task or via the general entry point.

## Bottom Panel — Terminal

- **IDE-UX-059:** The bottom terminal panel SHALL show tabs: AGENT TERMINAL (active/first), TERMINAL, OUTPUT, PROBLEMS.
- **IDE-UX-060:** The active terminal tab SHALL have a blue underline indicator.
- **IDE-UX-061:** Terminal content SHALL use a monospace font (JetBrains Mono or equivalent).

## Status Bar

- **IDE-UX-062:** Status bar SHALL show: active WO status, git branch, problems count, file type, cursor position, Foundry version.
- **IDE-UX-063:** Status bar background SHALL use VS Code's blue theme color.

## Notifications

- **IDE-UX-064:** Notification toasts SHALL appear in the top-center of the editor area (not overlapping the right panel).
- **IDE-UX-065:** Notifications SHALL fire for: new WO assigned, task ready, agent waiting for input, task completed, task failed, WO completed.
- **IDE-UX-066:** Each notification SHALL include a dismiss button and optionally an action button (e.g., "Open" to jump to the relevant task).

## Navigation Model

- **IDE-UX-067:** All views (WO detail, task graph, agent output) open as editor tabs following VS Code's native tab model.
- **IDE-UX-068:** Tabs can be dragged out into separate windows for side-by-side viewing.
- **IDE-UX-069:** Agent output tabs are navigable from: (a) clicking task nodes in the graph, (b) clicking entries in the Employed Agents panel, (c) notifications.
- **IDE-UX-070:** "Back to Graph" navigation in agent output tabs SHALL return focus to the WO Detail + Task Graph tab.

## Sidebar — Foundry Workspace Panel

Module concept: [Foundry Workspace Panel](../concepts/foundry-workspace-panel.md).

- **IDE-UX-078:** The sidebar SHALL include a collapsible **Foundry Workspace** section, placed above the Work Orders tree by default.
- **IDE-UX-079:** The panel SHALL display workspace metadata: name, ID, workspace type, and environment (dev / staging / prod).
- **IDE-UX-080:** The panel SHALL display workbench metadata: workbench name, team summary, and product scope.
- **IDE-UX-081:** A **Quick Links** subsection SHALL list related Git repositories and external links (Jira, Confluence, dashboards). Clicking a repo link SHALL reveal the path in Explorer or open the repo root; external links SHALL open in the browser.
- **IDE-UX-082:** A **WO Runtime Settings** subsection SHALL expose session-scoped settings (default capable agent, quota summary, approval policies, work-context sync interval). Writable settings SHALL persist via WO Runtime for the active session.
- **IDE-UX-083:** Collapse/expand state for the Foundry Workspace section SHALL persist for the builder across sessions (local IDE preference).
- **IDE-UX-084:** When WO Runtime metadata is unavailable (degraded mode), the panel SHALL show a clear placeholder and retry affordance without blocking the Work Orders Panel.

## Sidebar — Work Orders Panel (Historic Work)

- **IDE-UX-085:** The Work Orders Panel SHALL support a **Historic Work** view in addition to active assigned WOs.
- **IDE-UX-086:** Historic view SHALL be toggled via a control in the panel header (e.g. "Active" / "Historic" segmented control or filter chip).
- **IDE-UX-087:** Historic WOs SHALL support filters: status (completed, failed, cancelled), date range, and scenario name.
- **IDE-UX-088:** Historic WOs SHALL support sort: by completion date (default), duration, and task count.
- **IDE-UX-089:** The panel SHALL support search across WO ID, title, and task titles (debounced typeahead).
- **IDE-UX-090:** Opening a historic WO SHALL use the same WO Detail + Task Graph tab as active WOs; task tree and agent output tabs SHALL be read-only when the WO is terminal.

## Create Scenario Journey

Module concept: [Scenario Authoring](../concepts/scenario-authoring.md).

- **IDE-UX-091:** Builders SHALL create scenarios via: (a) Command Palette — "Foundry: Create Scenario", (b) context menu on `user-work-catalog/` in Explorer — "Create Scenario".
- **IDE-UX-092:** Create Scenario SHALL open a modal with fields: Scenario name (required), trigger type (Ingress / Internal), optional parent scenario (searchable catalog picker).
- **IDE-UX-093:** Ingress SHALL map to `scope: workspace-ingress`; Internal SHALL map to `scope: workspace-internal`.
- **IDE-UX-094:** On submit, the IDE SHALL scaffold `scenario.yaml`, `skilled-agent.yaml`, and `agent-skill.md` under `user-work-catalog/work-catalog/{track}/{oi-type}/{workspace}/scenarios/{name}/`.
- **IDE-UX-095:** After scaffold, the IDE SHALL open `scenario.yaml` in the Scenario Editor and reveal the new folder in Explorer.
- **IDE-UX-096:** Parent scenario selection SHALL be optional; when set, the scaffold SHALL include an `extends:` reference and copy applicable defaults without modifying the parent file.
- **IDE-UX-097:** Create Scenario SHALL NOT require an active Work Order or Orchestration Item context.
- **IDE-UX-098:** Validation errors from WO Runtime or catalog schema SHALL surface inline in the modal before scaffold completes.

## Workspace Explorer View

Module concept: [Workspace Folder Structure](../concepts/workspace-folder-structure.md).

- **IDE-UX-099:** The VS Code Explorer SHALL reflect the session folder root `$HOME/<workbench>-<workspace>/` with top-level folders: `workbench-knowledge/`, `user-work-catalog/`, `workspace-work-catalog/`, `work-orders/`.
- **IDE-UX-100:** Read-only roots (`workbench-knowledge/`, `workspace-work-catalog/`) SHALL use a visual indicator (badge, dimmed label, or lock icon) distinct from writable roots.
- **IDE-UX-101:** Under `work-orders/WO-{id}/`, Explorer SHALL show `work-context/` and `repos/` as expandable children.
- **IDE-UX-102:** Under `repos/`, each cloned product repo SHALL appear as a workspace folder root with the active `wo/WO-{id}` branch indicated in the status bar when that WO is focused.
- **IDE-UX-103:** `work-context/` SHALL display OI-scoped artifacts using the OI-type convention layout; the IDE does not enforce a fixed subdirectory schema.
- **IDE-UX-104:** Explorer or a work-context decoration SHALL show work-context sync status: last sync time from `work-context/.sync/last-sync.json` and optional pending-change indicator when WO Runtime reports drift.

## Figma Mockup Frames

The following frames SHALL be created in the Figma file (`lgbHENxIZV4deGmSyk6u2p`):

| Frame | Title | Key Content |
|-------|-------|-------------|
| 0 | Default State | Code editing + Employed Agents Panel (right) — update existing frame |
| 1 | WO Detail + Task Graph | Editor tab with collapsible WO detail (top) + folder-style task tree (bottom) |
| 2 | Agent Chat — Live | Task header + live chat transcript + input + green "LIVE" banner |
| 3 | Agent Chat — Completed | Same layout, muted banner, no input, artifacts section |
| 4 | Agent Terminal — Live | Task header + live terminal output + monospace + green banner |
| 5 | Agent Terminal — Completed | Read-only log, muted, artifacts, [Re-run] |
| 6 | Task Failed | Red banner, error summary, [Retry] / [Escalate to Human] |
| 7 | Create Task Dialog | Modal with task metadata fields (title, description, parent, dependencies). No agent config. |
| 8 | Employ Agent Prompt | Task association picker shown when starting an agent session from outside a task context |
| 9 | Foundry Workspace Panel | Collapsible sidebar: workspace/workbench info, quick links, WO Runtime settings |
| 10 | Work Orders — Historic | Historic WO list with filter, sort, and search controls |
| 11 | Create Scenario Dialog | Modal: name, trigger type (Ingress/Internal), parent scenario picker |
| 12 | Workspace Explorer | Multi-root Explorer with work-context expanded and sync status |

Frames 0 and 1 SHALL include the Foundry Workspace Panel (expanded in Frame 0, collapsed in Frame 1).

## Open Design Questions

- Exact icon set for Activity Bar (use VS Code Codicons or custom Foundry icons?)
- Virtualization for very large task trees (>100 rows)
- Keyboard shortcuts for common actions (create task, jump to waiting agent, etc.)
- Accessibility requirements for color-coded status indicators (patterns/shapes in addition to color)
- Animation/transition behavior when task states change in the graph
- "[+ Employ Agent]" button placement within the Human Task tab (header bar? floating action? bottom toolbar?)
