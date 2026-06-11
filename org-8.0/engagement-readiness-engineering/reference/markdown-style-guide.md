# Markdown Style Guide

[← Back to ERE Guide](../README.md)

Standardized conventions for writing project documentation in markdown. All ERE tools enforce and validate these conventions.

---

## Status Indicators

Use consistent emoji indicators across all documentation:

| Indicator | Status | Use For |
|-----------|--------|---------|
| 🟢 **On Track** | Proceeding as planned | Milestones, objectives, deliverables |
| 🟡 **At Risk** | May miss target without intervention | Milestones, objectives, deliverables |
| 🔴 **Blocked** | Cannot proceed; requires escalation | Milestones, objectives, deliverables |
| ⏸️ **On Hold** | Deliberately paused | Milestones, work items |
| ✅ **Complete** | Done | Tasks, milestones, deliverables |
| ❌ **Cancelled** | Will not be done | Tasks, milestones |

### Usage Example

```markdown
## Milestone Status

| Milestone | Status | Notes |
|-----------|--------|-------|
| Requirements complete | 🟢 On Track | Final review next week |
| Architecture approved | 🟡 At Risk | Waiting on customer decision |
| Go-live | ⏸️ On Hold | Dependent on external system |
```

---

## ROAM Risk Status (SAFe)

For risk tracking, use SAFe's ROAM model with these indicators:

| Indicator | Status | Definition |
|-----------|--------|------------|
| ✅ `[R]` | **Resolved** | Risk eliminated; root cause addressed |
| 🔶 `[O]` | **Owned** | Owner assigned; mitigation in progress |
| 🤝 `[A]` | **Accepted** | Conscious decision to accept; no action planned |
| 🛡️ `[M]` | **Mitigated** | Actions taken; residual risk reduced |

### ROAM Transition Rules

- New risks start as 🔶 `[O]` — every risk needs an owner
- 🔶 `[O]` → 🛡️ `[M]` when mitigation actions complete
- 🔶 `[O]` → ✅ `[R]` when risk is eliminated
- 🔶 `[O]` → 🤝 `[A]` when team decides to accept (requires documented rationale)
- 🤝 `[A]` risks reviewed each PI — still valid to accept?

### Usage Example

```markdown
## PI Risks

| ID | Risk | Status | Owner | Mitigation |
|----|------|--------|-------|------------|
| R1 | Vendor API instability | 🔶 [O] | @jane | Circuit breaker implementation |
| R2 | Resource availability | 🛡️ [M] | @bob | Cross-training completed |
| R3 | Scope creep | 🤝 [A] | @epm | Monitored; change control in place |
```

---

## Priority / Severity

Use priority indicators consistently across requirements, bugs, and work items:

| Indicator | Level | Meaning |
|-----------|-------|---------|
| 🔥 **P0** | Critical | Immediate action required |
| 🔶 **P1** | High | Address this PI |
| 🔷 **P2** | Medium | Address next PI |
| ⬜ **P3** | Low | Backlog |

### Usage Example

```markdown
## Open Issues

| ID | Issue | Priority | Owner |
|----|-------|----------|-------|
| BUG-101 | Payment processing timeout | 🔥 P0 | @dev-lead |
| BUG-102 | Report formatting issue | 🔷 P2 | @ui-team |
```

---

## Task Lists

Use GitHub-compatible task list syntax:

```markdown
- [x] Completed task
- [ ] Pending task
- [ ] ~Cancelled task~ (strikethrough)
```

Renders as:

- [x] Completed task
- [ ] Pending task
- [ ] ~Cancelled task~

---

## Callouts (GitHub-supported)

Use GitHub's alert syntax for important information:

```markdown
> [!NOTE]
> Useful information the reader should know.

> [!TIP]
> Helpful advice for better outcomes.

> [!IMPORTANT]
> Key information the reader must not miss.

> [!WARNING]
> Potential issue that needs attention.

> [!CAUTION]
> Risk of negative consequences.
```

### When to Use Each

