# ETSL and Multi-Jurisdiction Enterprises
## Scope Boundaries and Acknowledged Complexity

**Audience:** Enterprise Architects, Legal/Compliance Teams, CIOs  
**Status:** Scope Boundary Document

---

## 1. Purpose of This Document

This document explicitly defines **what ETSL does not address** regarding multi-jurisdiction and cross-legal-entity scenarios.

Large enterprises—especially global banks—operate across jurisdictions with differing regulatory requirements, data residency laws, and legal entity structures. These realities introduce significant complexity.

This document acknowledges that complexity and states clearly: **multi-jurisdiction handling is beyond the current scope of ETSL.**

---

## 2. What Is Out of Scope

### Jurisdiction-Scoped Entities

ETSL does not currently model entities that have different semantic definitions or authority structures by jurisdiction.

**Example of what is NOT addressed:**
- A "Customer" entity that has different required attributes in the EU (GDPR) vs. US (CCPA)
- A "Party" entity whose identity verification rules differ by country
- An "Account" entity subject to different regulatory reporting in different jurisdictions

Jurisdiction-scoped entities introduce **substantial modeling overhead**:
- Parallel semantic definitions per jurisdiction
- Conditional attribute requirements
- Jurisdiction-aware reconciliation logic
- Cross-jurisdiction identity resolution

This overhead is not handled in the current ETSL scheme.

---

### Conditional Authority

ETSL models authority as **functional mandates** that are stable across the enterprise.

**What is NOT addressed:**
- Authority that varies by jurisdiction (e.g., "Compliance has authority in EU, but Legal has authority in US")
- Authority that is conditional on legal entity (e.g., "Risk authority applies only to the holding company")
- Time-of-day or market-hours conditional authority

> **Any conditional treatment of authority is out of scope.**

Authority in ETSL is:
- Explicit and modeled
- Stable across the enterprise
- Not conditional on jurisdiction, legal entity, or runtime context

---

### Data Residency

ETSL does not prescribe or enforce data residency requirements.

**What is NOT addressed:**
- Where ETSL Data Artifacts are physically stored
- Cross-border data transfer restrictions
- Jurisdiction-specific retention policies

Data residency is a **platform and compliance concern**, not an ETSL semantic concern. Enterprises must address residency at the infrastructure layer.

---

### Cross-Legal-Entity Reconciliation

ETSL assumes a unified enterprise semantic model.

**What is NOT addressed:**
- Reconciliation of the "same" entity across legal entities with different regulatory regimes
- Conflicts that arise from jurisdiction-specific interpretations of truth
- Legal entity boundaries as reconciliation barriers

---

## 3. Why This Is Out of Scope

### Modeling Overhead

Jurisdiction-scoped semantics would require:
- Multiple versions of each Semantic Artifact per jurisdiction
- Conditional invariants and constraints
- Jurisdiction as a first-class dimension in all ETSL constructs

This complexity is substantial and would fundamentally change ETSL's architecture.

### Authority Stability

ETSL's value proposition depends on **stable, explicit authority**. Conditional authority:
- Complicates reconciliation logic
- Makes audit trails harder to follow
- Introduces runtime decision-making into semantic truth

This undermines the core principle that **authority is modeled, not computed**.

### Current Focus

ETSL is designed to establish **enterprise truth within a coherent semantic boundary**. Multi-jurisdiction enterprises often have:
- Distinct regulatory regimes
- Separate legal entities with their own data ownership
- Conflicting definitions of the "same" concept

These are legitimate enterprise realities, but addressing them requires architectural patterns beyond ETSL's current scope.

---

## 4. What Enterprises Can Do Today

### Option A: Separate ETSL Instances

Enterprises may choose to operate **separate ETSL instances** per jurisdiction or legal entity, with explicit integration points.

- Each instance has its own Semantic Artifacts and authority model
- Cross-instance integration is treated as external data exchange
- No assumption of unified truth across instances

### Option B: Unified Model with Jurisdictional Attributes

Enterprises may model jurisdiction as a **non-authoritative attribute** on entities, without conditional semantics.

- Entities carry a `jurisdiction` attribute
- Authority and reconciliation remain jurisdiction-agnostic
- Jurisdiction-specific logic is handled in downstream Data Products, not ETSL

### Option C: Defer Multi-Jurisdiction Complexity

Enterprises may start ETSL adoption within a **single jurisdiction or legal entity** and defer multi-jurisdiction handling.

- Proves ETSL value in a bounded scope
- Multi-jurisdiction can be addressed later as ETSL matures

---

## 5. Future Considerations

Multi-jurisdiction handling may be addressed in future ETSL evolution. Potential directions include:

- Jurisdiction as a scoping dimension in Semantic Artifacts
- Conditional authority models with explicit governance
- Federation patterns across ETSL instances

These are **not commitments**. They are acknowledged as areas for future exploration if enterprise demand warrants.

---

## 6. Summary

| Topic | Status |
|-------|--------|
| Jurisdiction-scoped entities | Out of scope |
| Conditional authority | Out of scope |
| Data residency | Out of scope (platform concern) |
| Cross-legal-entity reconciliation | Out of scope |

**ETSL assumes a unified enterprise semantic boundary.** Multi-jurisdiction complexity is acknowledged but not addressed in the current design.

---

