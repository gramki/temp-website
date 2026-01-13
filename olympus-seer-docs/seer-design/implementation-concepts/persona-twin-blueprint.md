# Persona Twin Blueprint

> **Category:** UX Architecture
> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-14

---

## Overview

A **Persona Twin Blueprint** is a Trained Agent Blueprint with additional metadata fields that provide signal suggestions and OPA filter templates for creating Persona Twins. It enables any collaborator (not just developers) to create personal AI agents by selecting from pre-configured options rather than writing specifications from scratch. Persona Twin Blueprints are available in all workbenches as part of the default Hub Platform subscription.

---

## Ontology Context

### Relationship to Ontology

The ontology defines training as the development of KSA (Knowledge, Skills, Abilities) appropriate to an assigned Role. Persona Twin Blueprints extend this by providing collaborator-friendly templates for personal agent training.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Training | Persona Twin Blueprint | Template for personal agent training |
| Role | Delegated Role | Blueprint defines role capabilities |
| (not covered) | Signal Suggestions | Common signals for delegation |
| (not covered) | Filter Suggestions | OPA policies for signal filtering |

### Gap This Fills

Standard Trained Agent Blueprints require developer expertise to configure. Persona Twin Blueprints address:
1. **Accessibility**: Collaborators without developer skills can create agents
2. **Common patterns**: Pre-configured signals and filters for typical delegation scenarios
3. **Rapid setup**: Blueprint-based creation is faster than manual configuration
4. **Best practices**: Suggested configurations encode proven patterns

---

## Definition

**Persona Twin Blueprint** is a Trained Agent Blueprint CRD extended with signal suggestions and OPA filter templates that enable collaborators to create personal AI agents for delegation.

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Platform-level; available in all workbenches via Hub Platform subscription |
| **Lifecycle** | Published by Hub or tenant admins; versioned and immutable once published |
| **Ownership** | Platform team (Hub blueprints) or tenant admins (custom blueprints) |
| **Multiplicity** | Multiple blueprints available; collaborator selects one to create twin |

---

## Rationale

### Why This Design?

Persona Twin Blueprints are designed to:
1. **Extend existing infrastructure**: Built on standard Trained Agent Blueprint, not a new CRD type
2. **Provide suggestions, not constraints**: Signal suggestions are optional starting points
3. **Enable customization**: Collaborators can modify or remove suggested configurations
4. **Support evolution**: New blueprints can be added without platform changes

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| Separate PersonaTwinBlueprint CRD | Unnecessary complexity; extends existing blueprint |
| Hardcoded signal configurations | No flexibility for different use cases |
| Wizard-only creation (no blueprints) | No reusable patterns; slower creation |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0121](../../../olympus-hub-docs/decision-logs/0121-persona-twin-blueprint-structure.md) | Blueprint extends Trained Agent Blueprint with metadata fields |

---

## Structure

### Blueprint Schema Extension

