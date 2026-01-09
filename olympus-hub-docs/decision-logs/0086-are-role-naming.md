# ADR-0086: Agent Reliability Engineer (ARE) Role Naming

> **Status:** Accepted  
> **Date:** 2026-01-09  
> **Category:** personas

---

## Context

Seer defines a role responsible for the operational health, cost efficiency, and reliability of AI agents in production. This role was initially named "AI Reliability Engineer (AIRE)."

Questions arose about the appropriate naming:

1. **AI vs Agent** — is the focus on AI technology or on agents specifically?
2. **Industry alignment** — should we use established SRE naming patterns?
3. **Domain specificity** — should the name reflect agentic systems?

---

## Decision

### Name: Agent Reliability Engineer (ARE)

Rename the role from "AI Reliability Engineer (AIRE)" to **"Agent Reliability Engineer (ARE)"**.

| Aspect | Before | After |
|--------|--------|-------|
| **Name** | AI Reliability Engineer | Agent Reliability Engineer |
| **Acronym** | AIRE | ARE |
| **Focus** | AI technology | Agent systems |

### Rationale: "Agentic is Different from AI"

The distinction matters:

| Aspect | AI (Broad) | Agentic (Specific) |
|--------|------------|-------------------|
| **Scope** | Any AI/ML model | Autonomous agents with goals |
| **Concerns** | Model accuracy, inference | Autonomy, decisions, actions |
| **Observability** | Model metrics | OPD (Observability, Predictability, Directability) |
| **Reliability** | Uptime, latency | Behavioral consistency, outcome quality |

ARE focuses on **agent-specific** concerns, not general AI/ML operations:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ARE FOCUS AREAS                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  AGENT-LEVEL                              AOS-LEVEL (Agent-Oriented System) │
│  ───────────                              ─────────                          │
│                                                                              │
│  • Agent Health Score (AHS)               • System-wide AHS                  │
│  • Action quality                         • Cost-to-Health Ratio (CHR)       │
│  • Task completion                        • Cascade detection                │
│  • Behavioral bounds                      • Cross-agent patterns             │
│  • Cost attribution                       • Resource allocation              │
│                                                                              │
│  NOT IN SCOPE (Platform Provider):                                           │
│  • Model serving infrastructure                                              │
│  • GPU cluster management                                                    │
│  • LLM provider SLAs                                                         │
│  • Base model performance                                                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Key Metrics Renamed

As part of this decision, associated metrics were also renamed for clarity:

| Before | After | Rationale |
|--------|-------|-----------|
| Operational Outcome Score (OOS) | **Agent Health Score (AHS)** | "Health" is intuitive; OOS was too operational |
| Cost-to-Operation Ratio (COR) | **Cost-to-Health Ratio (CHR)** | Aligns with AHS terminology |

---

## Consequences

### Positive

1. **Domain specificity** — "Agent" clearly scopes to agentic systems
2. **Conceptual clarity** — distinguishes from general AI/ML ops
3. **Consistent naming** — aligns with Agent Engineer (AE), Agent-Oriented Systems (AOS)
4. **Memorable acronym** — ARE is shorter than AIRE

### Negative

1. **Documentation updates** — references to AIRE need updating
2. **Industry unfamiliarity** — "ARE" is not yet an established industry term

### Neutral

1. **Platform provider clarity** — explicitly excludes infrastructure concerns
2. **Seer-specific role** — only appears in Seer documentation

---

## Alternatives Considered

### 1. Keep AIRE (AI Reliability Engineer)

Maintain the original name with "AI" prefix.

**Rejected because:**
- "AI" is too broad — covers all ML, not just agents
- Conflates agent reliability with model reliability
- Platform infrastructure is handled by provider

### 2. Agent SRE

Use "Agent Site Reliability Engineer" for industry alignment.

**Rejected because:**
- "Site" doesn't apply to agent systems
- "SRE" has specific infrastructure connotations
- ARE maintains reliability focus without baggage

### 3. AOS Reliability Engineer

Use "Agent-Oriented System Reliability Engineer."

**Rejected because:**
- Too long
- "ARE" already implies AOS context
- Acronym would be unclear

---

## Related Documentation

- [Agent Reliability Engineer (ARE) Persona](../../olympus-seer-docs/seer-design/personas-and-needs/are.md)
- [Seer Roles Overview](../../olympus-seer-docs/seer-design/personas-and-needs/roles.md)
- [Agent Health Score (AHS)](../../olympus-seer-docs/seer-design/personas-and-needs/are.md#agent-health-score-ahs)

