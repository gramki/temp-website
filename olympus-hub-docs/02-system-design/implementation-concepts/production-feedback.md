# Production Feedback

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-09  
> **ADR:** [0081](../../decision-logs/0081-production-feedback-loop.md)

---

## Overview

**Production Feedback** is the mechanism by which observations, issues, and learnings from production workbenches flow back to development workbenches for incorporation into future releases. This completes the **Evolve** stage of the Automation Lifecycle.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PRODUCTION FEEDBACK FLOW                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   PRODUCTION WORKBENCHES                    DEVELOPMENT WORKBENCH           │
│                                                                              │
│   ┌─────────────────────────┐                                               │
│   │ dispute-ops-prod-apac   │────┐                                          │
│   │                         │    │                                          │
│   │  Agent ─── Promote ─────┤    │                                          │
│   │  Supervisor ── Promote ─┤    │   ┌─────────────────────────┐            │
│   │                         │    ├──▶│ dispute-ops-dev         │            │
│   └─────────────────────────┘    │   │                         │            │
│                                  │   │  APO Inbox ◀── Review   │            │
│   ┌─────────────────────────┐    │   │       │                 │            │
│   │ dispute-ops-prod-emea   │────┤   │       ├── Accept        │            │
│   │                         │    │   │       ├── Reject        │            │
│   │  Supervisor ── Promote ─┤    │   │       ├── Route to PA   │            │
│   │                         │    │   │       └── Resolve       │            │
│   └─────────────────────────┘    │   │                         │            │
│                                  │   └─────────────────────────┘            │
│   ┌─────────────────────────┐    │              │                           │
│   │ dispute-ops-staging     │────┘              │                           │
│   │                         │                   ▼                           │
│   │  Developer ── Promote ──┤    Status Reflected Back                      │
│   │                         │                                               │
│   └─────────────────────────┘                                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Why Production Feedback?

| Problem | Solution |
|---------|----------|
| Operational issues have no formal channel to development | Structured promotion with lineage |
| APO must manually gather feedback | Centralized inbox with filtering |
| Actions on feedback are not tracked | Full lifecycle with status reflection |
| No link between issue and fix | Resolution links to scenario version |

---

## Key Concepts

### Feedback Topology

Workbenches form an **N:1 feedback topology**:

- Each non-development workbench (STAGING, PROD) can point to **one** development workbench
- Multiple production workbenches can point to the **same** development workbench
- The development workbench is where the APO resides and reviews feedback

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-ops-prod-apac
spec:
  dev_lifecycle_stage: PROD
  
  # Feedback configuration
  feedback:
    development_workbench_ref: dispute-ops-dev
    enabled: true
```

### Feedback Entity Types

Two top-level entities with subtypes:

#### Problems

Defects and constraints requiring remediation:

| Subtype | Description | Severity Levels |
|---------|-------------|-----------------|
| **Bug** | Implementation defect | Critical, High, Medium, Low |
| **Issue** | Operational constraint | High, Medium, Low |
| **Critical Limitation** | Capability gap blocking operations | Critical only |

#### Feedback

Observations and suggestions for improvement:

| Subtype | Description | Severity Levels |
|---------|-------------|-----------------|
| **Observation** | Behavioral pattern or anomaly | Medium, Low |
| **Suggestion** | Improvement idea | Low |
| **Learning** | Validated insight worth incorporating | Medium, Low |

---

## Feedback Lifecycle

### States

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│ PENDING  │────▶│ IN_REVIEW│────▶│ ACCEPTED │────▶│ RESOLVED │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
     │                │                │
     │                │                │
     ▼                ▼                ▼
┌──────────┐     ┌──────────┐     ┌──────────┐
│ (waiting │     │ REJECTED │     │ ROUTED   │
│  in inbox)│    │          │     │ (to PA/  │
└──────────┘     └──────────┘     │  Dev)    │
                                  └──────────┘
```

| State | Description |
|-------|-------------|
| `pending` | Promoted, waiting in APO inbox |
| `in_review` | APO is actively reviewing |
| `accepted` | APO accepted for implementation |
| `rejected` | APO rejected (with reason) |
| `routed` | APO routed to PA or Developer |
| `resolved` | Fix delivered, linked to scenario version |

### State Transitions

| Transition | Trigger | Effect |
|------------|---------|--------|
| `pending` → `in_review` | APO opens feedback | Promoter notified |
| `in_review` → `accepted` | APO clicks Accept | Status reflected to source |
| `in_review` → `rejected` | APO clicks Reject | Reason sent to source |
| `in_review` → `routed` | APO routes | Target persona notified |
| `accepted` → `resolved` | APO links fix | Resolution details sent to source |

---

## Lineage Information

Every feedback item includes immutable lineage:

