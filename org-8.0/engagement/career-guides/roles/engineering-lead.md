# Engineering Lead (EL) — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#engineering-lead-el)

---

## 1. Success in the Role

### First 90 Days (or First Increment)

- **Understand your squad's context:** Are you leading a CP Squad, Studio Squad, or PL Squad? Each context has different concerns. CP Squad ELs deal with customer-specific integration; Studio Squad ELs deal with reusable component design; PL Squad ELs deal with platform capability under Engagement demand. Know which archetype is in use, what the EA's gap analysis says for your squad's scope, and what the AVA requires from your squad's assembly-impacting work.
- **Align with EA on quality standards:** EA sets the engineering quality standards across the Engagement — architecture decisions, coding standards for architecture-significant concerns, mandatory review, inner source quality gates. You are responsible for meeting these standards within your squad. Understand what qualifies as "architecture-significant" (triggering EA mandatory review) and what qualifies as "assembly-impacting" (triggering AVA mandatory review). If the scope is unclear, clarify with EA and AVA before the first sprint, not after the first review failure.
- **Establish the squad cadence:** Work with the Scrum Master (if assigned) to set up ceremonies. Work with the Squad PM to establish the backlog and initial prioritisation. Your squad may be newly assembled from different Product Line contexts — establish rhythm fast.
- **Connect to the integrated view:** EPM owns the integrated progress view. You feed it — squad-level scope, timeline, risks, blockers, dependencies. Design a reporting cadence that gives EPM what they need without consuming your squad's time.
- **Plan for inner source:** EA prioritises inner source contributions. Include them in sprint capacity from the start. If you plan sprints without inner source overhead, the first inner source assignment will feel like a surprise.

### What "Good" Looks Like

- Your squad delivers on commitments — scope, timeline, quality. When commitments are at risk, you flag early to EPM with impact and options.
- Architecture-significant and assembly-impacting work is reviewed by EA and AVA respectively *before* completion. This is part of your squad's Definition of Done — not an afterthought.
- Inner source contributions are planned into sprint capacity and executed at the quality bar PL Maintainers expect. If the bar is unreachable within a sprint, you have discussed alternatives with EA before the sprint ends, not after.
- Your squad engineers are growing — you provide execution-axis feedback, and you engage with their Engineering Manager (functional axis) so that multi-Engagement career progression is informed by real Engagement experience.
- The Scrum Master facilitates process; you lead engineering. The boundary is respected — you do not manage ceremonies; the Scrum Master does not direct engineering decisions.

### Key Relationships

| Role | What You Need from Them | What They Need from You |
|------|------------------------|------------------------|
| EPM | Cross-squad coordination, staffing support, priority resolution for cross-squad dependencies | Squad-level progress, risks, blockers, dependencies, staffing needs |
| EA | Architecture guidance, mandatory review, quality standards, inner source prioritisation | Architecture-significant work submitted for review, inner source execution, quality standard adherence |
| AVA | Assembly-impacting change review, verification requirements, certification criteria | Assembly-impacting work submitted for review, squad-level testing aligned with verification strategy |
| Squad PM | Backlog management, prioritisation, requirements decomposition | Delivery alignment, sprint capacity, technical input on feasibility |
| Scrum Master | Process facilitation, ceremony management, impediment escalation | Engineering leadership, delivery commitment, process cooperation |
| Engineering Manager (functional axis) | Career guidance, multi-Engagement perspective, designation progression | Execution-axis feedback on engineers, growth observations |

### Performance Input and the Dual Axis

Your functional home is **Engineering**. Engineering leadership evaluates your career growth across Engagement assignments — multi-Engagement delivery record, technical growth, inner source contributions. EPM provides execution-axis input on your squad delivery effectiveness. Request feedback from EA on mandatory review quality and inner source contribution quality. Request feedback from AVA on your squad's assembly-impacting work and testing quality.

---

## 2. Expected Interactions, Tensions, and How to Navigate

### EL ↔ EPM

**Tension:** EPM needs the integrated view and process consistency across squads. You need squad autonomy to deliver effectively. Both are legitimate.

