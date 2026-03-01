# Engagement Program Manager (EPM) — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#engagement-program-manager-epm)

---

The EPM is the **primary customer-facing contact** for the Engagement, responsible for the integrated progress/risk/dependency view, commercial alignment, and the **Engagement Success** function (readiness, adoption, value delivery). The role is scoped **per-Engagement**. The EPM reports to EO on the execution axis and directs ELs and Scrum Masters. The functional home is **Program / Delivery Management**.

---

## 1. Empowerment

- **Customer-facing delivery communication.** You are the Engagement's voice to the customer on delivery progress, risks, and dependencies.
- **Integrated progress view.** You own the cross-squad view — scope, timeline, risk, dependencies, commercial alignment. No other role has this synthesis.
- **First escalation point for cross-role disputes.** EA ↔ AVA, EPO ↔ EA, EL ↔ EL cross-squad dependencies — you mediate before anything reaches EO.
- **Commercial alignment.** You ensure delivery scope and contract terms remain in sync. Scope changes are assessed for commercial impact and communicated to Account Management.
- **Engagement Success function.** You own readiness, adoption, and value delivery beyond engineering completion — not just "is it built?" but "is it working for the customer?"
- **What you cannot override.** You cannot override EA's mandatory review or inner source bar. You cannot override AVA's release-block authority — even under commercial pressure, the path is mediation → EO decides.

---

## 2. Assignment

