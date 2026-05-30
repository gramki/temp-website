# Onboarding a New Foundry

## Purpose

This guide walks through the complete process of creating and onboarding a new Foundry, from Platform Admin initiation through Foundry Admin configuration to an operational Foundry ready for Workshops and Workbenches.

## Audience

| Role | When to use this guide |
|------|------------------------|
| Platform Admin | When creating a new Foundry for an organization |
| Foundry Admin | When completing initial setup after receiving an invitation |

## Prerequisites

- **Platform Admin:** Access to the Platform Admin Web App with `foundry.create` permission
- **Foundry Admin:** Invitation email from Platform Admin, Olympus Cipher account (or ability to create one)
- **Prior reading:** [Foundry Management overview](../README.md), [Platform Admin Web App](../../foundry-platform-admin-web-app/README.md)

---

## Steps

### 1. Initiate Foundry creation (Platform Admin)

Navigate to the Foundries page in the Platform Admin Web App and click **Create Foundry**.

```
Platform Admin Web App
└── Foundries
    └── [+ Create Foundry]
```

### 2. Provide Foundry details (Platform Admin)

Fill in the creation form with the following information:

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Human-readable Foundry name |
| `slug` | Yes | URL-safe identifier (auto-generated from name) |
| `admin_email` | Yes | Foundry Admin's email address |
| `admin_name` | Yes | Foundry Admin's display name |
| `region` | Yes | Data residency region |
| `pg_instance` | No | Specific PG instance (or auto-assign) |

Example request payload:

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

### 3. Submit the creation request (Platform Admin)

Click **Submit** to create the Foundry. The platform returns a Foundry ID and begins automated provisioning.

```
POST /api/v1/foundries
Response: { foundry_id: "fnd-abc123", status: "provisioning" }
```

### 4. Wait for automated provisioning (Platform)

The platform automatically provisions the following resources:

| Resource | What happens |
|----------|--------------|
| **Database** | Logical PostgreSQL database `foundry_{slug}` created with schema migrations |
| **Storage** | Object storage prefix `s3://foundry-platform-data/{foundry_id}/` with IAM policy |
| **Identity** | Foundry registered as OAuth client in Olympus Cipher |
| **Repository** | Workshop Definition Repository created via GitHub App |
| **Record** | Foundry record created in platform database with status `created` |

Provisioning typically completes in 1–2 minutes.

**Workshop Definition Repository initial structure:**

```
{slug}-workshop-definition/
├── README.md
├── foundry.yaml          # Foundry-level configuration
├── workshops/            # Workshop definitions (empty)
└── workbenches/          # Workbench definitions (empty)
```

### 5. Receive and click the invitation link (Foundry Admin)

The Platform sends an invitation email to the designated Foundry Admin:

```
Subject: You've been invited to administer {Foundry name} on Foundry Platform

{Admin name},

You have been designated as the Foundry Administrator for {Foundry name}.

Click below to complete your setup:
https://{slug}.foundry.example.com/onboarding?token={token}

This link expires in 7 days.

— Foundry Platform
```

Click the link to proceed to the onboarding wizard.

### 6. Authenticate with Olympus Cipher (Foundry Admin)

Sign in to authenticate via Olympus Cipher. If you do not have an account, create one using the email address the invitation was sent to.

### 7. Choose and configure identity federation (Foundry Admin)

Select how your organization's users will authenticate:

| Option | When to choose |
|--------|----------------|
| **OAuth 2.0** | Standard protocol, most common choice |
| **SAML** | When your IdP requires SAML 2.0 |

**For OAuth 2.0, configure:**

```yaml
identity:
  provider: olympus-cipher
  federation_type: oauth2
  federation_config:
    authorization_endpoint: https://cipher.olympus.example.com/oauth/authorize
    token_endpoint: https://cipher.olympus.example.com/oauth/token
    userinfo_endpoint: https://cipher.olympus.example.com/oauth/userinfo
    client_id: foundry-{foundry_id}
    scopes: ["openid", "profile", "email", "groups"]
```

**For SAML, configure:**

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
    sp_entity_id: https://{slug}.foundry.example.com/saml
```

### 8. Test the federation connection (Foundry Admin)

Click **Test Connection** to verify:

- Connection to Olympus Cipher established
- User attributes received correctly
- Groups retrieved successfully

Resolve any errors before proceeding.

### 9. Configure GitHub integration (Foundry Admin)

Click **Install Foundry GitHub App** to connect your GitHub organization. This redirects to GitHub for authorization.

After installation, the configuration is stored:

```yaml
integrations:
  github:
    app_id: 12345
    app_installation_id: 67890
    organization: {your-org}
