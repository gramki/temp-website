# Swarm Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/swarms`

**Group:** Agent Fabric

**Purpose:** View and manage Swarms at the current scope — browse visible Swarms, manage owned Swarms, view membership and activity.

> **Console boundary:** Swarm management is an operational activity (like Team management), not an admin activity. Managers at each scope manage their own Swarms. Foundry-level Swarm management is in [Foundry Settings > Agent Fabric](../../foundry-settings/agent-fabric.md).

---

## Type

List + Detail

## Audience

Workbench Managers, Workshop Managers, Workspace Owners

---

## Page Sections

### 1. Swarm Summary

| Metric | Description |
|--------|-------------|
| **Total visible Swarms** | Across all inherited scopes |
| **Owned Swarms** | Swarms managed at this scope |
| **Platform Swarms** | Platform-shipped Swarms |
| **Total Trained Agents** | Aggregate across all visible Swarms |
| **Active Employed Agents** | Currently running instances from visible Swarms |

### 2. Swarm List

| Column | Description |
|--------|-------------|
| **Name** | Swarm identifier (clickable → [Swarm Details](swarm-details.md)) |
| **Scope** | Foundry / Workshop / Workbench / Workspace |
| **Provenance** | Platform-shipped / Tenant-added / Tenant-extended |
| **Trained Agents** | Count of members |
| **Active Employed** | Running instances from this Swarm |
| **Owner** | Who manages this Swarm |
| **Manageable** | Whether current user can edit (based on scope) |

### 3. Scope Tabs

| Tab | Content |
|-----|---------|
| **All** | All visible Swarms across scopes |
| **Foundry** | Foundry-level Swarms |
| **Workshop** | Workshop-level Swarms |
| **Workbench** | Workbench-level Swarms |
| **Workspace** | Workspace-level Swarms (grouped by Workspace) |

### 4. Swarm Activity

Recent activity across all visible Swarms:

| Column | Description |
|--------|-------------|
| **Swarm** | Which Swarm |
| **Event** | Agent added, agent removed, Swarm created, Swarm promoted |
| **Actor** | Who performed the action |
| **Timestamp** | When |

---

## Filters

- By scope (Foundry / Workshop / Workbench / Workspace)
- By provenance (Platform / Tenant)
- By owner
- By activity (active / idle)
- Search by name

---

## Actions

### View Actions (All Users)

| Action | Description |
|--------|-------------|
| View Swarm | Navigate to [Swarm Details](swarm-details.md) |
| View Trained Agents | Navigate to [Trained Agents](trained-agents.md) filtered to Swarm |
| View Employed Agents | Navigate to [Employed Agents](employed-agents.md) filtered to Swarm |

### Management Actions (Scope Owners)

| Action | Who | Description |
|--------|-----|-------------|
| Create Swarm | Manager at scope | Create a new Swarm at the current scope |
| Edit Swarm | Manager at scope | Update Swarm metadata, charter, policies |
| Add Trained Agent | Manager at scope | Add a Trained Agent to an owned Swarm |
| Remove Trained Agent | Manager at scope | Remove a Trained Agent from an owned Swarm |
| Promote Swarm | Manager at scope | Move Swarm manifest to a higher scope |
| Delete Swarm | Manager at scope | Delete an owned Swarm (requires empty membership) |

---

## Access Model

| Scope | Who Can Manage | Via |
|-------|----------------|-----|
| **Foundry Swarms** | Foundry Admin | [Foundry Settings](../../foundry-settings/agent-fabric.md) |
| **Workshop Swarms** | Workshop Manager | This console |
| **Workbench Swarms** | Workbench Manager | This console |
| **Workspace Swarms** | Workspace Owner | This console |

The console shows all Swarms visible at the current scope and allows management of Swarms owned at that scope.

---

## Related Consoles

- **[Agent Fabric Overview](agent-fabric-overview.md)** — Landing page
- **[Swarm Details](swarm-details.md)** — Full Swarm profile + usage analytics
- **[Trained Agents](trained-agents.md)** — Trained Agent list within Swarm
- **[Employed Agents](employed-agents.md)** — Runtime activity from Swarm
- **[Team Console](../workforce/team-console.md)** — Human team management (analogous pattern)

---

## Related Documentation

- [../../../../agent-fabric/concepts/swarm.md](../../../../agent-fabric/concepts/swarm.md) — Swarm concept
- [../../../../agent-fabric/platform-developer-guide/swarm-registry.md](../../../../agent-fabric/platform-developer-guide/swarm-registry.md) — Swarm Registry API
- [../../../../agent-fabric/user-guide/swarms.md](../../../../agent-fabric/user-guide/swarms.md) — Creating and managing Swarms