```json
{
  "feedback_id": "fb-12345",
  "type": "Problem",
  "subtype": "Bug",
  "severity": "high",
  
  "content": {
    "title": "Escalation not triggering for priority disputes",
    "description": "When a dispute is marked as priority...",
    "attachments": []
  },
  
  "lineage": {
    "source_workbench_id": "dispute-ops-prod-apac",
    "source_workbench_stage": "PROD",
    "promoted_by": "supervisor@acme.com",
    "promoted_at": "2026-01-09T10:30:00Z",
    "promoted_from_desk": "supervisor-desk",
    
    "related_entities": {
      "requests": ["req-abc", "req-def"],
      "tasks": ["task-123"],
      "scenarios": ["standard-dispute"]
    }
  },
  
  "status": {
    "state": "in_review",
    "updated_at": "2026-01-09T11:00:00Z",
    "updated_by": "apo@acme.com"
  },
  
  "resolution": null
}
```

---

## Action Reflection

When APO takes action, the status is **reflected back** to the source workbench:

| APO Action | Source Effect |
|------------|---------------|
| **Accept** | `status.state` → `accepted`, promoter notified |
| **Reject** | `status.state` → `rejected`, reason included, promoter notified |
| **Route** | `status.state` → `routed`, target indicated, promoter notified |
| **Resolve** | `status.state` → `resolved`, resolution details included, promoter + supervisor notified |

### Resolution Details

When feedback is resolved:

```json
{
  "resolution": {
    "scenario_version": "1.4.0",
    "release_notes": "Fixed escalation trigger timing for priority disputes",
    "fix_reference": "commit-abc123",
    "resolved_by": "developer@acme.com",
    "resolved_at": "2026-01-15T14:00:00Z",
    "deployment_date": "2026-01-16"
  }
}
```

---

## Persona Responsibilities

### Source Workbench Personas

| Persona | Capabilities |
|---------|-------------|
| **Agent** | Promote bugs, observations from task context |
| **Supervisor** | Promote issues, bugs, observations, suggestions |
| **Auditor** | Promote compliance observations, process gaps |
| **Developer** (in staging) | Promote bugs found during testing |

### Development Workbench Personas

| Persona | Capabilities |
|---------|-------------|
| **APO** | Review inbox, accept/reject/route, resolve |
| **Process Architect** | Receive routed feedback, update normative specs |
| **Developer** | Receive routed feedback, implement fixes |

---

## Scope Exclusions

Production Feedback is specifically for **automation and process enhancement**. The following are handled through separate mechanisms:

| Excluded | Mechanism |
|----------|-----------|
| Knowledge evolution | Knowledge Services (per workbench) |
| Enterprise Memory promotion | CAF and Memory Services |
| Agent Memory evolution | Seer memory systems |
| Cross-tenant learnings | Enterprise Learning Services (future) |

---

## Integration Points

### Desks

| Desk | Capability |
|------|------------|
| **Agent Desk** | Feedback Promotion dialog |
| **Supervisor Desk** | Feedback Console with local and promoted views |
| **Automation Product Desk** | Production Feedback Inbox (dev workbenches) |

### APIs

| Channel | Endpoints |
|---------|-----------|
| **Agent REST** | `POST /feedback`, `GET /feedback/promoted` |
| **Supervisor REST** | `POST /feedback`, `GET /feedback`, `POST /feedback/{id}/promote` |
| **Creator REST** | `GET /feedback/inbox`, `POST /feedback/inbox/{id}/accept`, etc. |

### MCP Tools

| Role | Tools |
|------|-------|
| **Promotion** | `promote_feedback`, `list_promoted_feedback`, `get_feedback_status` |
| **Inbox** | `list_feedback_inbox`, `accept_feedback`, `reject_feedback`, `route_feedback`, `resolve_feedback` |

---

## Configuration

### Enable Feedback for a Workbench

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-ops-prod-apac
spec:
  dev_lifecycle_stage: PROD
  
  feedback:
    # Reference to development workbench
    development_workbench_ref: dispute-ops-dev
    
    # Enable/disable feedback promotion
    enabled: true
    
    # Optional: restrict which personas can promote
    allowed_promoters:
      - role: supervisor
      - role: agent
```

### Feedback Notifications

```yaml
feedback:
  notifications:
    on_promote:
      - group: dev-team
    on_accept:
      - role: promoter
    on_reject:
      - role: promoter
    on_resolve:
      - role: promoter
      - role: supervisor
```

---

## Related Documentation

- [ADR-0081: Production Feedback Loop](../../decision-logs/0081-production-feedback-loop.md) — Architecture decision
- [Automation Lifecycle Journey](../../08-personas-and-journeys/journeys/automation-lifecycle.md) — Full lifecycle context
- [Production Feedback Journey](../../08-personas-and-journeys/journeys/production-feedback-loop.md) — Step-by-step workflow
- [Automation Product Desk](../../06-ux-architecture/tenant-domain/automation-product-desk.md) — APO interface
- [Dev-Lifecycle-Stage](./dev-lifecycle-stage.md) — Workbench stage definitions
- [Promotion](./promotion.md) — Forward artifact promotion (complementary concept)

