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

Sidecar guardrails are **enforcement functions** that execute before and/or after agent invocation:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      SIDECAR GUARDRAIL PIPELINE                               │
│                                                                               │
│   ┌─────────────┐                                                            │
│   │   Request   │                                                            │
│   └──────┬──────┘                                                            │
│          │                                                                    │
│          ▼                                                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    BEFORE GUARDRAILS                                 │   │
│   │   Can: Transform request, Reject, Add context                        │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│          │                                                                    │
│          ▼                                                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    AGENT INVOCATION                                  │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│          │                                                                    │
│          ▼                                                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    AFTER GUARDRAILS                                  │   │
│   │   Can: Transform response, Reject, Redact                            │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
```

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

- `subsystems/seer-sidecar/README.md` - Seer Sidecar subsystem (guardrail execution)
- `subsystems/agent-lifecycle-manager/README.md` - Guardrail configuration in Training/Employment Specs
- `implementation-concepts/authority-enforcement.md` - Authority enforcement (complementary to guardrails)

---

*For detailed implementation, see `subsystems/guardrails.md` (to be migrated to `subsystems/seer-sidecar/`).*
