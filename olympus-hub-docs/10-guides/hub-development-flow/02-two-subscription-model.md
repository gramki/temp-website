# The Two-Subscription Model

[← Previous: Why Different?](./01-why-different-model.md) | [Back to Index](./README.md) | [Next: Workbench-Based Development →](./03-workbench-based-development.md)

---

## Overview

Hub recommends using **two separate subscriptions** to achieve near-physical separation between development and production contexts. This isn't just a recommendation — for regulated industries, it's often a compliance requirement.

---

## Why Two Subscriptions?

### The Security Boundary Problem

In traditional setups, development and production often share:
- The same Git repository
- The same CI/CD pipeline
- The same container registry (with different tags)
- The same access control policies

This creates risk:

| Risk | Description |
|------|-------------|
| **Credential leakage** | Dev credentials that accidentally work in prod |
| **Configuration drift** | Dev settings that leak into prod |
| **Access creep** | Developers with prod access "for debugging" |
| **Audit ambiguity** | Unclear which environment an action targeted |

### The Two-Subscription Solution

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TWO-SUBSCRIPTION MODEL                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DEV SUBSCRIPTION                       PROD SUBSCRIPTION                   │
│   ─────────────────                      ─────────────────                   │
│   Different credentials                  Different credentials               │
│   Different registry                     Different registry                  │
│   Different Git repo                     Different Git repo                  │
│   Different access policies              Different access policies           │
│                                                                              │
│   ┌─────────────────────────┐           ┌─────────────────────────┐         │
│   │                         │           │                         │         │
│   │  DEV Workbench          │           │  PROD Workbench         │         │
│   │  └── Snapshot Registry  │           │  └── Production Registry│         │
│   │                         │           │                         │         │
│   │  STAGING Workbench      │           │                         │         │
│   │  └── Production Registry│           │                         │         │
│   │  (or in PROD sub)       │           │                         │         │
│   │                         │           │                         │         │
│   └─────────────────────────┘           └─────────────────────────┘         │
│                                                                              │
│              │                                     ▲                         │
│              │         PROMOTION                   │                         │
│              └─────────────────────────────────────┘                         │
│              (explicit, approved, artifacts copied)                          │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## What Each Subscription Contains

### DEV Subscription

| Component | Purpose |
|-----------|---------|
| **Snapshot Registry** | Development builds, work-in-progress artifacts |
| **Production Registry** | Also available for STAGING workbenches |
| **Git Repository** | DEV workbench CRDs and configurations |
| **DEV Workbench(es)** | Active development, experimentation |
| **STAGING Workbench** | Pre-production validation (optional, can be in PROD subscription) |

> **Note:** STAGING workbenches use the **production registry** (not snapshot), ensuring what you test in STAGING matches production. STAGING can alternatively be placed in the PROD subscription for stricter separation.

**Who has access:**
- Developers (full access to DEV workbenches)
- CI system (build and push to snapshot registry)
- Admins (oversight)

### PROD Subscription

| Component | Purpose |
|-----------|---------|
| **Production Registry** | Released, approved artifacts only |
| **Git Repository** | PROD workbench CRDs and configurations |
| **PROD Workbench(es)** | Production operations |

**Who has access:**
- Admins (full access)
- Operators (limited access for operations)
- Developers (read-only or no access, depending on policy)

---

## What Happens During Promotion

When you promote a Scenario from DEV to PROD subscription:

```
PROMOTION PROCESS:

1. Developer requests promotion
   └── Specifies: Scenario, version, target

2. Admin reviews and approves
   └── Recorded: who approved, when, why

3. Artifacts are COPIED (not referenced)
   ├── Container images → copied to PROD registry
   └── CRDs → copied to PROD Git repository

4. Deployment in PROD subscription
   └── Using PROD credentials, PROD configurations

Result: Complete isolation maintained
```

### Why Physical Copy?

