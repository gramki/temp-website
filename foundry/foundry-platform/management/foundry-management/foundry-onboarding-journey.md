# Foundry Onboarding Journey

This document walks through the complete process of creating and onboarding a new Foundry, from Platform Admin initiation to Foundry Admin completion.

## Overview

```
Platform Admin Creates → Provisioning → Admin Invited → Federation Setup → Initial Config → Active
```

The journey involves two actors:
- **Platform Admin** — Creates the Foundry, initiates onboarding
- **Foundry Admin** — Completes setup, configures the Foundry

## The Journey

### Phase 1: Foundry Creation

**Location:** Platform Admin Web App  
**Actor:** Platform Admin (foundry-platform-admin)

#### Step 1.1: Initiate Foundry Creation

Platform Admin navigates to the Foundries page and clicks "Create Foundry":

```
Platform Admin Web App
└── Foundries
    └── [+ Create Foundry]
```

#### Step 1.2: Provide Foundry Details

Platform Admin fills in the creation form:

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Human-readable Foundry name |
| `slug` | Yes | URL-safe identifier (auto-generated from name) |
| `admin_email` | Yes | Foundry Admin's email address |
| `admin_name` | Yes | Foundry Admin's display name |
| `region` | Yes | Data residency region |
| `pg_instance` | No | Specific PG instance (or auto-assign) |

```json
{
  "name": "Acme Corporation",
  "slug": "acme-corp",
  "admin_email": "alice@acme.com",
  "admin_name": "Alice Smith",
  "region": "us-east-1",
  "pg_instance": null
}
```

#### Step 1.3: Submit Creation Request

Platform Admin submits the form:

```
POST /api/v1/foundries
Body: { ... form data ... }
Response: { foundry_id: "fnd-abc123", status: "provisioning" }
```

---

### Phase 2: Provisioning

**Location:** Platform Backend Services  
**Actor:** Foundry Platform (automated)

#### Step 2.1: Create Database

Platform provisions a logical PostgreSQL database:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PostgreSQL Instance                                                         │
│                                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │  foundry_acme   │  │ foundry_other1  │  │ foundry_other2  │  ...        │
│  │    (new)        │  │                 │  │                 │             │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘             │
└─────────────────────────────────────────────────────────────────────────────┘
```

Database setup:
1. Create logical database `foundry_{slug}`
2. Create database user with credentials
3. Store credentials in secrets store
4. Run schema migrations

#### Step 2.2: Create Storage Partition

Object storage prefix created:

```
s3://foundry-platform-data/
└── fnd-abc123/
    ├── artifacts/
    ├── uploads/
    └── backups/
```

IAM policy applied to restrict access to this prefix.

#### Step 2.3: Register in Olympus Cipher

Foundry registered as an identity client in Olympus Cipher:

```
POST /api/v1/clients (Olympus Cipher)
Body: {
  "client_id": "foundry-fnd-abc123",
  "client_name": "Acme Corporation Foundry",
  "redirect_uris": ["https://acme-corp.foundry.example.com/auth/callback"],
  "grant_types": ["authorization_code", "refresh_token"]
}
```

#### Step 2.4: Create Workshop Definition Repository

GitHub App creates the Workshop Definition Repository:

```
POST /orgs/{platform_org}/repos (GitHub API)
Body: {
  "name": "acme-corp-workshop-definition",
  "private": true,
  "auto_init": true
}
```

Initial structure created:

```
acme-corp-workshop-definition/
├── README.md
├── foundry.yaml          # Foundry-level configuration
├── workshops/            # Workshop definitions (empty)
└── workbenches/          # Workbench definitions (empty)
```

#### Step 2.5: Create Foundry Record

Foundry record created in platform database:

```json
{
  "id": "fnd-abc123",
  "name": "Acme Corporation",
  "slug": "acme-corp",
  "status": "created",
  "admin_email": "alice@acme.com",
  "database_name": "foundry_acme_corp",
  "storage_prefix": "fnd-abc123",
  "cipher_client_id": "foundry-fnd-abc123",
  "workshop_repo": "platform-org/acme-corp-workshop-definition",
  "created_at": "2026-05-29T00:00:00Z"
}
```

---

### Phase 3: Admin Invitation

**Location:** Email / Olympus Cipher  
**Actor:** Foundry Admin (recipient)

#### Step 3.1: Send Invitation Email

Platform sends invitation to Foundry Admin:

```
To: alice@acme.com
Subject: You've been invited to administer Acme Corporation on Foundry Platform

