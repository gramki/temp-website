# Engagement Formation — Team Assembly and Evolution

[← Back to Guide](README.md)

---

## Purpose

This document is the **single source of truth** for how an Engagement team is formed: who assigns whom, from which function, at what designation level, when roles activate, and how the team evolves through the lifecycle. It also describes scaling patterns for large Engagements and how the team demobilizes at Transfer and Complete.

For squad types and composition, see [Squad Model and Staffing](squad-model.md). For phase-by-phase activities, see [Lifecycle](lifecycle.md).

---

## Formation Philosophy

- **ERC provides ingredients of success** — The Engagement Readiness Council assigns Engagement-level leadership and ensures the right people are in place for the Engagement's complexity and risk profile.
- **Assignment is function-based** — Roles are filled from functional benches (Engineering, Architecture, Product, Program/Delivery, SRE, Account Management). Career progression is evaluated on the functional axis; see [Career Paths](career-paths.md).
- **Designation level matches Engagement complexity** — ERC and EO match individual designation level to the Engagement's size, technical complexity, and client context.

---

## Three-Stage Assignment Model

### Stage 1 — ERC Assigns Engagement Leadership (at Initiate)

ERC assigns:

- **Client Partner + CPA(s)** — Per-client. A Client Partner may already be assigned if the client has existing Engagements. ERC ensures at least one Client Partner Associate (CPA) is in place for the Client Partner. For complex multi-Engagement clients, multiple CPAs may be staffed.
- **EO (Engagement Owner)** — Per-Engagement. EO reports to Client Partner on the execution axis. ERC considers Engagement complexity, risk profile, customer relationship depth, and **candidate heritage** for EO (Architecture, Delivery, or Engineering heritage — see [Roles](roles.md#engagement-owner-eo)).
- **EPM, EA, AVA** — Per-Engagement. ERC matches designation level to Engagement complexity.

**EO heritage matching:** EO may be drawn from Architecture heritage (architects who have guided multiple Engagement lifecycles), Delivery heritage (EPMs who have delivered multiple complex Engagements), or senior Engineering leadership (ELs or Engineering Managers who have demonstrated broad program leadership). The EO must understand both what is being built and how it is being delivered.

### Stage 2 — EO Assigns Squad-Level Leadership (at Initiate / early Discover)

EO assigns, with ERC/PPM support:

- **ELs** — One per functional squad (CP Squad, Studio Squad(s), PL Squad(s) contributing to the Engagement). The **Exploration Lead is the preferred candidate for CP Squad EL** when they continue from Exploration.
- **EPO** — One per Engagement. From Product function.
- **SRE Lead** — One per Engagement. Typically from the dominant Product Line's SRE team or from the SRE/Operations function.

### Stage 3 — Squad Staffing Through PPM (at Discover)

Once ELs are in place:

1. **Request** — ELs submit staffing requests to the ERC Portfolio Program Manager (PPM).
2. **Demand consolidation** — PPM consolidates demand across all Engagements and presents a unified view to Product Line Squad leads.
3. **Capacity check** — PL Squad leads check capacity against consolidated demand.
4. **Commitment** — PL Squad leads commit individuals through PPM; Engineering Leadership resolves priority conflicts when multiple Engagements compete for the same capacity.
5. **Assignment** — Named individuals are assigned; return dates are documented.
6. **Kickoff** — Team is convened; RACI and escalation paths are agreed.

Squad PMs and Scrum Masters are staffed through the same coordination (from Product and Program/Delivery functions respectively). Verification Squad engineers, when a dedicated Verification Squad is activated, are assigned through PPM like any other squad.

See [team-composition.md](../product-line-engineering/processes/team-composition.md) for the Product Line perspective on assignment and conflict resolution.

---

## Designation-to-Complexity Matching

ERC and EO match individual designation level to Engagement complexity. The following table is illustrative — actual assignment depends on availability and organizational calibration.

| Role | Small Engagement | Medium Engagement | Large / Complex Engagement |
|------|------------------|-------------------|----------------------------|
| **EA** | Staff Engineer (PE-1) or Architect | Architect | Senior Architect or Principal Architect |
| **AVA** | Staff Engineer (PE-1) or Architect | Architect | Senior Architect (verification depth required) |
| **EPM** | Program Manager | Senior Program Manager | Director of Delivery or Senior Program Manager |
| **EPO** | Product Manager | Senior Product Manager | Director of Product or Senior PM |
| **EO** | Heritage-matched senior leader | Heritage-matched senior leader | Senior leader; complexity drives seniority |
| **SRE Lead** | SRE or Senior SRE | SRE Lead (designation) | SRE Lead or SRE Manager |
| **Client Partner** | Per-client; one CP may span multiple small Engagements | Per-client | Per-client; may have multiple CPAs |

For the function-role model and which functions supply which roles, see [Career Paths — Role Assignment](career-paths.md#5-role-assignment-engagement-roles-vs-functions).

---

## Phase-by-Phase Team Evolution

| Phase | Formation / release actions | Roles active (summary) |
|-------|-----------------------------|------------------------|
| **Initiate** | Stage 1 and Stage 2 assignments. Client Partner + CPA(s), EO, EPM, EA, AVA assigned by ERC. EO assigns ELs, EPO, SRE Lead. | Client Partner, CPA, EO, EPM, EA, AVA, EPO, ELs |
| **Discover** | Stage 3 staffing. ELs submit requests to PPM; squads staffed. AVA and SRE Lead ramp up (SRE Lead advisory). | Full leadership; Squad PMs, Scrum Masters, engineers join as committed |
| **Build** | Full team active. Verification Squad activated if scope and complexity warrant. | Client Partner, CPA (supporting), EO, EPM, EA, AVA, EPO, ELs, Squad PMs, Scrum Masters, SRE Lead, engineers |
| **Transfer** | Squad members begin releasing per plan. Handover activities. | Client Partner, CPA (supporting); same leadership and squads with progressive release |
| **Complete** | Progressive release; Engagement formally closed. | Client Partner, CPA (informed at close); EO, EPM, SRE Lead, EA/AVA advisory; remaining squad members released |

For the full Role Activity by Stage table, see [README — Role Activity by Stage](README.md#role-activity-by-stage).

---

## Scaling Patterns for Large Engagements (6+ squads)

When an Engagement has **6+ squads** (across CP, Studio, and PL) or spans **multiple Product Lines** with significant architecture complexity, the following scaling patterns apply.

### Stream Delivery Leads (EPM scaling)

- **When:** EPM spans 6+ squads and cannot maintain effective coordination without delegation.
- **What:** Introduce **Stream Delivery Leads** (Stream DLs) from the Program/Delivery function. Each Stream DL manages 2–4 squads; the EPM coordinates across streams.
- **Reporting:** Stream DLs report to EPM on the execution axis. EPM retains integrated progress view, risk, and customer-facing accountability.
- **Functional axis:** Stream DLs belong to the Program/Delivery function (same as EPM).

**Scaled hierarchy (delivery):**

```
                    EO
                     │
                    EPM
                     │
        ┌────────────┼────────────┐
        │            │            │
   Stream DL A  Stream DL B  Stream DL C
        │            │            │
      ELs          ELs          ELs
```

### Stream Architects (EA scaling)

- **When:** Engagement spans multiple Product Lines or 6+ squads with significant architecture complexity; a single EA cannot maintain adequate coverage.
- **What:** Introduce **Stream Architects** from the Architecture function. Each Stream Architect owns a domain slice (e.g. a Product Line boundary or integration domain); the EA coordinates across streams and retains overall solution architecture accountability.
- **Reporting:** Stream Architects report to EA on the execution axis. EA retains archetype selection, variability documentation, and cross-stream design decisions.
- **Functional axis:** Stream Architects belong to the Architecture function.

**Scaled hierarchy (architecture):**

```
                    EO
                     │
                    EA
                     │
        ┌────────────┼────────────┐
        │            │            │
  Stream Arch A  Stream Arch B  Stream Arch C
```

### Activation criteria (summary)

| Trigger | Scaling pattern |
|---------|------------------|
| 6+ squads under one EPM | Stream Delivery Leads |
| Multiple Product Lines or 6+ squads with high architecture complexity | Stream Architects |

ERC and EO decide when to activate these patterns during Initiate or early Discover based on squad count, Product Line count, and integration complexity.

---

## Team Release

At **Transfer** and **Complete**:

- **Squad members** are released per the staffing plan and return dates. Return is guaranteed per the [Rotation Model](../product-line-engineering/processes/rotation-model.md). Engineers return to their Product Line Squads or move to another Engagement per rotation model.
- **ELs, Squad PMs, Scrum Masters** are released as their squads wind down. They return to their functional-axis homes (Engineering, Product, Program/Delivery).
- **EPO, SRE Lead** typically release at or after Transfer when handover and operational readiness sign-off are complete.
- **EA, AVA** often remain in an advisory capacity into Complete (e.g. archetype updates, knowledge capture); then release.
- **EPM, EO** remain until the Engagement is formally closed. **Client Partner and CPA** are client-scoped and do not "release" from the client; they may have no active Engagements with that client for a period.

Inner source repatriation — ensuring Engagement-specific work that proved reusable is contributed back to Product Lines — is completed before or during Complete. See [Completion and Termination](completion-and-termination.md).

---

## References

- [Roles and Responsibilities](roles.md) — Role descriptions, dual-axis reporting, Client Partner and CPA
- [Squad Model and Staffing](squad-model.md) — Squad types, composition, staffing summary
- [Lifecycle](lifecycle.md) — Phase-by-phase objectives and activities
- [Career Paths](career-paths.md) — Functions, role assignment, designation ladders
- [Governance and Escalation](governance.md) — ERC composition and assignment authority
- [Rotation Model](../product-line-engineering/processes/rotation-model.md) — Return guarantees, rotation cadence
- [Team Composition (PLE)](../product-line-engineering/processes/team-composition.md) — Product Line perspective on assignment and conflicts

---

[← Previous: Lifecycle](lifecycle.md) | [→ Next: Squad Model and Staffing](squad-model.md)
