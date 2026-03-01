# Assembly Verification Architect (AVA) — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#assembly-verification-architect-ava)

---

The AVA is a **peer architect to the EA**. The EA architects the functional assembly; the AVA **architects, builds, and operates the verification system** that certifies it. The AVA certifies the assembled product at every increment and holds **independent authority to block release** when assembly quality criteria are not met. The role is scoped **per-Engagement**. The AVA reports to EO on the execution axis and directs the Verification Squad. The functional home is **Architecture** (or **Engineering** if a senior engineer plays the role).

---

## The AVA Leads the Verification Squad

The AVA **designs the verification system and directs the squad that builds it**. The Verification Squad builds the verification module — test suites, IaC environment definitions, test data preparation, CI orchestration — as a first-class artifact group of the Engagement Assembly. This is real engineering output: code, infrastructure, automation.

The Verification Squad has no EL. The AVA is the squad's leader, but the authority comes from the architect role and certification responsibility, not from the engineering management hierarchy. In practice this means:

- **You design and direct.** You define the system-under-test boundary, the verification strategy, the environment topology, and the certification criteria. The squad implements what you design. You review their work against your architecture, not against a test plan.
- **You lead people.** You assign work, review output, unblock engineers, and manage the squad's delivery cadence. The model says "not an EL" to clarify the authority source, not to suggest you are hands-off.
- **The risk is reducing to test management.** If your daily work is tracking test case counts, coordinating manual execution, or maintaining a spreadsheet of test results — you have lost the architecture. The verification module should be automated infrastructure that proves assembly correctness at every increment. When you find yourself managing execution instead of designing the system that makes execution automatic, step back and redesign.

---

## 1. Empowerment

