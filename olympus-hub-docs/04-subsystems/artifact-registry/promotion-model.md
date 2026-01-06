# Promotion Model

## Overview

Promotion is the controlled movement of artifacts from one workbench or subscription to another. Hub provides a structured promotion model with configurable destinations, approval workflows, and atomic promotion units.

---

## Sensible Defaults for Small Teams

Hub is designed for **small teams in regulated enterprises**. The promotion model provides sensible defaults that satisfy compliance requirements with minimal configuration:

### Out-of-the-Box Promotion Path

When using the recommended two-subscription model, a **default promotion path** is pre-configured:

```
DEV Subscription ──────────────────────▶ PROD Subscription
(DEV/STAGING workbenches)                (PROD workbenches)
```

| Default Setting | Value | Rationale |
|-----------------|-------|-----------|
| **Approval Required** | Yes | Compliance requirement |
| **Approver** | Tenant Admin | Single approver for small teams |
| **Notification Recipients** | Requester + Admin | Minimal but sufficient |
| **Artifact Copy** | Physical copy | Subscription isolation |

### Default Developer Permissions

| Workbench Stage | Sync Permission | Promotion Permission |
|-----------------|-----------------|---------------------|
| **DEV** | ✅ Can sync | ✅ Can request promotion |
| **STAGING** | ❌ Admin only | ✅ Can request promotion |
| **PROD** | ❌ Admin only | ❌ Admin only |

> **Note:** All controls are present and auditable. Defaults simply reduce configuration burden for small teams.

---

## Promotion Units

Artifacts can only be promoted at specific granularities:

| Unit | Scope | What's Promoted |
|------|-------|-----------------|
| **Scenario** | Atomic, smallest unit | All artifacts associated with the Scenario |
| **Workbench** | Collection of Scenarios | All Scenarios + workbench-level resources |
| **Subscription** | Largest unit | All Workbenches + subscription-level resources |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PROMOTION UNIT HIERARCHY                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   SUBSCRIPTION                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   WORKBENCH A                        WORKBENCH B                     │   │
│   │   ┌─────────────────────────┐       ┌─────────────────────────┐     │   │
│   │   │                         │       │                         │     │   │
│   │   │  Scenario 1   Scenario 2│       │  Scenario 3             │     │   │
│   │   │  ┌─────────┐ ┌─────────┐│       │  ┌─────────┐            │     │   │
│   │   │  │• App    │ │• App    ││       │  │• App    │            │     │   │
│   │   │  │• Triggers│ │• Triggers││       │  │• Triggers│            │     │   │
│   │   │  │• Specs  │ │• Specs  ││       │  │• Specs  │            │     │   │
│   │   │  └─────────┘ └─────────┘│       │  └─────────┘            │     │   │
│   │   │                         │       │                         │     │   │
│   │   │  Workbench Resources    │       │  Workbench Resources    │     │   │
│   │   └─────────────────────────┘       └─────────────────────────┘     │   │
│   │                                                                      │   │
│   │   Subscription-Level Resources (shared CRDs)                         │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Scenario Promotion

When a Scenario is promoted, all associated artifacts are included:

| Artifact Type | Included |
|---------------|----------|
| Scenario Specification (Normative, Automation, Deployment) | ✅ |
| Hub Application container(s) | ✅ |
| Trigger definitions | ✅ |
| Notification templates | ✅ |
| Task queue configurations | ✅ |
| Tool bindings | ✅ |
| Migration CRDs (for data stores) | ✅ |

> **Note:** Partial Scenario promotion is not supported. Scenarios are atomic.

---

## Promotion Destinations

A **Promotion Destination** is a configured target for artifact promotion.

### Destination Types

| Type | Target | Use Case |
|------|--------|----------|
| **Subscription** | Another subscription (same or different tenant) | Cross-environment, cross-tenant sharing |
| **Workbench** | Specific workbench within a subscription | Direct workbench-to-workbench promotion |

### Destination Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: PromotionDestination
metadata:
  name: production-sub
  namespace: acme-bank
spec:
  display_name: "Production Subscription"
  
  # Target type
  target:
    type: subscription  # subscription | workbench
    subscription_id: acme-bank-prod-001
    # workbench_id: dispute-ops-prod  # If type: workbench
  
  # Credentials for target access
  credentials:
    type: service_account
    secret_ref: prod-promotion-creds
  
  # Approval configuration
  approval:
    required: true
    workflow: two-level-approval
    approvers:
      level_1:
        - role: developer-lead
      level_2:
        - role: tenant-admin
  
  # Notification configuration
  notifications:
    on_request:
      - group: dev-team
      - group: ops-team
    on_approval:
      - group: ops-team
    on_completion:
      - group: all-stakeholders
