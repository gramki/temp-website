# ETSL Documentation: Conceptual Review Findings
## Gaps, Inconsistencies, and Inadequacies

**Review Date:** December 30, 2025  
**Scope:** All documents in `/etsl-background/`

---

## Executive Summary

The ETSL documentation corpus is architecturally coherent and well-structured. The core concepts are consistently defined, and the document hierarchy is clear. However, this review identified **5 conceptual gaps**, **4 inconsistencies**, and **3 inadequacies** that, if addressed, would strengthen the corpus.

| Category | Count | Priority Distribution |
|----------|-------|----------------------|
| Conceptual Gaps | 5 | 2 High, 2 Medium, 1 Low |
| Inconsistencies | 4 | 1 High, 2 Medium, 1 Low |
| Inadequacies | 3 | 1 High, 1 Medium, 1 Low |

---

## 1. Conceptual Gaps (Missing Topics)

### ✅ ~~Gap 1: ETSL Versioning and Evolution (High Priority)~~ — ADDRESSED

**Resolution:**
Added comprehensive Section 8 "ETSL Versioning and Evolution" to `etsl-semantic-model-guidance-for-architects.md` covering:
- Semantic versioning scheme (MAJOR.MINOR.PATCH)
- Change classification (breaking/additive/clarifying)
- Invariant evolution problem
- Deprecation lifecycle (ACTIVE → DEPRECATED → REMOVED)
- Breaking change handling and dual-version patterns
- Data Product tolerance levels for semantic versions
- Version registry guidance
- Evolution anti-patterns
- Governance and checklists

---

### ✅ ~~Gap 2: Error Handling and Exception Semantics (High Priority)~~ — ADDRESSED

**Resolution:**
Added comprehensive Section 11 "Reconciliation Failure and Error Handling" to `building-etsl-data-artifacts-in-a-large-enterprise.md` covering:
- Core principle: Don't right-shift problems (fail fast, fail loud)
- Error classification taxonomy (validation, authority, reconciliation, temporal)
- Two reconciliation patterns: Last-Known-Good (Pattern B) and Conservative Rejection (Pattern C)
- Default pattern is Conservative Rejection
- Pattern declaration per attribute in Semantic Artifacts
- Resolution SLAs for all conflicts
- Ingress-level rejections and dead-letter handling
- Error lineage and traceability requirements
- Four banking examples (credit limit, customer identity, preferred channel, unknown source)
- Monitoring and alerting guidance
- Explicit scope exclusion for technical infrastructure errors

---

### ✅ ~~Gap 3: ETSL and Real-Time/Streaming Architectures (Medium Priority)~~ — ADDRESSED

**Resolution:**
Created new document `conceptual/etsl-and-temporal-ordering.md` covering:
- Why out-of-order assertions are unavoidable (effective time vs processing time)
- How ETSL handles out-of-order internally (recompute, correct, annotate)
- ETSL delivers truth-as-known (no reconciliation states exposed)
- Corrections are first-class and explicit (not just versions)
- Correction annotations propagate through lineage
- Consumer responsibilities (no guarantees on order; must handle corrections)
- Patterns for reducing out-of-order impact (assertion/source-specific)
- Unhandled out-of-order quarantined with alerts/SLAs
- Three banking examples

Document is technology-agnostic and focuses on semantic principles, not streaming platform details.

---

### ✅ ~~Gap 4: ETSL for Multi-Region and Cross-Jurisdictional Enterprises (Medium Priority)~~ — ADDRESSED

**Resolution:**
Created scope boundary document `conceptual/etsl-multi-jurisdiction-scope.md` that explicitly states:
- Jurisdiction-scoped entities are **out of scope** (substantial modeling overhead)
- Conditional authority is **out of scope** (authority must be stable, not computed)
- Data residency is **out of scope** (platform concern, not ETSL semantic concern)
- Cross-legal-entity reconciliation is **out of scope** (assumes unified semantic boundary)

Document provides three options for enterprises today: separate ETSL instances, jurisdiction as non-authoritative attribute, or defer complexity.

---

### ✅ ~~Gap 5: ETSL and Data Quality (Low Priority)~~ — ADDRESSED

**Resolution:**
Added Section 8.6 "Data Quality vs ETSL Quality: A Clear Boundary" to `building-etsl-data-artifacts-in-a-large-enterprise.md` covering:
- Clear boundary: DQ before ingress, ETSL Quality at/after ingress
- What ETSL does not replace (source-level DQ responsibilities)
- What ETSL validates (authority, semantic conformance, temporal validity)
- Two distinct metric sets (DQ Metrics vs ETSL Quality Metrics)
- Alert visibility to both ETSL Ops and Source teams
- Anti-pattern: expecting ETSL to fix DQ problems