```yaml
apiVersion: seer.olympus.io/v1
kind: TrainingSpec
metadata:
  name: collaborator-assistant-base
  namespace: hub-platform
  labels:
    blueprint-type: "persona-twin"
    hub-managed: "true"
spec:
  # Standard Trained Agent Blueprint fields
  rawAgent:
    name: assistant-raw
    version: "^2.0.0"
  
  knowledge:
    sources:
      - type: knowledge-base
        ref: general-assistant-kb
  
  skills:
    - name: task-analysis
      procedure: procedures/task-analysis-v1
    - name: context-gathering
      procedure: procedures/context-gathering-v1
    - name: recommendation-drafting
      procedure: procedures/recommendation-drafting-v1
  
  prompts:
    system: |
      You are a personal assistant for a collaborator.
      Help them manage tasks, gather information, and prepare recommendations.
      Always respect the delegator's authority boundaries.
    style: professional
    tone: helpful
  
  guardrails:
    - ref: safety/no-unauthorized-actions
    - ref: compliance/data-privacy
  
  # Persona Twin Blueprint specific additions
  personaTwinBlueprint:
    version: "1.0.0"
    displayName: "Collaborator Assistant"
    description: "General-purpose assistant for task management and information gathering"
    
    signalSuggestions:
      - id: task-assigned
        signalType: "task.assigned"
        displayName: "Task Assignments"
        description: "Trigger when tasks are assigned to you"
        defaultEnabled: true
        defaultFilter: |
          package persona.twin.task_filter
          default allow = false
          allow {
            input.payload.task.assignee == input.delegator_id
          }
      
      - id: platform-notification
        signalType: "platform.notification"
        displayName: "Platform Notifications"
        description: "Trigger on platform notifications for you"
        defaultEnabled: false
        defaultFilter: |
          package persona.twin.notification_filter
          default allow = false
          allow {
            input.payload.recipient == input.delegator_id
            input.payload.scope == "workbench"
          }
      
      - id: request-update
        signalType: "request.update"
        displayName: "Request Updates"
        description: "Trigger when requests you're assigned to are updated"
        defaultEnabled: false
        defaultFilter: |
          package persona.twin.request_filter
          default allow = false
          allow {
            input.payload.request.tasks[_].assignee == input.delegator_id
          }
    
    filterSuggestions:
      - id: high-priority-only
        name: "High Priority Only"
        description: "Only trigger on high or critical priority items"
        applicableTo: ["task-assigned", "request-update"]
        policy: |
          package persona.twin.priority_filter
          default allow = false
          allow {
            input.payload.priority == "high"
          }
          allow {
            input.payload.priority == "critical"
          }
      
      - id: business-hours-only
        name: "Business Hours Only"
        description: "Only trigger during business hours (9 AM - 5 PM)"
        applicableTo: ["task-assigned", "platform-notification", "request-update"]
        policy: |
          package persona.twin.business_hours
          default allow = false
          allow {
            hour := time.clock(input.timestamp)[0]
            hour >= 9
            hour < 17
          }
      
      - id: exclude-routine
        name: "Exclude Routine Tasks"
        description: "Skip routine and low-priority tasks"
        applicableTo: ["task-assigned"]
        policy: |
          package persona.twin.exclude_routine
          default allow = true
          allow = false {
            input.payload.task.priority == "low"
            input.payload.task.category == "routine"
          }
    
    scheduleSuggestions:
      - id: daily-summary
        name: "Daily Summary"
        description: "Generate a daily summary at end of day"
        defaultCron: "0 17 * * 1-5"
        defaultTimezone: "America/New_York"
      
      - id: weekly-review
        name: "Weekly Review"
        description: "Prepare a weekly review on Friday afternoon"
        defaultCron: "0 15 * * 5"
        defaultTimezone: "America/New_York"
      
      - id: morning-briefing
        name: "Morning Briefing"
        description: "Prepare a morning briefing before work starts"
        defaultCron: "0 8 * * 1-5"
        defaultTimezone: "America/New_York"
```

### Signal Suggestion Structure

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier for the signal suggestion |
| `signalType` | string | Signal type to subscribe to |
| `displayName` | string | Human-readable name for UI |
| `description` | string | Explanation for collaborators |
| `defaultEnabled` | boolean | Whether enabled by default |
| `defaultFilter` | string | Default OPA policy for filtering |

### Filter Suggestion Structure

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier |
| `name` | string | Human-readable name |
| `description` | string | Explanation for collaborators |
| `applicableTo` | array | Signal suggestion IDs this applies to |
| `policy` | string | OPA policy content |

### Schedule Suggestion Structure

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier |
| `name` | string | Human-readable name |
| `description` | string | Explanation for collaborators |
| `defaultCron` | string | Default cron expression |
| `defaultTimezone` | string | Default timezone |

---

## Behavior

### How It Works

