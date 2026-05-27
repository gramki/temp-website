---
name: Marketplace Documentation
overview: Document the Marketplace subsystem with component files, publisher/subscriber guides, integration updates across existing subsystems, UX architecture changes, and decision logs.
todos:
  - id: decision-logs
    content: Create 9 ADRs for key Marketplace decisions (0093-0101)
    status: completed
  - id: subsystem-readme
    content: Create Marketplace subsystem README.md with architecture and key concepts
    status: completed
    dependencies:
      - decision-logs
  - id: subsystem-components
    content: Create 8 component files (blueprints, catalog, publishing, subscription, etc.)
    status: completed
    dependencies:
      - subsystem-readme
  - id: operators-update
    content: Update Operators subsystem and create marketplace-operators.md
    status: completed
    dependencies:
      - subsystem-components
  - id: artifact-registry-update
    content: Update Artifact Registry docs for Marketplace integration
    status: completed
    dependencies:
      - subsystem-components
  - id: platform-notifications
    content: Create Platform Notifications subsystem (3 files)
    status: completed
    dependencies:
      - subsystem-components
  - id: other-subsystems-update
    content: Update Workbench Mgmt, Registry Services, Subscription Mgmt
    status: completed
    dependencies:
      - subsystem-components
  - id: marketplace-console
    content: Create Marketplace Console UX documentation
    status: completed
    dependencies:
      - subsystem-components
  - id: desk-updates
    content: Update 5 desk docs with Marketplace Console integration
    status: completed
    dependencies:
      - marketplace-console
  - id: cli-update
    content: Update CLI documentation with hub marketplace commands
    status: completed
    dependencies:
      - subsystem-components
  - id: publisher-guides
    content: Create 4 publisher guides (registration, scenario, workbench, manifest)
    status: completed
    dependencies:
      - subsystem-components
      - marketplace-console
  - id: subscriber-guides
    content: Create 4 subscriber guides (subscribing, blueprintspecs, building, updates)
    status: completed
    dependencies:
      - publisher-guides
---

# Marketplace Subsystem Documentation Plan

This plan documents the Marketplace subsystem comprehensively, following Hub documentation patterns. The work is organized into 6 phases.

---

## Phase 1: Marketplace Subsystem Core Documentation

Create the subsystem folder at [olympus-hub-docs/04-subsystems/marketplace/](olympus-hub-docs/04-subsystems/marketplace/) with one file per component.

### Files to Create

| File | Purpose |

|------|---------|

| `README.md` | Subsystem overview, architecture diagram, key concepts, component index |

| `blueprints-and-packages.md` | Hub Package model, BlueprintSpec types, package-manifest-container, Package Manifest CRD |

| `marketplace-artifact-repository.md` | Storage architecture, container cloning, hash-based deduplication, signing |

| `catalog-services.md` | OpenSearch catalog, listing manifest indexing, search and discovery, visibility enforcement |

| `publishing-services.md` | Publisher registration, publishing workflow, validation, security scanning, quarantine |

| `subscription-services.md` | Package subscription model, BlueprintSpec availability, derived resource creation, unsubscription |

| `version-management.md` | Semver semantics, update notifications, Blueprint update workflow, divergent resources |

| `security-and-compliance.md` | Federated IAM, artifact signing, security scanning, blacklisting, credential policy |

| `integration-points.md` | Integration with Artifact Registry, Promotion Model, Workbench Management, Registry Services |

### README.md Structure (following [artifact-registry/README.md](olympus-hub-docs/04-subsystems/artifact-registry/README.md) pattern)

```markdown
# Marketplace Subsystem

> **Status:** 🟡 WIP — Design Complete

## Overview
Platform-level service for publishing, discovering, and subscribing to Hub Packages...

## Architecture (ASCII diagram)

## Key Concepts (Hub Package, Blueprint, BlueprintSpec, Package Subscription)

## Components (table with links)

## Publishing Flow (diagram)

## Subscription Flow (diagram)

## Related Documentation
```

---

## Phase 2: Publisher Guides

Create guides in [olympus-hub-docs/10-guides/](olympus-hub-docs/10-guides/) for publishers.

### Files to Create

| File | Purpose |

|------|---------|

| `marketplace-publisher-registration.md` | How to register as a publisher (tenant admin + Hub Win approval) |

| `publishing-scenario-blueprints.md` | Step-by-step guide to publish Scenario Blueprints |

| `publishing-workbench-blueprints.md` | Step-by-step guide to publish Workbench Blueprints |

| `package-manifest-reference.md` | Complete Package Manifest CRD reference with field descriptions |

### Guide Structure (following [idea-to-deployment-guide.md](olympus-hub-docs/10-guides/idea-to-deployment-guide.md) pattern)

