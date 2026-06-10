# Raw Agent Registry

The Raw Agent Registry manages the catalog of OCI-packaged agent systems available for deployment in Foundry. This specification covers the registry schema, API, two-layer distribution model, and lifecycle management.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|---------------------------|
| **Agent** | Registry catalogs available agent systems by OCI URI |
| **Workforce Repository** | Registry is the source of truth for available Raw Agents |
| **Governance** | Registry enforces versioning, deprecation, and visibility policies |

## Two-Layer Distribution Model

Raw Agents are distributed through a two-layer registry model that separates platform-shipped agents from tenant-added agents.

### Registry Layers

| Layer | Registry URI | Visibility | Managed By |
|-------|--------------|------------|------------|
| **Platform-shipped** | `registry.foundry.io/raw-agents/{agent}:{version}` | All tenants | Foundry Platform |
| **Tenant-added** | `registry.{tenant}.foundry.io/raw-agents/{agent}:{version}` | Organization only | Tenant Org Admin |

### Platform-Shipped Raw Agents

Foundry provides a curated set of Raw Agents available to all tenants:

| Raw Agent | OCI URI | Provider | Primary Interface |
|-----------|---------|----------|-------------------|
| Codex | `registry.foundry.io/raw-agents/codex:v2.4.1` | OpenAI | App-server (JSON-RPC) |
| Cursor Agent | `registry.foundry.io/raw-agents/cursor-agent:v1.2.0` | Cursor | CLI |
| Claude Code | `registry.foundry.io/raw-agents/claude-code:v1.0.3` | Anthropic | CLI |
| Gemini CLI | `registry.foundry.io/raw-agents/gemini-cli:v0.8.0` | Google | CLI |

Platform-shipped agents are:
- Vetted for security and compliance
- Supported by Foundry Platform team
- Automatically available in all tenant registries
- Updated on platform release cadence

### Tenant-Added Raw Agents

Organizations can add custom Raw Agents to their tenant registry:

| Use Case | Example |
|----------|---------|
| Custom tooling | Internal agent with proprietary tools |
| Compliance variants | Modified agent with audit logging |
| Experimental | Candidate agents under evaluation |
| Pinned versions | Specific version locked for stability |

Tenant-added agents are:
- Visible only within the organization
- Managed by Foundry Admin or designated roles
- Not covered by platform support SLA
- Subject to tenant's own security review

## Registry Schema

### Raw Agent Entry

```yaml
apiVersion: foundry.io/v1
kind: RawAgentEntry
metadata:
  name: codex
  version: 2.4.1
  registry: platform  # or 'tenant'
  tenant: null        # populated for tenant registry
  created: "2025-03-15T10:00:00Z"
  updated: "2025-06-01T14:30:00Z"
spec:
  oci-uri: registry.foundry.io/raw-agents/codex:v2.4.1
  provider: openai
  description: OpenAI Codex agent with app-server interface
  interfaces:
    - type: app-server
      protocol: json-rpc
      port: 8080
      recommended: true
    - type: cli
      protocol: spawn-stdio
  models:
    - name: codex-3
      provider: openai
      default: true
    - name: gpt-5
      provider: openai
    - name: gpt-5-thinking
      provider: openai
  deployment:
    modes:
      - container
      - workspace-program
    resources:
      cpu: 2
      memory: 4Gi
      gpu: optional
  capabilities:
    - code-generation
    - code-review
    - test-writing
    - refactoring
  certification:
    security-review: passed
    compliance-review: passed
    reviewed-date: "2025-03-10"
status:
  state: active  # active | deprecated | retired
  deprecation:
    deprecated: false
    successor: null
    sunset-date: null
```

### Schema Reference

| Field | Type | Description |
|-------|------|-------------|
| `metadata.name` | string | Agent identifier (lowercase, alphanumeric) |
| `metadata.version` | string | Semantic version |
| `metadata.registry` | enum | `platform` or `tenant` |
| `metadata.tenant` | string | Tenant ID (null for platform registry) |
| `spec.oci-uri` | string | Full OCI image URI |
| `spec.provider` | string | Agent provider name |
| `spec.interfaces` | list | Supported interfaces |
| `spec.models` | list | Supported models |
| `spec.deployment.modes` | list | `container`, `workspace-program` |
| `spec.deployment.resources` | object | CPU, memory, GPU requirements |
| `spec.capabilities` | list | Declared capabilities for matching |
| `spec.certification` | object | Security and compliance status |
| `status.state` | enum | `active`, `deprecated`, `retired` |

## Registry API

### Discovery Endpoints

```
GET /api/v1/raw-agents
GET /api/v1/raw-agents/{name}
GET /api/v1/raw-agents/{name}/versions
GET /api/v1/raw-agents/{name}/versions/{version}
```

### Discovery Order

When resolving a Raw Agent reference, the registry searches in order:

1. **Tenant registry** — `registry.{tenant}.foundry.io/raw-agents/...`
2. **Platform registry** — `registry.foundry.io/raw-agents/...`

This allows tenants to override platform-shipped agents with custom versions.

### List Raw Agents

```http
GET /api/v1/raw-agents?registry=all&state=active
```

**Query Parameters:**

| Parameter | Values | Default | Description |
|-----------|--------|---------|-------------|
| `registry` | `platform`, `tenant`, `all` | `all` | Filter by registry layer |
| `state` | `active`, `deprecated`, `retired`, `all` | `active` | Filter by lifecycle state |
| `capability` | capability name | — | Filter by declared capability |
| `interface` | interface type | — | Filter by supported interface |

**Response:**

