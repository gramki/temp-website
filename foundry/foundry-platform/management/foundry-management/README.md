# Foundry Management — Lifecycle

**Module scope:** Subsystem of Management — Foundry lifecycle, tenancy, settings, and admin console.

## Purpose

A Foundry is the top-level organizational construct in Foundry Platform. Each Foundry represents an isolated tenant — a complete environment for an organization to evolve their products using ACE practices.

Foundry Management handles the full lifecycle of Foundries: creation by platform administrators, configuration by Foundry administrators, ongoing operation, and eventual archival. It ensures strict data isolation between tenants while providing a consistent administrative experience.

The subsystem serves two distinct personas: **Platform Administrators** who create and provision Foundries, and **Foundry Administrators** who configure and manage their own Foundry after onboarding.

## What this subsystem does

- **Foundry lifecycle management** — create, activate, archive, delete Foundries
- **Tenant provisioning** — provision database, storage, repositories, identity
- **Tenant isolation** — enforce data separation across all layers
- **Foundry settings** — configure identity, agents, integrations, governance, defaults
- **Resource quotas** — enforce limits on storage, users, workbenches, model usage
- **Foundry Admin Console** — administrative UI for Foundry configuration

## What this subsystem does NOT do

| Boundary | Owned By |
|----------|----------|
| Create Platform Admin accounts | Platform-level identity (Olympus Cipher) |
| Manage Workshops/Workbenches | Workshop Provisioning, Workbench Provisioning |
| Manage teams and users | Team Management subsystem |
| Execute Work Orders | WO Runtime |

## Tenancy Model

Each Foundry is an isolated tenant:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          Foundry Platform                                    │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                    foundry-platform-admin                              │  │
│  │         (creates Foundries, manages platform infrastructure)           │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                    │                                         │
│                              creates                                         │
│                                    ▼                                         │
│  ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐  │
│  │     Foundry A       │  │     Foundry B       │  │     Foundry C       │  │
│  │                     │  │                     │  │                     │  │
│  │  ┌───────────────┐  │  │  ┌───────────────┐  │  │  ┌───────────────┐  │  │
│  │  │ Logical PG DB │  │  │  │ Logical PG DB │  │  │  │ Logical PG DB │  │  │
│  │  └───────────────┘  │  │  └───────────────┘  │  │  └───────────────┘  │  │
│  │  ┌───────────────┐  │  │  ┌───────────────┐  │  │  ┌───────────────┐  │  │
│  │  │Object Storage │  │  │  │Object Storage │  │  │  │Object Storage │  │  │
│  │  └───────────────┘  │  │  └───────────────┘  │  │  └───────────────┘  │  │
│  └─────────────────────┘  └─────────────────────┘  └─────────────────────┘  │
│           ▲                        ▲                        ▲                │
│           │     strict isolation   │                        │                │
└───────────┴────────────────────────┴────────────────────────┴────────────────┘
```

## Foundry Lifecycle

| State | Description | Managed By |
|-------|-------------|------------|
| **Created** | Foundry provisioned, awaiting admin onboarding | Platform Admin |
| **Active** | Foundry operational, in regular use | Foundry Admin |
| **Archived** | Foundry disabled, data retained | Platform Admin |
| **Deleted** | Foundry and data permanently removed | Platform Admin |

```
Created ──► Active ──► Archived ──► Deleted
              │                        ▲
              └────────────────────────┘
                  (can skip archive)
```

## Tenant Provisioning

When a Platform Admin creates a Foundry, the following resources are provisioned:

| Resource | Provisioning |
|----------|--------------|
| **PostgreSQL Database** | Logical database (possibly separate PG instance) |
| **Object Storage** | Prefix/partition in shared bucket |
| **Foundry Definition Repo** | GitHub repository via GitHub App for Foundry-level config |
| **Identity Registration** | Foundry registered in Olympus Cipher |
| **Foundry Admin Account** | Invitation sent to designated admin |

### Foundry Definition Repository

The Foundry Definition Repo stores organization-wide configuration:

| Content | Purpose |
|---------|---------|
| `foundry.yaml` | Foundry metadata |
| `domain/` | Foundry-level domain knowledge (universal + workspace-specific) |
| `practices/` | Foundry-level practices (universal + workspace-specific) |
| `capable-agents.yaml` | Foundry-level Capable Agent configuration |

Domain and Practices at Foundry level provide the base knowledge layer that cascades to all Workshops and Workbenches.

→ [../foundry-definition-repository.md](../foundry-definition-repository.md) for complete structure

### Database Isolation

- Each Foundry gets a **logical PostgreSQL database**
- Foundries may be on the same or different PG instances (platform decision)
- No cross-database queries; isolation enforced at connection level
- Credentials are Foundry-scoped

### Storage Isolation

- Object storage uses Foundry-prefixed paths: `s3://foundry-data/{foundry_id}/...`
- IAM policies restrict access to Foundry's prefix
- No cross-Foundry access possible

## Tenant Resource Quotas

Foundries have configurable resource limits:

| Quota | Default | Description |
|-------|---------|-------------|
| `max_users` | 500 | Maximum users in Foundry |
| `max_workshops` | 10 | Maximum Workshops |
| `max_workbenches` | 100 | Maximum Workbenches |
| `max_storage_gb` | 500 | Object storage limit |
| `monthly_model_budget_usd` | 10000 | Model usage spending cap |

