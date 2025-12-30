# Building Data Products on ETSL — Quick Reference Card
## One-Page Cheat Sheet for Product Managers, Architects, and Engineers

**Full Document:** `building-data-products-using-etsl-data-artifacts.md`

---

## The Core Distinction

| | ETSL Data Artifact | Data Product |
|---|---|---|
| **Purpose** | Stabilize enterprise truth | Serve a use case |
| **Authority** | Explicitly modeled | Inherited from ETSL |
| **Evolution** | Slow, governed | Fast, product-team-owned |
| **Reconciliation** | Happens here | Does NOT happen here |

> **Data Products interpret truth. They do not define it.**

---

## Data Product Types

| Type | Example | Change Cadence |
|------|---------|----------------|
| **Analytical** | Credit portfolio dashboard | Slow |
| **Consumer-Aligned** | Customer 360 view | Moderate |
| **Feature-Oriented** | ML fraud features | Fast |
| **Operationally-Consumed** | Real-time decisioning input | Critical |

---

## Builder Checklist (Before Release)

| # | Checkpoint |
|---|------------|
| 1 | ETSL Data Artifacts identified for cross-domain truth |
| 2 | Lineage preserved (outputs → ETSL artifacts) |
| 3 | Temporal pattern explicit (current / as-of / history) |
| 4 | Authority metadata not discarded |
| 5 | Semantic contract inherited, not redefined |
| 6 | Freshness expectations documented |
| 7 | Tier-2 classification declared |
| 8 | Escalation path defined for semantic gaps |

---

## Consumer Checklist (Before Adoption)

| # | Checkpoint |
|---|------------|
| 1 | Product consumes ETSL for truth-sensitive inputs |
| 2 | Freshness bounds acceptable |
| 3 | Temporal assumptions match use case |
| 4 | Lineage documentation available |
| 5 | Contract versioning understood |
| 6 | Escalation path known |

---

## DO vs DON'T

| ✅ DO (Allowed Interpretations) | ❌ DON'T (Architectural Violations) |
|--------------------------------|-------------------------------------|
| Derive aggregates (sum limits) | Override authoritative facts |
| Calculate indicators (utilization ratio) | Fix perceived data issues locally |
| Apply segmentation/filters | Silently reinterpret semantics |
| Reshape for consumers | Apply undocumented reconciliation |
| Add derived labels ("high value") | Discard authority metadata |
| Compute time-based trends | Flatten temporal semantics |

---

## When to ESCALATE (Not Workaround)

| Trigger | Action |
|---------|--------|
| **Semantic gap** | Propose addition to ETSL |
| **Contested definition** | Request Authority Review |
| **Authority dispute** | Request reconciliation clarification |
| **Temporal ambiguity** | Request temporal expansion |
| **Cross-product inconsistency** | Investigate consumption patterns |

> **Escalate upstream. Never fix locally.**

---

## Common Consumption Mistakes

| Mistake | Consequence |
|---------|-------------|
| Going around ETSL to SORs | No authority, no reconciliation |
| Local reconciliation logic | Divergent truth across products |
| Caching without refresh | Stale data, failed audits |
| Snapshot-only reasoning | Cannot answer "what was true on date X?" |

---

## 10 Anti-Patterns (Avoid These)

| # | Anti-Pattern | Core Problem |
|---|--------------|--------------|
| 1 | Rebuilding truth locally | Creates competing truth |
| 2 | Hiding authority in code | Breaks audit trail |
| 3 | Caching ETSL forever | Serves stale data |
| 4 | Feature stores redefining semantics | Semantic drift |
| 5 | Compliance logic diverging | Inconsistent regulatory outcomes |
| 6 | Ignoring temporal semantics | Reconstruction fails |
| 7 | Treating derived values as authoritative | No governed authority |
| 8 | Bypassing ETSL for "speed" | Technical debt compounds |
| 9 | Discarding authority metadata | Explainability fails |
| 10 | Local "fixes" to ETSL data | Two versions of truth |

---

## What "Good" First Product Looks Like

| Dimension | Criteria |
|-----------|----------|
| **Scope** | One cross-domain use case |
| **ETSL Consumption** | ≥1 ETSL Data Artifact |
| **Consumer** | Committed user before build |
| **Lineage** | Complete to ETSL sources |
| **Contract** | Documented, versioned |
| **Timeline** | 8–12 weeks |

---

## Reading Guide by Role

| Role | Focus Sections |
|------|----------------|
| **Product Manager** | 1–2, 12, 15 |
| **Architect** | 3–5, 7–9, 13 |
| **Data Engineer** | 5–6, 8, 11 |
| **CIO / Executive** | 1, 14–15 |

---

## Key Principles (Memorize These)

1. **Consume, don't recreate** — ETSL has already reconciled
2. **Interpret, don't redefine** — semantics are inherited
3. **Preserve, don't discard** — lineage and authority matter
4. **Refresh, don't cache forever** — ETSL evolves
5. **Escalate, don't workaround** — fixes belong upstream

---

## Further Reading

- ETSL and Data Mesh: `../conceptual/etsl-and-data-mesh-coexistence-guidance.md`
- Tier-2 Classifications: `../terminology/tier-2-etsl-canonical-classifications.md`
- Full Design Checklist: Appendix A of full document
- Comparison with Other Approaches: `etsl-data-products-vs-other-approaches.md`

---

