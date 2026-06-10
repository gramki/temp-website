# Employed Agent Details

**URL pattern:** `/workbenches/{workbenchId}/agents/employed/{employedAgentId}`

**Group:** Agent Fabric detail page

**Purpose:** Full Employed Agent session view — identity, delegation, current state, task history, and usage analytics.

---

## Canonical Contract

This page is the source of truth for Employed Agent details. Any "View Employed Agent" action from Agent Fabric consoles, Workspace Session Details, or Workforce must deep-link to this route.

---

## 1. Identity

| Field | Description |
|-------|-------------|
| **Instance ID** | Unique Employed Agent instance identifier |
| **Trained Agent** | Source Trained Agent name (clickable → [Trained Agent Details](trained-agent-details.md)) |
| **JID** | `{agent}@{swarm}.agents.{tenant}.foundry.io` |
| **Swarm** | Parent Swarm (clickable → [Swarm Details](swarm-details.md)) |
| **Workspace Session** | Bound session (clickable → [Workspace Session Details](../workspaces/workspace-session-details.md)) |

## 2. Delegation

| Field | Description |
|-------|-------------|
| **Human delegator** | Session owner who delegated (clickable → Team Member Profile) |
| **Delegation Token scope** | What the token authorizes |
| **Granted authority** | Model access, tool access, repo access, Jira access |
| **Token issued** | When the Delegation Token was created |
| **Token expiry** | When the token expires |

## 3. Current State

| Field | Description |
|-------|-------------|
| **Status** | Active / idle / terminated / error |
| **Current task** | Task currently being executed (if active) |
| **Current skill** | Skill being invoked (if active) |
| **Uptime** | Duration since employment began |
| **Last activity** | Most recent action timestamp |

### Status Transitions

```
Spawned → Active → Idle → Active → ... → Terminated
                    ↓                       ↑
                  Error ────────────────────┘
```

## 4. Task History

All tasks executed by this Employed Agent:

| Column | Description |
|--------|-------------|
| **Task ID** | Task identifier |
| **Scenario** | Scenario type |
| **Work Order** | Parent WO (clickable) |
| **Skill invoked** | Which skill was used |
| **Started** | When task began |
| **Duration** | How long it took |
| **Tokens** | Input + output tokens |
| **Cost** | USD cost |
| **Outcome** | Success / failure / retry |
| **Error** | Error message (if failed) |

---

## 5. Usage Analytics

Usage metrics for this specific Employed Agent instance.

### Metrics

| Metric | Description |
|--------|-------------|
| **Total tasks** | Tasks executed in this employment |
| **Token consumption** | Input tokens, output tokens, total |
| **Cost (USD)** | Total cost for this instance |
| **Task success rate** | Success / failure ratio |
| **Skills invoked** | List of skills used with counts |
| **Average task duration** | Mean execution time |
| **Quota used** | Percentage of allocated quota consumed |

### Charts

| Chart | Description |
|-------|-------------|
| **Token consumption by skill** | Breakdown per skill |
| **Task timeline** | Chronological task execution |
| **Cost by skill** | USD per skill |
| **Success/failure by skill** | Outcome distribution per skill |

### Filters

| Dimension | Options |
|-----------|---------|
| **Scenario** | Filter by Scenario type |
| **Work Order** | Filter by parent WO |
| **Time** | Today, custom range within employment period |

---

## 6. Execution Log

Chronological event stream for this Employed Agent:

| Event Type | Details |
|------------|---------|
| `agent.spawned` | Trained Agent resolved, harness prepared |
| `token.issued` | Delegation Token issued |
| `task.assigned` | Task assigned from Work Order |
| `skill.invoked` | Skill execution started |
| `skill.completed` | Skill execution finished |
| `model.call` | Model API call (model, tokens, cost) |
| `tool.call` | MCP tool invocation |
| `task.completed` | Task finished (outcome) |
| `agent.terminated` | Agent terminated (reason) |

Log follows observability-style structured lines with RFC3339 timestamps.

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| View Trained Agent | All | Navigate to source Trained Agent |
| View Swarm | All | Navigate to parent Swarm |
| View session | All | Navigate to Workspace Session |
| View delegator | All | Navigate to session owner profile |
| View Work Order | All | Navigate to parent Work Order |
| View logs | Manager | Full execution logs |
| Retry task | Manager | Re-execute a failed task |
| Export report | Manager | Download instance usage report |

---

## Entry Points and Cross-Links

Inbound links:
- [Employed Agents](employed-agents.md) — Row click
- [Swarm Details](swarm-details.md) — Employment Summary click
- [Trained Agent Details](trained-agent-details.md) — Employment History click
- [Workspace Session Details](../workspaces/workspace-session-details.md) — Agent card click

Outbound links:
- Trained Agent → [Trained Agent Details](trained-agent-details.md)
- Swarm → [Swarm Details](swarm-details.md)
- Workspace Session → [Workspace Session Details](../workspaces/workspace-session-details.md)
- Work Order → Work Order Details
- Delegator → Team Member Workbench Profile

This page is a detail page — it does not appear in side navigation.