```

### 10. Configure Jira integration (Foundry Admin, optional)

Enter your Jira instance URL and click **Connect to Jira** to establish the OAuth connection.

| Field | Value |
|-------|-------|
| Instance URL | `https://{your-org}.atlassian.net` |

Skip this step if you plan to configure Jira later at the Workshop level.

### 11. Configure notifications (Foundry Admin, optional)

Enter your MS Teams webhook URL and click **Test Notification** to verify delivery.

| Setting | Value |
|---------|-------|
| MS Teams Webhook URL | `https://outlook.office.com/webhook/...` |

Skip this step to configure notifications later.

### 12. Review and complete setup (Foundry Admin)

Review your configuration summary:

| Setting | Status |
|---------|--------|
| Foundry | {Foundry name} |
| Identity | {federation type} with Olympus Cipher |
| GitHub | Connected to {org} |
| Jira | {Connected / Not configured} |
| Notifications | {MS Teams configured / Not configured} |

Click **Complete Setup** to finalize onboarding.

### 13. Access the Foundry Admin Console (Foundry Admin)

After completion, you are redirected to the Admin Console with suggested next steps:

- Create your first Workshop
- Invite team members
- Configure Capable Agents
- Complete remaining integrations

### 14. Verify completion notification (Platform Admin)

The Platform Admin receives a notification confirming onboarding completion:

```
Subject: Foundry onboarding completed: {Foundry name}

The Foundry "{Foundry name}" has completed onboarding.

Admin: {admin_email}
Status: Active
Completed: {timestamp}
```

---

## Expected outcome

After completing all steps:

- Foundry status is **Active**
- Foundry Admin can access the Admin Console at `https://{slug}.foundry.example.com`
- Identity federation is functional (users can authenticate)
- GitHub integration is connected (repositories can be created)
- Foundry is ready for Workshop and Workbench provisioning

---

## Summary

| Phase | Location | Actor | Key Output |
|-------|----------|-------|------------|
| Creation | Platform Admin App | Platform Admin | Foundry creation request |
| Provisioning | Platform Backend | Automated | Database, storage, repo, identity |
| Invitation | Email | Foundry Admin | Admin authenticated |
| Federation | Onboarding Wizard | Foundry Admin | Identity federation configured |
| Configuration | Onboarding Wizard | Foundry Admin | Integrations configured |
| Active | Foundry Web App | Foundry Admin | Foundry operational |

## Timing

| Phase | Typical Duration |
|-------|------------------|
| Provisioning | 1–2 minutes |
| Admin invitation acceptance | 1–7 days (depends on admin) |
| Federation setup | 10–30 minutes |
| Initial configuration | 15–60 minutes |

---

## Related

### Concepts

- [Containment Hierarchy](../../concepts/containment-hierarchy.md) — Foundry as the top-level container
- [Repositories](../../concepts/repositories.md) — The 15 canonical repository types provisioned
- [Metadata Service](../../concepts/metadata-service.md) — Central configuration store
- [Declarative Provisioning](../concepts/declarative-provisioning.md) — Admins describe desired state (module-specific)

### Guides

- [Management README](README.md) — Foundry Management overview
- [Foundry settings](foundry-settings.md) — Complete settings specification
- [Platform Admin Web App](../../foundry-platform-admin-web-app/README.md) — Platform Admin interface
- [Workshop provisioning](workshop-provisioning.md) — Creating Workshops after onboarding
- [Foundry lifecycle spec](../platform-developer-guide/foundry-management/README.md) — Foundry lifecycle implementation details

---

## Troubleshooting

| Symptom | Likely cause | What to do |
|---------|--------------|------------|
| Provisioning failed notification | Database or storage provisioning error | Platform Admin reviews error logs; retry or escalate to infrastructure team |
| Invitation link expired | More than 7 days since Foundry creation | Platform Admin resends invitation from Platform Admin Web App |
| Federation test fails | Incorrect IdP configuration | Verify endpoint URLs and certificates; check IdP logs for errors |
| GitHub App installation fails | Insufficient org permissions | Ensure you have owner access to the GitHub org; retry installation |
| "User not found" after federation | User provisioning not configured | Check `identity.user_provisioning` setting; verify JIT or SCIM is enabled |
| Cannot create Workshop after onboarding | Foundry status not Active | Verify onboarding completed; check status in Platform Admin Web App |
