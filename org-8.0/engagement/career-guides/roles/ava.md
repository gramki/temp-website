# Assembly Verification Architect (AVA) — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#assembly-verification-architect-ava)

---

## Architecture vs. Technical Architecture

This distinction is critical for the AVA role:

- **Architecture (solution / enterprise):** The AVA architects the verification system — a complex, multi-component system that certifies the assembled product. This requires understanding the full assembly (all Product Lines, Customer Product, Studio Components), their integration topology, the operating model, and the customer's quality expectations. This is architecture work.
- **Technical architecture (software architecture):** Test automation frameworks, CI/CD pipeline design, environment topology. Necessary, but the AVA must think beyond tooling — the verification architecture must answer "what does correct assembly mean?" and "what is the system-under-test boundary?", not just "what test framework should we use?"

The AVA is **not a test manager**. The Verification Squad has no EL — the AVA directs engineers through architectural authority and certification responsibility. If you find yourself managing test execution rather than designing verification architecture, you are not operating at the right level.

---

## 1. Success in the Role

### First 90 Days (or First Increment)

- **Co-design with EA:** Meet your EA peer and jointly define the system-under-test boundary, the integration seams that require assembly-level verification, and the assembly acceptance criteria. The architecture determines what "correct assembly" means — you translate that into verifiable criteria.
- **Design the verification architecture:** Define the verification strategy, test environment topology, test data model, and CI orchestration. This is architecture work — treat it with the same rigour you would apply to the functional system architecture.
- **Establish the Verification Squad:** If a dedicated Verification Squad is activated, you direct it. You are not an EL — direction comes through your architectural authority and certification responsibility. Engineers in the Verification Squad build verification infrastructure (IaC environment definitions, test suites, test data preparation, CI orchestration), not "test cases."
- **Define certification criteria:** What must be true for you to certify an increment for release? Define it early, communicate it to ELs and EPM, and enforce it consistently. If the criteria change mid-Build, communicate the change.
- **Understand the release coordination model:** You certify (decide *whether* the assembly can be released); SRE Lead deploys (manages *how* it is released). This boundary is fundamental — do not blur it.

### What "Good" Looks Like

- The verification module is a first-class artifact — maintained with the same rigour as functional code, versioned, and evolving with each increment.
- Every increment is certified against defined criteria. Release decisions are based on evidence, not opinion or pressure.
- The system-under-test boundary is accurate and current — what is inside (real deployed components), what is simulated at the edges, and the boundary evolves as the assembly grows.
- ELs know the mandatory review scope (assembly-impacting changes) and bring work for review proactively.
- Release-block authority is exercised when warranted and respected by the team. The hardest measure of AVA success is: when you block, no one is surprised, because the criteria were clear from the start.
- At Transfer, the verification module (test suites, environment definitions, test data tooling, CI orchestration, certification records) is a complete, handoverable deliverable.

### Key Relationships

| Role | What You Need from Them | What They Need from You |
|------|------------------------|------------------------|
| EA | Architecture clarity, system-under-test boundary co-design, integration topology | Verification perspective, assembly acceptance criteria, certification feedback |
| ELs | Assembly-impacting changes for review, testing infrastructure support, squad-level test quality | Mandatory review feedback, verification requirements, clear certification criteria |
| EPM | Release coordination, schedule, commercial context for release timing | Certification status, release readiness, release-block decisions with rationale |
| SRE Lead | Deployment mechanics, environment promotion, production readiness | Release certification (you certify; SRE deploys) |
| EO | Backing for release-block authority, Verification Squad resourcing, governance event documentation | Certification status, risk assessment, governance event input |
| Verification Squad engineers | Implementation of verification infrastructure, test automation | Architecture direction, design guidance, certification criteria |

### Performance Input and the Dual Axis

Your functional home is **Architecture** (or **Engineering** if you are a Staff/Principal Engineer playing AVA). Architecture leadership evaluates your growth — certification track record, verification module quality, multi-Engagement experience. EO provides execution-axis input. Request feedback from EA (on co-design quality), EPM (on release coordination effectiveness), and SRE Lead (on the certification → deployment handoff).

---

## 2. Expected Interactions, Tensions, and How to Navigate

### AVA ↔ EA

**Tension:** You are peer architects with different domains. Disagreements on architecture scope (what EA should have designed) vs. verification scope (what you need to verify) are normal. The architecture may not be fully verifiable as defined — requiring AVA to push back.

