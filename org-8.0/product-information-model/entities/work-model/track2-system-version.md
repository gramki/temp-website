# System Version

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction) — Artifact
**Owner:** Tech Lead, Developers, QA

## Definition

A versioned, quality-gated artifact of a single System (Dim 5), continuously produced by CI/CD pipelines. System Versions are *results* of engineering progress, not planned entities — they are routinely and continuously incremented as Technical Tasks flow through the pipeline. A System Version with status `Released` has passed all quality gates and is available for deployment.

System Version is the **atomic deployment unit** — the Run Track deploys System Versions to Deployment Environments (Dim 7). It is the first tier of the three-tier versioning model: System Version (atomic deployment) → Module Version (integrated deployment + integration verification) → Product Version (complete deployment + certification). Module Version and Product Version are also deployable (via Module Package and Product Package, enriched by the Run Track), but System Version is the atomic, independently deployable unit. See DR-026, DR-027.

> **Renamed from Module Version:** The Build Track builds Systems (Dim 5), not Modules (Dim 8). Engineers produce `payments-service v2.3.3` (a System Version), not "Payments Module v2.3.3." Modules are functional boundaries (Dim 8); Systems are the deployable technical units (Dim 5). The many-to-many System-to-Module mapping means a single System Version may contribute to multiple Module Versions.

## Purpose

Captures the deployable output of Build Track work. Without System Versions:
- There is no versioned artifact to deploy — "deploy to production" has no artifact reference
- Quality gate results have no structured home — test coverage, security scan, performance benchmarks are untracked
- Module Version (integration tier) has no constituent parts to compose
- Operational Readiness (Dim 7) has no build-quality data to assess against

**Quality gate fields on System Version reflect in Operational Readiness (Dim 7).** When a System Version is released, its quality gate results feed the Operational Readiness assessment for the System in each Deployment Environment. This connects Build Track output quality to Run Track operational acceptance.

## Fields

| Field | Type | Description |
|---|---|---|
| System | Reference (Dim 5) | Which System this version belongs to |
| Version | Semver | Semantic version number (e.g., `2.3.3`) |
| Build Timestamp | DateTime | When the artifact was produced |
| Artifact URI | String | Location in the artifact registry |
| Git Reference | String | Commit SHA or tag |
| Quality Gate — Test Coverage | Percentage | Code coverage from automated tests |
| Quality Gate — Tests Passed | Boolean + Count | All tests pass; total count |
| Quality Gate — Security Scan | Enum + Text | `Pass` / `Fail` / `Warnings`; findings summary |
| Quality Gate — Performance Benchmark | Text | Latency, throughput, resource benchmarks vs. baseline |
| Quality Gate — Static Analysis | Enum + Text | `Pass` / `Fail`; code quality findings |
| Quality Gate — Dependency Audit | Enum + Text | `Pass` / `Fail`; known vulnerabilities in dependencies |
| Release Notes | Text | What changed — features, fixes, breaking changes |
| Included Work | List of References (Track 2) | Technical Tasks, Bug fixes included in this version |

## Statuses

| Status | Description |
|---|---|
| Building | Code in progress, CI pipeline running |
| Released | All quality gates passed — artifact available for deployment in the artifact registry |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Belongs to | System (Dim 5) | System Version is a versioned artifact of a System |
| Composed into | Module Version (Track 2) | System Versions compose a Module Version (integration verification) |
| Deployed by | Deployment (Track 3) | System Versions are deployed to environments by the Run Track |
| Contains | Technical Task(s) (Track 2) | System Version includes completed Technical Tasks |
| Contains | Bug fix(es) (Track 2) | System Version includes Bug fixes |
| Reflects in | Operational Readiness (Dim 7) | Quality gate results feed Operational Readiness assessment |

## Examples

| System | Version | Tests | Security | Performance | Status |
|---|---|---|---|---|---|
| payments-service | v2.3.3 | 94% coverage, 1,247 tests pass | Pass (0 critical, 2 low) | p99 < 180ms (baseline: 200ms) | Released |
| fx-service | v1.8.1 | 91% coverage, 832 tests pass | Pass | p99 < 45ms (baseline: 50ms) | Released |
| bank-adapter | v1.5.2 | 88% coverage, 456 tests pass | Warnings (1 medium — dependency update scheduled) | Batch: 10K records/min (baseline: 8K) | Released |
| compliance-service | v3.1.1 | 96% coverage, 1,102 tests pass | Pass | p99 < 120ms | Building |

---
