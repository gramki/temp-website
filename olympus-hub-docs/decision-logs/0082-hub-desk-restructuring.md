# ADR-0082: Hub Desk Restructuring

> **Status:** Accepted  
> **Date:** 2026-01-09  
> **Category:** ux-architecture

---

## Context

Hub's original UX architecture included a **Workbench Studio** that combined capabilities for multiple personas:

- **Process Architect** — normative design (SOPs, roles, escalation)
- **Developer** — automation implementation (applications, triggers, tools)
- **Automation Product Owner (APO)** — business intent and outcomes

This conflation created several issues:

1. **Persona confusion** — unclear which capabilities belonged to which role
2. **Access control complexity** — difficult to grant appropriate permissions per role
3. **Navigation overhead** — users had to mentally filter irrelevant capabilities
4. **Inconsistency with Seer** — Seer uses persona-specific desks

---

## Decision

### Restructure Workbench Studio into Three Persona-Specific Desks

Replace the monolithic **Workbench Studio** with three independent desks:

| Desk | Persona | Purpose |
|------|---------|---------|
| **Automation Product Desk** | Automation Product Owner (APO) | Business intent, charters, outcomes, feedback |
| **Scenario Design Desk** | Process Architect | Normative specifications, SOPs, knowledge, escalation |
| **Automation Development Desk** | Developer | Applications, triggers, tools, testing, deployment |

### Desk Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    WORKBENCH DESIGNER DESKS                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  AUTOMATION PRODUCT DESK (APO)                                              │
│  ├── Charter Console                                                        │
│  ├── Outcomes Console                                                       │
│  ├── Backlog Console                                                        │
│  ├── Feedback Console                                                       │
│  └── Production Feedback Inbox (dev workbenches)                            │
│                                                                              │
│  SCENARIO DESIGN DESK (Process Architect)                                   │
│  ├── Scenario Console                                                       │
│  ├── SOP Console                                                            │
│  ├── Knowledge Console                                                      │
│  ├── Memory Console                                                         │
│  └── Escalation Console                                                     │
│                                                                              │
│  AUTOMATION DEVELOPMENT DESK (Developer)                                    │
│  ├── Development Console                                                    │
│  ├── Test Console                                                           │
│  ├── Release Console                                                        │
│  ├── Tool Console                                                           │
│  └── UI Console                                                             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Workbench Ownership

- **Workbenches originate from APO** via the Automation Product Desk
- APO creates the automation charter and proposes the workbench
- Process Architect and Developer join after workbench is established

### Design-Build Handoff

```
APO                    Process Architect           Developer
 │                           │                         │
 ├── Create Charter ────────▶│                         │
 │   Propose Approach        │                         │
 │                           │                         │
 │                           ├── Design Scenarios ────▶│
 │                           │   Define SOPs           │
 │                           │                         │
 │                           │                         ├── Implement
 │                           │                         │   Test & Deploy
 │                           │                         │
```

---

## Consequences

### Positive

1. **Clear persona boundaries** — each desk serves one persona with focused capabilities
2. **Simplified access control** — grant desk access by role
3. **Consistent with Seer** — aligns with Seer's persona-specific desk model
4. **Better navigation** — users see only relevant capabilities
5. **Explicit handoffs** — clear transition points between personas

### Negative

1. **Migration required** — existing Workbench Studio configurations need migration
2. **More desk definitions** — three desks instead of one (but simpler individually)
3. **Cross-desk visibility** — personas may need read access to other desks

### Neutral

1. **No functional change** — same capabilities, different organization
2. **API unchanged** — Creator REST/MCP channels still serve all three personas

---

## Alternatives Considered

### 1. Keep Workbench Studio with Role-Based Views

Filter capabilities in Workbench Studio based on current user's role.

**Rejected because:**
- Still conflated conceptually
- Harder to document and explain
- Permission complexity remains

### 2. Two Desks (Design + Development)

Combine APO and Process Architect into "Design Desk."

**Rejected because:**
- APO focus is business outcomes, not design
- Process Architect focus is normative specifications
- Different skill sets and concerns

---

## Related Documentation

- [Automation Product Desk](../06-ux-architecture/tenant-domain/automation-product-desk.md)
- [Scenario Design Desk](../06-ux-architecture/tenant-domain/scenario-design-desk.md)
- [Automation Development Desk](../06-ux-architecture/tenant-domain/automation-development-desk.md)
- [UX Architecture README](../06-ux-architecture/README.md)

