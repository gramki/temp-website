# Publishing Services

> **Status:** 🟡 WIP — Design Complete

This document describes publisher registration, the publishing workflow, validation processes, security scanning, and quarantine procedures.

---

## Overview

Publishing Services handles the complete lifecycle of getting packages into the Marketplace, from publisher registration through security clearance.

| Aspect | Description |
|--------|-------------|
| **Publisher Registration** | Hub Win team approval required |
| **Publishing Workflow** | Developer → Admin → Marketplace |
| **Validation** | Completeness, signing, format checks |
| **Security** | Scanning, quarantine, continuous monitoring |

---

## Publisher Registration

Before publishing packages, a tenant must register as a publisher.

### Registration Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       PUBLISHER REGISTRATION                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. TENANT ADMIN INITIATES                                                 │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  • Submits registration request                                    │    │
│   │  • Provides publisher name and contact information                 │    │
│   │  • Submits signing certificate                                     │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   2. HUB WIN TEAM REVIEWS                                                   │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  • Reviews business legitimacy                                     │    │
│   │  • Validates signing certificate                                   │    │
│   │  • Checks compliance requirements                                  │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   3. APPROVAL/REJECTION                                                     │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  If Approved:                                                      │    │
│   │  • Publisher status activated                                      │    │
│   │  • Signing certificate stored                                      │    │
│   │  • Publisher can now publish packages                              │    │
│   │                                                                    │    │
│   │  If Rejected:                                                      │    │
│   │  • Tenant notified with reason                                     │    │
│   │  • Can reapply with corrections                                    │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Registration Requirements

| Requirement | Description |
|-------------|-------------|
| **Initiator** | Tenant Admin |
| **Approver** | Hub Win (Customer Success) team |
| **Certificate** | Valid signing certificate required |
| **Information** | Publisher name, contact, business details |

---

## Publishing Workflow

### Step 1: Create Package Manifest CRD

Developer creates a Package Manifest CRD in their workbench:

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: PackageManifest
metadata:
  name: dispute-ops-package
spec:
  packageName: "Dispute Operations Suite"
  version: "1.2.0"
  shortDescription: "Complete dispute resolution automation"
  blueprints:
    scenarios:
      - name: dispute-triage
      - name: dispute-resolution
  visibility:
    mode: "public"
  categories:
    - "dispute-resolution"
```

### Step 2: Publish via Automation Developer Desk

1. Developer opens Marketplace Console → Publishing section
2. Selects Package Manifest CRD to publish
3. Tool packages artifacts:
   - Extracts referenced specifications
   - Automatically includes associated children
   - Creates package-manifest-container
   - Prepares container images for signing
4. Admin notified for approval

### Step 3: Admin Approval

1. Tenant Admin reviews package contents
2. Reviews visibility settings
3. If approved:
   - Signs containers with publisher certificate
   - Submits package to Marketplace
4. If rejected:
   - Developer notified with reason

### Step 4: Marketplace Validation

| Check | Description |
|-------|-------------|
| **Publisher Authorization** | Is publisher registered and active? |
| **Signature Verification** | Valid signature from registered certificate? |
| **Container Integrity** | Hash verification for all containers |
| **Package Completeness** | All referenced artifacts included? |
| **Manifest Validity** | All required fields present and valid? |
| **Visibility Rules** | Tenant/region lists valid? |
| **Credential Check** | No credentials included in package? |

### Step 5: Security Scanning

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         SECURITY SCANNING                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   QUARANTINE                                                                │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Package artifacts held in quarantine location                     │    │
│   │  • Not visible in catalog                                          │    │
│   │  • Not available for subscription                                  │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   SCANNING                                                                  │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  • Malware scanning                                                │    │
│   │  • Vulnerability scanning                                          │    │
│   │  • Dependency analysis                                             │    │
│   │  • License compliance (if configured)                              │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   OUTCOME                                                                   │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Pass:                                                             │    │
│   │  • Package released from quarantine                                │    │
│   │  • Marketplace signs containers                                    │    │
│   │  • Package indexed in catalog                                      │    │
│   │                                                                    │    │
│   │  Fail:                                                             │    │
│   │  • Publisher notified with issues                                  │    │
│   │  • Package remains in quarantine                                   │    │
│   │  • Can be corrected and resubmitted                                │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Step 6: Catalog Indexing

After security clearance:
1. Manifest extracted from package-manifest-container
2. Manifest indexed in OpenSearch
3. Package becomes discoverable (subject to visibility)
4. Publisher notified of successful publication

---

## Validation Rules

### Package Manifest Validation

| Field | Validation |
|-------|------------|
| `package_id` | Unique across all packages |
| `package_name` | 3-100 characters, alphanumeric + hyphens |
| `version` | Valid semver format |
| `short_description` | 10-200 characters |
| `artifact_types` | At least one valid type |
| `visibility_mode` | Valid enum (public/restricted/private) |
| `tenant_allow_list` | Required if restricted/private |
| `blueprints` | Non-empty array |

### Content Validation

| Check | Criteria |
|-------|----------|
| **Blueprint References** | All referenced blueprints exist |
| **Associated Children** | Automatically included |
| **Platform References** | Referenced platform resources exist |
| **No External Dependencies** | No references to other packages |
| **No Credentials** | No secrets/credentials in package |

---

## Version Management for Publishing

### New Version Publishing

- Same workflow as initial publishing
- Version must be higher (semver)
- Minor versions must be backward compatible

### Package States

| State | Description |
|-------|-------------|
| **Published** | Active and available |
| **Deprecated** | Visible but not recommended; replacement may exist |
| **Withdrawn** | Removed from discovery; existing subscriptions continue |

### Deprecation

```yaml
# Publisher can mark a package deprecated
deprecation:
  deprecated_date: "2026-03-01"
  reason: "Superseded by v2.0.0"
  replacement_package_id: "dispute-ops-v2.0.0"
```

### Withdrawal

- Publisher or Hub Win can withdraw packages
- Withdrawn packages hidden from search
- Existing subscriptions continue to work
- Derived resources marked as "orphaned"

---

## Continuous Monitoring

After publication, packages are continuously monitored:

| Activity | Frequency |
|----------|-----------|
| **Vulnerability Scanning** | Periodic (configurable) |
| **Malware Scanning** | Periodic |
| **Issue Notification** | On detection |
| **Blacklisting** | Immediate if critical |

---

## Related Documentation

- [Blueprints and Packages](./blueprints-and-packages.md) — Package model
- [Security and Compliance](./security-and-compliance.md) — Security details
- [Catalog Services](./catalog-services.md) — Discovery and indexing
- [ADR-0099: Publisher Registration Approval](../../decision-logs/0099-publisher-registration-approval.md)

