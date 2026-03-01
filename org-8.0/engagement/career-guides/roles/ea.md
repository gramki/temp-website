# Engagement Architect (EA) — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#engagement-architect-ea)

---

The EA owns **architecture across the entire Engagement span** — Customer Product, Studio Components, and their integration. The role is scoped **per-Engagement**. The EA reports to EO on the execution axis and is a peer architect to AVA. The functional home is **Architecture** (or **Engineering** if a Staff/Principal Engineer plays the role).

---

## Architecture vs. Technical Architecture

This distinction is fundamental to the EA role:

- **Architecture (solution / enterprise):** The EA must synthesise technical, functional, commercial, and operational contexts into a coherent solution. Which archetype fits? What are the gaps? How does the operating model (Fully Managed, Co-Managed, Customer-Operated) shape the solution? What inner source contributions are worth the timeline cost? These are architecture decisions, not just technical ones.
- **Technical architecture (software architecture):** Component design, API contracts, data flow, deployment topology. This is necessary but not sufficient. A Staff Engineer playing EA brings technical architecture depth; what they must develop is the broader synthesis.

If you find yourself only making technical decisions and not engaging with the commercial context, the customer's operating model, or the inner source vs. custom trade-off at a business level, you are doing technical architecture — not the EA role.

---

## 1. Empowerment

- **Architecture decisions.** You own end-to-end solution architecture: Product Line selection, configuration approach, integration design, Studio Component architecture, archetype selection and adaptation.
- **Engineering quality standards.** You set the quality standards across the Engagement — architecture decisions, coding standards for architecture-significant concerns, mandatory review in Definition of Done, inner source quality gates. ELs are responsible for meeting these standards within their squads.
- **Mandatory review.** Architecture-significant changes require your review before implementation. This is part of the squad's Definition of Done ([mandatory architect consultation](../../roles.md#mandatory-architect-consultation)).
- **Inner source priority.** You maintain a view of inner source debt across the Engagement and prioritise contributions. Inner source vs. custom build is your decision, with timeline impact communicated to EPM.
- **Gap analysis authority.** You produce the gap register — platform capability vs. customer need — with inner source vs. custom recommendations for each gap.
- **What you cannot override.** You cannot override AVA on verification or release decisions. AVA prevails on these. If you disagree with AVA's certification criteria, the path is: EPM mediates → EO decides.

---

## 2. Assignment

