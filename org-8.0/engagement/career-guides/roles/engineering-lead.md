# Engineering Lead (EL) — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#engineering-lead-el)

---

The EL is the **per-squad role** responsible for squad delivery commitments — engineering and technical leadership with delivery accountability. The role is scoped **per-squad** (CP Squad, Studio Squad, or PL Squad). The EL reports to EPM on the execution axis. The functional home is **Engineering**.

---

## 1. Empowerment

- **Squad delivery decisions.** You are primarily responsible for squad delivery commitments — scope, timeline, quality. When EPM and EL disagree on squad-level decisions, **EL prevails** (per the [escalation model](../../governance.md#escalation-model)). This authority comes with accountability — if you prevail and the squad misses, it is on you.
- **Technical decisions within the squad.** Engineering and technical leadership within the squad is your domain. You direct engineers and coordinate with the Squad PM.
- **Meeting EA's engineering quality standards.** EA sets the standards; you are responsible for meeting them within your squad — mandatory review compliance, inner source execution, architecture-significant work submitted for review before completion.
- **Staffing input.** You submit staffing requests to PPM (through EPM) and provide execution-axis feedback on engineers to their Engineering Manager (functional axis).
- **What you cannot override.** You cannot override EA's quality standards or skip mandatory review. You cannot override AVA's assembly-impacting review requirement. You cannot independently approach PL Squad leads for staffing — staffing goes through PPM.

---

## 2. Assignment

EO assigns ELs at **Stage 2** ([engagement-formation.md](../../engagement-formation.md#stage-2--eo-assigns-squad-level-leadership-at-initiate--early-discover)). One EL per functional squad. The **Exploration Lead is the preferred candidate for CP Squad EL** when they continue from Exploration. ELs are drawn from the Engineering function.

**Scope:** Per-squad. Squad types include CP Squad, Studio Squad, and PL Squad(s) contributing to the Engagement.

---

## 3. Ambition

### First 90 Days (or First Increment)

- **Understand your squad's context.** Are you leading a CP Squad, Studio Squad, or PL Squad? Each context has different concerns. Know which archetype is in use, what the EA's gap analysis says for your squad's scope, and what the AVA requires from your squad's assembly-impacting work.
- **Align with EA on quality standards.** Understand what qualifies as "architecture-significant" (triggering EA mandatory review) and what qualifies as "assembly-impacting" (triggering AVA mandatory review). Clarify with EA and AVA before the first sprint.
- **Establish the squad cadence.** Work with the Scrum Master (if assigned) to set up ceremonies. Work with the Squad PM to establish the backlog and initial prioritisation. Your squad may be newly assembled from different Product Line contexts — establish rhythm fast.
- **Connect to the integrated view.** EPM owns the integrated progress view. You feed it — squad-level scope, timeline, risks, blockers, dependencies. Design a reporting cadence that gives EPM what they need without consuming your squad's time.
- **Plan for inner source.** EA prioritises inner source contributions. Include them in sprint capacity from the start.

### What Great Looks Like

- Your squad delivers on commitments — scope, timeline, quality. When commitments are at risk, you flag early to EPM with impact and options.
- Architecture-significant and assembly-impacting work is reviewed by EA and AVA respectively *before* completion. This is part of your squad's Definition of Done.
- Inner source contributions are planned into sprint capacity and executed at the quality bar PL Maintainers expect.
- Your squad engineers are growing — you provide execution-axis feedback, and you engage with their Engineering Manager (functional axis) so multi-Engagement career progression is informed by real Engagement experience.
- The Scrum Master facilitates process; you lead engineering. The boundary is respected.

---

## 4. Commitments

### Dimensions

| Dimension | EL SLA |
|---|---|
| **Quality** | EA's engineering quality standards are met within the squad. Mandatory review compliance — architecture-significant and assembly-impacting work is submitted for EA/AVA review before completion, as part of the squad Definition of Done. Inner source contributions meet PL Maintainer quality gates. |
| **Predictability** | Sprint commitments are met. When they are at risk, early warning is delivered to EPM with impact and options — before the sprint ends, not after. Dependencies on other squads are flagged through the EPM coordination mechanism. |
| **Velocity** | Squad throughput is sufficient for the Engagement's needs. Impediments within the squad are resolved; impediments beyond the squad are escalated to EPM. Inner source overhead is planned into capacity, not treated as a surprise. |

### Contractual Connection — Tier 3 (Roll-up)

The EL does not interface with the contract. EL SLAs aggregate upward through EPM to the Engagement-level commitments. When every squad meets its Predictability and Velocity SLAs, the EPM can forecast reliably and the Engagement meets its milestones. When every squad meets its Quality SLAs, the AVA can certify the assembly and the client receives a product that works.

---

## 5. Collaboration

### Key Relationships

| Role | What You Need from Them | What They Need from You |
|------|------------------------|------------------------|
| EPM | Cross-squad coordination, staffing support, priority resolution for cross-squad dependencies | Squad-level progress, risks, blockers, dependencies, staffing needs |
| EA | Architecture guidance, mandatory review, quality standards, inner source prioritisation | Architecture-significant work submitted for review, inner source execution, quality standard adherence |
| AVA | Assembly-impacting change review, verification requirements, certification criteria | Assembly-impacting work submitted for review, squad-level testing aligned with verification strategy |
| Squad PM | Backlog management, prioritisation, requirements decomposition | Delivery alignment, sprint capacity, technical input on feasibility |
| Scrum Master | Process facilitation, ceremony management, impediment escalation | Engineering leadership, delivery commitment, process cooperation |
| Engineering Manager (functional axis) | Career guidance, multi-Engagement perspective, designation progression | Execution-axis feedback on engineers, growth observations |

### Tensions and Navigation

**EL ↔ EPM.** EPM needs the integrated view and process consistency across squads. You need squad autonomy to deliver effectively. Per the [escalation model](../../governance.md#escalation-model), when EPM and EL disagree on squad-level decisions, **EL prevails** — the escalation path is EA (for architecture-related disputes), then EO.

- Provide EPM with regular, honest status. The worst outcome is EPM discovering a risk from the customer or Client Partner rather than from you.
- Accept minimum coordination requirements (weekly status, dependency flags, risk escalation). Push back if EPM imposes process that adds overhead without value — but through conversation, not non-compliance.
- When your squad's commitments are at risk, escalate to EPM with impact and options before the deadline passes.

**EL ↔ EA.** EA sets quality standards and requires mandatory review. Inner source contributions (prioritised by EA) compete with delivery timelines.

- Include mandatory review and inner source overhead in sprint planning from the start.
- Submit architecture-significant work for EA review early in the sprint, not at the end.
- When inner source contributions threaten delivery commitments, bring data to EA and escalate to EPM if needed.

**EL ↔ AVA.** AVA requires mandatory review of assembly-impacting changes and may raise verification requirements that affect your squad's work.

- Understand what qualifies as "assembly-impacting." If the scope is unclear, ask AVA.
- AVA's mandatory review should be efficient. If it is slow, provide feedback through EPM.

**EL ↔ Squad PM.** Squad PM owns what the squad builds and in what order. You own how it is built and whether it is delivered on time.

- Align on sprint commitments jointly. Neither of you should override the other.
- Respect the product-process boundary: Squad PM owns backlog priority; Scrum Master owns process; you own engineering leadership and delivery commitment.

**EL ↔ Scrum Master.** Scrum Master facilitates process and may push for process consistency. You may want to skip ceremonies under delivery pressure.

- Ceremonies and process are how the squad sustains delivery — they are not overhead. When delivery is behind, the answer is rarely "skip the retro" and usually "use the retro to fix the bottleneck."

---

## 6. Management

### Dual-Axis Reporting

- **Execution axis:** Reports to **EPM**. EPM provides execution-axis input on your squad delivery effectiveness.
- **Functional/career axis:** **Engineering leadership** evaluates your career growth across Engagement assignments — multi-Engagement delivery record, technical growth, inner source contributions.

### Performance Input

Request feedback from EA on mandatory review quality and inner source contribution quality. Request feedback from AVA on your squad's assembly-impacting work and testing quality. Provide execution-axis feedback on your engineers to their Engineering Manager — multi-Engagement career development depends on this input.

---

## 7. Accountability

### Escalation: Dos and Don'ts

**Do:**

- Escalate cross-squad dependencies and blockers to **EPM** — EPM coordinates across squads ([governance.md](../../governance.md#escalation-model)).
- Escalate architecture disputes to **EA** (architecture), then to **EPM** if unresolved.
- Escalate delivery commitment risks to **EPM** early, with impact and options.
- Provide execution-axis feedback on engineers to their **Engineering Manager** (functional axis).

**Don't:**

- Override EA's quality standards or skip mandatory review under delivery pressure. If the standards are unreasonable, escalate — don't silently bypass.
- Override AVA's assembly-impacting review requirement. Submit the work; if AVA is slow, escalate through EPM.
- Independently approach PL Squad leads for staffing. Staffing coordination goes through PPM. Work through EPM and PPM.
- Absorb Scrum Master process responsibilities. You own engineering leadership; Scrum Master owns process facilitation.

### When Commitments Are Missed

EL commitments are primarily **commitment-based** (per the [accountability framework](../../people-and-culture/accountability.md)): sprint commitment accuracy, mandatory review compliance, and early warning on risks are binary — done or not done. When a sprint commitment is missed without early warning, the response is immediate transparency to EPM, diagnosis of the cause, and a revised plan. The EL's reliability is measured by the accuracy of commitments made and the timeliness of risk communication, not by whether problems exist.

However, squad throughput and engineering quality improvement are **outcome-based**: these trend over time, and the EL's judgement on capacity planning and quality investment is evaluated by trajectory, not by individual sprint results.

---

## 8. Objectives in Perspective

The EL's immediate objectives — squad delivery, quality compliance, inner source execution — serve a broader purpose: ensuring that the squad's work contributes to a verifiable, certified assembly that meets the customer's need and extends the platform.

When you meet EA's quality standards and submit work for mandatory review, you enable the AVA to certify the assembly. When you execute inner source contributions at the PL Maintainer quality bar, you extend the platform for future Engagements. When you communicate risks early to EPM, you enable the EPM to manage the client's expectations and the EO to make informed decisions.

The EL who delivers on time but ignores quality standards has produced a sprint output. The EL who delivers on time, meets quality standards, executes inner source, and communicates risks early has produced a squad that the Engagement can rely on.

---

## Further Learning

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
| *Software Product Lines: Practices and Patterns* — Clements & Northrop ([SEI](https://www.informit.com/store/software-product-lines-practices-and-patterns-9780201703320)) | PLE foundations; helps ELs understand the "extend, don't fork" discipline driving inner source decisions |

---

[← Back to Career Guides](../README.md)