```
1. Collaborator browses available Persona Twin Blueprints
   └── Marketplace-style discovery within Workbench Studio

2. Collaborator selects a blueprint
   └── Blueprint provides starting configuration

3. Collaborator configures signals
   ├── Reviews signal suggestions (enabled/disabled)
   ├── Applies filter suggestions (optional)
   └── Configures schedules (optional)

4. Collaborator customizes training
   ├── Modifies prompts and behavior
   ├── Adds knowledge sources
   └── Configures guardrails

5. System creates Training Spec
   ├── Based on blueprint
   ├── With collaborator's customizations
   └── Labeled as persona-twin

6. Collaborator trains and deploys
   └── Standard agent lifecycle continues
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Training Spec Manager | → | Blueprint used to create Training Spec |
| Workbench Studio | ← | Blueprint discovery and selection |
| Marketplace | ← | Blueprint subscription (if external) |
| Trigger Definitions | → | Signal suggestions become triggers |

---

## Common Signals

### Task Assignment Signal

Triggered when a task is assigned to the delegator:

```yaml
signalType: "task.assigned"
payload:
  task:
    id: string
    assignee: string
    priority: string
    category: string
    due_date: datetime
    context: object
```

### Platform Notification Signal

Triggered when a platform notification is sent to the delegator:

```yaml
signalType: "platform.notification"
payload:
  notification:
    id: string
    recipient: string
    scope: "workbench" | "subscription" | "platform"
    category: string
    message: string
    metadata: object
```

### Request Update Signal

Triggered when a request the delegator is assigned to is updated:

```yaml
signalType: "request.update"
payload:
  request:
    id: string
    status: string
    tasks:
      - id: string
        assignee: string
        status: string
    update_type: string
    update_data: object
```

---

## Hub-Provided Blueprints

The Hub Platform subscription includes these Persona Twin Blueprints:

| Blueprint | Description | Primary Use Case |
|-----------|-------------|------------------|
| **Collaborator Assistant** | General-purpose task management | Personal productivity |
| **Compliance Monitor** | Regulatory and compliance alerts | Compliance officers |
| **Knowledge Assistant** | Knowledge capture and organization | Knowledge workers |
| **Review Coordinator** | Meeting prep and review support | Managers, supervisors |
| **On-Call Assistant** | Off-hours monitoring and triage | Developers, operators |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Extends Trained Agent Blueprint** | Must include all standard Training Spec fields |
| **Signal suggestions optional** | Collaborator can disable any suggestion |
| **Filter policies valid OPA** | All policy content must be valid Rego |
| **Immutable once published** | Published blueprint versions cannot change |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Accessible** | Any collaborator can create agents |
| ✅ **Rapid setup** | Pre-configured patterns accelerate creation |
| ✅ **Best practices** | Suggested configurations encode proven patterns |
| ✅ **Customizable** | Suggestions can be modified or removed |
| ✅ **Extensible** | New blueprints can be added over time |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ Limited flexibility vs. manual | Suggestions are starting points, not limits |
| ⚠️ Blueprint maintenance | Version management, deprecation support |
| ⚠️ Signal compatibility | Suggestions must match available signals |

---

## Examples

### Example 1: Task Triage Blueprint

Blueprint for supervisors who need help triaging incoming tasks:

```yaml
apiVersion: seer.olympus.io/v1
kind: TrainingSpec
metadata:
  name: task-triage-assistant
  namespace: hub-platform
  labels:
    blueprint-type: "persona-twin"
