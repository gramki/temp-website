# Subscription Configuration Guide

> **Audience:** Administrators  
> **Prerequisites:** Subscription created by Customer Success Executive

This guide walks through the complete setup of a new tenant subscription in Olympus Hub.

---

## Overview

Setting up a tenant subscription involves:

1. [Initial Access](#1-initial-access)
2. [User Provisioning](#2-user-provisioning)
3. [Identity Domain Configuration](#3-identity-domain-configuration)
4. [Resource Allocation](#4-resource-allocation)
5. [I/O Gateway Configuration](#5-io-gateway-configuration)
6. [Notification Services](#6-notification-services)
7. [Budgets and Quotas](#7-budgets-and-quotas)
8. [Branding (Optional)](#8-branding-optional)

---

## 1. Initial Access

### What You Receive

When your subscription is created, you'll receive:

| Item | Description |
|------|-------------|
| **Tenant ID** | Unique identifier for your subscription |
| **Admin Credentials** | Initial administrator login |
| **Hub Console URL** | Access point for Hub management |
| **Cipher IAM URL** | Identity management console |

### First Login

1. Access the Hub Console using provided URL
2. Authenticate with initial admin credentials
3. Complete MFA setup (mandatory)
4. Change initial password

---

## 2. User Provisioning

### User Personas to Provision

| Persona | Responsibilities | When to Create |
|---------|------------------|----------------|
| **Administrator** | Manage subscription, users, resources | Immediately |
| **Process Architect** | Define Workbenches, Scenarios | Before workbench setup |
| **Developer** | Build and deploy Hub Applications | Before development |
| **Auditor** | Review compliance | As needed |
| **Agent** | Execute tasks | Before operations |
| **Supervisor** | Manage queues and agents | Before operations |

### Provisioning Steps

#### Create Additional Administrators

```
Hub Console → Administration → Users → Create User
├── Role: Administrator
├── Domain: [Your tenant domain]
├── MFA: Required
└── Permissions: Full subscription access
```

#### Create Process Architects

```
Hub Console → Administration → Users → Create User
├── Role: Process Architect
├── Domain: [Your tenant domain]
├── Permissions: Workbench design, Knowledge management
└── Workbench Access: All or specific workbenches
```

#### Create Developers

```
Hub Console → Administration → Users → Create User
├── Role: Developer
├── Domain: [Your tenant domain]
├── Permissions: Application development, Tool enrollment
└── Environment Access: Development, Staging, Production
```

#### Create Auditors

```
Hub Console → Administration → Users → Create User
├── Role: Auditor
├── Domain: [Your tenant domain]
├── Permissions: Read-only across all workbenches
└── Audit Access: Full audit log access
```

> **Note:** Agents and Supervisors are typically created as part of Workbench setup.

---

## 3. Identity Domain Configuration

### Domain Options

| Option | Description | When to Use |
|--------|-------------|-------------|
| **Single Domain** | All tenant users in one domain | Small organizations |
| **Multiple Domains** | Separate domains per user group | Large organizations |
| **Federated** | Connect to existing IdP (SAML/OIDC) | Enterprise with existing IAM |

### Configure Federation (if applicable)

```
Cipher IAM Console → Domains → [Your Domain] → Federation
├── Protocol: SAML 2.0 or OIDC
├── IdP Metadata: [Upload/URL]
├── Attribute Mapping:
│   ├── Email → email
│   ├── Name → displayName
│   └── Groups → groups
└── Test Connection
```

### Configure Groups

Create groups that align with your organizational structure:

```
Cipher IAM Console → Groups → Create Group
├── Dispute Operations Agents
├── Dispute Operations Supervisors
├── Payment Operations Agents
├── Payment Operations Supervisors
└── [Domain-specific groups]
```

---

## 4. Resource Allocation

### Data Stores

Provision Ganymede instances for your subscription:

```
Hub Console → Resources → Data Stores → Provision
├── Name: [e.g., "tenant-operations-db"]
├── Type: Ganymede (PostgreSQL)
├── Size: [Based on subscription tier]
├── Backup: Enabled
└── Region: [Your primary region]
```

### Memory Stores

Configure memory services:

```
Hub Console → Resources → Memory Stores → Configure
├── Enterprise Memory:
│   ├── Enabled: Yes
│   ├── Retention: [Policy]
│   └── Visibility: [Cross-workbench rules]
├── User Memory:
│   ├── Enabled: Yes
│   └── Retention: [Policy]
└── Agent Memory: [Per-workbench]
```

### Knowledge Stores

Set up Knowledge Bank:

```
Hub Console → Resources → Knowledge Bank → Create Store
├── Name: [e.g., "corporate-policies"]
├── Type: Tenant Knowledge Base
├── Ingestion Sources: [Configure later per workbench]
└── Access: [Workbenches that can access]
```

### Machines (External Integrations)

Register external systems:

```
Hub Console → Resources → Machines → Register
├── Name: [e.g., "core-banking-system"]
├── Type: [REST API / SOAP / Database / etc.]
├── Connection:
│   ├── Endpoint: [URL]
│   ├── Authentication: [OAuth2 / API Key / mTLS]
│   └── Credentials: [Stored securely]
└── Permissions: [Which workbenches can access]
```

---

## 5. I/O Gateway Configuration

### Atropos (Event Bus)

Configure event sources:

```
Hub Console → I/O Gateways → Atropos → Configure
├── Topics:
│   ├── payment.events → [Subscribe]
│   ├── customer.events → [Subscribe]
│   └── [domain].events → [Subscribe]
├── Consumer Groups: [Per workbench]
└── Dead Letter Handling: [Configure]
```

### Heracles (API Gateway)

Configure API endpoints:

```
Hub Console → I/O Gateways → Heracles → Configure
├── Base Path: /api/v1/[tenant]
├── Authentication: Cipher OAuth2
├── Rate Limits: [Per subscription tier]
└── CORS: [Configure if needed]
```

### Dia (File Gateway)

Configure file ingestion:

```
Hub Console → I/O Gateways → Dia → Configure
├── SFTP Endpoint: [Configure]
├── File Patterns: [*.csv, *.xlsx, etc.]
├── Processing Schedule: [Polling interval]
└── Error Handling: [Quarantine rules]
```

### Kale (Scheduler)

Configure scheduled signals:

```
Hub Console → I/O Gateways → Kale → Configure
├── Timezone: [Your timezone]
├── Schedules: [Defined per workbench]
└── Monitoring: [Configure alerts]
```

---

## 6. Notification Services

Configure outbound notification channels:

### Email

```
Hub Console → Notifications → Email → Configure
├── Provider: [SMTP / SendGrid / SES]
├── From Address: [no-reply@yourcompany.com]
├── Templates: [Configure per notification type]
└── Rate Limits: [Per hour/day]
```

### SMS (Optional)

```
Hub Console → Notifications → SMS → Configure
├── Provider: [Twilio / SNS]
├── Sender ID: [Your sender]
└── Rate Limits: [Per hour/day]
```

### Push Notifications (Optional)

```
Hub Console → Notifications → Push → Configure
├── Provider: [FCM / APNS]
├── Credentials: [Configure]
└── Topics: [Define notification channels]
```

### Webhooks

```
Hub Console → Notifications → Webhooks → Configure
├── Endpoints: [Registered webhook URLs]
├── Authentication: [HMAC / OAuth2]
├── Retry Policy: [Configure]
└── Event Types: [Subscribe to specific events]
```

---

## 7. Budgets and Quotas

### Set Resource Quotas

```
Hub Console → Administration → Quotas → Configure
├── Workbenches: [Max number]
├── Scenarios per Workbench: [Max]
├── Requests per Month: [Max]
├── Storage: [GB limit]
├── Compute: [CPU/Memory limits]
└── API Calls: [Per minute/hour/day]
```

### Configure Alerts

```
Hub Console → Administration → Alerts → Create
├── Type: Quota threshold
├── Threshold: [70%, 90%, 100%]
├── Recipients: [Administrators]
└── Channels: [Email, Slack, etc.]
```

### Usage Dashboard

Access usage metrics:

```
Hub Console → Administration → Usage
├── Current Period Usage
├── Trend Analysis
├── Cost Attribution
└── Forecast
```

---

## 8. Branding (Optional)

### Configure Theme

```
Hub Console → Administration → Branding → Theme
├── Primary Color: [Hex code]
├── Secondary Color: [Hex code]
├── Logo: [Upload]
├── Favicon: [Upload]
└── Font: [Select or upload]
```

### White-Labeling (Enterprise)

```
Hub Console → Administration → Branding → White Label
├── Custom Domain: [ops.yourcompany.com]
├── SSL Certificate: [Upload or managed]
├── Login Page: [Customize]
└── Email Templates: [Customize]
```

---

## Setup Checklist

Use this checklist to track your progress:

```
□ Initial Access
  □ First login completed
  □ MFA configured
  □ Password changed

□ Users
  □ Additional Administrators created
  □ Process Architects created
  □ Developers created
  □ Auditors created (if needed)

□ Identity
  □ Domain configuration complete
  □ Federation configured (if applicable)
  □ Groups created

□ Resources
  □ Data stores provisioned
  □ Memory stores configured
  □ Knowledge stores created
  □ Machines registered

□ I/O Gateways
  □ Atropos configured (events)
  □ Heracles configured (APIs)
  □ Dia configured (files) - if needed
  □ Kale configured (schedules) - if needed

□ Notifications
  □ Email configured
  □ SMS configured (if needed)
  □ Push configured (if needed)
  □ Webhooks configured (if needed)

□ Governance
  □ Quotas set
  □ Alerts configured
  □ Usage dashboard reviewed

□ Branding (Optional)
  □ Theme configured
  □ White-labeling (if applicable)
```

---

## Next Steps

After completing tenant setup:

1. **Hand off to Process Architects** — They will create Workbenches
2. **Review [Workbench Setup Guide](./workbench-setup-guide.md)** — Understand the next phase
3. **Schedule Developer Onboarding** — Prepare for application development

---

## Troubleshooting

### Common Issues

| Issue | Resolution |
|-------|------------|
| Cannot access Hub Console | Verify subscription is active, check Cipher IAM credentials |
| Federation not working | Validate IdP metadata, check attribute mappings |
| Resource provisioning fails | Check quota limits, contact support |
| I/O Gateway connection errors | Verify network access, check credentials |

### Getting Help

- **Technical Support:** Contact Zeta support portal
- **Account Issues:** Contact your Customer Success Executive
- **Documentation:** Refer to [Subscription Management](../04-subsystems/subscription-management/README.md)

---

## Related Documentation

- [Subscription Management](../04-subsystems/subscription-management/README.md) — Technical reference
- [User Management](../04-subsystems/user-management/README.md) — Persona details
- [Workbench Setup Guide](./workbench-setup-guide.md) — Next phase

