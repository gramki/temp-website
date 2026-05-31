# Platform Settings Page

**Path:** `/settings`

## Purpose

The Platform Settings page allows Platform Admins to configure global settings that apply to the entire Foundry Platform and serve as defaults for new Foundries.

## Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Platform Admin                                              [Admin Name ▼] │
├─────────────────────────────────────────────────────────────────────────────┤
│  Dashboard │ Foundries │ Infrastructure │ Settings                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Platform Settings                                                          │
│                                                                              │
│  ┌──────────────────────────────────────┐                                   │
│  │  General                             │                                   │
│  │  Default Quotas                      │                                   │
│  │  GitHub Integration                  │                                   │
│  │  Olympus Cipher                      │                                   │
│  │  Atropos                             │                                   │
│  │  Regions                             │                                   │
│  │  Audit & Compliance                  │                                   │
│  └──────────────────────────────────────┘                                   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  GENERAL                                             [Save Changes]  │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │                                                                      │   │
│  │  Platform Name                                                       │   │
│  │  ┌─────────────────────────────────────────────────────────────┐    │   │
│  │  │  Foundry Platform                                           │    │   │
│  │  └─────────────────────────────────────────────────────────────┘    │   │
│  │  Displayed in emails and notifications.                             │   │
│  │                                                                      │   │
│  │  Platform Domain                                                    │   │
│  │  ┌─────────────────────────────────────────────────────────────┐    │   │
│  │  │  foundry.example.com                                        │    │   │
│  │  └─────────────────────────────────────────────────────────────┘    │   │
│  │  Base domain for Foundry URLs: {slug}.foundry.example.com           │   │
│  │                                                                      │   │
│  │  Support Email                                                       │   │
│  │  ┌─────────────────────────────────────────────────────────────┐    │   │
│  │  │  support@foundry.example.com                                │    │   │
│  │  └─────────────────────────────────────────────────────────────┘    │   │
│  │  Displayed in error messages and help links.                        │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Settings Categories

### General

Basic platform identification and contact information.

| Setting | Type | Description |
|---------|------|-------------|
| `platform_name` | String | Display name for the platform |
| `platform_domain` | String | Base domain for Foundry URLs |
| `support_email` | Email | Support contact email |
| `support_url` | URL | Link to support portal (optional) |

### Default Quotas

Default resource limits applied to newly created Foundries. Foundries can have these adjusted individually.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEFAULT QUOTAS                                             [Save Changes]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  These defaults are applied when creating new Foundries.                   │
│  Individual Foundry quotas can be adjusted on the Foundry detail page.     │
│                                                                              │
│  Default Max Users                                                          │
│  ┌────────────────────┐                                                    │
│  │  500               │                                                    │
│  └────────────────────┘                                                    │
│                                                                              │
│  Default Max Workshops                                                      │
│  ┌────────────────────┐                                                    │
│  │  10                │                                                    │
│  └────────────────────┘                                                    │
│                                                                              │
│  Default Max Workbenches                                                    │
│  ┌────────────────────┐                                                    │
│  │  100               │                                                    │
│  └────────────────────┘                                                    │
│                                                                              │
│  Default Storage (GB)                                                       │
│  ┌────────────────────┐                                                    │
│  │  500               │                                                    │
│  └────────────────────┘                                                    │
│                                                                              │
│  Default Monthly Model Budget (USD)                                         │
│  ┌────────────────────┐                                                    │
│  │  10000             │                                                    │
│  └────────────────────┘                                                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### GitHub Integration

Platform-level GitHub App configuration.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  GITHUB INTEGRATION                                         [Save Changes]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  The Foundry Platform uses a GitHub App to create and manage                │
│  Workshop Definition Repositories for each Foundry.                         │
│                                                                              │
│  GitHub App ID                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  12345                                                             │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  GitHub App Private Key                                                     │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  ••••••••••••••••••••••••••••••                      [Update Key]  │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│  Last updated: May 15, 2026                                                │
│                                                                              │
│  GitHub Organization                                                        │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  foundry-platform-repos                                            │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│  Organization where Workshop repos are created.                            │
│                                                                              │
│  Webhook Secret                                                             │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  ••••••••••••••••••••••••••••••                   [Regenerate]     │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  Connection Status: ● Connected                   [Test Connection]         │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Olympus Cipher

Platform's identity provider configuration.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  OLYMPUS CIPHER                                             [Save Changes]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Olympus Cipher is the identity provider for the Foundry Platform.         │
│  Platform Admins authenticate via Cipher, and Foundries federate           │
│  their identity through Cipher.                                            │
│                                                                              │
│  Cipher Instance URL                                                        │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  https://cipher.olympus.example.com                                │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  Platform Admin Group                                                       │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  foundry-platform-admin                                            │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│  Members of this Cipher group can access the Platform Admin Web App.       │
│                                                                              │
│  OAuth Client ID                                                            │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  foundry-platform-admin-app                                        │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  OAuth Client Secret                                                        │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  ••••••••••••••••••••••••••••••                      [Update]      │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  Connection Status: ● Connected                   [Test Connection]         │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Atropos

Platform-wide configuration for the Olympus event fabric. Each Foundry receives a tenant id used as the first path segment for all platform events.

