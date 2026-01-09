# Automation Ideation

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-09  
> **ADR:** [0087](../../decision-logs/0087-idea-intent-charter-model.md)

---

## Overview

**Automation Ideation** manages the lifecycle from raw automation opportunities (Ideas) through formalized business cases (Intents) to design contracts (Charters). This subsystem captures the "why" of automation before the "how" begins.

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

---

## Key Concepts

| Term | Definition | Owner |
|------|------------|-------|
| **Idea** | Raw automation opportunity — problem, observation, or suggestion | Anyone (submitted) |
| **Intent** | Formalized business case with success criteria and approach | APO (created) |
| **Charter** | Intent accepted by PA — design contract to proceed | APO + PA (agreed) |

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Idea Management](./idea-management.md) | Capture, review, and triage ideas | 🟡 Draft |
| [Intent Formalization](./intent-formalization.md) | APO creates and refines intents | 🟡 Draft |
| [Charter Acceptance](./charter-acceptance.md) | PA accepts intent, design begins | 🟡 Draft |
| [Outcome Tracking](./outcome-tracking.md) | Measure success, feed back to ideas | 🟡 Draft |

---

## Why Ideation?

| Problem | Solution |
|---------|----------|
| Automation built without business justification | Ideas require formalization to Intents |
| No clear success criteria | Intents define measurable KPIs |
| Design starts without agreement | Charters require PA acceptance |
| No feedback loop | Outcomes feed back to new Ideas |

---

## Integration Points

| Component | Integration |
|-----------|-------------|
| **Feedback Services** | Suggestions promoted to Ideas |
| **Automation Product Desk** | APO manages Ideas, Intents, Charters |
| **Scenario Design Desk** | PA receives Charters for design |
| **Workbench Management** | Charters trigger Workbench creation |
| **Hub Analytics** | Outcome tracking and KPI dashboards |

---

## Lifecycle Flow

### 1. Idea Submission (Anyone)

Ideas can come from any source:

| Source | Example |
|--------|---------|
| **Agent** | "This manual step could be automated" |
| **Supervisor** | "We have a pattern that should be handled" |
| **Business User** | "I wish I could do X without waiting" |
| **Production Feedback** | Suggestion promoted to Idea |
| **APO** | Direct insight from business analysis |

### 2. Idea Review (APO)

APO triages ideas:

| Outcome | Action |
|---------|--------|
| **Promote** | Convert to Intent (formalize) |
| **Park** | Good idea, not now (backlog) |
| **Reject** | Not aligned or feasible |
| **Merge** | Combine with existing Idea/Intent |

### 3. Intent Formalization (APO)

APO creates a complete Intent:

- Business problem and value proposition
- Success criteria with measurable KPIs
- Scope boundaries (in/out)
- Automation approach (conventional/agentic/hybrid)
- Stakeholder alignment

### 4. Charter Acceptance (PA)

PA reviews Intent and accepts:

- Validates design feasibility
- Confirms approach
- Commits to design timeline
- Triggers Workbench creation (if new)

### 5. Outcome Tracking (APO)

After deployment:

- Monitor KPIs against targets
- Report value realization
- Feed learnings back to new Ideas

---

## Related Documentation

- [Feedback Services](../feedback-services/README.md) — Source of suggestions
- [Automation Product Desk](../../06-ux-architecture/tenant-domain/automation-product-desk.md) — APO interface
- [Scenario Design Desk](../../06-ux-architecture/tenant-domain/scenario-design-desk.md) — PA interface
- [Workbench Management](../workbench-management/README.md) — Workbench creation
- [Automation Lifecycle Journey](../../08-personas-and-journeys/journeys/automation-lifecycle.md)