```

---

## Promotion Paths

A **Promotion Path** is a developer-configured, admin-approved route for frequent promotions from a specific workbench.

```yaml
apiVersion: hub.olympus.io/v1
kind: PromotionPath
metadata:
  name: dev-to-staging
  namespace: acme-bank
spec:
  # Source workbench
  source_workbench: dispute-ops-dev
  
  # Target destination
  destination_ref: staging-workbench
  
  # Approval status
  status: approved  # pending | approved | revoked
  approved_by: admin@acme.com
  approved_at: "2026-01-06T10:00:00Z"
  
  # Path-specific approval workflow (overrides destination default)
  approval_workflow:
    required: true
    auto_approve_for:
      - user: senior-dev@acme.com
    manual_approval:
      - role: developer-lead
```

### Path Lifecycle

```
Developer                    Admin                    Destination
    │                          │                          │
    │  Define Promotion Path   │                          │
    ├─────────────────────────▶│                          │
    │                          │                          │
    │  Path Status: PENDING    │                          │
    │                          │                          │
    │                          │  Review & Approve        │
    │                          ├─────────────────────────▶│
    │                          │                          │
    │  Path Status: APPROVED   │                          │
    │◀─────────────────────────┤                          │
    │                          │                          │
    │  Use Path for Promotions │                          │
    ├──────────────────────────┼─────────────────────────▶│
    │                          │                          │
```

---

## Approval Workflow

### Built-in Approval

Hub provides a built-in approval workflow engine:

| Feature | Support |
|---------|---------|
| Multi-level approval | ✅ Up to N levels |
| Role-based approvers | ✅ IAM roles |
| User-based approvers | ✅ Specific users |
| Auto-approval rules | ✅ Configurable |
| Timeout handling | ✅ With escalation |
| Rejection handling | ✅ With comments |

### Approval Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    APPROVAL WORKFLOW                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐             │
│   │ REQUESTED│───▶│ LEVEL 1  │───▶│ LEVEL 2  │───▶│ APPROVED │             │
│   │          │    │ REVIEW   │    │ REVIEW   │    │          │             │
│   └──────────┘    └──────────┘    └──────────┘    └──────────┘             │
│        │               │               │               │                    │
│        │               │               │               │                    │
│        ▼               ▼               ▼               ▼                    │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐             │
│   │ CANCELLED│    │ REJECTED │    │ REJECTED │    │ DEPLOYED │             │
│   │          │    │          │    │          │    │          │             │
│   └──────────┘    └──────────┘    └──────────┘    └──────────┘             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### External Tool Integration (Future)

| Tool | Status |
|------|--------|
| Jira | 🔴 Placeholder |
| ServiceNow | 🔴 Placeholder |
| Custom Webhook | 🔴 Placeholder |

---

## Promotion Mechanics

### Same Subscription Promotion

```
SOURCE WORKBENCH                       TARGET WORKBENCH
┌─────────────────────┐               ┌─────────────────────┐
│                     │               │                     │
│  Scenario v1.2.3    │   Promote     │  Scenario v1.2.3    │
│  ┌───────────────┐  │──────────────▶│  ┌───────────────┐  │
│  │ App Container │  │               │  │ App Container │  │
│  │ (registry ref)│  │               │  │ (same ref)    │  │
│  └───────────────┘  │               │  └───────────────┘  │
│  ┌───────────────┐  │               │  ┌───────────────┐  │
│  │ CRDs          │  │    Clone      │  │ CRDs          │  │
│  │ (git ref)     │  │──────────────▶│  │ (new copy)    │  │
│  └───────────────┘  │               │  └───────────────┘  │
│                     │               │                     │
└─────────────────────┘               └─────────────────────┘

SAME SUBSCRIPTION:
• Container: Reference stays (same production registry)
• CRDs: Cloned to target workbench folder in git
```

### Cross-Subscription Promotion

```
SOURCE SUBSCRIPTION                    TARGET SUBSCRIPTION
┌─────────────────────┐               ┌─────────────────────┐
│  Production         │    Copy       │  Production         │
│  Registry           │──────────────▶│  Registry           │
│  (container)        │               │  (container copy)   │
└─────────────────────┘               └─────────────────────┘

