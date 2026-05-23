# Progress Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/progress`

**Group:** Work

**Purpose:** Work completion analytics — burndown, velocity, completion rates.

---

## Page Sections

### 1. Summary Metrics

| Metric | Description |
|--------|-------------|
| **Active Work Orders** | Total WOs in progress |
| **Completed (this week)** | WOs finished this week |
| **Completion rate** | % of WOs meeting due dates |
| **Average cycle time** | Mean time from WO start to completion |

### 2. Burndown Charts

| Chart | Description |
|-------|-------------|
| **Workbench burndown** | All active WOs over time |
| **Per-PI burndown** | Select a PI to see its progress |
| **Per-Workspace burndown** | Filter by Workspace |

### 3. Velocity Trends

| Chart | Description |
|-------|-------------|
| **WOs completed per week** | Historical trend |
| **Tasks completed per day** | Granular view |
| **By persona/role** | Who's completing what |

### 4. Completion Analysis

| Element | Description |
|---------|-------------|
| **On-time vs late** | WOs meeting due dates |
| **Blockers** | Most common blocking reasons |
| **Bottlenecks** | Workspaces with longest wait times |

### 5. Work Order Table

| Column | Description |
|--------|-------------|
| WO ID | Identifier |
| PI | Product Intent |
| Workspace | Current location |
| Started | Start date |
| Due | Expected completion |
| Status | In progress, blocked, complete |
| Cycle time | Days from start |

---

## Filters

- By PI
- By Workspace
- By date range
- By status (active, completed, blocked)
- By assignee type (agent, human)

---

## Export

- CSV export of Work Order data
- PDF report generation

---

## Related Consoles

- **PI Console** — Drill into specific PI
- **Track Console** — Track-level analytics
- **Team Console** — Who's doing the work
