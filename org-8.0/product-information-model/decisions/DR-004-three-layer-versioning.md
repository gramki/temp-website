# DR-004: Three-Layer Versioning: Module Version, Product Version, Customer Release

**Status:** Accepted
**Date:** 2026-02-15
**Related FAQ:** Q13, Q14

---

## Context

The model needed to represent the output of engineering work (what gets built and deployed) and connect it to business delivery (what customers receive). Several terminology and structural challenges arose:

1. **"Product Increment" conflates with SAFe's "Program Increment" (PI)** — both abbreviate to PI, causing confusion.
2. **Versions are results, not plans** — in CI/CD, versions are continuously and routinely incremented as code flows through pipelines. They are not planned entities.
3. **Multi-module products have no single "product version"** — each module has its own CI/CD pipeline producing its own versions. Without a product-level composition, there is no way to assess composition integrity, certify compatibility, or reference "the product" for documentation.
4. **Composite artifacts should use version ranges** — following dependency management conventions, a product composition should declare compatible version ranges (like `package.json`) rather than pinning specific versions.

## Decision

Introduce a three-layer versioning model:

| Layer | Entity | Nature | Versioning | Model Location |
|---|---|---|---|---|
| Module level | **Module Version** | Continuous CI/CD output per module | Semver | Work Model — Build Track output |
| Product level | **Product Version** | Certified composition (BOM) of compatible Module Versions | Semver | Work Model — Build Track output |
| Business level | **Customer Release** | Named delivery of capabilities to customers | Named (no versions) | Definition Model — Dim 1 (Strategy) |

**Product Version uses a Bill of Materials (BOM)** with two facets:
- **Declared BOM:** Compatible version ranges per module (e.g., `payments-service ^2.3.0`)
- **Resolved BOM:** Specific versions tested and certified together

Both Module Version and Product Version are **Work Model entities** (Build Track outputs) because they are results of engineering progress, not planned upfront.

## Rationale

1. **Module Version replaces "Product Increment"** — avoids PI acronym collision with SAFe, and correctly positions versions as continuous CI/CD results rather than planned increments.
2. **Product Version solves real composition problems:**
   - **Integrity:** Which Module Versions are compatible with each other?
   - **Certification:** Is this specific composition tested and certified?
   - **Documentation:** Technical docs can reference "Product v3.2" for dependency compatibility.
   - **Reproducibility:** "What exactly was running in production on Feb 1?"
3. **BOM with version ranges** follows established dependency management patterns (npm/package.json, Maven/pom.xml, pip/requirements.txt). Allows Module Version patches within compatibility ranges without full re-certification.
4. **Work Model placement** for both versions because they are results, not plans. You don't plan "we'll produce v2.3.1" — you plan "we'll build feature X" and versions are cut continuously.

## Consequences

- **Positive:** Clean three-layer model with no terminology collisions.
- **Positive:** Each layer serves a distinct audience: Module Version (dev team), Product Version (release engineering/QA), Customer Release (business/customers).
- **Positive:** BOM approach is familiar to engineering teams.
- **Negative:** Introduces Product Version as an additional concept to manage. Organizations must invest in tooling to automate BOM assembly and verification.
- **Negative:** Small/single-module products may find Product Version unnecessary — it adds value primarily for multi-module products.
