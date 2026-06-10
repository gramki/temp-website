# Swarm Details

**URL pattern:** `/workbenches/{workbenchId}/swarms/{swarmId}`

**Group:** Agent Fabric detail page

**Purpose:** Full Swarm profile — identity, governance, membership, employment summary, and aggregated usage analytics.

---

## Canonical Contract

This page is the source of truth for Swarm details. Any "View Swarm" action from Agent Fabric consoles, Workspace consoles, or Workforce must deep-link to this route.

---

## 1. Identity

| Field | Description |
|-------|-------------|
| **Name** | Swarm display name |
| **ID** | Unique Swarm identifier |
| **Scope** | Foundry / Workshop / Workbench / Workspace |
| **Owner** | Who manages this Swarm |
| **Created** | Creation timestamp |
| **Last modified** | Most recent update |

## 2. Provenance

| Field | Description |
|-------|-------------|
| **Origin** | Platform-shipped / Tenant-added |
| **Platform version** | If platform-shipped, the version of Foundry defaults |
| **Extended by tenant** | Whether tenant has added Trained Agents to a platform Swarm |
| **Promotion history** | If promoted, the source scope and timestamp |

## 3. Governance

| Field | Description |
|-------|-------------|
| **Charter** | Purpose and responsibilities of this Swarm |
| **Policies** | Applied governance policies |
| **Membership rules** | Criteria for adding Trained Agents |
| **Quota allocation** | Token/cost budgets allocated to this Swarm |

## 4. Trained Agents

List of all Trained Agents in this Swarm:

| Column | Description |
|--------|-------------|
| **Name** | Agent name (clickable → [Trained Agent Details](trained-agent-details.md)) |
| **JID** | `{agent}@{swarm}.agents.{tenant}.foundry.io` |
| **Raw Agent** | Referenced Raw Agent + version |
| **Skills** | Count of configured skills |
| **Provenance** | Platform-shipped / Tenant-added (for extended platform Swarms) |
| **Last employed** | Most recent employment |

## 5. Employment Summary

Active Employed Agents from this Swarm:

| Column | Description |
|--------|-------------|
| **Instance ID** | Employed Agent ID (clickable → [Employed Agent Details](employed-agent-details.md)) |
| **Trained Agent** | Source Trained Agent |
| **Workspace** | Where running |
| **Human delegator** | Session owner |
| **Status** | Active / idle / terminated |
| **Started** | When employment began |

---

## 6. Usage Analytics

Aggregated usage across all Trained Agents in this Swarm.

### Metrics

| Metric | Description |
|--------|-------------|
| **Total invocations** | Sum across all Trained Agents |
| **Token consumption** | Input tokens, output tokens, total |
| **Cost (USD)** | Aggregated cost |
| **Active Employed Agents** | Currently running instances |
| **Task success rate** | Aggregate success / failure |
| **Top skills** | Most used skills across Swarm |
| **Top delegators** | Humans with most delegation to this Swarm |

### Charts

| Chart | Description |
|-------|-------------|
| **Invocations over time** | Daily/weekly trend |
| **Token consumption trend** | Input/output over time |
| **Cost trend** | USD per day/week/month |
| **Skill distribution** | Usage by skill |
| **Delegator breakdown** | Usage by human delegator |
| **Workspace distribution** | Activity by Workspace |

### Filters

| Dimension | Options |
|-----------|---------|
| **Scope** | Workshop, Workbench, Workspace |
| **Actor** | Human User (delegator) |
| **Time** | Today, Week, Month, Custom range |
| **Skills** | Breakdown by skill name and version |

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| View Trained Agent | All | Navigate to Trained Agent detail |
| View Employed Agent | All | Navigate to Employed Agent detail |
| Edit Swarm | Manager at scope | Update charter, policies, membership rules |
| Add Trained Agent | Manager at scope | Add agent to this Swarm |
| Remove Trained Agent | Manager at scope | Remove agent from this Swarm |
| Promote Swarm | Manager at scope | Move manifest to higher scope |
| Export report | Manager | Download Swarm usage report |

---

## Entry Points and Cross-Links

Inbound links:
- [Swarm Console](swarm-console.md) — Swarm list click
- [Agent Fabric Overview](agent-fabric-overview.md) — Swarm overview click
- [Trained Agents](trained-agents.md) — Swarm column click
- [Employed Agents](employed-agents.md) — Swarm column click

Outbound links:
- Trained Agent → [Trained Agent Details](trained-agent-details.md)
- Employed Agent → [Employed Agent Details](employed-agent-details.md)
- Raw Agent → [Raw Agent Details](raw-agent-details.md)
- Workspace → Workspace Session Details

This page is a detail page — it does not appear in side navigation.
