# Integration Points

> **Status:** 🟡 WIP — Design Complete

This document describes how Marketplace integrates with other Hub subsystems including Artifact Registry, Promotion Model, Workbench Management, and Registry Services.

---

## Overview

Marketplace integrates with multiple Hub subsystems to provide seamless artifact sharing.

| Subsystem | Integration Purpose |
|-----------|---------------------|
| **Artifact Registry** | Container storage and cloning |
| **Promotion Model** | Cross-workbench deployment |
| **Workbench Management** | BlueprintSpec and derived resources |
| **Registry Services** | Platform resource references |
| **Platform Notifications** | Update and security notifications |
| **Subscription Management** | Publisher registration |

---

## Artifact Registry Integration

### Relationship

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ARTIFACT REGISTRY INTEGRATION                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   PUBLISHER TENANT                 MARKETPLACE               SUBSCRIBER     │
│   ┌────────────────┐              ┌────────────────┐       ┌────────────┐  │
│   │  Tenant        │   Publish    │  Marketplace   │  Clone │  Tenant    │  │
│   │  Artifact      │ ──────────▶  │  Artifact      │ ─────▶ │  Artifact  │  │
│   │  Registry      │              │  Repository    │        │  Registry  │  │
│   │                │              │                │        │            │  │
│   │  (Source)      │              │  (Platform)    │        │  (Target)  │  │
│   └────────────────┘              └────────────────┘        └────────────┘  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Key Integration Points

| Point | Description |
|-------|-------------|
| **Publishing** | Containers cloned from publisher's registry to Marketplace |
| **Subscription** | BlueprintSpecs available (containers not yet cloned) |
| **Deployment** | Containers cloned to subscriber's registry on first use |

### Lazy Container Cloning

- Containers remain in Marketplace until first deployment
- Clone triggered by Scenario Deployment
- Signature verified during clone
- Stored in subscriber's tenant registry

### Container Deduplication

- Publisher's containers may already exist in Marketplace (same hash)
- Hash-based deduplication avoids duplicate storage
- References existing container if hash matches

---

## Promotion Model Integration

### Cross-Workbench Deployment

When a Blueprint-derived resource is promoted to a new workbench:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PROMOTION MODEL INTEGRATION                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   SOURCE WORKBENCH                              TARGET WORKBENCH            │
│   ┌────────────────────────┐                   ┌────────────────────────┐   │
│   │                        │                   │                        │   │
│   │  Derived Resource      │    Promote        │  Derived Resource      │   │
│   │  (Blueprint reference) │ ───────────────▶  │  (Blueprint reference) │   │
│   │                        │                   │                        │   │
│   │  Package Subscription  │                   │  Package Subscription  │   │
│   │  (existing)            │                   │  (auto-created)        │   │
│   │                        │                   │                        │   │
│   └────────────────────────┘                   └────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Automatic Subscription

1. Promotion detects Blueprint reference in resource
2. Target workbench needs access to Blueprint
3. Platform operators create package subscription automatically
4. Subscription enables Blueprint tracking in target workbench

### Benefits

- Maintains Blueprint reference integrity across workbenches
- Enables update propagation to promoted resources
- Transparent to user (no manual subscription needed)

---

## Workbench Management Integration

### BlueprintSpec Handling

| Responsibility | Description |
|----------------|-------------|
| **Marketplace** | Delivers BlueprintSpecs on subscription |
| **Workbench Management** | Stores and exposes BlueprintSpecs |
| **User** | Creates derived resources from BlueprintSpecs |

### Derived Resource Creation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   WORKBENCH MANAGEMENT INTEGRATION                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   MARKETPLACE                     WORKBENCH MANAGEMENT                       │
│   ┌────────────────────────┐     ┌────────────────────────────────────────┐ │
│   │                        │     │                                        │ │
│   │  BlueprintSpecs        │ ──▶ │  BlueprintSpecs (available)            │ │
│   │  (package contents)    │     │                                        │ │
│   │                        │     │              │                         │ │
│   └────────────────────────┘     │              ▼                         │ │
│                                  │                                        │ │
│                                  │  User creates derived resources        │ │
│                                  │                                        │ │
│                                  │              │                         │ │
│                                  │              ▼                         │ │
│                                  │                                        │ │
│                                  │  Derived Resources (workbench specs)   │ │
│                                  │  + Blueprint Reference Section         │ │
│                                  │                                        │ │
│                                  └────────────────────────────────────────┘ │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Blueprint Reference Section

