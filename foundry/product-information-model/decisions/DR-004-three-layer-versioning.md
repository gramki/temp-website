# DR-004: Three-Layer Versioning: System Version, Module Version, Product Version

> **Superseded for operational use by DR-036 (2026-05-19).** Module Version, Module/Product Package, and SDD/MDD/PDD are retired. See DR-036 and Amended Records table in DR-036.

**Status:** Accepted (updated by DR-026)
**Date:** 2026-02-15
**Related FAQ:** Q13, Q14, Q86

---

## Context

The model needed to represent the output of engineering work (what gets built and deployed) and connect it to business delivery (what customers receive). Several terminology and structural challenges arose:

1. **"Product Increment" conflates with SAFe's "Program Increment" (PI)** — both abbreviate to PI, causing confusion.
2. **Versions are results, not plans** — in CI/CD, versions are continuously and routinely incremented as code flows through pipelines. They are not planned entities.
3. **Multi-module products have no single "product version"** — each system has its own CI/CD pipeline producing its own versions. Without a product-level composition, there is no way to assess composition integrity, certify compatibility, or reference "the product" for documentation.
4. **Composite artifacts should use version ranges** — following dependency management conventions, a product composition should declare compatible version ranges (like `package.json`) rather than pinning specific versions.
5. **Integration verification gap** — jumping from individual System testing to full-product testing is an O(n²) problem. A Module-scoped integration layer is needed.

## Decision

Introduce a four-level versioning model (three artifact tiers + one business entity):

| Layer | Entity | Nature | Versioning | Model Location |
|---|---|---|---|---|
| System level | **System Version** | Continuous CI/CD output per System (Dim 5) — atomic deployment unit | Semver | Work Model — Build Track artifact |
| Module level | **Module Version** | Integration-verified composition of System Versions for a Module (Dim 8) — unit of integration verification | Semver | Work Model — Build Track artifact |
| Product level | **Product Version** | Certified composition (BOM) of compatible Module Versions | Semver | Work Model — Build Track artifact |
| Business level | **Customer Release Intent** | Named intended delivery of capabilities to customers | Named (no versions) | Definition Model — Dim 1 (Strategy) |

**Product Version uses a Bill of Materials (BOM)** with two facets:
- **Declared BOM:** Compatible version ranges per Module Version (e.g., `Payments Module ^2.3.0`)
- **Resolved BOM:** Specific Module Versions tested and certified together (each containing its constituent System Versions)

All three artifact tiers are **Work Model artifacts** (Build Track outputs) because they are results of engineering progress, not planned upfront.

> **Updated from original DR-004:** The original decision described three layers: Module Version (CI/CD output), Product Version (composition), Customer Release (business). DR-026 refined this: the CI/CD output is now **System Version** (you build Systems, not Modules), and **Module Version** is repositioned as the integration-verified composition of System Versions within a Module boundary. DR-038 clarifies the strategy-layer business entity as **Customer Release Intent**.

## Rationale

1. **System Version replaces the original "Module Version"** — the Build Track builds Systems (Dim 5), not Modules (Dim 8). `payments-service v2.3.3` is a System Version. Avoids PI acronym collision with SAFe, and correctly positions versions as continuous CI/CD results.
2. **Module Version as integration layer** — reduces the integration verification problem from O(n²) across all Systems to O(k) within each Module. Proves that Systems implementing a Module work together before Product-level certification.
3. **Product Version solves real composition problems:**
   - **Integrity:** Which Module Versions are compatible with each other?
   - **Certification:** Is this specific composition tested and certified?
   - **Documentation:** Technical docs can reference "Product v3.2" for dependency compatibility.
   - **Reproducibility:** "What exactly was running in production on Feb 1?"
4. **BOM with version ranges** follows established dependency management patterns (npm/package.json, Maven/pom.xml, pip/requirements.txt). Allows Module Version updates within compatibility ranges without full re-certification.
5. **Work Model placement** for all three tiers because they are results, not plans. You don't plan "we'll produce v2.3.1" — you plan "we'll build feature X" and versions are cut continuously.

## Consequences

- **Positive:** Clean four-level model (three artifact tiers + business entity) with no terminology collisions.
- **Positive:** Each layer serves as a **communication bridge** at progressively broader organizational scope: System Version is the shared vocabulary between Build and Run teams (engineers + SREs). Module Version bridges Build, Run, and Product teams (engineers + SREs + PMs reason about capability-level versions). Product Version is the **ubiquitous language** across all teams and customers (Win teams, compliance, customers all reference "Product v3.2"). Customer Release Intent provides the business-level name.
- **Positive:** Each artifact tier is a **composite system** with emergent operational properties — Module Version has integrated failure modes and end-to-end latency that individual Systems lack; Product Version has cross-module workflow behavior and product-wide compliance posture. All tiers are operable, observable, and operationally meaningful.
- **Positive:** BOM approach is familiar to engineering teams.
- **Positive:** Integration verification layer (Module Version) reduces integration risk before Product-level certification.
- **Negative:** Introduces Module Version (integration artifact) as an additional concept to manage. Organizations must invest in tooling to automate BOM assembly, integration verification, and Product-level certification.
- **Negative:** Small/single-module products may find Product Version and Module Version unnecessary — they add value primarily for multi-module, multi-system products.
- **Negative:** Cultural adoption required — teams must actually use Module Version and Product Version as their shared vocabulary, not just produce them as artifacts nobody references. The communication-bridge value depends on organizational buy-in.
- **Negative:** Module boundary stability assumption — Module Versions are meaningful only if Module boundaries (Dim 8) are stable. Frequent Module restructuring destabilizes composition history.
