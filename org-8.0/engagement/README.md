# Engagement Operating Model Guide

This is the **practitioner's guide** to how [Engagements](engagement-definition.md) are explored, staffed, executed, and governed. It describes the roles, responsibilities, lifecycle phases, squad model, architecture practices, operating models, and governance structures that together constitute the Engagement operating model.

**Scope:** This guide is a referenceable operating manual — it defines roles, processes, governance, and practices that apply to **any** Engagement. It does not describe specific Engagements, the current Engagement portfolio, or individual Product Line capabilities. For Product Line details, see the [PLE Guide](../product-line-engineering/README.md).

This guide is **not**:

- A definitions-only reference — see [engagement-definition.md](engagement-definition.md) for canonical definitions of Engagement, Engagement Engineering, Engagement Success, and Exploration
- A terminology deliberation — see [whats-in-the-name.md](whats-in-the-name.md) for the naming rationale
- A specific Engagement's plan, architecture, or status
- A Product Line capability reference
- A portfolio dashboard or pipeline view

**Audience:** Sales, Account Management, Client Partner, EPM, EPO, EA, AVA, ELs, Squad PMs, Product Managers, Program Managers, SRE Leads, Engineering Leadership

---

## The Engagement Model at a Glance

### End-to-End Flow

```
Exploration ──► Engagement ──────────────────────────────────────────► Steady State
                │                                                      │
                Initiate → Discover → Build → Transfer → Complete ─────┘
```

### Role Activity by Stage

| Role | Exploration | Initiate | Discover | Build | Transfer | Complete |
|------|:-----------:|:--------:|:--------:|:-----:|:--------:|:--------:|
| **Sales / Account Management** | ● | ○ | | | | |
| **Exploration Lead** | ● | ○ | | | | |
| **Client Partner** | | ● | ● | ○ | ○ | ○ |
| **EO (Engagement Owner)** | | ● | ● | ● | ● | ● |
| **EPM (Engagement Program Manager)** | | ● | ● | ● | ● | ● |
| **EA (Engagement Architect)** | ○ | ● | ● | ● | ● | ○ |
| **AVA (Assembly Verification Architect)** | | | ● | ● | ● | ○ |
| **EPO (Engagement Product Owner)** | | ● | ● | ● | ● | ○ |
| **SRE Lead** | | | ○ | ● | ● | ● |
| **Engineering Leads (ELs)** | | ● | ● | ● | ● | ○ |
| **Squad PMs** | | | ● | ● | ○ | |
| **Scrum Masters** | | | ● | ● | ● | ○ |

● = primary activity &nbsp; ○ = supporting/advisory

### Engagement-Level Role Hierarchy

```
              Client Partner
                │       │
               CPA     EO
                        │
        ┌──────────┬────┼────────┬──────────┐
        │          │    │        │          │
       EPM        EA   AVA     EPO     SRE Lead
        │                  │
   ┌────┼────┬────┐    Verification
   │    │    │    │      Squad
  CP  Studio  PL  Scrum
  EL    EL   ELs  Masters
```

- **Client Partner** — senior-most per-client role; owns strategic client relationship; EO reports to Client Partner
- **Client Partner Associate (CPA)** — generalist support for Client Partner; governance prep, stakeholder coordination, commercial tracking
- **Engagement Owner (EO)** — overall accountability for the Engagement; reports to Client Partner
- **Engagement Program Manager (EPM)** — primary customer-facing contact; integrated view; Engagement Success; directs ELs and Scrum Masters
- **Engagement Architect (EA)** — architecture across the entire span; peer architect to Assembly Verification Architect; engineering quality standards
- **Assembly Verification Architect (AVA)** — verification architecture; assembly certification; release authority; directs Verification Squad
- **Engagement Product Owner (EPO)** — customer discovery, requirements, training
- **Site Reliability Engineering Lead (SRE Lead)** — operational readiness; release coordination
- **Engineering Leads (ELs)** — per-squad delivery accountability (report to EPM)
- **Scrum Masters** — process facilitation across 1-3 squads (report to EPM)

---

## Guide Contents

