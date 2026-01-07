# 0064. Memory Services Subfolder Organization

## Status

Accepted

## Date

2026-01-07

## Context

Hub Memory Services encompasses two distinct capability areas:
1. **Enterprise Memory** — Organizational-level, durable, CAF-compliant memory for audit and institutional learning
2. **Agent Memory** — Agent/session-level, ephemeral memory for operational continuity

As documentation grew, a decision was needed on how to organize these within the subsystem structure:
- Should they be separate subsystems?
- Should they be subfolders within memory-services?
- Should they remain as flat files?

### Constraints

- Enterprise and Agent Memory share the ESPP taxonomy
- They may use different storage backends
- Promotion flows from Agent → Enterprise
- Documentation is growing with distinct APIs and semantics for each

### Requirements

- Clear separation of Enterprise vs Agent concerns
- Shared concepts documented once (DRY)
- Easy navigation for developers
- Future extensibility

## Decision

We will organize Memory Services into **subfolders** within the memory-services subsystem:

```
memory-services/
  README.md                     # Unified overview
  
  enterprise-memory/            # Enterprise Memory Services
    README.md
    query-api.md
    access-tools.md
    retention-policy.md
  
  agent-memory/                 # Agent Memory Services
    README.md
    sdk.md
    retention-and-decay.md
  
  shared/                       # Shared concepts
    README.md
    espp-taxonomy.md
    pii-policy.md
```

### Key Points

- **Same subsystem, different capabilities**: Both are "Memory Services" offered by Hub
- **Subfolders for separation**: Clear distinction without creating separate subsystems
- **Shared folder for commonality**: ESPP taxonomy, PII policy documented once
- **Unified README**: Parent README provides overview of both

## Alternatives Considered

### Alternative 1: Separate Subsystems

Create `enterprise-memory-services/` and `agent-memory-services/` as sibling subsystems.

**Pros:**
- Maximum separation
- Parallel structure with other subsystems

**Cons:**
- Duplicates shared concepts (ESPP, provisioning)
- Obscures the promotion relationship (Agent → Enterprise)
- They share infrastructure and taxonomy

**Why rejected:** They're interconnected capabilities, not independent subsystems.

---

### Alternative 2: Flat Structure with Prefixes

Keep flat files but prefix by type: `enterprise-*.md`, `agent-*.md`.

**Pros:**
- Simple, no nesting
- All files visible at top level

**Cons:**
- Gets cluttered as documentation grows
- Harder to navigate
- No clear grouping

**Why rejected:** Already has 6+ files; will grow larger. Subfolders provide better organization.

---

## Consequences

### Positive

- **Clear separation**: Enterprise vs Agent concerns clearly delineated
- **DRY compliance**: Shared concepts documented once
- **Extensibility**: Easy to add more documents to each subfolder
- **Navigation**: Developers can find the relevant section quickly
- **Relationship visible**: Parent README shows both capabilities together

### Negative

- **Deeper paths**: File paths are longer (e.g., `memory-services/enterprise-memory/query-api.md`)
- **Cross-references**: More relative paths to manage

### Neutral

- Legacy files at root level retained for reference during transition
- Some documents may need path updates

## Implementation Notes

- Created three subfolders: `enterprise-memory/`, `agent-memory/`, `shared/`
- Moved/copied enterprise-focused files to `enterprise-memory/`
- Created new agent-memory structure with stubs
- Created shared ESPP taxonomy and PII policy documents
- Updated parent README with unified overview

## Related Decisions

- [ADR-0030: Workbench-Scoped Data Stores](./0030-workbench-scoped-data-stores.md) — Store scoping model
- [ADR-0029: CAF Control Plane](./0029-caf-control-plane.md) — CAF as control plane

## References

- [Memory Services README](../04-subsystems/memory-services/README.md)
- [Enterprise Memory README](../04-subsystems/memory-services/enterprise-memory/README.md)
- [Agent Memory README](../04-subsystems/memory-services/agent-memory/README.md)

