# Foundry Settings Specification

This document provides the complete specification for Foundry-level settings, including keys, types, defaults, and cascade behavior.

## Overview

Foundry settings configure the behavior of a Foundry and its child Workshops and Workbenches. Settings are organized into categories and follow a hierarchical cascade:

```
Foundry Settings (defaults)
    └── Workshop Settings (can override)
        └── Workbench Settings (can override)
            └── Workspace Settings (can override)
```

## Settings Categories

| Category | Purpose |
|----------|---------|
| `identity` | Authentication and user provisioning |
| `agents` | Capable Agent configuration |
| `integrations` | External tool connections |
| `notifications` | Alert and notification channels |
| `governance` | Compliance and audit settings |
| `defaults` | Template defaults for child entities |
| `quotas` | Resource limits (read-only, set by Platform Admin) |

---

## Identity Settings

Authentication and user provisioning configuration.

### identity.provider

```yaml
key: identity.provider
type: enum
allowed_values: [olympus-cipher]
default: olympus-cipher
mutable: false
cascade: no
description: Identity provider for the Foundry (always Olympus Cipher)
```

### identity.federation_type

```yaml
key: identity.federation_type
type: enum
allowed_values: [oauth2, saml]
default: null
mutable: true
cascade: no
description: Federation protocol used with Olympus Cipher
```

### identity.federation_config

```yaml
key: identity.federation_config
type: object
schema:
  # For OAuth 2.0
  oauth2:
    authorization_endpoint: { type: string, format: url }
    token_endpoint: { type: string, format: url }
    userinfo_endpoint: { type: string, format: url }
    client_id: { type: string }
    client_secret_ref: { type: string }  # Reference to secrets store
    scopes: { type: array, items: string }
  
  # For SAML
  saml:
    idp_entity_id: { type: string }
    idp_sso_url: { type: string, format: url }
    idp_certificate: { type: string }
    sp_entity_id: { type: string }
    attribute_mapping: { type: object }

default: null
mutable: true
cascade: no
description: Protocol-specific federation configuration
```

### identity.user_provisioning

```yaml
key: identity.user_provisioning
type: enum
allowed_values: [jit, scim, manual]
default: jit
mutable: true
cascade: no
description: |
  How users are provisioned:
  - jit: Just-in-time on first login
  - scim: SCIM-based sync from IdP
  - manual: Admin manually creates users
```

### identity.default_role

```yaml
key: identity.default_role
type: string
default: foundry-member
mutable: true
cascade: no
description: Default role assigned to newly provisioned users
```

---

## Capable Agent Settings

Configuration for AI agents available in the Foundry.

### agents.enabled

```yaml
key: agents.enabled
type: array
items:
  type: object
  properties:
    agent_id: { type: string }  # e.g., "cursor-agent", "github-copilot"
    enabled: { type: boolean }
schema_example:
  - agent_id: cursor-agent
    enabled: true
  - agent_id: github-copilot
    enabled: true
  - agent_id: anthropic-claude
    enabled: false
default: []
mutable: true
cascade: override
description: List of Capable Agents enabled for this Foundry
```

### agents.{agent_id}.api_key_ref

```yaml
key: agents.{agent_id}.api_key_ref
type: string
default: null
mutable: true
cascade: override
description: Reference to API key in secrets store for the specified agent
example: secrets://foundry/fnd-abc123/cursor-agent-api-key
```

### agents.{agent_id}.models

```yaml
key: agents.{agent_id}.models
type: array
items: { type: string }
default: []  # All models enabled by default
mutable: true
cascade: override
description: Specific models enabled for this agent (empty = all)
example:
  - claude-3-opus
  - claude-3-sonnet
```

### agents.{agent_id}.quota

```yaml
key: agents.{agent_id}.quota
type: object
schema:
  monthly_budget_usd: { type: number, minimum: 0 }
  daily_limit_requests: { type: integer, minimum: 0 }
  hourly_limit_requests: { type: integer, minimum: 0 }
default:
  monthly_budget_usd: 10000
  daily_limit_requests: 0  # 0 = no limit
  hourly_limit_requests: 0
mutable: true
cascade: sum  # Child quotas cannot exceed parent
description: Usage quotas for this Capable Agent
```

