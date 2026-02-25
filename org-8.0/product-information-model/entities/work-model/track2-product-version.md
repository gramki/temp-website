# Product Version

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction) — Artifact
**Owner:** Tech Lead, Release Engineering

## Definition

The **highest-order composite system** in the versioning model — a certified composition of compatible Module Versions representing the full product. A Product Version has its own emergent properties (end-to-end user journeys, cross-module workflows, product-wide availability and compliance posture) that do not exist at the Module or System level. It declares compatible version ranges for constituent Module Versions (Declared BOM) and records the specific Module Versions tested together (Resolved BOM). Product Versions are the third and final tier of the three-tier versioning model: System Version (atomic deployment) → Module Version (integrated deployment + integration verification) → **Product Version (complete deployment + certification)**. Product Version is the **complete deployment unit** — the Run Track enriches it with Module Package Versions and cross-module operational wiring to produce a Product Package Version (environment-independent), which is deployed via PDDs (Product Deployment Descriptors). See DR-026, DR-027, DR-028, DR-029.

Product Versions are results of integration and certification work, not planned entities. They emerge when Module Versions are composed and pass end-to-end certification.

> **Product Version as ubiquitous language.** Product Version is the shared vocabulary across *all* teams and external stakeholders. Win teams reference it in support cases: "customer X is running v3.2." Release Notes are written against it. Compliance certifies it. Customers identify what they're running. System Version is Build+Run language; Module Version bridges Build+Run+Product; Product Version is the lingua franca that enables cross-team and customer-facing communication. Without Product Version, "what is the customer running?" requires reconstructing from deployment logs across dozens of Systems.
>
> **Composes Module Versions, not System Versions:** Product Version references Module Versions, not System Versions directly. Each Module Version is itself a composite system — a verified composition of System Versions. This two-level indirection (Product Version → Module Version → System Version) reflects reality: a product is composed of functional Modules (Dim 8), each Module is implemented by Systems (Dim 5), and each System produces versioned artifacts. See DR-026.
>
> **"Highest-order composite system" uses "system" in the systems-thinking sense.** Product Version is not a System entity (Dim 5). It is a system in the generic sense: a whole composed of interacting Module Versions with emergent product-level properties (end-to-end user journeys, cross-module workflows, product-wide availability and compliance posture) that do not exist at the Module or System level. Product Version operates at the **Complete** composition level — the highest tier in the Atomic → Integrated → Complete hierarchy. See FAQ Q93.

## Purpose

In multi-module products, individual Modules have their own version streams. Without a Product Version:

1. **Composition integrity:** No way to know which Module Versions are compatible with each other.
2. **Certification:** Individual Module Versions are integration-verified, but the full product composition is not — cross-Module failures go undetected.
3. **Documentation:** Technical docs cannot reference "Product v3.2" — they'd have to list every Module Version (which in turn lists every System Version).
4. **Reproducibility:** "What exactly was running in production on Feb 1?" requires reconstructing from deployment logs across Systems and Modules.
5. **Cross-team communication:** Build, Run, Win, and customer-facing teams have no common reference for the product — engineers say service names, PMs say module names, Win teams say feature names, and customers say "that thing that broke last week."
6. **Emergent product-level properties:** End-to-end user journeys, cross-module workflows, and product-wide compliance posture have no entity to attach to.

Product Version solves these by providing a certified BOM and a shared vocabulary — analogous to a lock file in dependency management (see FAQ Q14).

## Fields

| Field | Type | Description |
|---|---|---|
| Version | Semver | Product-level semantic version (e.g., `3.2.0`) |
| Declared BOM | Map | Compatible version ranges per Module Version (e.g., `Payments Module ^2.3.0`, `FX Module ~1.8.0`) |
| Resolved BOM | Map | Specific Module Versions certified together (e.g., `Payments Module v2.3.0 = {payments-service v2.3.3, payment-gateway v1.2.1}`) |
| End-to-End Test Suite | Reference + Results | End-to-end test suite and results for this composition |
| Certification Date | DateTime | When the composition was certified |
| Compatibility Notes | Text | External dependency compatibility (e.g., "requires Java 21+, PostgreSQL 15+") |
| Release Notes | Text | Product-level changelog aggregated from Module Versions |

## Statuses

| Status | Description |
|---|---|
| Assembling | Module Versions being identified and composed |
| Verified | End-to-end integration tests pass for this composition |
| Certified | All quality gates, compliance, and security checks pass |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Composes | Module Version(s) (Track 2) | Product Version composes Module Versions via BOM |
| Enriched into | Product Package Version (Track 3) | Run Track enriches Product Version with Module Package Versions and cross-module operational wiring to produce a Product Package Version (environment-independent), which instantiates a Product Package specification (Dim 7) |
| Referenced by | Customer Release (Dim 1) | Customer Releases reference Product Version(s) |
| Supersedes | Product Version (Track 2) | Each Product Version supersedes the previous |

## Examples

### Resolved BOM Example

```
Product v3.2.0
├── Payments Module v2.3.0
│   ├── payments-service v2.3.3
│   └── payment-gateway v1.2.1
├── FX Module v1.8.0
│   ├── fx-service v1.8.1
│   └── fx-calculator v1.8.0
├── Compliance Module v3.1.0
│   └── compliance-service v3.1.1
└── Settlement Module v1.5.0
    ├── settlement-service v1.5.2
    └── bank-adapter v1.5.2
```

Declared BOM: `{Payments Module ^2.3.0, FX Module ~1.8.0, Compliance Module >=3.1.0 <4.0.0, Settlement Module ~1.5.0}`

---