spec:
  rawAgent:
    name: triage-raw
    version: "^2.0.0"
  
  skills:
    - name: task-triage
      procedure: procedures/task-triage-v1
    - name: priority-assessment
      procedure: procedures/priority-assessment-v1
  
  prompts:
    system: |
      You are a task triage assistant. Review incoming tasks,
      assess priority, gather context, and prepare recommendations.
  
  personaTwinBlueprint:
    version: "1.0.0"
    displayName: "Task Triage Assistant"
    description: "Help supervisors triage and prioritize tasks"
    
    signalSuggestions:
      - id: task-assigned
        signalType: "task.assigned"
        displayName: "All Assigned Tasks"
        description: "Trigger on all task assignments"
        defaultEnabled: true
        defaultFilter: |
          package persona.twin.all_tasks
          default allow = false
          allow {
            input.payload.task.assignee == input.delegator_id
          }
    
    filterSuggestions:
      - id: high-volume-filter
        name: "High Volume Filter"
        description: "Skip tasks from high-volume scenarios"
        applicableTo: ["task-assigned"]
        policy: |
          package persona.twin.high_volume
          default allow = true
          allow = false {
            input.payload.task.scenario_id == "bulk-processing"
          }
```

### Example 2: Compliance Monitor Blueprint

Blueprint for compliance officers monitoring high-risk activities:

```yaml
apiVersion: seer.olympus.io/v1
kind: TrainingSpec
metadata:
  name: compliance-monitor-assistant
  namespace: hub-platform
  labels:
    blueprint-type: "persona-twin"
spec:
  rawAgent:
    name: monitor-raw
    version: "^2.0.0"
  
  knowledge:
    sources:
      - type: knowledge-base
        ref: compliance-regulations-kb
  
  skills:
    - name: risk-assessment
      procedure: procedures/risk-assessment-v1
    - name: compliance-check
      procedure: procedures/compliance-check-v1
  
  prompts:
    system: |
      You are a compliance monitoring assistant. Watch for high-risk
      activities, flag violations, and prepare compliance reports.
  
  guardrails:
    - ref: compliance/regulatory-disclosure
    - ref: safety/no-false-positives
  
  personaTwinBlueprint:
    version: "1.0.0"
    displayName: "Compliance Monitor"
    description: "Monitor activities for compliance violations"
    
    signalSuggestions:
      - id: high-risk-notification
        signalType: "platform.notification"
        displayName: "High-Risk Alerts"
        description: "Trigger on high-risk activity notifications"
        defaultEnabled: true
        defaultFilter: |
          package persona.twin.high_risk
          default allow = false
          allow {
            input.payload.notification.category == "high_risk"
            input.payload.recipient == input.delegator_id
          }
    
    scheduleSuggestions:
      - id: compliance-report
        name: "Daily Compliance Report"
        description: "Generate daily compliance summary"
        defaultCron: "0 9 * * 1-5"
        defaultTimezone: "America/New_York"
```

---

## Implementation Notes

### For Developers

- Blueprint CRD extends standard TrainingSpec with `personaTwinBlueprint` field
- Signal suggestions generate corresponding trigger configurations
- Filter policies must be valid Rego and will be validated at Training Spec creation
- `input.delegator_id` is injected by the system in all filter evaluations

### For Operators

- Hub-provided blueprints are managed by Platform team
- Custom blueprints can be created by tenant admins
- Blueprint versioning follows semantic versioning
- Deprecated blueprints should be marked and eventually removed

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Persona Twins](./persona-twins.md) | Agents created from blueprints |
| [Agent Lifecycle](./agent-lifecycle.md) | Blueprints create Training Specs |
| [Trained Agent Blueprint](./agent-lifecycle.md#trained-agent-blueprints) | Base concept extended |
| [Blueprint](../../../olympus-hub-docs/02-system-design/implementation-concepts/blueprint.md) | Hub blueprint pattern |

---

## References

- [Training Spec Manager](../subsystems/trained-agent-lifecycle-manager/training-spec-manager.md)
- [Trained Agent Directory](../subsystems/trained-agent-lifecycle-manager/trained-agent-directory.md)
- [Trigger Definitions](../../../olympus-hub-docs/04-subsystems/workbench-management/trigger-definitions.md)
- [Kale Scheduler](../../../olympus-hub-docs/04-subsystems/signal-providers/kale-scheduler.md)
