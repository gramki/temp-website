# Trained Agents Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/trained-agents`

**Group:** Agent Fabric

**Purpose:** Browse Trained Agents within Swarms — view configuration, Swarm membership, Raw Agent references, and employment history.

---

## Type

List + Detail

## Audience

Workbench Managers, Workshop Managers, Platform Engineers

---

## Page Sections

### 1. Trained Agent Summary

| Metric | Description |
|--------|-------------|
| **Total Trained Agents** | Across all visible Swarms |
| **Active (employed)** | Currently running as Employed Agents |
| **Idle** | Configured but not currently employed |
| **Swarms** | Count of Swarms containing visible Trained Agents |

### 2. Trained Agent List

| Column | Description |
|--------|-------------|
| **Name** | Agent name (clickable → [Trained Agent Details](trained-agent-details.md)) |
| **JID** | `{agent}@{swarm}.agents.{tenant}.foundry.io` |
| **Swarm** | Parent Swarm (clickable → [Swarm Details](swarm-details.md)) |
| **Raw Agent** | Referenced Raw Agent name + version |
| **Skills** | Count of configured skills |
| **Guardrails** | Count of applied guardrails |
| **Employed instances** | Currently active Employed Agents |
| **Last employed** | Most recent employment timestamp |

### 3. Swarm Grouping

| Tab | Content |
|-----|---------|
| **All** | All Trained Agents across visible Swarms |
| **By Swarm** | Grouped by parent Swarm |
| **By Raw Agent** | Grouped by referenced Raw Agent |

### 4. Configuration Preview

When a Trained Agent is selected, show a read-only preview of its manifest:

| Element | Description |
|---------|-------------|
| **Name and JID** | Identity |
| **Swarm membership** | Parent Swarm |
| **Raw Agent reference** | OCI URI + version |
| **Skills** | List of configured skills with versions |
| **Guardrails** | Applied guardrails |
| **Evaluation criteria** | Quality gates |

---

## Filters

- By Swarm
- By Raw Agent
- By scope (Foundry / Workshop / Workbench / Workspace)
- By status (active / idle)
- By skill
- Search by name or JID

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| View details | All | Navigate to [Trained Agent Details](trained-agent-details.md) |
| View Swarm | All | Navigate to parent Swarm |
| View employment | All | Navigate to [Employed Agents](employed-agents.md) filtered to this Trained Agent |
| Edit configuration | Manager at scope | Open manifest in IDE |
| Move to Swarm | Manager at scope | Transfer Trained Agent to a different Swarm at same scope |

---

## Related Consoles

- **[Agent Fabric Overview](agent-fabric-overview.md)** — Landing page
- **[Swarm Console](swarm-console.md)** — Swarm management
- **[Trained Agent Details](trained-agent-details.md)** — Full Trained Agent profile + usage analytics
- **[Employed Agents](employed-agents.md)** — Runtime instances of Trained Agents
- **[Raw Agent Registry](raw-agent-registry.md)** — Raw Agents referenced by Trained Agents

---

## Related Documentation

- [../../../../agent-fabric/concepts/trained-agent.md](../../../../agent-fabric/concepts/trained-agent.md) — Trained Agent concept
- [../../../../agent-fabric/platform-developer-guide/trained-agents.md](../../../../agent-fabric/platform-developer-guide/trained-agents.md) — Manifest schema and configuration