---

## 2. Inconsistencies Across Documents

### ✅ ~~Inconsistency 1: Definition of "Fact" (High Priority)~~ — FIXED

**Finding:**
The definition of "Fact" varied across documents and was missing from Tier-1.

**Resolution:**
Added "Fact" as Section 8 in `tier-1-etsl-canonical-terminology.md` with definition aligned to `events-vs-facts.md`:
> "A semantically asserted truth about the enterprise, valid from a point in time, and attributable to an explicit authority."

---

### ✅ ~~Inconsistency 2: "Event" Authority Treatment (Medium Priority)~~ — FIXED

**Resolution:**
Updated `events-vs-facts.md` to clarify:
- Section 3 table: Changed "Implicit (emitter)" to "Explicit (derived or induced)"
- Added note: Both Facts and Events are ETSL artifacts and must have authority attributed
- Section 8: Expanded to explain that Event authority is derived/induced, not optional
- Added "Source vs Authority" table distinguishing source (who emitted) from authority (who has mandate)
- Added three derivation patterns: source-registered, event-type-based, domain-induced
- Clarified: Regardless of derivation method, authority must be explicit and auditable

---

### ✅ ~~Inconsistency 3: State Definition Variations (Medium Priority)~~ — FIXED

**Resolution:**
Added clarifying notes to both documents:
- `state-modeling.md`: Added note stating definition elaborates Tier-1 for architect audience (emphasizes invariants and integrity)
- `state-engineering.md`: Added note stating definition elaborates Tier-1 for engineering audience (emphasizes determinism and recomputability)

Both notes explicitly state: "The Tier-1 definition remains authoritative; this document provides the [architect/engineering] perspective."

---

### ✅ ~~Inconsistency 4: ETSL Ingress Boundary Responsibilities (Low Priority)~~ — FIXED

**Resolution:**
Added clarifying content to both documents:
- `tier-2-etsl-canonical-classifications.md`: Added "Normalization vs Interpretation" table distinguishing allowed (format normalization, validation, provenance capture) from not allowed (semantic interpretation, conflict resolution, truth determination)
- `building-etsl-data-artifacts-in-a-large-enterprise.md` Section 8: Added "Normalization vs Semantic Interpretation (Critical Distinction)" subsection with examples and cross-reference to Tier-2 definition

---

## 3. Inadequacies (Underdeveloped Areas)

### 🔴 Inadequacy 1: Security and Access Control (High Priority)

**What's Underdeveloped:**
The corpus has **no guidance on ETSL security**:

- Who can read ETSL Data Artifacts?
- Who can write/assert into ETSL?
- How is access control modeled (RBAC? ABAC? Domain-based?)
- How does ETSL interact with enterprise identity and access management?
- Are there sensitivity classifications for ETSL artifacts?

**Current State:**
Zero coverage.

**Recommendation:**
Create `conceptual/etsl-security-and-access-control.md` addressing:
- Assertion-level access (who can emit)
- Artifact-level access (who can consume)
- Authority Registry as an access control mechanism
- Integration with enterprise IAM

---

### 🟡 Inadequacy 2: Testing and Validation Patterns (Medium Priority)

**What's Underdeveloped:**
While validation is mentioned, there is no comprehensive testing guidance:

- How do you test an ETSL Core Data Application?
- What are the contract testing patterns for ETSL artifacts?
- How do you regression-test reconciliation logic changes?
- What are the CI/CD considerations for ETSL?

**Current State:**
- `state-engineering.md` has "Operational Sanity Checks"
- `building-etsl-data-artifacts.md` Section 12 mentions validation
- No dedicated testing document

**Recommendation:**
Add a section to `building-etsl-data-artifacts-in-a-large-enterprise.md` or create `building-etsl/data-artifacts/etsl-testing-patterns.md`.

---

### 🟢 Inadequacy 3: Migration Patterns from Legacy Systems (Low Priority)

**What's Underdeveloped:**
While the corpus acknowledges starting from legacy estates, detailed migration patterns are thin:

- How do you migrate a legacy DW to ETSL-based architecture?
- What are the dual-run patterns during transition?
- How do you prove equivalence between legacy and ETSL artifacts?
- What are the rollback patterns?

