# ADR-0077: Seer Agent Evaluation Deferred to Post-MVP

**Status**: Accepted (Deferred)  
**Date**: 2026-01-08  
**Category**: seer

---

## Context

AI agents require evaluation and testing infrastructure for:
- Validating agent behavior before deployment
- CI/CD quality gates
- Regression testing
- Deterministic replay for debugging

We considered whether to include Agent Evaluation in the initial Seer design.

---

## Decision

Agent Evaluation subsystem is **deferred to post-MVP**. The following capabilities are parked:

| Gap ID | Capability | Status |
|--------|------------|--------|
| SEER-EVL-001 | Agent Evaluation Service API | PARKED |
| SEER-EVL-002 | CI/CD integration for agent testing | PARKED |
| SEER-EVL-003 | Sandbox environment provisioning | PARKED |
| SEER-EVL-004 | Deterministic replay harness | PARKED |

### Rationale

1. **Evaluation patterns are immature**: The industry has not converged on best practices for agent evaluation. Premature design risks obsolescence.

2. **MVP focus**: Initial deployment prioritizes core agent lifecycle, not advanced testing. Manual evaluation is acceptable for early adopters.

3. **Dependency on production experience**: Effective evaluation requires understanding of real-world failure modes, which we lack before production.

4. **Framework diversity**: Different agentic frameworks have different testing idioms. Imposing a standard may conflict.

### Interim Approach

- Developers use their framework's native testing tools
- Manual validation in development workbenches
- Observability-based monitoring in production

---

## Consequences

### Positive
- Faster MVP delivery
- Avoids premature standardization
- Resources focused on core runtime

### Negative
- No automated quality gates for agents
- Higher risk of production issues
- Manual validation is error-prone

### Neutral
- Training Spec includes placeholder for `evaluationConfig`
- Sandbox environment concept defined (provisioning deferred)
- Replay harness depends on CAF episodic record completeness

---

## Future Work (Post-MVP)

When Agent Evaluation is prioritized:
1. Survey production failure modes
2. Analyze framework-specific testing patterns
3. Design replay harness using CAF episodic records
4. Define evaluation service API
5. Integrate with Hub CI subsystem

---

## Related

- [GAPS.TODO — Seer Agent Evaluation](../aosm-and-hub/GAPS.TODO)
- [Training Spec CRD — evaluationConfig](../../olympus-seer-docs/seer-design/hub-integration/training-spec-crd.md)
- [Hub CI Subsystem](../04-subsystems/ci-subsystem/README.md)