Alice,

You have been designated as the Foundry Administrator for Acme Corporation.

Click below to complete your setup:
https://acme-corp.foundry.example.com/onboarding?token=xyz789

This link expires in 7 days.

— Foundry Platform
```

#### Step 3.2: Admin Clicks Link

Foundry Admin clicks the invitation link and is redirected to onboarding flow.

#### Step 3.3: Admin Authenticates with Olympus Cipher

Admin authenticates via Olympus Cipher:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          Olympus Cipher Login                                │
│                                                                              │
│  Sign in to administer Acme Corporation                                     │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────┐               │
│  │  Email: alice@acme.com                                  │               │
│  └─────────────────────────────────────────────────────────┘               │
│  ┌─────────────────────────────────────────────────────────┐               │
│  │  Password: ••••••••••••                                 │               │
│  └─────────────────────────────────────────────────────────┘               │
│                                                                              │
│                    [ Sign In ]                                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### Phase 4: Federation Setup

**Location:** Foundry Web App (Onboarding Wizard)  
**Actor:** Foundry Admin

#### Step 4.1: Choose Federation Type

Foundry Admin selects how their organization will authenticate:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Step 1: Identity Federation                                                 │
│                                                                              │
│  How will your organization's users authenticate?                           │
│                                                                              │
│  ○ OAuth 2.0                                                                │
│    Connect via OAuth 2.0 protocol                                           │
│                                                                              │
│  ○ SAML                                                                     │
│    Connect via SAML 2.0 protocol                                            │
│                                                                              │
│                              [ Next ]                                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Step 4.2: Configure Federation

For OAuth 2.0:

```yaml
identity:
  provider: olympus-cipher
  federation_type: oauth2
  federation_config:
    authorization_endpoint: https://cipher.olympus.example.com/oauth/authorize
    token_endpoint: https://cipher.olympus.example.com/oauth/token
    userinfo_endpoint: https://cipher.olympus.example.com/oauth/userinfo
    client_id: foundry-fnd-abc123
    scopes: ["openid", "profile", "email", "groups"]
```

For SAML:

```yaml
identity:
  provider: olympus-cipher
  federation_type: saml
  federation_config:
    idp_entity_id: https://cipher.olympus.example.com/saml
    idp_sso_url: https://cipher.olympus.example.com/saml/sso
    idp_certificate: |
      -----BEGIN CERTIFICATE-----
      ...
      -----END CERTIFICATE-----
    sp_entity_id: https://acme-corp.foundry.example.com/saml
```

#### Step 4.3: Test Federation

Admin tests the federation by performing a test login:

```
[ Test Connection ]

✓ Connected to Olympus Cipher
✓ User attributes received
✓ Groups retrieved

Federation test successful!
```

---

### Phase 5: Initial Configuration

**Location:** Foundry Web App (Onboarding Wizard)  
**Actor:** Foundry Admin

#### Step 5.1: Configure GitHub Integration

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Step 2: GitHub Integration                                                  │
│                                                                              │
│  Connect your GitHub organization to enable repository management.          │
│                                                                              │
│  [ Install Foundry GitHub App ]                                             │
│                                                                              │
│  This will redirect you to GitHub to authorize the installation.            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

After GitHub App installation:

```yaml
integrations:
  github:
    app_id: 12345
    app_installation_id: 67890
    organization: acme-corp
