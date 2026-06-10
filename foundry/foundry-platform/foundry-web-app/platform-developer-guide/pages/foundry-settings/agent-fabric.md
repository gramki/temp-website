# Foundry Agent Fabric Settings

**URL pattern:** `/foundries/{foundryId}/settings/agent-fabric`

**Purpose:** Foundry-level administration of Agent Fabric — Raw Agent Registry management and Foundry Swarms configuration.

---

## Page Sections

### 1. Agent Fabric Overview

| Element | Description |
|---------|-------------|
| **Platform Raw Agents** | Count of platform-shipped Raw Agents |
| **Tenant Raw Agents** | Count of tenant-added Raw Agents |
| **Foundry Swarms** | Count of Foundry-level Swarms |
| **Total Trained Agents** | Aggregate across Foundry Swarms |
| **Active Employed Agents** | Foundry-wide active instances |

### 2. Raw Agent Registry

#### Platform-Shipped Raw Agents

Raw Agents provided by the Foundry platform:

| Column | Description |
|--------|-------------|
| **Name** | Raw Agent name |
| **OCI URI** | `registry.foundry.io/raw-agents/{agent}:{version}` |
| **Latest version** | Most recent version tag |
| **Interface type** | app-server, cli, sdk, etc. |
| **Trained Agents using** | Count across all scopes |
| **Status** | Active / Deprecated |

#### Tenant-Added Raw Agents

Raw Agents added by this Foundry tenant:

| Column | Description |
|--------|-------------|
| **Name** | Raw Agent name |
| **OCI URI** | `registry.{tenant}.foundry.io/raw-agents/{agent}:{version}` |
| **Latest version** | Most recent version tag |
| **Interface type** | app-server, cli, sdk, etc. |
| **Publisher** | Who added this agent |
| **Trained Agents using** | Count across all scopes |
| **Status** | Active / Deprecated |

### 3. Foundry Swarms

Swarms managed at the Foundry level (visible to all Workshops, Workbenches, Workspaces):

| Column | Description |
|--------|-------------|
| **Name** | Swarm name |
| **Provenance** | Platform-shipped / Tenant-added |
| **Trained Agents** | Count of members |
| **Extended** | Whether tenant has added agents to a platform Swarm |
| **Active Employed** | Running instances from this Swarm |
| **Last modified** | Most recent update |

### 4. Foundry Quota Policy

| Setting | Options | Description |
|---------|---------|-------------|
| **Foundry token budget** | Monthly USD/token limit | Tenant-wide aggregate limit |
| **Workshop allocation** | Per-Workshop limits | Default quota per Workshop |
| **Workbench allocation** | Per-Workbench limits | Default quota per Workbench |
| **Employed Agent limit** | Per-instance limit | Default per-instance cap |
| **Overage policy** | Block / Warn / Allow | What happens when quota is exceeded |

---

## Actions

### Raw Agent Registry Actions

| Action | Who | Description |
|--------|-----|-------------|
| Add Raw Agent | Foundry Admin | Register a new tenant Raw Agent |
| Deprecate Raw Agent | Foundry Admin | Mark a tenant Raw Agent as deprecated |
| Remove Raw Agent | Foundry Admin | Remove a tenant Raw Agent (requires no active references) |
| View details | Foundry Admin | Navigate to Raw Agent details |
| Sync registry | Foundry Admin | Force sync with OCI registry |
| Update Platform version | Foundry Admin | Upgrade platform Raw Agents to newer version |

### Foundry Swarm Actions

| Action | Who | Description |
|--------|-----|-------------|
| Create Swarm | Foundry Admin | Create a new Foundry-level Swarm |
| Edit Swarm | Foundry Admin | Update Swarm charter, policies, membership rules |
| Add Trained Agent | Foundry Admin | Add a Trained Agent to a Foundry Swarm |
| Remove Trained Agent | Foundry Admin | Remove a Trained Agent from a Foundry Swarm |
| Delete Swarm | Foundry Admin | Delete a Foundry Swarm (requires empty membership) |
| Extend Platform Swarm | Foundry Admin | Add tenant Trained Agents to a platform Swarm |

### Quota Actions

| Action | Who | Description |
|--------|-----|-------------|
| Set Foundry budget | Foundry Admin | Configure tenant-wide limits |
| Set Workshop defaults | Foundry Admin | Configure default Workshop allocations |
| View usage report | Foundry Admin | Download Foundry-wide usage/cost report |

---

## Governance

| Policy | Description |
|--------|-------------|
| **Change approval** | All Raw Agent and Swarm changes require Foundry Admin |
| **Audit trail** | All changes recorded with actor, timestamp, reason |
| **Quota enforcement** | Quota changes take effect immediately |
| **Deprecation notice** | 30-day notice before Raw Agent removal |

---

## Related Pages

- **[Workbench Consoles > Agent Fabric](../consoles/agent-fabric/agent-fabric-overview.md)** — Workbench-level Agent Fabric console
- **[Workbench Consoles > Swarm Console](../consoles/agent-fabric/swarm-console.md)** — Swarm management at Workbench scope
- **Foundry Settings > General** — Foundry configuration

---

## Related Documentation

- [../../../../agent-fabric/platform-developer-guide/raw-agent-registry.md](../../../../agent-fabric/platform-developer-guide/raw-agent-registry.md) — Raw Agent Registry API
- [../../../../agent-fabric/platform-developer-guide/swarm-registry.md](../../../../agent-fabric/platform-developer-guide/swarm-registry.md) — Swarm Registry API
- [../../../../agent-fabric/concepts/swarm.md](../../../../agent-fabric/concepts/swarm.md) — Swarm concept