Workbench Management adds Blueprint reference to derived resources:

```yaml
blueprintReference:
  packageSha: "sha256:abc123..."
  packageUri: "marketplace://packages/dispute-ops-v1.2.0"
  blueprintName: "dispute-triage"
  blueprintType: "ScenarioBlueprintSpec"
  packageVersion: "1.2.0"
```

### Resource States

Workbench Management tracks:
- Synced / Out-of-Sync status
- Divergence from Blueprint
- Update availability

---

## Registry Services Integration

### Platform Resource References

Packages can reference platform-provided resources:

| Resource Type | Example |
|---------------|---------|
| **Machine Definitions** | Core banking connectors |
| **Tool Definitions** | Standard utilities |
| **Platform Services** | Common integrations |

### Resolution Flow

```
1. Package references platform Machine Definition
2. Derived resource created with reference
3. Registry Services resolves reference at deployment
4. Validates platform resource exists and is compatible
```

### Validation

During publishing:
- Referenced platform resources validated
- Version compatibility checked
- Missing resources flagged as errors

---

## Platform Notifications Integration

Marketplace uses Platform Notifications for user communication.

### Notification Types

| Event | Notification |
|-------|--------------|
| **Publishing** | Approval/rejection, security scan results |
| **Subscription** | Approval/rejection, resource availability |
| **Updates** | New version available |
| **Security** | Vulnerability detected, blacklisting |

### Flow

```
Marketplace Event
       │
       ▼
Platform Notifications
       │
       ▼
Cipher Notification Service
       │
       ▼
Email / SMS / Push / Webhook
```

---

## Subscription Management Integration

### Publisher Registration

| Step | Subsystem |
|------|-----------|
| Registration Request | Subscription Management (Tenant Admin) |
| Registration Approval | Hub Win Operations |
| Publisher Status | Marketplace Services |

### Flow

```
1. Tenant Admin requests publisher registration
   └── Via Subscription Management / Hub Control Center

2. Hub Win Team reviews and approves
   └── Via Hub Win Ops Center

3. Publisher status activated
   └── Marketplace Services enables publishing

4. Signing certificate stored
   └── Marketplace Security Services
```

---

## Operator Integration

Marketplace requires operators for CRD management.

### Marketplace Operators

| Operator | CRDs Managed |
|----------|--------------|
| **Package Manifest Operator** | PackageManifest CRD |
| **BlueprintSpec Operators** | ScenarioBlueprintSpec, WorkbenchBlueprintSpec, etc. |
| **Subscription Operator** | PackageSubscription CRD |

### Reconciliation

- Package Manifest changes trigger publishing workflow
- Subscription changes trigger BlueprintSpec delivery
- Derived resources tracked for Blueprint references

---

## Integration Summary

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        INTEGRATION OVERVIEW                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────┐     ┌─────────────┐     ┌─────────────┐                   │
│   │  Artifact   │     │  Workbench  │     │  Registry   │                   │
│   │  Registry   │     │  Management │     │  Services   │                   │
│   └──────┬──────┘     └──────┬──────┘     └──────┬──────┘                   │
│          │                   │                   │                          │
│          │   Container       │  BlueprintSpec    │  Platform                │
│          │   Storage/Clone   │  Delivery         │  Resources               │
│          │                   │                   │                          │
│          └───────────────────┴───────────────────┘                          │
│                              │                                               │
│                              ▼                                               │
│                    ┌─────────────────────┐                                  │
│                    │     MARKETPLACE     │                                  │
│                    │      SUBSYSTEM      │                                  │
│                    └─────────────────────┘                                  │
│                              │                                               │
│          ┌───────────────────┴───────────────────┐                          │
│          │                   │                   │                          │
│          ▼                   ▼                   ▼                          │
│   ┌─────────────┐     ┌─────────────┐     ┌─────────────┐                   │
│   │  Promotion  │     │  Platform   │     │Subscription │                   │
│   │   Model     │     │ Notifs      │     │ Management  │                   │
│   └─────────────┘     └─────────────┘     └─────────────┘                   │
│                                                                              │
│   Cross-workbench        User              Publisher                        │
│   deployment          notifications        registration                     │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Related Documentation

- [Artifact Registry](../artifact-registry/README.md)
- [Workbench Management](../workbench-management/README.md)
- [Registry Services](../registry-services/README.md)
- [Platform Notifications](../platform-notifications/README.md)
- [Operators](../operators/README.md)

