# ADR-0083: Automation Product Owner as Hub Persona

> **Status:** Accepted  
> **Date:** 2026-01-09  
> **Category:** personas

---

## Context

The **Product Owner** role for automation capabilities was initially named "Agent Product Owner (APO)" and documented in Seer, implying ownership of AI agent-based automation.

However, analysis revealed:

1. **Automation scope is broader** — APO should own business intent for *all* automation, not just agentic
2. **Conventional automation needs product ownership too** — rule-based workflows need business justification
3. **Automation approach is a downstream decision** — whether to use agents or conventional automation is decided *after* the business case is established
4. **Hub is the foundation** — all automation starts in Hub; Seer extends for agentic scenarios

---

## Decision

### 1. Rename to "Automation Product Owner"

Change the role name from "Agent Product Owner" to **"Automation Product Owner"** to reflect broader scope.

| Aspect | Before | After |
|--------|--------|-------|
| **Name** | Agent Product Owner | Automation Product Owner |
| **Acronym** | APO (unchanged) | APO (unchanged) |
| **Scope** | AI agent automation | All automation types |

### 2. Define as Hub Persona

APO is a **Hub persona**, not a Seer persona:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    APO PERSONA SCOPE                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  APO Owns (Hub)                           Seer Extensions                   │
│  ─────────────                            ───────────────                   │
│                                                                              │
│  • Business intent for automation         • Agent-specific KPIs             │
│  • Success criteria and KPIs              • Autonomy proposals              │
│  • Automation approach proposal           • Agent evaluation criteria       │
│  • Improvement prioritization                                               │
│  • Production feedback review                                               │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                      │   │
│  │   CONVENTIONAL PATH            │            AGENTIC PATH            │   │
│  │   (Hub only)                   │            (Hub + Seer)            │   │
│  │                                │                                    │   │
│  │   APO → PA → Developer →       │   APO → PA → CSA → AE → ARE →     │   │
│  │   Supervisor                   │   Supervisor                       │   │
│  │                                │                                    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3. Automation Approach Decision

APO proposes whether automation should be:
- **Conventional** — rule-based, deterministic (stays in Hub)
- **Agentic** — AI-based, requires judgment (transitions to Seer)
- **Hybrid** — combination of both

This proposal is validated by Process Architect (for feasibility) and CSA (for agentic viability).

---

## Consequences

### Positive

1. **Unified ownership** — one persona owns business intent for all automation
2. **Clear lifecycle** — APO initiates, approach is decided, then paths diverge
3. **Hub foundation** — Hub documentation is complete without Seer dependency
4. **Consistent naming** — "Automation" aligns with Hub's automation focus

### Negative

1. **Documentation updates** — references to "Agent Product Owner" need updating
2. **Seer documentation** — APO extensions in Seer need clear boundary

### Neutral

1. **Acronym preserved** — APO remains unchanged
2. **Same person** — in practice, often the same individual in both contexts

---

## Alternatives Considered

### 1. Separate Personas (APO for Agents, PPO for Process)

Have "Agent Product Owner" for agentic and "Process Product Owner" for conventional.

**Rejected because:**
- Artificial split — automation intent is unified
- Unclear ownership when switching approaches
- More roles to understand

### 2. Keep APO in Seer Only

Let Hub scenarios lack formal product ownership.

**Rejected because:**
- All automation needs business justification
- Conventional automation still needs success criteria
- Gap in Hub's persona model

---

## Related Documentation

- [Automation Product Owner Persona](../08-personas-and-journeys/personas/automation-product-owner.md)
- [Automation Lifecycle Journey](../08-personas-and-journeys/journeys/automation-lifecycle.md)
- [ADR-0082: Hub Desk Restructuring](./0082-hub-desk-restructuring.md)

