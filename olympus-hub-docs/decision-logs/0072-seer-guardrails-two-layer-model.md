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
- **Inbound guardrails**: Execute on `/dispatch` requests coming into the agent
- **Outbound guardrails**: Execute on every Hub API call from the agent (request updates, decisions, task completions, etc.)
- Outbound guardrails support per-API configuration with wildcard pattern matching
- Guardrail responses: **Allow**, **Alert**, **Deny**
- Each guardrail processor defines its own configuration schema for alert/deny behavior
- Implemented as Python libraries in OCI images
- Publish error codes with human-readable descriptions
- Failure policy: Defaults to **Deny** (fail-closed)

### Enforcement Pipeline

```
Inbound:
  Dispatch Request → Inbound Guardrails (Allow/Alert/Deny) → Agent

Outbound:
  Agent → Hub API Call → Outbound Guardrails (pattern-matched, Allow/Alert/Deny) → Hub API
```

### Configuration

- **Training Spec**: Defines guardrail references and base configuration (immutable once published)
- **Employment Spec**: Can add stricter guardrails, never relax
- **Per-API Configuration**: Outbound guardrails can be configured per API endpoint with wildcard patterns
- **Failure Policy**: Guardrail failure defaults to Deny (fail-closed)

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

- [Guardrail Service Design](../../olympus-seer-docs/seer-design/subsystems/seer-sidecar/guardrail-service.md)
- [Guardrails Concepts](../../olympus-seer-docs/seer-design/implementation-concepts/guardrails.md)
- [Guardrails Best Practices Guide](../../olympus-seer-docs/seer-design/guides/guardrails-best-practices.md)
- [Training Spec CRD](../../olympus-seer-docs/seer-design/hub-integration/training-spec-crd.md)

