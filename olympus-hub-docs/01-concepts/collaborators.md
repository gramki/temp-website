# Collaborators

> **Category:** Platform Concept

---

## Overview

**Collaborators** are all Hub Personas who work within or around a Workbench to configure, operate, or administer Hub capabilities. This collective term distinguishes Hub Personas (who use Hub as a platform) from Business Domain Actors (whose activities generate Requests but don't necessarily use Hub to process them).

---

## Definition

**Collaborators** are all Hub Personas who work within or around a Workbench to configure, operate, or administer Hub capabilities. This includes:

- **Workbench Operations**: Agents, Supervisors
- **Workbench Designers**: Process Architects, Developers, Automation Product Owners (APO)
- **Tenant Administration**: Administrators, Auditors

Collaborators are distinguished from **Business Domain Actors** (Business Customers, Business Employees, Business System Actors) whose activities generate Requests but who don't necessarily use Hub as a platform to process them.

---

## Scope

### Workbench Collaborators

All Hub Personas working within a specific workbench context:

- **Agents** — Complete tasks, process requests
- **Supervisors** — Manage queues, oversee operations
- **Process Architects** — Design scenarios and knowledge (when working on this workbench)
- **Developers** — Build applications for this workbench
- **APOs** — Own automation outcomes for this workbench
- **Administrators** — Configure workbench resources
- **Auditors** — Review workbench compliance

### Tenant Collaborators

All Hub Personas within a tenant subscription (broader scope):

- All workbench collaborators across all workbenches
- Tenant-level Administrators and Auditors
- Process Architects, Developers, and APOs working across multiple workbenches

---

## Distinction from Business Domain Actors

| Category | Purpose | Examples |
|----------|---------|----------|
| **Collaborators** | Use Hub as a platform to configure, operate, or administer | Agent processing tasks, Supervisor managing queues, Process Architect designing scenarios |
| **Business Domain Actors** | Generate Requests through business activities | Customer filing dispute, Employee initiating onboarding, System emitting events |

### Key Distinction

- **Collaborators** = Use Hub to *process* Requests
- **Business Domain Actors** = *Generate* Requests

### Overlap

A person can be both:
- **Business Employee** (as Business Actor) when triggering a request
- **Agent** (as Collaborator) when processing tasks

The distinction is based on *what they're doing*, not *who they are*.

---

## Relationship to Personas

Collaborators encompass all Hub Personas:

```
Collaborators
├── Workbench Operations
│   ├── Agent
│   └── Supervisor
├── Workbench Designers
│   ├── Automation Product Owner (APO)
│   ├── Process Architect
│   └── Developer
└── Tenant Administration
    ├── Administrator
    └── Auditor
```

**Excluded:**
- Hub System personas (SRE, Customer Success) — operate at platform level, not workbench level
- Business Domain Actors (Business Customer, Business Employee, Business System Actor)

---

## Usage Context

Use "collaborators" when:
- Referring collectively to Hub Personas working in a workbench context
- Describing workbench-scoped features accessible to multiple personas
- Discussing collaboration patterns within workbenches
- Specifying permissions or access controls for Hub Personas

Use specific persona names when:
- Specificity is required for clarity
- Describing persona-specific responsibilities or capabilities
- Documenting persona-specific workflows

---

## Related Concepts

- [Personas](../08-personas-and-journeys/README.md) — Individual user archetypes
- [Workbench](./ontology-1-perception-layer.md#workbench) — Operational environment where collaborators work
- [Business Domain Actors](../08-personas-and-journeys/README.md#business-domain-actors) — Request originators

---

## See Also

- [Personas and Journeys](../08-personas-and-journeys/README.md)
- [User Management](../04-subsystems/user-management/README.md)
- [ADR-0114: Collaborators Terminology](../decision-logs/0114-collaborators-terminology.md)
