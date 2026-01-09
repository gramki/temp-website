# Scenario Definitions

> **Status:** 🔴 Stub — Placeholder for expansion

Defines how Scenarios are configured within Workbenches.

---

## Overview

A **Scenario** represents a situational context that determines:
- Which Hub Application handles the Request
- Which Roles are involved in responding
- What Goals must be achieved
- Which SOPs govern the response

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
  tags: array
  status: enum  # active | deprecated
```

---

## Scenario Examples

| Scenario | Application Type | Automation Runtime |
|----------|------------------|-------------------|
| Suspicious Login Attempt | Workflow App | Rhea |
| Payment Dispute Filed | Seer Case Orchestration Agent | Seer |
| Daily Settlement Processing | File App | Perseus |
| High-Value Payment Review | Procedure App | Atlantis |

---

## Related Documentation

- [Workbench Management Overview](./README.md)
- [Trigger Definitions](./trigger-definitions.md)
- [Application Configuration](./application-configuration.md)

---

*TODO: Detailed design — role assignment, goal tracking, SOP linking*

