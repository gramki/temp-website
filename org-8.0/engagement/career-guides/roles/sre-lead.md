# SRE Lead — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#sre-lead)

---

The SRE Lead ensures **operational readiness** for the Engagement — monitoring, alerting, runbooks, capacity planning, incident response, and the operational transition. The SRE Lead also owns the **release mechanics**: deployment sequencing, environment promotion, and production cutover. The role is scoped **per-Engagement**. The SRE Lead reports to EO on the execution axis. The functional home is **SRE / Operations**.

---

## 1. Empowerment

- **Operational readiness sign-off.** SRE Lead must approve that operational criteria are met before Transfer. This is an authority, not a rubber stamp — when you approve, it means monitoring, alerting, runbooks, capacity, and incident response are in place.
- **Release mechanics authority.** You own *how* the assembly is released — deployment sequencing, environment promotion, release notes, production cutover, rollback procedures. AVA decides *whether* it can be released (certification); you manage the mechanics.
- **Operational requirements input.** You embed operational thinking (logging, metrics, health checks, graceful degradation) into squad work from Discover. This input shapes EA's architecture decisions.
- **What you cannot override.** You cannot certify assembly quality — that is AVA's authority. You deploy only after AVA certifies. You cannot override AVA's certification decisions.

---

## 2. Assignment

