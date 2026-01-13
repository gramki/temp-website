# Scenario Definitions

> **Status:** 🟡 In Progress
> **Last Updated:** 2026-01-14

Defines how Scenarios are configured within Workbenches.

---

## Overview

A **Scenario** represents a situational context that determines:
- Which Hub Application handles the Request
- Which Roles are involved in responding
- What Goals must be achieved
- Which SOPs govern the response

Scenarios are categorized as either **Business Scenarios** (organizational workflows) or **Persona Twin Scenarios** (personal delegation agents).

---

## Scenario Schema

```yaml
scenario:
  id: string
  name: string
  workbench_id: string
  
  # Description
  description: string
  
  # Application binding
  application:
    automation_system: enum  # atlantis | perseus | rhea | chronoshift | seer
    application_id: string
    application_type: string  # File App, Workflow App, etc.
  
  # Roles involved
  roles:
    - role_id: string
      responsibilities: array
  
  # Goals
  goals:
    - goal_id: string
      description: string
      sla: object
  
  # SOPs
  sops:
    - sop_id: string
      knowledge_base_id: string
  
  # Metadata
  metadata:
    labels:
      persona-twin: string  # "true" | undefined
    category: enum  # business | persona-twin
    visibility: enum  # public | private
    delegator: string  # For Persona Twin scenarios: user reference
  tags: array
  status: enum  # active | deprecated
```

---

## Scenario Categories

### Business Scenarios

Standard organizational workflows that handle business operations:

```yaml
scenario:
  id: "sc-dispute-resolution"
  name: "Dispute Resolution"
  workbench_id: "wb-disputes"
  metadata:
    category: "business"
    visibility: "public"
  application:
    automation_system: seer
    application_id: "dispute-resolution-agent"
```

### Persona Twin Scenarios

Personal delegation scenarios created by collaborators:

```yaml
scenario:
  id: "sc-john-smith-assistant"
  name: "John's Task Assistant"
  workbench_id: "wb-disputes"
  metadata:
    labels:
      persona-twin: "true"
    category: "persona-twin"
    visibility: "private"
    delegator: "user:john.smith@acme.com"
  application:
    automation_system: seer
    application_id: "john-smith-assistant"
```

---

## Visibility Controls

Scenarios support visibility settings that control who can see them:

| Visibility | Description | Access |
|------------|-------------|--------|
| **public** | Visible to all workbench members | All collaborators can see |
| **private** | Visible only to creator and admins | Delegator + admins only |

### Private Visibility for Persona Twins

Persona Twin Scenarios can be set to `private` visibility:

- **Creator/Delegator**: Always has full access
- **Workbench Admins**: Can see all scenarios (for governance)
- **Other Collaborators**: Cannot see private scenarios

```yaml
scenario:
  metadata:
    category: "persona-twin"
    visibility: "private"
    delegator: "user:john.smith@acme.com"
```

### Visibility Enforcement

Visibility is enforced at the API level:

```yaml
# API Query: List scenarios
GET /workbenches/{workbench_id}/scenarios

# Filters
?category=business           # Only business scenarios
?category=persona-twin       # Only Persona Twin scenarios
?visibility=public           # Only public scenarios
?visibility=private          # Only private scenarios (requires admin)
?delegator=user:john@acme.com # Only scenarios for delegator

# Default behavior: Include all visible scenarios
# - All public scenarios
# - Private scenarios where user is delegator or admin
```

---

## Persona Twin Scenario Schema

Extended schema for Persona Twin Scenarios:

```yaml
personaTwinScenario:
  id: string
  name: string
  workbench_id: string
  
  # Description
  description: string
  
  # Required Persona Twin metadata
  metadata:
    labels:
      persona-twin: "true"
    category: "persona-twin"
    visibility: enum  # public | private (typically private)
    delegator: string  # Required: user reference
  
  # Application binding (Seer agent)
  application:
    automation_system: seer
    application_id: string  # Reference to Employed Agent
  
  # Triggers (Persona Twin specific)
  triggers:
    - type: task_assignment
      conditions:
        assignee: string  # Must match delegator
        opaFilter: string  # Optional OPA filter policy
    - type: platform_notification
      conditions:
        recipient: string  # Must match delegator
        scope: workbench
    - type: time_schedule
      gateway: kale
      schedule:
        cron: string
        timezone: string
  
  # Standard fields
  tags: array
  status: enum
```

---

## Scenario Isolation

Persona Twin Scenarios are isolated from Business Scenarios:

### UI Isolation

```
Workbench Studio → Scenarios
├── Business Scenarios (default view)
│   ├── Dispute Resolution
│   ├── Payment Processing
│   └── Customer Inquiry
└── Persona Twins (separate section)
    ├── My Twins (current user's twins)
    │   ├── John's Task Assistant
    │   └── John's Daily Summary
    └── All Twins (admin view, respects visibility)
```

### API Isolation

```yaml
# List Business Scenarios only
GET /workbenches/{workbench_id}/scenarios?category=business

# List Persona Twin Scenarios only
GET /workbenches/{workbench_id}/scenarios?category=persona-twin

# List My Persona Twins
GET /workbenches/{workbench_id}/scenarios?category=persona-twin&delegator={current_user}
```

---

## Scenario Examples

| Scenario | Category | Application Type | Automation Runtime |
|----------|----------|------------------|-------------------|
| Suspicious Login Attempt | Business | Workflow App | Rhea |
| Payment Dispute Filed | Business | Seer Case Orchestration Agent | Seer |
| Daily Settlement Processing | Business | File App | Perseus |
| High-Value Payment Review | Business | Procedure App | Atlantis |
| John's Task Assistant | Persona Twin | Seer Persona Twin Agent | Seer |
| Sarah's Compliance Monitor | Persona Twin | Seer Persona Twin Agent | Seer |

---

## Related Documentation

- [Workbench Management Overview](./README.md)
- [Trigger Definitions](./trigger-definitions.md)
- [Application Configuration](./application-configuration.md)
- [Persona Twins](../../../olympus-seer-docs/seer-design/implementation-concepts/persona-twins.md) — Persona Twin concept documentation

---

*Scenario Definitions describe how scenarios are configured, including support for Persona Twin Scenarios with category isolation, visibility controls, and specialized triggers.*
