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
| Name | Team member |
| Role | Manager or Member |
| Primary Workspace | Where they work most |
| Active Tasks | Currently assigned |
| Completed (week) | Tasks finished this week |
| Last active | Most recent activity |

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

### 5. Member Detail View

| Element | Description |
|---------|-------------|
| **Profile** | Name, role, contact |
| **Assignments** | Current tasks |
| **History** | Completed work |
| **Workspaces** | Where they contribute |
| **Permissions** | Access level |

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Add member | Manager | Invite to Workbench |
| Remove member | Manager | Remove from Workbench |
| Change role | Manager | Promote to Manager / demote |
| Assign task | Manager | Assign Human Task |
| View member | All | See member profile |

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

- **Agent Console** — Non-human workforce
- **Progress Console** — Overall completion
- **Workspaces Console** — Who's working where
- **Admin Console** — Team management settings