```markdown
# Guide: Publishing Scenario Blueprints

> **Status:** 🟡 Draft
> **Audience:** Developer, Tenant Admin
> **Last Updated:** 2026-01-11

## Table of Contents
## Overview
## Prerequisites (Publisher registration, workbench access)
## Step 1: Create Package Manifest CRD
## Step 2: Configure Package Contents
## Step 3: Add Visibility Controls
## Step 4: Publish via Automation Developer Desk
## Step 5: Admin Approval
## Step 6: Security Scanning and Acceptance
## Troubleshooting
## Related Documentation
```

---

## Phase 3: Subscriber Guides

### Files to Create

| File | Purpose |

|------|---------|

| `subscribing-to-packages.md` | How to discover, subscribe, and manage package subscriptions |

| `using-blueprintspecs.md` | How to create derived resources from BlueprintSpecs |

| `building-scenario-from-blueprint.md` | Complete guide to building a Scenario using a ScenarioBlueprintSpec |

| `managing-blueprint-updates.md` | How to handle version updates, divergent resources, manual merges |

### Building Scenario from Blueprint Guide Structure

```markdown
# Guide: Building a Scenario from BlueprintSpec

> **Status:** 🟡 Draft
> **Audience:** Process Architect, Developer
> **Last Updated:** 2026-01-11

## Overview
## Prerequisites (Package subscription, workbench access)
## Understanding BlueprintSpecs
## Step 1: Browse Available BlueprintSpecs
## Step 2: Create ScenarioNormativeSpec from ScenarioBlueprintSpec
## Step 3: Create ScenarioAutomationSpec
## Step 4: Create ScenarioDeploymentSpec
## Step 5: Deploy the Scenario
## Blueprint Reference Tracking
## Handling Updates from Blueprint
## Troubleshooting
```

---

## Phase 4: Subsystem Documentation Enhancements

Update existing subsystem documentation to incorporate Marketplace integration.

### Operators Subsystem

Update [olympus-hub-docs/04-subsystems/operators/README.md](olympus-hub-docs/04-subsystems/operators/README.md):

- Add **Marketplace Operators** section to architecture diagram
- Add new operator table entry for `marketplace-operator`

Create new file [olympus-hub-docs/04-subsystems/operators/marketplace-operators.md](olympus-hub-docs/04-subsystems/operators/marketplace-operators.md):

- Package Manifest CRD operator
- BlueprintSpec operators (ScenarioBlueprintSpec, WorkbenchBlueprintSpec, etc.)
- Package Subscription operator
- Derived Resource tracking

### Artifact Registry Subsystem

Update [olympus-hub-docs/04-subsystems/artifact-registry/README.md](olympus-hub-docs/04-subsystems/artifact-registry/README.md):

- Add section on Marketplace Artifact Repository relationship
- Document lazy container cloning from Marketplace

Update [olympus-hub-docs/04-subsystems/artifact-registry/promotion-model.md](olympus-hub-docs/04-subsystems/artifact-registry/promotion-model.md):

- Add section on automatic package subscription during cross-workbench promotion
- Document Blueprint-derived resource promotion behavior

### Workbench Management Subsystem

Update [olympus-hub-docs/04-subsystems/workbench-management/README.md](olympus-hub-docs/04-subsystems/workbench-management/README.md):

- Add section on BlueprintSpecs in workbench
- Document derived resource creation from BlueprintSpecs
- Add Blueprint reference section to derived resources

### Registry Services Subsystem

Update [olympus-hub-docs/04-subsystems/registry-services/README.md](olympus-hub-docs/04-subsystems/registry-services/README.md):

- Add section on platform-provided resource references in packages
- Document Blueprint dependency resolution

### Platform Notifications Subsystem (NEW)

**Rationale:** Notification Services is focused on tenant business domain notifications (Request Updates via Signal Exchange). Marketplace notifications are platform-to-tenant notifications, which require a different subsystem.

Create new subsystem at [olympus-hub-docs/04-subsystems/platform-notifications/](olympus-hub-docs/04-subsystems/platform-notifications/):

| File | Purpose |

|------|---------|

| `README.md` | Platform Notifications overview, architecture, notification types |

| `marketplace-notifications.md` | Marketplace-specific notifications (publishing, subscription, updates, security) |

| `subscription-notifications.md` | Tenant subscription notifications (renewal, quotas, announcements) |

**Notification Types to Document:**

**Marketplace Notifications:**

- Publisher registration approval/rejection
- Package publishing approval/rejection  
- Package subscription approval/rejection
- New package version availability
- Security vulnerability alerts
- Blacklisting notifications
- Out-of-sync Blueprint resource alerts
- Withdrawn Blueprint notifications

**Other Platform-to-Tenant Notifications:**

- Subscription renewal reminders
- Platform maintenance announcements
- Feature announcements
- Usage alerts / quota warnings
- Platform policy updates

### Subscription Management Subsystem

Update [olympus-hub-docs/04-subsystems/subscription-management/README.md](olympus-hub-docs/04-subsystems/subscription-management/README.md):

- Add section on Publisher registration workflow
- Document publisher allow/disallow lists

---

## Phase 5: UX Architecture Updates

### Desks to Update

