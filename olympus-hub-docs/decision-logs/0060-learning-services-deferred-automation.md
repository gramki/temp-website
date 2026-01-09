# ADR 0060: Enterprise Learning Services — Deferred Automation

**Status**: Accepted  
**Date**: 2026-01-07  
**Category**: caf

---

## Context

Enterprise Learning Services is responsible for promoting memory across the ESPP hierarchy (Episodic → Semantic/Procedural/Preference → ETSL). This involves pattern detection, evidence packaging, governance workflows, and conflict resolution.

The question arose: how much automation should be specified now?

---

## Decision

**Enterprise Learning Services is designed as a manual, human-supervised process initially.** Automation will be introduced incrementally after Hub adoption matures over several cycles.

### What Is Specified

| Aspect | Status |
|--------|--------|
| Promotion hierarchy | ✅ Defined |
| Promotion flows (all 4 paths) | ✅ Defined |
| Promotion types and triggers | ✅ Defined |
| Configurable criteria | ✅ Defined |
| API sketch (endpoints) | ✅ Defined |
| Conflict resolution strategies | ✅ Defined |

### What Is Intentionally Deferred

| Aspect | Reason |
|--------|--------|
| Pattern detection algorithms | Requires operational experience |
| Automated promotion workflows | Premature automation |
| ML for pattern recognition | Over-engineering before adoption |
| Governance workflow automation | Varies by organization |
| Conflict detection algorithms | Need real-world examples |
| Rollback automation | Manual sufficient initially |

### Phased Approach

**Phase 1 (Initial Adoption):**
- Analysts manually identify patterns
- Promotion candidates flagged via UI/reports
- Governance review via existing workflows
- ETSL promotion via manual assertion authoring

**Phase 2 (Maturity):**
- Pattern detection surfaced as suggestions
- Semi-automated evidence packaging
- Integrated governance workflow

**Phase 3 (Full Automation — Future):**
- Automated pattern detection with thresholds
- Auto-promotion for low-risk patterns
- Continuous monitoring and anomaly detection

---

## Consequences

### Positive

- **No Premature Optimization**: Wait for real usage patterns
- **Organizational Flexibility**: Let each org define their governance
- **Lower Initial Complexity**: Simpler to adopt and understand
- **Learn Before Automating**: Manual processes reveal what's worth automating

### Negative

- Initial adoption requires more human effort
- No out-of-box automation for early adopters

### Neutral

- Conceptual design is complete and stable
- Implementation can proceed incrementally

---

## Related

- [Enterprise Learning Services](../04-subsystems/cognitive-audit-fabric/enterprise-learning-services.md) — Full design
- [ADR 0059](./0059-caf-memory-not-knowledge.md) — CAF/ETSL boundary


