# SRE / Operations — Function Coaching Guide

[← Back to Career Guides](../README.md) | [Career Paths — SRE / Operations](../../career-paths.md#3e-sre--operations)

---

## Purpose

This guide helps SRE practitioners at every level understand what the Engagement Operating Model expects of them and how to grow within the SRE / Operations function. This function supplies the **SRE Lead** Engagement role — the person responsible for operational readiness, release coordination mechanics, and the operational transition at Transfer and Complete. The SRE function also plays a critical role in determining how the customer's chosen operating model (Fully Managed, Co-Managed, Customer-Operated) shapes the handover.

---

## SRE

### Required Craft, Skills, Competencies

- **Craft:** Build and maintain monitoring, alerting, and runbook infrastructure for an assembled product. Write IaC for production, staging, and test environments. Understand the deployment topology that EA designs and configure CI/CD pipelines that AVA's verification module feeds into.
- **Skills:** Work with ELs and squad engineers on operational requirements (logging, metrics, health checks) — embed operational thinking into Build, not as an afterthought at Transfer. Participate in the AVA's release coordination workflow — understand that AVA certifies the assembly and SRE deploys it; the mechanics of deployment sequencing, environment promotion, and production cutover are SRE's domain.
- **Competencies:** Distinguish between the three operating models (Fully Managed, Co-Managed, Customer-Operated) and understand what each means for the operational handover. In a Fully Managed model, you are building for long-term operations. In a Customer-Operated model, you are building for handover to a team you may never meet. The operational artifacts (runbooks, monitoring, alerting) must be sufficient for the target audience.

### Roles Expected to Play and Challenges

- **SRE within an Engagement** — supporting the SRE Lead on operational readiness tasks. Not yet expected to play SRE Lead.
- **Challenge:** Joining mid-Build and discovering that operational requirements were not included in the architecture. Retrofit is harder than building in — advocate early through the SRE Lead for architecture decisions that support operations.
- **Challenge:** Building runbooks and monitoring for a system that's still evolving. The target keeps moving until late Build. Iterate on operational artifacts in sync with each increment rather than waiting for a stable system.

### How to Learn

- **On the job:** Work on at least one Engagement in each operating model variant (Fully Managed, Co-Managed, Customer-Operated) to build breadth. Each variant demands different operational artifacts and different handover depth.
- **Feedback:** SRE Lead provides execution-axis input. SRE leadership evaluates growth across Engagements and operating model breadth.
- **Knowledge sharing:** Contribute runbook templates and monitoring patterns to the SRE community of practice.
- **External reading:** *Site Reliability Engineering* — Google ([sre.google/sre-book](https://sre.google/sre-book/table-of-contents/)) — the definitive SRE reference; available free online. Directly applicable to monitoring, alerting, incident response, and operational handover planning.

---

## Senior SRE

### Required Craft, Skills, Competencies

- **Craft:** Design the operational architecture for an Engagement — monitoring topology, alerting strategy, incident response plan, capacity planning. Define the environment promotion pipeline (dev → staging → pre-prod → production) in coordination with EA and AVA. Own the operational readiness checklist from Discover through Transfer.
- **Skills:** Coordinate with AVA on release mechanics — AVA certifies, SRE deploys. Define the deployment sequencing, rollback procedures, and production cutover plan. Coordinate with EPM on operational readiness communication to the customer and Client Partner. Work with EA on architecture-operations alignment — ensure the architecture supports monitoring, fault isolation, and graceful degradation.
- **Competencies:** Plan the operational transition per the operating model — for Fully Managed, prepare for ongoing operations; for Co-Managed, design the shared responsibility matrix; for Customer-Operated, produce a complete operational handover package (documentation, training, support runbook). Manage the tension between "operational readiness isn't ready" and delivery pressure to go live.

### Roles Expected to Play and Challenges

- **SRE Lead** on smaller Engagements. **Senior SRE supporting the SRE Lead** on complex Engagements.
- **Challenge:** Ensuring operational readiness isn't treated as an afterthought. Build teams focus on building; the SRE Lead must make operational readiness a first-class concern from Discover.
- **Challenge:** Different operating models require fundamentally different handover approaches. A Customer-Operated handover is an order of magnitude more documentation-intensive than a Fully Managed handover. Plan accordingly from Discover, not from Transfer.

### How to Learn

- **On the job:** Lead the operational readiness workstream on a medium-complexity Engagement. Own the Transfer handover for at least one Engagement.
- **Feedback:** EO and EPM assess operational readiness quality and handover smoothness. SRE leadership evaluates operating model breadth.
- **Knowledge sharing:** Contribute operational handover patterns differentiated by operating model to the SRE community.
- **External reading:** *The Site Reliability Workbook* — Google ([sre.google/workbook](https://sre.google/workbook/table-of-contents/)) — practical companion to the SRE book; useful for operational readiness checklists and incident response planning.

---

## SRE Lead (Designation)

### Required Craft, Skills, Competencies

- **Craft:** Own the end-to-end operational readiness for an Engagement from Discover (advisory) through Complete. Design and implement the full release coordination mechanics. Define SLA/SLO targets based on the operating model and customer contract. Architect the incident response framework (escalation matrix, communication templates, post-incident review process).
- **Skills:** Negotiate with EA on architecture decisions that affect operability — fault isolation, service dependencies, monitoring surface area. Coordinate with AVA on the release certification → deployment handoff — this is the most critical operational boundary in the model. Present operational readiness status to EO, EPM, and Client Partner in business terms (risk to go-live, risk to SLA, remediation plan).
- **Competencies:** Exercise operational readiness sign-off authority — SRE Lead must approve that operational criteria are met before Transfer. This is an authority, not a suggestion. Manage the tension between delivery velocity and operational readiness — the EO and EPM want to go live; the SRE Lead must confirm the operations are in place.

### Roles Expected to Play and Challenges

- **SRE Lead** (the Engagement role) on complex Engagements.
- **Challenge:** The SRE Lead's release mechanics authority runs up against AVA's release certification authority and EPM's delivery communication. The boundary is clear (AVA certifies, SRE deploys) but pressure from Client Partner and EO can blur it. Hold the boundary.
- **Challenge:** Building the incident response plan for a system that crosses Product Line boundaries — incident ownership must be clear even when the system spans multiple PL operational teams.

### How to Learn

- **On the job:** Lead operational readiness across the full lifecycle of a complex Engagement. Take at least one assignment in each operating model variant.
- **Feedback:** EO rates operational readiness effectiveness. SRE leadership evaluates multi-Engagement operational record and operating model breadth.
- **Knowledge sharing:** Lead SRE community sessions on release coordination patterns. Document operational handover templates differentiated by operating model.

---

## SRE Manager / SRE Leadership (Director → VP)

- **Craft:** Own the SRE function's career path. Evaluate SREs across Engagements and operating model variants.
- **Key model construct:** Participate in ERC to advise on SRE Lead designation-to-complexity matching. Ensure the SRE function's operational standards are consistent across Engagements while allowing for operating-model-specific adaptation.
- **Challenge:** The SRE function often has fewer practitioners than Engineering or Architecture. Prioritise assignments carefully — a mismatched SRE Lead on a complex Engagement creates operational risk that surfaces late.
- **Challenge:** Defining operational readiness standards that span all three operating models without becoming overly prescriptive for simpler variants.

---

## Further Reading

| Resource | Why Relevant |
|----------|--------------|
| *Site Reliability Engineering* — Google ([sre.google/sre-book](https://sre.google/sre-book/table-of-contents/)) | Definitive SRE reference; directly applicable to monitoring, alerting, incident response, and the operational disciplines SRE Leads practice in this model. Free online. |
| *The Site Reliability Workbook* — Google ([sre.google/workbook](https://sre.google/workbook/table-of-contents/)) | Practical companion with checklists and case studies; useful for operational readiness planning and incident response design. Free online. |

---

[← Back to Career Guides](../README.md)
