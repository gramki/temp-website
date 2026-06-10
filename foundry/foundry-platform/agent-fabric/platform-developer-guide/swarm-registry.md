# Swarm Registry

The Swarm Registry manages the catalog of organizational units for Trained Agents. This specification covers the registry schema, API, scope hierarchy, and the two-layer distribution model.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|---------------------------|
| **Agent** | Registry organizes Trained Agents into functional Swarms |
| **Workforce Repository** | Registry is the source of truth for agent organization |
| **Governance** | Registry enforces scope visibility and membership rules |

## Two-Layer Distribution Model

Swarms are distributed through a two-layer model that separates platform-shipped Swarms from tenant-added Swarms.

### Swarm Layers

| Layer | Examples | Visibility | Managed By |
|-------|----------|------------|------------|
| **Platform-shipped** | Build, Review, Test, Documentation, Release, Governance | All tenants | Foundry Platform |
| **Tenant-added** | Custom Swarms at Foundry/Workshop/Workbench/Workspace scope | Organization only | Tenant roles |

### Platform-Shipped Swarms

Foundry provides standard Swarms available to all tenants:

| Swarm | Purpose | Default Trained Agents |
|-------|---------|------------------------|
| **build-swarm** | Feature implementation | feature-implementer, code-refactorer, test-writer |
| **review-swarm** | Code review and analysis | code-reviewer, security-reviewer, style-checker |
| **test-swarm** | Test execution and analysis | test-executor, test-analyzer, coverage-reporter |
| **documentation-swarm** | Documentation generation | doc-writer, changelog-generator, api-documenter |
| **release-swarm** | Release preparation | release-preparer, deployment-validator |
| **governance-swarm** | Policy and compliance | policy-reviewer, compliance-checker |

Platform-shipped Swarms:
- Are available in all tenants
- Can be extended with tenant Trained Agents
- Cannot be deleted or renamed by tenants
- Receive Trained Agent updates on platform release cadence

### Tenant Swarm Extension

Tenants can add Trained Agents to platform-shipped Swarms:

```yaml
# swarms/build-swarm/trained-agents/custom-implementer.yaml
name: custom-implementer
swarm: build-swarm  # References platform-shipped Swarm
raw-agent-ref: registry.acme.foundry.io/raw-agents/custom-agent:v1.0.0
skills:
  - name: internal-code-generator
    version: ^1.0.0
guardrails:
  - internal-compliance-rules
```

This allows:
- Customization without duplicating Swarms
- Mixed platform + tenant agents in one Swarm
- Scenarios that reference platform Swarms to use tenant agents

## Scope Hierarchy

Swarms exist at four scopes with strict visibility rules:

```
Foundry Swarms (visible to all)
└── Workshop Swarms (visible to Workshop + children)
    └── Workbench Swarms (visible to Workbench + children)
        └── Workspace Swarms (visible to Workspace only)
```

### Scope Resolution

| Scope | Source Path | Managed By |
|-------|-------------|------------|
| **Foundry** | `foundry-{id}/swarms/` | Foundry Admin |
| **Workshop** | `workshop-{id}/swarms/` | Workshop Manager |
| **Workbench** | `workbench-{id}/swarms/` | Workbench Manager |
| **Workspace** | `workbench-{id}/workspaces/{type}/swarms/` | Workspace Owner |

### Visibility Rules

When resolving a Swarm reference:

1. Check current scope (e.g., Workspace)
2. Check parent scope (Workbench)
3. Check grandparent scope (Workshop)
4. Check top scope (Foundry)
5. Check platform-shipped Swarms

First match wins. This allows lower scopes to shadow higher-scope Swarms.

## Registry Schema

### Swarm Definition

```yaml
apiVersion: foundry.io/v1
kind: Swarm
metadata:
  name: build-swarm
  scope: foundry           # foundry | workshop | workbench | workspace
  scope-id: foundry-123    # ID of the containing scope
  layer: platform          # platform | tenant
  created: "2025-01-15T10:00:00Z"
  updated: "2025-06-01T14:30:00Z"
spec:
  description: Agents for feature implementation and code generation
  charter: |
    The Build Swarm contains agents responsible for implementing features,
    refactoring code, and writing tests. Members should prioritize code quality
    and maintainability.
  policies:
    - require-code-review
    - max-file-changes-per-task: 50
  quota:
    max-concurrent-employed: 10
    max-daily-invocations: 1000
    max-daily-tokens: 5000000
```

