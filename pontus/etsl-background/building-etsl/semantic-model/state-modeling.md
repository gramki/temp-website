# ETSL Guidance Document  
## State Modeling for ETSL Modeling Architects

---

## 1. Purpose of This Document

This document provides **architectural guidance** for modeling *State* within the Enterprise Truth & Semantics Layer (ETSL).

It is intended for:
- ETSL Modeling Architects
- Enterprise Data Architects
- Domain Architects responsible for semantic integrity

The focus is on:
- Semantic correctness
- Integrity guarantees
- Lifecycle and invariants
- Clear separation of Facts, Events, and State

This document does **not** prescribe storage technologies or pipeline mechanics.

---

## 2. What State Means in ETSL (Authoritative Definition)

> **State is the authoritative, point-in-time realization of an enterprise entity, derived from facts and constrained by explicit invariants.**

Key properties:
- Derived, not asserted
- Bounded to an entity
- Time-addressable ("as of T")
- Semantically complete enough to defend integrity

State is the **form in which enterprise reality is operationally consumed**.

> **Relationship to Tier-1 Definition:** This definition elaborates the Tier-1 canonical definition of State ("a derived, point-in-time representation of an entity produced by reconciling relevant facts and relationships under ETSL rules") for an **architect audience**. It emphasizes invariants and integrity guarantees—the aspects architects must model. The Tier-1 definition remains authoritative; this document provides the architectural perspective.

---

## 3. Why State Is a First-Class Model (Not a Projection)

Facts assert individual truths.  
Events explain causality.  
**State encodes integrity.**

Without state:
- Integrity exists only implicitly in code
- Regulators and auditors must replay logic
- Decisions rely on fragile joins

State exists so that:
> *All facts required for an entity to be valid at time T are simultaneously true.*

---

## 4. State as a Closure Over Facts

State is a **semantic closure**, not an aggregation.

It enforces:
- Completeness
- Consistency
- Authority precedence
- Temporal coherence

A valid state answers:
- What is true?
- What is no longer true?
- Under which authority?
- Since when?

---

## 5. Modeling State Invariants

### 5.1 What Are Invariants?

Invariants are **conditions that must always hold** for an entity’s state to be valid.

Examples:
- An Account must have exactly one owner
- An Obligation must have a debtor and creditor
- A Contract cannot be ACTIVE without an effective date

Invariants are:
- Evaluated on state
- Explicitly documented
- Non-negotiable

---

### 5.2 Where Invariants Live

Invariants belong to:
- The ETSL state model
- Not pipelines
- Not downstream products
- Not application code

They are part of the **semantic contract** of the entity.

---

## 6. State Lifecycle Modeling

Each state model must define:
- Lifecycle stages (e.g., CREATED, ACTIVE, TERMINATED)
- Allowed transitions
- Illegal transitions

State transitions are:
- Derived from facts
- Validated against invariants
- Never implicit

---

## 7. Temporal Semantics of State

State must be:
- Versioned
- Time-bounded
- Queryable “as of” any point

Architectural rule:
> **If you cannot reconstruct state as of a past time without replaying code, the model is incomplete.**

---

## 8. Authority and Precedence in State

State must encode:
- Which authority asserts it
- Which authority overrides another
- How conflicts are resolved

Authority resolution is:
- Explicit
- Deterministic
- Auditable

---

## 9. What State Is Not (Anti-Patterns)

State is NOT:
- A transaction ledger
- A fact table
- A denormalized analytics view
- A cache without semantics
- A use-case-specific snapshot

If state changes when a consumer changes, it is **not state**.

---

## 10. Canonical Principles for Architects

1. State is derived; facts are asserted.
2. State encodes all integrity constraints.
3. State models are stable and slow-moving.
4. Invariants are semantic, not technical.
5. State must be defensible without code replay.

---

## 11. Validation Question (Mandatory)

> *Can this state representation be handed to a regulator and defended as complete and correct at that point in time?*

If not, the state model is insufficient.

---