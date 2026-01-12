# Guardrails

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-11

## Overview

Seer Guardrails provide **safety constraints and enforcement** for AI agents. Guardrails operate at two levels:

1. **Behavioral Guidelines** — Advisory instructions embedded in agent prompts (not enforced programmatically)
2. **Sidecar Guardrails** — Enforcement functions that intercept and validate requests/responses

Both types are complementary: behavioral guidelines shape agent behavior, while sidecar guardrails provide programmatic enforcement.

> **Important**: Behavioral guidelines rely on LLM compliance and are advisory. Sidecar guardrails are the **actual enforcement layer**. Critical safety requirements should always have sidecar enforcement.

---

## Two-Layer Model

### Behavioral Guidelines (Prompt-Based)

Behavioral guidelines are **advisory instructions** embedded in the Training Spec that shape agent behavior. They are **not programmatically enforced** — the agent may ignore them (especially under adversarial prompting).

**Key Characteristics:**
- Specified distinctly in Training Spec
- CAE ensures they are retained in compiled context
- **Advisory only** — not enforced programmatically
- LLMs can ignore guidelines (especially with jailbreaks)
- **Must be paired with sidecar guardrails** for critical safety requirements

### Sidecar Guardrails

Sidecar guardrails are **enforcement functions** that intercept agent traffic at two points:

- **Inbound guardrails**: Execute on `/dispatch` requests coming into the agent
- **Outbound guardrails**: Execute on every Hub API call from the agent (request updates, decisions, task completions, etc.)

Outbound guardrails support **per-API configuration** with wildcard pattern matching, and each guardrail returns **Allow**, **Alert**, or **Deny**.

> **See**: [Guardrail Service Design](../subsystems/seer-sidecar/guardrail-service.md) for detailed implementation.

---

## Execution Order

Guardrails execute in a specific order:

1. **Training Spec Guardrails** (before) — Immutable, cannot be relaxed
2. **Employment Spec Guardrails** (before) — Additional restrictions only
3. **Agent Invocation**
4. **Training Spec Guardrails** (after) — Immutable
5. **Employment Spec Guardrails** (after) — Additional restrictions

**Key Principle**: Training Spec guardrails are **immutable** — they cannot be relaxed at employment time. Employment Spec guardrails can only add restrictions.

---

## Verification Pattern

For critical behavioral guidelines, add a sidecar guardrail that verifies compliance:

```yaml
# Behavioral guideline (advisory)
behavioralGuidelines:
  - name: pii-protection
    guideline: "Never include PII..."

# Sidecar enforcement (verification)
sidecarGuardrails:
  after:
    - ref: pii-detector
      config:
        mode: reject  # Enforces what the guideline advises
```

---

## Key Principles

- **Never rely solely on behavioral guidelines** for security-critical constraints
- **Always pair with sidecar enforcement** for critical safety requirements
- **Training Spec guardrails are immutable** — cannot be relaxed at employment
- **Employment Spec guardrails can only add restrictions**, never relax training guardrails

---

## Related

- [Guardrail Service Design](../subsystems/seer-sidecar/guardrail-service.md) — Detailed sidecar guardrail design
- [Seer Sidecar](../subsystems/seer-sidecar/README.md) — Sidecar subsystem overview
- [Agent Lifecycle Manager](../subsystems/agent-lifecycle-manager/README.md) — Guardrail configuration
- [Authority Enforcement](./authority-enforcement.md) — Complementary enforcement
- [ADR-0072: Guardrails Two-Layer Model](../../../olympus-hub-docs/decision-logs/0072-seer-guardrails-two-layer-model.md)

---

*For detailed sidecar guardrail implementation, see [Guardrail Service Design](../subsystems/seer-sidecar/guardrail-service.md).*
