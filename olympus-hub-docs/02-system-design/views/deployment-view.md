# Deployment View

> **How the system is deployed and promoted**

---

## Audience

- Platform Engineers
- DevOps Engineers
- Release Managers

---

## Overview

This view shows how Olympus Hub is deployed across environments, how tenants and subscriptions are structured, and how artifacts move from development to production through the promotion model.

---

## Deployment Topology

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         DEPLOYMENT TOPOLOGY                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   PUBLISHER DOMAIN (Hub Platform)                                            │
│   ───────────────────────────────                                            │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │ Hub Cluster (Managed by SRE)                                         │   │
│   │                                                                      │   │
│   │   Platform Services    Automation Runtimes    Data Services          │   │
│   │   ─────────────────    ──────────────────    ─────────────          │   │
│   │   Signal Exchange      Atlantis              Ganymede (shared)       │   │
│   │   I/O Gateways         Rhea                  Europa (shared)         │   │
│   │   Operators            ChronoShift           Cipher IAM              │   │
│   │   Registry Services    Seer                  Knowledge Services      │   │
│   │                        Perseus               Memory Services         │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   TENANT DOMAIN (Per Enterprise)                                             │
│   ──────────────────────────────                                             │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │ Tenant: ACME Bank                                                    │   │
│   │                                                                      │   │
│   │   ┌───────────────────────────┐  ┌───────────────────────────┐      │   │
│   │   │ DEV Subscription          │  │ PROD Subscription         │      │   │
│   │   │                           │  │                           │      │   │
│   │   │ ┌───────────────────────┐ │  │ ┌───────────────────────┐ │      │   │
│   │   │ │ dispute-ops-dev       │ │  │ │ dispute-ops-prod      │ │      │   │
│   │   │ │ (DEV stage)           │ │  │ │ (PROD stage)          │ │      │   │
│   │   │ └───────────────────────┘ │  │ └───────────────────────┘ │      │   │
│   │   │                           │  │                           │      │   │
│   │   │ ┌───────────────────────┐ │  │ ┌───────────────────────┐ │      │   │
│   │   │ │ dispute-ops-staging   │ │  │ │ reconciliation-prod   │ │      │   │
│   │   │ │ (STAGING stage)       │ │  │ │ (PROD stage)          │ │      │   │
│   │   │ └───────────────────────┘ │  │ └───────────────────────┘ │      │   │
│   │   │                           │  │                           │      │   │
│   │   │ Registry: snapshot        │  │ Registry: production      │      │   │
│   │   │ Git: sub-acme-dev         │  │ Git: sub-acme-prod        │      │   │
│   │   └───────────────────────────┘  └───────────────────────────┘      │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Tenant/Subscription/Workbench Hierarchy

```
Tenant (Enterprise Boundary)
    │
    ├── Subscription (DEV)
    │       ├── Workbench (dispute-ops-dev) — DEV stage
    │       ├── Workbench (dispute-ops-staging) — STAGING stage
    │       └── Workbench (reconciliation-dev) — DEV stage
    │
    └── Subscription (PROD)
            ├── Workbench (dispute-ops-prod) — PROD stage
            └── Workbench (reconciliation-prod) — PROD stage
```

---

## Promotion Model

### Promotion Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PROMOTION FLOW                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DEV SUBSCRIPTION                         PROD SUBSCRIPTION                 │
│   ────────────────                         ─────────────────                 │
│                                                                              │
│   dispute-ops-dev                                                            │
│   (DEV stage)                                                                │
│        │                                                                     │
│        │ Promote (within subscription)                                       │
│        ▼                                                                     │
│   dispute-ops-staging                                                        │
│   (STAGING stage)                                                            │
│        │                                                                     │
│        │ Promote (cross-subscription, requires approval)                     │
│        │                                                                     │
│        └─────────────────────────────────────▶ dispute-ops-prod             │
│                                                (PROD stage)                  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### What Gets Promoted

| Artifact | Promotes | Notes |
|----------|----------|-------|
| **Hub Application images** | ✅ | Physical copy to destination registry |
| **Scenario Normative Spec** | ✅ | CRD content |
| **Scenario Automation Spec** | ✅ | CRD content |
| **Scenario Deployment Spec** | ✅ | CRD content |
| **Data migrations** | ✅ | Schema changes |
| **Trigger definitions** | ✅ | CRD content |

### What Does NOT Promote

| Artifact | Promotes | Notes |
|----------|----------|-------|
| **Environment configuration** | ❌ | Secrets, endpoints differ per environment |
| **Secrets** | ❌ | Security isolation |
| **Machine instance bindings** | ❌ | Different endpoints per environment |
| **Runtime data** | ❌ | Requests, tasks stay in source |

---

## Registry Model

### Container Registries (Per Subscription)

| Registry | Purpose | Content |
|----------|---------|---------|
| **Snapshot** | Development images | Unstable, frequent updates |
| **Production** | Promoted images | Stable, versioned, immutable |

### Git Repositories (Per Subscription)

| Content | Branch | Access |
|---------|--------|--------|
| CRD specifications | `main` only | GitOps reconciliation |
| Scenario specs | `main` only | Operator-watched |
| Tool definitions | `main` only | Operator-watched |

---

## Dev-Lifecycle Stages

| Stage | Purpose | Characteristics |
|-------|---------|-----------------|
| **DEV** | Development and experimentation | Unstable, frequent changes |
| **STAGING** | Pre-production validation | Stable, production-like config |
| **PROD** | Live operations | Immutable, monitored, audited |

---

## Promotion Approval

| Promotion Type | Approval Required |
|----------------|-------------------|
| **Within subscription** (DEV → STAGING) | Optional (configurable) |
| **Cross-subscription** (STAGING → PROD) | Required |

---

## Related Documentation

- [Subscription](../implementation-concepts/subscription.md)
- [Dev-Lifecycle-Stage](../implementation-concepts/dev-lifecycle-stage.md)
- [Promotion](../implementation-concepts/promotion.md)
- [Artifact Registry](../implementation-concepts/artifact-registry.md)