### Schema Reference

| Field | Type | Description |
|-------|------|-------------|
| `metadata.name` | string | Swarm identifier (lowercase, alphanumeric, hyphens) |
| `metadata.scope` | enum | `foundry`, `workshop`, `workbench`, `workspace` |
| `metadata.scope-id` | string | ID of the containing scope |
| `metadata.layer` | enum | `platform` or `tenant` |
| `spec.description` | string | Human-readable description |
| `spec.charter` | string | Extended description of Swarm purpose and guidelines |
| `spec.policies` | list | Policies applied to all members |
| `spec.quota` | object | Resource quotas for the Swarm |

### Trained Agent Membership

Trained Agents declare their Swarm membership:

```yaml
# swarms/build-swarm/trained-agents/feature-implementer.yaml
apiVersion: foundry.io/v1
kind: TrainedAgent
metadata:
  name: feature-implementer
  swarm: build-swarm
spec:
  raw-agent-ref: registry.foundry.io/raw-agents/codex:v2.4.1
  identity:
    jid: feature-implementer@build-swarm.agents.acme.foundry.io
  skills:
    - name: code-generator
      version: ^2.1.0
  guardrails:
    - no-force-push
    - require-tests-for-new-code
```

**Constraint:** Each Trained Agent belongs to exactly one Swarm.

## Registry API

### Discovery Endpoints

```
GET /api/v1/swarms
GET /api/v1/swarms/{name}
GET /api/v1/swarms/{name}/trained-agents
GET /api/v1/swarms/{name}/trained-agents/{agent}
```

### List Swarms

```http
GET /api/v1/swarms?scope=workbench&scope-id=wb-123&include-inherited=true
```

**Query Parameters:**

| Parameter | Values | Default | Description |
|-----------|--------|---------|-------------|
| `scope` | `foundry`, `workshop`, `workbench`, `workspace` | — | Filter by scope |
| `scope-id` | ID | — | Specific scope instance |
| `include-inherited` | boolean | `true` | Include parent scope Swarms |
| `layer` | `platform`, `tenant`, `all` | `all` | Filter by layer |

**Response:**

```json
{
  "items": [
    {
      "name": "build-swarm",
      "scope": "foundry",
      "layer": "platform",
      "description": "Agents for feature implementation",
      "trained-agent-count": 5
    },
    {
      "name": "custom-swarm",
      "scope": "workbench",
      "scope-id": "wb-123",
      "layer": "tenant",
      "description": "Custom agents for this product",
      "trained-agent-count": 2
    }
  ],
  "total": 2
}
```

### Get Swarm Details

```http
GET /api/v1/swarms/build-swarm?scope=workbench&scope-id=wb-123
```

**Response:**

```json
{
  "metadata": {
    "name": "build-swarm",
    "scope": "foundry",
    "layer": "platform",
    "created": "2025-01-15T10:00:00Z"
  },
  "spec": {
    "description": "Agents for feature implementation and code generation",
    "charter": "The Build Swarm contains agents responsible for...",
    "policies": ["require-code-review"],
    "quota": {
      "max-concurrent-employed": 10,
      "max-daily-invocations": 1000
    }
  },
  "trained-agents": [
    {
      "name": "feature-implementer",
      "layer": "platform",
      "jid": "feature-implementer@build-swarm.agents.acme.foundry.io"
    },
    {
      "name": "custom-implementer",
      "layer": "tenant",
      "jid": "custom-implementer@build-swarm.agents.acme.foundry.io"
    }
  ]
}
```

### Create Swarm (Tenant)

```http
POST /api/v1/swarms
Authorization: Bearer {manager-token}
```

**Request:**

```json
{
  "metadata": {
    "name": "custom-swarm",
    "scope": "workbench",
    "scope-id": "wb-123"
  },
  "spec": {
    "description": "Custom agents for this product",
    "charter": "Agents specialized for our internal workflows",
    "policies": ["internal-compliance"],
    "quota": {
      "max-concurrent-employed": 5
    }
  }
}
```

**Response:** `201 Created`

### Add Trained Agent to Swarm

```http
POST /api/v1/swarms/build-swarm/trained-agents
Authorization: Bearer {manager-token}
```

**Request:**

