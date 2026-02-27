# PLE Rollout Plan

## Overview

Zeta adopts Product Line Engineering in three phases:

- **Phase 0: Foundation** (Weeks 1–4) — Governance setup, leadership alignment, naming, stakeholder analysis
- **Phase 1: Launch & Pilot** (Weeks 5–12) — Pilot engagements, first archetype, inner source setup; **Launch and Pilot complete within one quarter**
- **Phase 2+: Expand & Steady State** (Week 13+) — All new Engagements follow PLE; existing engagements migrate gradually; continuous improvement

Because engagement volume is not high, Phase 2 and Phase 3 (Expand and Steady State) are merged: we expand and operate in steady state as one ongoing phase.

---

## Phase 0: Foundation (Weeks 1–4)

**Objective:** Establish governance, align leadership, prepare for change.

| Workstream | Activities | Owner | Output |
|------------|------------|-------|--------|
| **Executive Alignment** | Define vision, success metrics, risk tolerance; align on org structure | Engineering Leadership | PLE Charter (or equivalent) |
| **Governance Setup** | Form Platform Architecture Council; define initial membership | Engineering Leadership | Council charter, initial members |
| **Stakeholder Analysis** | Map concerns (by role) to teams/individuals; plan communication | HR + Engineering Leadership | Stakeholder concern matrix |
| **Naming Decision** | Finalize terminology (Product Line Engineering, Engagement Engineering, Customer Product, etc.) | Leadership + Council | Approved terminology |

**Key decision points:**

- Confirm org structure (Product Line Squads, Engagement Engineering, ERC, Council/PAC, SRE)
- Confirm naming (Product Line Engineer, Product Line Maintainer, Customer Product Squad, Customer Product)
- Select pilot engagement(s) for Phase 1

**Success criteria:**

- Council formed and charter published
- Stakeholder concern matrix documented
- Naming and structure communicated to engineering

---

## Phase 1: Launch & Pilot (Weeks 5–12)

**Objective:** Test the model on 1–2 new Engagements; learn and adjust. **Complete within the first quarter.**

| Workstream | Activities | Owner | Output |
|------------|------------|-------|--------|
| **Pilot Engagement Selection** | Choose 1–2 new Engagements that fit an existing archetype; not too complex, not too simple | ERC + Engagement Architects | Selected pilots |
| **Team Composition** | Compose pilot Customer Product Squads per new model; document rotation agreements | Product Line Squad Leads + EPM + PPM | Staffing plan with return/rotation dates |
| **Archetype Development** | Develop or formalize one solution archetype (blueprint, cookbook, playbook) for the pilot | Engagement Architects | First archetype package |
| **Inner Source Setup** | Define DoD, PR review process, Maintainer assignments for platforms involved | Product Line Squad Leads + Council | Inner source guidelines (or updates) |
| **Operating Model Selection** | Select operating model for pilot; document in engagement contract | EPM + EA + Customer | Operating model agreement |
| **Execute Pilot** | Run engagement using new model; weekly or bi-weekly retrospectives | EO + EPM + ELs | Pilot delivery + learnings |

**Parallel: Stakeholder communication**

| Audience | Message | Format | Timing |
|----------|----------|--------|--------|
| All Engineering | Why PLE, what it means for you, what’s changing | Town hall + Q&A | Week 5 |
| Product Line Squads | Rotation model, inner source expectations, capacity implications | Team meetings | Week 6 |
| Engagement Architects | Archetype ownership, engagement portfolio, authority | Working session | Week 6 |
| EOs, EPMs, and ELs | New model, team composition, accountability | Working session | Week 6 |

**Key metrics to track:**

- Time to compose team
- PR review cycle time (inner source)
- Engagement velocity (vs. comparable past engagements)
- Team member satisfaction (pulse survey)
- Quality of knowledge capture (retrospectives, archetype updates)

**Success criteria:**

- Pilot engagement(s) delivered using PLE model
- First archetype in use and documented
- Inner source in practice with at least one merged PR (or documented learnings)
- Retrospectives and learnings documented; process refinements identified

---

## Phase 2+: Expand & Steady State (Week 13+)

**Objective:** All new Engagements follow PLE; existing engagements migrate gradually; continuous improvement. No separate “Phase 3”; expand and steady state are one ongoing phase.

| Workstream | Activities | Owner | Output |
|------------|------------|-------|--------|
| **New Engagement Rollout** | All new Engagements follow PLE (team composition, archetypes, inner source, variability documentation) | EOs + EPMs + ERC | Consistent new Engagements |
| **Existing Engagement Migration** | Select 2–3 existing engagements for gradual migration; document migration playbook | EOs + EPMs + ELs | Migration playbook; migrated engagements |
| **Process Refinement** | Incorporate pilot learnings; update guidelines, blueprints, cookbooks, playbooks | Council + Engagement Architects | Refined process docs |
| **Archetype Expansion** | Develop 2–3 additional archetypes based on engagement pipeline | Engagement Architects | Archetype library |
| **Inner Source Scaling** | Expand Maintainer pool; establish or refine PR review SLAs | Product Line Squad Leads | Scaled inner source |
| **Council Cadence** | Monthly Practice Mode sessions; Governance Mode as needed | Council | Regular knowledge sharing and governance |
| **Variability Governance** | Quarterly variability review; document and govern configuration points | Council + Engagement Architects | Variability model and docs |
| **Career Path Communication** | Document and communicate Product Line depth vs. Customer Product breadth; recognition for inner source and archetypes | HR + Engineering Leadership | Career path docs |

**Key metrics:**

- Proportion of new Engagements following PLE
- Time to compose team (trend)
- Inner source health (PR cycle time, merge rate, tech debt trend)
- Archetype reuse rate
- Variability documentation coverage
- Customer satisfaction and delivery velocity

**Success criteria:**

- All new Engagements operate under PLE model
- Archetype library covers major solution types
- Inner source and variability governance are routine
- Migration playbook exists and at least some existing engagements have migrated

---

## Success Metrics Summary

| Phase | Metrics |
|-------|---------|
| **Phase 0** | Council formed; stakeholder matrix and naming communicated |
| **Phase 1** | Pilot(s) delivered; first archetype in use; inner source in practice; learnings captured |
| **Phase 2+** | New engagements on PLE; archetype reuse; inner source and variability governance sustained; migration in progress |

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| **Resistance or confusion** | Clear communication; executive coaching; address concerns per [Stakeholder Concerns](stakeholder-concerns.md) and [Executive Coaching Guide](executive-coaching-guide.md) |
| **Pilot delay** | Select pilots that are already scoped or imminent; protect pilot capacity |
| **Inner source quality** | DoD and Maintainer governance from day one; tech debt tracking; Council oversight |
| **Capacity crunch** | Engagement forecasting; reserve Product Line Squad capacity; rotation model with return guarantees |
| **Knowledge loss** | Archetypes, retrospectives, Council pattern extraction; rotation for knowledge preservation |

---

## References

- [PLE Overview](../framework/ple-overview.md)
- [Stakeholder Concerns](stakeholder-concerns.md)
- [Executive Coaching Guide](executive-coaching-guide.md)
- [Engagement Lifecycle](../processes/engagement-lifecycle.md)
