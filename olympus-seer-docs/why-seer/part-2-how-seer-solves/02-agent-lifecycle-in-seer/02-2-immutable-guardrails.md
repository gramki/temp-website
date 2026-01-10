# 2.2 Immutable Training Guardrails

A critical security property of Seer is that guardrails defined in Training Specifications cannot be bypassed by Employment Specifications. This section explains how Seer enforces this immutability.

## The Enforcement Mechanism

### Specification-Time Validation

When an Employment Specification is submitted, Seer validates it against the referenced Training Specification:

1. **Schema Validation:** Employment Spec must reference a valid Training Spec version
2. **Constraint Validation:** All Employment constraints must be subsets of Training constraints
3. **Guardrail Preservation:** Guardrails from Training must be preserved

If validation fails, the Employment Specification is rejected with specific error messages indicating the violation.

### Runtime Enforcement

Even if a malformed Employment Specification were to enter the system, runtime enforcement provides a second layer of protection:

1. **Guardrail Evaluation:** Before any agent action, guardrails are evaluated
2. **Training Authority:** Guardrail evaluation uses Training Spec as authoritative source
3. **Block and Alert:** Guardrail violations block the action and generate alerts

### Sidecar Pattern

Guardrail enforcement uses a sidecar pattern—evaluation happens independently from the primary agent reasoning loop:

```
┌─────────────────────────────────────────────────────────┐
│                    AGENT POD                             │
│                                                          │
│   ┌──────────────────┐    ┌──────────────────────────┐  │
│   │   Agent Container │    │   Guardrail Sidecar      │  │
│   │                   │    │                          │  │
│   │   Reasoning       │───▶│   Evaluate guardrails    │  │
│   │   + Tool calls    │    │   from Training Spec     │  │
│   │                   │◀───│                          │  │
│   │   (blocked if     │    │   Block or Allow         │  │
│   │    violation)     │    │   + Audit log            │  │
│   └──────────────────┘    └──────────────────────────┘  │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

The sidecar cannot be bypassed by the agent container because:
- All actions must pass through the sidecar
- The sidecar has read-only access to Training Spec
- The sidecar operates in a separate security context

## What Immutability Guarantees

### Security Certification

Organizations can certify a Training Specification and trust that certification applies to all valid Employment configurations:
- Red team a Training Spec once
- Deploy with confidence across environments
- Audit against Training Spec, not Employment variations

### Accountability Clarity

When violations occur, the investigation is clear:
- **Guardrail worked:** Agent was blocked from inappropriate action
- **Guardrail failed:** Training Spec defect (requires Training update)
- **Guardrail bypassed:** Security incident (system compromise)

Employment configuration cannot be the source of guardrail failure.

### Regulatory Defensibility

For regulated industries:
- Training Spec becomes the auditable artifact
- Employment variations do not change risk profile
- Compliance sign-off applies to Training, not each deployment

## What Employment Can Still Do

Employment Specifications can specialize without violating immutability:

| Employment Can | Example |
|----------------|---------|
| **Restrict tools** | Training allows 5 tools; Employment uses 2 |
| **Narrow scope** | Training covers all disputes; Employment covers refunds only |
| **Add constraints** | Training has $1000 ceiling; Employment sets $500 ceiling |
| **Specify environment** | Training defines protocol; Employment binds to specific endpoint |
| **Allocate resources** | Training has no budget; Employment sets $500/month |

None of these weaken the guardrails—they only narrow the operational envelope.

## Implementation Details

### Guardrail Reference Structure

Guardrails are referenced by stable identifiers:

```yaml
guardrails:
  - ref: safety/no-financial-advice
    version: "^1.0.0"
  - ref: compliance/data-privacy
    version: "~2.1.0"
  - ref: operations/escalation-required
    version: ">=1.0.0"
```

### Guardrail Evaluation API

At runtime, the sidecar evaluates each action:

```python
evaluation = guardrail_service.evaluate(
    action=proposed_action,
    training_spec=agent.training_spec,
    context=current_context
)

if evaluation.blocked:
    audit_service.log_guardrail_block(evaluation)
    raise GuardrailViolationError(evaluation.reason)
```

### Audit Trail

All guardrail evaluations are logged:
- Action proposed
- Guardrails evaluated
- Result (allow/block)
- Reason if blocked
- Timestamp and agent identity

This creates a defensible record of guardrail enforcement.

---

**References:**
*   `aosm-meta-model/raw-trained-employed-agents.md` — Section on guardrail immutability
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-2-immutability-principle.md`
