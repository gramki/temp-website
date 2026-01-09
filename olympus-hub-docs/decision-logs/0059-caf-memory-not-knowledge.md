# ADR 0059: CAF Does Not Govern Knowledge

**Status**: Accepted  
**Date**: 2026-01-07  
**Category**: caf

---

## Context

CAF is defined as the "Enterprise Memory Control Plane." A question arose whether CAF should also govern Enterprise Knowledge (facts, rules, constraints) in addition to Enterprise Memory (episodic, semantic, procedural, preference).

The distinction between Memory and Knowledge:

| Aspect | Memory | Knowledge |
|--------|--------|-----------|
| **Nature** | Learned from experience | Asserted by authority |
| **Confidence** | Probabilistic (0-1) | Binary (true/declared) |
| **Source** | Observation, inference | Policy, definition, rule |
| **Mutability** | Can be updated as evidence changes | Versioned, governed changes |
| **Authority** | Evidence-grounded | Authority-qualified |

---

## Decision

**CAF governs Memory only. Knowledge is governed by ETSL (Enterprise Temporal Semantic Layer).**

### Scope Clarification

| CAF Governs (Memory) | ETSL Governs (Knowledge) |
|----------------------|--------------------------|
| Episodic Memory | Facts (asserted truths) |
| Semantic Memory | Rules (normative constraints) |
| Procedural Memory | Definitions (authoritative terms) |
| Preference Memory | Policies (binding guidelines) |

### Promotion Path

When learned patterns in Semantic Memory are validated and approved, they are **promoted to ETSL** via Enterprise Learning Services. This is the only pathway from Memory → Knowledge.

```
Episodic → Semantic → [Governance Review] → ETSL
```

CAF facilitates this promotion but does not own or govern the resulting ETSL assertions.

---

## Consequences

### Positive

- **Clear Boundaries**: CAF = Memory, ETSL = Knowledge
- **Appropriate Governance**: Knowledge requires different governance (authority, versioning)
- **No Scope Creep**: CAF stays focused on its core mission
- **Separation of Concerns**: Different teams can own different layers

### Negative

- Two systems to understand for full picture
- Promotion workflow spans system boundaries

### Neutral

- Enterprise Learning Services acts as the bridge between CAF and ETSL
- Semantic Memory records may reference ETSL assertions they originated from

---

## Related

- [CAF README](../04-subsystems/cognitive-audit-fabric/README.md) — CAF scope
- [Enterprise Learning Services](../04-subsystems/cognitive-audit-fabric/enterprise-learning-services.md) — Promotion to ETSL
- [Semantic Memory Store](../04-subsystems/cognitive-audit-fabric/semantic-memory-store/README.md) — Memory vs Knowledge distinction


