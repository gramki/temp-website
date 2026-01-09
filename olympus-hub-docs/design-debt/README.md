# Design Debt Registry

This folder tracks **design debt** — expedient decisions that require future attention.

---

## What is Design Debt?

Design debt occurs when we:

- Choose a simpler approach knowing a more robust solution is needed later
- Defer detailed design for a component to meet timelines
- Make assumptions that need validation
- Leave gaps in documentation that need filling
- Create temporary solutions that should be replaced

Design debt is **not inherently bad** — it's a conscious trade-off. The key is **tracking it** so it doesn't become hidden technical risk.

---

## When to Log Design Debt

Log an entry when:

| Situation | Example |
|-----------|---------|
| **Expedient choice** | "Used simple algorithm; need to evaluate performance at scale" |
| **Deferred detail** | "Error handling TBD; happy path only documented" |
| **Assumption made** | "Assumed max 100 concurrent users; needs load testing" |
| **Known gap** | "Security model placeholder; needs threat modeling" |
| **Temporary solution** | "Hardcoded config; should be externalized" |

---

## Design Debt Entry Format

Each entry should be a separate file: `DD-NNNN-short-name.md`

```markdown
# DD-NNNN: [Short Title]

## Status
[Open | In Progress | Resolved | Accepted]

## Priority
[High | Medium | Low]

## Location
[Path to affected documentation or code]

## Description
[What is the debt? What was the expedient choice?]

## Ideal State
[What should the solution look like?]

## Incurred
- **Date:** [YYYY-MM-DD]
- **Context:** [Why was this choice made?]
- **Related ADR:** [Link if applicable]

## Impact
[What are the risks if this isn't addressed?]

## Resolution Plan
[How should this be addressed? What's needed?]

## Resolution
[Fill in when resolved]
- **Date:** [YYYY-MM-DD]
- **How resolved:** [Description]
- **Reference:** [Link to updated docs/ADR]
```

---

## Current Debt Summary

| ID | Title | Priority | Status | Location |
|----|-------|----------|--------|----------|
| [DD-0001](DD-0001-example.md) | [Example Title] | Medium | Open | [path] |

<!-- Update this table as entries are added/resolved -->

---

## Priority Definitions

| Priority | Definition | Action |
|----------|------------|--------|
| **High** | Blocks progress or creates significant risk | Address in next sprint/phase |
| **Medium** | Technical risk or maintenance burden | Schedule within quarter |
| **Low** | Cleanup, optimization, or polish | Address when convenient |

---

## Relationship to Other Artifacts

| Artifact | Relationship |
|----------|--------------|
| **ADRs** | ADRs capture *decisions*; design debt captures *known gaps* in those decisions |
| **Open Points** | Open points are *questions*; design debt is *known suboptimal answers* |
| **TODO** | TODOs are *tasks*; design debt is *technical state* requiring tasks |

---

## Process

### Adding Debt

1. Create entry file: `DD-NNNN-short-name.md`
2. Fill in template fields
3. Add to summary table above
4. Add `<!-- DESIGN-DEBT: DD-NNNN -->` comment in affected documentation

### Reviewing Debt

- Review quarterly during planning
- Prioritize based on risk and upcoming work
- Resolve debt before building on affected areas

### Resolving Debt

1. Address the underlying issue
2. Update documentation/code
3. Mark entry as Resolved with details
4. Update summary table
5. Remove `<!-- DESIGN-DEBT -->` comments from docs

---

## See Also

- [Decision Logs](../decision-logs/README.md) — For architectural decisions
- [PERIODIC-TODO](../PERIODIC-TODO.md) — For regular quality checks