| Callout | Use For |
|---------|---------|
| `[!NOTE]` | Background information, context, clarifications |
| `[!TIP]` | Best practices, efficiency suggestions |
| `[!IMPORTANT]` | Critical information that affects decisions |
| `[!WARNING]` | Potential problems or risks to be aware of |
| `[!CAUTION]` | Actions that could cause harm or data loss |

---

## Requirements Language (RFC 2119)

Use standardized keywords for requirements:

| Keyword | Meaning |
|---------|---------|
| **MUST** / **REQUIRED** | Absolute requirement |
| **MUST NOT** | Absolute prohibition |
| **SHOULD** / **RECOMMENDED** | Strong preference; valid exceptions exist |
| **SHOULD NOT** | Strong preference against |
| **MAY** / **OPTIONAL** | Truly optional |

### Usage Example

```markdown
## Security Requirements

- The system **MUST** encrypt all data at rest
- Authentication tokens **MUST NOT** be logged
- Sessions **SHOULD** expire after 30 minutes of inactivity
- The UI **MAY** support biometric authentication
```

---

## Cross-References

### Internal Links

Use relative paths for internal documentation links:

```markdown
Internal links:
- See [CR-001](../change-requests/CR-001-title.md)
- Relates to [ADR-003](../decisions/ADR-003-title.md)
- Per [PI-2 Objectives](../pi/PI-2/pi-objectives.md)
```

### External Links (SharePoint)

Use full URLs for SharePoint and external content:

```markdown
External links (SharePoint):
- Customer requirements: [Link](https://sharepoint.com/sites/...)
- Original RFP: [Link](https://sharepoint.com/sites/...)
```

---

## Tables

Use tables for structured data. Align columns for readability:

```markdown
| ID | Item | Status | Owner | Due |
|----|------|--------|-------|-----|
| 001 | Requirements review | 🟢 On Track | @jane | 2024-03-15 |
| 002 | Architecture sign-off | 🟡 At Risk | @bob | 2024-03-20 |
```

### Table Guidelines

- Use header row with column names
- Align numeric data right (if supported)
- Keep cell content concise
- Use status indicators consistently

---

## Dates

Use ISO 8601 format: `YYYY-MM-DD`

Examples:
- `2024-03-15`
- `2024-Q1` (for quarters)
- `2024-W12` (for weeks, if needed)

This format:
- Sorts correctly
- Is unambiguous across locales
- Works with automation tools

---

## File Naming

### General Rules

- **Lowercase with hyphens**: `pi-objectives.md`, `requirements-matrix.md`
- **Prefix with number for ordering**: `01-introduction.md`, `02-scope.md`
- **Include identifier in name**: `ADR-003-database-choice.md`, `CR-001-api-change.md`

### Common Patterns

| Pattern | Example | Use For |
|---------|---------|---------|
| `{type}-{number}-{title}.md` | `ADR-003-database-choice.md` | Numbered records |
| `{date}-{topic}.md` | `2024-03-15-kickoff.md` | Meeting notes, updates |
| `{feature-area}.md` | `payment-processing.md` | Requirements by area |
| `{category}.md` | `performance.md` | Non-functional requirements |

---

## Headers and Structure

### Document Structure

```markdown
# Document Title

Brief introduction paragraph.

---

## Major Section

Content...

### Subsection

More detail...

---

## Another Major Section

...
```

### Guidelines

- One `#` title per document
- Use `---` to separate major sections visually
- Keep header hierarchy logical (don't skip levels)
- Use sentence case for headers

---

## Code Blocks

Use fenced code blocks with language specification:

````markdown
```yaml
config:
  setting: value
```

```sql
SELECT * FROM engagements WHERE status = 'active';
```

```bash
git clone https://github.com/org/repo.git
```
````

---

## Related Content

- [PI Artifacts Reference](pi-artifacts.md) — SAFe artifact definitions
- [Document Governance](../05-document-governance/README.md) — where documentation lives
- [Glossary](glossary.md) — terminology definitions
