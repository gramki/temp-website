# Agent Fabric Overview Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/agent-fabric`

**Group:** Agent Fabric

**Purpose:** Landing page for Agent Fabric — summary of Raw Agents, Swarms, Trained Agents, and Employed Agents across visible scopes.

---

## Type

Landing

## Audience

Workbench Managers, Workshop Managers, Foundry Admins, Governance

---

## Page Sections

### 1. Agent Fabric Summary

| Metric | Description |
|--------|-------------|
| **Raw Agents available** | Platform-shipped + tenant-added Raw Agents visible at this scope |
| **Swarms** | Total Swarms visible (Foundry + Workshop + Workbench + Workspace) |
| **Trained Agents** | Total Trained Agents across all visible Swarms |
| **Active Employed Agents** | Currently running Employed Agent instances |

### 2. Swarm Overview

Quick view of all Swarms visible at the current Workbench scope:

| Column | Description |
|--------|-------------|
| **Swarm name** | Swarm identifier |
| **Scope** | Foundry / Workshop / Workbench / Workspace |
| **Provenance** | Platform-shipped or Tenant-added |
| **Trained Agents** | Count of Trained Agents in Swarm |
| **Active Employed** | Currently running instances from this Swarm |
| **Utilization** | Invocations this period |

Click action: Navigate to [Swarm Details](swarm-details.md).

### 3. Employed Agent Activity

Recent Employed Agent activity across all Swarms:

| Column | Description |
|--------|-------------|
| **Agent JID** | Employed Agent identity |
| **Swarm** | Parent Swarm |
| **Workspace** | Where the agent is running |
| **Status** | Active / idle / terminated |
| **Current task** | What the agent is working on |
| **Started** | When employment began |

### 4. Token & Cost Summary

| Metric | Description |
|--------|-------------|
| **Tokens today** | Input + output tokens across all Employed Agents |
| **Cost today** | USD cost for today |
| **Tokens this week** | Weekly aggregate |
| **Cost this week** | Weekly cost aggregate |
| **Top Swarm** | Highest token-consuming Swarm |

### 5. Quick Actions

| Action | Who | Description |
|--------|-----|-------------|
| View Raw Agents | All | Navigate to Raw Agent Registry |
| View Swarms | All | Navigate to Swarm Console |
| View Employed Agents | All | Navigate to Employed Agents console |
| Manage Swarms | Manager | Navigate to Swarm Console (management view) |

---

## Scope Visibility

The overview aggregates data across all visible scopes:

| Scope | What's Visible |
|-------|----------------|
| **Foundry Swarms** | Always visible |
| **Workshop Swarms** | Visible to Workbenches in that Workshop |
| **Workbench Swarms** | Visible to this Workbench |
| **Workspace Swarms** | Visible per Workspace |

---

## Related Consoles

- **[Raw Agent Registry](raw-agent-registry.md)** — Browse available Raw Agents
- **[Swarm Console](swarm-console.md)** — Manage Swarms
- **[Trained Agents](trained-agents.md)** — View Trained Agents within Swarms
- **[Employed Agents](employed-agents.md)** — Runtime agent activity
- **[Workforce Overview](../workforce/workforce-overview.md)** — Combined team + agent summary
