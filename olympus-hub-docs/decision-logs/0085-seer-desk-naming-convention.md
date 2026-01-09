# ADR-0085: Seer Desk Naming Convention

> **Status:** Accepted  
> **Date:** 2026-01-09  
> **Category:** ux-architecture

---

## Context

Seer's UX architecture initially used inconsistent terminology for persona workspaces:

| Original Name | Persona |
|---------------|---------|
| Agent Design **Studio** | CSA |
| Agent Development **Workbench** | AE |
| Agent Operations **Center** | ARE |
| Cognitive Health **Desk** | COS |

This inconsistency created confusion:
- "Studio," "Workbench," "Center," and "Desk" implied different things
- Hub uses "Desk" consistently for persona workspaces
- No clear rationale for different terms

Additionally, within the Cognitive Health Desk, console names were unclear:
- "Detection Console" — what is being detected?
- "Routing Console" — routing of what?

---

## Decision

### 1. Standardize on "Desk" Terminology

Rename all Seer persona workspaces to use "Desk" suffix:

| Before | After |
|--------|-------|
| Agent Design Studio | **Agent Design Desk** |
| Agent Development Workbench | **Agent Development Desk** |
| Agent Operations Center | **Agent Operations Desk** |
| Cognitive Health Desk | Cognitive Health Desk (unchanged) |

### 2. Clarify Console Names in Cognitive Health Desk

| Before | After | Rationale |
|--------|-------|-----------|
| Detection Console | **Patterns Console** | Detects and displays patterns |
| Routing Console | **Issues Console** | Routes issues for resolution |

### Complete Desk Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SEER DESKS (STANDARDIZED)                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  AGENT DESIGN DESK (CSA)                                                    │
│  ├── Architecture Console                                                   │
│  ├── Autonomy Console                                                       │
│  └── Governance Console                                                     │
│                                                                              │
│  AGENT DEVELOPMENT DESK (AE)                                                │
│  ├── Development Console                                                    │
│  ├── Test Console                                                           │
│  └── Release Console                                                        │
│                                                                              │
│  AGENT OPERATIONS DESK (ARE)                                                │
│  ├── Health Console                                                         │
│  ├── Performance Console                                                    │
│  └── Incidents Console                                                      │
│                                                                              │
│  COGNITIVE HEALTH DESK (COS)                                                │
│  ├── Patterns Console (was Detection Console)                               │
│  ├── Issues Console (was Routing Console)                                   │
│  └── Insights Console                                                       │
│                                                                              │
│  KNOWLEDGE & MEMORY DESK (KMO)                                              │
│  ├── Knowledge Console                                                      │
│  ├── Memory Console                                                         │
│  └── Quality Console                                                        │
│                                                                              │
│  COMPLIANCE & AUDIT DESK (ARAO)                                             │
│  ├── Audit Console                                                          │
│  ├── Compliance Console                                                     │
│  └── Reports Console                                                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Rationale

### Why "Desk"?

| Term | Connotation | Issue |
|------|-------------|-------|
| Studio | Creative, design-focused | Implies art, not operations |
| Workbench | Development, technical | Implies coding only |
| Center | Command, control | Implies monitoring only |
| **Desk** | Work surface, role-based | **Neutral, consistent with Hub** |

### Why Rename COS Consoles?

| Console | New Name | Why |
|---------|----------|-----|
| Detection Console | Patterns Console | "Detection" is vague; "Patterns" clarifies what COS observes |
| Routing Console | Issues Console | "Routing" is an action; "Issues" clarifies what gets routed |

---

## Consequences

### Positive

1. **Consistency** — Seer aligns with Hub's "Desk" terminology
2. **Clarity** — console names reflect purpose, not action
3. **Simpler onboarding** — one term to learn for persona workspaces
4. **Professional tone** — "Desk" is business-neutral

### Negative

1. **Documentation updates** — references to old names need updating
2. **User migration** — existing users may need to adjust

### Neutral

1. **No functional change** — same capabilities, different names
2. **Hub alignment** — reinforces Hub-Seer UX consistency

---

## Alternatives Considered

### 1. Keep Mixed Terminology

Preserve Studio/Workbench/Center as persona-appropriate labels.

**Rejected because:**
- Inconsistency confuses users
- No clear mapping of term to persona type
- Harder to document and maintain

### 2. Use "Console" for Everything

Call them "Design Console," "Development Console," etc.

**Rejected because:**
- Console is a sub-unit within a Desk
- Would conflict with actual console names
- Loses hierarchical clarity

---

## Related Documentation

- [Seer UX Architecture README](../../olympus-seer-docs/seer-design/ux-architecture/README.md)
- [Seer Desk Requirements](../../olympus-seer-docs/seer-design/ux-architecture/desk-requirements.md)
- [ADR-0082: Hub Desk Restructuring](./0082-hub-desk-restructuring.md)

