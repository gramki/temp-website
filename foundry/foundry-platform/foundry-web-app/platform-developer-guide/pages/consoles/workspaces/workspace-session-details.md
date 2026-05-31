# Workspace Session Details

**URL pattern:** `/workbenches/{workbenchId}/sessions/{sessionId}`

**Group:** Workspaces detail page (shared by all workspace consoles)

**Purpose:** Canonical session-level contract for execution, observability, and drill-down behavior.

---

## Canonical Contract

This page is the source of truth for Workspace Session details. Any "View session" action from Workspaces, Team, or My Work must deep-link to this route and follow this page contract.
The contract is field/behavior authoritative. Visual treatment (badges vs plain metadata rows) is implementation-defined as long as required information remains present and readable.

Page layout:
- Main column: Session Overview, Linked Work Orders, Coder Pod, Employed Agents, Token Usage.
- Right rail: Session Activity (single unified event stream).

---

## 1. Session Overview

Displays session metadata only (no PI details, no WO detail content):

| Field | Behavior |
|------|----------|
| Owner | Session owner identity |
| Workspace type | One of the ACE workspace types |
| Status | Session status (active/closed/etc.) |
| Started | Session start timestamp |
| Last updated | Most recent update timestamp |
| Elapsed | Duration from start to now (or close) |

### Launch IDE action

`Launch IDE` follows a two-step flow:
1. Open the remote pod session URL first.
2. Attach VS Code to that remote pod session.

---

## 2. Linked Work Orders

Shows linked Work Orders as summary cards only:
- WO ID and title
- Status
- Stage
- Elapsed time within current session

Click behavior:
- Card click navigates to Work Order Details route: `/workbenches/{workbenchId}/work-orders/{woId}`.
- The session page does not embed full Work Order detail content.

---

## 3. Coder Pod

Session-scoped coder pod observability section.

### Required blocks

| Block | Behavior |
|------|----------|
| Active pod | Exactly one active pod for the session |
| Pod history | Prior pods associated with the same session |
| Monitoring link | External link to pod monitoring/telemetry |

### Pod detail panels

Each pod detail view includes:
- Metadata panel
- Conditions panel
- Resources panel
- Security context panel
- Controlled-by style panel

---

## 4. Employed Agents

Session-scoped agent usage only.

### Time windows

- All
- Today
- 24h
- 7d

### Required views

| View | Behavior |
|------|----------|
| Agent list | Agents active in this session for selected window |
| Skills by agent | All invoked skills grouped by agent |
| Invocation counts | Invocation count per skill per agent |
| Agent detail dialog | Clicking an agent card opens a detailed usage log dialog |

### Interaction and log behavior

- Agent list should be rendered as rich summary cards (invocations, skill count, top skills).
- Selecting/clicking an agent card opens an agent usage log dialog.
- Dialog log must be chronological and timestamped.
- Dialog log should include per-session entries and skill invocation entries.
- Session IDs in the log should deep-link to Workspace Session Details.

### Log format expectations

The log should follow observability-style structured lines with the following fields:
- Timestamp (RFC3339/ISO8601 UTC form recommended)
- Event name (for example: `session.start`, `agent.summary`, `skill.invocation`, `session.end`)
- Context fields (session id/title, owner, invocation counts, skill counts)
- Optional level marker (for example: `INFO`, `WARN`)

---

## 5. Token Usage

Tokscale-inspired token and cost panels for the current session.

### Required views

| View | Behavior |
|------|----------|
| Session totals | Aggregate input/output/total tokens |
| Tokens per day timeline | Daily token chart for the session (tokscale-inspired) |
| Daily log | Readable per-day token and cost rows with timestamps |
| Model breakdown | Token usage by model |
| Agent breakdown | Token usage by agent |
| Page agent token view | Token view scoped to page agents |
| Cost | USD only (no multi-currency rendering) |

### Breakdown detail expectations

- Model breakdown should include token detail fields: input, output, cache-read, cache-write.
- Model and agent breakdowns should support ranking by cost and show relative contribution/share.

---

## 6. Session Activity (Right Rail)

Single unified chronological stream in the right rail.

### Filter enum (authoritative)

- `task_created`
- `task_completed`
- `work_order_assigned`
- `work_order_status_changed`
- `work_order_status_completed`
- `repo_sync_started`
- `repo_sync_completed`

No additional event types should be assumed without an explicit contract update.

---

## Entry Points and Cross-Links

Expected inbound links:
- Workspaces Overview and each workspace console (`View session`).
- Team Console active-session drill-downs.
- My Work active-session drill-downs.

Outbound links:
- Linked Work Orders -> Work Order Details route.
- Coder Pod monitoring link -> external observability surface.

This page remains a detail page, not a side-nav console destination.
