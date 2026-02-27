# Engagement Program Manager (EPM) — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#engagement-program-manager-epm)

---

## 1. Success in the Role

### First 90 Days (or First Increment)

- **Build the integrated view:** Establish the reporting cadence across all squads (CP, Studio, PL). Collect scope, timeline, risk, and dependency information from every EL. Do not wait for ELs to come to you — design a lightweight, repeatable cadence (weekly sync, shared status format) that ELs can sustain alongside their squad work.
- **Understand the commercial baseline:** Review contract terms, scope, and any existing scope-commercial misalignment. Meet with Account Management to understand the commercial relationship. You are not a negotiator — you ensure delivery and commercial are in sync.
- **Align with Client Partner and EO:** Understand the communication split — Client Partner leads relationship strategy; you lead delivery communication. EO provides strategic direction; you provide operational execution. Agree on what the client hears from you vs. from the Client Partner.
- **Establish Engagement Success ownership:** Engagement Success — readiness, adoption, and value delivery — is your function. Begin planning for customer training and enablement early (even at Discover), not as an afterthought at Transfer.
- **Activate staffing coordination:** Work with ELs and PPM to ensure squad staffing requests are submitted, consolidated, and tracked. You serve ELs on staffing needs and rotation coordination.

### What "Good" Looks Like

- You can answer "how is this Engagement doing?" at any time — scope, timeline, risk, dependencies, commercial alignment — without chasing ELs or EA.
- The customer receives consistent, accurate delivery communication from you. The Client Partner is briefed before governance meetings without being surprised.
- Engagement Success is planned from Discover — training, enablement, adoption metrics, and value delivery are on the roadmap, not bolted on at Transfer.
- Scope changes are managed — every change is assessed for commercial impact, communicated to Account Management, and documented.
- ELs and Scrum Masters work through you for cross-squad coordination. Escalations reach EO only when you have tried and cannot resolve.
- Commercial and delivery are in sync — no surprises for AM, Client Partner, or the customer.

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

### Performance Input and the Dual Axis

Your functional home is **Program / Delivery Management**. Delivery leadership evaluates your career growth across Engagements — multi-Engagement delivery record, Engagement Success outcomes, process maturity. EO provides execution-axis input on your effectiveness within the current Engagement. Request feedback from EO, Client Partner, and EA after each major milestone. Client Partner feedback on customer-facing communication quality is particularly valuable.

---

## 2. Expected Interactions, Tensions, and How to Navigate

### EPM ↔ EO

**Tension:** EO owns overall accountability; you own the operational execution. The boundary between "EPM resolves" and "EO intervenes" is judgment-dependent. Too much EO involvement undermines your authority; too little lets problems grow.

**How to navigate:**
- Escalate to EO when you have tried to resolve and cannot, or when the issue exceeds your authority (portfolio impact, ERC-level decisions, Client Partner disputes).
- Present escalations with data, options, and a recommendation — not just the problem. EO needs your assessment to decide, not a raw dump.

### EPM ↔ Client Partner

**Tension:** Both of you are customer-facing. You own delivery communication; Client Partner owns relationship strategy. The boundary is clear in theory but blurry in practice, especially during governance meetings and customer escalations.

**How to navigate:**
- Agree on the communication split early and revisit it at every major milestone. Who leads the governance meeting? Who handles the follow-up? Who fields the ad-hoc client call?
- If a client escalation arrives, coordinate with Client Partner before responding. The worst outcome is contradictory messages.
- When Client Partner makes client-facing commitments that affect delivery (scope, timeline), bring to EO for assessment. Do not absorb the commitment silently.

### EPM ↔ ELs

**Tension:** ELs own squad delivery; you own the integrated view. You need process consistency and cross-squad coordination; ELs want squad autonomy. Both are legitimate. Per the [escalation model](../../governance.md#escalation-model), when EPM and EL disagree on squad-level decisions, **EL prevails** — the escalation path is EA (for architecture-related disputes), then EO.

**How to navigate:**
- Set minimum coordination requirements (e.g. weekly status, dependency flags, risk escalation) but let ELs manage their squads internally. If an EL's squad misses a dependency, address it through the coordination mechanism, not by micromanaging the squad.
- Inner source contributions (prioritised by EA) affect EL timelines. When EA and EL disagree on inner source priority, mediate by surfacing the timeline impact to both sides. You hold the integrated timeline; use it.

### EPM ↔ EA

**Tension:** EA's inner source priorities and mandatory review requirements affect delivery timelines. You need predictability; EA needs architecture integrity.

**How to navigate:**
- Include inner source timelines and mandatory review overhead in your integrated plan from the start. If they are surprises, the plan was incomplete.
- When inner source contributions cause timeline slip, bring EA and the affected EL together. The trade-off (deliver now with custom build vs. contribute to PL with timeline cost) is a business decision that you mediate and, if necessary, escalate to EO.

### EPM ↔ AM

**Tension:** You ensure delivery-commercial alignment. Account Management owns the commercial relationship. Scope creep, contract amendments, and change orders sit at the intersection.

**How to navigate:**
- Surface scope changes to AM early with delivery impact. Do not negotiate commercial terms — flag and coordinate. If a scope change affects commercial terms, AM leads the negotiation; you provide the delivery data.

---

## 3. Escalation: Dos and Don'ts

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
- Commit delivery timelines to the client without confirming with ELs and EA. A timeline commitment is a promise — make sure it is one you can keep.

---

## 4. Further Learning

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
| *Making the Matrix Work* — Hall ([Nicholas Brealey](https://www.nicholasbrealey.com/making-the-matrix-work)) | Matrix organisation dynamics; applicable to the dual-axis model, multiple authorities, and the EPM's position at the intersection |

---

[← Back to Career Guides](../README.md)
