# Operating Models

## Overview

After a Customer Solution goes live, **who operates and maintains it** is defined by the **operating model** chosen for that engagement. Zeta defines three operating models. The choice is made during scoping and documented in the engagement contract.

**Non-negotiable:** **Platform operations are always Zeta.** Olympus, Tachyon, and other domain platforms are always run and operated by Zeta (SRE). What varies is who operates and maintains the **Customer Solution** layer (configuration, integrations, customer-specific components).

---

## The Three Operating Models

| Model | Platform Ops | Config Changes | Integration Maintenance | Incident Response | Feature Enhancements |
|-------|--------------|----------------|--------------------------|-------------------|----------------------|
| **Fully Managed** | Zeta | Zeta | Zeta | Zeta | Zeta |
| **Co-Managed** | Zeta | Shared (Zeta + Customer) | Customer or Zeta (per contract) | Zeta | Customer or Zeta (per contract) |
| **Customer-Operated** | Zeta | Customer | Customer | Zeta (escalation) | Customer |

**Platform operations** — Runtime, monitoring, patching, capacity for the domain platforms. Always Zeta.

**Customer Solution operations** — Configuration changes, integration maintenance, incident response for the solution layer, and feature enhancements. Varies by model.

---

## Fully Managed

**Description:** Zeta operates and maintains the entire Customer Solution. Customer consumes outcomes; they do not operate or change configuration/integrations themselves.

**Typical use:** Customer wants a turnkey solution; they have limited in-house ops or prefer to focus on business outcomes.

**Responsibilities:**

- Platform ops: Zeta (SRE)
- Config changes: Zeta
- Integration maintenance: Zeta
- Incident response: Zeta
- Feature enhancements: Zeta (per contract/change process)

**Contract:** Defines scope of “fully managed,” change process, SLAs, and escalation.

---

## Co-Managed

**Description:** Zeta operates the platform; customer and Zeta share or split responsibility for configuration, integrations, incidents, and enhancements per contract.

**Typical use:** Customer has some in-house capability; they want to own certain changes (e.g. config, integrations) while Zeta handles platform and escalation.

**Responsibilities:**

- Platform ops: Zeta (SRE)
- Config changes: Shared (defined in contract)
- Integration maintenance: Customer or Zeta (per contract)
- Incident response: Zeta (e.g. platform and L2); customer may do L1 or specific areas
- Feature enhancements: Customer or Zeta (per contract)

**Contract:** Clearly defines which responsibilities are Zeta vs. customer; escalation path; change and release process.

---

## Customer-Operated

**Description:** Zeta operates the platform only; customer operates and maintains the Customer Solution layer (config, integrations, enhancements). Zeta provides escalation and support (e.g. platform issues, upgrades).

**Typical use:** Customer has strong in-house ops and wants to own solution-layer operations; they rely on Zeta for platform reliability and support.

**Responsibilities:**

- Platform ops: Zeta (SRE)
- Config changes: Customer
- Integration maintenance: Customer
- Incident response: Zeta for platform; customer for solution layer; Zeta escalation path defined
- Feature enhancements: Customer

**Contract:** Defines platform SLAs, escalation path, support scope, and upgrade/maintenance process. Clarifies that solution-layer operations are customer-owned.

---

## How to Select Operating Model During Scoping

- **Customer capability** — Can they operate config, integrations, and incidents? Do they want to?
- **Customer preference** — Turnkey vs. co-managed vs. customer-operated.
- **Commercial and risk** — Pricing, liability, and support scope align with the chosen model.
- **Engagement contract** — Model is documented in the SoW; responsibility matrix is explicit.

Solution Architect and Engagement Lead agree with the customer on the operating model before or early in delivery; it drives handover and run-team design.

---

## Transition and Handover Criteria

When the Win Engineering Team transitions the Customer Solution to steady state:

- **Fully Managed** — Handover to Zeta run team (or existing SRE/ops); run team has playbooks, escalation matrix, and access; customer is not expected to operate.
- **Co-Managed** — Handover to Zeta run team and customer per contract; responsibilities and handover checklist are clear for both.
- **Customer-Operated** — Handover to customer with documentation, runbooks, and escalation path; Zeta retains platform ops and support per contract.

**Handover criteria** (customize per engagement): documentation complete, operational readiness criteria met, runbooks and escalation matrix in place, operating model responsibilities signed off.

---

## References

- [Engagement Lifecycle](../processes/engagement-lifecycle.md) — Scoping and transition phases
- [Win Engineering](win-engineering.md) — What Win Engineering delivers
- [Stakeholder Concerns](../adoption/stakeholder-concerns.md) — SRE/ops concerns and mitigations