### agents.default_fallback

```yaml
key: agents.default_fallback
type: boolean
default: true
mutable: true
cascade: override
description: Whether to automatically fall back to alternative agents when primary is unavailable
```

---

## Integration Settings

External tool connections.

### integrations.atropos

```yaml
key: integrations.atropos
type: object
schema:
  base_url: { type: string, format: url }
  tenant_id: { type: string }           # maps to foundry-id in event paths
  callback_auth_ref: { type: string }   # secret for validating inbound callbacks
default: null
mutable: true
cascade: no
description: Atropos (Olympus event fabric) integration. Platform events use paths `/{foundry-id}/foundry.{module}.{event}`. See event-contracts.md.
```

### integrations.github

```yaml
key: integrations.github
type: object
schema:
  app_id: { type: integer }
  app_installation_id: { type: integer }
  organization: { type: string }
  webhook_secret_ref: { type: string }
default: null
mutable: true
cascade: no
description: GitHub App integration configuration
```

### integrations.jira

```yaml
key: integrations.jira
type: object
schema:
  instance_url: { type: string, format: url }
  oauth_client_id: { type: string }
  oauth_client_secret_ref: { type: string }
  project_key_pattern: { type: string }  # Regex for allowed project keys
default: null
mutable: true
cascade: no
description: Jira Cloud/Server integration configuration (Work Repository adapter). Shared projects filter by `foundry-workbench-{workbenchId}`; Work Orders use dedicated `workRepoProject`.
```

### integrations.figma

```yaml
key: integrations.figma
type: object
schema:
  oauth_client_id: { type: string }
  oauth_client_secret_ref: { type: string }
default: null
mutable: true
cascade: no
description: Figma integration for design assets
```

### integrations.testrail

```yaml
key: integrations.testrail
type: object
schema:
  instance_url: { type: string, format: url }
  api_key_ref: { type: string }
default: null
mutable: true
cascade: no
description: TestRail integration for test management
```

### integrations.weave

```yaml
key: integrations.weave
type: object
schema:
  endpoint: { type: string, format: url }
  api_key_ref: { type: string }
default: null
mutable: true
cascade: no
description: Olympus Weave integration for observability
```

---

## Notification Settings

Alert and notification channel configuration.

### notifications.ms_teams

```yaml
key: notifications.ms_teams
type: object
schema:
  webhook_url: { type: string, format: url }
  channels:
    alerts: { type: string }      # Channel for system alerts
    releases: { type: string }    # Channel for release notifications
    governance: { type: string }  # Channel for governance notifications
default: null
mutable: true
cascade: override
description: MS Teams incoming webhook configuration
```

### notifications.email

```yaml
key: notifications.email
type: object
schema:
  smtp_host: { type: string }
  smtp_port: { type: integer }
  smtp_username: { type: string }
  smtp_password_ref: { type: string }
  from_address: { type: string, format: email }
  from_name: { type: string }
default: null
mutable: true
cascade: no
description: Email notification configuration (optional)
```

### notifications.preferences

```yaml
key: notifications.preferences
type: object
schema:
  wo_assigned: { type: array, items: { type: string, enum: [ms_teams, email] } }
  wo_completed: { type: array, items: { type: string, enum: [ms_teams, email] } }
  governance_required: { type: array, items: { type: string, enum: [ms_teams, email] } }
  release_deployed: { type: array, items: { type: string, enum: [ms_teams, email] } }
default:
  wo_assigned: [ms_teams]
  wo_completed: []
  governance_required: [ms_teams, email]
  release_deployed: [ms_teams]
mutable: true
cascade: override
description: Which notification types go to which channels
```

---

## Governance Settings

Compliance, audit, and governance configuration.

### governance.required_gates

