# Module Version

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction) — Artifact
**Owner:** Tech Lead, Integration Architect

## Definition

A **composite system** — an integration-verified composition of System Versions for a Module (Dim 8). Module Version is not merely a verification record; it is a system in its own right, with emergent operational properties (end-to-end latency across the Module's Systems, integrated failure modes, cross-system data consistency) that do not exist at the individual System level. Module Version is the second tier of the three-tier versioning model: System Version (atomic deployment) → **Module Version (integrated deployment + integration verification)** → Product Version (complete deployment + certification). Module Version is the **integrated deployment unit** — the Run Track enriches it with operational System Versions and configuration to produce a Module Package, which is deployed to environments. See DR-026, DR-027.

A Module Version contains:
- **System Versions** — the specific versions of each System that implements this Module
- **Integration contracts** — validated API schemas, event schemas, data contracts between those Systems
- **Integration test suite** — the test suite that verified interoperability between those Systems

Module Versions are *artifacts* produced by verified Integration Epics and Integration Stories. They are not planned entities — they emerge when the Systems composing a Module are verified to work together.

> **Module Version as communication bridge.** Module Version serves as the shared vocabulary between Build, Run, and Product teams. Product managers reason in Modules: "Payments capability v4.1 includes the new compliance flow." SREs monitor integrated capability health: "Payments Module v4.1 is healthy in LATAM." Build teams know which Systems compose it: "Payments Module v4.1 = {payments-service v2.3.3, payment-gateway v1.2.1}." Without Module Version, these teams have no common reference point — engineers speak System names, PMs speak feature names, and SREs translate between the two ad hoc.
>
> **Module Version is NOT the old "Module Version" (renamed to System Version).** The previous "Module Version" was a versioned artifact of a single deployable unit — that is now **System Version**. This new Module Version is a *composition* artifact — a composite system that proves multiple System Versions integrate correctly within a Module boundary. See DR-026.
>
> **"Composite system" uses "system" in the systems-thinking sense.** When we say Module Version is a "composite system," we do not mean it is a System entity (Dim 5). We mean it is a system in the generic sense: a whole composed of interacting parts (System Versions) with emergent properties (end-to-end latency, integrated failure modes, cross-system data consistency) that do not exist at the individual System level. Module Version operates at the **Integrated** composition level — between the Atomic level (individual Systems) and the Complete level (Product). See FAQ Q93.

## Purpose

Bridges the gap between individual System Versions and the Product Version — as both a verified composition and a shared vocabulary. Without Module Versions:
- System Versions are deployed independently, but their integration is unverified — "payments-service v2.3.3 and fx-service v1.8.1 work together" is a hope, not a fact
- Product Version has to verify all Systems at once — an O(n²) integration problem instead of Module-scoped verification
- Integration test results have no structured home — they exist in CI logs but not in the model
- The functional boundary (Module, Dim 8) has no versioned integration artifact
- Build, Run, and Product teams have no shared reference point for a capability — engineers say "payments-service v2.3.3," PMs say "the Payments capability," and SREs translate between the two informally
- Emergent operational properties (end-to-end latency, integrated failure modes, cross-system data consistency) have no entity to attach to — they exist as Module-level phenomena but are tracked only at the System level

## Fields

| Field | Type | Description |
|---|---|---|
| Module | Reference (Dim 8) | Which Module this version represents |
| Version | Semver | Module-level version (e.g., `2.3.0`) |
| System Versions | Map | Specific System Versions composing this Module Version (e.g., `{payments-service: v2.3.3, payment-gateway: v1.2.1}`) |
| Integration Contracts | List of Text/Reference | Validated API schemas, event schemas, data contracts |
| Integration Test Suite | Reference + Results | Integration test suite and pass/fail results |
| Binding Configuration | Structured Config | The wiring and composition constraints that make this composition operational: service mesh routes, event topic bindings, orchestration definitions, adapter selections, protocol version bindings, and capability activation flags. Defines the **legal composition** — which combinations of System Versions are valid, which capabilities are activated, and what behavior is expected. Environment-independent (environment-specific configuration is applied at Module Package level by the Run Track). |
| Verification Date | DateTime | When integration verification completed |
| Integration Epic | Reference (Track 2) | Integration Epic that produced this verification (if applicable) |

## Statuses

| Status | Description |
|---|---|
| Integrating | System Versions are being composed and integration tests are running |
| Verified | All integration contracts validated; integration test suite passes |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Composes | System Version(s) (Track 2) | Module Version composes specific System Versions |
| Represents | Module (Dim 8) | Module Version is a versioned, integration-verified instance of a Module |
| Produced by | Integration Epic (Track 2) | Integration Epic work produces Module Version verification |
| Produced by | Integration Story(ies) (Track 2) | Integration Stories contribute contracts and tests |
| Composed into | Product Version (Track 2) | Module Versions compose a Product Version |
| Enriched into | Module Package (Track 3) | Run Track enriches Module Version with operational System Versions and configuration to produce a Module Package |

## Examples

### Payments Module v2.3.0

```
Payments Module v2.3.0
├── payments-service v2.3.3
└── payment-gateway v1.2.1

Integration Contracts:
  - payments-service ↔ payment-gateway: gRPC PaymentProcessing v2 (validated)
  - payments-service → Kafka: payment.created event schema v3 (validated)

Integration Test Suite: 47 tests, 47 passed
Verification Date: 2026-02-10T14:30:00Z
```

### FX Module v1.8.0

```
FX Module v1.8.0
├── fx-service v1.8.1
└── fx-calculator v1.8.0

Integration Contracts:
  - fx-service ↔ fx-calculator: internal rate calculation API (validated)
  - fx-service → gRPC: GetRate, LockRate, UnlockRate endpoints (validated)

Integration Test Suite: 31 tests, 31 passed
Verification Date: 2026-02-11T09:15:00Z

Binding Configuration:
  - fx-service ↔ fx-calculator: internal gRPC (service mesh route)
  - fx-service rate-provider adapter: "provider-x-adapter" selected (not "provider-y-adapter")
  - rate-lock capability: ENABLED (24-hour lock with auto-release)
```

> **Binding Configuration and legal composition.** Module Version's binding configuration is not mere wiring — it represents **scoped, constrained, and deliberate** build-time choices. When the Build Track composes System Versions into a Module Version, it determines: which adapter variant to include (e.g., provider-x-adapter, not provider-y), which protocol version to bind (gRPC v2, not v1), which capability to activate (rate-lock enabled, batch disabled). Not all possible combinations of System Versions are valid — some are incompatible, some would produce unexpected functionality, some would violate regulatory constraints. The binding configuration constrains the composition to its **legal form**: the set of choices that make this composition intended, tested, and safe. This is analogous to compile-time feature flags or conditional dependency inclusion — the composition is a deliberate selection, not an unconstrained assembly. Environment-specific operational configuration (which environment to target, which probes to attach, which monitoring thresholds to set) is handled separately at the Module Package level by the Run Track.

---
