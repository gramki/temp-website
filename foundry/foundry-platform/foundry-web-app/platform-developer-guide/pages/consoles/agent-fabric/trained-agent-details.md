# Trained Agent Details

**URL pattern:** `/workbenches/{workbenchId}/agents/trained/{trainedAgentJid}`

**Group:** Agent Fabric detail page

**Purpose:** Full Trained Agent profile — identity, configuration, Service Principal, employment history, and usage analytics.

---

## Canonical Contract

This page is the source of truth for Trained Agent details. Any "View Trained Agent" action from Agent Fabric consoles must deep-link to this route.

---

## 1. Identity

| Field | Description |
|-------|-------------|
| **Name** | Trained Agent display name |
| **JID** | `{agent}@{swarm}.agents.{tenant}.foundry.io` |
| **Swarm** | Parent Swarm (clickable → [Swarm Details](swarm-details.md)) |
| **Raw Agent** | Referenced Raw Agent + version (clickable → [Raw Agent Details](raw-agent-details.md)) |
| **Scope** | Foundry / Workshop / Workbench / Workspace |
| **Created** | Creation timestamp |
| **Last modified** | Most recent manifest update |

## 2. Configuration

| Section | Content |
|---------|---------|
| **Skills** | List of configured skills with name, version, autonomy level |
| **Guardrails** | Applied guardrails (e.g. no-force-push, require-tests-for-new-code) |
| **Evaluation criteria** | Quality gates and success metrics |
| **Manifest source** | Link to manifest YAML in repository |

### Skill Detail

| Column | Description |
|--------|-------------|
| **Skill name** | Skill identifier |
| **Version** | Pinned version range |
| **Autonomy** | High (peer) / Low (assistant) |
| **Invocations** | Count of invocations this period |

## 3. Service Principal

| Field | Description |
|-------|-------------|
| **IAM identity** | Service Principal bound to this JID |
| **Permissions** | Granted permissions summary |
| **Delegation scope** | What the agent can be delegated to do |
| **Last authenticated** | Most recent identity verification |

## 4. Employment History

Current and historical Employed Agent instances:

| Column | Description |
|--------|-------------|
| **Instance ID** | Employed Agent ID (clickable → [Employed Agent Details](employed-agent-details.md)) |
| **Workspace** | Where it ran |
| **Human delegator** | Session owner |
| **Work Order** | What it worked on |
| **Status** | Active / terminated / error |
| **Started** | When employment began |
| **Duration** | How long it ran |
| **Tokens** | Total token consumption |
| **Cost** | USD cost |
| **Outcome** | Success / failure |

### Time Windows

- All
- Today
- 7 days
- 30 days
- Custom range

---

## 5. Usage Analytics

Usage metrics for this specific Trained Agent across all its Employed instances.

### Metrics

| Metric | Description |
|--------|-------------|
| **Total invocations** | Employment count over time |
| **Token consumption** | Input tokens, output tokens, total |
| **Cost (USD)** | Aggregated cost |
| **Task success rate** | Aggregate success / failure |
| **Top skills** | Most invoked skills |
| **Average task duration** | Mean execution time |

### Charts

| Chart | Description |
|-------|-------------|
| **Invocations over time** | Daily/weekly trend |
| **Token consumption trend** | Input/output over time |
| **Cost trend** | USD per day/week/month |
| **Skill usage breakdown** | Invocations by skill |
| **Success/failure trend** | Task outcome over time |
| **Delegator breakdown** | Usage by human delegator |

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
| View Swarm | All | Navigate to parent Swarm |
| View Raw Agent | All | Navigate to Raw Agent |
| View Employed Agent | All | Navigate to Employed Agent detail |
| Edit manifest | Manager at scope | Open manifest in IDE |
| View Service Principal | Manager | Navigate to IAM identity |
| Export report | Manager | Download Trained Agent usage report |

---

## Entry Points and Cross-Links

Inbound links:
- [Trained Agents](trained-agents.md) — Row click
- [Swarm Details](swarm-details.md) — Trained Agent list click
- [Employed Agents](employed-agents.md) — Trained Agent column click
- [Employed Agent Details](employed-agent-details.md) — Trained Agent link
- [Workspace Session Details](../workspaces/workspace-session-details.md) — Agent card click

Outbound links:
- Swarm → [Swarm Details](swarm-details.md)
- Raw Agent → [Raw Agent Details](raw-agent-details.md)
- Employed Agent → [Employed Agent Details](employed-agent-details.md)
- Workspace → Workspace Session Details

This page is a detail page — it does not appear in side navigation.
