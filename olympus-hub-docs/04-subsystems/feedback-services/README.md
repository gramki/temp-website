# Feedback Services

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-09  
> **ADR:** [0081](../../decision-logs/0081-production-feedback-loop.md)

---

## Overview

**Feedback Services** manages the flow of operational feedback from production workbenches to development workbenches. This enables continuous improvement by capturing bugs, issues, and suggestions from those closest to operations.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FEEDBACK FLOW                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  PRODUCTION WORKBENCHES                    DEVELOPMENT WORKBENCH            │
│                                                                              │
│  ┌─────────────────────────┐                                                │
│  │ dispute-ops-prod-apac   │────┐                                           │
│  │  Agent ── Promote       │    │                                           │
│  │  Supervisor ── Promote  │    │   ┌─────────────────────────┐             │
│  └─────────────────────────┘    ├──▶│ dispute-ops-dev         │             │
│                                 │   │                         │             │
│  ┌─────────────────────────┐    │   │  APO Inbox              │             │
│  │ dispute-ops-prod-emea   │────┤   │  ├── Review             │             │
│  │  Supervisor ── Promote  │    │   │  ├── Accept / Reject    │             │
│  └─────────────────────────┘    │   │  ├── Route to PA/Dev    │             │
│                                 │   │  └── Resolve            │             │
│  ┌─────────────────────────┐    │   │                         │             │
│  │ dispute-ops-staging     │────┘   └─────────────────────────┘             │
│  │  Developer ── Promote   │                    │                           │
│  └─────────────────────────┘                    │                           │
│                                                 ▼                           │
│                                    Status Reflected Back                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Concepts

| Term | Definition |
|------|------------|
| **Problem** | Defect or constraint requiring remediation (Bug, Issue, Critical Limitation) |
| **Feedback** | Observation or suggestion for improvement (Observation, Suggestion, Learning) |
| **Promotion** | Act of sending feedback from source to development workbench |
| **Inbox** | APO's queue of incoming feedback in development workbench |
| **Resolution** | APO's decision and action on feedback |

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Feedback Entities](./feedback-entities.md) | Problem and Feedback types, schemas | 🟡 Draft |
| [Feedback Promotion](./feedback-promotion.md) | Promotion flow and lineage | 🟡 Draft |
| [Feedback Inbox](./feedback-inbox.md) | APO inbox management | 🟡 Draft |
| [Resolution Tracking](./resolution-tracking.md) | Resolution lifecycle and reflection | 🟡 Draft |

---

## Feedback Topology

### N:1 Relationship

Multiple non-development workbenches can feed into one development workbench:

```yaml
# Production workbench configuration
workbench:
  id: dispute-ops-prod-apac
  dev_lifecycle_stage: PROD
  feedback:
    development_workbench_ref: dispute-ops-dev
    enabled: true
```

### Stage Attribution

- `Dev-Lifecycle-Stage` is attributed to the **workbench instance**, not specification
- `dispute-ops-dev` (DEV stage) and `dispute-ops-prod-apac` (PROD stage) are distinct instances

---

## Feedback Entity Types

### Problems

Defects and constraints requiring resolution:

| Subtype | Severity | Description |
|---------|----------|-------------|
| **Bug** | Critical, High, Medium, Low | Implementation defect |
| **Issue** | High, Medium, Low | Operational constraint |
| **Critical Limitation** | Critical | Capability gap blocking operations |

### Feedback

Observations and suggestions:

| Subtype | Severity | Description |
|---------|----------|-------------|
| **Observation** | Medium, Low | Behavioral pattern or anomaly |
| **Suggestion** | Low | Improvement idea |
| **Learning** | Medium, Low | Validated insight |

---

## Feedback Lifecycle

```
                    ┌──────────────┐
                    │   PENDING    │  (in APO inbox)
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  IN_REVIEW   │  (APO reviewing)
                    └──────┬───────┘
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
       ▼                   ▼                   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   ACCEPTED   │    │   REJECTED   │    │    ROUTED    │
│              │    │              │    │              │
│ → Backlog    │    │ Closed       │    │ → PA or Dev  │
└──────┬───────┘    └──────────────┘    └──────┬───────┘
       │                                       │
       └───────────────┬───────────────────────┘
                       │
                       ▼
                ┌──────────────┐
                │   RESOLVED   │
                │              │
                │ Fix deployed │
                └──────────────┘
```

---

## Who Can Promote

| Persona | Can Promote From | Types |
|---------|------------------|-------|
| **Agent** | Agent Desk | Bug, Observation |
| **Supervisor** | Supervisor Desk | Bug, Issue, Observation, Suggestion |
| **Auditor** | Auditor Desk | Observation, Learning |
| **Developer** (staging) | Development Desk | Bug |
| **APO** (production) | APO Desk | All types |

---

## Integration Points

| Component | Integration |
|-----------|-------------|
| **Automation Ideation** | Suggestions can be promoted to Ideas |
| **Automation Product Desk** | APO manages Feedback Inbox |
| **Agent Desk** | Agents promote feedback |
| **Supervisor Desk** | Supervisors promote feedback |
| **Workbench Management** | Workbench configuration for feedback |
| **Notification Services** | Promoter notifications |

---

## Action Reflection

When APO takes action, status is reflected to source workbench:

| APO Action | Source Effect |
|------------|---------------|
| **Accept** | Status → `accepted`, promoter notified |
| **Reject** | Status → `rejected`, reason included |
| **Route** | Status → `routed`, target indicated |
| **Resolve** | Status → `resolved`, fix details included |

---

## Scope Exclusions

Feedback Services handles **automation and process enhancement**. The following are handled separately:

| Excluded | Mechanism |
|----------|-----------|
| Knowledge evolution | Knowledge Services (per workbench) |
| Enterprise Memory promotion | CAF Enterprise Learning Services |
| Agent Memory evolution | Seer memory systems |

---

## Related Documentation

- [ADR-0081: Production Feedback Loop](../../decision-logs/0081-production-feedback-loop.md)
- [Production Feedback Concept](../../02-system-design/implementation-concepts/production-feedback.md)
- [Production Feedback Journey](../../08-personas-and-journeys/journeys/production-feedback-loop.md)
- [Automation Ideation](../automation-ideation/README.md) — Suggestions → Ideas
- [Automation Product Desk](../../06-ux-architecture/tenant-domain/automation-product-desk.md)