| Desk | File | Changes |

|------|------|---------|

| Automation Development Desk | [automation-development-desk.md](olympus-hub-docs/06-ux-architecture/tenant-domain/automation-development-desk.md) | Add Marketplace Console access, Package creation, Publishing workflow |

| Scenario Design Desk | [scenario-design-desk.md](olympus-hub-docs/06-ux-architecture/tenant-domain/scenario-design-desk.md) | Add Marketplace Console access, BlueprintSpec browsing, Subscription initiation |

| Automation Product Desk | [automation-product-desk.md](olympus-hub-docs/06-ux-architecture/tenant-domain/automation-product-desk.md) | Add Marketplace Console access, Package discovery |

| Hub Control Center | [hub-control-center.md](olympus-hub-docs/06-ux-architecture/tenant-domain/hub-control-center.md) | Add Marketplace Console (Admin view), Publisher management, Subscription authorization |

| Hub Win Ops Center | [hub-win-ops-center.md](olympus-hub-docs/06-ux-architecture/publisher-domain/hub-win-ops-center.md) | Add Publisher Registration approval, Marketplace admin, Blacklisting |

### New File: Marketplace Console

Create [olympus-hub-docs/06-ux-architecture/tenant-domain/marketplace-console.md](olympus-hub-docs/06-ux-architecture/tenant-domain/marketplace-console.md):

- Discovery section (browse, search, filter packages)
- Subscription section (subscribe, manage subscriptions)
- Authorization section (admin approval interface)
- Package Creation section (Package Manifest CRD editor)
- Publishing section (publish workflow, status tracking)
- Notifications section (updates, security issues)
- Publisher Management section (allow/disallow lists)
- ASCII wireframes for each section

### CLI Updates

Update [olympus-hub-docs/06-ux-architecture/tenant-domain/cli-channels-for-developers.md](olympus-hub-docs/06-ux-architecture/tenant-domain/cli-channels-for-developers.md):

- Add `hub marketplace` command section
- Document all publisher commands (publish, packages list/get/update/withdraw/deprecate)
- Document all subscriber commands (search, browse, subscribe, subscriptions list/get/update/unsubscribe)
- Document common commands (publishers list/get, status)

---

## Phase 6: Decision Logs

Create ADRs for key Marketplace decisions in [olympus-hub-docs/decision-logs/](olympus-hub-docs/decision-logs/):

| ADR | Title | Key Decision |

|-----|-------|--------------|

| `0093-marketplace-platform-service.md` | Marketplace as Platform Service | Platform-level vs tenant-scoped marketplace |

| `0094-hub-package-atomic-unit.md` | Hub Package as Atomic Publishing Unit | Package vs individual artifact publishing |

| `0095-blueprintspec-transformation.md` | BlueprintSpec Transformation Model | Export transforms specs to BlueprintSpecs |

| `0096-lazy-container-cloning.md` | Lazy Container Cloning | Containers cloned on first deployment, not subscription |

| `0097-package-subscription-isolation.md` | Package Subscription Isolation | No cross-package resource sharing |

| `0098-visibility-controls-private-marketplace.md` | Visibility Controls for Private Marketplace | Tenant allow/disallow lists in package manifest |

| `0099-publisher-registration-approval.md` | Publisher Registration Approval | Hub Win team approval for publishers |

| `0100-federated-iam-marketplace.md` | Federated IAM for Marketplace | Tenant IAM federates with Marketplace IAM |

| `0101-platform-notifications-subsystem.md` | Platform Notifications Subsystem | Separate from Notification Services for platform-to-tenant notifications |

### ADR Structure (following [0047-scenario-atomic-promotion-unit.md](olympus-hub-docs/decision-logs/0047-scenario-atomic-promotion-unit.md) pattern)

```markdown
# ADR-00XX: [Title]

## Status
Accepted

## Date
2026-01-11

## Context
[Problem statement and constraints]

## Decision
[Clear statement of decision]

## Alternatives Considered
[Other options and why rejected]

## Consequences
### Positive
### Negative
### Neutral

## References
[Links to related docs]
```

---

## Summary

| Phase | Files Created | Files Updated |

|-------|---------------|---------------|

| Phase 1: Subsystem Core | 9 files | - |

| Phase 2: Publisher Guides | 4 files | - |

| Phase 3: Subscriber Guides | 4 files | - |

| Phase 4: Subsystem Updates | 4 files (incl. Platform Notifications) | 5 files |

| Phase 5: UX Architecture | 1 file | 6 files |

| Phase 6: Decision Logs | 9 files | - |

| **Total** | **31 files** | **11 files** |

---

## Execution Order

1. Start with Phase 6 (Decision Logs) - captures rationale before detailed docs
2. Phase 1 (Subsystem Core) - establishes foundation
3. Phase 4 (Subsystem Updates) - updates integration points
4. Phase 5 (UX Architecture) - updates user-facing docs
5. Phase 2 and 3 (Guides) - practical user documentation last