┌─────────────────────┐               ┌─────────────────────┐
│  Git Repository     │    Clone      │  Git Repository     │
│  (CRDs)             │──────────────▶│  (CRD copies)       │
└─────────────────────┘               └─────────────────────┘

CROSS-SUBSCRIPTION:
• Container: Physical copy to target registry
• CRDs: Cloned to target subscription's git repo
```

---

## Version Compatibility

Promotion requires **semantic version compatibility** between source and target:

### Workbench Specification Compatibility

| Compatibility | Rule |
|---------------|------|
| **Same version** | ✅ Always compatible |
| **Same MAJOR.MINOR** | ✅ Compatible (patch differences OK) |
| **Same MAJOR** | ⚠️ May work (minor differences) |
| **Different MAJOR** | ❌ Breaking changes, blocked |

### Compatibility Check

```
Source Workbench Spec: 1.2.3
Target Workbench Spec: 1.2.0

Compatibility Check:
├── MAJOR: 1 == 1 ✅
├── MINOR: 2 == 2 ✅
└── PATCH: 3 >= 0 ✅

Result: COMPATIBLE
```

### Breaking Changes (Block Promotion)

- Removed roles referenced by Scenario
- Removed task types used by Scenario
- Incompatible Hub Environment changes
- Data store schema incompatibilities

---

## Subscription-Level Resources

Some resources are scoped to the subscription, not individual workbenches:

| Resource | Promotion Behavior |
|----------|-------------------|
| Machine Definitions | Promoted with subscription |
| Tool Definitions | Promoted with subscription |
| Shared Data Store specs | Promoted by admin via subscription-level paths |
| Environment configurations | NOT promoted (configured per subscription) |

> **Important:** Concrete entities (Machine Instances, Tool Instances, Environments) are NOT promoted. Only specifications/definitions are promoted. Admins configure concrete entities per subscription.

---

## Promotion Request

### Developer-Initiated

```yaml
apiVersion: hub.olympus.io/v1
kind: PromotionRequest
metadata:
  name: pr-dispute-scenario-001
  namespace: acme-bank
spec:
  # What to promote
  source:
    type: scenario  # scenario | workbench | subscription
    workbench: dispute-ops-dev
    scenario: standard-dispute
    version: 1.2.3
  
  # Where to promote
  destination:
    promotion_path_ref: dev-to-staging  # or destination_ref
  
  # Optional: promotion notes
  notes: "Feature complete, ready for staging validation"
  
status:
  state: pending_approval  # pending_approval | approved | rejected | deploying | deployed | failed
  approval:
    level_1:
      status: approved
      approver: lead@acme.com
      timestamp: "2026-01-06T11:00:00Z"
    level_2:
      status: pending
  deployment:
    started_at: null
    completed_at: null
    error: null
```

---

## Notifications

Promotion events trigger notifications via [Notification Services](../notification-services/README.md):

| Event | Default Recipients |
|-------|-------------------|
| Promotion Requested | Configured approvers, dev team |
| Approval Pending (per level) | Next-level approvers |
| Promotion Approved | Requester, ops team |
| Promotion Rejected | Requester, dev team |
| Deployment Started | Ops team |
| Deployment Completed | All stakeholders |
| Deployment Failed | Requester, ops team, admins |

---

## Rollback

### Supported

- Rollback to **last deployed version only**
- Initiated by Admin or authorized Developer

### Rollback Flow

```
Current: v1.2.3
Previous: v1.2.2

Rollback Request
    │
    ▼
┌──────────────────┐
│ Redeploy v1.2.2  │
│ artifacts        │
└──────────────────┘
    │
    ▼
Workbench now running v1.2.2
```

### Limitations

| Aspect | Limitation |
|--------|------------|
| Depth | Last version only (not v-2, v-3) |
| Data Stores | Manual intervention required |
| Migrations | Not automatically reversed |

---

## Related Documentation

- [Container Registry](./container-registry.md) — Registry mechanics
- [Dev-Lifecycle-Stages](./dev-lifecycle-stages.md) — Stage compatibility
- [Git Repository](./git-repository.md) — CRD storage and sync
- [Data Store Migrations](./data-store-migrations.md) — Migration handling


