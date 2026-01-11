# Blueprints and Packages

> **Status:** 🟡 WIP — Design Complete

This document describes the Hub Package model, BlueprintSpec types, and the package-manifest-container format used in the Marketplace subsystem.

---

## Overview

| Concept | Description |
|---------|-------------|
| **Hub Package** | Atomic unit of publishing; a self-sufficient collection of Blueprints |
| **Blueprint** | Definition/Specification exported for distribution |
| **BlueprintSpec** | CRD type for subscribed Blueprints |
| **Package Manifest** | Metadata file describing package contents and visibility |
| **Package-Manifest-Container** | OCI container holding all CRDs and manifest for a package |

---

## Hub Package

A **Hub Package** is the atomic unit of publishing to the Marketplace. It represents a self-sufficient, cohesive collection of Blueprints that can be discovered, subscribed to, and deployed.

### Package Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Self-sufficient** | Contains all required artifacts (no external package dependencies) |
| **Cohesive** | Related artifacts bundled together logically |
| **Versioned** | Follows semantic versioning (MAJOR.MINOR.PATCH) |
| **Signed** | Publisher signature for integrity verification |
| **Immutable** | Once published, package version cannot be modified |

### Package Content Types

A Hub Package can contain Blueprints of these types:

| Type | Description |
|------|-------------|
| **Scenario Blueprints** | Complete scenarios with normative, automation, and deployment specs (includes Trained Agents) |
| **Workbench Blueprints** | Workbench templates with scenarios and configurations |
| **Machine Blueprints** | Machine definitions for external system integration |
| **Tools Blueprints** | Standalone tool definitions |
| **Raw Agents Blueprints** | Raw agent specifications |
| **Hub Application Blueprints** | Reusable application containers with build recipes (DSL runtimes, interpreters) |
| **Mixed** | Combination of the above types |

### Package Dependencies

- Packages **can reference** platform-provided resources (e.g., platform Machine Definitions)
- Packages **cannot reference** resources from other packages
- All resources from a package are **isolated** to that package-subscription scope
- No shared resources between packages

---

## Blueprints

**Blueprints** are definitions/specifications exported for distribution. The term distinguishes:

| Term | Context | Description |
|------|---------|-------------|
| **Specification** | Workbench | Normative resource deployed and active in a workbench |
| **Blueprint** | Marketplace | Candidate specification that can be adopted/deployed |

### Blueprint Types

When specifications are exported to a package, their CRD types transform to corresponding BlueprintSpec types:

| Source Specification | BlueprintSpec Type |
|---------------------|-------------------|
| `ScenarioNormativeSpec` | `ScenarioBlueprintSpec` |
| `ScenarioAutomationSpec` | (included with Scenario) |
| `WorkbenchSpec` | `WorkbenchBlueprintSpec` |
| `MachineDefinitionSpec` | `MachineBlueprintSpec` |
| `ToolDefinitionSpec` | `ToolBlueprintSpec` |
| `RawAgentSpec` | `RawAgentBlueprintSpec` |
| `HubApplicationSpec` | `HubApplicationBlueprintSpec` |

> **Note:** `HubApplicationBlueprintSpec` includes a **Build Recipe** that defines how subscriber-provided files are combined with the base container. See [Hub Application Blueprints](./hub-application-blueprints.md) for details.

---

## BlueprintSpec Model

When a package is subscribed to, BlueprintSpecs become **usable** in the workbench but are not directly part of the workbench definition.

### BlueprintSpec Lifecycle

```
1. SUBSCRIPTION
   └── BlueprintSpecs become available in workbench
   └── Not yet used; just available for reference

2. DERIVED RESOURCE CREATION
   └── User creates regular specs from BlueprintSpecs
   └── e.g., ScenarioBlueprintSpec → ScenarioNormativeSpec
   └── Blueprint reference section added to derived resource

3. DEPLOYMENT
   └── Derived resources deployed as normal
   └── Containers cloned on first deployment (lazy cloning)
```

### Blueprint Reference Section

Derived resources include a reference section linking back to the source Blueprint:

```yaml
blueprintReference:
  packageSha: "sha256:abc123..."     # Package integrity hash
  packageUri: "marketplace://packages/dispute-ops-v1.2.0"
  blueprintName: "dispute-triage"
  blueprintType: "ScenarioBlueprintSpec"
  packageVersion: "1.2.0"
```

This enables:
- Update tracking from later Blueprint versions
- Divergence detection (if derived resource is modified)
- Provenance and audit

### Derived Resource States

