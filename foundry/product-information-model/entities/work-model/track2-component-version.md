# Component Version

**Model:** Work Model
**Track:** Build — Artifact
**Owner:** Tech Lead, Developers, QA

## Definition

A versioned, quality-gated build artifact of a single Component (Technical) — the container image, Lambda package, frontend bundle, or equivalent deployable produced by that Component's CI/CD pipeline. Component Versions are *results* of engineering progress, not planned entities; they are routinely and continuously incremented as Technical Tasks flow through the pipeline. A Component Version with status `Released` has passed all quality gates and is available for assembly into a System Version.

Component Version is the **atomic build artifact** — the first tier of the three-tier versioning model: **Component Version** (atomic) → System Version (composed, sealed BOM) → Product Version (complete product composition). See DR-036.

> **Emergency gate profile.** Component Versions produced for P0 Bugs (typically Run-provenance SEV-0/SEV-1 Incidents) may use the `Emergency` gate profile, which requires only peer review, security scan, and smoke tests — deferring full regression suite, performance benchmarks, and static analysis. The deferred gates must be passed by a subsequent Standard Component Version; the originating Bug tracks this obligation via its `Deferred Gate Obligation` field (see DR-031 D2, D3).

## Purpose

Captures the atomic output of Build Track work at Component granularity. Without Component Versions:

- CI/CD pipelines have no UPIM anchor for artifact registry entries and image tags
- System Version has no constituent parts to seal into a BOM
- Quality gate results have no structured home at the atomic tier
- Technical Tasks and Bug fixes have no versioned artifact to attach to

**Quality gate fields on Component Version feed System Version assembly and Operational Readiness (Operational).** When Component Versions are composed into a released System Version, their quality gate results contribute to the System's operational acceptance assessment in each Deployment Environment.

## Fields

| Field | Type | Description |
|---|---|---|
| Component | Reference (Technical) | Which Component this version belongs to |
| Version | Semver | Semantic version number (e.g., `2.3.1`) |
| Build Timestamp | DateTime | When the artifact was produced |
| Artifact URI | String | Location in the artifact registry (e.g., `ghcr.io/org/payments-service:2.3.1`) |
| Git Reference | String | Commit SHA or tag |
| Quality Gate — Test Coverage | Percentage | Code coverage from automated tests |
| Quality Gate — Tests Passed | Boolean + Count | All tests pass; total count |
| Quality Gate — Security Scan | Enum + Text | `Pass` / `Fail` / `Warnings`; findings summary |
| Quality Gate — Performance Benchmark | Text | Latency, throughput, resource benchmarks vs. baseline |
| Quality Gate — Static Analysis | Enum + Text | `Pass` / `Fail`; code quality findings |
| Quality Gate — Dependency Audit | Enum + Text | `Pass` / `Fail`; known vulnerabilities in dependencies |
| Gate Profile | Enum | `Standard` / `Emergency`. Standard = all gates required. Emergency = peer review + security scan + smoke tests required; full regression + performance benchmarks + static analysis deferred. See DR-031 D2. |
| Release Notes | Text | What changed — features, fixes, breaking changes |
| Included Work | List of References (Build) | Technical Tasks, Bug fixes included in this version |

## Statuses

| Status | Description |
|---|---|
| Building | Code in progress, CI pipeline running |
| Released | All quality gates passed — artifact available in the artifact registry for System Version assembly |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Belongs to | Component (Technical) | Component Version is a versioned artifact of a Component |
| Composed into | System Version (Build) | Component Versions are sealed into a System Version BOM |
| Contains | Technical Task(s) (Build) | Component Version includes completed Technical Tasks |
| Contains | Bug fix(es) (Build) | Component Version includes Bug fixes |
| Reflects in | Operational Readiness (Operational) | Quality gate results contribute when composed into a released System Version |

## Example

| Component | Version | Tests | Security | Performance | Status |
|---|---|---|---|---|---|
| payments-service | v2.3.1 | 94% coverage, 1,247 tests pass | Pass (0 critical, 2 low) | p99 < 180ms (baseline: 200ms) | Released |
| payment-reconciler | v1.4.0 | 88% coverage, 312 tests pass | Pass | Batch: 10K records/min (baseline: 8K) | Released |
| payment-notification-worker | v1.2.0 | 91% coverage, 428 tests pass | Pass | Consumer lag < 5s | Released |
| fx-engine | v1.8.1 | 91% coverage, 832 tests pass | Pass | p99 < 45ms (baseline: 50ms) | Released |
| portal-web-app | v3.0.0 | 87% coverage, 956 tests pass | Pass | LCP < 2.1s | Building |

---
