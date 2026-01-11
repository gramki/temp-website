# Marketplace Subsystem

> **Status:** 🟡 WIP — Design Complete

The Marketplace subsystem provides a **platform-level service** for publishing, discovering, and subscribing to reusable Hub artifacts. Publishers can share Scenarios, Workbenches, Tools, and other resources as **Hub Packages**, while subscribers can discover and deploy these packages to their own workbenches.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Scope** | Platform-level (serves all tenants) |
| **Purpose** | Artifact sharing and reuse across tenants |
| **Key Concept** | Hub Package (collection of Blueprints) |
| **Storage** | Marketplace Artifact Repository |
| **Discovery** | OpenSearch-based Catalog Services |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MARKETPLACE ARCHITECTURE                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   PUBLISHERS                              SUBSCRIBERS                        │
│   ┌──────────────────────┐               ┌──────────────────────┐           │
│   │  Tenant Subscription │               │  Tenant Subscription │           │
│   │  ┌────────────────┐  │               │  ┌────────────────┐  │           │
│   │  │   Workbench    │  │               │  │   Workbench    │  │           │
│   │  │  (DEV)         │  │               │  │  (DEV/PROD)    │  │           │
│   │  │                │  │               │  │                │  │           │
│   │  │ Package        │  │               │  │ BlueprintSpecs │  │           │
│   │  │ Manifest CRDs  │  │               │  │ (subscribed)   │  │           │
│   │  └───────┬────────┘  │               │  └───────▲────────┘  │           │
│   └──────────│───────────┘               └──────────│───────────┘           │
│              │                                      │                        │
│              │ Publish                              │ Subscribe              │
│              ▼                                      │                        │
│   ┌──────────────────────────────────────────────────────────────────────┐  │
│   │                         MARKETPLACE SERVICES                          │  │
│   │                                                                       │  │
│   │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐       │  │
│   │  │   Publishing    │  │    Catalog      │  │  Subscription   │       │  │
│   │  │   Services      │  │    Services     │  │    Services     │       │  │
│   │  │                 │  │                 │  │                 │       │  │
│   │  │ • Validation    │  │ • OpenSearch    │  │ • Package Sub   │       │  │
│   │  │ • Scanning      │  │ • Search/Filter │  │ • BlueprintSpec │       │  │
│   │  │ • Quarantine    │  │ • Visibility    │  │ • Unsubscribe   │       │  │
│   │  └────────┬────────┘  └────────▲────────┘  └────────▲────────┘       │  │
│   │           │                    │                    │                │  │
│   │           │                    │                    │                │  │
│   │  ┌────────▼────────────────────┴────────────────────┴────────────┐   │  │
│   │  │                MARKETPLACE ARTIFACT REPOSITORY                 │   │  │
│   │  │                                                                │   │  │
│   │  │  ┌──────────────────┐  ┌──────────────────────────────────┐   │   │  │
│   │  │  │    Containers    │  │  Package-Manifest-Containers     │   │   │  │
│   │  │  │  (OCI, signed,   │  │  (CRDs + Manifest per package)   │   │   │  │
│   │  │  │   deduplicated)  │  │                                  │   │   │  │
│   │  │  └──────────────────┘  └──────────────────────────────────┘   │   │  │
│   │  └────────────────────────────────────────────────────────────────┘   │  │
│   │                                                                       │  │
│   └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│   SECURITY                                                                   │
│   ┌──────────────────────────────────────────────────────────────────────┐  │
│   │  • Federated IAM           • Container Signing (Publisher + MP)      │  │
│   │  • Security Scanning       • Quarantine Process                      │  │
│   │  • Blacklisting            • Continuous Vulnerability Monitoring     │  │
│   └──────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Hub Package** | Atomic unit of publishing; a self-sufficient collection of Blueprints |
| **Blueprint** | Definition/Specification exported for distribution (candidate for adoption) |
| **BlueprintSpec** | CRD type for subscribed Blueprints (e.g., ScenarioBlueprintSpec) |
| **Package Subscription** | Composite of (package-listing, tenant, workbench-id) |
| **Derived Resource** | Regular specification created from a BlueprintSpec |
| **Publisher** | Registered tenant subscription authorized to publish packages |
| **Visibility Controls** | Allow/disallow lists for tenants and regions in package manifest |

---

## Core Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **Package Publishing** | Accept, validate, scan, and store Hub Packages |
| **Catalog Management** | Index and expose package listings for discovery |
| **Subscription Management** | Track package subscriptions per workbench |
| **BlueprintSpec Delivery** | Make BlueprintSpecs available in subscribed workbenches |
| **Version Management** | Handle package versions and update notifications |
| **Security Enforcement** | Signing, scanning, quarantine, blacklisting |

---

## Components

| Component | Description | Documentation |
|-----------|-------------|---------------|
| Blueprints and Packages | Hub Package model, BlueprintSpec types | [blueprints-and-packages.md](./blueprints-and-packages.md) |
| Hub Application Blueprints | Reusable application containers with build recipes | [hub-application-blueprints.md](./hub-application-blueprints.md) |
| Marketplace Artifact Repository | Container and CRD storage | [marketplace-artifact-repository.md](./marketplace-artifact-repository.md) |
| Catalog Services | OpenSearch-based discovery | [catalog-services.md](./catalog-services.md) |
| Publishing Services | Publisher registration, workflow | [publishing-services.md](./publishing-services.md) |
| Subscription Services | Package subscription model | [subscription-services.md](./subscription-services.md) |
| Version Management | Semver, updates, divergence | [version-management.md](./version-management.md) |
| Security and Compliance | IAM, signing, scanning | [security-and-compliance.md](./security-and-compliance.md) |
| Integration Points | Subsystem integrations | [integration-points.md](./integration-points.md) |

