# ADR-0087: Idea-Intent-Charter Model for Automation Ideation

> **Status:** Accepted  
> **Date:** 2026-01-09  
> **Category:** ideation

---

## Context

Automation initiatives need a structured path from initial concept to design. Without structure:

1. **Ideas are lost** — good suggestions from operations never reach decision-makers
2. **No business case** — development starts without clear value justification
3. **Unclear handoffs** — when does design start? Who commits to what?
4. **No traceability** — can't track value realization back to original intent

The challenge was defining a model that:
- Captures ideas from anyone (agents, supervisors, APO)
- Formalizes business cases (APO responsibility)
- Creates design contracts (APO + PA agreement)
- Tracks outcomes back to original intent

---

## Decision

### Three-Entity Model: Idea → Intent → Charter

We define three distinct entities representing the ideation lifecycle:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    IDEATION LIFECYCLE                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  IDEA                    INTENT                   CHARTER                   │
│  (Anyone)                (APO)                    (APO + PA)                │
│                                                                              │
│  ┌─────────────┐        ┌─────────────┐         ┌─────────────┐            │
│  │  Raw        │  APO   │  Business   │   PA    │  Design     │            │
│  │  Opportunity│──────▶ │  Case +     │────────▶│  Contract   │──▶ Workbench
│  │             │ Review │  Success    │ Accepts │             │            │
│  │             │        │  Criteria   │         │             │            │
│  └─────────────┘        └─────────────┘         └─────────────┘            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Entity Definitions

| Entity | Definition | Owner | Creates |
|--------|------------|-------|---------|
| **Idea** | Raw automation opportunity — problem, observation, or suggestion | Anyone (submitted) | Anyone |
| **Intent** | Formalized business case with success criteria and approach | APO | APO (from ideas or directly) |
| **Charter** | Intent accepted by PA — design contract to proceed | APO + PA | Created when PA accepts Intent |

### Key Transitions

| Transition | Trigger | Owner |
|------------|---------|-------|
| Idea → Intent | APO reviews and promotes | APO |
| Intent → Charter | PA accepts Intent | PA (acceptance) |
| Charter → Workbench | Design begins | APO initiates |

### Idea Sources

Ideas can come from:
- Agents (from task context)
- Supervisors (from operational patterns)
- Auditors (from compliance observations)
- Production Feedback (suggestions promoted)
- APO (direct business insight)

### Intent Contents

Intent captures:
- Problem statement and value proposition
- Success criteria with measurable KPIs
- Scope (in/out)
- Automation approach (conventional/agentic/hybrid)
- Stakeholders (sponsor, accountable)

### Charter Significance

A Charter represents:
- PA's commitment to design
- Agreed approach
- Target timeline
- Workbench initiation trigger

---

## Consequences

### Positive

1. **Ideas are captured** — anyone can submit, nothing is lost
2. **Business justification required** — Intent enforces business case
3. **Clear handoff** — Charter marks PA commitment
4. **Traceability** — Outcome → Charter → Intent → Ideas
5. **Feedback loop** — Suggestions from operations become Ideas

### Negative

1. **Process overhead** — three stages may feel bureaucratic for small changes
2. **Learning curve** — new terminology to understand

### Neutral

1. **APO gate** — APO decides what becomes Intent (filter, not bottleneck)
2. **PA acceptance** — PA can request clarification before accepting

---

## Alternatives Considered

### 1. Single "Charter" Entity

Use only Charter, created directly by APO.

**Rejected because:**
- Loses idea capture from operations
- No distinction between informal ideas and formal business cases
- No explicit PA acceptance

### 2. Two Entities (Idea → Charter)

Skip Intent, go directly from Idea to Charter.

**Rejected because:**
- Charter implies PA acceptance
- APO's business case work needs a separate stage
- Intent is APO's domain before PA involvement

### 3. Workflow States on Single Entity

Single "Proposal" entity with states: Idea → Intent → Charter.

**Rejected because:**
- Different personas own different stages
- Different schemas needed at each stage
- Cleaner with separate entities

---

## Related Documentation

- [Automation Ideation Subsystem](../04-subsystems/automation-ideation/README.md)
- [Idea Management](../04-subsystems/automation-ideation/idea-management.md)
- [Intent Formalization](../04-subsystems/automation-ideation/intent-formalization.md)
- [Charter Acceptance](../04-subsystems/automation-ideation/charter-acceptance.md)
- [Automation Product Desk](../06-ux-architecture/tenant-domain/automation-product-desk.md)
- [ADR-0082: Hub Desk Restructuring](./0082-hub-desk-restructuring.md)