- **Release-block authority.** You may block any release of the assembled product when assembly quality criteria are not met. This authority is independent — EA, EL, EPM, and Client Partner cannot override it. EO can override, but only as a documented **governance event**.
- **Certification authority.** You certify the integrated assembly at every increment. Release decisions are based on evidence against your defined criteria, not on opinion or pressure.
- **Verification Squad direction.** You direct the Verification Squad through architectural authority, not through the EL hierarchy. You design, assign work, review output, and manage the squad's cadence.
- **Mandatory review of assembly-impacting changes.** Assembly-impacting changes across all squads require your review ([mandatory architect consultation](../../roles.md#mandatory-architect-consultation)).
- **Co-design authority on acceptance criteria.** You jointly define assembly acceptance criteria with EA — these criteria drive the verification module and become the basis for certification decisions.
- **What you cannot override.** You cannot override EA on architecture decisions. EA prevails on architecture; you prevail on verification and release.

---

## 2. Assignment

ERC assigns the AVA at **Stage 1** ([engagement-formation.md](../../engagement-formation.md#stage-1--erc-assigns-engagement-leadership-at-initiate)). ERC matches designation level to Engagement complexity — Architect for medium Engagements, Senior Architect for large/complex Engagements where verification depth is required.

**Scope:** Per-Engagement. One AVA per Engagement. A person may be shared across Engagements if bandwidth permits. When scope warrants it, the AVA directs a dedicated Verification Squad.

---

## 3. Ambition

### First 90 Days (or First Increment)

- **Co-design with EA.** Meet your EA peer and jointly define the system-under-test boundary, the integration seams that require assembly-level verification, and the assembly acceptance criteria. The architecture determines what "correct assembly" means — you translate that into verifiable criteria.
- **Design the verification architecture.** Define the verification strategy, test environment topology, test data model, and CI orchestration. This is architecture work — treat it with the same rigour you would apply to the functional system architecture.
- **Establish the Verification Squad.** If a dedicated Verification Squad is activated, you direct it. Engineers in the Verification Squad build verification infrastructure (IaC environment definitions, test suites, test data preparation, CI orchestration), not "test cases."
- **Define certification criteria.** What must be true for you to certify an increment for release? Define it early, communicate it to ELs and EPM, and enforce it consistently. If the criteria change mid-Build, communicate the change.
- **Understand the release coordination model.** You certify (decide *whether* the assembly can be released); SRE Lead deploys (manages *how* it is released). This boundary is fundamental — do not blur it.

### What Great Looks Like

- The verification module is a first-class artifact — maintained with the same rigour as functional code, versioned, and evolving with each increment.
- Every increment is certified against defined criteria. Release decisions are based on evidence, not opinion or pressure.
- The system-under-test boundary is accurate and current — what is inside (real deployed components), what is simulated at the edges, and the boundary evolves as the assembly grows.
- ELs know the mandatory review scope (assembly-impacting changes) and bring work for review proactively.
- Release-block authority is exercised when warranted and respected by the team. The hardest measure of AVA success is: when you block, no one is surprised, because the criteria were clear from the start.
- At Transfer, the verification module (test suites, environment definitions, test data tooling, CI orchestration, certification records) is a complete, handoverable deliverable.

---

## 4. Commitments

### Dimensions

| Dimension | AVA SLA |
|---|---|
| **Quality** | Certification pass rate is meaningful — certification is evidence-based, not rubber-stamped. Verification coverage is adequate for the Engagement's risk profile. Release-block authority is exercised when criteria are not met — blocking correctly is as important as certifying correctly. The verification module is maintained as automated infrastructure, not as manual test execution. |
| **Fitment** | The verification system proves that the integrated assembly works as the architecture specified. Assembly-level verification covers integration seams, cross-squad interfaces, configuration correctness, and deployment topology. The system-under-test boundary is accurate and evolves with the assembly. |

### Contractual Connection — Tier 2 (Mechanism)

The AVA does not interface with the contract directly, but certification is the evidence that assembly quality meets the contracted acceptance criteria. If the contract includes acceptance criteria (and most do), the AVA's certification is the mechanism that proves they are met. The verification module — test suites, certification records, environment definitions — may be a contractual deliverable at Transfer.

---

## 5. Collaboration

### Key Relationships

| Role | What You Need from Them | What They Need from You |
|------|------------------------|------------------------|
| EA | Architecture clarity, system-under-test boundary co-design, integration topology | Verification perspective, assembly acceptance criteria, certification feedback |
| ELs | Assembly-impacting changes for review, testing infrastructure support, squad-level test quality | Mandatory review feedback, verification requirements, clear certification criteria |
| EPM | Release coordination, schedule, commercial context for release timing | Certification status, release readiness, release-block decisions with rationale |
| SRE Lead | Deployment mechanics, environment promotion, production readiness | Release certification (you certify; SRE deploys) |
| EO | Backing for release-block authority, Verification Squad resourcing, governance event documentation | Certification status, risk assessment, governance event input |
| Verification Squad engineers | Implementation of verification infrastructure, test automation | Architecture direction, design guidance, certification criteria |

### Tensions and Navigation

**AVA ↔ EA.** You are peer architects with different domains. Disagreements on architecture scope (what EA should have designed) vs. verification scope (what you need to verify) are normal.

- Architecture decisions: EA prevails. If you believe the architecture makes verification impractical, raise it as a risk in co-design — before the architecture is implemented.
- Verification and release decisions: you prevail. If EA disagrees with your certification criteria, the path is: EPM mediates → EO decides.
- Co-design early and continuously. The system-under-test boundary is not a one-time decision — it evolves as the assembly evolves.

**AVA ↔ EPM.** You may need to block a release under commercial and customer pressure. EPM owns the customer-facing timeline and may push for release.

- Make certification criteria visible from the start. If EPM and the team know the criteria and see the status throughout Build, a release block should never be a surprise.
- When you block: provide evidence (what criteria are not met, what the risk of releasing is, what remediation is needed). A release block without evidence erodes trust.
- If EPM disputes the block, EPM escalates to EO. EO decides. An EO override of your release block is a governance event documented in the decision log.

**AVA ↔ ELs.** You require mandatory review of assembly-impacting changes. ELs may see this as overhead that slows their squads.

- Define "assembly-impacting" clearly — integration seams, cross-squad interfaces, configuration correctness, deployment topology. Not every change is assembly-impacting. If ELs are bringing everything for review, the scope definition is too broad.
- Review quickly. If your review turnaround is slow, ELs will stop bringing work proactively.

**AVA ↔ SRE Lead.** You certify; SRE deploys. The boundary is clear but the handoff must be explicit — certification status, deployment sequencing, rollback criteria.

- Define the certification → deployment protocol: what artifacts does SRE Lead need from you? What does SRE Lead need to confirm?
- If SRE Lead identifies an operational concern that affects release readiness, treat it as verification-relevant input.

---

## 6. Management

### Dual-Axis Reporting

- **Execution axis:** Reports to **EO**. EO provides execution-axis input on your effectiveness within the Engagement.
- **Functional/career axis:** **Architecture leadership** (or **Engineering leadership** if you are a Staff/Principal Engineer playing AVA). Your functional-axis leader evaluates growth — certification track record, verification module quality, multi-Engagement experience.

### Performance Input

Request feedback from EA (on co-design quality), EPM (on release coordination effectiveness), and SRE Lead (on the certification → deployment handoff). EO provides the overall effectiveness assessment.

---

## 7. Accountability

### Escalation: Dos and Don'ts

**Do:**

- Exercise **release-block authority** when assembly quality criteria are not met. This authority is independent — EA, EL, EPM, and Client Partner cannot override it. EO can override, but only as a documented governance event (see [governance.md](../../governance.md#ava-release-block-authority)). If you block, document the evidence and remediation needed.
- Escalate architecture disputes with EA to **EPM** (EPM mediates per the [escalation model](../../governance.md#escalation-model)).
- When EO overrides your release block, ensure it is documented as a governance event in the decision log. This is not insubordination — it is the model working as designed.

**Don't:**

- Use release-block authority as leverage for non-verification concerns (e.g. blocking release because you disagree with an architecture decision that is EA's domain). Release-block authority is about assembly quality — not a general veto.
- Direct functional squad engineers (outside the Verification Squad). Mandatory review is your mechanism; directing is EL's responsibility. If an EL is not sending assembly-impacting work for review, escalate to EPM.
- Allow certification criteria to drift silently. If criteria change, communicate to EPM, ELs, and EO. Surprises at release time destroy trust.
- Treat the Verification Squad as a test team. They build verification infrastructure — IaC, CI orchestration, test data, automation. If the work looks like manual test execution, you have a design problem.

### When Commitments Are Missed

AVA commitments span both types (per the [accountability framework](../../people-and-culture/accountability.md)):

- **Outcome-based:** Verification coverage adequacy and the accuracy of the system-under-test boundary are judgement calls. When verification misses a real integration risk (a post-release defect that should have been caught), the response is diagnosis — was the boundary wrong? Was the verification strategy too narrow? — and correction.
- **Commitment-based:** Certification timeliness, review turnaround, and criteria communication are binary. When certification is slow (holding up release without evidence) or criteria change silently (creating release-time surprises), that is a reliability failure.

---

## 8. Objectives in Perspective

The AVA's immediate objectives — certification, release-block authority, verification module quality — serve a broader purpose: protecting the client from assembly failures and protecting the organisation from the downstream cost of quality shortcuts.

When you certify an increment, you are not just saying "the tests passed." You are saying "this assembled product, built from multiple Product Lines, Studio Components, and customer-specific configuration, works as the architecture intended." That is a statement of professional judgement, backed by evidence you designed and infrastructure your squad built.

When you block a release, you are protecting not just quality but trust — the client's trust in the product, the organisation's trust in the assembly model, and the platform's integrity. The cost of a false certification (releasing an assembly that fails) is always higher than the cost of a justified block.

The verification module you build is not throwaway — at Transfer, it becomes the client's (or operations team's) ongoing verification capability. The AVA who builds disposable tests has done testing. The AVA who builds a verification system has done architecture.

---

## Further Learning

**Internal references:**
- [Roles and Responsibilities — AVA](../../roles.md#assembly-verification-architect-ava)
- [Mandatory Architect Consultation](../../roles.md#mandatory-architect-consultation)
- [Verification and Certification](../../verification-and-certification.md)
- [Governance — AVA Release-Block Authority](../../governance.md#ava-release-block-authority)
- [Architecture Function Guide](../functions/architecture.md) — career progression and architecture vs. technical architecture

**External references:**

| Resource | Why Relevant |
|----------|--------------|
| *Software Architecture in Practice* — Bass, Clements, Kazman, 4th ed. ([Pearson](https://www.pearson.com/en-us/subject-catalog/p/software-architecture-in-practice/P200000000111/9780137468218)) | Architecture quality attributes and evaluation; applicable to verification architecture and the AVA's system-level thinking |
| *Just Enough Software Architecture* — Fairbanks ([georgefairbanks.com](https://www.georgefairbanks.com/e-book/)) | Risk-driven architecture; helps calibrate verification depth per Engagement |
| *Site Reliability Engineering* — Google ([sre.google/sre-book](https://sre.google/sre-book/table-of-contents/)) | Operational reliability principles; relevant to the AVA ↔ SRE Lead relationship and understanding operational readiness criteria. Free online. |
| *Solution Architecture Foundations* — Lovatt ([BCS](https://www.amazon.com/Solution-Architecture-Foundations-Mark-Lovatt/dp/1780175655)) | Solution architecture practice — stakeholder interaction, gap analysis, solution definition; applicable to the AVA's system-level verification design |

---

[← Back to Career Guides](../README.md)
