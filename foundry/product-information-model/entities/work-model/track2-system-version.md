# System Version

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction) — Artifact
**Owner:** Tech Lead, Integration Architect, SRE (for operational Systems)

## Definition

A **sealed, immutable package of Component Versions** — the composed and Component-integration-verified version of a System (Dim 5). System Version is the second tier of the three-tier versioning model: Component Version (atomic) → **System Version (composed)** → Product Version (complete). Once assembled and verified, a System Version is immutable; only deployment parameters may vary across environments via System Deployment Specifications (Track 3).

System Version is the **operational deployment unit** — what SRE deploys as a whole when they deploy "Payments System v3.1.0." It is not an atomic build artifact (that is Component Version) and not the complete product (that is Product Version). System Version captures which exact Component artifact versions work together within one System, validated by integration contracts and tests. See DR-036.

> **Build Track ownership for all Systems.** Product-facing Systems and SRE-operational Systems (probes, reconcilers, monitoring agents) alike produce System Versions through the Build Track. The `Purpose / Serving Persona(s)` field on the System entity (Dim 5) distinguishes who the System serves; the versioning model does not. See DR-036 D10.

> **Emergency gate profile.** System Versions assembled for P0 hotfixes may include Component Versions built under the `Emergency` gate profile. The System Version may be released with abbreviated verification when governed by Emergency Change procedures; deferred Component-level gates remain tracked on the originating Bug (DR-031).

## Purpose

Bridges atomic Component builds and Product-level certification. Without System Versions:

- Components are built independently, but their composition within a System is unverified — "payments-service v2.3.1 and payment-reconciler v1.4.0 work together" is a hope, not a fact
- SRE has no single versioned unit to deploy — "deploy payments-service" would deploy one Component without its co-deployed peers
- Integration contracts and binding configuration have no structured home
- Product Version would need to compose raw Component Versions — an unwieldy flat list across dozens of Components

System Version is where **Component integration verification** happens. Product Version is where **cross-System integration verification** happens.

## Fields

| Field | Type | Description |
|---|---|---|
| System | Reference (Dim 5) | Which System this version belongs to |
| Version | Semver | System-level semantic version (e.g., `3.1.0`) |
| Component Versions BOM | Map | Sealed map of Component → Component Version (e.g., `{payments-service: v2.3.1, payment-reconciler: v1.4.0, payment-notification-worker: v1.2.0}`) |
| Integration Contracts | List of Text/Reference | Validated API schemas, event schemas, data contracts between Components within this System |
| Integration Test Suite | Reference + Results | Integration test suite and pass/fail results for Component interoperability |
| Binding Configuration | Structured Config | Environment-independent wiring: service mesh routes, event topic bindings, protocol version selections, adapter activations, capability flags. Defines the **legal composition** of Component Versions within this System. Environment-specific operational parameters belong on System Deployment Specifications (Track 3). |
| Build Timestamp | DateTime | When assembly and verification completed |
| Gate Profile | Enum | `Standard` / `Emergency` — reflects whether any constituent Component Version used Emergency gates |
| Release Notes | Text | System-level changelog for this composition |
| Integration Epic | Reference (Track 2) | Integration Epic that produced this verification (if applicable) |

## Statuses

| Status | Description |
|---|---|
| Assembling | Component Versions are being identified, composed, and integration tests are running |
| Verified | All integration contracts validated; integration test suite passes; BOM is sealed |
| Released | System Version is immutable and available for Product Version composition and deployment |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Belongs to | System (Dim 5) | System Version is a versioned, integration-verified instance of a System |
| Composes | Component Version(s) (Track 2) | System Version seals specific Component Versions in its BOM |
| Composed into | Product Version (Track 2) | System Versions compose a Product Version |
| Described by | System Deployment Specification(s) (Track 3) | Environment-specific deployment is specified by System Deployment Specifications |
| Deployed by | Deployment Task (Track 3) | System Versions are deployed via System Deployment Specifications applied by Deployment Tasks |
| Produced by | Integration Epic / Integration Story (Track 2) | Integration work produces contracts and tests that verify the composition |
| Reflects in | Operational Readiness (Dim 7) | Released System Versions feed Operational Readiness assessment per environment |

## Example

### Payments System v3.1.0

```
Payments System v3.1.0
├── payments-service v2.3.1
├── payment-reconciler v1.4.0
└── payment-notification-worker v1.2.0

Integration Contracts:
  - payments-service ↔ payment-reconciler: settlement batch API v2 (validated)
  - payments-service → Kafka: payment.created event schema v3 (validated)
  - payment-notification-worker ← Kafka: payment.status.changed v2 (validated)

Integration Test Suite: 47 tests, 47 passed
Binding Configuration:
  - payments-service ↔ payment-reconciler: internal gRPC (service mesh route)
  - notification retry policy: exponential backoff, max 5 attempts
Status: Released
```

> **Binding Configuration and legal composition.** Binding configuration represents **scoped, deliberate** build-time choices — which adapter variant, which protocol version, which capability is activated. Not all combinations of Component Versions are valid. Environment-specific sizing, replicas, and secrets belong on the System Deployment Specification, not here.

---
