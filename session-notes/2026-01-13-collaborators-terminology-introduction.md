# Session Notes: Collaborators Terminology Introduction

**Date**: 2026-01-13  
**Focus**: Introduce "collaborators" as a collective term for all Hub Personas working in workbench context, excluding Business Domain Actors

---

## Objective

Introduce "collaborators" as a standardized collective term to refer to all Hub Personas who work within or around a Workbench to configure, operate, or administer Hub capabilities. This term distinguishes Hub Personas (who use Hub as a platform) from Business Domain Actors (whose activities generate Requests but don't use Hub to process them).

---

## Work Completed

### Phase 1: Concept Definition

**Created new concept document:**
- `olympus-hub-docs/01-concepts/collaborators.md` — Comprehensive definition of Collaborators concept including:
  - Definition and scope (Workbench vs Tenant level)
  - Distinction from Business Domain Actors
  - Relationship to Personas
  - Usage guidelines
  - Related concepts and cross-references

**Updated ontology reference:**
- Added Collaborators to document index in `ontology-reference.md`

### Phase 2: Personas Documentation

**Updated personas README:**
- Added Collaborators section explaining the collective term
- Updated Hub Personas section with note about collaborators
- Updated visual summary to show collaborators grouping
- Added cross-references to Collaborators concept

**Updated user management documentation:**
- `user-management/README.md` — Added collaborators definition, updated user scope hierarchy diagram
- `workbench-users.md` — Added note about collaborators
- `tenant-subscription-users.md` — Added note about collaborators

### Phase 3: Decision Log

**Created ADR:**
- `decision-logs/0114-collaborators-terminology.md` — Complete ADR documenting:
  - Context and rationale
  - Definition and scope
  - Alternatives considered
  - Usage guidelines
  - Consequences

**Updated decision log index:**
- Added ADR-0114 to decision log README

### Phase 4: Applied Term in Hub Documentation

**Updated implementation concepts:**
- `persona.md` — Added "Collaborators vs Business Domain Actors" section
- `ontology-1-perception-layer.md` — Added collaborators note in Workbench section

**Updated subsystem documentation:**
- `notification-services/README.md` — Updated to use "collaborators" term, fixed ASCII diagram formatting

### Phase 5: Applied Term in Seer Design Documentation

**Updated Seer UX architecture:**
- `seer-design/ux-architecture/seer-and-hub-ux-integration.md` — Updated stakeholders reference
- `seer-design/ux-architecture/README.md` — Added collaborators note in overview

---

## Artifacts Created

| File | Description | Status |
|------|-------------|--------|
| `olympus-hub-docs/01-concepts/collaborators.md` | Complete Collaborators concept definition | ✅ Complete |
| `olympus-hub-docs/decision-logs/0114-collaborators-terminology.md` | ADR documenting terminology decision | ✅ Complete |

---

## Files Updated

| File | Changes | Status |
|------|---------|--------|
| `olympus-hub-docs/01-concepts/ontology-reference.md` | Added Collaborators to document index | ✅ Complete |
| `olympus-hub-docs/08-personas-and-journeys/README.md` | Added Collaborators section, updated Hub Personas section | ✅ Complete |
| `olympus-hub-docs/04-subsystems/user-management/README.md` | Added collaborators definition, updated hierarchy diagram | ✅ Complete |
| `olympus-hub-docs/04-subsystems/user-management/workbench-users.md` | Added collaborators note | ✅ Complete |
| `olympus-hub-docs/04-subsystems/user-management/tenant-subscription-users.md` | Added collaborators note | ✅ Complete |
| `olympus-hub-docs/02-system-design/implementation-concepts/persona.md` | Added Collaborators vs Business Domain Actors section | ✅ Complete |
| `olympus-hub-docs/01-concepts/ontology-1-perception-layer.md` | Added collaborators note in Workbench section | ✅ Complete |
| `olympus-hub-docs/04-subsystems/notification-services/README.md` | Updated to use collaborators term, fixed diagram | ✅ Complete |
| `olympus-hub-docs/decision-logs/README.md` | Added ADR-0114 to index | ✅ Complete |
| `olympus-seer-docs/seer-design/ux-architecture/seer-and-hub-ux-integration.md` | Updated stakeholders reference | ✅ Complete |
| `olympus-seer-docs/seer-design/ux-architecture/README.md` | Added collaborators note | ✅ Complete |

---

## Key Decisions Made

1. **Term Selection**: Chose "Collaborators" over alternatives (Users, Personas, Operators, Team Members, Workbench Users) for clarity and emphasis on collaborative nature
2. **Scope Definition**: Established two scopes:
   - **Workbench Collaborators**: All Hub Personas within a specific workbench
   - **Tenant Collaborators**: All Hub Personas within a tenant subscription
3. **Exclusions**: Clearly defined that Hub System personas (SRE, Customer Success) and Business Domain Actors are excluded
4. **Usage Guidelines**: Documented when to use "collaborators" vs specific persona names

**ADR Created**: [ADR-0114: Collaborators Terminology](../olympus-hub-docs/decision-logs/0114-collaborators-terminology.md)

---

## Definition Established

**Collaborators** are all Hub Personas who work within or around a Workbench to configure, operate, or administer Hub capabilities. This includes:

- **Workbench Operations**: Agents, Supervisors
- **Workbench Designers**: Process Architects, Developers, Automation Product Owners (APO)
- **Tenant Administration**: Administrators, Auditors

Collaborators are distinguished from **Business Domain Actors** (Business Customers, Business Employees, Business System Actors) whose activities generate Requests but who don't necessarily use Hub as a platform to process them.

---

## Editorial Review

Completed editorial review:
- ✅ Terminology consistency verified
- ✅ Capitalization rules applied correctly (Collaborators for concept, collaborators for common noun)
- ✅ Cross-references validated
- ✅ Fixed ASCII diagram formatting issue in notification-services README
- ✅ No linter errors

---

## Files Identified for Future Review

The following files were identified as potential candidates for using the collaborators term but were not automatically updated (marked for review):

- `platform-notifications/README.md`
- `marketplace-console.md`
- `ms-teams-integration/README.md`
- `workbench-anatomy.md`
- `seer-design/guides/agent-development-lifecycle.md`
- `seer-design/implementation-concepts/agent-observability.md`

---

## Impact

- **Consistency**: Single term for collective references to Hub Personas
- **Clarity**: Clear distinction from Business Domain Actors
- **Conciseness**: Shorter than listing all personas repeatedly
- **Context**: Workbench-scoped term aligns with operational reality

---

## Next Steps

1. Review identified files for additional usage opportunities
2. Monitor documentation for consistency in using the term
3. Consider adding examples in guides showing when to use "collaborators" vs specific persona names

---

## Related Documentation

- [Collaborators Concept](../olympus-hub-docs/01-concepts/collaborators.md)
- [ADR-0114: Collaborators Terminology](../olympus-hub-docs/decision-logs/0114-collaborators-terminology.md)
- [Personas and Journeys](../olympus-hub-docs/08-personas-and-journeys/README.md)
