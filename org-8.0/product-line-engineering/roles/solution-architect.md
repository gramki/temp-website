# Solution Architect

## Purpose

The **Solution Architect (SA)** owns **solution design**, **archetype application**, and **architectural quality** for a Customer Solution. The SA selects or adapts a solution archetype, designs the solution (platforms, integrations, extensions), performs gap analysis, and documents **variability** (configuration points, options, binding time, customer usage). The SA does **not** own delivery timeline or customer liaison; the Engagement Lead does. The SA owns **architecture and variability**.

---

## Responsibilities

- **Solution architecture** — Design the Customer Solution: which domain platforms, how they are configured and integrated, what extensions and integrations are needed. Ensure the solution fits the product line and aligns with Council standards.
- **Archetype selection and adaptation** — Select the appropriate solution archetype (e.g. Credit Card Issuer, Lending); adapt it to the customer’s needs. Use blueprint, cookbook, and playbook; propose archetype updates when the engagement reveals gaps or improvements.
- **Gap analysis** — Identify gaps between customer requirements and available platform/archetype capabilities. Plan custom components or inner source contributions; escalate to Council when new configuration points or options are needed.
- **Variability documentation** — **Critical:** Document variability for the engagement per [Variability Management](../framework/variability-management.md): configuration points used, options chosen, binding time, and which customer/engagement uses what. Submit or update variability documentation so Council can govern and reuse.
- **Archetype ownership (when assigned)** — When the SA is assigned as owner of an archetype (e.g. Credit Card Issuer), maintain that archetype: blueprint, cookbook, playbook, integration patterns, variability points. Allocate time for archetype maintenance alongside engagement work.
- **Knowledge capture** — Own decision log and variability documentation for the engagement; propose archetype updates at transition; contribute to Council pattern extraction (e.g. retrospective summary, case review).

---

## Authority

- **Architectural decisions** — Make solution-level architectural decisions within Council and platform standards. Does not override Domain Maintainers on platform code or Domain Teams on platform roadmap.
- **Escalation to Council** — Escalate to Platform Architecture & Practice Council when: architectural dispute cannot be resolved locally, new configuration point or option is needed, or scope conflicts with archetype or product line boundaries.
- **Archetype updates** — Propose updates to archetypes (blueprint, cookbook, playbook); significant or structural changes may require Council review. Variability changes (new points or options) are governed by Council.

---

## Relationship to Engagement Lead

- **Engagement Lead** owns delivery: timeline, customer liaison, scope discipline, handover. EL owns **when** and **outcomes**.
- **Solution Architect** owns architecture and variability: **what** we build and **how** it fits the product line. SA owns **design** and **variability documentation**.
- **Alignment** — EL and SA align on scope and operating model from engagement start. Disputes (e.g. scope vs. architecture) are escalated to Council or Engineering Leadership.

---

## Engagement Portfolio Limits

To avoid SAs being stretched too thin:

- **Concurrent engagements** — No SA is assigned to more than a defined number of concurrent engagements (e.g. 2–3). Exact cap is set by Solution Architecture and Engineering Leadership.
- **Capacity planning** — Solution Architecture manages SA capacity; if no SA is available, engagement start may be delayed or scope may be reduced (e.g. lighter architecture involvement).
- **Recognition** — Archetype ownership and variability documentation are part of SA performance and recognition; overload is not acceptable.

---

## Variability Tracking Ownership (Critical)

Solution Architects **own** variability documentation for their engagements. This is a **mandatory** part of the role, not optional.

- **Per engagement** — Document which configuration points were used, which options were chosen, binding time, and how this maps to the customer/engagement. Use the template in [Variability Management](../framework/variability-management.md).
- **Submit to Council** — Ensure variability documentation is submitted or updated so Council can perform quarterly variability review and governance.
- **New points or options** — When an engagement needs a configuration point or option not yet in the model, propose it to Council; Council approves or rejects. Do not introduce undocumented variability.

---

## Success Metrics

- **Solution quality** — Customer Solution meets architectural standards; fits archetype and product line; no major rework due to design gaps.
- **Archetype reuse** — Solution is derived from archetype (blueprint, cookbook, playbook); custom work is justified and documented.
- **Variability documentation** — All configuration points and options for the engagement are documented; Council has visibility; no undocumented variability.
- **Archetype evolution** — When owning an archetype: archetype is updated from engagement feedback; blueprint, cookbook, and playbook stay current.
- **Knowledge capture** — Decision log and variability documentation are complete at transition; archetype update proposals are submitted; Council receives input for pattern extraction.

---

## Career Path

Solution Architect is a **technical leadership** role. Career progression may include: senior or principal Solution Architect, Council member, or move to Domain Team (e.g. Principal Domain Engineer) or Engineering Manager. See [Career Paths](career-paths.md).

---

## References

- [Win Engineering](../framework/win-engineering.md) — Win Engineering Teams and SA role
- [Solution Archetypes](../framework/solution-archetypes.md) — Archetype concept and ownership
- [Variability Management](../framework/variability-management.md) — Variability documentation (critical for SA)
- [Council Charter](../governance/council-charter.md) — Council and variability governance
- [Engagement Lead](engagement-lead.md) — EL vs. SA boundaries
- [Engagement Lifecycle](../processes/engagement-lifecycle.md) — SA responsibilities per phase
- [Knowledge Capture](../processes/knowledge-capture.md) — Decision log, archetype updates
- [Stakeholder Concerns](../adoption/stakeholder-concerns.md) — SA concerns and mitigations
