# Engagement Product Owner (EPO) — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#engagement-product-owner-epo)

---

The EPO drives **customer discovery, needs analysis, and requirements detailing**, translating customer needs into actionable requirements that squads can execute. The role is scoped **per-Engagement**. The EPO reports to EO on the execution axis and works as a peer to EA on the requirements-architecture boundary. The functional home is **Product Management**.

---

## 1. Empowerment

- **Requirements authority.** You determine what the customer needs. Squad PMs determine how to prioritise and execute within their squads.
- **Customer discovery.** You engage directly with the customer to understand needs, pain points, and desired outcomes. Discovery continues through Build — requirements evolve as the customer sees the product take shape.
- **Training and enablement.** You own the training and enablement that makes customer adoption possible. EPM owns the Engagement Success function; you drive the content that makes it work.
- **Requirements flow to Squad PMs.** You produce Engagement-level requirements; Squad PMs decompose and prioritise within their squads.
- **What you cannot override.** You cannot override EA on architecture decisions. EA prevails on architecture; if you believe the architecture does not address the customer need, present the evidence and escalate through EPM.

---

## 2. Assignment

EO assigns the EPO at **Stage 2** ([engagement-formation.md](../../engagement-formation.md#stage-2--eo-assigns-squad-level-leadership-at-initiate--early-discover)). One EPO per Engagement. A person may serve as EPO for multiple Engagements if bandwidth permits. The EPO is drawn from the Product Management function.

**Scope:** Per-Engagement.

---

## 3. Ambition

### First 90 Days (or Discover Phase)

- **Launch customer discovery.** Engage directly with the customer to understand needs, pain points, and desired outcomes. The gap between "what the Product Line provides" and "what the customer needs" is your primary concern. You do not build requirements in isolation — you discover them with the customer and translate them for the Engagement team.
- **Connect requirements to architecture.** Work with EA to translate customer needs into architectural decisions. Every requirement has an architecture implication — it either fits the platform's existing capability, requires configuration, needs an inner source contribution, or requires custom build.
- **Design the requirements flow to Squad PMs.** You produce Engagement-level requirements; Squad PMs decompose and prioritise within their squads. Design the handoff so Squad PMs can work independently within a well-defined scope — if every requirement must pass through you, you become a bottleneck.
- **Plan for training and enablement.** Begin planning customer training and enablement early — what the customer needs to learn, who needs training, what enablement materials are required.

### What Great Looks Like

- Requirements are clear, actionable, and traceable to customer needs. Engineers can implement them without ambiguity; EA can map them to architecture decisions.
- The requirements flow to Squad PMs is smooth — Squad PMs have enough context to decompose and prioritise independently. You are not a bottleneck.
- Customer discovery continues through Build — as the customer sees the product take shape, needs evolve. You capture changes, assess impact, and coordinate with EPM and EA before updating backlogs.
- Training and enablement are planned and resourced. At Transfer, customers understand and can use the delivered product.
- The requirements-architecture boundary with EA is productive — EA raises architecture implications of requirements; you raise customer implications of architecture decisions.
- You distinguish "the customer wants X" from "the customer needs X." Architecture decisions address needs, not wants.

---

## 4. Commitments

### Dimensions

| Dimension | EPO SLA |
|---|---|
| **Fitment** | Requirements accurately reflect the customer's actual needs (not just stated wants). Requirements are traceable to customer discovery. When requirements change during Build, the change is assessed for commercial, architecture, and timeline impact before backlogs are updated. |
| **Velocity** | Requirements flow to Squad PMs is timely — Squad PMs are never blocked waiting for requirements clarification. Requirements are sufficiently decomposed and have clear acceptance criteria so engineers can implement without ambiguity. |

### Contractual Connection — Tier 3 (Roll-up)

The EPO does not interface with the contract directly, but requirements reflect contract scope. If requirements drift from contract scope, commercial misalignment follows. The EPO's Fitment SLA aggregates upward to the EPM's and Client Partner's Tier 1 commitments. When requirements are accurate and traceable, the Engagement delivers what was promised.

---

## 5. Collaboration

### Key Relationships

| Role | What You Need from Them | What They Need from You |
|------|------------------------|------------------------|
| EA | Architecture decisions, gap analysis, inner source vs. custom recommendations | Customer requirements, discovery findings, requirements-architecture translation |
| Squad PMs | Decomposition of requirements into squad backlogs, progress on requirements delivery | Engagement-level requirements, priority guidance, clarification on acceptance criteria |
| EPM | Customer alignment, scope change management, Engagement Success coordination | Requirements status, customer discovery insights, training/enablement plan |
| Client Partner | Customer access, stakeholder context, relationship dynamics | Customer-facing requirements communication, discovery progress |
| EO | Priority decisions when requirements exceed capacity, strategic direction | Requirements landscape, customer need assessment, training readiness |

### Tensions and Navigation

**EPO ↔ EA.** You define what the customer needs; EA defines how the solution is architected. The requirements-architecture boundary is where most Engagement scope issues originate.

- Work jointly, not sequentially. Do not hand requirements to EA and wait — co-develop the requirements-to-architecture mapping.
- EA prevails on architecture decisions (per the [escalation model](../../governance.md#escalation-model)). If you believe EA's architecture does not address the customer need, bring the evidence and escalate through EPM to EO if needed.
- Distinguish "the customer wants X" from "the customer needs X." Architecture decisions should address needs, not wants.

**EPO ↔ Squad PMs.** You set Engagement-level requirements; Squad PMs prioritise within their squads. Multiple inputs compete for squad backlog space: your requirements, EA's inner source contributions, AVA's verification requirements, and tech debt.

- Give Squad PMs enough context to decompose independently.
- When requirements change during Build, coordinate with EPM before updating squad backlogs. Silent backlog changes create chaos.
- If Squad PMs are deprioritising your requirements in favour of other inputs, surface it to EPM.

**EPO ↔ EPM.** EPM owns Engagement Success (readiness, adoption, value). You drive the training and enablement that makes adoption possible. If training is deprioritised under delivery pressure, adoption suffers.

- Advocate for training and enablement throughout Build, not just at Transfer.
- Coordinate customer-facing communication with EPM. You have deep customer knowledge from discovery; EPM has the integrated delivery view.

**EPO ↔ Client Partner.** You need customer access for discovery; Client Partner manages the client relationship.

- Coordinate customer access through Client Partner. Do not reach out to client stakeholders independently without Client Partner's awareness.
- Provide Client Partner with discovery insights that help the relationship — customer sentiment, unmet expectations, and satisfaction signals.

---

## 6. Management

### Dual-Axis Reporting

- **Execution axis:** Reports to **EO**. EO provides execution-axis input on your effectiveness within the Engagement.
- **Functional/career axis:** **Product leadership** evaluates your career growth across Engagements — discovery depth, requirements quality, cross-squad thinking.

### Performance Input

Request feedback from EA on requirements-architecture translation quality and from Squad PMs on requirements clarity. EPM provides feedback on your customer alignment and Engagement Success contribution. Product leadership evaluates your trajectory across Engagements.

---

## 7. Accountability

### Escalation: Dos and Don'ts

**Do:**

- Escalate requirements-vs-architecture disputes with EA to **EPM** first (EPM mediates; EA prevails on architecture per the [escalation model](../../governance.md#escalation-model)).
- Escalate training/enablement resource constraints to **EPM** — Engagement Success is EPM's function and deprioritising training is an Engagement Success risk.
- Escalate customer access constraints to **Client Partner** — they manage the relationship and can facilitate access.

**Don't:**

- Override EA on architecture decisions. Present the evidence and escalate through EPM.
- Direct Squad PM backlogs at the task level. You set Engagement-level priorities; Squad PMs decompose and prioritise within squads.
- Reach out to client stakeholders without Client Partner's awareness.
- Let requirements change silently during Build. Every change must be assessed for commercial impact (EPM/AM), architecture impact (EA), and timeline impact (EPM/ELs).

### When Commitments Are Missed

EPO commitments are primarily **outcome-based** (per the [accountability framework](../../people-and-culture/accountability.md)): discovery quality and requirements accuracy are judgement-dependent. When a requirement proves wrong (the customer's actual need was different from what was specified), the response is diagnosis — was discovery insufficient? Did the customer's context change? — and correction. The EPO is not penalised for customer needs evolving, but is accountable for the quality of the discovery process that uncovers them.

However, requirements flow timeliness is **commitment-based**: if Squad PMs are blocked waiting for requirements, that is a reliability failure.

---

## 8. Objectives in Perspective

The EPO's immediate objectives — discovery, requirements, training — serve a broader purpose: ensuring the Engagement delivers something the customer actually needs and can use.

The platform provides capability; the archetype provides structure; the EA translates both into a solution. But the EPO is the role that ensures this solution addresses the customer's real problem, not just a technically correct interpretation of it. When you discover deeply, the solution fits. When you plan training early, the customer adopts. When you manage requirements changes transparently, the Engagement remains commercially viable.

The EPO who produces technically accurate requirements that miss the customer's actual pain point has done documentation. The EPO who discovers the real need, translates it for the team, and ensures the customer can use what is built has done product ownership.

---

## Further Learning

**Internal references:**
- [Roles and Responsibilities — EPO](../../roles.md#engagement-product-owner-epo)
- [Governance and Escalation](../../governance.md) — escalation model for EPO ↔ EA disputes
- [Product Management Function Guide](../functions/product-management.md) — career progression toward EPO
- [Engagement Formation](../../engagement-formation.md) — EPO assignment at Stage 2

**External references:**

| Resource | Why Relevant |
|----------|--------------|
| *Inspired: How to Create Tech Products Customers Love* — Cagan ([svpg.com](https://www.svpg.com/inspired-how-to-create-tech-products-customers-love/)) | Product discovery and delivery fundamentals; directly applicable to the EPO's customer discovery and requirements detailing |
| *Continuous Discovery Habits* — Torres ([producttalk.org](https://www.producttalk.org/continuous-discovery-habits/)) | Structured customer discovery framework; applicable to the EPO's ongoing discovery through Discover and Build |

---

[← Back to Career Guides](../README.md)
