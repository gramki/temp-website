# Engagement Owner (EO) — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#engagement-owner-eo)

---

## 1. Success in the Role

### First 90 Days (or First Increment)

- **Understand the Engagement context:** Review the archetype in use, the gap analysis, the customer's operating model choice, and the commercial terms. You own overall Engagement outcomes — delivery, quality, customer satisfaction — so you need the full picture before directing anyone.
- **Align with Client Partner:** Establish the authority boundary — Client Partner owns client-facing decisions; you retain full internal delivery authority. Agree on communication protocols and escalation triggers. If the Client Partner is already established with the client, learn the relationship history.
- **Assess your leadership team:** Meet EPM, EA, AVA, EPO, SRE Lead individually. Understand each person's strengths, concerns, and where they need support. Your job is to lead through them, not around them.
- **Set the escalation culture:** Make clear that EPM is the first escalation point for cross-role disputes within the Engagement. You are the final escalation endpoint within the Engagement — but you should rarely be the first person to hear about a problem.
- **Understand your heritage bias:** ERC assigns EOs based on heritage (Architecture, Delivery, or Engineering). Know your own heritage and its blind spot. Architecture-heritage EOs may over-index on technical decisions; Delivery-heritage EOs may over-index on process; Engineering-heritage EOs may over-index on squad-level concerns. Compensate by leaning on the team member who covers your blind spot.

### What "Good" Looks Like