**Current State:**
- `building-etsl-data-artifacts.md` Section 16 has a brief roadmap
- No detailed migration playbook

**Recommendation:**
This may be intentionally light (avoiding prescriptiveness). If desired, add `conceptual/etsl-migration-patterns.md`.

---

## 4. Minor Issues and Observations

### Terminology Precision

| Term | Observation |
|------|-------------|
| "Enterprise Truth" | Used pervasively but never formally defined. Consider adding to Tier-1 or a dedicated definition in Purpose doc. |
| "Semantic Contract" | Used in multiple places but not defined in terminology docs. |
| "Truth Boundary" | Appears in `etsl-for-cios-ai-at-scale.md` but not elsewhere. |

### Cross-Reference Gaps

| Document | Missing Reference |
|----------|-------------------|
| `tier-1-etsl-canonical-terminology.md` | Should reference `events-vs-facts.md` for Fact concept |
| `etsl-physical-layers.md` | Should reference `state-modeling.md` for Layer 3 semantics |
| `state-engineering.md` | Should reference `tier-2-etsl-canonical-classifications.md` for Data Application types |

### Document Freshness Indicators

Some documents reference internal systems or projects that may be stale:
- ~~`etsl-physical-layers.md` references "Quark outputs," "Neutrino decisions," "Ibuki memory" — these may be internal project names that need context or removal for external audiences.~~ **RESOLVED**: Internal project names replaced with generic terms.

---

## 5. Recommended Priority Actions

### Immediate (Before Next Major Use)

| # | Action | Documents Affected | Status |
|---|--------|-------------------|--------|
| 1 | Add "Fact" to Tier-1 Canonical Terminology | `tier-1-etsl-canonical-terminology.md` | ✅ Done |
| 2 | Clarify Event authority vs. emitter attribution | `events-vs-facts.md` | ✅ Done |
| 3 | Add cross-reference note for State definitions | `state-modeling.md`, `state-engineering.md` | ✅ Done |

### Short-Term (Next 30 Days)

| # | Action | Effort | Status |
|---|--------|--------|--------|
| 4 | Create ETSL Versioning and Evolution guide | New section | ✅ Done |
| 5 | Create ETSL Error and Exception Handling guide | New section | ✅ Done |
| 6 | Add Security and Access Control section | New document | Pending |

### Medium-Term (Next 90 Days)

| # | Action | Effort | Status |
|---|--------|--------|--------|
| 7 | Add Real-Time/Streaming guidance | New document | ✅ Done |
| 8 | Add Testing and Validation patterns | New document or section | Pending |
| 9 | Review and normalize "enterprise truth" usage | Cross-corpus edit | Pending |

---

## 6. Corpus Strengths (For Balance)

The review also identified significant strengths:

✅ **Tier-1 terminology is stable and consistent** — The core semantic primitives are well-defined and not drifting.

✅ **The Fact/Event/State distinction is clear** — `events-vs-facts.md` is excellent and should be a model for other conceptual docs.

✅ **The Data Mesh coexistence framing is strong** — The corpus avoids the trap of positioning ETSL as a replacement.

✅ **Authority as a first-class concept** — This is genuinely differentiated and consistently applied.

✅ **Banking examples are concrete and useful** — The "available credit" example appears in multiple docs and ties concepts to reality.

✅ **Reading paths by persona are helpful** — The README provides clear navigation for different audiences.

---

## Appendix: Documents Reviewed

| Category | Documents |
|----------|-----------|
| Introduction | `etsl-purpose-and-story.md`, `etsl-one-page-onboarding-primer.md`, `etsl-for-cios-ai-at-scale.md` |
| Terminology | `tier-1-etsl-canonical-terminology.md`, `tier-2-etsl-canonical-classifications.md` |
| Conceptual | `artifacts-ontology-vs-semantic-vs-data.md`, `events-vs-facts.md`, `etsl-physical-layers.md`, `etsl-and-data-mesh-coexistence-guidance.md` |
| Building ETSL | `data-modeling-guidance.md`, `relationships-modeling-guidance.md`, `state-modeling.md`, `etsl-semantic-model-guidance-for-architects.md`, `etsl-authority-modeling-guidance-for-architects.md`, `building-etsl-data-artifacts-in-a-large-enterprise.md`, `state-engineering.md` |
| Building Data Products | `building-data-products-using-etsl-data-artifacts.md`, `etsl-data-products-vs-other-approaches.md` |

---

