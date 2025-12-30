# Tier-1 ETSL Canonical Terminology
## Normative Semantic Primitives (Must Not Drift)

This document defines the **Tier-1 canonical terminology** for the Enterprise Truth & Semantics Layer (ETSL).
Tier-1 terms are **semantic primitives**. If their meaning drifts, the ETSL model collapses.

**Rules**
- Tier-1 terms have exactly one meaning enterprise-wide.
- Tier-1 terms MUST NOT be redefined locally.
- Clarifications may be added; meanings may not change.
- Behavioral or execution-specific variations do NOT belong in Tier-1.

---

## 1. ETSL Semantic Artifact

**Definition**
> A formal, implementation-independent specification that defines the meaning, boundaries, and relationships of enterprise facts, relationships, and state.

**Is**
- Conceptual and normative
- Independent of storage, pipelines, or tools
- The source of semantic truth

**Is not**
- A table schema
- A query model
- A general-purpose ontology

---

## 2. ETSL Data Artifact

**Definition**
> A governed, authority-qualified, time-aware representation of enterprise truth produced by applying ETSL semantics to assertions.

**Is**
- Concrete and persisted
- Reusable across domains
- Stable relative to consumer use cases

**Is not**
- Raw ingested data
- A Domain Data Product
- A metric, KPI, or feature

---

## 3. Assertion

**Definition**
> A statement made by a system or function about an enterprise fact, relationship, or state at a point in time.

**Is**
- A claim, not guaranteed truth
- Time-bound and attributable

**Is not**
- Automatically authoritative
- A derived interpretation

---

## 4. Assertion Source

**Definition**
> A system, application, or function that emits assertions about the enterprise.

**Is**
- An emitter of claims
- Federated by nature

**Is not**
- Enterprise truth
- Automatically authoritative

---

## 5. Authority

**Definition**
> An explicitly modeled mandate that determines which assertions are accepted as valid for a defined semantic scope and temporal context.

**Is**
- Modeled and explicit
- Federated and contextual

**Is not**
- Centralized governance
- Data ownership
- An org chart role

---

## 6. Authority Registry

**Definition**
> A formal mapping that records which authorities are valid for which semantic scopes and under what conditions.

**Is**
- Explicit and inspectable
- Evolvable over time

**Is not**
- A permissions system
- A governance committee

---

## 7. Reconciliation

**Definition**
> The semantic process of resolving multiple assertions into an accepted enterprise representation using authority, time, and scope.

**Is**
- Deliberate and traceable
- Semantics-driven

**Is not**
- Deduplication
- Record merging

---

## 8. Fact

**Definition**
> A semantically asserted truth about the enterprise, valid from a point in time, and attributable to an explicit authority.

**Is**
- Declarative (what is true)
- Time-bound (effective from a point in time)
- Authority-qualified
- Immutable (superseded, never deleted)

**Is not**
- An event (what happened)
- A mutable record
- A derived interpretation

**Relationship to Other Concepts**
- Facts define what is true; Events explain how truth came to be
- State is derived from Facts; Facts are not derived from State
- For detailed guidance, see *Fact Modeling vs Event Modeling*

---

## 9. Event

**Definition**
> A semantically typed record of something that occurred at a specific point in time, attributable to an emitter and carrying derived or induced authority.

**Is**
- Narrative (what happened)
- Occurrence-time bound
- Authority-qualified (derived or induced, not implicit)
- Immutable (recorded, never deleted)

**Is not**
- A fact (what is true)
- A mutable record
- A source of truth (though it may induce facts)

**Relationship to Other Concepts**
- Events explain how truth came to be; Facts define what is true
- Events may induce Facts (e.g., `AccountOpened` event induces `AccountExists` fact)
- Event authority is derived (from the emitting system/process) or induced (from the fact it produces)
- For detailed guidance, see *Fact Modeling vs Event Modeling*

---

## 10. State

**Definition**
> A derived, point-in-time representation of an entity produced by reconciling relevant facts and relationships under ETSL rules.

**Is**
- Derived, not asserted
- Authority-aware

**Is not**
- A mutable record
- A source assertion

---

## 11. Derived Assertion

**Definition**
> An assertion produced by a system whose behavior was influenced by Data Products or prior derived state.

**Is**
- First-class enterprise truth
- Required to carry lineage

**Is not**
- Inferior or optional

---

## 12. Data Product

**Definition**
> A consumer-aligned, governed data asset that interprets ETSL Data Artifacts to serve a specific use case or decision.

**Is**
- Purpose-built
- Allowed to evolve quickly

**Is not**
- A source of enterprise truth
- An ETSL Data Artifact

---

## 13. Source-Aligned Data Product

**Definition**
> A domain-owned Data Product that closely reflects the semantics of an operational system or function.

**Is**
- Domain-local
- Legitimate and persistent

**Is not**
- Enterprise-wide truth

---

## 14. Data Application

**Definition**
> A software component that consumes **candidate assertions, ETSL Data Artifacts, or Data Products** and applies logic to produce derived data, decisions, or services.

**Is**
- Implementation-specific
- Executable logic

**Is not**
- A semantic authority
- A Data Product itself

---

## 15. Data-Driven Operational Application

**Definition**
> An operational system whose behavior or decisions are materially influenced by data products.

**Is**
- Part of business execution
- A producer of derived assertions

**Is not**
- A passive consumer

---

## Governance Note

Tier-1 terminology changes require:
- Explicit architectural review
- Backward semantic compatibility
- Enterprise-level approval

---