```json
{
  "metadata": {
    "name": "custom-implementer"
  },
  "spec": {
    "raw-agent-ref": "registry.acme.foundry.io/raw-agents/custom-agent:v1.0.0",
    "skills": [
      { "name": "internal-code-generator", "version": "^1.0.0" }
    ],
    "guardrails": ["internal-compliance-rules"]
  }
}
```

## Hierarchy Enforcement

### Membership Validation

When a Trained Agent is added:

1. **Single membership** — Verify agent not already in another Swarm
2. **Swarm exists** — Verify target Swarm exists at accessible scope
3. **Scope compatibility** — Tenant agents can only join Swarms at or below their scope

### Scope Restrictions

| Trained Agent Scope | Can Join Swarms At |
|--------------------|--------------------|
| Foundry | Foundry, Platform |
| Workshop | Workshop, Foundry, Platform |
| Workbench | Workbench, Workshop, Foundry, Platform |
| Workspace | Workspace, Workbench, Workshop, Foundry, Platform |

### Conflict Resolution

If a tenant creates a Swarm with the same name as a platform Swarm:

- The tenant Swarm shadows the platform Swarm at that scope
- Lower scopes see the tenant Swarm
- Higher scopes still see the platform Swarm
- Recommendation: Use unique names for tenant Swarms

## Promotion

Moving a Swarm to a higher scope increases its visibility:

### Promotion Process

```
Workbench Swarm
    │
    ├── Copy swarm.yaml to Workshop scope
    │   workbench-123/swarms/my-swarm/ → workshop-456/swarms/my-swarm/
    │
    ├── Copy trained-agents/ folder
    │
    ├── Update scope metadata
    │
    └── Swarm now visible to all Workbenches in Workshop
```

### Promotion API

```http
POST /api/v1/swarms/my-swarm/promote
Authorization: Bearer {admin-token}
```

**Request:**

```json
{
  "target-scope": "workshop",
  "target-scope-id": "ws-456"
}
```

### Promotion Rules

| From | To | Who Can Promote |
|------|----|-----------------|
| Workspace | Workbench | Workbench Manager |
| Workbench | Workshop | Workshop Manager |
| Workshop | Foundry | Foundry Admin |

## Quota Management

Quotas are enforced at the Swarm level and aggregate across all Trained Agents:

### Quota Types

| Quota | Description | Enforcement |
|-------|-------------|-------------|
| `max-concurrent-employed` | Max simultaneous Employed Agents | Spawn blocked when limit reached |
| `max-daily-invocations` | Max task invocations per day | Tasks queued when limit reached |
| `max-daily-tokens` | Max token consumption per day | Tasks blocked when limit reached |

### Quota Aggregation

```
Swarm: build-swarm
├── max-concurrent-employed: 10
├── Current employed:
│   ├── feature-implementer: 3
│   ├── code-refactorer: 2
│   └── custom-implementer: 4
└── Total: 9 (1 remaining)
```

## Sync to Metadata Service

Registry changes sync to the Metadata Service for discovery:

### Sync Events

| Event | Trigger | Action |
|-------|---------|--------|
| `swarm.created` | New Swarm added | Index new entry |
| `swarm.updated` | Swarm metadata changed | Update index |
| `swarm.deleted` | Swarm removed | Remove from index |
| `swarm.agent-added` | Trained Agent joined | Update membership |
| `swarm.agent-removed` | Trained Agent left | Update membership |

## Repository Structure

Swarms are stored in dedicated `swarms/` folders:

```
# Foundry-level
foundry-{id}/
├── work-catalog/
└── swarms/
    ├── build-swarm/          # Extends platform Swarm
    │   ├── swarm.yaml        # Optional overrides
    │   └── trained-agents/
    │       └── custom-implementer.yaml
    └── custom-swarm/         # Tenant-created Swarm
        ├── swarm.yaml
        └── trained-agents/
            ├── agent-a.yaml
            └── agent-b.yaml

# Workshop-level
workshop-{id}/
├── work-catalog/
└── swarms/

# Workbench-level  
workbench-{id}/
├── work-catalog/
└── swarms/

# Workspace-level
workbench-{id}/
└── workspaces/
    └── development/
        └── swarms/
```

## Related documentation

- [../concepts/swarm.md](../concepts/swarm.md) — Swarm concept definition
- [trained-agents.md](trained-agents.md) — Trained Agent manifests with Swarm membership
- [raw-agent-registry.md](raw-agent-registry.md) — Raw Agent catalog
- [../user-guide/swarms.md](../user-guide/swarms.md) — How to create and manage Swarms
