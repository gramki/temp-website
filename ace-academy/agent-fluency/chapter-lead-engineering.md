# Agent Fluency Chapter Lead — Engineering: Role Charter

> **v0.1 · last updated 2026-06-11**
> Role charter for the Agent Fluency Chapter Lead (Engineering). Pairs with the [Agent Fluency for Builders rubric](agent-fluency-for-builder.md) and the [developer how-to](developer-howto.md). KPI numbers are starting points, to be calibrated with the L&D anchor owner in the same spirit as the rubric's *Setting measurable bars* section.

---

## TL;DR

- The Chapter Lead owns the **outcome** of agent fluency adoption for the engineering function: AF3 (Practitioner) across the function by November 2026, and the durable structures — curriculum, shared-asset standards, Architect network, measurement — that keep the distribution moving after that.
- **L&D anchors the org-wide program** with a designated owner who co-designs Agent Fluency as a competency pillar alongside People, Execution, Organization, Strategy, and Craft.
- **Curriculum, learning resources, and tools decisions are made with a volunteer chapter group** that the Chapter Lead convenes and chairs. Implementation and rollout work is spread across teams; the Chapter Lead directs it and owns the result.
- Chapter leads for other functions follow; the Engineering Chapter Lead sets the template they inherit.

---

## Role framing

**Title:** Agent Fluency Chapter Lead — Engineering

**Mandate:** Own the outcome of agent fluency adoption for the engineering function — measurably moving the engineering population to Practitioner (AF3) by November 2026 and building the durable structures (curriculum, assets, Architect network, measurement) that keep the distribution moving after that.

**Fluency prerequisite:** The Chapter Lead should be at AF4–AF5 fluency — proof-by-example matters — but the job is program leadership, not being the org's best builder.

### Operating relationships

| Counterpart | Relationship |
|---|---|
| L&D anchor owner | Co-owner of program design; Chapter Lead brings function expertise, L&D brings competency-framework machinery and program governance |
| Volunteer chapter group | Chapter Lead convenes and chairs; decisions on curriculum, learning resources, and tools are made here, but the Chapter Lead breaks ties and owns the decision log |
| Agent Fluency Architects (per team) | The Chapter Lead's distribution network — recruits, calibrates, and rotates them per the rubric's Architect model |
| Engineering managers / tech leads | Accountable for their team's work architecture and quarterly re-measurement; Chapter Lead enables, doesn't substitute |
| Future chapter leads (other functions) | Peer community once the Operators framework lands; Engineering Chapter Lead sets the template they inherit |

### Chapter Lead vs. Agent Fluency Architect

The **Architect** (defined in the rubric) is a team-scoped role accountable for a team's agent surface — stack, risk policy, monitoring. The **Chapter Lead** is function-scoped and accountable for the *program* — competency integration, curriculum, and the aggregate fluency distribution. Architects are the Chapter Lead's distribution network, not their reports.

---

## Activities

### 1. Competency framework integration (with L&D)

- Co-design Agent Fluency as the sixth pillar alongside People, Execution, Organization, Strategy, and Craft — mapping AF1–AF5 onto the existing grade/level conventions without conflating fluency with career level (the rubric is explicit that AF levels are distinct from G/L levels).
- Define how the pillar appears in development conversations while protecting the rubric's red line: scores inform development plans, never compensation or performance ratings.
- Maintain the rubric as a living artifact — annual refresh, threshold calibration guidance, changelog discipline (the source-of-truth markdown → regenerated deliverables model already in place).

### 2. Curriculum and learning resources (via volunteer chapter)