```json
{
  "items": [
    {
      "name": "codex",
      "version": "2.4.1",
      "registry": "platform",
      "oci-uri": "registry.foundry.io/raw-agents/codex:v2.4.1",
      "provider": "openai",
      "state": "active"
    },
    {
      "name": "custom-agent",
      "version": "1.0.0",
      "registry": "tenant",
      "oci-uri": "registry.acme.foundry.io/raw-agents/custom-agent:v1.0.0",
      "provider": "internal",
      "state": "active"
    }
  ],
  "total": 2
}
```

### Get Raw Agent Details

```http
GET /api/v1/raw-agents/codex/versions/2.4.1
```

**Response:**

```json
{
  "metadata": {
    "name": "codex",
    "version": "2.4.1",
    "registry": "platform",
    "created": "2025-03-15T10:00:00Z"
  },
  "spec": {
    "oci-uri": "registry.foundry.io/raw-agents/codex:v2.4.1",
    "provider": "openai",
    "interfaces": [
      { "type": "app-server", "protocol": "json-rpc", "recommended": true },
      { "type": "cli", "protocol": "spawn-stdio" }
    ],
    "models": [
      { "name": "codex-3", "provider": "openai", "default": true },
      { "name": "gpt-5", "provider": "openai" }
    ],
    "deployment": {
      "modes": ["container", "workspace-program"],
      "resources": { "cpu": 2, "memory": "4Gi" }
    }
  },
  "status": {
    "state": "active"
  }
}
```

### Registration (Tenant Registry)

```http
POST /api/v1/raw-agents
Authorization: Bearer {admin-token}
```

**Request:**

```json
{
  "metadata": {
    "name": "custom-agent",
    "version": "1.0.0"
  },
  "spec": {
    "oci-uri": "registry.acme.foundry.io/raw-agents/custom-agent:v1.0.0",
    "provider": "internal",
    "description": "Custom agent for internal workflows",
    "interfaces": [
      { "type": "cli", "protocol": "spawn-stdio", "recommended": true }
    ],
    "models": [
      { "name": "claude-opus", "provider": "anthropic", "default": true }
    ],
    "deployment": {
      "modes": ["container"]
    }
  }
}
```

**Response:** `201 Created`

### Deprecation

```http
PATCH /api/v1/raw-agents/old-agent/versions/1.0.0
Authorization: Bearer {admin-token}
```

**Request:**

```json
{
  "status": {
    "state": "deprecated",
    "deprecation": {
      "deprecated": true,
      "successor": "new-agent:2.0.0",
      "sunset-date": "2026-01-01"
    }
  }
}
```

## Versioning

### Semantic Versioning

Raw Agents use semantic versioning: `MAJOR.MINOR.PATCH`

| Component | When to Increment |
|-----------|-------------------|
| **MAJOR** | Breaking interface changes, model removal |
| **MINOR** | New features, new model support |
| **PATCH** | Bug fixes, security updates |

### Version Constraints

Trained Agents reference Raw Agents with version constraints:

| Constraint | Meaning | Example |
|------------|---------|---------|
| Exact | Specific version | `codex:2.4.1` |
| Caret | Compatible minor | `codex:^2.4.0` → 2.4.x, 2.5.x |
| Tilde | Patch only | `codex:~2.4.0` → 2.4.x |
| Latest | Latest active | `codex:latest` |

### Version Resolution

At task start, WO Runtime resolves version constraints:

1. Parse constraint from Trained Agent manifest
2. Query registry for matching versions
3. Select highest matching active version
4. Record resolved version in task metadata

## Lifecycle Management

### States

| State | Description | Behavior |
|-------|-------------|----------|
| **active** | Available for use | Normal operation |
| **deprecated** | Scheduled for removal | Warning in logs, successor suggested |
| **retired** | No longer available | Cannot be used, returns error |

### Deprecation Flow

```
active
    │
    ├── PATCH status.state = deprecated
    │   └── Set successor and sunset-date
    │
    ├── (sunset-date reached)
    │
    └── PATCH status.state = retired
```

### Deprecation Notifications

When a Raw Agent is deprecated:

1. Trained Agents using it receive warnings in task logs
2. Foundry Admin receives deprecation notice
3. Successor recommendation included in warnings
4. After sunset-date, tasks fail with clear error

## Credential Management

### OCI Registry Authentication

Credentials for pulling OCI images are managed separately from model API credentials.

| Registry | Credential Source |
|----------|-------------------|
| Platform registry | Platform-managed (no tenant config needed) |
| Tenant registry | Tenant secrets store |
| External registry | Tenant secrets store |

### Configuration

```yaml
# In Foundry secrets
oci-registries:
  registry.acme.foundry.io:
    auth:
      type: basic
      username: ${OCI_USERNAME}
      password: ${OCI_PASSWORD}
  registry.external.io:
    auth:
      type: token
      token: ${EXTERNAL_REGISTRY_TOKEN}
```

## Sync to Metadata Service

Registry changes sync to the Metadata Service for discovery:

```
Raw Agent Registry
    │
    ├── Agent registered/updated/deprecated
    │
    ├── Webhook → Metadata Service
    │
    └── Metadata Service updates search index
```

### Sync Events

| Event | Trigger | Action |
|-------|---------|--------|
| `agent.registered` | New agent added | Index new entry |
| `agent.updated` | Metadata changed | Update index |
| `agent.deprecated` | State → deprecated | Mark in index, add warning |
| `agent.retired` | State → retired | Remove from active index |

## Related documentation

- [raw-agents.md](raw-agents.md) — OCI manifest specification, deployment modes
- [trained-agents.md](trained-agents.md) — How Trained Agents reference Raw Agents
- [gateway-policy.md](gateway-policy.md) — Credential resolution at runtime
- [../../work-order-runtime/platform-developer-guide/agent-spawning.md](../../work-order-runtime/platform-developer-guide/agent-spawning.md) — How Raw Agents are pulled and spawned
