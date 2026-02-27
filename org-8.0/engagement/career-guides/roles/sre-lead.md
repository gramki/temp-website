# SRE Lead — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#sre-lead)

---

## 1. Success in the Role

### First 90 Days (or Discover Phase)

- **Assess the operational landscape:** Understand the architecture (from EA), the verification strategy (from AVA), and the operating model choice (Fully Managed, Co-Managed, Customer-Operated). The operating model determines the depth of operational handover required — a Customer-Operated handover is an order of magnitude more documentation-intensive than a Fully Managed setup.
- **Define the operational readiness plan:** From Discover, begin identifying monitoring requirements, alerting thresholds, runbook needs, capacity planning, and incident response processes. Operational readiness is not a Transfer activity — it is built incrementally from Discover through Build.
- **Establish the release coordination protocol with AVA:** AVA certifies the assembly (decides *whether* it can be released); you manage the mechanics (deployment sequencing, environment promotion, production cutover, rollback procedures). Define the certification → deployment handoff: what artifacts you receive from AVA, what you need to confirm before deployment.
- **Connect with ELs on operational requirements:** Engage with ELs early to embed operational thinking (logging, metrics, health checks, graceful degradation) into squad work from the start. Retrofitting operational readiness is harder and more expensive than building it in.
- **Coordinate with EPM:** EPM owns the customer-facing timeline and Engagement Success. You provide the operational readiness status that EPM communicates to the customer and Client Partner.

### What "Good" Looks Like

- Operational readiness progresses incrementally alongside delivery — monitoring, alerting, and runbooks evolve with each increment, not as a last-minute effort at Transfer.
- The release coordination protocol with AVA is clear, practised, and efficient. AVA certifies; you deploy. No ambiguity about who decides what.
- The operating model handover is planned and resourced. For Fully Managed: you are building for long-term operations. For Customer-Operated: you are building a complete handover package (documentation, training, support runbook) for a team you may never meet.
- Operational readiness sign-off is meaningful — when you approve, it means monitoring, alerting, runbooks, capacity, and incident response are in place. It is an authority, not a rubber stamp.
- Architecture decisions support operability — EA has considered fault isolation, monitoring surface area, and service dependencies based on your input.

### Key Relationships

| Role | What You Need from Them | What They Need from You |
|------|------------------------|------------------------|
| AVA | Release certification, certification records, known issues for deployment | Deployment readiness, environment status, rollback confirmation |
| EA | Architecture decisions that support operability, monitoring surface area, fault isolation design | Operational requirements input, deployment topology needs, operability feedback |
| EPM | Customer-facing timeline, Engagement Success context, operational readiness communication | Operational readiness status, release mechanics plan, risk flags |
| ELs | Operational requirements implementation (logging, metrics, health checks), squad-level operational testing | Operational requirements specifications, monitoring configuration guidance |
| EO | Backing for operational readiness sign-off authority, resourcing support | Operational readiness assessment, risk-to-go-live communication |

### Performance Input and the Dual Axis

Your functional home is **SRE / Operations**. SRE leadership evaluates your growth across Engagements — multi-Engagement operational record, operating model breadth, release coordination quality. EO provides execution-axis input. EPM provides feedback on operational readiness communication and its impact on Engagement Success.

---

## 2. Expected Interactions, Tensions, and How to Navigate

### SRE Lead ↔ AVA

**Tension:** AVA certifies; you deploy. The boundary is clear but the handoff under time pressure can blur. AVA may certify with conditions; you must decide whether those conditions affect deployment mechanics.

**How to navigate:**
- Define the certification → deployment protocol formally: certification record format, known issues classification (blocking vs. non-blocking for deployment), rollback criteria.
- If AVA certifies with conditions that affect deployment (e.g. "certified for staging only, not production"), confirm explicitly. Do not interpret certification ambiguously.
- If you identify an operational concern (e.g. environment instability, capacity shortage) that affects release readiness, surface it to AVA and EPM. Operational readiness and assembly quality are related — your input is verification-relevant.

### SRE Lead ↔ EA

**Tension:** Architecture decisions have operational implications. EA may design for functional correctness without fully considering monitoring, fault isolation, or deployment complexity. You need architecture to support operability.

**How to navigate:**
- Engage EA during architecture design, not after. If you discover operational gaps after the architecture is implemented, retrofit is expensive. Provide operational requirements as input to EA's design decisions.
- If the architecture does not support adequate monitoring or fault isolation, raise it as a risk. If EA deprioritises, escalate through EPM.

### SRE Lead ↔ EPM

**Tension:** EPM wants predictability and a go-live date. You need operational readiness to be confirmed before Transfer. If operational readiness lags behind delivery, EPM faces a gap between "the code is done" and "the system is ready to run."

**How to navigate:**
- Make operational readiness status visible throughout Build — include it in the integrated view that EPM maintains. If EPM's integrated view does not include operational readiness, the plan is incomplete.
- When operational readiness is not on track, flag early with impact and remediation plan. Do not wait until Transfer to reveal that runbooks are incomplete or monitoring is not configured.

### SRE Lead ↔ ELs

**Tension:** You need engineers to implement operational requirements (logging, metrics, health checks). ELs may see these as lower priority than functional delivery.

**How to navigate:**
- Frame operational requirements as squad Definition of Done items, with EA's backing. If operational requirements are explicit DoD criteria, ELs cannot defer them.
- Provide clear, implementable specifications — not "add monitoring" but "emit metrics at these endpoints, with these labels, at this frequency." The more specific your requirements, the less overhead for engineers.

---

## 3. Escalation: Dos and Don'ts

**Do:**

- Exercise **operational readiness sign-off authority** — SRE Lead must approve that operational criteria are met before Transfer ([governance.md](../../governance.md#transfer-readiness)). This is an authority, not a suggestion.
- Escalate architecture-operations misalignment to **EPM** (who mediates between EA and SRE Lead) and then to **EO** if unresolved.
- Raise go-live readiness concerns to **EO** when operational readiness is at risk and remediation requires Engagement-level decisions.

**Don't:**

- Confuse your authority with AVA's authority. You sign off on operational readiness; AVA certifies assembly quality. These are complementary, not interchangeable.
- Deploy without AVA certification. You manage *how* the assembly is released — but *whether* it can be released is AVA's decision.
- Wait until Transfer to reveal operational readiness gaps. The EPM and EO need early warning to adjust plans — late surprises undermine trust.
- Accept "we'll do runbooks later" from the team. Runbooks deferred past Transfer become operational risk that falls on whoever runs the system in production.

---

## 4. Further Learning

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
