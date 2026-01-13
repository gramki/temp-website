# Persona Twins

> **Category:** UX Architecture
> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-14

---

## Overview

**Persona Twins** enable any Collaborator in a Workbench to create AI agent twins that delegate their responsibilities. Unlike Business Scenarios that handle organizational workflows, Persona Twin Scenarios are personal productivity agents that respond to tasks assigned to the delegator, platform notifications meant for them, and personally configured schedules. Persona Twins follow the standard three-layer agent lifecycle (Raw → Trained → Employed) with special recognition, isolation, and trigger mechanisms.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Agent** as an executor of work and **Role** as a functional responsibility. Persona Twins extend this by allowing collaborators to create personal AI agents that inherit their authority and act on their behalf.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Agent | Persona Twin | Personal AI agent for a collaborator |
| Role | Delegated Role | Twin inherits roles from delegator |
| Scenario | Persona Twin Scenario | Scenario labeled for personal delegation |
| Authority | User Delegation | Authority derived from delegator |

### Gap This Fills

The ontology focuses on organizational agents operating in business scenarios. Persona Twins address:
1. **Personal delegation**: Collaborators need personal assistants for routine tasks
2. **Individual triggers**: Tasks assigned to a specific person, not a role
3. **Privacy**: Personal workflows should be isolated from business scenarios
4. **Non-developer creation**: Any collaborator should be able to create twins without developer skills

---

## Definition

**Persona Twin** is an AI agent that a collaborator creates to handle tasks, notifications, and scheduled activities on their behalf, operating within the same authority boundaries as the delegator.

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-scoped; one twin per scenario |
| **Lifecycle** | Created from Persona Twin Blueprint → Trained → Employed; follows standard agent lifecycle |
| **Ownership** | Delegator (the collaborator who creates it) owns and manages the twin |
| **Multiplicity** | A collaborator can have multiple Persona Twins in a workbench |

---

## Rationale

### Why This Design?

Persona Twins are designed to:
1. **Empower collaborators**: Any collaborator, not just developers, can create personal AI assistants
2. **Reuse existing infrastructure**: Built on existing agent lifecycle, scenario, and trigger systems
3. **Maintain governance**: Subject to same authority delegation, guardrails, and audit as business agents
4. **Preserve privacy**: Private visibility option keeps personal workflows confidential

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| Separate "Personal Agent" system | Would duplicate agent lifecycle infrastructure; inconsistent governance |
| Business Scenarios for personal tasks | No isolation, privacy, or personal trigger mechanisms |
| Client-side assistants | No authority delegation, no platform integration |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0121](../../../olympus-hub-docs/decision-logs/0121-persona-twin-blueprint-structure.md) | Persona Twin Blueprint extends Trained Agent Blueprint |
| [ADR-0122](../../../olympus-hub-docs/decision-logs/0122-persona-twin-scenario-isolation.md) | Metadata label + category for isolation |
| [ADR-0123](../../../olympus-hub-docs/decision-logs/0123-persona-twin-trigger-mechanisms.md) | Task assignment creates new Request in twin scenario |
| [ADR-0124](../../../olympus-hub-docs/decision-logs/0124-persona-twin-visibility-controls.md) | Scenario-level visibility controls |

---

## Structure

### Key Attributes

```yaml
# Persona Twin Scenario
scenario:
  id: string
  name: string
  workbench_id: string
  metadata:
    labels:
      persona-twin: "true"
    category: "persona-twin"
    visibility: "public" | "private"
    delegator: "user:john.smith@acme.com"
  application:
    automation_system: seer
    application_id: string

# Training Spec with Persona Twin metadata
trainingSpec:
  metadata:
    labels:
      persona-twin: "true"
    personaTwin:
      delegator: "user:john.smith@acme.com"
      blueprintSource: "collaborator-assistant-base:1.0.0"

# Employment Spec with delegation
employmentSpec:
  delegation:
    type: user
    delegator: "user:john.smith@acme.com"
    accountable: "user:john.smith@acme.com"  # Same as delegator
    roles: "*"  # Inherits delegator's roles
    groups: "*" # Inherits delegator's groups
```

### States

