# Product Version

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction) — Output
**Owner:** Tech Lead, Release Engineering

## Definition

A verified, certified composition of compatible Module Versions — the Bill of Materials (BOM) for the product at a specific point. A Product Version declares compatible version ranges for constituent modules (Declared BOM) and records the specific versions tested together (Resolved BOM). Like Module Versions, Product Versions are results of build and integration work, not planned entities.

## Purpose

In multi-module products, individual modules have their own version streams. Without a Product Version, the following problems arise:

1. **Composition integrity:** No way to know which Module Versions are compatible with each other.
2. **Certification:** Individual modules are verified, but the composition is not — integration failures go undetected.
3. **Documentation:** Technical docs cannot reference "Product v3.2" for dependency compatibility — they'd have to list every Module Version.
4. **Reproducibility:** "What exactly was running in production on Feb 1?" requires reconstructing from deployment logs across modules.

Product Version solves these by providing a certified BOM — analogous to a lock file in dependency management (see FAQ Q14).

## Fields

| Field | Type | Description |
|---|---|---|
| Version | Semver | Product-level semantic version (e.g., `3.2.0`) |
| Declared BOM | Map | Compatible version ranges per module (e.g., `payments-service ^2.3.0`, `fx-engine ~1.8.0`) |
| Resolved BOM | Map | Specific Module Versions tested and certified together |
| Certification Date | DateTime | When the composition was certified |
| Compatibility Notes | Text | External dependency compatibility (e.g., "requires Java 21+, PostgreSQL 15+") |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Assembling | Module Versions being identified and composed |
| Verified | Integration tests pass for this composition |
| Certified | All quality gates, compliance, and security checks pass |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Composes | Module Version (Track 2) | Product Version composes Module Versions via BOM (compatibility ranges) |
| Referenced by | Customer Release (Dim 1) | Customer Releases reference Product Version(s) |
| Supersedes | Product Version (Track 2) | Each Product Version supersedes the previous |

## Example

`Product v3.2.0` = {payments-service v2.3.3, fx-engine v1.8.1, merchant-portal v4.1.1}. Declared BOM: {payments-service ^2.3.0, fx-engine ~1.8.0, merchant-portal >=4.1.0 <5.0.0}.
