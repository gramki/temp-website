# Agent Portfolio Desk

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Primary Persona:** [Automation Product Owner (APO)](../../../personas-and-needs/roles.md#1-automation-product-owner-apo)  
> **Related:** [APO Reference](../../../personas-and-needs/apo.md) | [APO Needs](../../../personas-and-needs/needs/apo-business-outcomes-and-autonomy.md)

---

## Purpose

The Agent Portfolio Desk is the primary workspace for the **Automation Product Owner (APO)** ([role definition](../../../personas-and-needs/roles.md#1-automation-product-owner-apo)). It provides capabilities to:

- Manage the agent portfolio (catalog, ownership, status)
- Track business outcomes and value delivery
- Propose and manage autonomy levels
- Prioritize improvements based on feedback

---

## Consoles

| Console | Purpose | Documentation |
|---------|---------|---------------|
| **Portfolio Console** | Agent catalog, charters, backlog, feedback | [portfolio-console.md](./portfolio-console.md) |
| **Outcomes Console** | KPI dashboard, value tracking, ROI | [outcomes-console.md](./outcomes-console.md) |
| **Autonomy Console** | Autonomy levels, proposals, approval workflow | [autonomy-console.md](./autonomy-console.md) |

---

## Key Journeys

| Journey | Description | Consoles Used |
|---------|-------------|---------------|
| **Agent Chartering** | Define new agent purpose, scope, success criteria | Portfolio Console |
| **Autonomy Proposal** | Propose autonomy level, submit for ARAO approval | Autonomy Console |
| **Outcome Review** | Assess agent value delivery, adjust priorities | Outcomes Console |
| **Feedback Triage** | Review COS/ARE feedback, prioritize responses | Portfolio Console |

---

## OPDA Integration

The Agent Portfolio Desk demonstrates OPDA capabilities for APO:

| OPDA | Capability | Console |
|------|------------|---------|
| **Observable** | Business outcome metrics, value delivery tracking | Outcomes Console |
| **Predictable** | Trend analysis, outcome forecasting | Outcomes Console |
| **Directable** | Autonomy adjustment, scope modification | Autonomy Console |
| **Authority Enforceable** | Autonomy approval workflow, policy enforcement | Autonomy Console |

### How APO Actions, Assesses, and Evidences OPDA

| OPDA | APO Actions | APO Assesses | APO Evidences |
|------|-------------|--------------|---------------|
| **Observable** | Define KPIs, configure dashboards | Review outcome metrics | Export value reports |
| **Predictable** | Set baseline expectations | Compare to forecasts | Document predictions vs. actuals |
| **Directable** | Propose autonomy changes | Review proposal status | Track approved changes |
| **Authority Enforceable** | Submit proposals to ARAO | Check approval status | Audit trail of approvals |

---

## Channel Access

| Channel | Capabilities |
|---------|--------------|
| **Web UI** | Full desk access via Seer Portal |
| **REST API** | `/api/seer/apo/v1` — [API Documentation](../../rest-channels/apo-channel.md) |
| **MCP** | `seer-apo-mcp` server for AI assistant integration |
| **Email** | Notifications, scheduled reports |

---

## Integration Points

### Receives From

| Source | Data |
|--------|------|
| **COS** | Behavioral issues, drift alerts |
| **ARE** | Operational feedback, cost alerts |
| **ARAO** | Autonomy approval decisions |

### Sends To

| Destination | Data |
|-------------|------|
| **ARAO** | Autonomy proposals |
| **CSA** | Intent clarification requests |
| **AE** | Improvement priorities |

---

## Indicative Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT PORTFOLIO DESK                                          APO: Jane D. │
├─────────────────────────────────────────────────────────────────────────────┤
│  [Portfolio] [Outcomes] [Autonomy]                              🔔 🔍 ⚙️    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────┐  ┌──────────────────────────────┐  │
│  │ PORTFOLIO OVERVIEW                  │  │ QUICK STATS                  │  │
│  │                                     │  │                              │  │
│  │ Active Agents: 12                   │  │ Total Value Delivered: $1.2M │  │
│  │ Draft Agents: 3                     │  │ Avg Agent ROI: 340%          │  │
│  │ Under Review: 2                     │  │ Autonomy Utilization: 78%    │  │
│  │                                     │  │ Pending Proposals: 2         │  │
│  └─────────────────────────────────────┘  └──────────────────────────────┘  │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ RECENT ACTIVITY                                                      │   │
│  ├──────────────────────────────────────────────────────────────────────┤   │
│  │ • Invoice Processor: Autonomy proposal approved by ARAO         2h   │   │
│  │ • Customer Service: COS flagged drift detection                 4h   │   │
│  │ • Order Validator: Monthly outcome review due                   1d   │   │
│  │ • Expense Approver: New feedback from ARE                       1d   │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ FEEDBACK INBOX                                              [3 New]  │   │
│  ├──────────────────────────────────────────────────────────────────────┤   │
│  │ 🔴 HIGH   │ COS │ Customer Service agent showing inconsistent...    │   │
│  │ 🟡 MEDIUM │ ARE │ Invoice Processor cost spike last week            │   │
│  │ 🟢 LOW    │ KMO │ Knowledge update available for Order Validator     │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Console Summaries

### Portfolio Console

The central view of all agents under APO ownership.

**Sections:**
- **Agent Catalog** — All agents with status, version, owner
- **Agent Charters** — Purpose, scope, success criteria per agent
- **Improvement Backlog** — Prioritized list of enhancements
- **Feedback Inbox** — Issues routed from COS/ARE/ARAO

**Key Features:**
- Agent lifecycle status tracking (Draft → Active → Deprecated)
- Charter templates and version history
- Priority scoring for backlog items
- Feedback categorization and routing

[Full specification →](./portfolio-console.md)

---

### Outcomes Console

Track whether agents are delivering business value.

**Sections:**
- **KPI Dashboard** — Business metrics per agent
- **Value Tracker** — ROI, cost savings, time savings
- **Comparison View** — Agent vs. baseline (pre-agent)
- **Stakeholder Reports** — Executive summaries, scheduled reports

**Key Features:**
- Customizable KPI definitions
- Trend analysis over time
- Export to PDF/PPT for stakeholder reviews
- Outcome alerts and thresholds

[Full specification →](./outcomes-console.md)

---

### Autonomy Console

Manage autonomy levels and proposals.

**Sections:**
- **Current Autonomy** — View autonomy levels per agent
- **Proposal Drafts** — Create and edit autonomy proposals
- **Approval Status** — Track ARAO review status
- **Policy History** — Audit trail of autonomy changes

**Key Features:**
- Autonomy level templates (L0-L4)
- Justification builder with risk/value prompts
- ARAO submission workflow
- Expiration and re-review tracking

[Full specification →](./autonomy-console.md)

---

## REST API Overview

The APO REST channel provides programmatic access:

```
Base: /api/seer/apo/v1

Portfolio:
  GET    /agents              - List agents
  GET    /agents/{id}         - Get agent details
  POST   /agents              - Create agent (draft)
  PUT    /agents/{id}/charter - Update charter

Outcomes:
  GET    /agents/{id}/outcomes    - Get outcome metrics
  GET    /agents/{id}/kpis        - Get KPI definitions
  POST   /agents/{id}/kpis        - Define KPI
  GET    /reports                 - Get available reports
  POST   /reports/generate        - Generate report

Autonomy:
  GET    /autonomy/levels         - List autonomy levels
  GET    /autonomy/proposals      - List proposals
  POST   /autonomy/proposals      - Create proposal
  GET    /autonomy/proposals/{id} - Get proposal details
  POST   /autonomy/proposals/{id}/submit - Submit to ARAO
```

[Full API documentation →](../../rest-channels/apo-channel.md)

---

*Status: 🟡 Draft — Overview and console specifications complete*
