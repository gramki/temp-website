# Subscription Services

> **Status:** 🟡 WIP — Design Complete

This document describes the package subscription model, BlueprintSpec availability, derived resource creation, and unsubscription procedures.

---

## Overview

Subscription Services manages how subscribers access and use Marketplace packages within their workbenches.

| Aspect | Description |
|--------|-------------|
| **Subscription Unit** | Package to workbench |
| **Approval** | Admin approval required |
| **Delivery** | BlueprintSpecs made available |
| **Usage** | Derived resources created from BlueprintSpecs |

---

## Package Subscription Model

A **package-subscription** is a composite of:

| Component | Description |
|-----------|-------------|
| **Package Listing** | The published package |
| **Subscribing Tenant** | Tenant subscription ID |
| **Subscribing Workbench** | Target workbench ID |

Subscriptions are tracked at the **workbench level**, not just tenant level.

---

## Subscription Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          SUBSCRIPTION FLOW                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. DISCOVER & SELECT                                                      │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  User browses Marketplace Console                                  │    │
│   │  • Searches/filters packages                                       │    │
│   │  • Reviews package details                                         │    │
│   │  • Selects package to subscribe                                    │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   2. INITIATE SUBSCRIPTION                                                  │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  User specifies target workbench                                   │    │
│   │  • Subscription request created                                    │    │
│   │  • Request includes: package, version, workbench                   │    │
│   │  • Admin notified                                                  │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   3. ADMIN APPROVAL                                                         │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Tenant Admin reviews request                                      │    │
│   │  • Checks publisher allow/disallow lists                           │    │
│   │  • Reviews package contents                                        │    │
│   │  • Approves or rejects                                             │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   4. BLUEPRINTSPECS AVAILABLE                                               │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  If approved:                                                      │    │
│   │  • Package subscription created                                    │    │
│   │  • BlueprintSpecs added to workbench                               │    │
│   │  • Containers NOT cloned (lazy cloning)                            │    │
│   │  • User notified                                                   │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## BlueprintSpec Availability

When a package is subscribed to:

### What Becomes Available

| Resource | Status |
|----------|--------|
| **BlueprintSpecs** | Visible and usable in workbench |
| **Container Images** | Remain in Marketplace (not cloned yet) |
| **Package Manifest** | Accessible for reference |

### BlueprintSpec Visibility

- BlueprintSpecs appear in workbench resource lists
- Can be viewed and inspected
- Can be used to create derived resources
- Are **not** directly part of workbench definition

---

## Derived Resource Creation

To use a BlueprintSpec, subscribers create **derived resources**.

### Transformation

| BlueprintSpec | Creates |
|---------------|---------|
| `ScenarioBlueprintSpec` | `ScenarioNormativeSpec` + `ScenarioAutomationSpec` |
| `WorkbenchBlueprintSpec` | Workbench template resources |
| `MachineBlueprintSpec` | `MachineDefinitionSpec` |
| `ToolBlueprintSpec` | `ToolDefinitionSpec` |

### Creation Flow

```
1. User selects BlueprintSpec
2. User initiates "Create from Blueprint"
3. Derived resource created with:
   - Content from BlueprintSpec
   - Blueprint reference section added
   - Subscriber can customize

4. Derived resource is regular workbench resource
   - Can be modified
   - Can be deployed
   - Follows normal lifecycle
```

### Blueprint Reference Section

Every derived resource includes:

```yaml
blueprintReference:
  packageSha: "sha256:abc123..."
  packageUri: "marketplace://packages/dispute-ops-v1.2.0"
  blueprintName: "dispute-triage"
  blueprintType: "ScenarioBlueprintSpec"
  packageVersion: "1.2.0"
```

---

## Container Cloning

Containers are cloned **lazily** — only when first deployed.

### Cloning Trigger

| Event | Container Action |
|-------|------------------|
| Package Subscription | No cloning |
| Derived Resource Creation | No cloning |
| Scenario Deployment | Container cloned to tenant registry |

### Cloning Process

1. Scenario Deployment references container
2. Check if container exists in tenant registry
3. If not: clone from Marketplace Artifact Repository
4. Verify Marketplace signature
5. Store in tenant artifact registry
6. Deployment proceeds

---

## Subscription Tracking

Marketplace maintains comprehensive subscription records:

### Tracked Information

| Field | Description |
|-------|-------------|
| `subscription_id` | Unique subscription identifier |
| `package_id` | Package being subscribed |
| `package_version` | Version subscribed |
| `tenant_id` | Subscribing tenant |
| `workbench_id` | Target workbench |
| `status` | active / pending-unsubscription / unsubscribed |
| `subscribed_date` | When subscription was created |
| `approved_by` | Admin who approved |

### Visibility

| Viewer | Can See |
|--------|---------|
| **Publisher** | All subscriptions to their packages |
| **Tenant Admin** | All subscriptions in their tenant |
| **Hub Win Team** | All subscriptions across platform |

---

## Publisher Allow/Disallow Lists

Tenant admins can control which publishers are trusted:

### Allow/Disallow Logic (Apache-style)

```
Order: Allow, Disallow (first match wins)

Allow: publisher-a, publisher-b
Disallow: publisher-c

Result:
- publisher-a packages: Visible
- publisher-b packages: Visible
- publisher-c packages: Hidden
- publisher-d packages: Visible (not in any list)
```

### Configuration

- Managed via Marketplace Console (Admin view) or Hub Control Center
- Applies to all workbenches in subscription
- Affects visibility (hidden publishers' packages not shown)

---

## Unsubscription

### Unsubscription Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          UNSUBSCRIPTION FLOW                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. USER INITIATES UNSUBSCRIPTION                                          │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  User requests to unsubscribe from package                         │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   2. SUBSCRIPTION MARKED PENDING                                            │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Status: "pending-unsubscription"                                  │    │
│   │  • BlueprintSpecs become invisible                                 │    │
│   │  • Cannot create new derived resources                             │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   3. DERIVED RESOURCES REMAIN                                               │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Existing derived resources continue to work                       │    │
│   │  • Deployments still run                                           │    │
│   │  • Manual deletion required                                        │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   4. CLEANUP                                                                │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  User manually deletes derived resources                           │    │
│   │  • Deployments deleted → containers evicted                        │    │
│   │  • All derived resources deleted                                   │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   5. UNSUBSCRIPTION COMPLETE                                                │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  When no derived resources remain:                                 │    │
│   │  • Status: "unsubscribed"                                          │    │
│   │  • Subscription record archived                                    │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Why Manual Cleanup?

- Prevents accidental deletion of production resources
- User maintains control over timing
- Allows graceful wind-down

---

## Cross-Workbench Deployment

When a Blueprint-derived resource is promoted to a new workbench:

### Automatic Subscription

1. Promotion initiated to target workbench
2. System detects Blueprint reference in resource
3. Target workbench automatically gets package subscription
4. Created by platform operators (not manual)
5. Ensures Blueprint tracking across workbenches

### Benefits

- Maintains Blueprint reference integrity
- Enables update propagation across workbenches
- Transparent to user

---

## Related Documentation

- [Blueprints and Packages](./blueprints-and-packages.md) — Package model
- [Version Management](./version-management.md) — Updates and versions
- [Marketplace Console](../../06-ux-architecture/tenant-domain/marketplace-console.md) — Subscription UI
- [ADR-0096: Lazy Container Cloning](../../decision-logs/0096-lazy-container-cloning.md)
- [ADR-0097: Package Subscription Isolation](../../decision-logs/0097-package-subscription-isolation.md)

