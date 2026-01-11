# Marketplace Operators

> **Status:** 🟡 WIP — Design Complete

Operators for managing Marketplace-related CRDs including Package Manifests, BlueprintSpecs, and Package Subscriptions.

---

## Overview

| Operator | CRDs Managed | Persona |
|----------|--------------|---------|
| **marketplace-package-operator** | PackageManifest | Developer |
| **marketplace-subscription-operator** | PackageSubscription | Admin |
| **blueprintspec-operator** | *BlueprintSpec types | System |

---

## Package Manifest Operator

Manages `PackageManifest` CRDs for package publishing.

### CRD: PackageManifest

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: PackageManifest
metadata:
  name: dispute-ops-package
  namespace: acme-dev
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
status:
  phase: Draft | Pending | Published | Failed
  publishedVersion: "1.2.0"
  publishedDate: "2026-01-15T10:00:00Z"
  message: "Successfully published"
```

### Reconciliation

1. Validate manifest fields
2. Resolve blueprint references
3. Track publishing status
4. Update status on publishing events

---

## Package Subscription Operator

Manages `PackageSubscription` CRDs for workbench subscriptions.

### CRD: PackageSubscription

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: PackageSubscription
metadata:
  name: dispute-ops-sub
  namespace: acme-prod
spec:
  packageId: "dispute-ops"
  packageVersion: "^1.2.0"  # Semver range
  workbenchId: "dispute-ops-prod"
status:
  phase: Pending | Active | PendingUnsubscription | Unsubscribed
  subscribedVersion: "1.2.3"
  subscribedDate: "2026-01-15T10:00:00Z"
  blueprintSpecs:
    - name: dispute-triage
      type: ScenarioBlueprintSpec
    - name: dispute-resolution
      type: ScenarioBlueprintSpec
  derivedResources: 3
```

### Reconciliation

1. Validate subscription request
2. Fetch BlueprintSpecs from Marketplace
3. Make BlueprintSpecs available in workbench
4. Track subscription status

---

## BlueprintSpec Operators

Manages various BlueprintSpec types delivered from Marketplace.

### BlueprintSpec Types

| Type | Source Spec |
|------|-------------|
| `ScenarioBlueprintSpec` | ScenarioNormativeSpec |
| `WorkbenchBlueprintSpec` | WorkbenchSpec |
| `MachineBlueprintSpec` | MachineDefinitionSpec |
| `ToolBlueprintSpec` | ToolDefinitionSpec |
| `RawAgentBlueprintSpec` | RawAgentSpec |
| `HubApplicationBlueprintSpec` | HubApplicationSpec |

> **Note:** `HubApplicationBlueprintSpec` includes a build recipe that the CI subsystem uses to combine the Blueprint's base container with subscriber-provided files. See [Hub Application Blueprints](../marketplace/hub-application-blueprints.md).

### Example: ScenarioBlueprintSpec

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: ScenarioBlueprintSpec
metadata:
  name: dispute-triage
  namespace: acme-prod
  labels:
    marketplace.hub.olympus/package-id: "dispute-ops"
    marketplace.hub.olympus/package-version: "1.2.0"
spec:
  # Original ScenarioNormativeSpec content
  scenarioName: "Dispute Triage"
  goals:
    - name: "Triage disputes within SLA"
  # ... rest of scenario spec
status:
  available: true
  derivedResources:
    - name: dispute-triage-normative
      type: ScenarioNormativeSpec
```

---

## Cross-Operator Dependencies

```
PackageManifest
       │
       │ Publish triggers
       ▼
Marketplace Services (external)
       │
       │ Subscription delivers
       ▼
PackageSubscription
       │
       │ Creates
       ▼
BlueprintSpecs (various types)
       │
       │ User creates from
       ▼
Derived Resources (regular specs)
```

---

## Related Documentation

- [Marketplace Subsystem](../marketplace/README.md)
- [Blueprints and Packages](../marketplace/blueprints-and-packages.md)
- [Subscription Services](../marketplace/subscription-services.md)