---

## Publishing Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PUBLISHING FLOW                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. CREATE PACKAGE MANIFEST CRD                                            │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Developer creates Package Manifest CRD in workbench               │    │
│   │  • References Specification artifacts                              │    │
│   │  • Includes package metadata (name, description, categories)       │    │
│   │  • Configures visibility controls                                  │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   2. PUBLISH VIA AUTOMATION DEVELOPER DESK                                  │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Developer initiates publishing                                    │    │
│   │  • Tool packages containers and CRDs                               │    │
│   │  • Associated children automatically included                      │    │
│   │  • Admin notified for approval                                     │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   3. ADMIN APPROVAL                                                         │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Tenant Admin reviews and approves                                 │    │
│   │  • Signs containers with publisher certificate                     │    │
│   │  • Submits to Marketplace                                          │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   4. SECURITY SCANNING & QUARANTINE                                         │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Marketplace validates and scans                                   │    │
│   │  • Signature verification                                          │    │
│   │  • Malware and vulnerability scanning                              │    │
│   │  • Artifacts quarantined until cleared                             │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   5. CATALOG INDEXING                                                       │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Package added to catalog                                          │    │
│   │  • Manifest extracted and indexed in OpenSearch                    │    │
│   │  • Package becomes discoverable                                    │    │
│   │  • Marketplace re-signs containers                                 │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Subscription Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          SUBSCRIPTION FLOW                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. DISCOVER                                                               │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  User browses Marketplace Console                                  │    │
│   │  • Search, filter, browse packages                                 │    │
│   │  • View package details and contents                               │    │
│   │  • Visibility controls enforced                                    │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   2. INITIATE SUBSCRIPTION                                                  │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  User selects package and target workbench                         │    │
│   │  • Subscription request created                                    │    │
│   │  • Admin notified for approval                                     │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   3. ADMIN APPROVAL                                                         │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Tenant Admin approves subscription                                │    │
│   │  • Checks publisher allow/disallow lists                           │    │
│   │  • Approves or rejects                                             │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   4. BLUEPRINTSPECS AVAILABLE                                               │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Package resources become available in workbench                   │    │
│   │  • BlueprintSpecs visible and usable                               │    │
│   │  • Containers NOT yet cloned (lazy cloning)                        │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   5. CREATE DERIVED RESOURCES                                               │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  User creates regular specs from BlueprintSpecs                    │    │
│   │  • ScenarioBlueprintSpec → ScenarioNormativeSpec                  │    │
│   │  • Blueprint reference section added                               │    │
│   │  • Containers cloned on first deployment                           │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Hub Package Contents

A Hub Package can contain Blueprints of these types:

| Blueprint Type | Description |
|----------------|-------------|
| **Scenario Blueprints** | Complete scenarios with all specifications (includes Trained Agents) |
| **Workbench Blueprints** | Workbench templates with scenarios and configurations |
| **Machine Blueprints** | Machine definitions for external system integration |
| **Tools Blueprints** | Standalone tool definitions |
| **Raw Agents Blueprints** | Raw agent specifications |
| **Hub Application Blueprints** | Reusable application containers with build recipes (DSL runtimes, interpreters) |

Packages are **self-sufficient** — they contain all required resources and don't depend on other packages. Packages can reference **platform-provided resources** (e.g., platform Machine Definitions).

---

## Security Model

| Aspect | Mechanism |
|--------|-----------|
| **Authentication** | Federated IAM (Tenant IAM → Marketplace IAM) |
| **Publisher Identity** | Signing certificate submitted during registration |
| **Container Signing** | Publisher signs → Marketplace re-signs for distribution |
| **Security Scanning** | Pre-acceptance + continuous vulnerability scanning |
| **Quarantine** | Artifacts held until security clearance |
| **Blacklisting** | Publishers and Hub Win can block packages |
| **Credentials** | Packages must NOT contain credentials |

---

## Related Decision Records

| ADR | Title |
|-----|-------|
| [ADR-0093](../../decision-logs/0093-marketplace-platform-service.md) | Marketplace as Platform Service |
| [ADR-0094](../../decision-logs/0094-hub-package-atomic-unit.md) | Hub Package as Atomic Publishing Unit |
| [ADR-0095](../../decision-logs/0095-blueprintspec-transformation.md) | BlueprintSpec Transformation Model |
| [ADR-0096](../../decision-logs/0096-lazy-container-cloning.md) | Lazy Container Cloning |
| [ADR-0097](../../decision-logs/0097-package-subscription-isolation.md) | Package Subscription Isolation |
| [ADR-0098](../../decision-logs/0098-visibility-controls-private-marketplace.md) | Visibility Controls for Private Marketplace |
| [ADR-0099](../../decision-logs/0099-publisher-registration-approval.md) | Publisher Registration Approval |
| [ADR-0100](../../decision-logs/0100-federated-iam-marketplace.md) | Federated IAM for Marketplace |

---

## Related Documentation

- [Artifact Registry](../artifact-registry/README.md) — Tenant artifact storage
- [Workbench Management](../workbench-management/README.md) — Workbench resources
- [Platform Notifications](../platform-notifications/README.md) — Marketplace notifications
- [Marketplace Console](../../06-ux-architecture/tenant-domain/marketplace-console.md) — User interface
- [Hub Win Ops Center](../../06-ux-architecture/publisher-domain/hub-win-ops-center.md) — Publisher approval