ERC assigns the EA at **Stage 1** ([engagement-formation.md](../../engagement-formation.md#stage-1--erc-assigns-engagement-leadership-at-initiate)). ERC matches designation level to Engagement complexity — from Staff Engineer (PE-1) or Architect for smaller Engagements to Senior or Principal Architect for large/complex Engagements.

**Scope:** Per-Engagement. One EA per Engagement. A person may serve as EA for multiple Engagements if bandwidth permits.

**Scaling:** For large Engagements spanning multiple Product Lines or 6+ squads with significant architecture complexity, Stream Architects may be introduced from the Architecture function. Each Stream Architect owns a domain slice; the EA retains overall solution architecture accountability.

---

## 3. Ambition

### First 90 Days (or First Increment)

- **Master the archetype.** Before writing any architecture, understand the solution archetype in use — what it covers, where its boundaries are, and where this Engagement will deviate. Review the archetype cookbook, the variability documentation, and any previous Engagement adaptations.
- **Run the gap analysis.** Compare platform capability to customer need. Produce the gap register with inner source vs. custom recommendations for each gap. This is the EA's most important early deliverable — it sets the scope, influences the timeline, and determines inner source workload.
- **Co-design with AVA.** Meet your AVA peer and jointly define the system-under-test boundary, the assembly acceptance criteria, and the verification approach. The architecture determines what "correct assembly" means — if you cannot articulate it, AVA cannot verify it. This co-design is substantial work, not a handoff.
- **Set engineering quality standards.** Define the mandatory review scope, the DoD architecture criteria, and the inner source quality gates. Communicate these to ELs — they are responsible for meeting the standards within their squads.
- **Understand the commercial context.** Know why the customer chose this operating model, what the contract covers, and where scope boundaries are. Architecture decisions have commercial implications — a custom build increases delivery cost; an inner source contribution delays timeline but reduces long-term cost.

### What Great Looks Like

- The gap register is current and actionable — every gap has a recommended approach (inner source, custom, workaround) with rationale.
- Architecture is "just enough" — sufficient to guide squads and enable AVA to verify, but not so prescriptive that it blocks squad-level design judgement.
- Inner source contributions are planned into squad capacity (not treated as surprise overhead) and accepted by PL Maintainers.
- Mandatory review is working — architecture-significant changes are reviewed before completion, not after. ELs understand the standard and bring work for review proactively.
- The solution architecture is verifiable — AVA can design verification that certifies the assembly against your architecture.
- Variability documentation is maintained — future Engagements can leverage your decisions.
- Knowledge capture is continuous — the decision log is current, archetype adaptations are documented, and patterns are extracted for PAC Practice Mode.

---

## 4. Commitments

### Dimensions

| Dimension | EA SLA |
|---|---|
| **Quality** | Engineering quality standards are defined, communicated, and enforced through mandatory review. Inner source contributions meet PL Maintainer quality gates. Architecture-significant changes are reviewed before completion. The architecture enables AVA to verify — if AVA cannot certify the assembly against the architecture, the architecture is incomplete. |
| **Fitment** | The solution architecture fits the customer's need and the platform's capability. Gap analysis is current. Archetype selection is defensible. The inner source vs. custom trade-off is made with full context (timeline, reusability, platform evolution). |
| **Cost** | Inner source reduces long-term platform cost; custom build may reduce short-term Engagement cost but creates drift. The EA's architecture decisions determine what is in scope and what is not, directly affecting delivery cost and commercial terms. |

### Contractual Connection — Tier 2 (Mechanism)

The EA does not interface with the contract directly, but architecture decisions determine contractual scope. When the gap analysis recommends inner source over custom build, it affects timeline and cost — both contractual concerns. When architecture decisions exclude something from scope, it affects what is contractually deliverable. The EA's gap register and architecture decisions are the mechanism through which scope becomes concrete.

---

## 5. Collaboration

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

### Tensions and Navigation

**EA ↔ AVA.** You architect the functional system; AVA architects the verification system. You are peers, not in a reporting relationship. Disagreements on architecture scope vs. verification scope are normal.

- Architecture decisions: EA prevails (per the [escalation model](../../governance.md#escalation-model)). But "prevails" means you should still listen — AVA sees verifiability concerns you may miss.
- Verification/release disagreements: AVA prevails. If you believe AVA's verification criteria are too strict, the path is: EPM mediates → EO decides.
- Co-design the system-under-test boundary jointly. If the boundary is unclear, verification will be either too broad (slow) or too narrow (missing real integration risks).

**EA ↔ ELs.** You set engineering quality standards and require mandatory review. ELs own squad delivery and may see mandatory review and inner source work as overhead that threatens their commitments.

- Set standards early and clearly. If ELs discover mandatory review requirements mid-sprint, the failure is in communication, not in the standard.
- Make mandatory review efficient — define what qualifies as "architecture-significant" so ELs know what to bring and what to handle at squad level.
- Inner source prioritisation is your authority, but the timeline impact is real. Work with ELs to plan inner source contributions into sprint capacity.

**EA ↔ EPM.** Inner source contributions and mandatory review add time. EPM needs predictability and manages the customer-facing timeline.

- Include inner source timelines in the architecture plan from the start. If EPM's plan doesn't account for inner source, you both have a problem.
- When inner source causes timeline slip, present options: accept the slip, defer the contribution (with tech debt documented), or adjust scope. Frame it as a business trade-off, not "engineering vs. delivery."

**EA ↔ PL Maintainers.** You prioritise inner source contributions from Engagement squads. PL Maintainers gatekeep platform quality. Your contributions may not meet the bar, or PL Maintainers may not have review capacity.

- Engage PL Maintainers early — before the contribution is written, not after.
- If PL Maintainer review capacity is a bottleneck, escalate through PPM and Engineering leadership.

---

## 6. Management

### Dual-Axis Reporting

- **Execution axis:** Reports to **EO**. EO provides execution-axis input on your effectiveness within the Engagement.
- **Functional/career axis:** **Architecture leadership** (or **Engineering leadership** if you are a Staff/Principal Engineer playing EA). Your functional-axis leader evaluates growth across EA assignments — multi-Engagement architecture record, archetype contributions, inner source quality.

### Performance Input

Request feedback from AVA (on co-design quality), ELs (on mandatory review usefulness), and EPM (on inner source timeline impact). EO provides the overall effectiveness assessment. Architecture leadership evaluates your breadth across Engagements and your contribution to the platform's architectural evolution.

---

## 7. Accountability

### Escalation: Dos and Don'ts

**Do:**

- Escalate to **EPM** for EA ↔ AVA disputes (EPM mediates per the escalation model).
- Escalate to **PAC** when an architecture decision affects the Product Line or sets a precedent that other Engagements should follow.
- Escalate to **EO** (through EPM) when inner source timelines are unsolvable at the EA ↔ EL level and require Engagement-level priority decisions.

**Don't:**

- Override AVA on verification or release decisions. AVA prevails on these. If you disagree, use the escalation model.
- Direct engineers in squads. You advise and review; ELs direct. If an EL is not meeting quality standards, escalate to EPM, not to the engineers.
- Deprioritise variability documentation under delivery pressure. It is the primary mechanism for future Engagement leverage and is part of your accountability.
- Escalate to Architecture leadership to override EO or EPM on delivery decisions. The execution axis goes through EO; the functional axis is for career development.

### When Commitments Are Missed

EA commitments are primarily **outcome-based** (per the [accountability framework](../../people-and-culture/accountability.md)): architecture quality, inner source contribution acceptance, and gap anticipation are judgement-dependent. When an architecture decision proves wrong (a gap was missed, an inner source approach fails PL Maintainer review), the response is diagnosis and correction — not blame. The EA's accountability is for the quality of architectural judgement over time, not for never being wrong.

However, mandatory review timeliness and quality standard communication are **commitment-based**: if ELs submit work and the review is slow or the standard was never clearly communicated, that is a reliability failure.

---

## 8. Objectives in Perspective

The EA's immediate objectives — gap analysis, architecture decisions, inner source prioritisation — serve a broader purpose: ensuring that each Engagement extends the platform rather than fragmenting it.

When you choose inner source over custom build, you accept a timeline cost on this Engagement to reduce cost and increase capability for every future Engagement. When you document variability, you enable the next EA to start from your decisions rather than rediscovering them. When you co-design with AVA, you ensure the assembly can be verified — which protects the client from quality failures.

The EA who optimises for this Engagement alone (custom builds, undocumented decisions, skipped inner source) delivers faster today but leaves the platform weaker. The EA who balances Engagement delivery with platform evolution delivers the model's actual value: sustainable, accelerating delivery across Engagements.

---

## Further Learning

**Internal references:**
- [Roles and Responsibilities — EA](../../roles.md#engagement-architect-ea)
- [Mandatory Architect Consultation](../../roles.md#mandatory-architect-consultation)
- [Variability Management](../../../product-line-engineering/framework/variability-management.md)
- [Solution Archetypes](../../../product-line-engineering/framework/solution-archetypes.md)
- [Inner Source Guidelines](../../../product-line-engineering/governance/inner-source-guidelines.md)
- [Governance and Escalation](../../governance.md)
- [Architecture Function Guide](../functions/architecture.md) — career progression in the Architecture function

**External references:**

| Resource | Why Relevant |
|----------|--------------|
| *Software Architecture in Practice* — Bass, Clements, Kazman, 4th ed. ([Pearson](https://www.pearson.com/en-us/subject-catalog/p/software-architecture-in-practice/P200000000111/9780137468218)) | Architecture quality attributes and evaluation; directly applicable to gap analysis and multi-PL architecture |
| *Just Enough Software Architecture* — Fairbanks ([georgefairbanks.com](https://www.georgefairbanks.com/e-book/)) | Risk-driven architecture; helps calibrate "how much architecture" for each Engagement |
| *Solution Architecture Foundations* — Lovatt ([BCS](https://www.amazon.com/Solution-Architecture-Foundations-Mark-Lovatt/dp/1780175655)) | Solution architecture practice aligned with EA's synthesis role |
| *Software Product Line Engineering* — Pohl, Böckle, van der Linden ([Springer](https://link.springer.com/book/10.1007/978-3-662-03764-7)) | PLE and variability management; relevant to archetype design and variability documentation |
| *Understanding the InnerSource Checklist* — Cooper & Stol ([O'Reilly](https://www.oreilly.com/library/view/understanding-the-innersource/9781491986899/)) | Inner source mechanics; applicable to inner source prioritisation and PL Maintainer coordination |

---

[← Back to Career Guides](../README.md)
