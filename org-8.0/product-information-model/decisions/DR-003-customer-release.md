# DR-003: Customer Release as Named Business Delivery Entity

**Status:** Accepted
**Date:** 2026-02-15
**Related FAQ:** Q12

---

## Context

The model needed an entity to represent "a coherent delivery of capabilities to customers." The word "release" is deeply overloaded in the software industry:

- **DevOps convention:** "Release" = a versioned build artifact that has passed quality gates (GitHub Releases, Helm releases, release pipelines, release branches).
- **Business convention:** "Release" = making functionality available to customers.

SAFe and Continuous Delivery practitioners explicitly decouple "release" (business act) from "deployment" (technical act). However, in practice, the DevOps usage of "release" for artifacts is so entrenched that trying to reclaim the word exclusively for the business concept would create adoption friction.

Additionally, the question arose whether this entity should carry version numbers (semver) or use descriptive names.

## Decision

1. Introduce **"Customer Release"** as the business delivery entity in the Definition Model (Dimension 1, Strategy).
2. Customer Releases use **descriptive names** (e.g., "LATAM Expansion", "Project Mercury"), not version numbers or semver.
3. DevOps artifact versioning continues to use "released" freely — a System Version with status `Released` is a versioned artifact that passed quality gates. The term "artifact release version" is acceptable.

## Rationale

1. **"Customer" qualifier eliminates ambiguity.** No one will confuse "Customer Release: LATAM Expansion" with "payments-service v2.3.3 released."
2. **Zero adoption friction on the DevOps side.** Engineering teams continue using "release" for artifacts as they always have.
3. **Names over versions** because:
   - Names convey business meaning ("LATAM Expansion" vs. "Release 3.2").
   - A Customer Release may span multiple Product Versions (v3.2.0 through v3.2.4 as patches ship during rollout) — a version number creates a false 1:1 mapping.
   - Customer Releases are strategy entities, not technical artifacts. Versioning is for technical artifacts.
4. **Aligned with industry precedent:** macOS (Sonoma, Sequoia), Android (codenames), many enterprise products use named releases.

## Consequences

- **Positive:** Clean separation between business and technical use of "release."
- **Positive:** Customer-facing communication uses meaningful names.
- **Positive:** Customer Release is correctly positioned as a strategy entity alongside Objectives and Initiatives.
- **Negative:** Requires organizational discipline to use "Customer Release" consistently in business contexts. Some stakeholders may initially default to "release" without the qualifier.
