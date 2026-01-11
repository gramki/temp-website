# Security and Compliance

> **Status:** 🟡 WIP — Design Complete

This document describes the security model for Marketplace, including federated IAM, artifact signing, security scanning, blacklisting, and credential policies.

---

## Overview

Marketplace implements a comprehensive security model to ensure trust and integrity across the artifact sharing ecosystem.

| Aspect | Mechanism |
|--------|-----------|
| **Authentication** | Federated IAM |
| **Integrity** | Container signing (Publisher + Marketplace) |
| **Scanning** | Pre-acceptance + continuous |
| **Response** | Blacklisting capability |
| **Credentials** | Never in packages |

---

## Federated IAM

Marketplace uses **federated identity** to authenticate users across tenant boundaries.

### Federation Model

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          FEDERATED IAM                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   TENANT IAM DOMAIN                    MARKETPLACE IAM DOMAIN               │
│   ┌────────────────────┐              ┌────────────────────┐                │
│   │                    │              │                    │                │
│   │   User Identity    │   Federation │  Federated Identity│                │
│   │   (Full Profile)   │ ──────────▶  │  (Minimal PII)     │                │
│   │                    │              │                    │                │
│   │   • Full name      │              │  • Federated ID    │                │
│   │   • Email          │              │  • Tenant ref      │                │
│   │   • Phone          │              │  • Display name    │                │
│   │   • Roles          │              │  • Roles           │                │
│   │                    │              │                    │                │
│   └────────────────────┘              └────────────────────┘                │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Identity Attributes

| Attribute | Source | Purpose |
|-----------|--------|---------|
| Federated ID | Marketplace | Unique identifier in Marketplace |
| Tenant Reference | Tenant IAM | Links to source tenant |
| Display Name | Tenant (desensitized) | UI display only |
| Roles | Both domains | Authorization |

### PII Protection

- **No PII beyond desensitized name** stored in Marketplace
- Email, phone, full name not transferred
- Audit logs use federated ID, not PII
- Protects user privacy across tenant boundaries

### Authentication Flow

1. User accesses Marketplace from tenant desk
2. Tenant IAM issues federated token
3. Marketplace IAM validates token
4. Federated identity created/updated
5. Request attributed to federated identity

---

## Artifact Signing

All containers are signed to ensure integrity and authenticity.

### Signing Chain

```
1. PUBLISHER SIGNS
   ┌────────────────────────────────────────────────────────────────────┐
   │  Publisher signs containers with registered certificate           │
   │  • Certificate submitted during publisher registration            │
   │  • Signing happens during admin approval step                     │
   └────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
2. MARKETPLACE VALIDATES
   ┌────────────────────────────────────────────────────────────────────┐
   │  Marketplace verifies publisher signature                         │
   │  • Checks signature against registered certificate                │
   │  • Verifies container integrity (hash)                            │
   └────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
3. MARKETPLACE RE-SIGNS
   ┌────────────────────────────────────────────────────────────────────┐
   │  Marketplace signs with its private key                           │
   │  • Creates chain of trust                                         │
   │  • Enables subscriber verification                                │
   └────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
4. SUBSCRIBER VERIFIES
   ┌────────────────────────────────────────────────────────────────────┐
   │  Subscriber verifies Marketplace signature                        │
   │  • Uses Marketplace public key                                    │
   │  • Confirms integrity and authenticity                            │
   │  • Happens during container cloning                               │
   └────────────────────────────────────────────────────────────────────┘
```

### Verification Points

| Point | Verification |
|-------|--------------|
| **Publishing** | Publisher signature validated |
| **Catalog Entry** | Marketplace signature added |
| **Container Clone** | Marketplace signature verified |
| **Deployment** | Hash verification |

---

## Security Scanning

All artifacts undergo security scanning before and after publication.

### Pre-Acceptance Scanning

| Scan Type | Purpose |
|-----------|---------|
| **Malware Scan** | Detect known malware |
| **Vulnerability Scan** | Identify security vulnerabilities |
| **Dependency Analysis** | Check for vulnerable dependencies |
| **Credential Detection** | Ensure no secrets included |

