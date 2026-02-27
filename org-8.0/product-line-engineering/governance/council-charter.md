# Platform Architecture Council Charter

## Purpose and Authority

The **Platform Architecture Council (PAC)** is a single body that serves two modes:

1. **Practice Mode** — Monthly, advisory: knowledge sharing, case reviews, pattern extraction, and best-practice development.
2. **Governance Mode** — Ad-hoc, decision authority: architectural disputes, standards decisions, escalation resolution, and variability governance.

The Council does not replace Product Line Squad or Engagement Engineering accountability; it provides alignment, dispute resolution, and governance across the product line.

---

## Membership

- **Senior/Principal Engineers** from Product Line Squads (nominated or appointed per team)
- **Engagement Architects** (assigned via ERC)

Membership is stable enough to build continuity; it may be refreshed periodically (e.g. annually) to reflect role changes and growth.

**Quorum:** Defined by the Council (e.g. majority of members) for Governance Mode decisions. Practice Mode has no formal quorum but benefits from broad attendance.

---

## Practice Mode (Monthly)

**Cadence:** Monthly (e.g. fixed day of month).

**Purpose:** Advisory; no binding decisions required.

**Typical agenda:**

- Knowledge sharing across Engagements and domains
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

- Architectural dispute between Product Line Squads and Engagement Engineering (or between engagements)
- Change to platform or solution architecture standards
- New or deprecated configuration points or options (variability governance)
- Escalation from Product Line Maintainers (e.g. repeated quality or scope issues)
- Escalation from Engineering Leads (ELs) or Engagement Architects (e.g. scope vs. platform boundary)

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
- **Enforcement** is through Product Line Maintainers (for PRs and platform standards), Engagement Architects (for archetypes and variability), and Engineering Leads (ELs, for squad delivery scope). Council does not enforce day-to-day; it sets the rules and resolves exceptions.

---

## Variability Governance Responsibility

The Council owns **variability governance**:

- Reviewing variability documentation (e.g. quarterly) and ensuring it stays coherent
- Approving new configuration points or options when engagements need them
- Deprecating unused or harmful options (with migration path)
- Resolving conflicts when engagements need incompatible variants
- Feeding back to Product Line Squads and Engagement Architects for platform or archetype changes

Engagement Architects document variability per Engagement; Council governs the **model** and the **exceptions**. See [Variability Management](../framework/variability-management.md).

---

## Relationship to Product Line Squads and Engagement Engineering

- **Product Line Squads** — Council sets or endorses platform-level standards; Product Line Maintainers enforce them. Council resolves disputes that Maintainers cannot resolve.
- **Engagement Engineering** — Council sets or endorses solution-level standards and variability; Engagement Architects and ELs/EPMs apply them. Council resolves disputes that affect multiple Engagements or the product line.
- **Escalation path** — Product Line Maintainers, Engagement Architects, and ELs/EPMs can escalate to Council when they need a binding decision or when local agreement cannot be reached.

---

## Relationship to ERC and PAC

The Platform Architecture Council (PAC — this Council) and the Engagement Readiness Council (ERC) are complementary governance bodies:

- **PAC** governs architecture standards, practice sharing, pattern extraction, variability, and inner source quality. Its members are engineers and architects.
- **ERC** governs the Engagement pipeline: readiness assessments, role assignments (EA, EPM, AVA), and capacity coordination through the Portfolio Program Manager (PPM).

PAC sets the technical rules; ERC ensures Engagements start with the right people and ingredients. Both feed into each other: PAC patterns improve archetype quality that ERC uses for readiness; ERC delivery learnings feed PAC practice reviews.

See the [Engagement Operating Model Guide](../../engagement/README.md) for ERC details.

---

## References

- [PLE Overview](../framework/ple-overview.md)
- [Variability Management](../framework/variability-management.md)
- [Inner Source Guidelines](inner-source-guidelines.md)
- [Engagement Architect Role](../roles/engagement-architect.md)
- [Engagement Operating Model Guide](../../engagement/README.md) — ERC, role structure
