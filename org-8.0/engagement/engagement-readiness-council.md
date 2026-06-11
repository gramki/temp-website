# Engagement Readiness Council Charter

[← Back to Guide](README.md)

## Purpose and Authority

The **Engagement Readiness Council (ERC)** governs the Engagement pipeline and ensures every Engagement starts with the ingredients of success: the right leadership, adequate capacity, and appropriate framework guidance.

ERC does not execute Engagements; it ensures Engagements are set up to succeed and provides cross-Engagement coordination through the Portfolio Program Manager (PPM) function.

---

## Composition

- **Engineering leadership** — ensures technical capacity and squad health
- **Architecture leadership** — ensures architectural alignment and EA availability
- **Delivery/Program leadership** — ensures delivery capacity and EPM availability
- **Account Management leadership** — ensures commercial alignment and Client Partner availability

Exact membership varies per organizational structure. ERC meets regularly (e.g. weekly) to review the Engagement pipeline and make assignment decisions.

---

## Core Functions

### 1. Role Assignment

ERC assigns all Engagement-level leadership roles:

| Role | Assigned By |
|------|-------------|
| **Client Partner** | ERC (per-client; may already be in place) |
| **Engagement Owner (EO)** | ERC |
| **Engagement Program Manager (EPM)** | ERC |
| **Engagement Architect (EA)** | ERC |
| **Assembly Verification Architect (AVA)** | ERC |

ERC also ensures **Client Partner Associate (CPA)** support is in place for each Client Partner.

Once ERC assigns these roles, **EO** assigns the remaining Engagement roles: Engineering Leads (ELs), Engagement Product Owner (EPO), and SRE Lead.

See [Engagement Formation](engagement-formation.md) for the full assignment model.

### 2. Capacity Coordination (PPM Function)

The **Portfolio Program Manager (PPM)** is an ERC function responsible for cross-Engagement capacity coordination:

- Maintains the cross-Engagement portfolio view
- Consolidates staffing demand from all Engagements
- Presents a unified demand view to Product Line Squad leads
- Coordinates supply commitments so ELs do not independently approach PL Squads
- Supports ERC in prioritization decisions when multiple Engagements compete for the same capacity

PPM ensures that capacity allocation is a governed, portfolio-level decision — not an ad hoc negotiation between individual Engagements and squads.

### 3. Framework Guidance

ERC provides the structural ingredients that Engagements need:

- **Archetype references** — blueprints, cookbooks, and playbooks that accelerate Engagement assembly
- **Operating model guidance** — Fully Managed, Co-Managed, or Customer-Operated; selected during Exploration and confirmed at Initiate
- **Governance templates** — charter templates, RACI frameworks, escalation models

### 4. Exploration Pipeline Governance

ERC governs the Exploration-to-Engagement boundary:

- Reviews Exploration qualification criteria
- Approves Engagement initiation when customer commitment triggers the delivery lifecycle
- Ensures Exploration artifacts (scope outline, preliminary architecture, commercial terms) are complete before Initiate

See [Exploration](exploration.md) for the pre-Engagement phase.

### 5. EPM Governance

EPM reports to ERC on Engagement progress, risks, and commercial alignment:

- Regular status reporting (cadence defined by ERC)
- Risk escalation and mitigation tracking
- Commercial alignment verification (delivery scope vs. contract terms)

### 6. Security Function

A shared security team operates under ERC:

- Performs VA/PT (Vulnerability Assessment / Penetration Testing)
- Conducts security reviews — periodic or on-demand
- Not embedded per Engagement; shared across the portfolio

---

## Authority Boundaries

| ERC Has Authority Over | ERC Does NOT Have Authority Over |
|------------------------|----------------------------------|
| Engagement-level role assignment | Squad-level staffing (EO/EL responsibility after ERC assigns capacity) |
| Cross-Engagement capacity prioritization | Day-to-day Engagement execution (EO/EPM responsibility) |
| Exploration pipeline qualification | Architecture standards (PAC responsibility) |
| Framework and operating model guidance | Technical disputes (escalate to PAC) |
| EPM governance and reporting | Release/verification decisions (AVA authority) |

---

## Decision Documentation

ERC decisions are recorded with:

- **Date** — when the decision was made
- **Context** — the Engagement, Exploration, or portfolio situation
- **Decision** — role assignment, capacity allocation, or qualification outcome
- **Rationale** — why this decision was made
- **Follow-up** — any actions required (e.g. onboarding, handover)

---

## Relationship to PAC

The Engagement Readiness Council (ERC) and the Platform Architecture Council (PAC) are complementary governance bodies:

| Council | Governs | Members |
|---------|---------|---------|
| **ERC** | Engagement pipeline, role assignment, capacity coordination, EPM governance | Leadership from Engineering, Architecture, Delivery, Account Management |
| **PAC** | Architecture standards, practice sharing, pattern extraction, variability, inner source quality | Senior/Principal Engineers, Engagement Architects |

**How they interact:**

- PAC patterns improve archetype quality that ERC uses for readiness assessments
- ERC delivery learnings (via EPM reporting and retrospectives) feed PAC practice reviews
- Architecture disputes escalate to PAC; role assignment and capacity disputes stay with ERC
- Client Partner ↔ EO disagreements escalate to ERC (ERC assigned both roles)

See [PAC Charter](../product-line-engineering/governance/council-charter.md) for PAC details.

---

## References

- [Engagement Operating Model Guide](README.md)
- [Engagement Formation](engagement-formation.md) — role assignment model
- [Exploration](exploration.md) — pre-Engagement phase
- [Governance and Escalation](governance.md) — escalation model, scope change, commercial alignment
- [Roles and Responsibilities](roles.md) — role definitions
- [PAC Charter](../product-line-engineering/governance/council-charter.md) — architecture governance

---

[← Previous: Verification and Certification](verification-and-certification.md) | [→ Next: Governance and Escalation](governance.md)
