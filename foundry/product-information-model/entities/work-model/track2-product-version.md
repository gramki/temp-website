# Product Version

**Model:** Work Model
**Track:** Build — Artifact
**Owner:** Tech Lead, Release Engineering

## Definition

The **highest-order composition** in the versioning model — a certified composition of System Versions representing the full product. Product Version is the third and final tier: Component Version (atomic) → System Version (composed) → **Product Version (complete)**. Product Version assembly is the **cross-System integration verification** point — end-to-end user journeys, cross-System workflows, and product-wide compliance posture are validated here.

Product Versions are results of integration and certification work, not planned entities. They emerge when System Versions are composed and pass end-to-end certification. See DR-036.

> **Product Version as ubiquitous language.** Product Version is the shared vocabulary across all teams and external stakeholders. Win teams reference it in support cases: "customer X is running v4.0.0." Release Notes are written against it. Compliance certifies it. Customers identify what they're running. Component Version is Build engineering language; System Version is Build + Run language; Product Version is the lingua franca for cross-team and customer-facing communication.

> **Composes System Versions directly — no Module Version tier.** Product Version references System Versions, not Module Versions or Component Versions directly. Module (Structural) remains the functional boundary customers recognize ("Payments Module"), but traceability flows Module → System (Technical) → System Version in the Product Version BOM. Module is not an operational versioning tier. See DR-036 D3, D12.

> **"Highest-order composition" uses "composition" in the systems-thinking sense.** Product Version is not a System entity (Technical). It is a whole composed of interacting System Versions with emergent product-level properties that do not exist at the System or Component level.

## Purpose

In multi-System products, individual Systems have their own version streams. Without a Product Version:

1. **Composition integrity:** No way to know which System Versions are certified together.
2. **Certification:** Individual System Versions are integration-verified within their System, but the full product composition is not — cross-System failures go undetected.
3. **Documentation:** Technical docs cannot reference "Product v4.0.0" — they'd have to list every System Version.
4. **Reproducibility:** "What exactly was running in production on Feb 1?" requires reconstructing from deployment logs across Systems.
5. **Cross-team communication:** Build, Run, Win, and customer-facing teams have no common reference for the product.
6. **Emergent product-level properties:** End-to-end user journeys and product-wide compliance posture have no entity to attach to.

Product Version solves these by providing a certified System Versions BOM and a shared vocabulary.

## Fields

| Field | Type | Description |
|---|---|---|
| Version | Semver | Product-level semantic version (e.g., `4.0.0`) |
| System Versions BOM | Map | Specific System Versions certified together (e.g., `{payments-system: v3.1.0, fx-system: v2.0.1, compliance-system: v3.2.0, bank-connectivity-system: v1.6.0, customer-portal-system: v2.1.0}`) |
| End-to-End Test Suite | Reference + Results | Cross-System end-to-end test suite and results for this composition |
| Certification Date | DateTime | When the composition was certified |
| Compatibility Notes | Text | External dependency compatibility (e.g., "requires Java 21+, PostgreSQL 15+") |
| Release Notes | Text | Product-level changelog aggregated from constituent System Versions |

## Statuses

| Status | Description |
|---|---|
| Assembling | System Versions being identified and composed |
| Verified | Cross-System end-to-end integration tests pass for this composition |
| Certified | All quality gates, compliance, and security checks pass — ready for deployment via Product Deployment Specification |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Composes | System Version(s) (Build) | Product Version composes System Versions via BOM |
| Instantiated from | Product Specification (Technical) | Product Version is the Work Model instance of the Product Specification's System composition |
| Described by | Product Deployment Specification(s) (Run) | Environment-specific full-product deployment is specified by Product Deployment Specifications |
| Referenced by | Customer Release Intent (Strategy) | Customer Release Intents reference Product Version(s) |
| Supersedes | Product Version (Build) | Each Product Version supersedes the previous |

## Example

### Product v4.0.0 — flat System Versions BOM

```
Product v4.0.0
├── payments-system v3.1.0
│   ├── payments-service v2.3.1
│   ├── payment-reconciler v1.4.0
│   └── payment-notification-worker v1.2.0
├── fx-system v2.0.1
│   ├── fx-engine v1.8.1
│   └── fx-rate-cache v1.2.0
├── compliance-system v3.2.0
│   ├── compliance-service v3.1.1
│   └── ofac-screening-adapter v1.0.4
├── bank-connectivity-system v1.6.0
│   ├── bank-adapter v1.5.2
│   └── bank-file-generator v1.3.0
├── customer-portal-system v2.1.0
│   ├── portal-web-app v3.0.0
│   └── portal-bff v2.1.0
└── payments-monitoring-system v1.2.0        ← operational System (SRE-owned)
    ├── payments-healthcheck v1.2.0
    └── payments-dashboard-agent v1.1.0

End-to-End Test Suite: 128 tests, 128 passed
Certification Date: 2026-05-15T18:00:00Z
Status: Certified
```

Capability traceability example: **Real-Time FX Rate Lock** (Capability, Structural) → FX Module (Structural) → fx-system (Technical) → fx-system v2.0.1 in Product v4.0.0 BOM. No Module Version entity is required.

---
