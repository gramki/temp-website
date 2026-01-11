# Guide: Publishing Scenario Blueprints

> **Status:** 🟡 Draft
> **Audience:** Developer, Tenant Admin
> **Last Updated:** 2026-01-11

This guide walks through publishing Scenario Blueprints to the Marketplace, from creating a Package Manifest to catalog availability.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Step 1: Prepare Your Scenario](#step-1-prepare-your-scenario)
4. [Step 2: Create Package Manifest CRD](#step-2-create-package-manifest-crd)
5. [Step 3: Configure Package Contents](#step-3-configure-package-contents)
6. [Step 4: Add Visibility Controls](#step-4-add-visibility-controls)
7. [Step 5: Publish via Automation Developer Desk](#step-5-publish-via-automation-developer-desk)
8. [Step 6: Admin Approval](#step-6-admin-approval)
9. [Step 7: Security Scanning and Acceptance](#step-7-security-scanning-and-acceptance)
10. [Troubleshooting](#troubleshooting)
11. [Related Documentation](#related-documentation)

---

## Overview

Publishing a Scenario Blueprint makes your scenario available for other Hub subscribers to discover and deploy. The publishing process:

1. Creates a Package Manifest defining what's included
2. Packages all artifacts (automatically includes associated children)
3. Signs containers with your publisher certificate
4. Submits to Marketplace for security scanning
5. Upon clearance, package appears in catalog

---

## Prerequisites

| Requirement | Description |
|-------------|-------------|
| **Publisher Registration** | Tenant must be a registered publisher |
| **Scenario** | Complete, tested scenario in your workbench |
| **Role** | Developer (for creation) + Tenant Admin (for approval) |

---

## Step 1: Prepare Your Scenario

Before publishing, ensure your scenario is complete:

| Checklist | Description |
|-----------|-------------|
| ✅ **Scenario Normative Spec** | Goals, roles, SOPs defined |
| ✅ **Scenario Automation Spec** | Hub Application, triggers configured |
| ✅ **Testing Complete** | All tests passing |
| ✅ **No Credentials** | Ensure no secrets are included |
| ✅ **Documentation** | README and usage instructions ready |

---

## Step 2: Create Package Manifest CRD

### Via CLI

```bash
hub create package-manifest dispute-ops-package
```

### Via Automation Developer Desk

1. Open **Marketplace Console** → **Package Creation**
2. Click **Create New Package Manifest**
3. Enter package name

### Initial Structure

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: PackageManifest
metadata:
  name: dispute-ops-package
  namespace: acme-dev

spec:
  packageName: ""
  version: ""
  shortDescription: ""
  blueprints:
    scenarios: []
```

---

## Step 3: Configure Package Contents

Edit the Package Manifest with your scenario details:

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: PackageManifest
metadata:
  name: dispute-ops-package
  namespace: acme-dev

spec:
  # Package Identity
  packageName: "Dispute Operations Suite"
  version: "1.0.0"
  
  # Descriptions
  shortDescription: "Complete dispute resolution automation with AI-powered triage"
  longDescription: |
    This package includes two complete scenarios for dispute resolution:
    - Dispute Triage: AI-powered initial assessment and categorization
    - Dispute Resolution: End-to-end resolution workflow with escalation
    
    Includes trained agents, SOPs, and tool integrations.
  
  # Package Contents
  blueprints:
    scenarios:
      - name: dispute-triage
      - name: dispute-resolution
    tools:
      - name: card-network-lookup
  
  # Categorization
  categories:
    - "dispute-resolution"
    - "customer-service"
  industryTags:
    - "financial-services"
  keywords:
    - "disputes"
    - "chargebacks"
    - "card-not-present"
```

### Associated Children

When you reference a scenario, these are **automatically included**:

| Artifact Type | Included Automatically |
|---------------|----------------------|
| Hub Application | ✅ |
| Triggers | ✅ |
| Notification Templates | ✅ |
| Task Queue Configs | ✅ |
| Tool Bindings | ✅ |
| Migration CRDs | ✅ |

You don't need to list these explicitly.

---

## Step 4: Add Visibility Controls

Configure who can see your package:

### Public Package

```yaml
spec:
  visibility:
    mode: "public"
```

### Restricted (Specific Tenants)

```yaml
spec:
  visibility:
    mode: "restricted"
    tenantAllowList:
      - "tenant-partner-bank"
      - "tenant-subsidiary-corp"
```

### Region Restrictions

```yaml
spec:
  visibility:
    mode: "public"
    regionAllowList:
      - "us-east-1"
      - "eu-west-1"
    regionDisallowList:
      - "cn-north-1"
```

---

## Step 5: Publish via Automation Developer Desk

### Validate First

```bash
hub validate package-manifest dispute-ops-package
```

### Initiate Publishing

**Via CLI:**

```bash
hub marketplace publish dispute-ops-package
```

**Via UI:**

1. Open **Marketplace Console** → **Publishing**
2. Select your Package Manifest
3. Click **Publish**

### What Happens

1. Tool packages all referenced artifacts
2. Containers are prepared for signing
3. Admin notification sent
4. Status: **Pending Approval**

---

## Step 6: Admin Approval

Tenant Admin must approve before submission to Marketplace.

### Admin Actions

1. Admin receives notification
2. Reviews package contents and visibility
3. Signs containers with publisher certificate
4. Approves submission

### Via Hub Control Center

1. Navigate to **Marketplace** → **Pending Approvals**
2. Review package details
3. Click **Approve and Submit** or **Reject**

---

## Step 7: Security Scanning and Acceptance

After admin approval, Marketplace processes the package:

### Process Flow

```
Package Submitted
       │
       ▼
┌──────────────────┐
│    QUARANTINE    │  Artifacts held for scanning
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│    SCANNING      │  Malware, vulnerabilities, credentials
└────────┬─────────┘
         │
    Pass │ Fail
    ┌────┴────┐
    ▼         ▼
Published   Rejected
```

### Timeline

- Scanning typically completes in **1-4 hours**
- Complex packages may take longer

### Check Status

```bash
hub marketplace packages get dispute-ops-v1.0.0
```

### Upon Success

1. Package released from quarantine
2. Marketplace signs containers
3. Manifest indexed in catalog
4. Package discoverable by subscribers
5. Publisher notified

---

## Troubleshooting

### Validation Errors

| Error | Resolution |
|-------|------------|
| `missing required field` | Add missing field to manifest |
| `scenario not found` | Verify scenario exists in workbench |
| `credentials detected` | Remove secrets from package contents |

### Scanning Failures

| Issue | Resolution |
|-------|------------|
| **Vulnerability found** | Update dependencies, repackage |
| **Malware detected** | Review container contents |
| **Credential detected** | Remove secrets, use placeholder |

### Publishing Rejected

Check rejection reason:

```bash
hub marketplace packages get dispute-ops-v1.0.0 --show-status
```

Common reasons:
- Security scan failure
- Invalid signing certificate
- Missing required metadata

---

## Related Documentation

- [Publisher Registration](./marketplace-publisher-registration.md) — Register as publisher
- [Publishing Workbench Blueprints](./publishing-workbench-blueprints.md) — Publish workbenches
- [Package Manifest Reference](./package-manifest-reference.md) — Complete field reference
- [Marketplace Console](../06-ux-architecture/tenant-domain/marketplace-console.md) — UI documentation

