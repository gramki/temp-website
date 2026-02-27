# Engagement Architect (EA) — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#engagement-architect-ea)

---

## Architecture vs. Technical Architecture

This distinction is fundamental to the EA role:

- **Architecture (solution / enterprise):** The EA must synthesise technical, functional, commercial, and operational contexts into a coherent solution. Which archetype fits? What are the gaps? How does the operating model (Fully Managed, Co-Managed, Customer-Operated) shape the solution? What inner source contributions are worth the timeline cost? These are architecture decisions, not just technical ones.
- **Technical architecture (software architecture):** Component design, API contracts, data flow, deployment topology. This is necessary but not sufficient. A Staff Engineer playing EA brings technical architecture depth; what they must develop is the broader synthesis.

If you find yourself only making technical decisions and not engaging with the commercial context, the customer's operating model, or the inner source vs. custom trade-off at a business level, you are doing technical architecture — not the EA role.

---

## 1. Success in the Role

### First 90 Days (or First Increment)

- **Master the archetype:** Before writing any architecture, understand the solution archetype in use — what it covers, where its boundaries are, and where this Engagement will deviate. Review the archetype cookbook, the variability documentation, and any previous Engagement adaptations.
- **Run the gap analysis:** Compare platform capability to customer need. Produce the gap register with inner source vs. custom recommendations for each gap. This is the EA's most important early deliverable — it sets the scope, influences the timeline, and determines inner source workload.
- **Co-design with AVA:** Meet your AVA peer early. Jointly define the system-under-test boundary, the assembly acceptance criteria, and the verification approach. The architecture determines what "correct assembly" means — if you cannot articulate it, AVA cannot verify it. This co-design is substantial work, not a handoff.
- **Set engineering quality standards:** Define the mandatory review scope, the DoD architecture criteria, and the inner source quality gates. Communicate these to ELs — they are responsible for meeting the standards within their squads.
- **Understand the commercial context:** Know why the customer chose this operating model, what the contract covers, and where scope boundaries are. Architecture decisions have commercial implications — a custom build increases delivery cost; an inner source contribution delays timeline but reduces long-term cost.

### What "Good" Looks Like

- The gap register is current and actionable — every gap has a recommended approach (inner source, custom, workaround) with rationale.
- Architecture is "just enough" — sufficient to guide squads and enable AVA to verify, but not so prescriptive that it blocks squad-level design judgment.
- Inner source contributions are planned into squad capacity (not treated as surprise overhead) and accepted by PL Maintainers.
- Mandatory review is working — architecture-significant changes are reviewed before completion, not after. ELs understand the standard and bring work for review proactively.
- The solution architecture is verifiable — AVA can design verification that certifies the assembly against your architecture. If AVA cannot verify it, the architecture is incomplete.
- Variability documentation is maintained — future Engagements can leverage your decisions.
- Knowledge capture is continuous — the decision log is current, archetype adaptations are documented, and patterns are extracted for PAC Practice Mode.

### Key Relationships

| Role | What You Need from Them | What They Need from You |
|------|------------------------|------------------------|
| AVA | Verification perspective, assembly acceptance criteria co-design, certification feedback | Architecture clarity, system-under-test boundary definition, verifiable acceptance criteria |
| EPO | Customer requirements, discovery findings | Requirements-architecture translation, gap analysis, inner source vs. custom recommendations |
| ELs | Squad-level design decisions, implementation feedback, inner source contribution execution | Architecture guidance, mandatory review, quality standards, inner source prioritisation |
| EPM | Timeline reality, resourcing, scope change impact | Architecture status, inner source timeline impact, risk communication |
| EO | Strategic direction, backing for inner source bar, resourcing support | Architecture assessment, gap register, risk flags |
| PL Maintainers | Inner source review, contribution acceptance, platform capability guidance | Quality contributions, clear contribution rationale, variability documentation |
| SRE Lead | Operational requirements, deployment topology needs | Architecture decisions that support operability, monitoring surface area definition |

### Performance Input and the Dual Axis

Your functional home is **Architecture** (or **Engineering** if you are a Staff/Principal Engineer playing EA). Architecture leadership evaluates your growth across EA assignments — multi-Engagement architecture record, archetype contributions, inner source quality. EO provides execution-axis input on your effectiveness. Request feedback from AVA (on co-design quality), ELs (on mandatory review usefulness), and EPM (on inner source timeline impact).

---

## 2. Expected Interactions, Tensions, and How to Navigate

### EA ↔ AVA

**Tension:** You architect the functional system; AVA architects the verification system. You are peers, not in a reporting relationship. Disagreements on architecture scope, acceptance criteria, or verification approach are normal.