| # | Document | What It Covers |
|---|----------|---------------|
| 1 | [Engagement Engineering in Practice](engagement-engineering-in-practice.md) | Ownership boundary, five artifact groups, PL Squad relationship, inner source for squads, behavioral guardrails |
| 2 | [Exploration](exploration.md) | Pre-Engagement: triggers, Exploration Lead, qualification gate, artifacts |
| 3 | [Roles and Responsibilities](roles.md) | Client Partner, CPA, EO, EPM, EA, AVA, EPO, SRE Lead, EL, Squad PM, Scrum Master, Security; dual-axis reporting model |
| 4 | [Lifecycle](lifecycle.md) | Phase-by-phase: Initiate → Discover → Build → Transfer → Complete |
| 5 | [Engagement Formation](engagement-formation.md) | Team assembly, three-stage assignment, designation-to-complexity matching, phase evolution, scaling patterns (Stream DLs, Stream Architects), team release |
| 6 | [Squad Model and Staffing](squad-model.md) | Squad types, composition, staffing summary, rotation, migration squads; see Engagement Formation for full formation model |
| 7 | [Architecture and Archetypes](architecture-and-archetypes.md) | Archetype-driven assembly, gap analysis, inner source, EA assessment |
| 8 | [Verification and Certification](verification-and-certification.md) | Verification module, system-under-test boundary, EA-AVA model, continuous verification, increment certification, Verification Squad, handover |
| 9 | [Engagement Readiness Council (ERC)](engagement-readiness-council.md) | ERC charter: purpose, composition, role assignment, capacity coordination (PPM), framework guidance, EPM governance |
| 10 | [Governance and Escalation](governance.md) | Governance bodies overview, scope change, commercial alignment, escalation model, decision-point governance |
| 11 | [Metrics and Feedback](metrics-and-feedback.md) | Metrics, knowledge capture, feedback loops, inner source debt |
| 12 | [Completion and Termination](completion-and-termination.md) | Successful completion, early termination, scope reduction, handover artifacts |
| 13 | [Career Paths](career-paths.md) | Function-role model; functional tracks (Engineering, Architecture, Product, Delivery, SRE, Account Management); cross-track jumps to Architecture; role assignment by Engagement complexity; dual-axis career tracking; recognition mechanisms |
| 14 | [Open Items](open-items.md) | What this guide does not yet cover, organized by stakeholder perspective |

---

## Companion Documents

| Document | What It Covers |
|----------|---------------|
| [Career Guides](career-guides/README.md) | Coaching-style guides for every function (by seniority level) and every Engagement role — craft, interactions, tensions, escalation, further reading |
| [engagement-definition.md](engagement-definition.md) | Canonical definitions, leadership guidelines, staffing principles, style guide, FAQ |
| [whats-in-the-name.md](whats-in-the-name.md) | Terminology deliberation record |

---

## PLE References — Platform-Owned Content

The PLE guide owns structural ingredients that the Engagement Operating Model uses. These references point to PLE-owned content — the platform side of the relationship.

| Document | What It Covers |
|----------|---------------|
| [PLE Overview](../product-line-engineering/framework/ple-overview.md) | PLE foundations, PLE-Engagement relationship |
| [Solution Archetypes](../product-line-engineering/framework/solution-archetypes.md) | Archetype framework (blueprints, cookbooks, playbooks) |
| [Operating Models](../product-line-engineering/framework/operating-models.md) | Post-delivery operating models (Fully Managed, Co-Managed, Customer-Operated) |
| [Variability Management](../product-line-engineering/framework/variability-management.md) | Configuration point tracking and governance |
| [PAC Charter](../product-line-engineering/governance/council-charter.md) | Platform Architecture Council |
| [Inner Source Guidelines](../product-line-engineering/governance/inner-source-guidelines.md) | Inner source contribution process |
| [Tech Debt Policy](../product-line-engineering/governance/tech-debt-policy.md) | Tech debt tracking and remediation |
| [Rotation Model](../product-line-engineering/processes/rotation-model.md) | Engineer rotation and return guarantees |
| [Knowledge Capture](../product-line-engineering/processes/knowledge-capture.md) | Knowledge flow back to platforms and PAC |

---

## Glossary

| Term | Definition |
|------|-----------|
| **Assembly Construct** | The construct-type label for Engagement — emphasizing that what we produce is an assembled artifact, not a service. |
| **Client Partner** | The senior-most per-client role; owns the strategic client relationship. May span multiple Engagements with the same client. EO reports to Client Partner. Assigned by ERC. |
| **Client Partner Associate (CPA)** | Generalist support for the Client Partner: governance prep, stakeholder coordination, commercial tracking, cross-Engagement alignment. Reports to Client Partner; at least one per Client Partner. |
| **Engagement** | The complete collection of software artifacts (configurations, extensions, integrations, studio-built components, verification artifacts) that together constitute a customer-specific product instantiation derived from Product Lines. An Assembly Construct. |
| **Engagement Engineering** | The discipline of designing and assembling customer-specific product instantiations by leveraging Product Lines and studio-built components. |
| **Engagement Success** | The function responsible for ensuring an Engagement is successfully deployed and adopted — readiness, adoption, value delivery. Owned by EPM. |
| **ERC (Engagement Readiness Council)** | Governs the Engagement pipeline; assigns Engagement-level roles (Client Partner, EO, EPM, EA, AVA); houses the Portfolio Program Manager (PPM) function for capacity coordination; provides framework guidance and archetype references. See [ERC Charter](engagement-readiness-council.md). |
| **Exploration** | Pre-commitment work of discovering customer needs, assessing feasibility, and qualifying whether an Engagement should be initiated. |
| **PAC (Platform Architecture Council)** | Governs architecture standards, practice sharing, pattern extraction, and variability across Product Lines. Operates in Practice Mode (monthly, advisory) and Governance Mode (ad-hoc, decision authority). See [PAC Charter](../product-line-engineering/governance/council-charter.md). |
