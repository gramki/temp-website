# ADR-0084: Automation Lifecycle Split (Conventional vs Agentic)

> **Status:** Accepted  
> **Date:** 2026-01-09  
> **Category:** journeys

---

## Context

Hub initially documented a unified "Automation Lifecycle" journey that covered both conventional and agentic automation paths. This created several issues:

1. **Seer dependencies in Hub docs** — Hub documentation referenced Seer personas (CSA, AE, ARE)
2. **Conflated paths** — readers couldn't clearly see which steps applied to which approach
3. **Hub self-sufficiency** — Hub should be fully documented without requiring Seer
4. **Decision point unclear** — when and how the "agentic path" diverged was ambiguous

---

## Decision

### Split into Two Distinct Lifecycle Documents

#### 1. Conventional Automation Lifecycle (Hub)

Location: `olympus-hub-docs/08-personas-and-journeys/journeys/automation-lifecycle.md`

**Personas:** APO, Process Architect, Developer, Supervisor

**Stages:** Design → Build → Deploy → Run → Evolve

**Characteristics:**
- Deterministic, rule-based automation
- No AI agents
- Hub-only personas and capabilities
- Complete without Seer reference

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CONVENTIONAL AUTOMATION LIFECYCLE                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  DESIGN                BUILD                DEPLOY                           │
│  ─────────            ──────               ─────────                         │
│  APO: Charter         Developer:           Supervisor:                       │
│  PA: Scenarios        Hub App              Queue config                      │
│  PA: SOPs             Triggers             Agent enrollment                  │
│                       Tests                Activation                        │
│                                                                              │
│  RUN                  EVOLVE                                                │
│  ─────                ───────                                               │
│  Agents:              Feedback to APO                                       │
│  Task completion      APO: Prioritize                                       │
│  Supervisor:          Next iteration                                        │
│  Monitor, intervene                                                         │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  FORK POINT: If agentic approach selected in Design stage,           │  │
│  │  transition to Seer's Agentic Automation Lifecycle                   │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 2. Agentic Automation Lifecycle (Seer)

Location: `olympus-seer-docs/seer-design/personas-and-needs/journeys/agentic-automation-lifecycle.md`

**Personas:** APO, CSA, AE, KMO, ARE, COS, ARAO (with Hub personas supporting)

**Stages:** Extends conventional lifecycle with agent-specific concerns

**Characteristics:**
- AI agent-based automation
- Seer personas and capabilities
- Builds on Hub foundation
- References Hub for operational infrastructure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AGENTIC AUTOMATION LIFECYCLE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  From Hub:           Agent Design          Agent Build                       │
│  ─────────           ─────────────         ───────────                       │
│  APO: Charter        CSA: Architecture     AE: Implementation                │
│  PA: Scenarios       CSA: Autonomy model   AE: Training specs                │
│                                            KMO: Knowledge prep               │
│                                                                              │
│  Agent Deploy        Agent Run             Agent Evolve                     │
│  ────────────        ─────────             ────────────                     │
│  ARE: Operability    ARE: Monitoring       COS: Pattern detection           │
│  Supervisor: Queues  COS: Cognitive health ARE: Tuning                      │
│                      ARAO: Audit           ARAO: Compliance review          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Fork Point

The **automation approach decision** occurs in the Design stage:

| Decision | Owner | Next Step |
|----------|-------|-----------|
| Conventional | APO + PA | Continue in Hub lifecycle |
| Agentic | APO + PA + CSA | Transition to Seer lifecycle |
| Hybrid | APO + PA + CSA | Define boundaries, parallel paths |

---

## Consequences

### Positive

1. **Hub self-sufficiency** — Hub docs complete without Seer dependency
2. **Clear paths** — readers know exactly which lifecycle applies
3. **Persona clarity** — Hub lifecycle uses Hub personas only
4. **Better onboarding** — can learn Hub first, then Seer

### Negative

1. **Two documents** — maintain two lifecycle journeys
2. **Cross-reference needed** — Seer doc references Hub foundation

### Neutral

1. **Fork point documented** — explicit transition point
2. **Shared foundation** — APO, PA, Supervisor appear in both

---

## Alternatives Considered

### 1. Single Document with Conditional Sections

One document with "if agentic, do X; if conventional, do Y" sections.

**Rejected because:**
- Harder to read
- Conditional logic obscures the core flow
- Different audiences (Hub-only vs Hub+Seer users)

### 2. Keep Everything in Hub

Document agentic lifecycle in Hub with Seer references.

**Rejected because:**
- Hub shouldn't depend on Seer conceptually
- Seer owns its personas and journeys
- Blurs product boundaries

---

## Related Documentation

- [Automation Lifecycle (Hub)](../08-personas-and-journeys/journeys/automation-lifecycle.md)
- [Agentic Automation Lifecycle (Seer)](../../olympus-seer-docs/seer-design/personas-and-needs/journeys/agentic-automation-lifecycle.md)
- [ADR-0083: APO as Hub Persona](./0083-apo-as-hub-persona.md)

