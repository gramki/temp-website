# Platform Architecture & Practice Council Charter

## Purpose and Authority

The **Platform Architecture & Practice Council (PAPC)** is a single body that serves two modes:

1. **Practice Mode** — Monthly, advisory: knowledge sharing, case reviews, pattern extraction, and best-practice development.
2. **Governance Mode** — Ad-hoc, decision authority: architectural disputes, standards decisions, escalation resolution, and variability governance.

The Council does not replace Domain Team or Win Engineering accountability; it provides alignment, dispute resolution, and governance across the product line.

---

## Membership

- **Senior/Principal Engineers** from Domain Teams (nominated or appointed per team)
- **Solution Architects** from the Solution Architecture team

Membership is stable enough to build continuity; it may be refreshed periodically (e.g. annually) to reflect role changes and growth.

**Quorum:** Defined by the Council (e.g. majority of members) for Governance Mode decisions. Practice Mode has no formal quorum but benefits from broad attendance.

---

## Practice Mode (Monthly)

**Cadence:** Monthly (e.g. fixed day of month).

**Purpose:** Advisory; no binding decisions required.

**Typical agenda:**

- Knowledge sharing across engagements and domains
- Case reviews: what worked, what didn’t, what to reuse
- Pattern extraction: common approaches that could become archetype updates or platform improvements
- Best-practice development: standards, playbooks, DoD refinements
- Variability review: usage of configuration points, consistency, gaps (feeds into Governance Mode if decisions needed)

**Outputs:** Notes, recommendations, and follow-up actions (e.g. archetype updates, documentation). Decisions that change standards or variability model are made in Governance Mode.

---

## Governance Mode (Ad-hoc)

**Cadence:** As needed (triggered by dispute, standards change, or escalation).

**Purpose:** Decision authority on cross-cutting technical and variability matters.

**Triggers:**

- Architectural dispute between Domain Teams and Win Engineering (or between engagements)
- Change to platform or solution architecture standards
- New or deprecated configuration points or options (variability governance)
- Escalation from Domain Maintainers (e.g. repeated quality or scope issues)
- Escalation from Engagement Leads or Solution Architects (e.g. scope vs. platform boundary)

**Process:**

1. Request for decision or escalation is submitted (with context and options).
2. Council convenes (or uses async process if defined).
3. Council decides: approve, reject, or defer with conditions.
4. Decision is documented and communicated to affected parties.
5. Follow-up (e.g. standard update, archetype change) is assigned and tracked.

**Authority:** Council decisions are binding for the scope defined (e.g. “this standard applies to all new PRs”; “this configuration option is approved for use”). Exceptions require Council approval.

---

## Decision Documentation and Enforcement

- **Decisions** (especially in Governance Mode) are recorded in a designated place (e.g. wiki, repo, decision log) with: date, context, decision, rationale, and owner for follow-up.
- **Enforcement** is through Domain Maintainers (for PRs and platform standards), Solution Architects (for archetypes and variability), and Engagement Leads (for delivery scope). Council does not enforce day-to-day; it sets the rules and resolves exceptions.

---

## Variability Governance Responsibility

The Council owns **variability governance**:

- Reviewing variability documentation (e.g. quarterly) and ensuring it stays coherent
- Approving new configuration points or options when engagements need them
- Deprecating unused or harmful options (with migration path)
- Resolving conflicts when engagements need incompatible variants
- Feeding back to Domain Teams and Solution Architecture for platform or archetype changes

Solution Architects document variability per engagement; Council governs the **model** and the **exceptions**. See [Variability Management](../framework/variability-management.md).

---

## Relationship to Domain Teams and Win Engineering

- **Domain Teams** — Council sets or endorses platform-level standards; Domain Maintainers enforce them. Council resolves disputes that Maintainers cannot resolve.
- **Win Engineering** — Council sets or endorses solution-level standards and variability; Solution Architects and Engagement Leads apply them. Council resolves disputes that affect multiple engagements or the product line.
- **Escalation path** — Domain Maintainers, Solution Architects, and Engagement Leads can escalate to Council when they need a binding decision or when local agreement cannot be reached.

---

## References

- [PLE Overview](../framework/ple-overview.md)
- [Variability Management](../framework/variability-management.md)
- [Inner Source Guidelines](inner-source-guidelines.md)
- [Solution Architect Role](../roles/solution-architect.md)