| State | Description |
|-------|-------------|
| **Synced** | Derived resource matches current Blueprint version |
| **Update Available** | Newer Blueprint version available |
| **Divergent** | Derived resource modified after creation |
| **Out-of-Sync** | User chose not to update; tracked but not enforced |
| **Orphaned** | Blueprint withdrawn; derived resource still works |

---

## Package Manifest CRD

Developers create a **Package Manifest CRD** to define what goes into a package.

### CRD Structure

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: PackageManifest
metadata:
  name: dispute-ops-package
  namespace: acme-dev

spec:
  # Package Identity
  packageName: "Dispute Operations Suite"
  version: "1.2.0"
  
  # Product Information
  shortDescription: "Complete dispute resolution automation"
  longDescription: |
    Comprehensive dispute resolution suite including...
  
  # Publisher Information (from subscription)
  # Automatically populated from registered publisher
  
  # Package Contents (references to specifications)
  blueprints:
    scenarios:
      - name: dispute-triage
      - name: dispute-resolution
    tools:
      - name: card-network-lookup
  
  # Visibility Controls
  visibility:
    mode: "restricted"  # public | restricted | private
    tenantAllowList:
      - "tenant-partner-bank"
    regionAllowList:
      - "us-east-1"
      - "eu-west-1"
  
  # Categorization
  categories:
    - "dispute-resolution"
    - "customer-service"
  industryTags:
    - "financial-services"
  keywords:
    - "disputes"
    - "chargebacks"
```

### Associated Children

When a Package Manifest references a Scenario, all associated children are **automatically included**:
- Hub Applications
- Triggers
- Notification templates
- Task queue configurations
- Tool bindings
- Migration CRDs

Publishers don't need to explicitly list these — the publishing flow includes them automatically.

---

## Package Manifest (Published)

The published package manifest is extracted from the CRD and stored in the package-manifest-container.

### Required Fields

| Field | Description |
|-------|-------------|
| `package_id` | Unique identifier (immutable) |
| `package_name` | Display name |
| `version` | Semver version |
| `package_uri` | Package location URI |
| `short_description` | Brief description (max 200 chars) |
| `artifact_types` | Types of artifacts included |
| `publisher_id` | Publisher subscription ID |
| `publisher_name` | Publisher display name |
| `blueprints` | List of BlueprintSpecs |
| `package_sha` | SHA-256 hash for integrity |
| `visibility_mode` | public / restricted / private |
| `published_date` | Publication timestamp |
| `status` | published / deprecated / withdrawn |
| `publisher_signature` | Publisher's signature |

### Optional Fields

| Category | Fields |
|----------|--------|
| **Product Info** | long_description, release_notes, keywords, categories, industry_tags |
| **Publisher Info** | contact_email, website, support_info, logo_uri |
| **Deployment** | deployment_instructions, system_requirements, prerequisites |
| **Documentation** | documentation_uri, screenshot_uris, video_uri, readme_uri |
| **Compliance** | compliance_certifications, security_notes, license_type |

→ See [Package Manifest Reference](../../10-guides/package-manifest-reference.md) for complete field documentation.

---

## Package-Manifest-Container

All non-container resources for a package are bundled into a single **OCI container** called the package-manifest-container.

### Contents

```
package-manifest-container/
├── manifest.yaml           # Package manifest file
├── blueprints/
│   ├── scenario-triage.yaml
│   ├── scenario-resolution.yaml
│   └── tool-card-lookup.yaml
└── metadata/
    └── signatures.json
```

### Characteristics

| Aspect | Description |
|--------|-------------|
| **Format** | OCI container |
| **Contents** | All CRDs + package manifest |
| **One per package** | Single container per package version |
| **Signed** | Publisher signature + Marketplace signature |
| **Immutable** | Cannot be modified after publication |

---

## Storage Model

### Marketplace Artifact Repository

| Artifact Type | Storage |
|---------------|---------|
| **Containers** | Stored individually with hash-based deduplication |
| **Package-Manifest-Container** | One per package version |
| **Catalog Index** | OpenSearch (extracted manifest data) |

### Container Deduplication

- Each container image has a unique SHA-256 hash
- Unchanged containers are not duplicated (reference existing if hash matches)
- Hash included in package manifest for verification
- Optimizes storage for shared/common base images

---

## Related Documentation

- [Marketplace Artifact Repository](./marketplace-artifact-repository.md) — Storage details
- [Publishing Services](./publishing-services.md) — Publishing workflow
- [Subscription Services](./subscription-services.md) — Subscription model
- [ADR-0094: Hub Package as Atomic Publishing Unit](../../decision-logs/0094-hub-package-atomic-unit.md)
- [ADR-0095: BlueprintSpec Transformation Model](../../decision-logs/0095-blueprintspec-transformation.md)

