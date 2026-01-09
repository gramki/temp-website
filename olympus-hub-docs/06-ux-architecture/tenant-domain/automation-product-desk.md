# Automation Product Desk

> **Status:** 🔴 Stub — Placeholder for expansion

**Automation Product Desk** is the strategic workspace for **Automation Product Owners (APO)** to define, track, and evolve automation capabilities within a Workbench.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Primary Persona** | Automation Product Owner (APO) |
| **Scope** | Workbench |
| **Access** | Web, MCP (Creator Gateway) |

---

## Purpose

The APO owns the **business intent** behind automation. This desk provides tools to:

1. **Define** — Create automation charters and articulate business value
2. **Track** — Monitor outcomes against success criteria
3. **Prioritize** — Manage the automation backlog and roadmap
4. **Evolve** — Review learnings and iterate on automation strategy

---

## Consoles

### Charter Console

Define and manage automation charters — the business case for each automation capability.

| Capability | Description |
|------------|-------------|
| **Charter Builder** | Create automation charters with business case, scope, success criteria |
| **Value Proposition** | Document problem, opportunity, and expected value |
| **Success Criteria** | Define measurable KPIs and targets |
| **Scope Definition** | Specify in-scope and out-of-scope boundaries |
| **Stakeholder Mapping** | Identify sponsors, approvers, and stakeholders |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          CHARTER CONSOLE                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  Automation Charters                                                 │    │
│  │                                                                      │    │
│  │  [+] New Charter    [Filter: Active ▼]    [Search...]               │    │
│  │                                                                      │    │
│  │  ┌───────────────────────────────────────────────────────────────┐  │    │
│  │  │ Dispute Resolution Automation              ACTIVE              │  │    │
│  │  │ Target: Reduce processing time by 80%     Progress: 65%       │  │    │
│  │  ├───────────────────────────────────────────────────────────────┤  │    │
│  │  │ Card Replacement Automation               DESIGN               │  │    │
│  │  │ Target: Same-day card dispatch            Progress: 20%       │  │    │
│  │  └───────────────────────────────────────────────────────────────┘  │    │
│  │                                                                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Outcomes Console

Track business outcomes and value realization for active automations.

| Capability | Description |
|------------|-------------|
| **KPI Dashboard** | Live metrics against charter targets |
| **Value Tracking** | Measure realized value (time saved, cost reduced, etc.) |
| **Trend Analysis** | Track progress over time |
| **Outcome Reports** | Generate stakeholder reports |

### Backlog Console

Manage the automation backlog and prioritization.

| Capability | Description |
|------------|-------------|
| **Backlog View** | List of proposed and in-progress automation initiatives |
| **Prioritization** | Rank by value, effort, risk |
| **Roadmap** | Timeline view of planned automation rollouts |
| **Dependencies** | Track cross-automation dependencies |

### Feedback Console

Capture and route feedback from operations.

| Capability | Description |
|------------|-------------|
| **Issue Aggregation** | View issues raised during Run stage |
| **Feedback Triage** | Categorize, prioritize, and route feedback |
| **Improvement Proposals** | Draft proposals for Evolve stage |
| **Stakeholder Updates** | Communicate progress to sponsors |

---

## Key Workflows

### 1. Charter Creation

```
APO                    Charter Console              Workbench
 │                           │                          │
 ├─── Create Charter ───────▶│                          │
 │                           ├─── Save to Workbench ───▶│
 │                           │                          │
 │◀── Charter Draft ─────────┤                          │
 │                           │                          │
 ├─── Submit for Approval ──▶│                          │
 │                           ├─── Notify Sponsor ──────▶│
 │                           │                          │
```

### 2. Outcome Review

```
APO                    Outcomes Console            Analytics
 │                           │                          │
 ├─── View Dashboard ───────▶│                          │
 │                           ├─── Fetch Metrics ───────▶│
 │                           │◀── Aggregated Data ──────┤
 │◀── KPI Dashboard ─────────┤                          │
 │                           │                          │
 ├─── Generate Report ──────▶│                          │
 │◀── Stakeholder Report ────┤                          │
```

### 3. Automation Approach Decision

```
APO                    Charter Console          Process Architect
 │                           │                          │
 ├─── Propose Approach ─────▶│                          │
 │    (Conventional/Agentic) │                          │
 │                           ├─── Notify PA ───────────▶│
 │                           │                          │
 │                           │◀── PA Validates ─────────┤
 │◀── Approach Confirmed ────┤                          │
 │                           │                          │
```

---

## Integration with Other Desks

| Related Desk | Handoff |
|--------------|---------|
| **Scenario Design Desk** | APO → PA: Charter approved, scenario design begins |
| **Automation Development Desk** | Visibility: Track implementation progress |
| **Supervisor Desk** | Run stage: Receive operational feedback |

---

## Automation Approach Decision

The APO proposes whether a scenario should use:

| Approach | Criteria | Next Step |
|----------|----------|-----------|
| **Conventional** | Structured inputs, rule-based logic | PA → Developer (Hub Application) |
| **Agentic** | Unstructured inputs, judgment required | Transition to Seer lifecycle |
| **Hybrid** | Mix of both | PA defines boundaries |

> **Note:** For agentic automation, the scenario transitions to the Seer Agentic Automation Lifecycle after APO/PA decision.

---

## Channel Support

| Channel | Access |
|---------|--------|
| **Web** | Full desk access |
| **MCP** | Charter query, outcome metrics via Creator Gateway |
| **REST** | Programmatic access to charters and outcomes |

---

## Related Documentation

- [Automation Product Owner Persona](../../08-personas-and-journeys/personas/automation-product-owner.md)
- [Automation Lifecycle Journey](../../08-personas-and-journeys/journeys/automation-lifecycle.md)
- [Scenario Design Desk](./scenario-design-desk.md) — Where PA takes over after charter approval
- [Hub Analytics](../../04-subsystems/hub-analytics/README.md) — Powers outcome dashboards

---

*TODO: Detailed charter templates, outcome tracking specifications, backlog management workflows*

