# ETSL Guidance Document  
## Implementing State from Facts and Events  
### For Data Engineers

---

## 1. Purpose of This Document

This document provides **practical engineering guidance** for implementing ETSL state models in code, pipelines, and storage systems.

It is intended for:
- Data Engineers
- Platform Engineers
- Pipeline and Streaming Engineers

It assumes:
- Events and facts are already modelled correctly
- ETSL state semantics are defined by architects

---

## 2. What State Means for Engineers

For engineers:

> **State is a deterministic, validated result derived from facts, suitable for operational use.**

State is:
- Computed
- Versioned
- Validated
- Recomputable

State is **not**:
- A cache
- A latest-row table
- An event replay side effect

---

## 3. Deterministic State Derivation (Non-Negotiable)

Given:
- The same set of facts
- The same derivation logic
- The same time horizon

State computation must:
- Produce identical results
- Be order-independent
- Have no side effects

If not, the implementation is invalid.

---

## 4. Inputs to State Derivation

State builders consume:
- Facts (filtered by relevance)
- Authority rules
- Temporal constraints

They do NOT depend on:
- Event order
- Arrival time
- Downstream projections

---

## 5. Relevance Filtering (Critical Step)

Engineers must:
- Select only facts relevant to the entity
- Filter by:
  - Entity ID
  - Fact type
  - Effective time

Never “join everything and see what sticks”.

Relevance is a **semantic rule**, not a performance optimization.

---

## 6. Conflict Resolution Rules

Common conflicts:
- Multiple facts for the same predicate
- Overlapping effective periods
- Competing authorities

Engineering guidance:
- Apply explicit precedence rules
- Never rely on “last write wins” unless defined
- Log conflicts; do not hide them

---

## 7. State Validation and Failure Handling

Before persisting state:
- Validate all invariants
- Validate referential integrity
- Validate completeness

If validation fails:
- Do NOT persist state
- Emit an error signal
- Preserve facts unchanged

> Invalid state is worse than missing state.

---

## 8. Temporal Handling and Late Facts

Late or backdated facts:
- Require recomputation of affected state windows
- Must not silently mutate historical state

Engineering rule:
> **Facts are immutable; state is recomputable.**

---

## 9. Versioning State Logic

State derivation logic:
- Must be versioned
- Must be traceable to produced state
- Must not change silently

Every state record should be attributable to:
- Logic version
- Input fact set
- Computation time

---

## 10. Performance and Storage Guidance

- Optimize reads on state, not facts
- Treat state as authoritative for operations
- Treat facts as authoritative for reconstruction
- Projections may cache state, but never redefine it

---

## 11. Common Engineering Anti-Patterns

❌ Deriving state inside ad-hoc pipelines  
❌ Encoding invariants in SQL filters  
❌ Mutating state records in place  
❌ Recomputing state differently per consumer  
❌ Using events directly as state  

---

## 12. Operational Sanity Checks

Ask yourself:
- Can this state be recomputed from facts?
- Can it be explained without code replay?
- Can it survive backfills?
- Can it be validated independently?

If any answer is “no”, fix the pipeline.

---

## 13. Canonical Engineering Rules

1. State is computed, not written.
2. Facts are immutable; state is recomputable.
3. Validation precedes persistence.
4. Logic changes are versioned.
5. Errors surface early and loudly.

---

## 14. Final Reminder

> **State is where enterprise truth becomes operational.  
Treat it with the same rigor as money movement or ledger balances.**

---