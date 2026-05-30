# DR-034: Role vs. Agent Separation

**Status:** Accepted
**Date:** 2026-04-06

## Context

The UPIM has persona/stakeholder entities across four dimensions: Win Stakeholder (Vendor Value), User Persona (User Experience), Developer Persona and Programmatic User Persona (Ecosystem), and Operational Persona (Operational). Simultaneously, the Workforce Repository (WFR, formerly AWR) tracks agents who do work, and work items reference both "who should do this" (role) and "who is doing this" (agent).

Without a clear separation, "Pre-Sales Engineer" could mean either "the product's commercial model requires this function" (a product definition concern) or "John Smith is assigned to this Win Case" (a workforce concern). This ambiguity affects entity ownership, repository placement, and relationship modeling.

## Decisions

### D1: Roles are Definition Model entities

Win Stakeholder (Vendor Value), User Persona (User Experience), Developer Persona (Ecosystem), Programmatic User Persona (Ecosystem), and Operational Persona (Operational) are all **role definitions** in the Definition Model. They describe *what* a role is — responsibilities, JTBD, outcomes, barriers, frictions, journeys. They are abstract, durable, and product-scoped.

**Rationale:** These entities describe what the product *requires* to succeed (a Pre-Sales Engineer function, a Merchant Admin persona, an SRE operator role) — not specific people. This is a product definition concern that belongs in the Definition Model alongside other structural descriptions of what the product is.

### D2: Agents are WFR entities bound to one or more role definitions

Specific people or AI agents who fulfill roles are tracked in the Workforce Repository (WFR). An agent in WFR references one or more role definitions from the Definition Model. WFR agents are the "who" that gets assigned to work items in WR.

**Rationale:** The same person may fill multiple roles (startup scenario). Multiple people may fill the same role (enterprise scenario). The binding between person and role is an organizational/workforce concern, not a product definition concern. WFR handles this binding while the Definition Model handles the role descriptions.

**The triad:** Role (Definition Model) → Agent (WFR) → Work (WR). "What function is needed?" → "Who can do it?" → "What are they doing?"

### D3: WFR tracks identity, role bindings, skills, availability, track access, governance

WFR's internal structure includes:
- **Agent Registry:** Identity, type (human/AI), contact/endpoint, onboarding status
- **Role Binding:** Which Definition Model roles an agent is qualified for and currently assigned to (references Vendor Value, User Experience, Ecosystem, Operational role entities)
- **Skills & Capabilities:** Certifications, domain expertise, tool proficiency
- **Track Access:** Which tracks the agent can pick up work in
- **Availability & Capacity:** Current workload, schedule, allocation
- **Governance:** Permissions, escalation authority, delegation rules
- **Performance Metrics:** Work throughput, quality, SLA adherence per role

**Rationale:** This structure supports both human and AI workers uniformly while enabling role-based assignment, skill-based routing, and governance enforcement.

### D4: ESR tracks external stakeholders — external parties are not agents

Customers, partners, prospects, and third-party developers are tracked in the External Stakeholder Registry (ESR), not WFR. External parties are *consumers* of the product, not agents in the product organization's work model. They do not pick up work across tracks.

**Rationale:** External stakeholders are referenced in work items (FIR reporters, Win Case customers, Incident affected tenants) but do not perform work in the vendor's tracks. Mixing them with internal workers in WFR would conflate fundamentally different concerns — workforce management vs. customer/partner management.

**Exception consideration:** In scenarios where external parties participate in the vendor's work (beta testers, advisory board members, co-development partners), the Operating Model should define how they are represented — potentially as limited-scope WFR agents with restricted track access, or as ESR stakeholders with collaboration references.

## Consequences

**Positive:**
- Clear separation of concerns: Definition Model owns role descriptions, WFR owns agent-to-role bindings, WR owns work assignments
- No ambiguity between "the product needs a Pre-Sales Engineer" and "John Smith is assigned"
- Cross-dimensional pattern is explicit and consistent (Vendor Value/User Experience/Ecosystem/Operational all follow the same role-definition pattern)
- WFR can be designed for workforce management without conflating product definition
- ESR provides a clean, separate registry for external parties

**Negative:**
- Adds a cross-reference layer: role definitions live in Definition Model entity files, but WFR must reference them
- Persona/stakeholder entities in the Definition Model need explicit "this is a role definition, not an agent" notes
- The Operating Model must define the role-binding process (how agents are matched to roles)

## Cross-Dimensional Role Pattern

| Dimension | Role Entity | What It Defines |
|---|---|---|
| Vendor Value | Win Stakeholder | Vendor-side roles in the AAARRR lifecycle |
| User Experience | User Persona | End-user roles with JTBD, journeys, channels |
| Ecosystem | Developer Persona, Programmatic User Persona | External builder/consumer roles |
| Operational | Operational Persona | Operator roles with operational jobs, journeys, pains |

All follow the pattern: **role defines** → **agent fulfills** → **work executes**.