**How to navigate:**
- Architecture decisions: EA prevails. If you believe the architecture makes verification impractical, raise it as a risk in co-design — before the architecture is implemented.
- Verification and release decisions: you prevail. If EA disagrees with your certification criteria, the path is: EPM mediates → EO decides.
- Co-design early and continuously. The system-under-test boundary is not a one-time decision — it evolves as the assembly evolves.

### AVA ↔ EPM

**Tension:** You may need to block a release under commercial and customer pressure. EPM owns the customer-facing timeline and may push for release.

**How to navigate:**
- Make certification criteria visible from the start. If EPM and the team know the criteria and see the status throughout Build, a release block should never be a surprise.
- When you block: provide evidence (what criteria are not met, what the risk of releasing is, what remediation is needed). A release block without evidence erodes trust.
- If EPM disputes the block, the path is: EPM mediates → EO decides. An EO override of your release block is a **governance event** documented in the decision log. This is by design — it creates accountability.

### AVA ↔ ELs

**Tension:** You require mandatory review of assembly-impacting changes. ELs may see this as overhead that slows their squads.

**How to navigate:**
- Define "assembly-impacting" clearly — integration seams, cross-squad interfaces, configuration correctness, deployment topology. Not every change is assembly-impacting. If ELs are bringing everything for review, the scope definition is too broad.
- Review quickly. If your review turnaround is slow, ELs will stop bringing work proactively. Make mandatory review efficient — ideally same-day for well-prepared submissions.

### AVA ↔ SRE Lead

**Tension:** You certify; SRE deploys. The boundary is clear but the handoff must be explicit — certification status, deployment sequencing, rollback criteria.

**How to navigate:**
- Define the certification → deployment protocol: what artifacts does SRE Lead need from you (certification record, release notes, known issues)? What does SRE Lead need to confirm (operational readiness, deployment sequence)?
- If SRE Lead identifies an operational concern that affects release readiness, treat it as verification-relevant input. Operational readiness and assembly quality are related.

---

## 3. Escalation: Dos and Don'ts

**Do:**

- Exercise **release-block authority** when assembly quality criteria are not met. This authority is independent — Client Partner, EO, EPM, and EA cannot override it. If you block, document the evidence and remediation needed.
- Escalate architecture disputes with EA to **EPM** (EPM mediates per the [escalation model](../../governance.md#escalation-model)).
- When EO overrides your release block, ensure it is documented as a **governance event** in the decision log. This is not insubordination — it is the model working as designed.

**Don't:**

- Use release-block authority as leverage for non-verification concerns (e.g. blocking release because you disagree with an architecture decision that is EA's domain). Release-block authority is about assembly quality — not a general veto.
- Direct functional squad engineers (outside the Verification Squad). Mandatory review is your mechanism; directing is EL's responsibility. If an EL is not sending assembly-impacting work for review, escalate to EPM.
- Allow certification criteria to drift silently. If criteria change, communicate to EPM, ELs, and EO. Surprises at release time destroy trust.
- Treat the Verification Squad as a test team. They build verification infrastructure — IaC, CI orchestration, test data, automation. If the work looks like manual test execution, you have a design problem.

---

## 4. Further Learning

**Internal references:**
- [Roles and Responsibilities — AVA](../../roles.md#assembly-verification-architect-ava)
- [Mandatory Architect Consultation](../../roles.md#mandatory-architect-consultation)
- [Verification and Certification](../../verification-and-certification.md)
- [Governance — AVA Release-Block Authority](../../governance.md#ava-release-block-authority)
- [Architecture Function Guide](../functions/architecture.md) — career progression and architecture vs. technical architecture

**External references:**

| Resource | Why Relevant |
|----------|--------------|
| *Software Architecture in Practice* — Bass, Clements, Kazman, 4th ed. ([Pearson](https://www.pearson.com/en-us/subject-catalog/p/software-architecture-in-practice/P200000009471/)) | Architecture quality attributes and evaluation; applicable to verification architecture and the AVA's system-level thinking |
| *Just Enough Software Architecture* — Fairbanks ([georgefairbanks.com](https://www.georgefairbanks.com/e-book/)) | Risk-driven architecture; helps calibrate verification depth per Engagement |
| *Site Reliability Engineering* — Google ([sre.google/sre-book](https://sre.google/sre-book/table-of-contents/)) | Operational reliability principles; relevant to the AVA ↔ SRE Lead relationship and understanding operational readiness criteria. Free online. |
| *Solution Architecture Foundations* — Hewitt ([Packt](https://www.packtpub.com/en-us/product/solution-architecture-foundations-9781838820688)) | Solution architecture practice; applicable to the AVA's system-level verification design |

---

[← Back to Career Guides](../README.md)
