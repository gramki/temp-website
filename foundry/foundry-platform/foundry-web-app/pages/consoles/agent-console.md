# Agent Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/agent`

**Group:** Workforce

**Purpose:** Agent activity analytics — utilization, performance, task execution.

---

## Page Sections

### 1. Agent Overview

| Metric | Description |
|--------|-------------|
| **Active agents** | Currently executing Tasks |
| **Tasks completed (today)** | Agent task count |
| **Average task duration** | Mean execution time |
| **Success rate** | % tasks completed without error |
| **Queue depth** | Tasks awaiting agent execution |

### 2. Agent Activity List

| Column | Description |
|--------|-------------|
| Agent ID | Identifier |
| Scenario | What it's executing |
| Work Order | Parent WO |
| Status | Running, idle, error |
| Started | When task began |
| Duration | How long running |

### 3. Agent Performance Metrics

| Element | Description |
|---------|-------------|
| **Tasks per hour** | Throughput |
| **Error rate** | % of tasks failing |
| **Retry rate** | Tasks requiring retry |
| **By Scenario** | Performance per Scenario type |
| **By Workspace** | Where agents work |

### 4. Agent Task History

| Column | Description |
|--------|-------------|
| Task ID | Identifier |
| Agent | Which agent executed |
| Scenario | Task type |
| Work Order | Parent |
| Duration | How long |
| Outcome | Success, failure, retry |
| Timestamp | When |

### 5. Agent Detail View

| Element | Description |
|---------|-------------|
| **Agent info** | ID, type, capabilities |
| **Skills** | What the agent can do |
| **Current task** | If active |
| **Recent tasks** | History |
| **Performance** | Success rate, avg duration |
| **Errors** | Recent failures |

---

## Analytics Charts

| Chart | Description |
|-------|-------------|
| **Utilization over time** | Agent activity trend |
| **Task distribution** | By Scenario type |
| **Error trends** | Failure rate over time |
| **Queue depth** | Waiting tasks over time |

---

## Filters

- By agent type
- By Scenario
- By Workspace
- By status (active, idle, error)
- By date range

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| View agent | All | See agent details |
| View task | All | Drill into task execution |
| Retry task | Manager | Re-execute failed task |
| View logs | Manager | Agent execution logs |

---

## Related Consoles

- **Team Console** — Human workforce
- **Workspaces Console** — Where agents work
- **Progress Console** — Overall task completion
- **Risk Console** — Agent-related risks
