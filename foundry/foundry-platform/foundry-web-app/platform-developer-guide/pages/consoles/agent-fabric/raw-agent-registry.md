# Raw Agent Registry Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/raw-agent-registry`

**Group:** Agent Fabric

**Purpose:** Browse and inspect Raw Agents — platform-shipped and tenant-added OCI containers available for training.

---

## Type

List + Detail

## Audience

Workbench Managers, Platform Engineers, Foundry Admins

---

## Page Sections

### 1. Registry Overview

| Metric | Description |
|--------|-------------|
| **Platform Raw Agents** | Count of platform-shipped agents |
| **Tenant Raw Agents** | Count of tenant-added agents |
| **Total versions** | Sum of all available versions |
| **Trained Agents using** | Count of Trained Agents referencing Raw Agents |

### 2. Raw Agent List

| Column | Description |
|--------|-------------|
| **Name** | Raw Agent display name (clickable → [Raw Agent Details](raw-agent-details.md)) |
| **OCI URI** | Registry URI (e.g. `registry.foundry.io/raw-agents/codex:v2.4.1`) |
| **Latest version** | Most recent version tag |
| **Interface type** | app-server, cli, sdk, etc. |
| **Provenance** | Platform-shipped / Tenant-added |
| **Trained Agents** | Count of Trained Agents using this Raw Agent |
| **Status** | Active / Deprecated |

### 3. Version History

When a Raw Agent is selected, show version timeline:

| Column | Description |
|--------|-------------|
| **Version** | Semantic version tag |
| **Published** | Publication date |
| **Trained Agents** | Count referencing this version |
| **Changelog** | Summary of changes |
| **Status** | Active / Deprecated / End-of-Support |

### 4. Capabilities Browser

| Element | Description |
|---------|-------------|
| **Capabilities list** | What the Raw Agent can do (from OCI manifest) |
| **Interface types** | Supported interfaces |
| **Deployment modes** | Container runtime, Coder workspace program |
| **Requirements** | Minimum resources, dependencies |

---

## Filters

- By provenance (Platform / Tenant)
- By interface type
- By status (Active / Deprecated)
- By capability
- Search by name or URI

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| View details | All | Navigate to [Raw Agent Details](raw-agent-details.md) |
| View Trained Agents | All | Show Trained Agents referencing this Raw Agent |
| Copy URI | All | Copy OCI URI to clipboard |

Foundry-level management (add/deprecate/remove) is in [Foundry Settings > Agent Fabric](../../foundry-settings/agent-fabric.md).

---

## Access Model

| Scope | Access |
|-------|--------|
| **Workbench** | Read-only browse and inspect |
| **Workshop** | Read-only browse and inspect |
| **Foundry** | Admin via [Foundry Settings](../../foundry-settings/agent-fabric.md) |

---

## Related Consoles

- **[Agent Fabric Overview](agent-fabric-overview.md)** — Landing page
- **[Swarm Console](swarm-console.md)** — Swarms that contain Trained Agents
- **[Trained Agents](trained-agents.md)** — Trained Agents that reference Raw Agents
- **[Raw Agent Details](raw-agent-details.md)** — Full Raw Agent profile + usage analytics

---

## Related Documentation

- [../../../../agent-fabric/platform-developer-guide/raw-agents.md](../../../../agent-fabric/platform-developer-guide/raw-agents.md) — Raw Agent specification
- [../../../../agent-fabric/platform-developer-guide/raw-agent-registry.md](../../../../agent-fabric/platform-developer-guide/raw-agent-registry.md) — Registry API and schema
