# Intent Formalization

> **Status:** 🟡 Draft

---

## Overview

An **Intent** is the formalized business case for automation, created and owned by the APO. Intents capture the "why" — business problem, value proposition, success criteria, and proposed approach — before design begins.

---

## Intent Schema

```yaml
apiVersion: hub.olympus.io/v1
kind: AutomationIntent
metadata:
  id: intent-67890
  name: dispute-auto-triage
  namespace: acme-bank
spec:
  # Display
  title: "Automated Dispute Triage"
  summary: "Automatically categorize and route incoming disputes"
  
  # Origin
  source_ideas:
    - idea-12345
    - idea-12346      # Multiple ideas can contribute
  
  # Business Case
  problem_statement: |
    Manual triage takes 15 minutes per dispute.
    Triage errors cause 20% of disputes to be misrouted.
    Agents spend 30% of time on routine categorization.
  
  value_proposition: |
    Automated triage will reduce handling time by 80%,
    eliminate misrouting, and free agents for complex cases.
  
  # Success Criteria
  success_criteria:
    - metric: "Average triage time"
      baseline: 15       # minutes
      target: 3          # minutes
      unit: "minutes"
      measurement: "Request analytics"
    
    - metric: "Misrouting rate"
      baseline: 20       # percent
      target: 2          # percent
      unit: "percent"
      measurement: "Escalation analysis"
    
    - metric: "Agent time on routine"
      baseline: 30       # percent
      target: 5          # percent
      unit: "percent"
      measurement: "Task type analysis"
  
  # Scope
  scope:
    in_scope:
      - "Standard disputes (card, ACH, wire)"
      - "Routine categorization"
      - "Initial routing to correct queue"
    out_of_scope:
      - "Complex disputes requiring investigation"
      - "Regulatory disputes"
      - "Cross-border disputes"
  
  # Approach
  automation_approach: agentic    # conventional | agentic | hybrid | undecided
  approach_rationale: |
    Disputes have unstructured descriptions requiring natural language understanding.
    Routing rules are complex and context-dependent.
    AI agent can learn from historical routing decisions.
  
  # Stakeholders
  stakeholders:
    sponsor: coo@acme.com
    accountable: apo@acme.com
    consulted:
      - dispute-ops-lead@acme.com
      - compliance@acme.com
    informed:
      - customer-experience@acme.com

status:
  state: complete               # draft | complete | accepted | withdrawn
  
  owner: apo@acme.com
  created_at: "2026-01-09T10:00:00Z"
  completed_at: "2026-01-09T14:00:00Z"
  
  # PA Review (populated when submitted)
  submitted_to_pa_at: null
  pa_reviewer: null
  
  # Charter (populated when accepted)
  charter_id: null
```

---

## Intent Lifecycle

```
           ┌──────────┐
           │  DRAFT   │
           └────┬─────┘
                │
                │ APO completes
                ▼
           ┌──────────┐
           │ COMPLETE │
           └────┬─────┘
                │
                │ Submit to PA
                ▼
    ┌───────────┴───────────┐
    │                       │
    ▼                       ▼
┌──────────┐          ┌──────────┐
│ ACCEPTED │          │ WITHDRAWN│
│          │          │          │
│→ Charter │          │ Closed   │
└──────────┘          └──────────┘
```

| State | Description | Owner | Next States |
|-------|-------------|-------|-------------|
| `draft` | APO is building the Intent | APO | `complete`, `withdrawn` |
| `complete` | Ready for PA review | APO | `accepted`, `withdrawn` |
| `accepted` | PA accepted, becomes Charter | PA | Terminal (creates Charter) |
| `withdrawn` | APO withdrew the Intent | APO | Terminal |

---

## Creating an Intent

### From Promoted Idea

When APO promotes an Idea:

```
APO                           Ideation Services
 │                                  │
 ├─── Promote Idea ────────────────▶│
 │    (idea-12345)                  │
 │                                  ├─── Create Intent (draft)
 │                                  │    - source_ideas: [idea-12345]
 │                                  │    - Pre-populate from Idea
 │                                  │
 │◀── New Intent Created ───────────┤
 │    (intent-67890)                │
 │                                  │
 ├─── Complete Intent Details ─────▶│
 │                                  │
```

### Direct Creation

APO can also create Intents directly without an Idea:

```
APO                           Ideation Services
 │                                  │
 ├─── Create Intent ───────────────▶│
 │    (no source idea)              │
 │                                  ├─── Create Intent (draft)
 │                                  │    - source_ideas: []
 │                                  │
 │◀── New Intent Created ───────────┤
 │                                  │
```

---

## Intent Completion Checklist

Before an Intent can move to `complete`:

| Section | Required Fields |
|---------|-----------------|
| **Business Case** | Problem statement, Value proposition |
| **Success Criteria** | At least 1 metric with baseline + target |
| **Scope** | In-scope items (out-of-scope optional) |
| **Approach** | Selected approach with rationale |
| **Stakeholders** | Sponsor, Accountable (APO) |

---

## Approach Selection

APO proposes the automation approach:

| Approach | When to Use | Validation |
|----------|-------------|------------|
| **Conventional** | Structured inputs, clear rules | PA reviews feasibility |
| **Agentic** | Unstructured, judgment needed | PA + CSA review feasibility |
| **Hybrid** | Mix of both | PA defines boundaries |
| **Undecided** | Need more analysis | PA helps decide |

### Approach Selection Criteria

| Criterion | → Conventional | → Agentic |
|-----------|---------------|-----------|
| Input structure | Structured, predictable | Unstructured, variable |
| Decision logic | Rules capture 90%+ | Judgment required |
| Exception rate | Low, predictable | High, contextual |
| Risk tolerance | Low | Moderate (with guardrails) |
| Process maturity | Well-documented SOPs | Expertise-based |

---

## Submitting to PA

When Intent is complete, APO submits for PA review:

```
APO                           PA                          Ideation
 │                             │                              │
 ├─── Submit Intent ──────────────────────────────────────────▶│
 │                             │                              │
 │                             │◀── Notification: New Intent ──┤
 │                             │                              │
 │                             ├─── Review Intent ────────────▶│
 │                             │                              │
 │                             │    Assess:                   │
 │                             │    - Design feasibility      │
 │                             │    - Approach validity       │
 │                             │    - Resource availability   │
 │                             │                              │
 │                             ├─── Accept Intent ────────────▶│
 │                             │                              │
 │                             │                              ├─── Create Charter
 │                             │                              │
 │◀── Charter Created ─────────┼──────────────────────────────┤
 │                             │                              │
```

---

## APIs

### REST (Creator Channel)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/intents` | Create new Intent |
| `GET` | `/intents` | List Intents (with filters) |
| `GET` | `/intents/{intent_id}` | Get Intent details |
| `PUT` | `/intents/{intent_id}` | Update Intent |
| `POST` | `/intents/{intent_id}/complete` | Mark as complete |
| `POST` | `/intents/{intent_id}/submit` | Submit to PA for review |
| `POST` | `/intents/{intent_id}/withdraw` | Withdraw Intent |

### MCP (Creator Channel)

| Tool | Description |
|------|-------------|
| `create_intent` | Create new Intent |
| `list_intents` | List with filters |
| `get_intent` | Get details |
| `update_intent` | Update Intent |
| `submit_intent_to_pa` | Submit for PA review |

---

## Related Documentation

- [Idea Management](./idea-management.md) — Source of Intents
- [Charter Acceptance](./charter-acceptance.md) — Next stage
- [Automation Product Owner](../../08-personas-and-journeys/personas/automation-product-owner.md)

