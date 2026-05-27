# Workspaces Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/workspaces`

**Group:** Work

**Purpose:** Navigate the 6 Workspace types; view and manage Workspace Sessions and Work Orders.

---

## Key Concepts

| Term | Definition |
|------|------------|
| **Workspace** (ACE) | One of 6 types: Product Specification, UX Design, Development, QA, Release, Governance |
| **Workspace Session** | A Coder-based ephemeral dev environment for working in a Workspace |
| **Work Order** | A unit of work that can be attached to a Session |

---

## Page Layout

```
[Product Spec] [UX Design] [Development] [QA] [Release] [Governance]
                              ↓ (selected)
┌─────────────────────────────────────────────────────────────────────┐
│ WORKSPACE SUMMARY                                                   │
│   👥 5 people │ 💻 3 active sessions │ ▶ 8 active WOs              │
│   ⏳ 2 pending WOs │ ⚠ 1 past due │ ✓ 12 completed (7 days)        │
├─────────────────────────────────────────────────────────────────────┤
│ + Create Session                                                    │
├─────────────────────────────────────────────────────────────────────┤
│ MY SESSIONS:                                                        │
│   ● "Payment Integration" — Active — 3 WOs (12h total) [Open][Stop] │
│   ○ "Legacy Cleanup" — Stopped — 0 WOs                 [Start]      │
├─────────────────────────────────────────────────────────────────────┤
│ TEAM SESSIONS:                                                      │
│   ● @alice — "Checkout Feature" — Active — 2 WOs       [View]       │
│   ● @bob — "Auth Refactor" — Active — 1 WO             [View]       │
│   ○ @carol — "DB Migration" — Stopped — 0 WOs          [View]       │
├─────────────────────────────────────────────────────────────────────┤
│ WORK ORDERS:                                                        │
│   [Unassigned (2)] [Assigned (3)] [Active (8)] [Past Due (1)]       │
│                                                                     │
│   • WO-126 — Implement caching — waiting 2d            [Assign]     │
│   • WO-127 — Fix memory leak — waiting 1d              [Assign]     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Page Sections

### 1. Workspace Type Tabs

The 6 standard Workspace types as tabs:

| Workspace | Description |
|-----------|-------------|
| **Product Specification** | Translate Intent to specs |
| **UX Design** | Design user experience |
| **Development** | Build the solution |
| **QA** | Verify and validate |
| **Release** | Publish artifacts |
| **Governance** | Validate transitions |

Click a tab → View Sessions and WOs for that Workspace type.

### 2. Workspace Summary

At-a-glance metrics for the selected Workspace type.

| Metric | Description |
|--------|-------------|
| **People** | Number of team members with Sessions in this Workspace |
| **Active Sessions** | Sessions currently running |
| **Active Work Orders** | WOs currently in progress |
| **Pending Work Orders** | WOs waiting (unassigned or assigned but not started) |
| **Past Due** | WOs past their due date (highlighted for attention) |
| **Completed (7 days)** | WOs completed in the last 7 days |

The summary provides quick visibility into Workspace activity and workload. Past due WOs are highlighted to draw attention to overdue work.

### 3. My Sessions

Current user's Workspace Sessions for the selected Workspace type.

| Element | Description |
|---------|-------------|
| **Session name** | User-provided identifier |
| **Status** | Active (running) / Stopped |
| **WO count** | Number of attached Work Orders |
| **Total time** | Cumulative time spent on WOs in this Session |
| **Actions** | Open (launch IDE), Stop, Start |

### 4. Team Sessions

Other team members' Sessions for the selected Workspace type.

| Element | Description |
|---------|-------------|
| **Owner** | Team member who owns the Session |
| **Session name** | Identifier |
| **Status** | Active / Stopped |
| **WO count** | Number of attached Work Orders |
| **Actions** | View (see details, read-only) |

### 5. Work Orders

Work Orders in this Workspace, organized by status tabs.

**Tabs (with counts):**

| Tab | Description | Default |
|-----|-------------|---------|
| **Unassigned (n)** | WOs not attached to any Session or person | ✓ Default |
| **Assigned (n)** | WOs assigned to a person but not yet in a Session |  |
| **Active (n)** | WOs currently being worked on in Sessions |  |
| **Past Due (n)** | WOs past their due date (any status) |  |

**Work Order Row:**

| Element | Description |
|---------|-------------|
| **WO ID** | Work Order identifier |
| **Title** | Brief description |
| **PI** | Parent Product Intent |
| **Status indicator** | Waiting time, assignee, or overdue flag |
| **Actions** | Varies by tab (Assign, View, Detach) |

**Actions by Tab:**

| Tab | Available Actions |
|-----|-------------------|
| **Unassigned** | Assign to me, Assign to Session |
| **Assigned** | View, Reassign, Start (create/attach to Session) |
| **Active** | View, Detach from Session |
| **Past Due** | View, Escalate, Reassign |

---

## Workspace Session Model

### Definition

A Workspace Session is a Coder-based ephemeral development environment.

| Aspect | Detail |
|--------|--------|
| **Created by** | Work Order Runtime module |
| **Template** | Per (Workspace Type, Workbench) — customized per Workbench |
| **Ownership** | Owned by one person (not shared) |
| **WO relationship** | Multiple WOs can be attached to one Session |
| **Assignment** | Manual now; Orchestrator may automate later |
| **Destruction** | User explicitly closes |

### Session States

| State | Description |
|-------|-------------|
| **Active** | Running, user can work in it |
| **Stopped** | Persisted but not running (can restart) |
| **Archived** | Read-only snapshot (after explicit close) |

### Session Detail View

Clicking a Session (own or team) navigates to the **Workspace Session Details** page (see below).

---

## Workspace Session Details Page

**URL pattern:** `/workbenches/{workbenchId}/sessions/{sessionId}`

This is a standalone page (not a modal) providing comprehensive details about a Workspace Session. The URL is referenceable and can be linked from anywhere (Team Console, governance reports, activity feeds, Work Order details).

**Audience:** Workspace Users, Managers, Governance Teams

### Page Header

| Element | Description |
|---------|-------------|
| **Session name** | User-provided identifier |
| **Workspace type** | e.g., Development, QA |
| **Owner** | Team member who owns this Session (links to their Workbench Profile) |
| **Status** | Active / Stopped / Archived |
| **Created** | Date and time Session was created |
| **Last active** | Most recent activity timestamp |
| **Total duration** | Cumulative active time |

**Quick Actions (for Session Owner):**

| Action | Availability |
|--------|--------------|
| Open in IDE | Active Sessions only |
| Stop | Active Sessions only |
| Start | Stopped Sessions only |
| Archive | Stopped Sessions only |

### Summary Metrics

| Metric | Description |
|--------|-------------|
| **Work Orders (Active)** | Currently attached and in-progress |
| **Work Orders (Completed)** | Completed in this Session |
| **Tasks Completed** | Total Tasks finished across all WOs |
| **Commits** | Total commits made from this Session |
| **Time Tracked** | Total tracked time across all WOs |

### Attached Work Orders

Current and historical Work Orders attached to this Session.

| Column | Description |
|--------|-------------|
| **WO ID** | Work Order identifier (clickable → PI Console) |
| **Title** | Brief description |
| **Product Intent** | Parent PI (clickable → PI Console) |
| **Status** | In progress, Blocked, Completed, Detached |
| **Attached** | When WO was attached to this Session |
| **Detached / Completed** | When WO left this Session (if applicable) |
| **Time in Session** | Time spent on this WO while in this Session |

**Tabs:**

| Tab | Contents |
|-----|----------|
| **Active (n)** | Currently attached WOs |
| **Completed (n)** | WOs completed in this Session |
| **Detached (n)** | WOs that were moved out before completion |

### Work Done

Detailed breakdown of all work performed in this Session.

#### Tasks

| Column | Description |
|--------|-------------|
| **Task ID** | Task identifier |
| **Title** | Task description |
| **Work Order** | Parent WO (clickable) |
| **Type** | Agent Task / Human Task |
| **Status** | Completed, In progress |
| **Completed at** | Timestamp |
| **Duration** | Time to complete |

Filters: By WO, By status, By type

#### Commits

| Column | Description |
|--------|-------------|
| **SHA** | Commit hash (short, clickable → repo) |
| **Message** | Commit message |
| **Repository** | Code repository |
| **Work Order** | Associated WO (if tagged) |
| **Timestamp** | When committed |
| **Files changed** | Count of files |

Filters: By WO, By repository, By date

#### Artifacts Produced

| Column | Description |
|--------|-------------|
| **Artifact** | Name / identifier |
| **Type** | Document, Design, Test case, Build artifact, etc. |
| **Repository** | Where stored |
| **Work Order** | Associated WO |
| **Created at** | Timestamp |

### Activity Timeline

Chronological stream of all activity in this Session.

| Activity Type | Details Shown |
|---------------|---------------|
| Session started | Timestamp |
| Session stopped | Timestamp, duration of this active period |
| Session resumed | Timestamp |
| WO attached | WO title, timestamp |
| WO detached | WO title, reason, timestamp |
| WO completed | WO title, time spent |
| Task started | Task title, WO, timestamp |
| Task completed | Task title, WO, duration |
| Commit pushed | SHA, message, repository |
| Build triggered | Build ID, status |
| Test run | Test suite, pass/fail count |

Filters:
- By date range
- By activity type
- By Work Order

### Time Tracking

Detailed time breakdown (for Managers and Governance):

| Element | Description |
|---------|-------------|
| **By Work Order** | Time spent on each WO in this Session |
| **By Day** | Daily breakdown of active time |
| **Idle time** | Time Session was active but no tracked work |
| **Total active** | Cumulative time Session was running |

Visual: Timeline chart showing work periods.

### Governance View

Metrics specifically for Governance Teams:

| Metric | Description |
|--------|-------------|
| **WOs within SLA** | % of WOs completed within expected time |
| **WOs past due** | Count of WOs that went past due while in this Session |
| **Avg WO completion time** | Average time from WO attachment to completion |
| **Compliance flags** | Any compliance issues raised |
| **Audit trail** | Full chronological record (exportable) |

### Actions

| Action | Who | Description |
|--------|-----|-------------|
| Open in IDE | Owner | Launch IDE (Active Sessions) |
| Stop / Start | Owner | Pause or resume Session |
| Archive | Owner | Close and snapshot |
| Attach WO | Owner | Add a Work Order to this Session |
| Export report | Manager | Download Session activity report |
| Export audit log | Governance | Download full audit trail |

---

## Cross-Linking

The Workspace Session Details page (`/workbenches/{workbenchId}/sessions/{sessionId}`) can be linked from:

| Source | Context |
|--------|---------|
| Workspaces Console | Session list (My Sessions, Team Sessions) |
| Team Console | Side panel when clicking member's Active Sessions count |
| Team Member Profile | Session inventory section |
| Work Order details | Session where WO is/was attached |
| Activity feeds | Session-related activity |
| Governance reports | Session audit references |
| Workbench Wall | Session activity attribution |

---

## Work Order Assignment

| Assignment Type | Meaning |
|-----------------|---------|
| **Unassigned** | In pool under Workspace tab, anyone can pick up |
| **Assigned to person** | That person works on it (in any of their Sessions) |
| **Assigned to Session** | Bound to a specific Session (owner works on it there) |

---

## Actions

### Session Actions

| Action | Who | Description |
|--------|-----|-------------|
| Create Session | All | Start a new Session for this Workspace type |
| Open | Owner | Launch IDE for the Session |
| Stop | Owner | Pause the Session (persists state) |
| Start | Owner | Resume a stopped Session |
| Archive | Owner | Close and create read-only snapshot |
| View | All | See Session details (read-only for others) |

### Work Order Actions

| Action | Who | Description |
|--------|-----|-------------|
| Assign to me | All | Pick up unassigned WO |
| Assign to Session | Owner | Attach WO to a specific Session |
| Detach from Session | Owner | Remove WO from Session (back to unassigned or person-assigned) |
| View details | All | Open Work Order detail page |

---

## Filters

- By Session status (Active, Stopped, Archived)
- By owner (My Sessions vs Team)
- By WO status (In progress, Blocked)
- Search by Session name or WO ID

---

## Scenario Catalog Section

Each Workspace type has an associated Scenario Catalog.

| Element | Description |
|---------|-------------|
| **Available Scenarios** | Scenarios added to this Workspace |
| **Scenario card** | Name, description, typical duration |
| **Add Scenario** | Manager action — browse platform catalog |
| **Remove Scenario** | Manager action — remove from Workspace |

---

## Related Consoles

- **PI Console** — See WOs by Product Intent
- **Progress Console** — Workspace completion metrics
- **Track Console** — Track-level view
- **Team Console** — Who's working in which Sessions