Quotas are set by Platform Admin and enforced by the platform.

## Foundry Settings

Foundry Admins configure their Foundry through settings. Settings cascade to Workshops and Workbenches.

### Identity

| Setting | Description |
|---------|-------------|
| `identity.provider` | `olympus-cipher` (required) |
| `identity.federation_type` | `oauth2` or `saml` |
| `identity.federation_config` | Provider-specific configuration |
| `identity.user_provisioning` | `jit` (just-in-time) or `scim` |

Foundry connects to **Olympus Cipher** via OAuth 2.0 or SAML federation.

### Capable Agents

| Setting | Description |
|---------|-------------|
| `agents.enabled` | List of enabled Capable Agents |
| `agents.{agent}.api_key_ref` | Reference to credential in secrets store |
| `agents.{agent}.models` | Enabled models for this agent |
| `agents.default_fallback` | Default fallback behavior |

### External Integrations

| Integration | Settings |
|-------------|----------|
| **GitHub** | `integrations.github.app_id`, `app_installation_id`, `webhook_secret_ref` |
| **Jira** | `integrations.jira.instance_url`, `oauth_client_id`, `oauth_client_secret_ref` |
| **Figma** | `integrations.figma.oauth_client_id`, `oauth_client_secret_ref` |
| **TestRail** | `integrations.testrail.instance_url`, `api_key_ref` |
| **Olympus Weave** | `integrations.weave.endpoint`, `api_key_ref` |

### Notifications

| Setting | Description |
|---------|-------------|
| `notifications.ms_teams.webhook_url` | MS Teams incoming webhook |
| `notifications.ms_teams.channels` | Channel mapping by alert type |
| `notifications.email.smtp_config` | SMTP configuration (optional) |

### Governance

| Setting | Description |
|---------|-------------|
| `governance.required_gates` | List of mandatory governance gates |
| `governance.audit_retention_days` | How long to retain audit logs |
| `governance.evidence_retention_days` | How long to retain evidence packs |

### Defaults

| Setting | Description |
|---------|-------------|
| `defaults.workshop_template` | Default configuration for new Workshops |
| `defaults.workbench_template` | Default configuration for new Workbenches |
| `defaults.workspace_image` | Default devcontainer base image |

→ [foundry-settings.md](foundry-settings.md) for complete settings specification

## Foundry Admin Console

The Foundry Admin Console is a section of the Foundry Web App accessible to Foundry Administrators.

### Console Sections

| Section | Capabilities |
|---------|--------------|
| **Dashboard** | Foundry health, usage metrics, alerts |
| **Workshops** | List, create, configure Workshops |
| **Teams** | Manage teams, roles, permissions (via Team Management) |
| **Capable Agents** | Enable/disable agents, configure credentials |
| **Integrations** | Connect external tools (GitHub, Jira, etc.) |
| **Quotas** | View quotas, current usage |
| **Settings** | All Foundry-level settings |
| **Audit Log** | View audit trail |

### Foundry Admin Permissions

| Permission | Description |
|------------|-------------|
| `foundry.settings.read` | View Foundry settings |
| `foundry.settings.write` | Modify Foundry settings |
| `foundry.workshops.create` | Create Workshops |
| `foundry.teams.manage` | Manage teams and roles |
| `foundry.agents.configure` | Configure Capable Agents |
| `foundry.integrations.manage` | Manage external integrations |
| `foundry.audit.read` | View audit logs |

## ACE Concepts Realized

| Concept | How this subsystem realizes it |
|---------|--------------------------------|
| **Foundry** | Full lifecycle management of the Foundry construct |
| **Workshop** | Provides container (Foundry) for Workshop provisioning |
| **Tenancy** | Implements multi-tenant isolation model |

## Key Design Decisions

- **Foundry = Tenant.** No separate tenancy abstraction; each Foundry is a complete isolated tenant.
- **Platform Admin creates, Foundry Admin configures.** Clear separation of responsibilities.
- **Logical database isolation.** Each Foundry gets its own PostgreSQL database; no schema-level sharing.
- **Settings cascade.** Foundry settings are defaults that Workshops/Workbenches can override.
- **Olympus Cipher for identity.** All Foundries federate with Olympus Cipher; no local identity stores.
- **No commercial constructs.** Foundry management has no billing or subscription concepts.

## Open Questions

- Foundry migration between PG instances
- Foundry data export for compliance
- Foundry clone/template functionality
- Cross-Foundry collaboration (if ever needed)

## Module Documents

| Document | Content |
|----------|---------|
| [foundry-onboarding-journey.md](foundry-onboarding-journey.md) | End-to-end Foundry creation and setup |
| [foundry-settings.md](foundry-settings.md) | Complete settings specification |
| [../foundry-definition-repository.md](../foundry-definition-repository.md) | Foundry repository structure |

## Read Next

- [../foundry-definition-repository.md](../foundry-definition-repository.md) — Foundry repository structure
- [../knowledge-management/README.md](../knowledge-management/README.md) — Knowledge Management subsystem
- [../team-management/README.md](../team-management/README.md) — Team and user management
- [../services/metadata-service.md](../services/metadata-service.md) — Where Foundry config is stored
- [../../foundry-platform-admin-web-app/README.md](../../foundry-platform-admin-web-app/README.md) — Platform Admin interface
- [../README.md](../README.md) — Management module overview
