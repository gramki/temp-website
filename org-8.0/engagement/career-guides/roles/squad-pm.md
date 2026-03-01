# Squad Product Manager (Squad PM) — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#squad-product-manager-squad-pm)

---

The Squad PM is a **product role at the squad level** — owning the squad backlog, prioritisation, and requirements decomposition. The Squad PM is not a process role; process facilitation belongs to the Scrum Master. The role is scoped **per-squad**. The Squad PM reports to EL within the squad on the execution axis. The functional home is **Product Management**.

---

## 1. Empowerment

- **Backlog ownership.** You own the squad backlog — all work items, their priority, and their acceptance criteria. This includes EPO requirements, EA inner source contributions, AVA verification requirements, and tech debt.
- **Prioritisation within the squad.** You determine what the squad builds and in what order, in coordination with the EL. Neither of you overrides the other silently.
- **Requirements decomposition.** You break EPO-level requirements into squad-executable work items with clear acceptance criteria.
- **What you cannot override.** You cannot override EL on technical feasibility. You cannot deprioritise EA inner source or AVA verification items without raising the trade-off to EPM. You do not own process — that is the Scrum Master's domain.

---

## 2. Assignment

EO assigns Squad PMs at **Stage 2**, staffed through PPM at **Stage 3** ([engagement-formation.md](../../engagement-formation.md#stage-3--squad-staffing-through-ppm-at-discover)). Squad PMs are drawn from the Product Management function.

**Scope:** Per-squad.

---

## 3. Ambition

### First 90 Days (or First Sprint)

- **Understand the requirements flow.** EPO produces Engagement-level requirements; you decompose them into your squad's backlog. Meet EPO early to understand the requirements landscape, the customer context, and where your squad's scope sits within the overall Engagement.
- **Build the backlog.** Populate the squad backlog with requirements from EPO, inner source contributions prioritised by EA, verification requirements from AVA, and any tech debt identified by the EL. Each backlog item needs clear acceptance criteria.
- **Align with the EL.** You own what the squad builds and in what order. EL owns how it is built and whether delivery commitments are met. Agree on sprint commitment jointly.
- **Coordinate with the Scrum Master.** The Scrum Master facilitates process; you manage product. You decide *what* to build; the Scrum Master decides *how the process runs*.
- **Learn the competing inputs.** Your backlog has multiple sources: EPO requirements, EA inner source, AVA verification, and tech debt. Each is legitimate. Prioritisation is your job — make the trade-offs transparent.

### What Great Looks Like

- The squad backlog is current, prioritised, and ready for engineering. Engineers rarely block on unclear requirements.
- Prioritisation trade-offs are transparent. EPM and EL can see why a requirement is prioritised ahead of inner source or tech debt — and vice versa.
- Requirements flow from EPO is smooth — you can decompose independently within a well-defined scope.
- Progress and blockers are communicated to EPM through the EL and the integrated view.
- The product-process boundary with the Scrum Master is clear and respected.

---

## 4. Commitments

### Dimensions

| Dimension | Squad PM SLA |
|---|---|
| **Predictability** | The squad backlog is ready for sprint planning — items are prioritised, acceptance criteria are defined, and EL can estimate confidently. Sprint commitment accuracy is high because backlog quality is high. When requirements change during Build, the change is coordinated with EPO and EPM before the backlog is updated. |
| **Velocity** | Requirements decomposition is timely — Squad PMs are never the bottleneck between EPO's Engagement-level requirements and engineering work. Backlog grooming keeps the pipeline of ready work ahead of the squad's consumption rate. |
| **Fitment** | Decomposition accuracy — squad-level work items faithfully reflect EPO's requirements and the customer's actual need. When multiple inputs compete for backlog space (EPO requirements, EA inner source, AVA verification, tech debt), the trade-off is visible and defensible. |

### Contractual Connection — Tier 3 (Roll-up)

The Squad PM does not interface with the contract. Squad PM SLAs aggregate upward through EL and EPM to the Engagement-level commitments. When the backlog is well-managed and decomposition is accurate, the squad delivers what was promised and the Engagement meets its contractual obligations.

---

## 5. Collaboration

### Key Relationships

| Role | What You Need from Them | What They Need from You |
|------|------------------------|------------------------|
| EPO | Engagement-level requirements, priority guidance, acceptance criteria clarification | Decomposed squad backlog, requirements delivery progress, discovery feedback from implementation |
| EL | Delivery commitment, technical feasibility input, sprint capacity | Prioritised backlog, clear acceptance criteria, trade-off transparency |
| Scrum Master | Process facilitation, ceremony management, impediment escalation | Product input for ceremonies (sprint planning, review), cooperation on cadence |
| EA | Inner source priorities, mandatory review scope, architecture-significant context | Inner source items in backlog, architecture-significant work flagged for review |
| AVA | Verification requirements, assembly-impacting change context | Verification items in backlog, assembly-impacting work flagged for review |
| EPM | Cross-squad coordination context, integrated view | Squad-level progress (through EL), dependency flags, scope change alerts |

### Tensions and Navigation

**Squad PM ↔ EPO.** EPO sets Engagement-level requirements; you decompose and prioritise within your squad. EPO may produce requirements that are too vague to decompose, or too many for your squad's capacity.

- Push back on vague requirements before putting them in the backlog. If an engineer cannot tell when it is done, ask EPO for clarification.
- When capacity is insufficient for all EPO requirements, surface the trade-off to EPO and EPM.
- If requirements change during Build, coordinate with EPO and EPM before updating the backlog.

**Squad PM ↔ EL.** You own what gets built; EL owns how it gets built and the delivery commitment.

- Agree on sprint commitments jointly in sprint planning.
- Respect EL's technical judgement on feasibility. If EL says inner source will take three sprints, take it seriously.
- When EA-prioritised inner source competes with EPO-sourced requirements, present the trade-off transparently.

**Squad PM ↔ Scrum Master.** You make product decisions (what to build, in what order). The Scrum Master makes process decisions (how to run the sprint).

- Let the Scrum Master facilitate. You provide content (prioritised backlog, acceptance criteria, trade-off context); the Scrum Master manages the conversation, the timebox, and the outcome.

**Squad PM ↔ EA / AVA.** EA inner source priorities and AVA verification requirements compete for backlog space alongside EPO requirements.

- Include EA inner source items and AVA verification requirements in the backlog as first-class items, not as "other work."
- When competing inputs exceed sprint capacity, make the trade-off visible and escalate to EPM if needed.

---

## 6. Management

### Dual-Axis Reporting

- **Execution axis:** Reports to **EL** (within squad). EL provides execution-axis input on your effectiveness within the squad.
- **Functional/career axis:** **Product leadership** evaluates your career growth across Engagements — backlog management quality, requirements decomposition skill, cross-squad thinking.

### Performance Input

Request feedback from EPO on your requirements decomposition quality and from the Scrum Master on your product-process boundary respect. EL provides day-to-day execution feedback. Product leadership evaluates your trajectory toward EPO — the Squad PM role is the primary developmental path for future EPOs.

---

## 7. Accountability

### Escalation: Dos and Don'ts

**Do:**

- Escalate requirements clarity issues to **EPO** — if requirements are too vague, ask for clarification before putting them in the backlog.
- Escalate cross-squad requirements dependencies to **EPM** (through EL) — EPM coordinates across squads.
- Escalate inner source vs. requirements prioritisation conflicts to **EPM** when EL and EA cannot resolve.

**Don't:**

- Override EL on technical feasibility. You own priority; EL owns feasibility. If you disagree, discuss; if unresolved, both escalate to EPM.
- Manage process (ceremonies, cadence, impediment removal). That is the Scrum Master's role.
- Change backlog priorities silently during Build without coordinating with EPO and EPM.
- Deprioritise EA inner source or AVA verification items without raising the trade-off. These items have Engagement-level implications.

### When Commitments Are Missed

Squad PM commitments are primarily **commitment-based** (per the [accountability framework](../../people-and-culture/accountability.md)): backlog readiness, decomposition timeliness, and transparent trade-off communication are binary. When the squad enters sprint planning with an unprepared backlog (vague items, missing acceptance criteria), that is a reliability failure. When a trade-off is hidden (inner source was silently deprioritised), that is a transparency failure.

However, decomposition accuracy — whether the squad-level work items faithfully reflect the customer's need — is **outcome-based**. As the team learns more during Build, decomposition improves. The Squad PM's judgement is evaluated by trajectory, not by getting every decomposition right on the first attempt.

---

## 8. Objectives in Perspective

The Squad PM's immediate objectives — backlog management, prioritisation, requirements decomposition — seem tactical, but they underpin the entire Engagement delivery chain. When the backlog is well-managed, engineers work efficiently, the EL can commit reliably, and EPM can forecast accurately.

The trade-offs you make in the backlog — between EPO requirements, EA inner source, AVA verification, and tech debt — are micro-decisions that aggregate into Engagement-level outcomes. When you prioritise inner source contributions, you extend the platform. When you prioritise verification requirements, you enable AVA to certify the assembly. When you prioritise customer requirements, you deliver the Engagement's purpose.

No single prioritisation is always right. The Squad PM who makes these trade-offs transparently — so that EL, EPM, and EPO can see and challenge them — has done the job. The Squad PM who hides trade-offs has created surprises that surface at certification or release.

---

## Further Learning

**Internal references:**
- [Roles and Responsibilities — Squad PM](../../roles.md#squad-product-manager-squad-pm)
- [Governance and Escalation](../../governance.md) — escalation model for Squad PM ↔ EPO disputes
- [Product Management Function Guide](../functions/product-management.md) — career progression through Squad PM to EPO
- [Engagement Formation](../../engagement-formation.md) — Squad PM staffing at Stage 3

**External references:**

| Resource | Why Relevant |
|----------|--------------|
| *Inspired: How to Create Tech Products Customers Love* — Cagan ([svpg.com](https://www.svpg.com/inspired-how-to-create-tech-products-customers-love/)) | Product discovery and delivery fundamentals; applicable to backlog ownership and requirements decomposition |
| *Continuous Discovery Habits* — Torres ([producttalk.org](https://www.producttalk.org/continuous-discovery-habits/)) | Structured discovery habits; helps Squad PMs develop the customer empathy that makes requirements decomposition more effective |

---

[← Back to Career Guides](../README.md)
