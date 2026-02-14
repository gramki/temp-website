# Tech Debt Policy

## Purpose

When a PR to a domain platform does not fully meet the [Definition of Done](inner-source-guidelines.md#definition-of-done) but there is strong timeline pressure (e.g. engagement deadline), we use a **soft gate**: the PR may be merged with **tech debt** tagging. This policy defines when that is allowed, how tech debt is tracked, and how it is remediated. The goal is to balance delivery speed with platform quality; tech debt is the exception, not the norm.

---

## Soft Gate Policy: When Substandard Code Can Merge

A PR may be merged **without** full DoD compliance only if:

1. **Timeline pressure is real** — Engagement deadline or customer commitment cannot be moved without material impact, and improving the PR to full DoD would exceed available time.
2. **Tech debt is tagged** — The merge is explicitly tagged as tech debt (e.g. label, ticket, or comment) with: description of what’s missing, owner for remediation, and target remediation date.
3. **Domain Maintainer and (if needed) Council agree** — Maintainer accepts the merge with tech debt; if the gap is large or contentious, Council is consulted.
4. **Remediation is scheduled** — A remediation ticket (or equivalent) is created and assigned; it is tracked until closed.

**Not allowed:** Merging without DoD and without tech debt tagging and remediation plan. That undermines platform quality and is not acceptable.

---

## Tech Debt Tagging and Tracking

- **Tag at merge time** — Use a consistent tag/label (e.g. `tech-debt`) and a short description of what’s missing (e.g. "Missing tests for X," "Documentation deferred").
- **Remediation ticket** — Create a ticket (or equivalent) with: link to PR/commit, description of debt, owner (Domain Team or agreed party), target date.
- **Central view** — Maintain a list or dashboard of open tech debt items (e.g. by platform or by engagement) so Council and Domain Teams can prioritize.
- **Review cadence** — Council or Domain Teams review tech debt periodically (e.g. monthly or quarterly); aging or high-impact items are escalated.

---

## Remediation Expectations

- **Timeframe** — Target remediation within a defined window (e.g. 4–8 weeks after merge, or next platform release cycle). Exact SLA is set by Council or Domain Team.
- **Ownership** — Remediation is owned by the Domain Team (or by the Win Engineering Team if agreed and feasible). Default is Domain Team so platform quality stays with platform owners.
- **Closure** — When remediation is done (tests added, docs updated, etc.), the tech debt ticket is closed and the tag/label is removed (or marked resolved).

---

## Council Oversight of Tech Debt

- **Practice Mode** — Council may review tech debt trends: volume, age, distribution by platform or engagement. Identifies systemic issues (e.g. repeated gaps in testing, documentation).
- **Governance Mode** — Council can set or tighten policy: e.g. stricter remediation SLA, limits on what can be accepted as tech debt, or escalation when tech debt exceeds a threshold.
- **Escalation** — If tech debt accumulates (e.g. many open items, repeated violations), Council can escalate to Engineering Leadership and require a remediation plan or process change.

---

## Reserved Capacity for Remediation

Domain Teams should reserve some capacity for tech debt remediation so that accepted debt does not pile up indefinitely. The exact percentage or allocation is set by Domain Team and Engineering Leadership; the principle is that accepting tech debt implies commitment to remediate it.

---

## Escalation for Excessive Tech Debt

If:

- Tech debt items are frequently overdue, or
- The same type of debt repeats (e.g. missing tests), or
- Tech debt volume exceeds an agreed threshold,

then:

1. **Domain Maintainers** raise to Domain Team lead and Council.
2. **Council** reviews and may: tighten DoD, shorten remediation SLA, restrict what can be accepted as tech debt, or escalate to Engineering Leadership.
3. **Engineering Leadership** may impose process changes (e.g. mandatory review of tech debt at engagement retrospectives, or capacity reservation for remediation).

---

## References

- [Inner Source Guidelines](inner-source-guidelines.md) — DoD, soft gate, PR flow
- [Council Charter](council-charter.md) — Council’s governance role
- [Domain Maintainer Role](../roles/domain-maintainer.md) — Maintainer authority and escalation
