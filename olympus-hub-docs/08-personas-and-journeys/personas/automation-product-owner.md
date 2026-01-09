# Persona: Automation Product Owner (APO)

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-09

---

## Overview

The **Automation Product Owner (APO)** owns the business intent and outcomes for automated capabilities within a Workbench. APO answers the question: *"Why does this automation exist, and is it delivering value?"*

APO works with Process Architects to define automation needs, whether implemented through agents (agentic path) or conventional automation (deterministic path).

| Attribute | Value |
|-----------|-------|
| **Category** | Hub Persona — Workbench Designer |
| **Scope** | Workbench |
| **Domain** | Tenant Identity Domain |
| **Primary Console** | Automation Portfolio Desk (planned) |

---

## Role Definition

> **APO owns automation intent and business accountability.**

This means:

| APO Owns | APO Does NOT Own |
|----------|------------------|
| Why automation exists | How automation is designed |
| What problems it solves | How it's implemented |
| Success criteria and KPIs | Runtime operations |
| Autonomy proposals (for agentic) | Autonomy approval |
| Improvement priorities | Day-to-day execution |

---

## Objectives

| Objective | Description |
|-----------|-------------|
| **Justify Automation** | Ensure every automation has a clear business case |
| **Define Success** | Establish measurable outcomes and KPIs |
| **Prioritize Roadmap** | Decide what to automate next |
| **Govern Autonomy** | Propose autonomy levels for agentic scenarios |
| **Track Value** | Measure and report business outcomes |

---

## Key Activities

### Initiation Phase

1. **Identify Automation Need**
   - Business problem requiring automation
   - Current pain points and inefficiencies
   - Expected value from automation

2. **Justify Investment**
   - Business case with ROI projection
   - Resource requirements
   - Risk assessment

3. **Define Success Criteria**
   - Measurable KPIs
   - Baseline vs. target metrics
   - Timeline for value realization

### Design Phase

4. **Collaborate with Process Architect**
   - Share business context
   - Review scenario designs
   - Validate alignment with intent

5. **Propose Automation Approach**
   - Recommend agentic vs. conventional
   - Based on complexity, judgment requirements, risk
   - Subject to CSA validation (for agentic)

### Operations Phase

6. **Track Outcomes**
   - Monitor business KPIs
   - Assess value delivery
   - Report to stakeholders

7. **Prioritize Improvements**
   - Review feedback from operations
   - Prioritize enhancement backlog
   - Balance new development vs. improvements

### Governance Phase

8. **Govern Autonomy** (for agentic scenarios)
   - Propose autonomy levels
   - Submit for ARAO approval
   - Review autonomy periodically

### Evolution Phase (Production Feedback)

9. **Review Production Feedback** (development workbenches only)
   - Receive feedback from linked production workbenches
   - Triage incoming bugs, issues, and suggestions
   - Accept, reject, or route feedback to PA/Developer
   - Mark resolved when fixes are delivered

---

## Automation Approach Decision

APO proposes whether a scenario should be automated via agents or conventional automation:

| Criterion | → Conventional | → Agentic |
|-----------|---------------|-----------|
| Input variability | Low, structured | High, unstructured |
| Decision logic | Rules can capture | Judgment required |
| Exceptions | Few, predictable | Many, contextual |
| Risk tolerance | Low tolerance for error | Can tolerate + correct |
| Current process | Scripted, checklist | Requires expertise |

**Process:**
1. APO proposes approach based on business need
2. If agentic: CSA validates feasibility
3. If agentic: ARAO approves autonomy

---

## Collaboration Model

| With | APO's Role |
|------|------------|
| **Process Architect** | APO defines "why" and "what outcomes"; PA designs "what happens" |
| **Developer** | APO provides success criteria; Developer implements |
| **Supervisor** | APO receives operational feedback; adjusts priorities |
| **CSA** (Seer) | APO proposes agentic approach; CSA validates |
| **ARE** (Seer) | APO receives operational signals; ARE reports constraints |
| **ARAO** | APO proposes autonomy; ARAO approves |

---

## Hub Capabilities Consumed

### Primary Interface: Automation Product Desk

| Console | What It Provides |
|---------|------------------|
| **Charter Console** | Create and manage automation charters |
| **Outcomes Console** | Track business KPIs per automation |
| **Backlog Console** | Prioritize improvements and enhancements |
| **Feedback Console** | Local feedback within workbench |
| **Production Feedback Inbox** | Review feedback from production workbenches (development workbenches only) |

See [Automation Product Desk](../../06-ux-architecture/tenant-domain/automation-product-desk.md) for full details.

### Hub Services Accessed

| Service | Usage |
|---------|-------|
| **Workbench Management** | Access workbench configuration |
| **Hub Analytics** | Track outcomes and KPIs |
| **CAF** | Review decision quality signals |

### What They Produce

| Output | Consumed By |
|--------|-------------|
| Automation Charter | Process Architect, Developer |
| Success Criteria | Developer, Supervisor |
| Autonomy Proposal | ARAO (for approval) |
| Improvement Priorities | Developer, Process Architect |

---

## Artifacts Owned

### Automation Charter

Every automation should have a charter that answers:

| Question | Example Answer |
|----------|----------------|
| Why does this automation exist? | "To reduce dispute resolution time by 60%" |
| What problem does it solve? | "Manual triage takes 2 hours per dispute" |
| What is success? | "90% of routine disputes resolved same-day" |
| What is out of scope? | "Complex legal disputes, regulatory escalations" |
| What autonomy is proposed? | "Full autonomy for routine; human-in-loop for exceptions" |

### Outcome Tracking

| Metric Type | Examples |
|-------------|----------|
| **Efficiency** | Processing time, throughput, cost per transaction |
| **Quality** | Error rate, rework rate, customer satisfaction |
| **Value** | Revenue impact, cost savings, risk reduction |

---

## Key Journeys

- [Automation Lifecycle](../journeys/automation-lifecycle.md) — Primary journey
- [Scenario Development](../journeys/scenario-development.md) — Supporting role
- [Production Feedback Loop](../journeys/production-feedback-loop.md) — Evolution journey (primary role in development workbenches)

---

## Anti-Patterns

| Pattern | Why It's Problematic |
|---------|---------------------|
| "Automate first, justify later" | No clear business case leads to waste |
| "The technology team decides what to automate" | Automation without business ownership fails |
| "Success is measured by uptime" | Operational metrics ≠ business value |
| "Autonomy decisions are technical" | Autonomy is a business risk decision |

---

## Related Documentation

- [Process Architect](./process-architect.md) — Designs scenarios
- [Automation Lifecycle Journey](../journeys/automation-lifecycle.md) — End-to-end workflow
- [Scenario Development Journey](../journeys/scenario-development.md) — Scenario creation
- [Production Feedback Loop Journey](../journeys/production-feedback-loop.md) — Evolution workflow
- [ADR-0081: Production Feedback Loop](../../decision-logs/0081-production-feedback-loop.md) — Architecture decision
- [Automation Product Desk](../../06-ux-architecture/tenant-domain/automation-product-desk.md) — Primary interface

---

*Status: 🟡 Draft — Role defined, desk documented*