### Quarantine Process

```
Package Submitted
       │
       ▼
┌──────────────┐
│  QUARANTINE  │  Artifacts held pending security clearance
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   SCANNING   │  All scans executed
└──────┬───────┘
       │
       ├─── Pass ──▶ Released to Catalog
       │
       └─── Fail ──▶ Publisher notified, remains quarantined
```

### Continuous Monitoring

After publication, packages are continuously monitored:

| Activity | Frequency |
|----------|-----------|
| Vulnerability Scanning | Periodic (configurable) |
| Malware Scanning | Periodic |
| New CVE Matching | On CVE publication |

### Issue Notification

When issues are detected:

1. Publisher notified with issue details
2. Affected subscribers notified
3. Severity-based response:
   - **Critical**: Immediate blacklisting option
   - **High**: Publisher given time to remediate
   - **Medium/Low**: Advisory notification

---

## Blacklisting

Publishers and Hub Win team can blacklist packages to prevent harm.

### Blacklist Actions

| Action | Effect |
|--------|--------|
| **Block New Subscriptions** | Package cannot be newly subscribed |
| **Block Existing Usage** | Existing subscriptions blocked |
| **Hide from Catalog** | Package hidden from search |

### Who Can Blacklist

| Actor | Scope |
|-------|-------|
| **Publisher** | Their own packages |
| **Hub Win Team** | Any package |

### Blacklist Workflow

```
1. Issue Identified (security scan, report, etc.)
2. Blacklist Decision Made
3. Package Marked Blacklisted
4. Subscribers Notified
5. New subscriptions blocked
6. Existing usage optionally blocked
```

---

## Credential Policy

**Packages must NOT contain any credentials.**

### Policy

| Aspect | Requirement |
|--------|-------------|
| **Package Contents** | No secrets, passwords, API keys, tokens |
| **Validation** | Credential detection during security scan |
| **Subscriber Responsibility** | Provide own credentials at deployment |
| **Marketplace Role** | Does not manage or store credentials |

### Credential Detection

During security scanning:
- Pattern matching for common credential formats
- Entropy analysis for secrets
- Known secret patterns (AWS keys, etc.)

### Subscriber Credential Management

- Subscribers provide their own credentials
- Credentials configured at deployment time
- Credentials stored in tenant's secret management
- Marketplace never sees subscriber credentials

---

## Publisher Allow/Disallow Lists

Tenant admins can control trusted publishers.

### Configuration

```yaml
publisherPolicy:
  mode: "allowlist"  # allowlist | denylist | mixed
  
  allow:
    - "publisher-trusted-vendor"
    - "publisher-partner-bank"
  
  deny:
    - "publisher-untrusted"
```

### Enforcement

- Applied at catalog query time
- Denied publishers' packages hidden
- Subscription requests to denied publishers rejected

---

## Audit Trail

All security-relevant events are logged:

| Event Category | Events |
|----------------|--------|
| **Publishing** | Submit, validate, scan results, approval |
| **Subscription** | Request, approval, rejection |
| **Security** | Scan results, blacklisting, notifications |
| **Access** | Federated authentication, API calls |

### Audit Access

| Viewer | Access |
|--------|--------|
| **Publisher** | Their package events |
| **Tenant Admin** | Their tenant's events |
| **Hub Win Team** | All platform events |

---

## Compliance Considerations

### Data Residency

- Visibility controls can restrict by region
- Region allow/disallow lists in package manifest
- Respects data sovereignty requirements

### Intellectual Property

- Packages are immutable and versioned
- Publisher signature establishes ownership
- Audit trail tracks provenance

---

## Related Documentation

- [Publishing Services](./publishing-services.md) — Publishing workflow
- [Subscription Services](./subscription-services.md) — Subscription model
- [ADR-0099: Publisher Registration Approval](../../decision-logs/0099-publisher-registration-approval.md)
- [ADR-0100: Federated IAM for Marketplace](../../decision-logs/0100-federated-iam-marketplace.md)

