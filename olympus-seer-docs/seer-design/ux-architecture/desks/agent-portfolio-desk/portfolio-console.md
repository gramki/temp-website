# Portfolio Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Portfolio Desk](./README.md)  
> **Primary Persona:** [Automation Product Owner (APO)](../../../personas-and-needs/roles.md#1-automation-product-owner-apo)

---

## Purpose

The Portfolio Console is the central view of all agents under **Automation Product Owner (APO)** ([role definition](../../../personas-and-needs/roles.md#1-automation-product-owner-apo)) ownership. It provides capabilities to manage the agent catalog, define charters, prioritize improvements, and triage feedback.

---

## Sections

### Agent Catalog

Central registry of all agents with their current state.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AGENT CATALOG                                                [12 Agents]    │
├─────────────────────────────────────────────────────────────────────────────┤
│ [+ New Agent] [Import] [Export] [Filters ▼]                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ Name               │ Status   │ Version │ Autonomy │ AHS   │ Last Active   │
│ ───────────────────────────────────────────────────────────────────────────│
│ invoice-processor  │ ✅ Active │ v2.3.1  │ Full     │ 0.92  │ 2 min ago     │
│ customer-service   │ ✅ Active │ v1.8.0  │ Suggest  │ 0.88  │ 5 min ago     │
│ order-validator    │ ⚠️ Review │ v1.2.3  │ Full     │ 0.71  │ 1 hr ago      │
│ expense-approver   │ ✅ Active │ v3.0.1  │ Full     │ 0.85  │ 10 min ago    │
│ data-enricher      │ 🔴 Paused │ v2.1.0  │ Suggest  │ 0.58  │ 2 days ago    │
│ compliance-checker │ 📝 Draft  │ v0.5.0  │ Watch    │ —     │ —             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Fields:**
| Field | Description |
|-------|-------------|
| Name | Agent name and identifier |
| Status | Draft, Active, Review, Paused, Deprecated |
| Version | Current production version |
| Autonomy | Current autonomy level (L0-L4) |
| AHS | Agent Health Score (from ARE) |
| Last Active | Last request processed |

**Actions:**
- Create new agent (opens charter wizard)
- Edit agent details
- View agent history
- Open in Agent Behavior Console
- Archive/deprecate agent

### Agent Charters

Define and manage agent purpose, scope, and success criteria.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AGENT CHARTER: invoice-processor                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│ Version: 2.3.1 │ Last Updated: 2026-01-10 │ Owner: Jane D. (APO)           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ PURPOSE                                                                     │
│ ────────────────────────────────────────────────────────────────────────── │
│ Automate routine invoice approval to reduce processing time and human      │
│ workload while maintaining compliance with financial policies.              │
│                                                                             │
│ SCOPE                                                                       │
│ ────────────────────────────────────────────────────────────────────────── │
│ IN SCOPE:                                                                   │
│ • Approve invoices under $1,000 with matching PO from approved vendors     │
│ • Flag discrepancies for human review                                      │
│ • Route exceptions to appropriate approvers                                 │
│                                                                             │
│ OUT OF SCOPE:                                                               │
│ • New vendor onboarding                                                     │
│ • Dispute resolution                                                        │
│ • Payment execution                                                         │
│                                                                             │
│ SUCCESS CRITERIA                                                            │
│ ────────────────────────────────────────────────────────────────────────── │
│ • Process 95% of routine invoices same-day                                 │
│ • Maintain error rate < 0.5%                                               │
│ • Reduce human processing time by 80%                                      │
│ • User satisfaction score > 4.0/5.0                                        │
│                                                                             │
│ [Edit Charter] [View History] [Export]                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Charter Elements:**
| Element | Description |
|---------|-------------|
| Purpose | Why this agent exists (one paragraph) |
| Scope | What the agent does and doesn't do |
| Success Criteria | Measurable outcomes |
| Autonomy Intent | Desired autonomy level with justification |
| Risk Profile | Known risks and mitigations |
| Dependencies | Other agents, systems, or teams |

**Actions:**
- Edit charter (versioned)
- View charter history
- Compare versions
- Export to PDF

### Improvement Backlog

Prioritized list of agent enhancements and fixes.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ IMPROVEMENT BACKLOG                                         [15 Items]      │
├─────────────────────────────────────────────────────────────────────────────┤
│ [+ Add Item] [Prioritize] [Bulk Actions]                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ # │ Priority │ Agent             │ Type        │ Source │ Status           │
│ ───────────────────────────────────────────────────────────────────────────│
│ 1 │ 🔴 High   │ order-validator   │ Bug         │ COS    │ In Progress      │
│ 2 │ 🔴 High   │ customer-service  │ Enhancement │ APO    │ Ready            │
│ 3 │ 🟡 Medium │ invoice-processor │ Enhancement │ Users  │ Ready            │
│ 4 │ 🟡 Medium │ expense-approver  │ Enhancement │ ARE    │ Backlog          │
│ 5 │ 🟢 Low    │ data-enricher     │ Optimization│ COS    │ Backlog          │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Item Fields:**
| Field | Description |
|-------|-------------|
| Priority | High, Medium, Low (with scoring) |
| Agent | Affected agent |
| Type | Bug, Enhancement, Optimization, Autonomy |
| Source | Who reported (COS, ARE, ARAO, Users, APO) |
| Status | Backlog, Ready, In Progress, Done |

**Actions:**
- Add new item
- Prioritize (drag-and-drop or scoring)
- Assign to sprint/milestone
- Link to feedback
- Route to AE

### Feedback Inbox

Issues and feedback routed from other personas.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ FEEDBACK INBOX                                               [8 New]        │
├─────────────────────────────────────────────────────────────────────────────┤
│ [Mark All Read] [Filter ▼] [Sort: Newest ▼]                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ 🔴 HIGH PRIORITY                                                            │
│ ─────────────────────────────────────────────────────────────────────────  │
│ □ COS │ customer-service │ Intent drift detected: agent refusing...        │
│        2 hours ago │ [View] [Triage] [Add to Backlog]                      │
│                                                                             │
│ □ ARAO │ expense-approver │ Compliance concern: approving without...       │
│         4 hours ago │ [View] [Triage] [Add to Backlog]                     │
│                                                                             │
│ 🟡 MEDIUM PRIORITY                                                          │
│ ─────────────────────────────────────────────────────────────────────────  │
│ □ ARE │ invoice-processor │ Cost spike: 3x normal for retry storm          │
│        1 day ago │ [View] [Triage] [Add to Backlog]                        │
│                                                                             │
│ □ KMO │ order-validator │ Knowledge update available for shipping...       │
│        1 day ago │ [View] [Acknowledge]                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Feedback Fields:**
| Field | Description |
|-------|-------------|
| Source | Persona who sent (COS, ARE, ARAO, KMO) |
| Agent | Affected agent |
| Summary | Brief description |
| Priority | Auto-classified based on source and type |
| Age | Time since received |

**Actions:**
- View full feedback with context
- Triage (classify, prioritize)
- Add to backlog
- Respond to source
- Acknowledge and close

---

## Key Features

### Agent Lifecycle Management

Track agents through their lifecycle:

```
Draft → Development → Review → Active → Deprecated
  ↑                     │
  └── Improvements ─────┘
```

### Charter Version Control

- All charter changes are versioned
- Diff view between versions
- Change history with author and timestamp
- Rollback capability

### Priority Scoring

Automatic priority calculation based on:
- Business impact (from charter)
- Source urgency (ARAO > COS > ARE)
- User volume affected
- Time in queue

### Feedback Routing

Intelligent triage suggestions:
| Source | Default Action |
|--------|----------------|
| COS - Intent | Review charter |
| COS - Design | Route to CSA |
| ARE - Cost | Review SLO, route to AE |
| ARAO - Compliance | Review immediately |

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Agent status, health scores, activity metrics |
| **Predictable** | Charter-defined success criteria, expected behavior |
| **Directable** | Backlog prioritization, improvement decisions |
| **Authority Enforceable** | Charter scope, autonomy boundaries |

---

## REST API

```
Base: /api/seer/apo/v1

# Agent Catalog
GET    /agents                    - List all agents
GET    /agents/{id}               - Get agent details
POST   /agents                    - Create agent (draft)
PUT    /agents/{id}               - Update agent
DELETE /agents/{id}               - Archive agent

# Charters
GET    /agents/{id}/charter       - Get current charter
PUT    /agents/{id}/charter       - Update charter
GET    /agents/{id}/charter/history - Charter history
GET    /agents/{id}/charter/diff  - Compare versions

# Backlog
GET    /backlog                   - List backlog items
POST   /backlog                   - Add item
PUT    /backlog/{id}              - Update item
PUT    /backlog/prioritize        - Bulk prioritize
DELETE /backlog/{id}              - Remove item

# Feedback
GET    /feedback                  - List feedback
GET    /feedback/{id}             - Get feedback details
PUT    /feedback/{id}/triage      - Triage feedback
POST   /feedback/{id}/respond     - Respond to source
```

---

## Indicative Wireframe

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ PORTFOLIO CONSOLE                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ [Agent Catalog] [Charters] [Backlog] [Feedback Inbox]                       │
├───────────────────────────────────────┬─────────────────────────────────────┤
│                                       │                                     │
│ AGENT CATALOG                         │ QUICK STATS                         │
│ ────────────────────────────────────  │ ──────────────────────────────────  │
│ [Search...]        [Filters ▼]        │ Active Agents: 8                    │
│                                       │ Draft Agents: 2                     │
│ invoice-processor    ✅ Active v2.3   │ Under Review: 2                     │
│ customer-service     ✅ Active v1.8   │                                     │
│ order-validator      ⚠️ Review v1.2   │ Avg AHS: 0.84                       │
│ expense-approver     ✅ Active v3.0   │ Portfolio ROI: $1.2M                │
│ data-enricher        🔴 Paused v2.1   │                                     │
│ compliance-checker   📝 Draft v0.5    │ Feedback: 8 new                     │
│                                       │ Backlog: 15 items                   │
│ [+ New Agent]                         │                                     │
├───────────────────────────────────────┴─────────────────────────────────────┤
│                                                                             │
│ RECENT ACTIVITY                                                             │
│ ──────────────────────────────────────────────────────────────────────────  │
│ • invoice-processor v2.3.1 deployed to production             2 hours ago   │
│ • COS flagged customer-service for intent drift               4 hours ago   │
│ • order-validator autonomy proposal approved by ARAO          1 day ago     │
│ • expense-approver charter updated                            2 days ago    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