- EPM, EA, AVA, EPO, and SRE Lead are empowered and effective — you intervene rarely and only when escalation reaches you. If you are solving every problem, your team is not working.
- Client Partner trusts you on delivery — they do not need to check on squads or architecture decisions because your assessment is reliable and timely.
- Delivery, quality, and customer satisfaction outcomes are on track — when they are not, you have early warning (through EPM's integrated view) and a plan.
- Portfolio impact is managed — your decisions on this Engagement do not silently consume capacity that other Engagements need. You surface trade-offs to ERC and PPM.
- The escalation model is working — disputes are resolved at the lowest appropriate level; you get only what EPM could not resolve.

### Key Relationships

| Role | What You Need from Them | What They Need from You |
|------|------------------------|------------------------|
| Client Partner | Client context, stakeholder priorities, commercial constraints | Honest delivery assessment, early risk signals, recommended options |
| EPM | Integrated progress view, risk register, commercial alignment status | Decision-making on escalated issues, systemic blocker removal, ERC representation |
| EA | Architecture assessment, gap register, inner source status, quality standards | Resourcing support, timeline protection for architecture work, backing for inner source bar |
| AVA | Certification status, release readiness, verification gaps | Backing for release-block authority, Verification Squad resourcing |
| EPO | Requirements quality, customer discovery findings, training readiness | Customer access, priority decisions when requirements exceed capacity |
| SRE Lead | Operational readiness status, release mechanics plan | Timeline for operational readiness activities, backing for operational sign-off authority |
| ERC | Role assignment, capacity coordination, escalation resolution | Engagement performance reporting, capacity needs, formation feedback |

### Performance Input and the Dual Axis

Your functional home may be **Architecture**, **Delivery**, or **Engineering** — wherever your heritage lies. Your functional-axis leader evaluates your career growth across EO assignments. Client Partner provides execution-axis input on your Engagement effectiveness. Request explicit feedback from Client Partner, EPM, and EA after each major milestone.

---

## 2. Expected Interactions, Tensions, and How to Navigate

### EO ↔ Client Partner

**Tension:** Client Partner wants to satisfy the client; you own what is technically and operationally feasible. The client wants more, faster; you may need to say "not in this timeline" or "not with this quality level."

**How to navigate:**
- When delivery decisions affect client commitments → you recommend; Client Partner decides. Give a clear recommendation with options, not just a "no."
- When client demands affect delivery feasibility → Client Partner brings to you; you assess. Be honest about impact — understating risk to keep Client Partner happy creates a bigger problem later.
- If you and Client Partner cannot agree, the escalation endpoint is **ERC** (which assigned both of you). Bring data, options, and a recommendation to ERC — not a complaint.

### EO ↔ EPM

**Tension:** EPM owns the integrated view and the customer-facing communication. You own overall accountability. The boundary between "EPM resolves" and "EO intervenes" is judgment-dependent.

**How to navigate:**
- Default: let EPM resolve. Intervene only when EPM escalates to you or when you see a risk that EPM has not surfaced.
- Over-involvement undermines EPM's authority and creates dependency. Under-involvement lets problems fester. The signal to intervene is when EPM has tried and failed, or when the issue is beyond EPM's authority (e.g. cross-Engagement portfolio impact, ERC-level decisions).

### EO ↔ EA / AVA

**Tension:** EA and AVA may flag architecture or quality concerns that delay delivery. You face pressure from Client Partner and commercial timelines.

**How to navigate:**
- Back EA's inner source bar and AVA's release-block authority by default. These authorities exist because shortcuts here create downstream cost (tech debt, assembly failures, post-release incidents).
- If you believe an AVA release block should be overridden, you have the authority — but it is a **governance event** that must be documented in the decision log. Use it only when the business impact of not releasing exceeds the quality risk, and you can articulate that trade-off explicitly.

### EO ↔ ERC

**Tension:** ERC provides ingredients of success (capacity, role assignments) and expects Engagement performance. You may need more capacity, different role assignments, or priority adjustments.

**How to navigate:**
- Bring needs early, with data. ERC mediates across Engagements — if you surface a capacity need late, it affects other Engagements.
- Accept ERC's portfolio-level decisions even when they constrain your Engagement. If you disagree, advocate with data — but the portfolio view may see things you do not.

---

## 3. Escalation: Dos and Don'ts

**Do:**

- Serve as the **final escalation endpoint within the Engagement** for all role-level disputes ([governance.md](../../governance.md#escalation-model)).
- Escalate to **ERC** when: capacity conflicts require portfolio-level resolution, Client Partner ↔ EO disagreements are unresolvable, or Engagement-level risks exceed your authority.
- Before overriding any role-level authority (especially AVA release-block), ensure it is documented as a governance event in the decision log.

**Don't:**

- Bypass EPM to direct ELs, Squad PMs, or Scrum Masters. The execution hierarchy exists for a reason — work through it.
- Override AVA release-block authority casually. It is your prerogative, but it is a governance event with consequences. If you override frequently, the verification system is providing signal you are ignoring.
- Absorb all escalations personally. If EPM can resolve it, let EPM resolve it. Your job is to lead the system, not to be the system.
- Escalate to Architecture leadership or Engineering leadership to override EA or EL decisions. The execution axis goes through you, not through functional leaders. Use the functional axis for career development, not for Engagement execution.

---

## 4. Further Learning

**Internal references:**
- [Roles and Responsibilities — EO](../../roles.md#engagement-owner-eo)
- [Engagement Formation — EO Heritage Matching](../../engagement-formation.md)
- [Career Paths — Convergence at EO](../../career-paths.md#6-convergence-at-eo)
- [Governance and Escalation](../../governance.md) — full escalation model
- [Client Partner ↔ EO Authority Boundary](../../roles.md#client-partner--eo-authority-boundary)

**External references:**

| Resource | Why Relevant |
|----------|--------------|
| *Making the Matrix Work* — Hall ([Nicholas Brealey](https://www.nicholasbrealey.com/making-the-matrix-work)) | Matrix organisation dynamics; directly applicable to the EO's position leading through EPM/EA/AVA without direct control, and navigating dual-axis reporting |
| *Agile and Lean Program Management* — Rothman ([jrothman.com](https://www.jrothman.com/books/agile-and-lean-program-management-scaling-collaboration-across-the-organization/)) | Scaling collaboration across teams; applicable to the multi-squad, cross-function coordination that the EO oversees through EPM |

---

[← Back to Career Guides](../README.md)
