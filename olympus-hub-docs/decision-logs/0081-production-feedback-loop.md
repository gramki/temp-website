# ADR-0081: Production Feedback Loop

> **Status:** Accepted  
> **Date:** 2026-01-09  
> **Category:** workbench-management

---

## Context

Hub's promotion model moves artifacts **forward** — from development to staging to production. However, there is no structured mechanism for feedback to flow **backward** — from production workbenches to development workbenches.

Currently:
- Observations, bugs, issues, and learnings identified during Run stage have no formal channel back to development
- APO and Process Architect must manually gather feedback through external channels
- Actions taken on feedback are not systematically tracked or reflected back to production

This creates a gap in the Evolve stage of the Automation Lifecycle, where operational learnings should inform design improvements.

### Workbench Topology

Hub supports multiple deployments of a workbench specification:
- A workbench specification can have N deployed instances
- Instances are assigned to Dev-Lifecycle-Stages (DEV, STAGING, PROD, etc.)
- Multiple production instances may exist (regional deployments, customer segments, etc.)

The need is for production instances to **feed back** to the development instance where the APO resides.

---

## Decision

### 1. Development Workbench Reference

Every non-development workbench (STAGING, PROD, etc.) **may** configure a reference to a development workbench:

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-ops-prod-apac
spec:
  # ... other configuration
  
  dev_lifecycle_stage: PROD
  
  # Feedback configuration
  feedback:
    development_workbench_ref: dispute-ops-dev
    enabled: true
```

### 2. Feedback Topology

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      FEEDBACK TOPOLOGY (N:1)                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   PRODUCTION INSTANCES                    DEVELOPMENT INSTANCE              │
│                                                                              │
│   ┌─────────────────────────┐                                               │
│   │ dispute-ops-prod-apac   │────┐                                          │
│   │ (PROD)                  │    │                                          │
│   └─────────────────────────┘    │                                          │
│                                  │        ┌─────────────────────────┐       │
│   ┌─────────────────────────┐    ├───────▶│ dispute-ops-dev         │       │
│   │ dispute-ops-prod-emea   │────┤        │ (DEV)                   │       │
│   │ (PROD)                  │    │        │                         │       │
│   └─────────────────────────┘    │        │ APO reviews feedback    │       │
│                                  │        └─────────────────────────┘       │
│   ┌─────────────────────────┐    │                                          │
│   │ dispute-ops-staging     │────┘                                          │
│   │ (STAGING)               │                                               │
│   └─────────────────────────┘                                               │
│                                                                              │
│   CONSTRAINTS:                                                               │
│   • Each source can point to only ONE development workbench                 │
│   • Multiple sources can point to the same development workbench            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3. Feedback Entity Types

Two top-level entities with subtypes:

#### Problems

Defects, constraints, and limitations requiring remediation:

| Subtype | Description | Typical Source |
|---------|-------------|----------------|
| **Bug** | Implementation defect | Agent, Supervisor |
| **Issue** | Operational constraint | Supervisor, Auditor |
| **Critical Limitation** | Capability gap blocking operations | Supervisor, APO |

#### Feedback

Observations and suggestions for improvement:

| Subtype | Description | Typical Source |
|---------|-------------|----------------|
| **Observation** | Behavioral pattern or anomaly | Agent, Supervisor |
| **Suggestion** | Improvement idea | Agent, Supervisor |
| **Learning** | Validated insight worth incorporating | APO, Supervisor |

### 4. Feedback Promotion Flow

```
SOURCE WORKBENCH                          DEVELOPMENT WORKBENCH
(STAGING/PROD)                            (DEV)

┌─────────────────────────┐              ┌─────────────────────────┐
│  Any Persona Desk       │              │  APO Desk               │
│                         │              │                         │
│  ┌───────────────────┐  │   Promote    │  ┌───────────────────┐  │
│  │ Problem/Feedback  │  │─────────────▶│  │ Inbox             │  │
│  │ (with lineage)    │  │              │  │                   │  │
│  └───────────────────┘  │              │  │ • Review          │  │
│                         │              │  │ • Triage          │  │
│                         │              │  │ • Route           │  │
│                         │              │  │ • Act             │  │
│                         │              │  └───────────────────┘  │
│                         │              │           │             │
│                         │              │           ▼             │
│  ┌───────────────────┐  │   Reflect    │  ┌───────────────────┐  │
│  │ Status Updated    │◀─│─────────────│  │ Actions Taken     │  │
│  │                   │  │              │  │                   │  │
│  └───────────────────┘  │              │  └───────────────────┘  │
│                         │              │                         │
└─────────────────────────┘              └─────────────────────────┘

KEY PRINCIPLES:
• Any persona can promote from their desk
• Promotion is immediate (no pre-approval)
• APO in development workbench reviews and triages
• Actions on feedback are reflected back to source
```

### 5. Lineage Information

Every promoted item includes:

```yaml
feedback_item:
  id: "fb-12345"
  type: "Problem"
  subtype: "Bug"
  
  content:
    title: "Escalation not triggering for priority disputes"
    description: "..."
    severity: "high"
  
  # Lineage (immutable)
  lineage:
    source_workbench_id: "dispute-ops-prod-apac"
    source_workbench_stage: "PROD"
    promoted_by: "supervisor@acme.com"
    promoted_at: "2026-01-09T10:30:00Z"
    promoted_from_desk: "supervisor-desk"
    
    # Context at time of promotion
    related_requests: ["req-abc", "req-def"]
    related_scenarios: ["standard-dispute"]
    related_tasks: ["task-123"]
  
  # Status (mutable)
  status:
    state: "in_review"  # pending | in_review | accepted | rejected | resolved
    updated_at: "2026-01-09T11:00:00Z"
    updated_by: "apo@acme.com"
