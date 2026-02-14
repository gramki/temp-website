# Domain Maintainer

## Purpose

The **Domain Maintainer** is dedicated to **governing contributions** to a domain platform. Maintainers review and approve (or reject) PRs from Win Engineering Teams and others, enforce the [Definition of Done](../governance/inner-source-guidelines.md#definition-of-done) and platform standards, coach contributors, and escalate disputes or quality issues to the Platform Architecture & Practice Council. Maintainers do **not** implement features for engagements; they **review and gatekeep**. The goal is to keep platform quality high while enabling inner source.

---

## Responsibilities

- **PR review** — Review PRs to the domain platform for correctness, alignment with platform standards, and DoD compliance. Approve, request changes, or accept with tech debt tagging per [Tech Debt Policy](../governance/tech-debt-policy.md).
- **Standards enforcement** — Enforce platform coding, testing, and architecture standards. Reject or request changes when PRs do not meet standards; use tech debt path only when justified and tracked.
- **Coaching** — Coach Win Engineering contributors on approach when PRs don’t meet bar: suggest design or implementation improvements rather than only rejecting. Consult before implementation (step 2 in [Inner Source flow](../governance/inner-source-guidelines.md#the-flow)) to reduce rework.
- **Escalation** — Escalate to Council when: dispute cannot be resolved locally (e.g. timeline vs. quality), repeated quality or scope issues, or need for standards or process change.
- **Tech debt oversight** — When accepting PRs with tech debt, ensure tagging and remediation ticket are in place; follow up that remediation is scheduled and assigned. See [Tech Debt Policy](../governance/tech-debt-policy.md).

---

## Authority

- **Approve or reject PRs** — Maintainers can approve (merge), reject (request changes), or accept with tech debt tagging. They do **not** have to accept substandard work without tagging or escalation.
- **Enforce DoD** — PRs must meet Definition of Done or be merged only under the tech debt process. Maintainers are the gatekeepers; they do not "do the work for" the Win Engineering Team.
- **Escalate to Council** — When dispute or repeated quality issues cannot be resolved with the Win Engineering Team or Engagement Lead, escalate to Council. Council can set or clarify standards, resolve disputes, or escalate to Engineering Leadership.

---

## Rotation

- **Dedicated role** — Domain Maintainer is a dedicated role (primary accountability is review and governance), but it is **rotated** (e.g. quarterly or semester) so that the burden and expertise are shared and no single person becomes a bottleneck.
- **Rotation cadence** — Exact cadence (e.g. 3 months, 6 months) is set by Domain Team and Council. When rotating out, the next Maintainer is trained and handed over pending PRs and context.
- **May do development** — Maintainers may also do platform development work, but their primary accountability is gatekeeping and quality for contributions to that platform.

---

## Relationship to Domain Engineers and Win Engineering Teams

- **Domain Engineers** — Maintainers are part of the Domain Team; they work with Domain Engineers on platform standards and roadmap. Domain Engineers may contribute to the platform; Maintainers review when the contribution is from someone outside the core Domain Team or when the Domain Team uses the same review process.
- **Win Engineering Teams** — Win Engineering Teams submit PRs to the platform; Maintainers review and merge (or reject, or accept with tech debt). Maintainers consult with Win Engineering Teams before implementation (inner source step 2) to align on approach. Maintainers do not implement for the engagement; they review and guide.

---

## Success Metrics

- **PR cycle time** — Time from PR open to first review (and to merge) meets agreed SLA. See [Inner Source Guidelines](../governance/inner-source-guidelines.md#pr-review-slas).
- **Quality** — Proportion of PRs merged without tech debt; proportion rejected or sent back with clear feedback. Goal: high quality, minimal tech debt; tech debt when used is tagged and remediated.
- **No "PR dumping"** — Win Engineering Teams do not submit half-finished PRs expecting Maintainers to complete them. DoD and consult-first process prevent this; escalation to Council if it persists.
- **Coaching effectiveness** — Contributors improve over time; repeat issues decrease. Maintainers are seen as helpful, not only as gatekeepers.

---

## Career Path

Domain Maintainer is a **technical leadership** role within the Domain Team. Career progression may include: senior or principal Domain Engineer, Council member, or Domain Team lead. Maintainer experience is valued for platform quality and cross-team collaboration. See [Career Paths](career-paths.md).

---

## References

- [Domain Engineering](../framework/domain-engineering.md) — Domain Teams and Maintainer role
- [Inner Source Guidelines](../governance/inner-source-guidelines.md) — Flow, DoD, PR review, soft gate
- [Tech Debt Policy](../governance/tech-debt-policy.md) — Soft gate, tagging, remediation
- [Council Charter](../governance/council-charter.md) — Escalation and governance
- [Stakeholder Concerns](../adoption/stakeholder-concerns.md) — Maintainer concerns and mitigations
