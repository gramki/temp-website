# Raw Agent Details

**URL pattern:** `/workbenches/{workbenchId}/agents/raw/{rawAgentId}`

**Group:** Agent Fabric detail page

**Purpose:** Full Raw Agent profile — identity, provenance, deployment modes, Trained Agent usage, and usage analytics.

---

## Canonical Contract

This page is the source of truth for Raw Agent details. Any "View Raw Agent" action from Agent Fabric consoles must deep-link to this route.

---

## 1. Identity

| Field | Description |
|-------|-------------|
| **Name** | Raw Agent display name |
| **OCI URI** | `registry.foundry.io/raw-agents/{agent}:{version}` |
| **Latest version** | Most recent version tag |
| **Interface type** | app-server, cli, sdk, etc. |
| **Capabilities** | Declared capabilities from OCI manifest |

## 2. Provenance

| Field | Description |
|-------|-------------|
| **Origin** | Platform-shipped / Tenant-added |
| **Publisher** | Organization or vendor that published the agent |
| **Certification** | Certification status (certified / uncertified / in-review) |
| **Registry** | `registry.foundry.io` or `registry.{tenant}.foundry.io` |
| **First published** | Initial publication date |

## 3. Deployment

| Field | Description |
|-------|-------------|
| **Deployment modes** | Container runtime, Coder workspace program |
| **Resource requirements** | CPU, memory, GPU requirements |
| **Dependencies** | Required services or tools |
| **Environment** | Required environment variables |

## 4. Version History

| Column | Description |
|--------|-------------|
| **Version** | Semantic version tag |
| **Published** | Publication date |
| **Trained Agents** | Count referencing this version |
| **Changelog** | Summary of changes |
| **Status** | Active / Deprecated / End-of-Support |

## 5. Trained Agents

List of Trained Agents using this Raw Agent:

| Column | Description |
|--------|-------------|
| **Name** | Trained Agent name (clickable → [Trained Agent Details](trained-agent-details.md)) |
| **Swarm** | Parent Swarm (clickable → [Swarm Details](swarm-details.md)) |
| **Version pinned** | Which version of this Raw Agent is referenced |
| **Scope** | Foundry / Workshop / Workbench / Workspace |
| **Last employed** | Most recent employment |

---

## 6. Usage Analytics

Aggregated usage across all Trained Agents referencing this Raw Agent.

### Metrics

| Metric | Description |
|--------|-------------|
| **Total invocations** | Sum across all Trained Agents using this Raw Agent |
| **Token consumption** | Input tokens, output tokens, total |
| **Cost (USD)** | Aggregated cost |
| **Active Employed Agents** | Currently running instances |
| **Trained Agent count** | How many Trained Agents reference this Raw Agent |

### Charts

| Chart | Description |
|-------|-------------|
| **Invocations over time** | Daily/weekly trend |
| **Token consumption trend** | Input/output over time |
| **Cost trend** | USD per day/week/month |
| **Version distribution** | Usage by version |
| **Swarm distribution** | Usage by Swarm |

### Filters

| Dimension | Options |
|-----------|---------|
| **Scope** | Workshop, Workbench |
| **Time** | Today, Week, Month, Custom range |

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| View Trained Agent | All | Navigate to Trained Agent detail |
| View Swarm | All | Navigate to parent Swarm |
| Copy URI | All | Copy OCI URI to clipboard |
| Export report | Manager | Download Raw Agent usage report |

---

## Entry Points and Cross-Links

Inbound links:
- [Raw Agent Registry](raw-agent-registry.md) — Row click
- [Trained Agents](trained-agents.md) — Raw Agent column click
- [Trained Agent Details](trained-agent-details.md) — Raw Agent reference click

Outbound links:
- Trained Agent → [Trained Agent Details](trained-agent-details.md)
- Swarm → [Swarm Details](swarm-details.md)

This page is a detail page — it does not appear in side navigation.
