# Team Composition

## Purpose

This document describes how **Win Engineering Teams** are formed for an engagement: who requests, who approves, who assigns, and how loaning from Domain Teams and Solution Architecture works. It also covers handling resource conflicts and team duration/rotation within an engagement.

---

## Trigger

Team composition starts when an engagement is **scoped** (Phase 1 complete) and approved to proceed. The Engagement Lead (or designated lead) initiates the staffing request.

---

## Role Requirements per Engagement Type

Typical roles on a Win Engineering Team:

| Role | Source | Purpose |
|------|--------|---------|
| **Engagement Lead** | Win / Delivery | Delivery accountability, customer liaison, scope and timeline |
| **Solution Architect** | Solution Architecture (loaned) | Solution design, archetype application, variability documentation |
| **Domain Engineers** | Domain Teams (loaned) | Platform configuration, extension development, integration |
| **Integration Engineers** | Domain Teams or shared pool (loaned) | Integrations with customer systems |
| **QA** | Domain Teams or shared pool (loaned) | Test design and execution, quality assurance |
| **Domain Analysts** | Domain Teams or shared pool (loaned) | Domain/business analysis, requirements clarification |

Exact mix depends on engagement size and archetype. SRE is not typically dedicated to a single engagement; Platform SRE supports the platform; a named owner for the engagement (e.g. run team lead) may be assigned at or after transition.

---

## Staffing Process

1. **Request** — Engagement Lead (or Solution Architect) submits staffing request: roles, estimated duration, preferred start date, and (if known) return or rotation expectations.
2. **Capacity check** — Domain Team leads and Solution Architecture check capacity; they may counter-propose dates or partial staffing if capacity is constrained.
3. **Approval** — Engineering Leadership (or designated authority) approves engagement and staffing; Domain Team leads and Solution Architecture commit specific individuals.
4. **Assignment** — Named individuals are assigned; return dates or rotation cadence are documented (e.g. in staffing plan or engagement charter).
5. **Kickoff** — Team is convened; RACI and escalation path are agreed; Engagement Lead and Solution Architect align team on scope and operating model.

**Who approves:** Engineering Leadership (or designated delegate) approves the engagement and overall staffing; Domain Team leads approve loan of their people; Solution Architecture approves loan of Solution Architect.

**Who assigns:** Domain Team leads assign loaned engineers from their team; Solution Architecture assigns Solution Architect; Engagement Lead is assigned by Win/Delivery leadership.

---

## Loaning from Domain Teams

- **Expectation:** Domain Teams loan engineers for the engagement duration (or for a rotation period within it). Return is guaranteed per the [Rotation Model](rotation-model.md).
- **Duration:** Documented in staffing plan (e.g. "Return by date X" or "Rotation every Y months"). A Win Engineering Team may remain on the Customer Solution for up to ~2 years; individual rotations may be shorter.
- **Capacity:** Domain Team leads reserve the right to decline or delay loan if platform capacity is at risk; engagement forecasting is used to reduce last-minute conflicts.
- **Return:** When the engagement transitions or the rotation period ends, loaned engineers return to their Domain Team (or move to another engagement per rotation model).

---

## Loaning Solution Architects

- **Expectation:** Solution Architecture loans a Solution Architect to the engagement. The SA may be on 2–3 concurrent engagements (cap per org); engagement portfolio is managed by Solution Architecture.
- **Duration:** Typically for the full engagement (scoping through transition) or until a handover point is agreed.
- **Capacity:** Solution Architecture manages SA capacity; if no SA is available, engagement start may be delayed or scope may be reduced (e.g. lighter architecture involvement).

---

## Handling Resource Conflicts

When multiple engagements compete for the same people (e.g. same Domain Engineers or same Solution Architect):

1. **Priority** — Engineering Leadership (or designated authority) sets priority: e.g. strategic customer, contract commitment, or first-come-first-served within a window.
2. **Negotiation** — Domain Team leads and Engagement Leads negotiate: partial staffing, delayed start, or substitution (e.g. different engineer with similar skills).
3. **Escalation** — If no agreement, escalate to Engineering Leadership; Leadership allocates or adjusts engagement portfolio.
4. **Visibility** — Engagement forecasting (e.g. pipeline of engagements and staffing needs) reduces surprise; Domain Teams and Solution Architecture plan capacity accordingly.

---

## Team Duration and Rotation Within Engagement

- **Team duration:** A Win Engineering Team may stay on a Customer Solution for an extended period (e.g. up to ~2 years). The team is still engagement-bound; it disbands or transitions when the engagement moves to steady state.
- **Rotation within engagement:** Individual members may rotate (e.g. every 6–12 months) for knowledge preservation and breadth, while the rest of the team continues. Not everyone rotates at once; rotation is planned so that continuity is maintained.
- **Return guarantees:** Loaned engineers have a documented return date or rotation point. Domain Team leads and Engagement Lead agree on this before or early in the engagement. See [Rotation Model](rotation-model.md).

---

## References

- [Engagement Lifecycle](engagement-lifecycle.md) — Phase 2: Compose Team
- [Rotation Model](rotation-model.md) — Return guarantees, rotation cadence
- [Win Engineering](../framework/win-engineering.md) — Win Engineering Team purpose and composition
- [Domain Engineering](../framework/domain-engineering.md) — Domain Teams and loaning