| State | Description | Transitions |
|-------|-------------|-------------|
| **Draft** | Training Spec created, not yet trained | → Training |
| **Training** | Twin being trained in workbench | → Trained, Failed |
| **Trained** | Training complete, not yet employed | → Employed |
| **Employed** | Active and responding to triggers | → Suspended, Revoked |
| **Suspended** | Temporarily disabled | → Employed, Revoked |
| **Revoked** | Permanently disabled | Terminal |

---

## Behavior

### How It Works

```
1. Collaborator selects Persona Twin Blueprint
   └── Blueprint provides signal suggestions and OPA filter templates

2. Collaborator configures Training Spec
   ├── Selects which signals to respond to
   ├── Configures OPA filters for each signal
   ├── Customizes skills and behavior prompts
   └── Sets knowledge base bindings

3. Collaborator trains twin in workbench
   └── Tests with sample scenarios, refines behavior

4. Collaborator deploys twin (creates Employment Spec)
   ├── Configures authority delegation (roles, scopes, groups)
   ├── Sets scenario visibility (public or private)
   └── Activates triggers

5. Twin responds to triggers
   ├── Task assigned to delegator → Creates Request in twin's scenario
   ├── Platform notification for delegator → Creates Request
   └── Scheduled time → Creates Request (via Kale)

6. Twin processes Request
   ├── Performs delegated work
   ├── May update original task, send notifications, etc.
   └── Actions subject to authority ceilings and guardrails
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Task Management System | ← | Receives task assignment signals |
| Platform Notifications | ← | Receives notification signals |
| Kale Scheduler | ← | Receives scheduled signals |
| Signal Exchange | ↔ | Trigger evaluation, request creation |
| Cipher IAM Extensions | → | Authority delegation configuration |
| Agent Lifecycle Manager | → | Manages employment and directory |

---

## Trigger Types

### 1. Task Assignment Trigger

When a task is assigned to the delegator, creates a new Request in the twin's scenario.

```yaml
trigger:
  name: "delegator-task-assignment"
  type: task_assignment
  target:
    workbench: "dispute-ops"
    scenario: "john-smith-assistant"
  conditions:
    assignee: "user:john.smith@acme.com"
    opaFilter: |
      package persona.twin.task_filter
      default allow = false
      allow {
        input.payload.task.priority == "high"
      }
  transform:
    request_type: "PersonaTwinTask"
    mapping:
      original_task_id: "$.task.id"
      delegator: "$.task.assignee"
```

### 2. Platform Notification Trigger

When a platform notification is sent to the delegator, routes to the twin's scenario.

```yaml
trigger:
  name: "delegator-notification"
  type: platform_notification
  target:
    workbench: "dispute-ops"
    scenario: "john-smith-assistant"
  conditions:
    recipient: "user:john.smith@acme.com"
    scope: "workbench"
```

### 3. Time Schedule Trigger

Cron-like schedules via Kale scheduler.

```yaml
trigger:
  name: "daily-summary"
  gateway: kale
  schedule:
    cron: "0 17 * * *"  # 5 PM daily
    timezone: "America/New_York"
  target:
    workbench: "dispute-ops"
    scenario: "john-smith-assistant"
  transform:
    request_type: "ScheduledSummary"
```

---

## Authority Delegation Model

### Delegator as Accountable Human

For Persona Twins, the **delegator** is also the **accountable human**:

```yaml
delegation:
  type: user
  delegator: "user:john.smith@acme.com"
  accountable: "user:john.smith@acme.com"  # Same person
  roles: "*"
  groups: "*"