```yaml
key: governance.required_gates
type: array
items:
  type: object
  properties:
    gate_id: { type: string }
    applies_to: { type: array, items: { type: string } }  # Scenario types
    required: { type: boolean }
schema_example:
  - gate_id: product-specification-review
    applies_to: [create-product-specification]
    required: true
  - gate_id: security-review
    applies_to: [implement-product-specification]
    required: true
default: []
mutable: true
cascade: merge
description: Governance gates required before certain scenarios complete
```

### governance.audit_retention_days

```yaml
key: governance.audit_retention_days
type: integer
minimum: 30
maximum: 3650
default: 365
mutable: true
cascade: no
description: How long to retain audit logs
```

### governance.evidence_retention_days

```yaml
key: governance.evidence_retention_days
type: integer
minimum: 30
maximum: 3650
default: 730
mutable: true
cascade: no
description: How long to retain evidence packs from governance scenarios
```

### governance.auto_archive_completed_pi_days

```yaml
key: governance.auto_archive_completed_pi_days
type: integer
minimum: 0  # 0 = never auto-archive
default: 90
mutable: true
cascade: override
description: Auto-archive completed Product Intents after this many days
```

---

## Default Settings

Template defaults for child entities.

### defaults.workshop_template

```yaml
key: defaults.workshop_template
type: object
schema:
  # Any Workshop settings that can be pre-configured
  description_template: { type: string }
  default_workspace_count: { type: integer }
default:
  description_template: "Workshop for {name}"
  default_workspace_count: 5
mutable: true
cascade: no
description: Default configuration applied when creating new Workshops
```

### defaults.workbench_template

```yaml
key: defaults.workbench_template
type: object
schema:
  default_scenario_set: { type: string }  # Reference to scenario set
  auto_create_workspaces: { type: boolean }
default:
  default_scenario_set: standard-build
  auto_create_workspaces: true
mutable: true
cascade: no
description: Default configuration applied when creating new Workbenches
```

### defaults.workspace_image

```yaml
key: defaults.workspace_image
type: string
default: "ghcr.io/foundry-platform/workspace-base:latest"
mutable: true
cascade: override
description: Default devcontainer base image for Workspaces
```

---

## Quota Settings (Read-Only)

Resource limits set by Platform Admin. Foundry Admins can view but not modify.

### quotas.max_users

```yaml
key: quotas.max_users
type: integer
default: 500
mutable: false  # Set by Platform Admin only
cascade: no
description: Maximum users allowed in this Foundry
```

### quotas.max_workshops

```yaml
key: quotas.max_workshops
type: integer
default: 10
mutable: false
cascade: no
description: Maximum Workshops allowed
```

### quotas.max_workbenches

```yaml
key: quotas.max_workbenches
type: integer
default: 100
mutable: false
cascade: no
description: Maximum Workbenches allowed (across all Workshops)
```

### quotas.max_storage_gb

```yaml
key: quotas.max_storage_gb
type: integer
default: 500
mutable: false
cascade: no
description: Maximum object storage in GB
```

### quotas.monthly_model_budget_usd

```yaml
key: quotas.monthly_model_budget_usd
type: number
default: 10000
mutable: false
cascade: no
description: Monthly spending cap for model usage (all agents combined)
```

---

## Cascade Behavior

Settings follow different cascade rules:

| Cascade Type | Behavior |
|--------------|----------|
| `no` | Setting is Foundry-only; does not cascade to children |
| `override` | Child entity can override with any value |
| `merge` | Child entity's value is merged with parent (arrays combined) |
| `sum` | Child values must sum to less than or equal to parent (quotas) |

### Cascade Example

```yaml
# Foundry settings
agents.cursor-agent.quota.monthly_budget_usd: 10000

# Workshop settings (overrides)
agents.cursor-agent.quota.monthly_budget_usd: 5000  # Can be less than Foundry

# Workbench settings
agents.cursor-agent.quota.monthly_budget_usd: 2000  # Can be less than Workshop
```

---

## Settings API

### Get Settings

