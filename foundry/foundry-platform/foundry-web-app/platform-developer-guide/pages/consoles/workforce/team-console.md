# Team Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/team`

**Group:** Workforce

**Purpose:** Team analytics — contributions, workload, team composition.

> **Console boundary:** Team Console owns workforce capacity, workload, contribution, skills, and WFR-backed recognition. Governance may consume team-level trends as operating-health indicators, but Team Console is not a governance enforcement surface.

---

## Page Sections

### 1. Team Overview

| Metric | Description |
|--------|-------------|
| **Team size** | Total members |
| **Managers** | Members with Manager role |
| **Active this week** | Members with recent activity |
| **Tasks completed** | Team total this period |

### 2. Team Roster

| Column | Description |
|--------|-------------|
| Name | Team member (clickable → opens Team Member Workbench Profile) |
| Role | Manager or Member |
| Primary Workspace | Where they work most |
| **Active Sessions** | Count of active Workspace Sessions (clickable) |
| **Work Orders** | Count of assigned Work Orders (clickable) |
| **Past Due** | Count of Work Orders past due (clickable, red highlight if > 0) |
| Last active | Most recent activity |

#### Clickable Metrics Behavior

Each metric count in the roster is clickable and opens a side panel:

| Metric Clicked | Side Panel Contents | Drill-down Link |
|----------------|---------------------|-----------------|
| Active Sessions | List of member's active Workspace Sessions with Workspace type, started time, attached WOs | Each session links to canonical [Workspace Session Details](../workspaces/workspace-session-details.md) |
| Work Orders | List of assigned Work Orders with title, status, Workspace type, due date | Each WO links to Orchestration Console at the specific Work Order |
| Past Due | List of overdue Work Orders with title, days overdue, Workspace type | Each WO links to Orchestration Console at the specific Work Order |

Side panel includes:
- Member name header
- Metric name and count
- Scrollable list of items
- Quick action to assign/reassign Work Orders (for Managers)

### 3. Contribution Analytics

| Element | Description |
|---------|-------------|
| **By member** | Tasks completed per person |
| **By Workspace** | Who works where |
| **Trend chart** | Contributions over time |
| **Leaderboard** | Top contributors (optional) |

### 4. Workload Distribution

| Element | Description |
|---------|-------------|
| **Current assignments** | Tasks per member |
| **Workload balance** | Visual distribution |
| **Overloaded** | Members with high task count |
| **Available capacity** | Members with low assignments |

### 5. Team Member Navigation

Clicking on a team member's name in the roster navigates to their **Team Member Workbench Profile** page (see below).

---

## Team Member Workbench Profile

**URL pattern:** `/workbenches/{workbenchId}/team/{memberId}`

This is a standalone page (not a modal) that provides comprehensive information about a team member's activity and performance within the Workbench. The URL is referenceable and can be linked from other locations (e.g., Work Order details, session logs, governance reports).

### Profile Header

| Element | Description |
|---------|-------------|
| **Name** | Full name |
| **Avatar** | Profile image |
| **Role** | Manager or Member |
| **Primary Workspace** | Most active Workspace type |
| **Member since** | Date joined this Workbench |
| **Last active** | Most recent activity timestamp |

### Summary Metrics

Key metrics for Engineering Managers and Governance Teams:

| Metric | Description |
|--------|-------------|
| **Active Sessions** | Current Workspace Sessions count |
| **Work Orders (Active)** | Assigned and in-progress WOs |
| **Work Orders (Past Due)** | Overdue WOs (highlighted if > 0) |
| **WOs Completed (30 days)** | Work Orders closed in last 30 days |
| **Avg Completion Time** | Average time from WO assignment to completion |
| **Workspace Coverage** | List of Workspace types member has worked in |

### Activity Timeline

Chronological stream of the member's activity within the Workbench:

| Activity Type | Details Shown |
|---------------|---------------|
| Work Order assigned | WO title, Workspace type, timestamp |
| Work Order completed | WO title, time spent, outcome |
| Session started | Workspace type, session ID |
| Session closed | Duration, WOs completed in session |
| Task completed | Task title, parent WO |
| Review submitted | What was reviewed |

Filters:
- By date range
- By Workspace type
- By activity type

### Workload View

| Element | Description |
|---------|-------------|
| **Current assignments** | List of active Work Orders with due dates |
| **Session inventory** | Active sessions with attached WOs |
| **Capacity indicator** | Visual showing workload relative to team average |

### Contribution History

| Element | Description |
|---------|-------------|
| **By Workspace** | Breakdown of WOs completed per Workspace type |
| **By Track** | Contributions to Discovery, Build, Run, Win, Evolve, Governance |
| **Trend chart** | Activity over time (weekly/monthly) |
| **Milestone contributions** | Significant completions (releases, major PIs) |

### Governance Summary

Metrics specifically for Governance Teams:

| Metric | Description |
|--------|-------------|
| **Compliance rate** | % of WOs completed within SLA |
| **Past due history** | Count of WOs that went past due (historical) |
| **Quality score** | Based on rework/rejection rate (if tracked) |
| **Risk items** | Any open risk items associated with member's work |

### Actions

| Action | Who | Description |
|--------|-----|-------------|
| Assign Work Order | Manager | Assign new WO to this member |
| Change role | Manager | Promote/demote role |
| View sessions | All | Jump to Workspaces Overview filtered to member |
| Export report | Manager | Download member activity report |
| Contact | All | Email or message member |

---

## Console Actions

| Action | Who | Description |
|--------|-----|-------------|
| Add member | Manager | Invite to Workbench |
| Remove member | Manager | Remove from Workbench |
| Change role | Manager | Promote to Manager / demote |
| Assign Work Order | Manager | Assign WO to member |
| View profile | All | Navigate to Team Member Workbench Profile |

---

## Filters

- By role (Manager, Member)
- By Workspace
- By activity level
- By date range

---

## Privacy Considerations

- Individual metrics visible to Managers only
- Members see aggregate team stats
- No time tracking or surveillance features

---

## Related Consoles

- **Workforce Overview** — Team + Agent summary
- **Agent Console** — Non-human workforce
- **Progress Console** — Overall completion
- **Workspaces Overview** — Who's working where
- **Admin Console** — Team management settings

---

## Cross-Linking

The Team Member Workbench Profile page (`/workbenches/{workbenchId}/team/{memberId}`) can be linked from:

| Source | Context |
|--------|---------|
| Work Order details | Assigned member |
| [Workspace Session Details](../workspaces/workspace-session-details.md) | Session owner |
| Activity feeds | Actor in activity |
| Risk items | Associated member |
| Governance reports | Member under review |
| Workspace consoles | Session owner link |
| Workbench Wall | Activity attribution |
