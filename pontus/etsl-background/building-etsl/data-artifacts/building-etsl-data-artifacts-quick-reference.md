# Building ETSL Data Artifacts — Quick Reference Card
## One-Page Cheat Sheet for Architects and Engineers

**Full Document:** `building-etsl-data-artifacts-in-a-large-enterprise.md`

---

## The Flow

```
Assertion Sources → Ingress → Reconciliation → ETSL Data Artifacts → Data Products
     (SORs)         (capture)   (resolve)        (enterprise truth)   (interpret)
```

---

## What ETSL Data Artifacts ARE vs ARE NOT

| ✅ ARE | ❌ ARE NOT |
|--------|-----------|
| Authority-qualified facts | Raw SOR tables |
| Temporal (effective dates) | Latest-wins snapshots |
| Cross-domain reusable | Domain-specific views |
| Reconciled truth | Unresolved assertions |
| Traceable to sources | Orphaned data |

---

## Ingress Layer — 4 Responsibilities

| # | Responsibility | Key Rule |
|---|----------------|----------|
| 1 | **Capture** | Accept source-native; no data loss |
| 2 | **Provenance** | Record source, timestamp, batch/event ID |
| 3 | **Authority Tag** | Look up in Authority Registry; attach |
| 4 | **Normalize** | Map to ETSL types (format, not semantics) |

> ⚠️ Ingress does **format normalization**, not **semantic interpretation**.

---

## Reconciliation Patterns

| Pattern | When to Use | Rule |
|---------|-------------|------|
| **Authority Precedence** | Multiple authorities assert same fact | Higher-precedence authority prevails |
| **Temporal Validity** | Overlapping effective dates | Most recent `effective_from` wins |
| **Explicit Override** | One assertion supersedes another | Preserve both; override is current truth |
| **Contextual Authority** | Authority varies by context (e.g., delinquency) | Context must be explicit, not inferred |

---

## Error Handling Patterns

| Pattern | Use When | Behavior |
|---------|----------|----------|
| **Conservative Rejection** (default) | High-integrity domains | No state emitted until resolved |
| **Last-Known-Good Fallback** | Continuity-critical domains | Stale state + alert for resolution |

**Every alert must have a resolution SLA.**

---

## Authority Registry — 4 Rules

1. **Start narrow** — cover only scoped facts/relationships
2. **Be explicit** — unclear authority → flag for governance
3. **Avoid system names** — systems act on behalf of authority
4. **Version it** — authority evolves; track changes

---

## First Artifact — Good v1 Checklist

| ✅ Do | ❌ Don't |
|-------|---------|
| One product type | All credit products |
| 2 sources | 5 systems |
| Clear authority | Disputed ownership |
| One active consumer | No committed user |
| 12-week timeline | 6-month roadmap |

**Scope for correctness, not coverage.**

---

## Validation Dimensions

| Dimension | What It Checks |
|-----------|----------------|
| **Semantic correctness** | Values conform to ETSL contracts |
| **Authority consistency** | Every assertion has valid authority |
| **Temporal coherence** | Effective dates present and valid |
| **Referential integrity** | Relationships reference valid entities |
| **Invariant compliance** | State satisfies ETSL invariants |

---

## "Done" for v1 — 6 Criteria

1. ✅ Lineage complete (artifact → sources)
2. ✅ Authority explicit on every fact
3. ✅ Temporal semantics present
4. ✅ At least one consumer using it
5. ✅ Validation passed
6. ✅ Documentation exists

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails |
|--------------|--------------|
| **Golden record fallacy** | Truth ≠ single record; authority varies |
| **System = authority** | Systems emit; functions/roles authorize |
| **Latest-wins reconciliation** | Time matters; authority matters more |
| **Skipping provenance** | Audit cannot reconstruct |
| **Semantic normalization at ingress** | Interpretation belongs downstream |

---

## Key Principles (Memorize These)

1. **Assertions are claims, not truth** — ETSL decides what becomes truth
2. **Authority is modeled, not assumed** — explicit in every artifact
3. **Time is a first-class dimension** — effective dates, not just timestamps
4. **Reconciliation is semantic, not technical** — governed, not coded
5. **Start narrow, prove value, expand** — v1 wins build momentum

---

## Further Reading

- Authority Modeling: `../semantic-model/etsl-authority-modeling-guidance-for-architects.md`
- Temporal Ordering: `../../conceptual/etsl-and-temporal-ordering.md`
- Error Handling: Section 11 of full document
- Data Quality vs ETSL Quality: Section 8.6 of full document

---