**How to navigate:**
- When EPM and EL disagree on squad-level decisions, **EL prevails** per the [escalation model](../../governance.md#escalation-model). The escalation path is EA (for architecture-related disputes), then EO (for Engagement-level disputes). This authority comes with accountability — if you prevail and the squad misses, it is on you.
- Provide EPM with regular, honest status. The worst outcome is EPM discovering a risk from the customer or Client Partner rather than from you.
- Accept minimum coordination requirements (weekly status, dependency flags, risk escalation). Push back if EPM imposes process that adds overhead without value — but push back through conversation, not through non-compliance.
- When your squad's commitments are at risk, escalate to EPM with impact and options before the deadline passes. Early escalation builds trust; late surprises destroy it.

### EL ↔ EA

**Tension:** EA sets quality standards and requires mandatory review. You own squad delivery and may see these as overhead. Inner source contributions (prioritised by EA) compete with Engagement delivery timelines.

**How to navigate:**
- Include mandatory review and inner source overhead in sprint planning from the start. If they are surprises, the sprint plan was incomplete.
- Submit architecture-significant work for EA review early in the sprint, not at the end. Late submissions create bottlenecks and frustration for both sides.
- When inner source contributions threaten delivery commitments, bring data to EA: effort estimate, PL Maintainer feedback timeline, delivery impact. The trade-off (deliver now with custom build vs. contribute to PL with timeline cost) is a business decision — present it clearly and escalate to EPM if needed.

### EL ↔ AVA

**Tension:** AVA requires mandatory review of assembly-impacting changes and may raise verification requirements that affect your squad's work.

**How to navigate:**
- Understand what qualifies as "assembly-impacting" — integration seams, cross-squad interfaces, configuration correctness, deployment topology. Not every change qualifies. If the scope is unclear, ask AVA.
- AVA's mandatory review should be efficient. If it is slow, provide feedback through EPM. If your submission quality is low (missing context, unclear impact), AVA's review will be slower — invest in clear submissions.

### EL ↔ Squad PM

**Tension:** Squad PM owns what the squad builds and in what order. You own how it is built and whether it is delivered on time. Product vs. delivery tension within the squad.

**How to navigate:**
- Align on sprint commitments jointly. Neither of you should override the other — if the Squad PM wants to prioritise a requirement and you believe it is technically infeasible in the sprint, discuss openly, not through silent deprioritisation.
- Respect the product-process boundary: Squad PM owns backlog priority; Scrum Master owns process; you own engineering leadership and delivery commitment. Three distinct authorities within one squad.

### EL ↔ Scrum Master

**Tension:** Scrum Master facilitates process and may push for process consistency that you see as constraining squad flexibility. You may want to skip ceremonies under delivery pressure.

**How to navigate:**
- Ceremonies and process are how the squad sustains delivery — they are not overhead. When delivery is behind, the answer is rarely "skip the retro" and usually "use the retro to fix the bottleneck."
- If you and the Scrum Master disagree on process, the escalation path is through EPM. EPM sets process expectations for the Engagement.

---

## 3. Escalation: Dos and Don'ts

**Do:**

- Escalate cross-squad dependencies and blockers to **EPM** — EPM coordinates across squads ([governance.md](../../governance.md#escalation-model)).
- Escalate architecture disputes to **EA** (architecture), then to **EPM** if unresolved.
- Escalate delivery commitment risks to **EPM** early, with impact and options.
- Provide execution-axis feedback on engineers to their **Engineering Manager** (functional axis). Multi-Engagement career development depends on this input.

**Don't:**

- Override EA's quality standards or skip mandatory review under delivery pressure. If the standards are unreasonable, escalate — don't silently bypass.
- Override AVA's assembly-impacting review requirement. Submit the work; if AVA is slow, escalate through EPM.
- Independently approach PL Squad leads for staffing. Staffing coordination goes through PPM to avoid multiple Engagements competing for the same capacity. Work through EPM and PPM.
- Absorb Scrum Master process responsibilities. You own engineering leadership; Scrum Master owns process facilitation. If you are running standups and retros, something is wrong.

---

## 4. Further Learning

**Internal references:**
- [Roles and Responsibilities — EL](../../roles.md#engineering-lead-el)
- [Mandatory Architect Consultation](../../roles.md#mandatory-architect-consultation)
- [Engagement Formation](../../engagement-formation.md) — EL assignment at Stage 2
- [Engineering Function Guide](../functions/engineering.md) — career progression including EL

**External references:**

| Resource | Why Relevant |
|----------|--------------|
| *Team Topologies* — Skelton & Pais ([teamtopologies.com](https://teamtopologies.com/book)) | Squad interaction modes (collaboration, X-as-a-Service, facilitation); directly applicable to understanding how CP/Studio/PL/Verification squads relate |
| *Inner Source Patterns* — InnerSource Commons ([innersourcecommons.org](https://innersourcecommons.org/learn/patterns/)) | Practical patterns for cross-team contribution; applicable to EL's responsibility for executing inner source contributions within the squad |
| *Software Product Lines: Practices and Patterns* — Clements & Northrop ([SEI](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=5765)) | PLE foundations; helps ELs understand the "extend, don't fork" discipline driving inner source decisions |

---

[← Back to Career Guides](../README.md)
