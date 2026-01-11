# Guide: Subscribing to Marketplace Packages

> **Status:** 🟡 Draft
> **Audience:** Developer, Process Architect, Tenant Admin
> **Last Updated:** 2026-01-11

This guide explains how to discover, subscribe to, and manage Marketplace package subscriptions.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Step 1: Browse the Marketplace](#step-1-browse-the-marketplace)
4. [Step 2: Review Package Details](#step-2-review-package-details)
5. [Step 3: Request Subscription](#step-3-request-subscription)
6. [Step 4: Admin Approval](#step-4-admin-approval)
7. [Step 5: Access BlueprintSpecs](#step-5-access-blueprintspecs)
8. [Managing Subscriptions](#managing-subscriptions)
9. [Troubleshooting](#troubleshooting)
10. [Related Documentation](#related-documentation)

---

## Overview

Subscribing to a Marketplace package makes its **BlueprintSpecs** available in your workbench. From these BlueprintSpecs, you can create derived resources (regular specifications) that become part of your workbench.

### Subscription Flow

```
Discover → Subscribe → Admin Approval → BlueprintSpecs Available → Create Derived Resources
```

---

## Prerequisites

| Requirement | Description |
|-------------|-------------|
| **Role** | Developer, Process Architect, or Product Owner |
| **Workbench Access** | Access to target workbench |
| **Admin Available** | Tenant Admin for subscription approval |

---

## Step 1: Browse the Marketplace

### Via Marketplace Console

1. Open any desk with Marketplace access:
   - Agent Developer Desk
   - Scenario Design Desk
   - Automation Product Desk
2. Navigate to **Marketplace Console** → **Discovery**

### Via CLI

```bash
# Search for packages
hub marketplace search "dispute resolution"

# Browse by category
hub marketplace browse --category "customer-service"

# Browse by publisher
hub marketplace browse --publisher "acme-bank"
```

### Search Tips

| Search Type | Example |
|-------------|---------|
| **Keyword** | `hub marketplace search "fraud detection"` |
| **Category** | `hub marketplace browse --category "payments"` |
| **Industry** | `hub marketplace search --industry "financial-services"` |
| **Publisher** | `hub marketplace browse --publisher "partner-corp"` |

---

## Step 2: Review Package Details

Before subscribing, review the package thoroughly.

### Via Marketplace Console

Click on a package to view:
- Package description
- Included BlueprintSpecs
- Publisher information
- Version history
- System requirements
- Prerequisites

### Via CLI

```bash
hub marketplace get dispute-ops-v1.2.0
```

### Key Information to Review

| Aspect | What to Check |
|--------|---------------|
| **Contents** | What scenarios/tools are included? |
| **Prerequisites** | What machines/tools do you need? |
| **Requirements** | Platform/runtime requirements |
| **Version** | Is this the version you need? |
| **Publisher** | Is the publisher trusted? |

---

## Step 3: Request Subscription

### Via Marketplace Console

1. On package detail page, click **Subscribe**
2. Select target workbench
3. Optionally specify version range (e.g., `^1.2.0`)
4. Click **Request Subscription**

### Via CLI

```bash
# Subscribe to specific version
hub marketplace subscribe dispute-ops-v1.2.0 dispute-ops-dev

# Subscribe with version range
hub marketplace subscribe dispute-ops "^1.2.0" dispute-ops-dev
```

### Subscription Request Status

After requesting, status will be **Pending Approval**.

```bash
hub marketplace subscriptions list --status pending
```

---

## Step 4: Admin Approval

Your Tenant Admin must approve the subscription.

### For Admins

1. Open **Hub Control Center** → **Marketplace**
2. Go to **Subscription Approvals**
3. Review the request:
   - Package details
   - Target workbench
   - Requesting user
   - Publisher
4. Click **Approve** or **Reject**

### Publisher Allow/Disallow Lists

If the publisher is on a disallow list, the subscription will be rejected. Contact your Tenant Admin to update publisher policies if needed.

---

## Step 5: Access BlueprintSpecs

Upon approval, BlueprintSpecs become available in your workbench.

### View Available BlueprintSpecs

```bash
# List all BlueprintSpecs
hub get blueprintspecs

# List Scenario BlueprintSpecs
hub get scenarioblueprintspecs

# List Tool BlueprintSpecs
hub get toolblueprintspecs
```

### Via Marketplace Console

Navigate to **Subscriptions** to see subscribed packages and their BlueprintSpecs.

### What's Available

| Resource | Description |
|----------|-------------|
| **BlueprintSpecs** | Visible and usable |
| **Containers** | NOT cloned yet (lazy cloning) |
| **Documentation** | Accessible via package info |

---

## Managing Subscriptions

### View Active Subscriptions

```bash
hub marketplace subscriptions list
```

### Check for Updates

```bash
hub marketplace subscriptions list --show-updates
```

### Update to New Version

```bash
hub marketplace subscriptions update dispute-ops-sub --version 1.3.0
```

### Unsubscribe

```bash
hub marketplace subscriptions unsubscribe dispute-ops-sub
```

**Note:** Unsubscription requires deleting all derived resources first.

---

## Troubleshooting

### Subscription Request Rejected

| Reason | Resolution |
|--------|------------|
| Publisher not allowed | Contact Admin to update publisher policy |
| Package not visible | Check visibility restrictions with publisher |
| Workbench access denied | Request workbench access |

### BlueprintSpecs Not Visible

| Issue | Resolution |
|-------|------------|
| Subscription pending | Wait for admin approval |
| Wrong workbench | Check subscription target workbench |
| Refresh needed | Refresh workbench view |

### Package Not Found

```bash
# Check if package exists and is visible to you
hub marketplace search --exact "package-name"
```

Possible causes:
- Package is private (not on your allow list)
- Package withdrawn
- Regional restrictions

---

## Related Documentation

- [Using BlueprintSpecs](./using-blueprintspecs.md) — Create derived resources
- [Building Scenario from Blueprint](./building-scenario-from-blueprint.md) — Complete workflow
- [Managing Blueprint Updates](./managing-blueprint-updates.md) — Handle version updates
- [Marketplace Console](../06-ux-architecture/tenant-domain/marketplace-console.md) — UI reference

