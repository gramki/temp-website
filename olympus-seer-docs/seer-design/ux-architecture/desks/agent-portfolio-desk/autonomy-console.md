# Autonomy Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Portfolio Desk](./README.md)  
> **Primary Persona:** [Automation Product Owner (APO)](../../../personas-and-needs/roles.md#1-automation-product-owner-apo)

---

## Purpose

The Autonomy Console enables the **Automation Product Owner (APO)** ([role definition](../../../personas-and-needs/roles.md#1-automation-product-owner-apo)) to manage agent autonomy levels, create proposals for autonomy changes, and track approval workflows with **AI Risk & Audit Owner (ARAO)** ([role definition](../../../personas-and-needs/roles.md#7-ai-risk--audit-owner-arao)).

---

## Sections

### Current Autonomy

View and understand current autonomy levels across all agents.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ CURRENT AUTONOMY LEVELS                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ [Filter by Level ▼] [Sort: Agent Name ▼]                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Agent               │ Current  │ Effective │ Utilization │ Expires        │
│ ───────────────────────────────────────────────────────────────────────────│
│ invoice-processor   │ L3       │ L3        │ 89%         │ Jul 15, 2026   │
│ expense-approver    │ L3       │ L3        │ 76%         │ Jun 1, 2026    │
│ customer-service    │ L2       │ L2        │ 92%         │ Aug 30, 2026   │
│ order-validator     │ L3       │ L2 ⚠️     │ 45%         │ Mar 1, 2026    │
│ data-enricher       │ L2       │ L1 ⚠️     │ N/A         │ —              │
│ compliance-checker  │ L1       │ L1        │ N/A         │ —              │
│                                                                             │
│ Legend: ⚠️ = Effective level reduced from approved level                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Autonomy Levels:**

> **Note:** Seer uses a 5-level autonomy scale (L0-L4). See [ARAO Autonomy Console](../agent-compliance-desk/autonomy-console.md) for definitions.

| Level | Name | Description | Human Role |
|-------|------|-------------|------------|
| **L4** | Fully Autonomous | Agent autonomous, audit only | Auditor |
| **L3** | Bounded Autonomous | Agent autonomous within rules | Exception Handler |
| **L2** | Supervised | Agent executes, human reviews | Reviewer |
| **L1** | Assisted | Agent proposes, human decides | Decision-maker |
| **L0** | Manual | Human executes, agent advises | Executor |

**Fields:**
| Field | Description |
|-------|-------------|
| Current | ARAO-approved autonomy level |
| Effective | Actual operational level (may be reduced by ARE) |
| Utilization | % of decisions using full autonomy |
| Expires | Approval expiration date |

**Click Agent for Details:**
- Autonomy scope (what decisions)
- Conditions (amount limits, vendor types)
- Controls (guardrails, monitoring)
- Approval history

### Proposal Drafts

Create and manage autonomy change proposals.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AUTONOMY PROPOSALS                                           [2 Drafts]     │
├─────────────────────────────────────────────────────────────────────────────┤
│ [+ New Proposal]                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ DRAFTS                                                                      │
│ ───────────────────────────────────────────────────────────────────────────│
│ □ customer-service: Suggest → Full                                          │
│   Change: Expand to full autonomy for standard queries                      │
│   Last Edited: 2 hours ago                        [Edit] [Submit] [Delete]  │
│                                                                             │
│ □ order-validator: Full → Full (expanded scope)                             │
│   Change: Add international orders to scope                                 │
│   Last Edited: 1 day ago                          [Edit] [Submit] [Delete]  │
│                                                                             │
│ SUBMITTED (Awaiting ARAO Review)                                            │
│ ───────────────────────────────────────────────────────────────────────────│
│ ○ expense-approver: Full → Full (increased limit)                          │
│   Change: Increase approval limit from $500 to $1,000                       │
│   Submitted: 3 days ago │ Status: Under Review    [View] [Withdraw]         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Proposal Builder

Step-by-step wizard for creating autonomy proposals.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ NEW AUTONOMY PROPOSAL                                        Step 2 of 4    │
├─────────────────────────────────────────────────────────────────────────────┤
│ [1. Agent ✓] [2. Change →] [3. Justification] [4. Review]                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ PROPOSED CHANGE                                                             │
│ ──────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│ Agent: customer-service                                                     │
│                                                                             │
│ Current Level:  ● Suggest                                                   │
│ Proposed Level: ○ Full                                                      │
│                                                                             │
│ SCOPE DEFINITION                                                            │
│ ──────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│ Decision Types (select which decisions get new autonomy):                   │
│ ☑ Answer standard product questions                                         │
│ ☑ Provide order status updates                                              │
│ ☑ Process simple refund requests (< $50)                                   │
│ ☐ Handle complaints (keep at Suggest)                                       │
│ ☐ Authorize exceptions (keep at Ask)                                        │
│                                                                             │
│ CONDITIONS                                                                   │
│ ──────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│ ☑ Confidence threshold: Agent confidence > 90%                              │
│ ☑ Query type: Standard (not escalation)                                     │
│ ☑ Customer tier: All tiers                                                  │
│ ☑ Value limit: Refunds < $50                                               │
│                                                                             │
│ [Back] [Save Draft]                                      [Continue →]       │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ NEW AUTONOMY PROPOSAL                                        Step 3 of 4    │
├─────────────────────────────────────────────────────────────────────────────┤
│ [1. Agent ✓] [2. Change ✓] [3. Justification →] [4. Review]                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ BUSINESS JUSTIFICATION                                                      │
│ ──────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│ Why is this autonomy needed? *                                              │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │ Current Suggest mode creates bottleneck with 500+ daily reviews.        ││
│ │ Human reviewers approve 97% without changes. Full autonomy for          ││
│ │ standard queries will reduce wait times and free human agents for       ││
│ │ complex issues.                                                         ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                                                                             │
│ EXPECTED VALUE                                                              │
│ ──────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│ Time Savings:        [150   ] hours/month                                   │
│ Cost Savings:        [$7,500] /month                                        │
│ Response Time:       [2 min ] → [30 sec ] (improvement)                     │
│ Customer Satisfaction: [4.1  ] → [4.5   ] (expected)                        │
│                                                                             │
│ RISK ANALYSIS                                                               │
│ ──────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│ What could go wrong?                                                        │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │ • Agent may give incorrect product information                          ││
│ │ • Agent may approve refunds that should be reviewed                     ││
│ │ • Customer may prefer human interaction                                 ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                                                                             │
│ Mitigation Plan:                                                            │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │ • 90% confidence threshold ensures uncertain cases go to humans         ││
│ │ • $50 refund cap limits financial exposure                              ││
│ │ • Daily COS review of autonomous decisions                              ││
│ │ • "Speak to human" option always available                              ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                                                                             │
│ [Back] [Save Draft]                                      [Continue →]       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Approval Status

Track proposals through the ARAO approval workflow.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ APPROVAL STATUS                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ PROPOSAL: expense-approver limit increase                                   │
│ ──────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│ Status: 🟡 UNDER REVIEW                                                     │
│                                                                             │
│ WORKFLOW                                                                    │
│                                                                             │
│   ✅ Submitted              ──→  🔄 ARAO Review        ──→  ⬜ Decision     │
│   Jan 10, 2026                   Started Jan 11              Pending        │
│   by Jane D. (APO)               by Jordan P. (ARAO)                        │
│                                                                             │
│ ARAO FEEDBACK                                                               │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Jan 11, 2026 - Jordan P.:                                                   │
│ "Need additional controls before approval:                                  │
│  1. Daily reporting requirement for approvals > $750                        │
│  2. Monthly audit review of all auto-approved expenses                      │
│                                                                             │
│ Can you confirm these controls will be implemented?"                        │
│                                                                             │
│ [Respond to Feedback] [Withdraw Proposal] [View Full Proposal]              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Policy History

Audit trail of all autonomy changes.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AUTONOMY HISTORY: invoice-processor                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Date        │ Change                      │ Approved By │ Expires          │
│ ───────────────────────────────────────────────────────────────────────────│
│ Jul 15, 25  │ Suggest → Full             │ ARAO (J.P.) │ Jul 15, 2026     │
│             │ Added: Auto-approve < $1000                                   │
│             │ Controls: Matching PO, approved vendor                        │
│                                                                             │
│ Mar 1, 25   │ Ask → Suggest              │ ARAO (J.P.) │ Jul 15, 2025     │
│             │ Added: Recommend approvals                                    │
│             │ Controls: Human review required                               │
│                                                                             │
│ Jan 15, 25  │ Initial: Watch → Ask       │ ARAO (S.A.) │ Mar 1, 2025      │
│             │ Initial deployment                                            │
│             │ Controls: All decisions need approval                         │
│                                                                             │
│ [Export History] [View Full Details]                                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Features

### Proposal Templates

Pre-built templates for common autonomy requests:

| Template | Use Case |
|----------|----------|
| **Level Upgrade** | Move from one level to higher |
| **Scope Expansion** | Add decisions to existing level |
| **Limit Increase** | Increase value/rate limits |
| **Condition Change** | Modify conditions |
| **Renewal** | Renew expiring approval |

### Justification Builder

Guided prompts for building strong proposals:

1. **Business Value** — What will the organization gain?
2. **Risk Assessment** — What could go wrong?
3. **Control Specification** — How will risks be mitigated?
4. **Success Metrics** — How will we measure success?
5. **Rollback Plan** — How to revert if needed?

### Autonomy Utilization Analytics

Track how effectively granted autonomy is used:

```
Autonomy Utilization: invoice-processor

Full Autonomy Used:     89% of eligible decisions
Suggest Fallback:       8% (low confidence)
Human Override:         3% (complexity)

Recommendation: Autonomy well utilized, no changes needed
```

### Approval Workflow Integration

Seamless integration with ARAO:

```
APO creates proposal
       ↓
System validates completeness
       ↓
APO submits to ARAO
       ↓
ARAO receives in Approval Queue
       ↓
ARAO reviews, requests changes, or decides
       ↓
APO notified of decision
       ↓
If approved: Controls implemented by AE
       ↓
ARE enables in production
```

### Expiration Management

- Automatic reminders before expiration
- Renewal workflow (simplified re-approval)
- Grace period handling
- Emergency extension process

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Autonomy levels, utilization, history |
| **Predictable** | Clear autonomy boundaries per proposal |
| **Directable** | Autonomy proposals, scope modifications |
| **Authority Enforceable** | ARAO approval workflow, expiration tracking |

---

## REST API

```
Base: /api/seer/apo/v1

# Current Autonomy
GET    /autonomy                      - List all agent autonomy
GET    /agents/{id}/autonomy          - Get agent autonomy details
GET    /agents/{id}/autonomy/history  - Autonomy history
GET    /agents/{id}/autonomy/utilization - Utilization metrics

# Proposals
GET    /autonomy/proposals            - List proposals
POST   /autonomy/proposals            - Create proposal
GET    /autonomy/proposals/{id}       - Get proposal details
PUT    /autonomy/proposals/{id}       - Update proposal
DELETE /autonomy/proposals/{id}       - Delete draft
POST   /autonomy/proposals/{id}/submit - Submit to ARAO
POST   /autonomy/proposals/{id}/withdraw - Withdraw proposal
POST   /autonomy/proposals/{id}/respond - Respond to ARAO feedback

# Templates
GET    /autonomy/templates            - List templates
GET    /autonomy/templates/{id}       - Get template
```

---

## Indicative Wireframe

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AUTONOMY CONSOLE                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│ [Current Levels] [Proposals] [History]                         [+ New]      │
├───────────────────────────────────────┬─────────────────────────────────────┤
│                                       │                                     │
│ CURRENT AUTONOMY LEVELS               │ PROPOSAL STATUS                     │
│ ────────────────────────────────────  │ ──────────────────────────────────  │
│                                       │                                     │
│ invoice-processor    Full     89%     │ Pending ARAO Review:                │
│ expense-approver     Full     76%     │ • expense-approver: limit increase │
│ customer-service     Suggest  92%     │   Submitted 3 days ago              │
│ order-validator      Full     45% ⚠️  │                                     │
│ data-enricher        Watch    —       │ Draft Proposals:                    │
│                                       │ • customer-service: → Full          │
│ [View Details] [Compare]              │ • order-validator: scope expansion  │
│                                       │                                     │
├───────────────────────────────────────┴─────────────────────────────────────┤
│                                                                             │
│ EXPIRING SOON                                                               │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ⚠️ order-validator: Full autonomy expires Mar 1, 2026 (47 days)             │
│    [Start Renewal] [View History]                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
