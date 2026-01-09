# ADR-0072: Seer Guardrails Two-Layer Model

**Status**: Accepted  
**Date**: 2026-01-08  
**Category**: seer

---

## Context

AI agents require guardrails to ensure safe, compliant, and controlled behavior. There are multiple approaches:
1. Prompt-only guardrails (system prompts)
2. Code-based enforcement (hardcoded rules)
3. Sidecar/gateway enforcement (runtime interception)
4. Hybrid approaches

We needed to decide how Seer should implement guardrails for Employed Agents.

---

## Decision

Seer uses a **two-layer guardrail model**:

### Layer 1: Behavioral Guidelines (Prompts)
- Defined in Training Spec as `behavioralGuidelines`
- Advisory in nature — LLM may ignore
- Compiled into agent context by Context Assembly Engine
- Retained in all LLM interactions

### Layer 2: Sidecar Guardrails (Enforcement)
- Deployed as Istio sidecars in agent pods
- Execute "before" and "after" agent actions
- Can transform, reject, or redact requests/responses
- Implemented as Python libraries in OCI images
- Publish error codes with human-readable descriptions

### Enforcement Pipeline

```
Request → Before Guardrails → Agent → After Guardrails → Response
              (reject/transform)        (redact/validate)
```

### Configuration

- **Training Spec**: Defines guardrail references and base configuration (immutable once published)
- **Employment Spec**: Can add stricter guardrails, never relax
- **Failure Policy**: Per-guardrail (`deny` or `allow` with justification)

---

## Consequences

### Positive
- Behavioral guidelines integrate naturally with LLM workflows
- Sidecar enforcement provides hard guarantees
- Stateless sidecars are easy to scale and test
- Istio deployment leverages existing service mesh
- Failure policies allow risk-appropriate responses

### Negative
- Two layers add complexity in understanding guardrail behavior
- Sidecar guardrails add latency (mitigated by parallelization)
- LLM-based guardrails are expensive (must be used sparingly)

### Neutral
- Developers must understand both layers
- Guardrails best practices guide needed

---

## Related

- [Guardrails Subsystem](../../olympus-seer-docs/seer-design/subsystems/guardrails.md)
- [Guardrails Best Practices Guide](../../olympus-seer-docs/seer-design/guides/guardrails-best-practices.md)
- [Training Spec CRD](../../olympus-seer-docs/seer-design/hub-integration/training-spec-crd.md)