ERC assigns the EPM at **Stage 1** ([engagement-formation.md](../../engagement-formation.md#stage-1--erc-assigns-engagement-leadership-at-initiate)). ERC matches designation level to Engagement complexity. A person may serve as EPM for multiple Engagements if bandwidth permits.

**Scope:** Per-Engagement. One EPM per Engagement.

**Scaling:** For large Engagements (6+ squads), Stream Delivery Leads may be introduced from the Program/Delivery function. Each Stream DL manages 2-4 squads; the EPM coordinates across streams and retains the integrated view and customer-facing accountability.

---

## 3. Ambition

### First 90 Days (or First Increment)

- **Build the integrated view.** Establish the reporting cadence across all squads (CP, Studio, PL). Collect scope, timeline, risk, and dependency information from every EL. Do not wait for ELs to come to you — design a lightweight, repeatable cadence that ELs can sustain alongside their squad work.
- **Understand the commercial baseline.** Review contract terms, scope, and any existing scope-commercial misalignment. Meet with Account Management to understand the commercial relationship. You are not a negotiator — you ensure delivery and commercial are in sync.
- **Align with Client Partner and EO.** Understand the communication split — Client Partner leads relationship strategy; you lead delivery communication. EO provides strategic direction; you provide operational execution.
- **Establish Engagement Success ownership.** Engagement Success — readiness, adoption, and value delivery — is your function. Begin planning for customer training and enablement early (even at Discover), not as an afterthought at Transfer.
- **Activate staffing coordination.** Work with ELs and PPM to ensure squad staffing requests are submitted, consolidated, and tracked.

### What Great Looks Like

- You can answer "how is this Engagement doing?" at any time — scope, timeline, risk, dependencies, commercial alignment — without chasing ELs or EA.
- The customer receives consistent, accurate delivery communication from you. The Client Partner is briefed before governance meetings without being surprised.
- Engagement Success is planned from Discover — training, enablement, adoption metrics, and value delivery are on the roadmap, not bolted on at Transfer.
- Scope changes are managed — every change is assessed for commercial impact, communicated to Account Management, and documented.
- ELs and Scrum Masters work through you for cross-squad coordination. Escalations reach EO only when you have tried and cannot resolve.

---

## 4. Commitments

### Dimensions

| Dimension | EPM SLA |
|---|---|
| **Predictability** | The integrated progress view is accurate and current. Milestone commitments are forecasted reliably. When milestones are at risk, early warning is delivered to EO and Client Partner with impact and options — not a last-minute surprise. Sprint commitment accuracy across squads is tracked and trended. |
| **Velocity** | Cross-squad throughput is monitored and systemic impediments are resolved at the Engagement level. Dependency bottlenecks across squads are identified and unblocked. Inner source timeline impact is included in the integrated plan from the start. |
| **Cost** | Scope changes are assessed for commercial impact before they are accepted. Delivery scope and contract terms remain in sync. Budget burn rate is tracked and communicated. Scope-commercial misalignment is flagged to Account Management before it becomes a dispute. |

### Contractual Connection — Tier 1 (Direct)

The EPM ensures delivery-commercial alignment. When SLA trends indicate risk to a contractual milestone, the EPM escalates to EO and Client Partner with data and options. Scope change cycle time — the speed at which a scope change is assessed, costed, and communicated to AM — is a direct measure of the EPM's contribution to contractual integrity. Engagement Success outcomes (adoption, value delivery) are often contractual.

---

## 5. Collaboration

### Key Relationships

| Role | What You Need from Them | What They Need from You |
|------|------------------------|------------------------|
| EO | Strategic direction, systemic blocker removal, decision on escalated issues | Integrated progress view, risk register, recommended actions on escalated issues |
| Client Partner | Client context, stakeholder priorities, governance coordination | Delivery status, risk communication, Engagement Success progress |
| EA | Architecture status, gap register, inner source impact on timeline, quality standards | Timeline reality, resourcing awareness, scope change impact on architecture |
| AVA | Certification status, release readiness, verification gaps | Release coordination, schedule communication, mediation for AVA ↔ EL disputes |
| ELs | Squad-level progress, risks, blockers, staffing needs | Cross-squad coordination, priority resolution, staffing coordination through PPM |
| EPO | Requirements flow, customer discovery findings, training/enablement plan | Customer alignment, scope change management, Engagement Success coordination |
| SRE Lead | Operational readiness status, release mechanics plan | Timeline for operational readiness activities, customer-facing communication of operational status |
| Scrum Masters | Process health across squads, impediment escalation | Process expectations, cross-squad alignment, EPM-level impediment resolution |
| Account Management | Commercial terms, contract status, scope change implications | Scope change notifications, delivery-commercial alignment status |

### Tensions and Navigation

**EPM ↔ EO.** EO owns overall accountability; you own operational execution. Too much EO involvement undermines your authority; too little lets problems grow.

- Escalate to EO when you have tried to resolve and cannot, or when the issue exceeds your authority (portfolio impact, ERC-level decisions, Client Partner disputes).
- Present escalations with data, options, and a recommendation — not just the problem.

**EPM ↔ Client Partner.** Both of you are customer-facing. You own delivery communication; Client Partner owns relationship strategy.

- Agree on the communication split early and revisit it at every major milestone.
- If a client escalation arrives, coordinate with Client Partner before responding.
- When Client Partner makes client-facing commitments that affect delivery, bring to EO for assessment. Do not absorb the commitment silently.

**EPM ↔ ELs.** ELs own squad delivery; you own the integrated view. You need process consistency and cross-squad coordination; ELs want squad autonomy. Per the [escalation model](../../governance.md#escalation-model), when EPM and EL disagree on squad-level decisions, **EL prevails** — the escalation path is EA (for architecture-related disputes), then EO.

- Set minimum coordination requirements but let ELs manage their squads internally.
- Inner source contributions (prioritised by EA) affect EL timelines. When EA and EL disagree on inner source priority, mediate by surfacing the timeline impact to both sides.

**EPM ↔ EA.** EA's inner source priorities and mandatory review requirements affect delivery timelines. You need predictability; EA needs architecture integrity.

- Include inner source timelines and mandatory review overhead in your integrated plan from the start.
- When inner source contributions cause timeline slip, bring EA and the affected EL together. The trade-off is a business decision that you mediate and, if necessary, escalate to EO.

---

## 6. Management

### Dual-Axis Reporting

- **Execution axis:** Reports to **EO**. EO provides execution-axis input on your effectiveness within the current Engagement.
- **Functional/career axis:** **Delivery leadership** evaluates your career growth across Engagements — multi-Engagement delivery record, Engagement Success outcomes, process maturity.

### Performance Input

Request feedback from EO, Client Partner, and EA after each major milestone. Client Partner feedback on customer-facing communication quality is particularly valuable. Delivery leadership evaluates your trajectory across Engagements — the ability to handle increasing complexity, multi-squad coordination, and Engagement Success maturity.

---

## 7. Accountability

### Escalation: Dos and Don'ts

**Do:**

- Serve as the **first escalation point for cross-role disputes** within the Engagement ([governance.md](../../governance.md#escalation-model)).
- Resolve EA ↔ AVA disputes (architecture → EA prevails; verification/release → AVA prevails) and EPO ↔ EA disputes (EA prevails) per the escalation model before escalating to EO.
- Escalate to **EO** when: you have tried and cannot resolve, or the issue exceeds your authority (portfolio impact, Client Partner disputes, systemic blockers).
- Mediate AVA release blocks under commercial pressure — if the release block is disputed, the path is: you mediate → EO decides. Document the governance event.

**Don't:**

- Escalate to EO without trying to resolve first. EO should rarely be your first call.
- Bypass ELs to direct engineers. The execution hierarchy exists — ELs direct their squads; you coordinate across squads.
- Override EA's mandatory review or inner source bar. EA owns engineering quality standards; if you disagree with the priority, mediate and escalate to EO if needed.
- Override AVA's release-block authority. Even under customer and commercial pressure, the path is mediation → EO decides. You cannot override independently.
- Commit delivery timelines to the client without confirming with ELs and EA.

### When Commitments Are Missed

The EPM carries both types of accountability (per the [accountability framework](../../people-and-culture/accountability.md)):

- **Outcome-based:** Engagement Success (adoption, value delivery) — these are uncertain and depend on customer actions you can influence but not control. When adoption lags, the response is diagnosis and adjustment, not blame.
- **Commitment-based:** Milestone delivery, commercial alignment, scope change cycle time — these are binary. When a milestone is missed or a scope change creates a commercial surprise, the response is immediate transparency to EO and Client Partner, impact containment, and a revised plan. The EPM's reliability is measured by whether surprises happen, not by whether problems exist.

---

## 8. Objectives in Perspective

The EPM sits at the intersection of delivery, commercial, and customer success. Your immediate objectives — accurate forecasting, commercial alignment, impediment resolution — serve a broader purpose: enabling the Engagement to deliver a customer-specific product instantiation that the client adopts and values.

When you manage scope changes rigorously, you protect Account Management from commercial surprises and the client from unmet expectations. When you drive Engagement Success from Discover (not Transfer), you ensure that what is built is actually used — which is the ultimate measure of Engagement value.

The EPM who delivers on time but ignores adoption has completed a project. The EPM who delivers on time and ensures the customer is ready, trained, and deriving value has completed an Engagement.

---

## Further Learning

**Internal references:**
- [Roles and Responsibilities — EPM](../../roles.md#engagement-program-manager-epm)
- [Engagement Formation — Stage 1 and Stage 2](../../engagement-formation.md)
- [Governance and Escalation](../../governance.md) — full escalation model, scope change management, commercial alignment
- [Engagement Success](../../engagement-definition.md) — EPM's Engagement Success function

**External references:**

| Resource | Why Relevant |
|----------|--------------|
| *Practical Customer Success Management* — Adams ([Amazon](https://www.amazon.com/Practical-Customer-Success-Management-Scientist/dp/0367183390)) | Customer success framework; directly applicable to the Engagement Success function the EPM owns — readiness, adoption, and value delivery beyond engineering completion |
| *Agile and Lean Program Management* — Rothman ([jrothman.com](https://www.jrothman.com/books/agile-and-lean-program-management-scaling-collaboration-across-the-organization/)) | Multi-team coordination and scaling collaboration; directly maps to the EPM's cross-squad orchestration and integrated view |
| *Making the Matrix Work* — Hall ([Nicholas Brealey](https://www.hachette.co.uk/titles/kevan-hall/making-the-matrix-work/9781904838425/)) | Matrix organisation dynamics; applicable to the dual-axis model, multiple authorities, and the EPM's position at the intersection |

---

[← Back to Career Guides](../README.md)
