# Engagement Product Owner (EPO) — Role Coaching Guide

[← Back to Career Guides](../README.md) | [Role Definition](../../roles.md#engagement-product-owner-epo)

---

## 1. Success in the Role

### First 90 Days (or Discover Phase)

- **Launch customer discovery:** Engage directly with the customer to understand their needs, pain points, and desired outcomes. The gap between "what the Product Line provides" and "what the customer needs" is your primary concern. You do not build requirements in isolation — you discover them with the customer and translate them for the Engagement team.
- **Connect requirements to architecture:** Work with EA to translate customer needs into architectural decisions. Every requirement has an architecture implication — it either fits the platform's existing capability, requires configuration, needs an inner source contribution, or requires custom build. You and EA must align early.
- **Design the requirements flow to Squad PMs:** You produce Engagement-level requirements; Squad PMs decompose and prioritise within their squads. Design the handoff so Squad PMs can work independently within a well-defined scope — if every requirement must pass through you, you become a bottleneck.
- **Plan for training and enablement:** Engagement Success depends on adoption, not just delivery. Begin planning customer training and enablement early — what the customer needs to learn, who needs training, what enablement materials are required. EPM owns the Engagement Success function, but you drive the training and enablement that makes adoption possible.

### What "Good" Looks Like

- Requirements are clear, actionable, and traceable to customer needs. Engineers can implement them without ambiguity; EA can map them to architecture decisions.
- The requirements flow to Squad PMs is smooth — Squad PMs have enough context to decompose and prioritise independently. You are not a bottleneck.
- Customer discovery continues through Build — as the customer sees the product take shape, needs evolve. You capture changes, assess impact, and coordinate with EPM and EA before updating backlogs.
- Training and enablement are planned and resourced. At Transfer, customers understand and can use the delivered product.
- The requirements-architecture boundary with EA is productive — EA raises architecture implications of requirements; you raise customer implications of architecture decisions. Neither role overrides the other's domain.

### Key Relationships

| Role | What You Need from Them | What They Need from You |
|------|------------------------|------------------------|
| EA | Architecture decisions, gap analysis, inner source vs. custom recommendations | Customer requirements, discovery findings, requirements-architecture translation |
| Squad PMs | Decomposition of requirements into squad backlogs, progress on requirements delivery | Engagement-level requirements, priority guidance, clarification on acceptance criteria |
| EPM | Customer alignment, scope change management, Engagement Success coordination | Requirements status, customer discovery insights, training/enablement plan |
| Client Partner | Customer access, stakeholder context, relationship dynamics | Customer-facing requirements communication, discovery progress |
| EO | Priority decisions when requirements exceed capacity, strategic direction | Requirements landscape, customer need assessment, training readiness |

### Performance Input and the Dual Axis

Your functional home is **Product Management**. Product leadership evaluates your career growth across Engagements — discovery depth, requirements quality, cross-squad thinking. EO provides execution-axis input. EPM provides feedback on your customer alignment and Engagement Success contribution. Request feedback from EA on requirements-architecture translation quality and from Squad PMs on requirements clarity.

---

## 2. Expected Interactions, Tensions, and How to Navigate

### EPO ↔ EA

**Tension:** You define what the customer needs; EA defines how the solution is architected. The requirements-architecture boundary is where most Engagement scope issues originate. A requirement may imply a platform gap that requires an inner source contribution (affecting timeline) or a custom build (affecting reusability).

**How to navigate:**
- Work jointly, not sequentially. Do not hand requirements to EA and wait — co-develop the requirements-to-architecture mapping. When you see a customer need, discuss the architecture implication with EA immediately.
- EA prevails on architecture decisions (per the [escalation model](../../governance.md#escalation-model)). If you believe EA's architecture does not address the customer need, bring the evidence (customer context, discovery data) and escalate through EPM to EO if needed.
- Distinguish "the customer wants X" from "the customer needs X." Architecture decisions should address needs, not wants. Your discovery work must separate the two.

### EPO ↔ Squad PMs

**Tension:** You set Engagement-level requirements; Squad PMs prioritise within their squads. Multiple inputs compete for squad backlog space: your requirements, EA's inner source contributions, AVA's verification requirements, and tech debt. The Squad PM makes the trade-off within the squad; you set the priorities across squads.

**How to navigate:**
- Give Squad PMs enough context to decompose independently. If every requirement needs your interpretation, the handoff is too thin.
- When requirements change (and they will — customers refine needs as they see the product), coordinate with EPM before updating squad backlogs. Silent backlog changes create chaos.
- If Squad PMs are deprioritising your requirements in favour of other inputs (inner source, tech debt), surface it to EPM. The trade-off is legitimate but should be visible, not hidden.

### EPO ↔ EPM

**Tension:** EPM owns Engagement Success (readiness, adoption, value). You drive the training and enablement that makes adoption possible. If training is deprioritised under delivery pressure, adoption suffers — and Engagement Success fails.

**How to navigate:**
- Advocate for training and enablement throughout Build, not just at Transfer. If training is cut from the plan, raise the risk to EPM explicitly: "Without training, the customer will not adopt, and Engagement Success will be at risk."
- Coordinate customer-facing communication with EPM. You have deep customer knowledge from discovery; EPM has the integrated delivery view. Neither can speak to the customer effectively without the other's input.

### EPO ↔ Client Partner

**Tension:** You need customer access for discovery; Client Partner manages the client relationship. Customer access may be constrained by client politics, availability, or Client Partner's relationship management concerns.

**How to navigate:**
- Coordinate customer access through Client Partner. Do not reach out to client stakeholders independently without Client Partner's awareness — it can undermine the relationship.
- Provide Client Partner with discovery insights that help the relationship — not just raw requirements, but customer sentiment, unmet expectations, and satisfaction signals.

---

## 3. Escalation: Dos and Don'ts

**Do:**

- Escalate requirements-vs-architecture disputes with EA to **EPM** first (EPM mediates; EA prevails on architecture per the [escalation model](../../governance.md#escalation-model)).
- Escalate training/enablement resource constraints to **EPM** — Engagement Success is EPM's function and deprioritising training is an Engagement Success risk.
- Escalate customer access constraints to **Client Partner** — they manage the relationship and can facilitate access.

**Don't:**

- Override EA on architecture decisions. If you believe the architecture does not address the customer need, present the evidence and escalate through EPM. EA's domain is architecture; yours is requirements.
- Direct Squad PM backlogs at the task level. You set Engagement-level priorities; Squad PMs decompose and prioritise within squads. If you micromanage squad backlogs, Squad PMs become clerks rather than product practitioners.
- Reach out to client stakeholders without Client Partner's awareness. Client Partner owns the relationship — coordinate access through them.
- Let requirements change silently during Build. Every change must be assessed for commercial impact (EPM/AM), architecture impact (EA), and timeline impact (EPM/ELs).

---

## 4. Further Learning

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