```http
GET /api/v1/foundries/{foundry_id}/settings
GET /api/v1/foundries/{foundry_id}/settings/{category}
GET /api/v1/foundries/{foundry_id}/settings/{category}/{key}
```

### Update Settings

```http
PATCH /api/v1/foundries/{foundry_id}/settings
Content-Type: application/json

{
  "agents.cursor-agent.quota.monthly_budget_usd": 15000,
  "notifications.ms_teams.webhook_url": "https://..."
}
```

### Reset to Default

```http
DELETE /api/v1/foundries/{foundry_id}/settings/{category}/{key}
```

### Get Effective Settings

Returns settings with cascade resolution from parent entities:

```http
GET /api/v1/workbenches/{workbench_id}/settings/effective
```

---

## Settings Validation

Settings are validated on write:

1. **Type validation** — Value matches declared type
2. **Format validation** — URLs, emails validated
3. **Range validation** — Numbers within min/max
4. **Reference validation** — Secret references exist
5. **Cascade validation** — Child values respect parent constraints

### Validation Errors

```json
{
  "error": "validation_failed",
  "details": [
    {
      "key": "agents.cursor-agent.quota.monthly_budget_usd",
      "error": "exceeds_parent_quota",
      "message": "Value 15000 exceeds Foundry quota of 10000"
    }
  ]
}
```

---

## Web App UI Mapping

This section maps settings categories to the Foundry Web App pages where they are exposed.

### Foundry-Level Settings Pages

| Settings category | Web App page | URL pattern | Notes |
|-------------------|--------------|-------------|-------|
| Work Catalog policy | [Foundry Work Catalogs Settings](../../foundry-web-app/platform-developer-guide/pages/foundry-settings/work-catalogs.md) | `/foundries/{foundryId}/settings/work-catalogs` | User catalog policy, Platform version |
| Identity | TBD | `/foundries/{foundryId}/settings/identity` | Page spec pending |
| Capable Agents | TBD | `/foundries/{foundryId}/settings/agents` | Page spec pending |
| Integrations | TBD | `/foundries/{foundryId}/settings/integrations` | Page spec pending |
| Notifications | TBD | `/foundries/{foundryId}/settings/notifications` | Page spec pending |
| Governance | TBD | `/foundries/{foundryId}/settings/governance` | Page spec pending |
| Defaults | TBD | `/foundries/{foundryId}/settings/defaults` | Page spec pending |
| Quotas | [Foundry Home](../../foundry-web-app/platform-developer-guide/pages/foundry-home.md) | `/` | View-only in dashboard |

### Workbench-Level Settings Inheritance

Settings that cascade to Workbenches are managed in the [Admin Console](../../foundry-web-app/platform-developer-guide/pages/consoles/settings/admin-console.md):

| Settings category | Admin Console section | Override behavior |
|-------------------|----------------------|-------------------|
| Integrations | Integration Settings | Workbench can add connections |
| Notifications | Notification Settings | Workbench can customize channels |
| Governance | Governance Configuration | Subject to inheritance rules |

See [governance-admin.md](../../foundry-web-app/platform-developer-guide/pages/consoles/settings/governance-admin.md) for governance inheritance configuration.

### Cross-Reference Notes

1. **Foundry Home page** references "Platform Settings" navigation but detailed page specs for most Foundry settings categories are pending.
2. **Work Catalog settings** are fully specified in the Web App page specs.
3. **Governance settings** have detailed Web App specs at the Workbench level (Governance Admin Console) but Foundry-level governance settings page spec is pending.
4. **Quota settings** are read-only and displayed in Foundry Home dashboard; no dedicated settings page required.

---

## Read Next

- [README.md](README.md) — Foundry Management overview
- [foundry-onboarding.md](foundry-onboarding.md) — Initial settings during onboarding
- [../platform-developer-guide/services/metadata-service.md](../platform-developer-guide/services/metadata-service.md) — Where settings are stored
- [../../foundry-web-app/platform-developer-guide/pages/README.md](../../foundry-web-app/platform-developer-guide/pages/README.md) — Web App pages overview