EO assigns the SRE Lead at **Stage 2** ([engagement-formation.md](../../engagement-formation.md#stage-2--eo-assigns-squad-level-leadership-at-initiate--early-discover)). Typically from the dominant Product Line's SRE team or from the SRE/Operations function.

**Scope:** Per-Engagement. One SRE Lead per Engagement.

---

## 3. Ambition

### First 90 Days (or Discover Phase)

- **Assess the operational landscape.** Understand the architecture (from EA), the verification strategy (from AVA), and the operating model choice (Fully Managed, Co-Managed, Customer-Operated). The operating model determines the depth of operational handover required.
- **Define the operational readiness plan.** From Discover, begin identifying monitoring requirements, alerting thresholds, runbook needs, capacity planning, and incident response processes. Operational readiness is not a Transfer activity — it is built incrementally.
- **Establish the release coordination protocol with AVA.** AVA certifies; you deploy. Define the certification → deployment handoff: what artifacts you receive from AVA, what you need to confirm before deployment.
- **Connect with ELs on operational requirements.** Engage with ELs early to embed operational thinking into squad work from the start. Retrofitting operational readiness is harder and more expensive than building it in.
- **Coordinate with EPM.** EPM owns the customer-facing timeline and Engagement Success. You provide the operational readiness status that EPM communicates to the customer and Client Partner.

### What Great Looks Like

- Operational readiness progresses incrementally alongside delivery — monitoring, alerting, and runbooks evolve with each increment, not as a last-minute effort at Transfer.
- The release coordination protocol with AVA is clear, practised, and efficient. AVA certifies; you deploy. No ambiguity about who decides what.
- The operating model handover is planned and resourced. For Fully Managed: you are building for long-term operations. For Customer-Operated: you are building a complete handover package for a team you may never meet.
- Operational readiness sign-off is meaningful — when you approve, it means the system is production-ready.
- Architecture decisions support operability — EA has considered fault isolation, monitoring surface area, and service dependencies based on your input.

---

## 4. Commitments

### Dimensions

| Dimension | SRE Lead SLA |
|---|---|
| **Quality** | Operational readiness criteria are defined and met — monitoring, alerting, runbooks, capacity planning, incident response. Operational readiness sign-off is evidence-based. The release mechanics are reliable — deployments are sequenced correctly, rollback procedures are tested, and production cutover is controlled. |
| **Predictability** | Operational readiness status is visible throughout Build — included in EPM's integrated view. When operational readiness is at risk, early warning is delivered to EPM and EO with impact and remediation plan. Release mechanics are executed on schedule once AVA certifies. |
| **Fitment** | The operational handover matches the contracted operating model (Fully Managed, Co-Managed, Customer-Operated). Runbooks, monitoring, and capacity are appropriate for the customer's operational context. Operational readiness criteria are proportionate to the Engagement's risk profile. |

### Contractual Connection — Tier 2 (Mechanism)

The SRE Lead does not interface with the contract directly, but the operating model is often contractually specified. Operational readiness sign-off is a precondition for Transfer — a contractual milestone. The release mechanics SLA (reliable deployments) underpins the client's confidence in the product's operational maturity. If the contract includes SLAs for uptime, response time, or incident resolution, the SRE Lead's operational readiness work is the mechanism that makes those SLAs achievable.

---

## 5. Collaboration

### Key Relationships

| Role | What You Need from Them | What They Need from You |
|------|------------------------|------------------------|
| AVA | Release certification, certification records, known issues for deployment | Deployment readiness, environment status, rollback confirmation |
| EA | Architecture decisions that support operability, monitoring surface area, fault isolation design | Operational requirements input, deployment topology needs, operability feedback |
| EPM | Customer-facing timeline, Engagement Success context, operational readiness communication | Operational readiness status, release mechanics plan, risk flags |
| ELs | Operational requirements implementation (logging, metrics, health checks), squad-level operational testing | Operational requirements specifications, monitoring configuration guidance |
| EO | Backing for operational readiness sign-off authority, resourcing support | Operational readiness assessment, risk-to-go-live communication |

### Tensions and Navigation

**SRE Lead ↔ AVA.** AVA certifies; you deploy. The boundary is clear but the handoff under time pressure can blur. AVA may certify with conditions; you must decide whether those conditions affect deployment mechanics.

- Define the certification → deployment protocol formally: certification record format, known issues classification (blocking vs. non-blocking for deployment), rollback criteria.
- If AVA certifies with conditions that affect deployment (e.g. "certified for staging only, not production"), confirm explicitly.
- If you identify an operational concern that affects release readiness, surface it to AVA and EPM. Your input is verification-relevant.

**SRE Lead ↔ EA.** Architecture decisions have operational implications. EA may design for functional correctness without fully considering monitoring, fault isolation, or deployment complexity.

- Engage EA during architecture design, not after. Provide operational requirements as input to EA's design decisions.
- If the architecture does not support adequate monitoring or fault isolation, raise it as a risk. If EA deprioritises, escalate through EPM.

**SRE Lead ↔ EPM.** EPM wants predictability and a go-live date. You need operational readiness to be confirmed before Transfer.

- Make operational readiness status visible throughout Build — include it in the integrated view that EPM maintains.
- When operational readiness is not on track, flag early with impact and remediation plan.

**SRE Lead ↔ ELs.** You need engineers to implement operational requirements (logging, metrics, health checks). ELs may see these as lower priority than functional delivery.

- Frame operational requirements as squad Definition of Done items, with EA's backing.
- Provide clear, implementable specifications — not "add monitoring" but "emit metrics at these endpoints, with these labels, at this frequency."

---

## 6. Management

### Dual-Axis Reporting

- **Execution axis:** Reports to **EO**. EO provides execution-axis input on your effectiveness within the Engagement.
- **Functional/career axis:** **SRE / Operations leadership** evaluates your growth across Engagements — multi-Engagement operational record, operating model breadth, release coordination quality.

### Performance Input

Request feedback from EPM on operational readiness communication and its impact on Engagement Success. AVA provides feedback on the certification → deployment handoff quality. SRE leadership evaluates your trajectory across Engagements, particularly your ability to handle increasingly complex operating models.

---

## 7. Accountability

### Escalation: Dos and Don'ts

**Do:**

- Exercise **operational readiness sign-off authority** — SRE Lead must approve that operational criteria are met before Transfer ([governance.md](../../governance.md#transfer-readiness)). This is an authority, not a suggestion.
- Escalate architecture-operations misalignment to **EPM** (who mediates between EA and SRE Lead) and then to **EO** if unresolved.
- Raise go-live readiness concerns to **EO** when operational readiness is at risk and remediation requires Engagement-level decisions.

**Don't:**

- Confuse your authority with AVA's authority. You sign off on operational readiness; AVA certifies assembly quality. These are complementary, not interchangeable.
- Deploy without AVA certification. You manage *how* the assembly is released — but *whether* it can be released is AVA's decision.
- Wait until Transfer to reveal operational readiness gaps. EPM and EO need early warning to adjust plans.
- Accept "we'll do runbooks later" from the team. Runbooks deferred past Transfer become operational risk that falls on whoever runs the system in production.

### When Commitments Are Missed

SRE Lead commitments are primarily **commitment-based** (per the [accountability framework](../../people-and-culture/accountability.md)): operational readiness criteria, release mechanics reliability, and operational readiness communication are binary — ready or not ready, on time or late. When operational readiness is not on track (e.g. monitoring is incomplete at Transfer), the response is immediate transparency, impact assessment, and a remediation plan. The SRE Lead's reliability is measured by whether the go-live is operationally sound, not by whether problems existed during Build.

---

## 8. Objectives in Perspective

The SRE Lead's immediate objectives — operational readiness, release mechanics, go-live preparedness — serve a broader purpose: ensuring that what the Engagement builds can actually run in production, and that whoever runs it (internal operations, the customer's team, or a co-managed arrangement) has what they need.

The most common failure mode in Engagement delivery is building a product that works in the development environment but is not ready for production — incomplete monitoring, missing runbooks, untested rollback procedures, no capacity planning. The SRE Lead exists to prevent this. Your work transforms a development artifact into an operational product.

The operating model choice (Fully Managed, Co-Managed, Customer-Operated) determines the depth of this transformation. A Fully Managed handover means you are building for your own operations team. A Customer-Operated handover means you are building for a team you may never meet — the documentation, training, and operational tooling must be complete enough for someone else to run it without your help. The SRE Lead who treats all operating models the same has missed the point.

---

## Further Learning

**Internal references:**
- [Roles and Responsibilities — SRE Lead](../../roles.md#sre-lead)
- [Governance — Go-Live Readiness](../../governance.md#go-live-readiness) and [Transfer Readiness](../../governance.md#transfer-readiness)
- [Engagement Formation](../../engagement-formation.md) — SRE Lead assignment at Stage 2
- [SRE / Operations Function Guide](../functions/sre-operations.md) — career progression in the SRE function

**External references:**

| Resource | Why Relevant |
|----------|--------------|
| *Site Reliability Engineering* — Google ([sre.google/sre-book](https://sre.google/sre-book/table-of-contents/)) | Definitive SRE reference; directly applicable to monitoring, alerting, incident response, and operational handover. Free online. |
| *The Site Reliability Workbook* — Google ([sre.google/workbook](https://sre.google/workbook/table-of-contents/)) | Practical companion; useful for operational readiness checklists, incident management, and post-incident review processes. Free online. |

---

[← Back to Career Guides](../README.md)
