# Module Version

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction) — Output
**Owner:** Tech Lead, Developers, QA

## Definition

A versioned, quality-gated artifact of a specific module, continuously produced by CI/CD pipelines. Module Versions are *results* of engineering progress, not planned entities — they are routinely and continuously incremented as code flows through the pipeline. A Module Version with status `Released` has passed all quality gates and is available for deployment.

## Purpose

Module Versions are the fundamental output of the Build Track. Each module in the product has its own CI/CD pipeline producing its own versions continuously. The term follows DevOps convention — a "released" Module Version is a versioned build that has passed quality gates. This is distinct from a Customer Release, which is the business act of making functionality available to customers (see FAQ Q12).

Composite artifacts (like Product Version) may refer to constituent Module Versions using **semver compatibility ranges** rather than pinned specific versions — e.g., `^2.3.0` (any compatible 2.x.x) rather than `2.3.3`. This follows standard dependency management conventions.

## Fields

| Field | Type | Description |
|---|---|---|
| Module | Reference | The module (Dim 8) this version belongs to |
| Version | Semver | Semantic version number (e.g., `2.3.3`) |
| Build Timestamp | DateTime | When the artifact was produced |
| Artifact URI | String | Location in the artifact registry |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Building | Code in progress, CI pipeline running |
| Released | All quality gates passed — artifact available for deployment in the artifact registry |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Belongs to | Module / Domain (Dim 8) | Module Version is a versioned artifact of a Module |
| Composed into | Product Version (Track 2) | Module Versions compose a Product Version (via BOM) |
| Deployed by | Deployment (Track 3) | Module Versions are deployed to environments by the Run Track |
| Traces to | Epic (Track 2) | Module Versions contain completed Epics/Stories |

## Example

`payments-service v2.3.3`, `fx-engine v1.8.1`, `merchant-portal v4.1.1`.