- Convene the chapter group on a fixed cadence; own the agenda, decision log, and roadmap.
- Direct production of the curriculum ladder: AF2→AF3 onboarding track, AF3→AF4 builder track, per-role how-tos beyond the developer how-to (QA, SRE, EM, PM, designer, data — the rubric's "builders" definition covers all of them).
- Own the academy track that trains G1/G2 hires to Practitioner, and the hiring-assessment rubric for future hires.
- Curate learning resources: internal demos, recorded sessions, the prompt cookbook, postmortem library.

### 3. Tools and shared infrastructure standards (via volunteer chapter)

- Drive decisions on the sanctioned tool surface (IDE agents, CLI agents, MCP connectors for the internal stack — Foundry CI, Weave CD, Delta, Nalanda, Olympus Watch).
- Direct the chapter group to agree, publish, and periodically revise the function's **conventions and practices** for agent-facing assets — project-instruction files, skill structure and documentation, versioning, eval coverage expectations. Specific conventions (e.g., AGENTS.md today) are evolving; the chapter's agreed convention set is the standard, not any single named artifact.
- Sponsor shared infrastructure that no single team will build alone — skill marketplaces/registries, eval harness templates, Governor/Monitor skill patterns.

### 4. Rollout direction and Architect network

- Direct the rollout across engineering teams: sequencing, team-level baseline assessments, work-architecture creation by managers/tech leads.
- Recruit, appoint, and calibrate Agent Fluency Architects; run their community of practice; manage rotation toward teams where adoption needs the most lift.
- Unblock teams where adoption stalls — distinguishing tooling gaps, context gaps ("AI is bad at our codebase" as a problem to solve), and incentive gaps.

### 5. Measurement and reporting

- Own the quarterly re-measurement cycle: baseline, distribution tracking, bottleneck-dimension analysis (the four dimensions give diagnostic signal — a function strong on Daily Use but weak on Judgment is a risk, not a success). Note that the rubric's composite cap (`min(round(average), min(dimensions) + 1)`) means the fastest way to move the function's numbers is fixing the weakest dimension — typically Judgment & Oversight or Org Influence. That's where to direct effort.
- Report distribution movement to engineering leadership and the L&D-anchored program — *movement, not leaderboards*, per the rubric's pitfalls.
- Run the calibration process so "roughly 80%" and "≥N assets" thresholds are set per-team against real work architectures, not gamed.

### 6. Risk, judgment, and governance posture

- Ensure the Judgment & Oversight dimension keeps pace with Daily Use across the function — postmortem culture for agent failures, prompt-injection awareness, cost discipline, the named-failure-mode vocabulary.
- Partner with security/legal counterparts as the cross-functional chapter structure emerges.

### 7. Cross-chapter program contribution

- Serve as the senior chapter lead in the L&D-anchored key program; template the chapter model (charter, cadence, measurement) for subsequent function chapters.
- Feed engineering learnings into the planned *Agent Fluency for Operators* framework.

---

## Key Result Areas (KRAs)

1. **Engineering function reaches and sustains the fluency bar** — AF3 across the function by Nov 2026; healthy AF4/AF5 layer thereafter.
2. **Agent Fluency is institutionalized as a competency pillar** — integrated into the framework, development conversations, and hiring; jointly owned with L&D.
3. **A complete, current curriculum and assessment system exists** — role-specific tracks, academy program, hiring assessment, annual rubric refresh.
4. **A functioning chapter and Architect network operates without the lead as bottleneck** — volunteer chapter making timely decisions; every team covered by an Architect or a named path to one.
5. **Shared asset and tooling ecosystem is healthy** — teams build on common infrastructure rather than parallel private setups; the chapter-agreed quality bar (docs, versioning, evals) holds.
6. **Judgment keeps pace with adoption** — risk posture, postmortem culture, and cost discipline scale with usage; no major incident attributable to ungoverned agent use.
7. **The chapter model is replicable** — playbook adopted by at least the next function chapter. *(Contains a stretch component — see KPIs.)*

---

## KPIs

Grouped by KRA. Numbers are starting points to calibrate with L&D.

Adoption KPIs are sourced from manager-reviewed composites with evidence sampling (per the rubric's *Evidence per dimension* lists) — never from individual leaderboards, and never connected to compensation or performance ratings. This protects the self-assessment honesty the whole measurement system depends on.

### Adoption (KRA 1)

- % of engineering at composite AF3+ — target ≥80% by Nov 2026, ≥95% within two quarters after.
- % at AF4+ — target 20–25% by mid-2027; AF5 in the rubric's 5–10% band (treat exceeding 10% as a calibration smell, not a win).
- Quarter-over-quarter upward distribution movement — positive every quarter; no dimension's function-wide median lagging the composite by more than one level.
- % of teams with a documented work architecture (the denominator for everything) — 100% within two quarters of rollout start.

### Institutionalization (KRA 2)

- Pillar live in the competency framework and used in development conversations — % of engineers with one agent-fluency growth move in their quarterly development plan (target ≥90%).
- 100% of new engineering hires assessed for Practitioner fluency at hiring; G1/G2 academy cohort pass rate to AF3 ≥90%.
- Zero instances of fluency scores feeding compensation/rating decisions (a guardrail KPI — it protects the signal quality everything else depends on).

### Curriculum (KRA 3)

- Per-role how-to coverage: % of builder roles with a published how-to (developer exists; target 100% of engineering roles within 3 quarters).
- Self-assessment + manager review completion per quarterly cycle ≥90%, within the rubric's ~45-min/person budget.
- Learner-reported usefulness of curriculum assets (≥4/5) and time-to-AF3 for new hires (target: within first quarter).

### Chapter & Architect network (KRA 4)

- Architect coverage: % of teams with an appointed Architect — target 100% by Nov 2026.
- Chapter decision latency: median time from question raised to decision logged ≤ 1 cycle; decision log current.
- Volunteer chapter health: active participation from ≥N teams; volunteer retention quarter over quarter.

### Asset ecosystem (KRA 5)

- Shared assets per team meeting the chapter-agreed quality bar (skill documentation, versioning, eval coverage) — ≥N per quarter, calibrated per team size.
- Cross-team asset reuse: % of shared assets used by someone outside the authoring team (the rubric's "at least one other person" bar, aggregated).
- % of repos conformant with the chapter-agreed conventions and practices for agent-facing assets (project-instruction files, skill structure, versioning); % of critical shared skills with eval harnesses in CI. The convention set itself is owned and revised by the volunteer chapter — conformance is measured against the current agreed set, not against any single named artifact.

### Judgment & governance (KRA 6)

- % of teams with a current documented risk policy and autonomy/risk grid.
- Postmortem completion rate for agent-related failures (target 100%); repeat-failure-mode rate trending down.
- % of autonomous flows with cost limits, alerting, and rollback defined before launch (target 100%); agent spend within budget per team.
- Judgment & Oversight dimension median ≥ AF3 function-wide — the leading indicator that adoption isn't outrunning safety.

### Program leverage (KRA 7)

- Measurable productivity evidence to feed the org program: documented time-on-task reductions on recurring jobs vs. pre-agent baselines (the rubric's own evidence category), sampled per team per quarter.
- **Stretch:** chapter playbook published and adopted by the next function chapter with <X weeks of Engineering Chapter Lead time required. This goes beyond the core engineering mandate — it is a stretch goal, not a baseline expectation for this lead.

