# Employed Agents Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/employed-agents`

**Group:** Agent Fabric

**Purpose:** Runtime Employed Agent activity — utilization, performance, task execution, token consumption, and cost analytics.

> **Migration note:** This console replaces the former Agent Console in the Workforce group. See [workforce/agent-console.md](../workforce/agent-console.md) for the deprecated predecessor.

---

## Type

List + Detail, Analytics

## Audience

Workbench Managers, Workshop Managers, Workspace Owners, Governance

---

## Page Sections

### 1. Employed Agent Overview

| Metric | Description |
|--------|-------------|
| **Active agents** | Currently executing tasks |
| **Tasks completed (today)** | Employed Agent task count |
| **Average task duration** | Mean execution time |
| **Success rate** | % tasks completed without error |
| **Queue depth** | Tasks awaiting agent execution |
| **Token usage (today)** | Input + output tokens |
| **Cost (today)** | USD cost for today |

### 2. Employed Agent Activity List

| Column | Description |
|--------|-------------|
| **Instance ID** | Employed Agent identifier (clickable → [Employed Agent Details](employed-agent-details.md)) |
| **Trained Agent** | Source Trained Agent name (clickable → [Trained Agent Details](trained-agent-details.md)) |
| **Swarm** | Parent Swarm (clickable → [Swarm Details](swarm-details.md)) |
| **JID** | Agent identity |
| **Workspace** | Where the agent is running |
| **Human delegator** | Session owner who delegated |
| **Scenario** | What it's executing |
| **Work Order** | Parent WO |
| **Status** | Active / idle / terminated / error |
| **Started** | When employment began |
| **Duration** | How long running |

### 3. Performance Metrics

| Element | Description |
|---------|-------------|
| **Tasks per hour** | Throughput |
| **Error rate** | % of tasks failing |
| **Retry rate** | Tasks requiring retry |
| **By Swarm** | Performance per Swarm |
| **By Scenario** | Performance per Scenario type |
| **By Workspace** | Where agents work |

### 4. Token & Cost Analytics

| Element | Description |
|---------|-------------|
| **Token consumption** | Input/output tokens over time |
| **Cost trend** | USD cost over time |
| **By Swarm** | Token/cost breakdown by Swarm |
| **By Trained Agent** | Token/cost breakdown by Trained Agent |
| **By model** | Token/cost breakdown by model used |
| **By skill** | Token/cost breakdown by skill invoked |

### 5. Task History

| Column | Description |
|--------|-------------|
| **Task ID** | Identifier |
| **Employed Agent** | Which agent executed (clickable → [Employed Agent Details](employed-agent-details.md)) |
| **Swarm** | Parent Swarm |
| **Scenario** | Task type |
| **Work Order** | Parent WO |
| **Duration** | How long |
| **Tokens** | Input + output |
| **Cost** | USD |
| **Outcome** | Success / failure / retry |
| **Timestamp** | When |

---

## Analytics Charts

| Chart | Description |
|-------|-------------|
| **Utilization over time** | Agent activity trend |
| **Task distribution** | By Scenario type |
| **Error trends** | Failure rate over time |
| **Queue depth** | Waiting tasks over time |
| **Token consumption** | Input/output trend |
| **Cost trend** | USD per day/week/month |
| **Swarm breakdown** | Activity by Swarm |
| **Delegator breakdown** | Activity by human delegator |

---

## Filters

- By Swarm
- By Trained Agent
- By Workspace
- By human delegator
- By Scenario
- By status (active / idle / terminated / error)
- By date range (today / week / month / custom)

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| View details | All | Navigate to [Employed Agent Details](employed-agent-details.md) |
| View task | All | Drill into task execution |
| View Swarm | All | Navigate to parent Swarm |
| View delegator | All | Navigate to session owner profile |
| Retry task | Manager | Re-execute failed task |
| View logs | Manager | Agent execution logs |
| Export report | Manager | Download activity/cost report |

---

## Related Consoles

- **[Agent Fabric Overview](agent-fabric-overview.md)** — Landing page
- **[Swarm Console](swarm-console.md)** — Swarm management
- **[Trained Agents](trained-agents.md)** — Trained Agent configurations
- **[Employed Agent Details](employed-agent-details.md)** — Full Employed Agent session + usage
- **[Workforce Overview](../workforce/workforce-overview.md)** — Combined team + agent summary
- **[Workspaces Overview](../workspaces/workspaces-overview.md)** — Where agents work

---

## Related Documentation

- [../../../../agent-fabric/concepts/employed-agent.md](../../../../agent-fabric/concepts/employed-agent.md) — Employed Agent concept
- [../../../../agent-fabric/platform-developer-guide/employed-agents.md](../../../../agent-fabric/platform-developer-guide/employed-agents.md) — Identity model and delegation
