# Guide: Publisher Registration

> **Status:** 🟡 Draft
> **Audience:** Tenant Admin
> **Last Updated:** 2026-01-11

This guide explains how to register as a Marketplace publisher so your organization can publish packages for other Hub subscribers.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Step 1: Prepare Signing Certificate](#step-1-prepare-signing-certificate)
4. [Step 2: Initiate Registration](#step-2-initiate-registration)
5. [Step 3: Submit Registration Request](#step-3-submit-registration-request)
6. [Step 4: Await Approval](#step-4-await-approval)
7. [Step 5: Verify Registration](#step-5-verify-registration)
8. [Troubleshooting](#troubleshooting)
9. [Related Documentation](#related-documentation)

---

## Overview

Publishing packages to the Marketplace requires **publisher registration**, which establishes trust between your organization and the Marketplace. The registration process is:

1. Tenant Admin initiates registration
2. Signing certificate submitted
3. Hub Win (Customer Success) team reviews
4. Upon approval, publisher status is activated

---

## Prerequisites

| Requirement | Description |
|-------------|-------------|
| **Role** | Tenant Admin |
| **Subscription** | Active Hub subscription |
| **Signing Certificate** | Valid X.509 certificate for container signing |
| **Business Information** | Publisher name, contact details |

---

## Step 1: Prepare Signing Certificate

Before registering, you need a valid signing certificate.

### Certificate Requirements

| Attribute | Requirement |
|-----------|-------------|
| **Type** | X.509 |
| **Key Length** | RSA 2048-bit minimum |
| **Validity** | At least 1 year remaining |
| **Usage** | Code/Container signing |

### Obtaining a Certificate

Options:
1. **Enterprise CA** — Use your organization's certificate authority
2. **Public CA** — Obtain from DigiCert, GlobalSign, etc.
3. **Hub-provided** — Contact Hub Win team for guidance

---

## Step 2: Initiate Registration

### Via Hub Control Center

1. Navigate to **Hub Control Center**
2. Go to **Marketplace** → **Publisher Management**
3. Click **Register as Publisher**

### Via CLI

```bash
hub marketplace publisher register --init
```

---

## Step 3: Submit Registration Request

### Required Information

| Field | Description |
|-------|-------------|
| **Publisher Name** | Organization name (as shown to subscribers) |
| **Contact Email** | Primary contact for Marketplace communications |
| **Business Description** | Brief description of your organization |
| **Website** | Organization website (optional) |
| **Signing Certificate** | Upload your X.509 certificate |

### Upload Certificate

```bash
# Via CLI
hub marketplace publisher register \
  --name "ACME Bank" \
  --email "marketplace@acme.bank" \
  --certificate ./signing-cert.pem
```

### Confirmation

Upon submission, you'll receive:
- Confirmation email
- Registration request ID
- Expected review timeline (typically 2-5 business days)

---

## Step 4: Await Approval

### Review Process

The Hub Win team reviews:

| Aspect | What's Checked |
|--------|----------------|
| **Business Legitimacy** | Valid organization |
| **Certificate Validity** | Certificate is valid and not compromised |
| **Compliance** | Meets Marketplace policies |

### Status Tracking

Track your registration status:

```bash
hub marketplace publisher status
```

Or via Hub Control Center → Marketplace → Publisher Management

---

## Step 5: Verify Registration

Upon approval:

1. **Notification** — Email confirmation sent
2. **Status** — Publisher status changes to "Active"
3. **Capabilities** — Publishing features enabled

### Verify

```bash
hub marketplace publisher status
# Output: Publisher Status: Active
```

---

## Troubleshooting

### Registration Rejected

| Reason | Resolution |
|--------|------------|
| **Invalid Certificate** | Obtain a valid signing certificate |
| **Incomplete Information** | Provide all required fields |
| **Business Verification Failed** | Contact Hub Win team |

### Certificate Issues

```bash
# Verify certificate is valid
openssl x509 -in signing-cert.pem -text -noout

# Check expiration
openssl x509 -in signing-cert.pem -checkend 31536000
```

### Re-applying

If rejected, you can reapply after addressing the issues:

```bash
hub marketplace publisher register --reapply
```

---

## Related Documentation

- [Publishing Scenario Blueprints](./publishing-scenario-blueprints.md) — Publish scenarios
- [Publishing Workbench Blueprints](./publishing-workbench-blueprints.md) — Publish workbenches
- [Package Manifest Reference](./package-manifest-reference.md) — Manifest documentation
- [Marketplace Publishing Services](../04-subsystems/marketplace/publishing-services.md) — System documentation

