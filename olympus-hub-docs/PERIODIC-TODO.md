# Periodic TODO

Regular quality assurance tasks to maintain documentation health.

---

## Weekly Tasks

### Documentation Hygiene

- [ ] **Review recent commits** — Ensure meaningful commit messages
- [ ] **Check open points** — Update any resolved items across subsystem `open-points.md` files
- [ ] **Validate recent cross-references** — Spot-check links in recently modified docs

### Session Management

- [ ] **Clear scratchpad** — Move any finalized content from `scratchpad/` to proper locations
- [ ] **Update TODO file** — Reflect current priorities and completed work

---

## Bi-Weekly Tasks

### Consistency Checks

- [ ] **Terminology audit** — Sample 2-3 documents for consistent term usage
- [ ] **Template compliance** — Check 1-2 recently created docs against templates
- [ ] **ADR currency** — Verify no pending decisions without ADRs

### Cross-Reference Validation

```bash
# Run from olympus-hub-docs root
find . -name "*.md" -exec grep -l "\](" {} \; | head -20 | xargs -I{} echo "Check: {}"
```

- [ ] **Validate links** — Run link checker or manual spot-check

---

## Monthly Tasks

### Comprehensive Reviews

- [ ] **Design debt review** — Review `design-debt/` for items to address or reprioritize
- [ ] **Open points consolidation** — Aggregate open points across subsystems; identify blockers
- [ ] **Index updates** — Ensure all folder README.md indexes are current

### Quality Metrics

- [ ] **Count open points** — Track trend (should decrease or stabilize)
- [ ] **Count design debt** — Track trend by priority
- [ ] **Documentation coverage** — Identify undocumented areas

### ADR Maintenance

- [ ] **ADR consistency check** — Verify no contradictions between active ADRs
- [ ] **Supersession audit** — Ensure superseded ADRs are properly marked
- [ ] **Related links** — Verify ADR cross-references are bidirectional

---

## Quarterly Tasks

### Strategic Review

- [ ] **Glossary update** — Add any new terms; review existing definitions
- [ ] **Template evolution** — Update templates based on patterns in recent docs
- [ ] **Cursor rules review** — Update `.cursor/rules/` based on learnings

### Comprehensive Validation

- [ ] **Full link validation** — Run comprehensive link checker

```bash
# If using markdown-link-check
find . -name "*.md" | xargs -I{} markdown-link-check {} 2>/dev/null | grep -E "(ERROR|WARN)"
```

- [ ] **Diagram audit** — Review diagrams for currency and accuracy
- [ ] **External reference check** — Verify any external links still work

### Design Debt Triage

- [ ] **Prioritize debt** — Re-evaluate priorities based on upcoming work
- [ ] **Debt retirement** — Identify 1-3 items to resolve this quarter
- [ ] **Debt acceptance** — Mark any debt as "Accepted" if resolution is not justified

---

## Annual Tasks

### Major Housekeeping

- [ ] **Archive obsolete content** — Move deprecated docs to `_archive/`
- [ ] **Restructure if needed** — Evaluate folder structure; reorganize if beneficial
- [ ] **Documentation strategy review** — Is the current approach serving its purpose?

### Stakeholder Feedback

- [ ] **Collect feedback** — Survey documentation consumers
- [ ] **Identify gaps** — What questions keep coming up?
- [ ] **Prioritize improvements** — Plan documentation enhancements

---

## On-Demand Tasks

### When Adding New Subsystem

- [ ] Create folder with `README.md` using template
- [ ] Create `open-points.md`
- [ ] Add to parent index
- [ ] Identify initial design decisions for ADRs

### When Making Significant Changes

- [ ] Update affected cross-references
- [ ] Check for ADR implications
- [ ] Update open points if questions resolved
- [ ] Log design debt if making expedient choices

### When Onboarding New Contributor

- [ ] Share `developing-design-with-cursor.md`
- [ ] Review Cursor rules together
- [ ] Walk through folder structure
- [ ] Explain ADR and design debt processes

---

## Tracking

| Period | Last Completed | Notes |
|--------|----------------|-------|
| Weekly | [YYYY-MM-DD] | [Any notes] |
| Bi-Weekly | [YYYY-MM-DD] | [Any notes] |
| Monthly | [YYYY-MM-DD] | [Any notes] |
| Quarterly | [YYYY-MM-DD] | [Any notes] |

---

## See Also

- [Collaboration Standards](../.cursor/rules/collaboration-standards.mdc)
- [Design Debt Registry](design-debt/README.md)
- [Decision Logs](decision-logs/README.md)

