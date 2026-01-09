# Idea Management

> **Status:** 🟡 Draft

---

## Overview

Ideas are **raw automation opportunities** submitted by anyone in the organization. The Idea Management service captures, reviews, and triages these opportunities before they become formalized Intents.

---

## Idea Sources

| Source | Channel | Example |
|--------|---------|---------|
| **Agent** | Agent Desk, MCP | "This manual verification could be automated" |
| **Supervisor** | Supervisor Desk | "We see this pattern repeatedly" |
| **Business User** | Business Portal | "I wish I could track status without calling" |
| **Production Feedback** | Feedback Services | Suggestion promoted to Idea |
| **APO** | APO Desk | Direct business insight |
| **External** | API | Partner or system integration |

---

## Idea Schema

```yaml
apiVersion: hub.olympus.io/v1
kind: Idea
metadata:
  id: idea-12345
  name: document-preview-in-solver
  namespace: acme-bank
spec:
  # Content
  title: "Add document preview in task solver"
  description: |
    Agents currently have to download and open documents externally.
    An inline preview would save 2-3 minutes per task.
  
  # Classification
  category: efficiency          # efficiency | quality | compliance | capability | cost
  estimated_value: medium       # high | medium | low
  urgency: normal               # critical | high | normal | low
  
  # Source
  submitted_by: agent@acme.com
  submitted_at: "2026-01-09T10:00:00Z"
  source_context:
    type: feedback              # direct | feedback | observation
    workbench_id: dispute-ops-prod-apac
    feedback_id: fb-789         # If from feedback services
  
  # Tags
  tags:
    - ux
    - agent-productivity
    - document-handling

status:
  state: submitted              # submitted | under_review | promoted | parked | rejected | merged
  
  # Review (populated by APO)
  reviewed_by: null
  reviewed_at: null
  review_notes: null
  
  # Promotion (if promoted to Intent)
  promoted_to_intent: null
  
  # Merge (if merged with another)
  merged_into: null
```

---

## Idea Lifecycle

```
                    ┌──────────────┐
                    │  SUBMITTED   │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ UNDER_REVIEW │
                    └──────┬───────┘
                           │
           ┌───────────────┼───────────────┬──────────────┐
           │               │               │              │
           ▼               ▼               ▼              ▼
    ┌──────────┐    ┌──────────┐    ┌──────────┐   ┌──────────┐
    │ PROMOTED │    │  PARKED  │    │ REJECTED │   │  MERGED  │
    │          │    │          │    │          │   │          │
    │→ Intent  │    │ Backlog  │    │ Closed   │   │→ Other   │
    └──────────┘    └──────────┘    └──────────┘   └──────────┘
```

| State | Description | Next States |
|-------|-------------|-------------|
| `submitted` | New idea awaiting review | `under_review` |
| `under_review` | APO is evaluating | `promoted`, `parked`, `rejected`, `merged` |
| `promoted` | Converted to Intent | Terminal |
| `parked` | Good idea, deferred to backlog | `under_review` (reactivate) |
| `rejected` | Not aligned or feasible | Terminal |
| `merged` | Combined with another Idea | Terminal |

---

## Review Workflow

### APO Reviews Idea

```
APO                              Idea Management              Submitter
 │                                     │                          │
 ├─── View Idea Queue ─────────────────│                          │
 │                                     │                          │
 │◀── Ideas (sorted by value/urgency) ─┤                          │
 │                                     │                          │
 ├─── Open Idea ───────────────────────│                          │
 │                                     │                          │
 │◀── Idea Details + Source Context ───┤                          │
 │                                     │                          │
 ├─── Decide: Promote / Park / Reject ─│                          │
 │                                     │                          │
 │                                     ├─── Notify Submitter ─────▶│
 │                                     │                          │
```

### Review Decision Criteria

| Criterion | Promote | Park | Reject |
|-----------|---------|------|--------|
| **Business Value** | Clear, measurable | Potential, unclear | None/minimal |
| **Alignment** | Fits strategy | Fits, not priority | Doesn't fit |
| **Feasibility** | Likely achievable | Unknown/complex | Not feasible |
| **Timing** | Now or soon | Future | Never |
| **Duplicate** | Unique | — | Merge with existing |

---

## Idea Queue Management

### Sorting and Filtering

| Filter | Options |
|--------|---------|
| **Status** | Submitted, Under Review, Parked |
| **Category** | Efficiency, Quality, Compliance, Capability, Cost |
| **Value** | High, Medium, Low |
| **Source** | Direct, Feedback, Observation |
| **Submitter** | By persona/user |

### Backlog (Parked Ideas)

Parked ideas remain in a backlog for future consideration:

- Periodic review (quarterly)
- Reactivate when priorities change
- Notify submitter if reactivated

---

## Integration with Feedback Services

When APO triages a **Suggestion** in the Feedback Inbox:

```
Feedback Services                    Ideation Services
      │                                    │
      ├─── APO clicks "Promote to Idea" ───▶│
      │                                    │
      │                                    ├─── Create Idea
      │                                    │    (with feedback_id reference)
      │                                    │
      │◀── Feedback status = "promoted" ────┤
      │                                    │
```

The new Idea includes:

```yaml
source_context:
  type: feedback
  workbench_id: dispute-ops-prod-apac
  feedback_id: fb-789
```

---

## APIs

### REST (Creator Channel)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/ideas` | Submit a new idea |
| `GET` | `/ideas` | List ideas (with filters) |
| `GET` | `/ideas/{idea_id}` | Get idea details |
| `PUT` | `/ideas/{idea_id}` | Update idea (submitter or APO) |
| `POST` | `/ideas/{idea_id}/review` | APO reviews idea |
| `POST` | `/ideas/{idea_id}/promote` | Promote to Intent |
| `POST` | `/ideas/{idea_id}/park` | Park idea |
| `POST` | `/ideas/{idea_id}/reject` | Reject idea |
| `POST` | `/ideas/{idea_id}/merge` | Merge with another idea |

### MCP (Creator Channel)

| Tool | Description |
|------|-------------|
| `submit_idea` | Submit a new idea |
| `list_ideas` | List ideas with filters |
| `get_idea` | Get idea details |
| `review_idea` | APO reviews and decides |
| `promote_idea_to_intent` | Convert to Intent |

---

## Related Documentation

- [Intent Formalization](./intent-formalization.md) — Next stage after promotion
- [Feedback Services](../feedback-services/README.md) — Source of suggestions
- [Automation Product Desk](../../06-ux-architecture/tenant-domain/automation-product-desk.md) — APO interface