```

### 6. Action Reflection

When APO or other personas take action on feedback in the development workbench, the action is reflected back to the source:

| Action | Reflected Status | Source Notification |
|--------|------------------|---------------------|
| **Accept** | `accepted` | Promoter notified |
| **Reject** | `rejected` (with reason) | Promoter notified |
| **Resolve** | `resolved` (with link to fix) | Promoter + Supervisor notified |
| **Route** | `routed` (to PA, Developer) | Promoter notified of routing |

### 7. Desk Integration

Each desk in source workbenches gains a **Feedback Promotion** capability:

| Desk | Typical Promotions |
|------|-------------------|
| **Agent Desk** | Bugs, Observations |
| **Supervisor Desk** | Issues, Bugs, Observations, Suggestions |
| **Steward Desk** | Issues, Critical Limitations |
| **Auditor Desk** | Compliance observations, Process gaps |
| **APO Desk** | Strategic feedback, Learnings |

### 8. APO Desk: Feedback Inbox

The APO Desk in the development workbench gains a **Feedback Console**:

| Capability | Description |
|------------|-------------|
| **Inbox** | View all incoming feedback from linked workbenches |
| **Filter** | Filter by source workbench, type, severity, status |
| **Triage** | Accept, reject, or route feedback |
| **Link** | Link feedback to backlog items |
| **Resolve** | Mark resolved and link to fix |

### 9. API Support

#### REST APIs

```
# APO Channel (Development Workbench)
GET  /feedback/inbox                    # List all incoming feedback
GET  /feedback/{id}                     # Get specific feedback item
POST /feedback/{id}/accept              # Accept feedback
POST /feedback/{id}/reject              # Reject with reason
POST /feedback/{id}/route               # Route to PA/Developer
POST /feedback/{id}/resolve             # Mark resolved

# Persona Channels (Source Workbenches)
POST /feedback                          # Promote new feedback
GET  /feedback/promoted                 # View promoted items and status
GET  /feedback/{id}/status              # Get status of promoted item
```

#### MCP Tools

```yaml
# APO MCP Channel (Development Workbench)
- list_feedback_inbox
- get_feedback_details
- accept_feedback
- reject_feedback
- route_feedback
- resolve_feedback

# Persona MCP Channels (Source Workbenches)
- promote_feedback
- list_my_promoted_feedback
- get_promoted_feedback_status
```

---

## Scope Exclusions

This ADR covers **automation and process enhancement feedback** only.

**NOT in scope:**
- Knowledge evolution (handled by Knowledge Services in respective workbenches)
- Enterprise Memory evolution (handled by CAF and Memory Services)
- Agent Memory evolution (handled by Seer memory systems)

These are managed through different mechanisms within each workbench deployment.

---

## Consequences

### Positive

1. **Structured feedback channel** — Formal path for operational learnings to reach development
2. **APO visibility** — APO sees all feedback across deployments in one inbox
3. **Lineage tracking** — Full provenance of where feedback originated
4. **Action transparency** — Actions reflected back to source workbenches
5. **Supports Evolve stage** — Enables the Automation Lifecycle Evolve → Design flow

### Negative

1. **Configuration required** — Each workbench must configure its development reference
2. **APO inbox management** — High-volume deployments may generate significant feedback
3. **Cross-workbench complexity** — Feedback flows across workbench boundaries

### Neutral

1. **Optional feature** — Workbenches can disable feedback if not needed
2. **Separate from promotion** — Feedback is not artifacts; uses different channel than promotion
3. **No knowledge scope** — Deliberately excludes knowledge evolution to avoid confusion

---

## Alternatives Considered

### 1. Use Existing Promotion Model

Extend the existing promotion model to support "reverse promotion."

**Rejected because:**
- Promotion is for artifacts (Scenarios, Apps), not observations
- Semantic mismatch between "promote code" and "report issue"

### 2. External Issue Tracker

Rely on external tools (Jira, ServiceNow) for feedback management.

**Rejected because:**
- Loses lineage to Hub entities (Requests, Tasks, Scenarios)
- No automatic reflection back to source workbenches
- External tool dependency

### 3. Single Feedback Type

Single entity type with `kind` field instead of Problem/Feedback split.

**Rejected because:**
- Problems and Feedback have different lifecycles
- Problems may require SLA tracking; Feedback is advisory

---

## Related Documentation

- [Workbench Anatomy](../02-system-design/workbench-anatomy.md) — Workbench structure
- [Dev-Lifecycle-Stages](../04-subsystems/artifact-registry/dev-lifecycle-stages.md) — Stage definitions
- [Promotion Model](../04-subsystems/artifact-registry/promotion-model.md) — Forward promotion
- [Automation Lifecycle](../08-personas-and-journeys/journeys/automation-lifecycle.md) — Lifecycle stages
- [Automation Product Desk](../06-ux-architecture/tenant-domain/automation-product-desk.md) — APO workspace

