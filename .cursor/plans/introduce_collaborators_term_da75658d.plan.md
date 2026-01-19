---
name: Introduce Collaborators Term
overview: Introduce the term "collaborators" to collectively refer to all Hub Personas working in a workbench context (excluding business domain actors), document it in concepts and personas, create a decision log, and apply it throughout Hub and Seer design documentation where appropriate.
todos:
  - id: "1"
    content: Add Collaborators concept definition to ontology-reference.md or create new collaborators.md file
    status: completed
  - id: "2"
    content: Update personas README to introduce and document collaborators term
    status: completed
    dependencies:
      - "1"
  - id: "3"
    content: Update user-management README to include collaborators in user scope hierarchy
    status: in_progress
    dependencies:
      - "1"
  - id: "4"
    content: Create decision log ADR-0114 for collaborators terminology
    status: pending
    dependencies:
      - "1"
  - id: "5"
    content: Apply collaborators term in notification-services README (replace collective persona references)
    status: pending
    dependencies:
      - "4"
  - id: "6"
    content: Apply collaborators term in workbench-users and tenant-subscription-users docs
    status: pending
    dependencies:
      - "4"
  - id: "7"
    content: Update persona.md implementation concept to include collaborators distinction
    status: pending
    dependencies:
      - "4"
  - id: "8"
    content: Update ontology-1-perception-layer.md Workbench section to mention collaborators
    status: pending
    dependencies:
      - "4"
  - id: "9"
    content: Apply collaborators term in Seer UX architecture docs (seer-and-hub-ux-integration.md, README.md)
    status: pending
    dependencies:
      - "4"
  - id: "10"
    content: Review and identify additional usage opportunities in Hub and Seer docs (mark for review, not auto-apply)
    status: pending
    dependencies:
      - "4"
---

# Introduce "Collaborators" Term in Hub and Seer Documentation

## Overview

Introduce "collaborators" as a collective term for all Hub Personas who work within or around a Workbench to configure, operate, or administer Hub capabilities. This excludes Business Domain Actors (Customers, Employees, System Actors) whose activities generate Requests but don't use Hub as a platform.

## Implementation Plan

### 1. Add Concept Definition

**File:** `olympus-hub-docs/01-concepts/ontology-reference.md` or new file `olympus-hub-docs/01-concepts/collaborators.md`

- Add definition of "Collaborators" in the concepts layer
- Clarify distinction from Business Domain Actors
- Include scope (workbench vs tenant-level)
- Reference relationship to Personas

**Location in ontology-reference.md:** Add new section after Personas or in a "Platform Concepts" section

### 2. Document in Personas Section

**File:** `olympus-hub-docs/08-personas-and-journeys/README.md`

- Add "Collaborators" as a key concept in the overview
- Update the Hub Personas section to introduce the term
- Add a table or section explaining who are collaborators vs business domain actors
- Update the visual summary to include collaborators grouping

**File:** `olympus-hub-docs/04-subsystems/user-management/README.md`

- Add collaborators definition in the overview
- Update user scope hierarchy diagram to show collaborators grouping
- Clarify that collaborators = Hub Personas (excluding business domain actors)

### 3. Create Decision Log

**File:** `olympus-hub-docs/decision-logs/0114-collaborators-terminology.md`

- Document the decision to introduce "collaborators" term
- Explain rationale (need for collective term, distinction from business actors)
- Define scope and boundaries
- List included/excluded personas
- Document consequences and alternatives considered

### 4. Apply Term in Hub Documentation (Where Certain)

**Files to update:**

1. **`olympus-hub-docs/04-subsystems/notification-services/README.md`**

- Replace "agents, business users, supervisors, tenant admins" with "collaborators" where referring to Hub Personas collectively
- Keep "business users" separate when referring to Business Domain Actors

2. **`olympus-hub-docs/04-subsystems/user-management/workbench-users.md`**

- Add note about collaborators in overview
- Update related documentation section to reference collaborators concept

3. **`olympus-hub-docs/04-subsystems/user-management/tenant-subscription-users.md`**

- Add note about collaborators in overview
- Clarify that tenant subscription users are part of collaborators

4. **`olympus-hub-docs/02-system-design/implementation-concepts/persona.md`**

- Add section on Collaborators vs Business Domain Actors
- Update persona definitions table if needed

5. **`olympus-hub-docs/01-concepts/ontology-1-perception-layer.md`**

- Update Workbench section to mention collaborators
- Add note about who collaborates within workbench context

### 5. Apply Term in Seer Design Documentation (Where Certain)

**Files to update:**

1. **`olympus-seer-docs/seer-design/ux-architecture/seer-and-hub-ux-integration.md`**

- Replace references to "all stakeholders" or "all personas" with "collaborators" where appropriate
- Clarify that collaborators work within Workbench scope

2. **`olympus-seer-docs/seer-design/ux-architecture/README.md`**

- Add note about collaborators in overview
- Update persona-focused section to reference collaborators

3. **`olympus-seer-docs/seer-design/hub-integration/README.md`**

- Add section on collaborators if it discusses Hub Personas
- Clarify collaboration patterns

### 6. Identify Additional Usage Opportunities (For Review)

**Files to review for potential usage:**

1. **`olympus-hub-docs/04-subsystems/platform-notifications/README.md`** - Check if "all personas" references should be "collaborators"

2. **`olympus-hub-docs/06-ux-architecture/tenant-domain/marketplace-console.md`** - Check if "accessible from Agent Developer Desk, Scenario Design Desk..." should reference collaborators

3. **`olympus-hub-docs/04-subsystems/ms-teams-integration/README.md`** - Check if workbench user references could use collaborators

4. **`olympus-hub-docs/02-system-design/workbench-anatomy.md`** - Add collaborators to workbench contents/identity sections

5. **`olympus-seer-docs/seer-design/guides/agent-development-lifecycle.md`** - Check for opportunities to use collaborators term

6. **`olympus-seer-docs/seer-design/implementation-concepts/agent-observability.md`** - Check if persona visibility discussions should reference collaborators

## Definition to Use

> **Collaborators** are all Hub Personas who work within or around a Workbench to configure, operate, or administer Hub capabilities. This includes:
> - **Workbench Operations**: Agents, Supervisors
> - **Workbench Designers**: Process Architects, Developers, Automation Product Owners (APO)
> - **Tenant Administration**: Administrators, Auditors
>
> Collaborators are distinguished from **Business Domain Actors** (Business Customers, Business Employees, Business System Actors) whose activities generate Requests but who don't necessarily use Hub as a platform to process them.

## Scope Clarification

- **Workbench Collaborators**: All Hub Personas working within a specific workbench context
- **Tenant Collaborators**: All Hub Personas within a tenant subscription (broader scope)
- When scope is unclear, prefer "workbench collaborators" for workbench-scoped features

## Notes

- Do NOT replace individual persona names when specificity is needed
- Do NOT use "collaborators" when referring to Business Domain Actors
- Maintain distinction: Business Employees can be both (as Business Actor when triggering requests, as Collaborator when acting as Agent)
- Use consistently but not excessively - prefer specificity when persona-level detail is important