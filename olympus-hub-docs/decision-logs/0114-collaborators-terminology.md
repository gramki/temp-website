# ADR-0114: Collaborators Terminology

> **Status:** Accepted  
> **Date:** 2026-01-13  
> **Category:** terminology

---

## Context

Olympus Hub documentation needed a collective term to refer to all Hub Personas who work within or around a Workbench to configure, operate, or administer Hub capabilities. The documentation frequently refers to "agents, supervisors, developers, architects, administrators, auditors" collectively, but lacked a concise, consistent term.

Additionally, there was a need to clearly distinguish Hub Personas (who use Hub as a platform) from Business Domain Actors (Business Customers, Business Employees, Business System Actors) whose activities generate Requests but don't necessarily use Hub to process them.

---

## Decision

Introduce **"Collaborators"** as the collective term for all Hub Personas working in a workbench context.

### Definition

**Collaborators** are all Hub Personas who work within or around a Workbench to configure, operate, or administer Hub capabilities. This includes:

- **Workbench Operations**: Agents, Supervisors
- **Workbench Designers**: Process Architects, Developers, Automation Product Owners (APO)
- **Tenant Administration**: Administrators, Auditors

Collaborators are distinguished from **Business Domain Actors** (Business Customers, Business Employees, Business System Actors) whose activities generate Requests but who don't necessarily use Hub as a platform to process them.

### Scope

- **Workbench Collaborators**: All Hub Personas working within a specific workbench context
- **Tenant Collaborators**: All Hub Personas within a tenant subscription (broader scope)
- When scope is unclear, prefer "workbench collaborators" for workbench-scoped features

### Exclusions

- **Hub System personas** (SRE, Customer Success) — operate at platform level, not workbench level
- **Business Domain Actors** — generate Requests but don't use Hub as a platform

---

## Rationale

### Why "Collaborators"?

| Aspect | Rationale |
|--------|-----------|
| **Meaning** | Emphasizes the collaborative nature of Hub Personas working together in workbenches |
| **Distinction** | Clearly separates Hub Personas (collaborators) from Business Domain Actors (request originators) |
| **Context** | Workbench-scoped term that reflects the operational environment |
| **Clarity** | More concise than listing all personas repeatedly |

### Why Not Other Terms?

| Alternative | Why Rejected |
|-------------|--------------|
| **Users** | Too generic; includes Business Domain Actors and customers |
| **Personas** | Already used for individual archetypes; would be confusing |
| **Operators** | Implies only operational roles, excludes designers and administrators |
| **Team Members** | Too informal; doesn't capture the platform-user relationship |
| **Workbench Users** | Ambiguous; could include Business Domain Actors who interact with workbenches |

---

## Consequences

### Positive

1. **Consistency** — Single term for collective references to Hub Personas
2. **Clarity** — Clear distinction from Business Domain Actors
3. **Conciseness** — Shorter than listing all personas
4. **Context** — Workbench-scoped term aligns with operational reality

### Negative

1. **Documentation Updates** — Need to update existing references throughout documentation
2. **Learning Curve** — New term to learn and understand
3. **Potential Ambiguity** — Must clarify scope (workbench vs tenant) when needed

### Neutral

1. **Overlap Handling** — Business Employees can be both (as Business Actor when triggering requests, as Collaborator when acting as Agent) — this distinction is already handled in persona overlap concept

---

## Usage Guidelines

### Use "Collaborators" When:

- Referring collectively to Hub Personas working in a workbench context
- Describing workbench-scoped features accessible to multiple personas
- Discussing collaboration patterns within workbenches
- Specifying permissions or access controls for Hub Personas

### Use Specific Persona Names When:

- Specificity is required for clarity
- Describing persona-specific responsibilities or capabilities
- Documenting persona-specific workflows

### Do NOT Use "Collaborators" When:

- Referring to Business Domain Actors
- Referring to Hub System personas (SRE, Customer Success) in platform-level context
- Specificity is more important than collective reference

---

## Alternatives Considered

### 1. Keep Existing Approach (No Collective Term)

Continue using lists like "agents, supervisors, developers, architects, administrators, auditors" when referring collectively.

**Rejected because:**
- Verbose and repetitive
- Inconsistent across documentation
- No clear distinction from Business Domain Actors

### 2. Use "Hub Users"

Use "Hub Users" as the collective term.

**Rejected because:**
- Too generic; could include Business Domain Actors
- Doesn't emphasize collaboration aspect
- "Users" is less descriptive than "Collaborators"

### 3. Use "Workbench Team"

Use "Workbench Team" as the collective term.

**Rejected because:**
- Too informal for technical documentation
- "Team" implies organizational structure rather than platform-user relationship
- Less precise than "Collaborators"

---

## Related Documentation

- [Collaborators Concept](../01-concepts/collaborators.md) — Detailed definition and scope
- [Personas and Journeys](../08-personas-and-journeys/README.md) — Hub Personas overview
- [User Management](../04-subsystems/user-management/README.md) — User scope hierarchy