```

#### Step 5.2: Configure Jira Integration (Optional)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Step 3: Jira Integration (Optional)                                         │
│                                                                              │
│  Instance URL: https://acme.atlassian.net                                   │
│                                                                              │
│  [ Connect to Jira ]                                                        │
│                                                                              │
│  [ Skip for now ]                                                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Step 5.3: Configure Notifications

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Step 4: Notifications                                                       │
│                                                                              │
│  MS Teams Webhook URL:                                                      │
│  ┌─────────────────────────────────────────────────────────┐               │
│  │  https://outlook.office.com/webhook/...                 │               │
│  └─────────────────────────────────────────────────────────┘               │
│                                                                              │
│  [ Test Notification ]                                                      │
│                                                                              │
│  [ Skip for now ]                                                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Step 5.4: Review and Complete

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Step 5: Review                                                              │
│                                                                              │
│  Foundry: Acme Corporation                                                  │
│  Identity: OAuth 2.0 with Olympus Cipher ✓                                  │
│  GitHub: Connected to acme-corp ✓                                           │
│  Jira: Not configured                                                       │
│  Notifications: MS Teams configured ✓                                       │
│                                                                              │
│  You can configure additional settings later from the Admin Console.        │
│                                                                              │
│                    [ Complete Setup ]                                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### Phase 6: Foundry Active

**Location:** Foundry Web App  
**Actor:** Foundry Admin

#### Step 6.1: Update Foundry Status

Platform marks Foundry as active:

```
PATCH /api/v1/foundries/fnd-abc123
Body: { "status": "active" }
```

#### Step 6.2: Redirect to Admin Console

Foundry Admin is redirected to the Admin Console:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Acme Corporation - Admin Console                                            │
│                                                                              │
│  Welcome, Alice!                                                            │
│                                                                              │
│  Your Foundry is ready. Here's what you can do next:                        │
│                                                                              │
│  → Create your first Workshop                                               │
│  → Invite team members                                                      │
│  → Configure Capable Agents                                                 │
│  → Complete remaining integrations                                          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Step 6.3: Notify Platform Admin

Platform Admin receives notification:

```
To: platform-admin@example.com
Subject: Foundry onboarding completed: Acme Corporation

The Foundry "Acme Corporation" has completed onboarding.

Admin: alice@acme.com
Status: Active
Completed: 2026-05-29 01:30:00 UTC
```

---

## Summary

| Phase | Location | Actor | Key Output |
|-------|----------|-------|------------|
| 1. Creation | Platform Admin App | Platform Admin | Foundry creation request |
| 2. Provisioning | Platform Backend | Automated | Database, storage, repo, identity |
| 3. Invitation | Email | Foundry Admin | Admin authenticated |
| 4. Federation | Onboarding Wizard | Foundry Admin | Identity federation configured |
| 5. Configuration | Onboarding Wizard | Foundry Admin | Integrations configured |
| 6. Active | Foundry Web App | Foundry Admin | Foundry operational |

## Timing

| Phase | Typical Duration |
|-------|------------------|
| Provisioning | 1-2 minutes |
| Admin invitation acceptance | 1-7 days (depends on admin) |
| Federation setup | 10-30 minutes |
| Initial configuration | 15-60 minutes |

## Error Handling

| Error | Handling |
|-------|----------|
| Provisioning failure | Rollback partial resources, notify Platform Admin |
| Invitation expired | Platform Admin can resend invitation |
| Federation test failure | Clear error message, allow retry |
| GitHub App installation failure | Allow retry, provide manual instructions |

## Read Next

- [README.md](README.md) — Foundry Management overview
- [foundry-settings.md](foundry-settings.md) — Complete settings specification
- [../../foundry-platform-admin-web-app/README.md](../../foundry-platform-admin-web-app/README.md) — Platform Admin interface
- [../team-management/README.md](../team-management/README.md) — Adding team members after onboarding