**How to navigate:**
- Architecture disagreements: EA prevails (per the [escalation model](../../governance.md#escalation-model)). But "prevails" means you should still listen — AVA sees verifiability concerns you may miss.
- Verification/release disagreements: AVA prevails. If you believe AVA's verification criteria are too strict, the path is: EPM mediates → EO decides.
- Co-design the system-under-test boundary jointly. If the boundary is unclear, verification will be either too broad (slow) or too narrow (missing real integration risks).

### EA ↔ ELs

**Tension:** You set engineering quality standards and require mandatory review. ELs own squad delivery and may see mandatory review and inner source work as overhead that threatens their commitments.

**How to navigate:**
- Set standards early and clearly. If ELs discover mandatory review requirements mid-sprint, the failure is in communication, not in the standard.
- Make mandatory review efficient — define what qualifies as "architecture-significant" so ELs know what to bring and what to handle at squad level. Not every change needs EA review.
- Inner source prioritisation is your authority, but the timeline impact is real. Work with ELs to plan inner source contributions into sprint capacity. If the contribution will take longer than the EL's sprint allows, discuss alternatives (phased contribution, alternative approach) rather than insisting on a timeline that will fail.

### EA ↔ EPM

**Tension:** Inner source contributions and mandatory review add time. EPM needs predictability and manages the customer-facing timeline.

**How to navigate:**
- Include inner source timelines in the architecture plan from the start. If EPM's plan doesn't account for inner source, you both have a problem.
- When inner source causes timeline slip, present options: accept the slip, defer the contribution (with tech debt documented), or adjust scope. Do not frame it as "engineering vs. delivery" — it is a business trade-off that EPM and EO should decide.

### EA ↔ PL Maintainers

**Tension:** You prioritise inner source contributions from Engagement squads. PL Maintainers gatekeep platform quality. Your contributions may not meet the bar, or PL Maintainers may not have review capacity.

**How to navigate:**
- Engage PL Maintainers early — before the contribution is written, not after. A contribution designed with PL Maintainer input is more likely to be accepted.
- If PL Maintainer review capacity is a bottleneck, escalate through PPM and Engineering leadership. Do not wait for the contribution to rot in a review queue.

---

## 3. Escalation: Dos and Don'ts

**Do:**

- Escalate to **EPM** for EA ↔ AVA disputes (EPM mediates per the escalation model).
- Escalate to **PAC** when an architecture decision affects the Product Line or sets a precedent that other Engagements should follow.
- Escalate to **EO** (through EPM) when inner source timelines are unsolvable at the EA ↔ EL level and require Engagement-level priority decisions.

**Don't:**

- Override AVA on verification or release decisions. AVA prevails on these. If you disagree, use the escalation model.
- Direct engineers in squads. You advise and review; ELs direct. If an EL is not meeting quality standards, escalate to EPM, not to the engineers.
- Deprioritise variability documentation under delivery pressure. It is the primary mechanism for future Engagement leverage and is part of your accountability.
- Escalate to Architecture leadership to override EO or EPM on delivery decisions. The execution axis goes through EO; the functional axis is for career development.

---

## 4. Further Learning

**Internal references:**
- [Roles and Responsibilities — EA](../../roles.md#engagement-architect-ea)
- [Mandatory Architect Consultation](../../roles.md#mandatory-architect-consultation)
- [Variability Management](../../product-line-engineering/framework/variability-management.md)
- [Solution Archetypes](../../product-line-engineering/framework/solution-archetypes.md)
- [Inner Source Guidelines](../../product-line-engineering/governance/inner-source-guidelines.md)
- [Governance and Escalation](../../governance.md)
- [Architecture Function Guide](../functions/architecture.md) — career progression in the Architecture function

**External references:**

| Resource | Why Relevant |
|----------|--------------|
| *Software Architecture in Practice* — Bass, Clements, Kazman, 4th ed. ([Pearson](https://www.pearson.com/en-us/subject-catalog/p/software-architecture-in-practice/P200000009471/)) | Architecture quality attributes and evaluation; directly applicable to gap analysis and multi-PL architecture |
| *Just Enough Software Architecture* — Fairbanks ([georgefairbanks.com](https://www.georgefairbanks.com/e-book/)) | Risk-driven architecture; helps calibrate "how much architecture" for each Engagement |
| *Solution Architecture Foundations* — Hewitt ([Packt](https://www.packtpub.com/en-us/product/solution-architecture-foundations-9781838820688)) | Solution architecture practice aligned with EA's synthesis role |
| *Solution vs. Software Architecture* — DZone ([dzone.com](https://dzone.com/articles/solution-architecture-vs-software-architecture)) | Concise distinction helping articulate the EA's scope to engineers |
| *Enterprise Integration Patterns* — Hohpe & Woolf ([enterpriseintegrationpatterns.com](https://www.enterpriseintegrationpatterns.com/)) | Integration patterns directly applicable to cross-PL integration design |
| *Software Product Line Engineering* — Pohl, Böckle, van der Linden ([Springer](https://link.springer.com/book/10.1007/978-3-662-03764-7)) | PLE and variability management; relevant to archetype design and variability documentation |
| *Understanding the InnerSource Checklist* — Cooper & Stol ([O'Reilly](https://www.oreilly.com/library/view/understanding-the-innersource/9781491986899/)) | Inner source mechanics; applicable to inner source prioritisation and PL Maintainer coordination |

---

[← Back to Career Guides](../README.md)
