# Scrum Master — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#scrum-master)

---

## 1. Success in the Role

### First 90 Days (or First Increment)

- **Assess your squads:** You may serve 1-3 squads. Each squad has a different context (CP, Studio, PL), a different EL, different team dynamics, and may be at a different maturity level. Before imposing any process, observe each squad's current cadence and working style. Adaptation to context is more valuable than uniform process.
- **Establish ceremonies:** Set up sprint planning, standups, retrospectives, and demos for each squad. Agree with each EL on ceremony cadence and format. Be prepared to adapt — a CP Squad that is deep in customer-specific integration may need different cadence than a PL Squad maintaining platform components.
- **Align with EPM:** EPM sets process expectations for the Engagement. Understand what minimum coordination EPM requires (e.g. sprint cadence alignment, dependency flagging, retrospective outputs). You are the process link between EPM and the squads.
- **Learn the product-process boundary:** You facilitate process; the Squad PM manages product (backlog, priority); the EL manages engineering and delivery. All three authorities operate within the same squad — your success depends on respecting these boundaries.
- **Note: Verification Squad exception:** The Verification Squad does not have a Scrum Master. AVA directs through architectural authority. If you are assigned to squads that include a Verification Squad, that squad is outside your scope.

### What "Good" Looks Like

- Ceremonies happen on cadence and are effective — sprint planning produces clear commitments; retrospectives produce actionable improvements; standups surface blockers early.
- Impediments are identified and escalated promptly. You do not solve every impediment yourself — you identify, categorise (squad-level vs. cross-squad vs. Engagement-level), and escalate to the right person (EL for squad-level, EPM for cross-squad, EO for Engagement-level).
- Team health is monitored. You notice workload imbalance, collaboration friction, or morale issues before they become crises. You surface them to EL and EPM with observations, not diagnoses.
- Process is consistent enough across your squads that EPM can maintain the integrated view, but flexible enough that each squad works effectively in its own context.
- When serving multiple squads, you surface common impediments and alignment opportunities to EPM — you are the cross-squad process radar.

### Key Relationships

| Role | What You Need from Them | What They Need from You |
|------|------------------------|------------------------|
| EL(s) | Engineering leadership, delivery commitments, cooperation on process | Process facilitation, ceremony management, impediment identification, team health monitoring |
| Squad PM(s) | Product input for ceremonies, backlog context | Process facilitation (sprint planning, review), cadence management |
| EPM | Process expectations, cross-squad alignment context, Engagement-level impediment resolution | Cross-squad process observations, impediment escalation, team health signals |
| Engineers | Participation in ceremonies, impediment reporting | Effective facilitation, protected ceremony time, impediment follow-through |

### Performance Input and the Dual Axis

Your functional home is **Program / Delivery Management**. Delivery leadership evaluates your career growth across Engagements — process facilitation skill, multi-squad experience, cross-functional coordination. EPM provides execution-axis input on your process effectiveness within the Engagement. Request feedback from ELs on facilitation quality and from engineers on ceremony usefulness.

---

## 2. Expected Interactions, Tensions, and How to Navigate

### Scrum Master ↔ EL

**Tension:** You want process consistency and ceremony discipline. EL wants squad flexibility and may see ceremonies as overhead, especially under delivery pressure.

**How to navigate:**
- When delivery is behind, the answer is rarely "skip the retro." It is usually "use the retro to find and fix the bottleneck." Advocate for process as a delivery enabler, not as bureaucratic compliance.
- Each EL has a different style. Adapt your facilitation to the EL's squad without abandoning the minimum coordination requirements EPM has set. Uniform process across all squads is not the goal — effective process in each squad is.
- If an EL consistently resists process (skips ceremonies, ignores cadence), discuss directly first. If unresolved, escalate to EPM. EPM owns process expectations for the Engagement.

### Scrum Master ↔ Squad PM

**Tension:** Product decisions (what to build, priority) and process decisions (how the sprint runs) overlap in practice, especially during sprint planning. The Squad PM may want to control the ceremony flow to drive a product outcome.

**How to navigate:**
- You facilitate; Squad PM provides content. In sprint planning, the Squad PM presents the prioritised backlog; you manage the discussion, the timebox, and the commitment. If the Squad PM is running the meeting, gently reclaim facilitation.
- If a product-process disagreement arises (e.g. Squad PM wants to skip the demo to gain a sprint day), discuss the trade-off and escalate to EPM if needed.

### Scrum Master Across Multiple Squads

**Tension:** Serving 2-3 squads with different ELs, different cadences, and different maturity levels requires context-switching and adaptation. Each squad may feel that you are not fully present.

**How to navigate:**
- Stagger ceremonies so you are fully present for each. If squads' schedules conflict, resolve with ELs rather than multitasking across simultaneous ceremonies.
- Surface common patterns across squads to EPM — if two squads share the same impediment (e.g. PL Maintainer review capacity), raising it once at the EPM level is more effective than solving it twice at squad level.
- Be transparent with each squad about your multi-squad assignment. They will respect boundaries if they understand the constraint.

### Scrum Master ↔ EPM

**Tension:** EPM sets process expectations for the Engagement. You implement them at squad level. EPM may push for consistency; you may push for squad-specific adaptation.

**How to navigate:**
- Understand the minimum coordination requirements EPM has set and meet them consistently. Beyond the minimum, adapt to each squad's context.
- Use your cross-squad perspective as a contribution to EPM's integrated view. You see process health, team dynamics, and impediment patterns across squads — EPM sees scope, timeline, and risk. Together, the view is more complete.

---

## 3. Escalation: Dos and Don'ts

**Do:**

- Escalate impediments that squads cannot resolve internally to **EPM** — EPM coordinates across squads and has Engagement-level authority.
- Escalate team health concerns (workload imbalance, collaboration friction, morale) to **EL** first, then to **EPM** if EL cannot address.
- Escalate process disagreements with ELs to **EPM** — EPM sets process expectations for the Engagement ([governance.md](../../governance.md#escalation-model)).

**Don't:**

- Direct engineering work. You facilitate process; EL directs engineering. If you find yourself making technical decisions or prioritising backlog items, you have crossed the boundary.
- Skip escalation to fight impediments you cannot solve yourself. Your value is in identification and escalation, not in solving every blocker personally.
- Impose uniform process across squads without regard for context. A PL Squad maintaining a stable platform needs different ceremony intensity than a CP Squad integrating a new customer deployment. Adapt.
- Escalate directly to EO without going through EPM first. EPM is your execution-axis reporting line and the first escalation point for process and coordination issues.

---

## 4. Further Learning

**Internal references:**
- [Roles and Responsibilities — Scrum Master](../../roles.md#scrum-master)
- [Engagement Formation](../../engagement-formation.md) — Scrum Master staffing at Stage 3
- [Governance and Escalation](../../governance.md) — escalation model for SM ↔ EL disputes
- [Program / Delivery Function Guide](../functions/program-delivery.md) — career progression from Scrum Master toward EPM

**External references:**

| Resource | Why Relevant |
|----------|--------------|
| *Nexus Framework* — Bittner et al. ([scrum.org](https://www.scrum.org/resources/scaling-scrum)) | Multi-team Scrum coordination; directly applicable to serving 2-3 squads and coordinating with EPM on cross-squad process |
| *Agile and Lean Program Management* — Rothman ([jrothman.com](https://www.jrothman.com/books/agile-and-lean-program-management-scaling-collaboration-across-the-organization/)) | Scaling collaboration across teams; helps Scrum Masters understand the EPM's perspective and how squad-level process feeds the integrated view |

---

[← Back to Career Guides](../README.md)
