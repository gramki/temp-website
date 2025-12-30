# Tier-2 ETSL Canonical Classifications & Terms
## Normative Behavioral and Architectural Classifications

This document defines **Tier-2 ETSL terms**.
Tier-2 terms are **normative classifications** that constrain behavior, review rigor, and engineering expectations.

They are **not semantic primitives** and MUST NOT redefine Tier-1 meanings.

---

## How Tier-2 Terms Are Used

- To classify Data Applications and Data Artifacts
- To set review and governance expectations
- To enable evolution without semantic drift

Tier-2 terms MAY evolve.
Tier-1 terms MUST remain stable.

---

## 1. ETSL Core Data Application

**Definition**
> A Data Application that operates inside the ETSL boundary to normalize assertions, apply authority, perform reconciliation, and derive ETSL Data Artifacts.

**Characteristics**
- Consumes candidate assertions
- Executes ETSL Semantic Artifacts
- Authority-aware by construction
- Produces enterprise truth

**Review Expectations**
- Architectural review mandatory
- Backward compatibility required
- Semantic changes are high-risk

---

## 2. Transforming Data Application

**Definition**
> A Data Application that consumes ETSL Data Artifacts or Data Products to produce derived datasets, aggregates, or features.

**Characteristics**
- Interpretation-oriented
- Use-case driven
- Does not assert enterprise truth

---

## 3. Serving Data Application

**Definition**
> A Data Application that exposes data via APIs, queries, or services to meet consumer latency, availability, and contract requirements.

**Characteristics**
- Consumer-facing
- SLA- and contract-driven
- Must not embed semantic reinterpretation

---

## 4. Data-Driven Operational Application

**Definition**
> An operational application whose runtime behavior is materially influenced by Data Products.

**Characteristics**
- Part of business execution
- Produces Derived Assertions
- Inside the ETSL feedback loop

---

## 5. Candidate Assertion

**Definition**
> An assertion captured at the ETSL ingress boundary that has not yet been normalized or reconciled into enterprise truth.

**Characteristics**
- Pre-authoritative
- Must preserve provenance
- Input to ETSL Core Data Applications

---

## 6. ETSL Ingress Boundary

**Definition**
> The logical boundary at which assertions are captured for consideration by ETSL.

**Characteristics**
- Capture-only
- No reconciliation or semantic interpretation
- Provenance-preserving

**Clarification: Normalization vs Interpretation**

| Allowed at Ingress | Not Allowed at Ingress |
|--------------------|------------------------|
| **Format normalization** (date formats, encoding, structural transformation) | **Semantic interpretation** (reconciliation, authority application, business logic) |
| **Validation** (schema conformance, required fields) | **Conflict resolution** (choosing between competing assertions) |
| **Provenance capture** (source, timestamp, authority tagging) | **Truth determination** (deciding what is true) |

Format normalization is mechanical and reversible. Semantic interpretation is governed and constitutes truth-making. Ingress performs the former; ETSL Core Data Applications perform the latter.

---

## Enforcement Guidance

- Every Data Application MUST declare its Tier-2 classification.
- Classification determines:
  - Review rigor
  - Change tolerance
  - Audit expectations
- Misclassification is an architectural defect.

---

## Evolution Guidance

- New Tier-2 classifications may be added as patterns emerge.
- Existing classifications may be refined.
- Tier-2 evolution MUST NOT redefine Tier-1 semantics.

---