| Aspect | Benefit |
|--------|---------|
| **Independence** | PROD doesn't depend on DEV subscription availability |
| **Immutability** | Promoted artifacts can't be changed in DEV after promotion |
| **Audit trail** | Clear record of what was promoted when |
| **Credential isolation** | PROD never pulls from DEV registry |

---

## Subscription Setup

### Initial Setup (Done by Admin)

```yaml
# DEV Subscription
apiVersion: hub.olympus.io/v1
kind: Subscription
metadata:
  name: acme-dev
spec:
  tenant: acme-bank
  purpose: development
  
  # Registries provisioned automatically
  # Git repository provisioned automatically
  
---
# PROD Subscription
apiVersion: hub.olympus.io/v1
kind: Subscription
metadata:
  name: acme-prod
spec:
  tenant: acme-bank
  purpose: production
```

### Default Promotion Path (Pre-configured)

When both subscriptions are created, a default promotion path is established:

```yaml
apiVersion: hub.olympus.io/v1
kind: PromotionDestination
metadata:
  name: dev-to-prod
  namespace: acme-dev
spec:
  target:
    type: subscription
    subscription_id: acme-prod
  
  # Default approval settings
  approval:
    required: true
    approver_role: tenant-admin
  
  # Default notifications
  notifications:
    on_request: [requester, admin]
    on_completion: [requester, admin, ops-team]
```

---

## Your Role as a Developer

### What You Have Access To

| Subscription | Your Access |
|--------------|-------------|
| **DEV** | Full access to your assigned workbench(es) |
| **PROD** | Typically none (or read-only for debugging) |

### What You Can Do

| Action | Where | How |
|--------|-------|-----|
| Edit Scenarios | DEV workbench | Direct CRD edits |
| Build applications | DEV subscription | Runtime CI |
| Run tests | DEV workbench | Hub Test Runner |
| Request promotion | DEV → PROD | Promotion request |
| **Deploy to PROD** | PROD subscription | ❌ Cannot — Admin approves |

### What You Cannot Do

| Action | Why |
|--------|-----|
| Push directly to PROD registry | No credentials |
| Edit PROD workbench CRDs | No access |
| Skip promotion approval | Built-in requirement |
| Access PROD secrets | Different subscription |

---

## Alternative: Single Subscription

For less regulated environments, a single subscription with multiple workbenches is possible:

```
SINGLE SUBSCRIPTION (Alternative):

┌─────────────────────────────────────────────────────────────────────────────┐
│   SUBSCRIPTION                                                               │
│   ┌───────────────┐  ┌───────────────┐  ┌───────────────┐                   │
│   │  DEV          │  │  STAGING      │  │  PROD         │                   │
│   │  Workbench    │──│  Workbench    │──│  Workbench    │                   │
│   └───────────────┘  └───────────────┘  └───────────────┘                   │
│                                                                              │
│   Single Registry (with lifecycle stages)                                    │
│   Single Git Repository                                                      │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Trade-offs:**

| Aspect | Single Subscription | Two Subscriptions |
|--------|--------------------|--------------------|
| **Simplicity** | ✅ Easier to manage | More setup |
| **Isolation** | Weaker | ✅ Stronger |
| **Compliance** | May not satisfy | ✅ Meets requirements |
| **Access control** | Shared policies | ✅ Separate policies |

> **Recommendation:** Use two subscriptions unless you have a specific reason not to.

---

## Summary

| Concept | Key Point |
|---------|-----------|
| **Two subscriptions** | DEV and PROD are completely separate |
| **Physical separation** | Different registries, repos, credentials |
| **Promotion copies** | Artifacts are copied, not referenced |
| **Developer access** | DEV only; PROD via promotion approval |
| **Compliance** | This model satisfies regulated industry requirements |

---

[← Previous: Why Different?](./01-why-different-model.md) | [Back to Index](./README.md) | [Next: Workbench-Based Development →](./03-workbench-based-development.md)