```

### Authority Narrowing

The twin's authority is always a subset of the delegator's current authority:
- If delegator loses a role, twin loses it too
- OPA policies per PEP can further restrict actions
- Authority ceilings from Training Spec are immutable

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Single Delegator** | Each Persona Twin has exactly one delegator |
| **Delegator is Manager** | The delegator is also the accountable manager |
| **Authority Subset** | Twin authority is always ≤ delegator authority |
| **Workbench Scope** | Persona Twin operates within one workbench |
| **Visibility Enforcement** | Private twins visible only to delegator and admin |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Personal productivity** | Collaborators can delegate routine work to AI |
| ✅ **Non-developer friendly** | Blueprint-based creation requires no coding |
| ✅ **Governance consistent** | Same lifecycle, authority, and audit as business agents |
| ✅ **Privacy options** | Private visibility for personal workflows |
| ✅ **Flexible triggers** | Tasks, notifications, and schedules |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ Proliferation of agents | Directory filtering, admin visibility |
| ⚠️ Resource consumption | Fair usage budgets, quotas per twin |
| ⚠️ Authority complexity | Inherits delegator authority, cannot exceed |

---

## Examples

### Example 1: Supervisor's Task Assistant

Jane, a supervisor in Dispute Operations, creates a Persona Twin to handle routine task triage:

```yaml
# Training Spec
apiVersion: seer.olympus.io/v1
kind: TrainingSpec
metadata:
  name: jane-task-assistant
  namespace: acme-disputes
  labels:
    persona-twin: "true"
spec:
  rawAgent:
    name: assistant-raw
    version: "^2.0.0"
  metadata:
    personaTwin:
      delegator: "user:jane.supervisor@acme.com"
      blueprintSource: "collaborator-assistant-base:1.0.0"
  knowledge:
    sources:
      - type: knowledge-base
        ref: dispute-sops-kb
  skills:
    - name: task-triage
      procedure: procedures/task-triage-v1
  prompts:
    system: "You are Jane's personal task assistant. Triage incoming tasks, gather context, and prepare recommendations."
```

### Example 2: Compliance Monitor

Sarah, a compliance officer, creates a twin to monitor high-risk transactions:

```yaml
# Trigger configuration
trigger:
  name: "compliance-monitor"
  type: platform_notification
  target:
    workbench: "compliance-ops"
    scenario: "sarah-compliance-monitor"
  conditions:
    recipient: "user:sarah.compliance@acme.com"
    opaFilter: |
      package persona.twin.compliance
      default allow = false
      allow {
        input.payload.notification.category == "high_risk"
      }
```

### Example 3: Daily Summary Assistant

Alex, a developer, creates a twin for daily summaries:

```yaml
# Kale schedule
trigger:
  name: "alex-daily-summary"
  gateway: kale
  schedule:
    cron: "0 18 * * 1-5"  # 6 PM Mon-Fri
    timezone: "America/New_York"
  target:
    workbench: "dev-ops"
    scenario: "alex-summary-assistant"
```

---

## Promotion

Persona Twins can be promoted to other workbenches:

1. **Promotion Request**: Delegator requests promotion to target workbench
2. **Admin Approval**: Each target workbench requires admin authorization
3. **New Identity**: Twin in target workbench has different identity (same Training Spec)
4. **Same Delegator**: Authority delegation remains with original delegator

A twin can exist in multiple workbenches simultaneously with different Employment Specs.

---

## Implementation Notes

### For Developers

- Persona Twin Blueprint extends standard Trained Agent Blueprint
- Use `persona-twin` label in metadata for recognition
- Directory queries support `personaTwin` filter
- Trigger system supports task assignment signal type

### For Operators

- Monitor Persona Twin proliferation via directories
- Set quotas to manage resource consumption
- Private visibility scenarios visible in admin view
- Standard kill switches apply to Persona Twins

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Agent Lifecycle](./agent-lifecycle.md) | Persona Twins follow standard lifecycle |
| [Authority Enforcement](./authority-enforcement.md) | Authority delegation model |
| [Persona Twin Blueprint](./persona-twin-blueprint.md) | Blueprint for creating twins |
| [Persona](../../../olympus-hub-docs/02-system-design/implementation-concepts/persona.md) | Hub user archetypes |

---

## References

- [Trained Agent Lifecycle Manager](../subsystems/trained-agent-lifecycle-manager/README.md)
- [Agent Lifecycle Manager](../subsystems/agent-lifecycle-manager/README.md)
- [Cipher IAM Extensions: Authority Delegation](../subsystems/cipher-iam-extensions/authority-delegation.md)
- [Kale Scheduler](../../../olympus-hub-docs/04-subsystems/signal-providers/kale-scheduler.md)
