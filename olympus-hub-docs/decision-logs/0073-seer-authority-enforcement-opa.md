# ADR-0073: Seer Authority Enforcement via OPA

**Status**: Accepted  
**Date**: 2026-01-08  
**Category**: seer

---

## Context

Employed Agents operate with delegated authority from humans. We needed to decide how to enforce authority limits at runtime, preventing agents from exceeding their authorized scope (e.g., approving transactions above their limit, accessing unauthorized resources).

Options considered:
1. Prompt-only (advisory, not enforceable)
2. Application-level enforcement (inconsistent)
3. Gateway-level enforcement (centralized)
4. Hybrid (multiple enforcement points)

---

## Decision

Authority enforcement uses **OPA (Open Policy Agent) policies** at two enforcement points:

### Enforcement Point 1: Tool Gateway
- Validates every tool invocation against policies
- Policies from: Tool Specification + Training Spec + Employment Spec
- Employment Spec overrides Training Spec
- Has access to: Agent IAM context, tool parameters, request context

### Enforcement Point 2: Signal Exchange
- Validates every `REQUEST_UPDATE` from agents
- Any agent update can be subject to policy
- Rejected updates are recorded (not discarded) with status `rejected`

### OPA Decision Format

```json
{
  "decision": "ALLOW | ALERT | REJECT",
  "reason_code": "string",
  "reason": "human-readable description"
}
```

### Violation Handling
- All violations recorded on the Request
- Observers notified via `REQUEST_UPDATE`
- Accountable person (IAM user/group) notified
- Workbench Observation created

---

## Consequences

### Positive
- Centralized, auditable policy enforcement
- OPA is industry-standard, well-understood
- Violations are recorded for audit
- Multiple enforcement points provide defense-in-depth
- Accountable humans are always notified

### Negative
- OPA adds latency to every tool call
- Policy complexity can grow
- Developers must define `opaContextSchema` for tools

### Neutral
- Outer agent responsible for sub-agent compliance (compound agents)
- Corrective actions are context-specific (task queue vs. application)

---

## Related

- [Authority Enforcement Subsystem](../../olympus-seer-docs/seer-design/subsystems/authority-enforcement.md)
- [Registry Services — OPA Context Schema](../04-subsystems/registry-services/README.md#tool-specification-requirements)
- [Employment Spec CRD](../../olympus-seer-docs/seer-design/hub-integration/employment-spec-crd.md)