| Setting | Type | Description |
|---------|------|-------------|
| `atropos.base_url` | URL | Atropos service endpoint (default: `https://atropos.olympus.tech`) |
| `atropos.platform_callback_secret_ref` | Secret ref | Shared secret for validating platform-level callbacks |
| `atropos.default_retention_days` | Integer | Event retention (default: 7) |

Foundry-level overrides (`integrations.atropos`) are configured during Foundry provisioning. Path convention: `/{foundry-id}/foundry.{module}.{event-semantic-name}`. See [event-contracts.md](../../../../foundry-work-plan/phase-1/event-contracts.md).

### Regions

Available regions for Foundry deployment.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  REGIONS                                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Regions where Foundries can be deployed. Each region must have             │
│  PostgreSQL and object storage infrastructure available.                    │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  Region        Display Name        Status     Foundries            │    │
│  │  ──────────────────────────────────────────────────────────────── │    │
│  │  us-east-1     US East (Virginia)  ● Active   12                  │    │
│  │  us-east-2     US East (Ohio)      ● Active   8                   │    │
│  │  eu-west-1     EU (Ireland)        ● Active   4                   │    │
│  │  ap-south-1    Asia (Mumbai)       ○ Planned  0                   │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  [+ Add Region]                                                             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Audit & Compliance

Platform-level audit and compliance settings.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AUDIT & COMPLIANCE                                         [Save Changes]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Platform Audit Log Retention (days)                                        │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  365                                                               │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│  How long to retain platform-level audit logs (admin actions, etc.)        │
│                                                                              │
│  Minimum Foundry Audit Retention (days)                                     │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  90                                                                │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│  Minimum retention Foundries must maintain (they can set higher).          │
│                                                                              │
│  Archived Foundry Data Retention (days)                                     │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  365                                                               │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│  How long to retain data after a Foundry is archived.                      │
│                                                                              │
│  Enable Audit Log Export                                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  [✓] Export audit logs to external SIEM                             │   │
│  │                                                                      │   │
│  │  Export Destination                                                  │   │
│  │  ┌─────────────────────────────────────────────────────────────┐    │   │
│  │  │  s3://audit-exports/foundry-platform/                       │    │   │
│  │  └─────────────────────────────────────────────────────────────┘    │   │
│  │                                                                      │   │
│  │  Export Format: [JSON ▼]                                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Settings Persistence

Settings changes are:
1. Validated on form submission
2. Saved to platform configuration store
3. Logged to audit trail
4. Applied immediately (or on next Foundry creation for defaults)

## Sensitive Settings

Settings containing secrets (API keys, private keys, etc.) are:
- Displayed masked (••••••••)
- Stored encrypted in secrets store
- Never returned in full via API
- Require explicit "Update" action to change

## API Dependencies

```yaml
GET /api/v1/admin/settings
Response:
  general:
    platform_name: "Foundry Platform"
    platform_domain: "foundry.example.com"
    support_email: "support@foundry.example.com"
  default_quotas:
    max_users: 500
    max_workshops: 10
    max_workbenches: 100
    max_storage_gb: 500
    monthly_model_budget_usd: 10000
  github:
    app_id: 12345
    organization: "foundry-platform-repos"
    has_private_key: true
    has_webhook_secret: true
    connection_status: "connected"
  cipher:
    instance_url: "https://cipher.olympus.example.com"
    admin_group: "foundry-platform-admin"
    oauth_client_id: "foundry-platform-admin-app"
    has_client_secret: true
    connection_status: "connected"
  atropos:
    base_url: "https://atropos.olympus.tech"
    default_retention_days: 7
    has_platform_callback_secret: true
    connection_status: "connected"
  regions:
    - id: "us-east-1"
      display_name: "US East (Virginia)"
      status: "active"
      foundries_count: 12
  audit:
    platform_log_retention_days: 365
    min_foundry_retention_days: 90
    archived_foundry_retention_days: 365
    export_enabled: true
    export_destination: "s3://audit-exports/foundry-platform/"
    export_format: "json"

PATCH /api/v1/admin/settings
Body: { "general.platform_name": "New Platform Name", ... }
Response: { settings: {...} }

POST /api/v1/admin/settings/github/test
Response: { success: true, message: "Connected successfully" }

POST /api/v1/admin/settings/cipher/test
Response: { success: true, message: "Connected successfully" }
```

## Validation

| Setting | Validation |
|---------|------------|
| `platform_domain` | Valid domain format, not already in use |
| `support_email` | Valid email format |
| Quota values | Positive integers |
| `github.app_id` | Numeric |
| `github.private_key` | Valid PEM format |
| `cipher.instance_url` | Valid HTTPS URL |
| Region IDs | Alphanumeric, lowercase, hyphens only |
| Retention days | Positive integers, within allowed range |

## Confirmation Dialogs

Sensitive changes show confirmation:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Confirm Settings Change                                               [×] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  You are about to change:                                                   │
│                                                                              │
│  • Platform domain: foundry.example.com → foundry.newdomain.com            │
│                                                                              │
│  This change will affect all Foundry URLs.                                 │
│                                                                              │
│                                        [Cancel]  [Confirm Change]           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```
