# Squad Product Manager (Squad PM) — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#squad-product-manager-squad-pm)

---

## 1. Success in the Role

### First 90 Days (or First Sprint)

- **Understand the requirements flow:** EPO produces Engagement-level requirements; you decompose them into your squad's backlog. Meet EPO early to understand the requirements landscape, the customer context, and where your squad's scope sits within the overall Engagement.
- **Build the backlog:** Populate the squad backlog with requirements from EPO, inner source contributions prioritised by EA, verification requirements from AVA, and any tech debt identified by the EL. Each backlog item needs clear acceptance criteria — if an engineer cannot tell when it is done, the item is not ready.
- **Align with the EL:** You own what the squad builds and in what order. EL owns how it is built and whether delivery commitments are met. Agree on sprint commitment jointly — neither of you should override the other silently.
- **Coordinate with the Scrum Master:** The Scrum Master facilitates process; you manage product. Distinguish clearly: you decide *what* to build; the Scrum Master decides *how the process runs*. If you find yourself managing ceremonies, you have crossed the boundary.
- **Learn the competing inputs:** Your backlog has multiple sources: EPO requirements, EA inner source, AVA verification, and tech debt. Each is legitimate. Prioritisation is your job — make the trade-offs transparent to EL and EPM, not hidden.

### What "Good" Looks Like

- The squad backlog is current, prioritised, and ready for engineering. Engineers rarely block on unclear requirements.
- Prioritisation trade-offs are transparent. EPM and EL can see why a requirement is prioritised ahead of inner source or tech debt — and vice versa. No hidden agenda.
- Requirements flow from EPO is smooth — you can decompose independently within a well-defined scope. You ask EPO for clarification when needed, not for permission on every item.
- Progress and blockers are communicated to EPM through the EL and the integrated view. EPM does not need to ask you directly for status — it flows through the coordination mechanism.
- The product-process boundary with the Scrum Master is clear and respected.

### Key Relationships

| Role | What You Need from Them | What They Need from You |
|------|------------------------|------------------------|
| EPO | Engagement-level requirements, priority guidance, acceptance criteria clarification | Decomposed squad backlog, requirements delivery progress, discovery feedback from implementation |
| EL | Delivery commitment, technical feasibility input, sprint capacity | Prioritised backlog, clear acceptance criteria, trade-off transparency |
| Scrum Master | Process facilitation, ceremony management, impediment escalation | Product input for ceremonies (sprint planning, review), cooperation on cadence |
| EA | Inner source priorities, mandatory review scope, architecture-significant context | Inner source items in backlog, architecture-significant work flagged for review |
| AVA | Verification requirements, assembly-impacting change context | Verification items in backlog, assembly-impacting work flagged for review |
| EPM | Cross-squad coordination context, integrated view | Squad-level progress (through EL), dependency flags, scope change alerts |

### Performance Input and the Dual Axis

Your functional home is **Product Management**. Product leadership evaluates your career growth across Engagements — backlog management quality, requirements decomposition skill, cross-squad thinking. EL provides execution-axis input on your effectiveness within the squad. Request feedback from EPO on your requirements decomposition quality and from the Scrum Master on your product-process boundary respect.

---

## 2. Expected Interactions, Tensions, and How to Navigate

### Squad PM ↔ EPO

**Tension:** EPO sets Engagement-level requirements; you decompose and prioritise within your squad. EPO may produce requirements that are too vague to decompose, or may produce too many requirements for your squad's capacity.

**How to navigate:**
- Push back on vague requirements before putting them in the backlog. If an engineer cannot tell when it is done, ask EPO for clarification — do not fill in the gaps yourself (you may misinterpret the customer intent).
- When capacity is insufficient for all EPO requirements, surface the trade-off to EPO and EPM. The prioritisation within the squad is your decision; the Engagement-level priority is EPO's and EPM's.
- If requirements change during Build (and they will), coordinate with EPO and EPM before updating the backlog. Silent changes create cascading surprises.

### Squad PM ↔ EL

**Tension:** You own what gets built; EL owns how it gets built and the delivery commitment. Product priority and engineering feasibility sometimes conflict.

**How to navigate:**
- Agree on sprint commitments jointly in sprint planning. If you want to prioritise a high-effort requirement and EL believes it is not feasible within the sprint, discuss openly. The Scrum Master facilitates this discussion.
- Respect EL's technical judgment on feasibility. If EL says inner source will take three sprints, take it seriously — EL has PL Maintainer feedback that you may not have.
- When EA-prioritised inner source competes with your EPO-sourced requirements, present the trade-off to EL transparently. The resolution may need to go to EPM.

### Squad PM ↔ Scrum Master

**Tension:** You make product decisions (what to build, in what order). The Scrum Master makes process decisions (how to run the sprint). Overlap happens — sprint planning, for example, involves both product priority and process management.

**How to navigate:**
- Let the Scrum Master facilitate. You provide the content (prioritised backlog, acceptance criteria, trade-off context); the Scrum Master manages the conversation, the timebox, and the outcome.
- If you disagree with a process decision (e.g. ceremony format, cadence), discuss with the Scrum Master. If unresolved, the escalation path is through EPM.

### Squad PM ↔ EA / AVA

**Tension:** EA inner source priorities and AVA verification requirements compete for your backlog space alongside EPO requirements.

**How to navigate:**
- Include EA inner source items and AVA verification requirements in the backlog as first-class items, not as "other work." They have priority just like EPO requirements.
- When these competing inputs exceed sprint capacity, make the trade-off visible: "If we take inner source item X, we defer EPO requirement Y. If we take EPO requirement Y, inner source contribution slips." Present this to EL and, if needed, to EPM.

---

## 3. Escalation: Dos and Don'ts

**Do:**

- Escalate requirements clarity issues to **EPO** — if requirements are too vague, ask for clarification before putting them in the backlog.
- Escalate cross-squad requirements dependencies to **EPM** (through EL) — EPM coordinates across squads.
- Escalate inner source vs. requirements prioritisation conflicts to **EPM** when EL and EA cannot resolve.

**Don't:**

- Override EL on technical feasibility. You own priority; EL owns feasibility. If you disagree, discuss; if unresolved, both escalate to EPM.
- Manage process (ceremonies, cadence, impediment removal). That is the Scrum Master's role. If you are running standups, the boundary has broken.
- Change backlog priorities silently during Build without coordinating with EPO and EPM. Every change may have commercial, architecture, or cross-squad implications.
- Deprioritise EA inner source or AVA verification items without raising the trade-off. These items have Engagement-level implications; silent deprioritisation creates risks that surface at certification or release.

---

## 4. Further Learning

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
