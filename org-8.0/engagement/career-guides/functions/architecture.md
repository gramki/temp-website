# Architecture — Function Coaching Guide

[← Back to Career Guides](../README.md) | [Career Paths — Architecture](../../career-paths.md#3b-architecture)

---

## Purpose

This guide helps architects at every level understand what the Engagement Operating Model expects of them and how to grow within the Architecture function. Architecture is a **cross-functional discipline** — it requires synthesis of technical, functional, commercial, and operational contexts. It is not "senior engineering." The Architecture function supplies the EA and AVA roles that shape every Engagement.

### Architecture vs. Technical Architecture

This distinction matters throughout the guide:

- **Architecture (solution / enterprise):** Concerned with stakeholder outcomes, business domains, operating model choices, commercial constraints, Product Line fit, and the synthesis of all of these into a solution. EA work is architecture in this sense — the EA decides which archetype to apply, what gaps exist, how inner source vs. custom trade-offs affect the Product Line roadmap, and how the operating model (Fully Managed, Co-Managed, Customer-Operated) shapes the solution.
- **Technical architecture (software architecture):** Concerned with system structure, component boundaries, data flow, API contracts, deployment topology, and non-functional requirements. Technical architecture is a subset of architecture — necessary but not sufficient. A Staff Engineer playing EA has technical architecture depth; what they must develop is the broader synthesis.

Both EA and AVA operate at the **architecture** level. AVA is not a test manager — the AVA architects the verification system, which is itself a complex, multi-component system requiring architecture-level design decisions.

---

## Architect

### Required Craft, Skills, Competencies

- **Craft:** Evaluate an Engagement against a solution archetype — identify which archetype components apply, which need adaptation, and where gaps exist. Design integration patterns that extend Product Lines without forking. Define the system-under-test boundary jointly with AVA. Produce variability documentation per [Variability Management](../../product-line-engineering/framework/variability-management.md).
- **Skills:** Lead gap analysis sessions — take the archetype, the customer's requirements (from EPO), and the platform's current capability and produce a gap register with inner source vs. custom recommendations. Present architecture decisions to non-technical stakeholders (EPM, Client Partner) with business rationale, not just technical rationale. Participate in PAC Practice Mode, presenting Engagement patterns for extraction.
- **Competencies:** Hold the "extend, don't fork" line under delivery pressure. When an EL requests a custom build because inner source contribution will take too long, evaluate whether the timeline concern is real or a planning gap — and either adjust the architecture to accommodate inner source timelines or document the exception with a repatriation plan. Navigate the peer relationship with AVA — co-design verification criteria without treating AVA as subordinate or adversarial.

### Roles Expected to Play and Challenges

- **EA** on medium-complexity Engagements. **AVA** if verification depth is the primary complexity dimension.
- **Challenge:** EA work is not solo design — the EA must co-design assembly acceptance criteria with AVA, translate requirements from EPO into architectural decisions, and set engineering quality standards that ELs must meet. The EA advises and escalates but cannot direct squads.
- **Challenge:** First-time EA assignment is the steepest growth step in the Architecture function. The archetype cookbook helps, but real Engagements deviate from archetypes. The EA must improvise within the model's constraints.
- **Challenge:** When playing AVA, separating verification architecture from test execution. The AVA designs the verification system; Verification Squad engineers implement it. The AVA is not an EL — direction comes through architectural authority and certification responsibility.

### How to Learn

- **On the job:** Request EA assignment on a medium-complexity Engagement with a senior mentor (Principal Architect or experienced EA) available for consultation. Shadow an AVA for one Engagement to understand the co-design dynamic before being assigned as EA.
- **Feedback:** Architecture Manager evaluates growth across Engagements. Request explicit feedback from the EO and EPM of your Engagement — they see your stakeholder effectiveness, which is as important as your technical judgment.
- **Knowledge sharing:** Document every architecture decision in the decision log. Propose at least one archetype adaptation for PAC review per Engagement.
- **External reading:** *Just Enough Software Architecture* (Fairbanks) — risk-driven architecture thinking directly applicable to calibrating how much architecture each Engagement needs.

---

## Senior Architect

### Required Craft, Skills, Competencies

- **Craft:** Lead complex Engagement architectures spanning multiple Product Lines. Evaluate and evolve archetypes — not just apply them but propose updates based on Engagement patterns. Define the variability model for a new archetype or a major archetype extension. Architect verification systems (when playing AVA) that handle multi-PL assemblies with complex integration topologies.
- **Skills:** Mentor Architects and Staff Engineers playing EA/AVA. Negotiate architecture decisions with commercial stakeholders (Client Partner, Account Management) — articulate trade-offs in business terms. Contribute to PAC Governance Mode on standards and pattern decisions. Lead the inner source priority and debt view across a complex Engagement.
- **Competencies:** Balance rigour with pragmatism — a complex Engagement with delivery pressure needs architecture that is "just enough" but not less. Know when an inner source contribution is worth the timeline cost and when a custom build with a repatriation plan is the better trade-off. Exercise release-block authority (when playing AVA) under commercial pressure — the hardest moment in the AVA role.

### Roles Expected to Play and Challenges

- **EA** on complex Engagements (6+ squads, multi-PL). **AVA** on Engagements with high verification complexity. May serve as **Stream Architect** in a scaled Engagement under a Principal Architect EA.
- **Challenge:** Multi-PL architecture — integration topology across Product Lines that were designed independently. The archetype may not cover cross-PL integration; the Senior Architect must design it.
- **Challenge:** Mentoring a first-time EA or AVA on a parallel Engagement while carrying your own EA/AVA responsibility. The dual demand is real; manage it through structured check-ins rather than ad-hoc availability.
- **Challenge:** Architecture-delivery tension at scale — with 6+ squads, the EA's mandatory review can become a bottleneck. Design review processes that scale (e.g. delegate domain-slice reviews to Stream Architects, retain cross-domain reviews).

### How to Learn

- **On the job:** Take multi-PL Engagement assignments. Lead at least one archetype update proposal through PAC Governance Mode. Serve as AVA on at least one Engagement if your experience has been primarily EA — the verification perspective deepens architecture thinking.
- **Feedback:** Architecture leadership evaluates your archetype contributions and multi-Engagement architecture record. Request feedback from PL Maintainers on your inner source prioritisation — they see whether your decisions respect platform integrity.
- **Knowledge sharing:** Lead PAC Practice Mode sessions on cross-PL integration patterns. Contribute case studies of archetype adaptations that succeeded or failed.
- **External reading:** *Software Architecture in Practice* (Bass, Clements, Kazman, 4th ed.) — comprehensive treatment of architecture quality attributes, tactics, and evaluation, applicable to the multi-stakeholder, multi-PL architecture decisions at this level.

---

## Principal Architect

### Required Craft, Skills, Competencies

- **Craft:** Shape the Product Line architecture itself — define or evolve extension points, configuration contracts, and platform boundaries that affect all future Engagements. Serve as the architecture reference across the organization. Evaluate whether a new Engagement type requires a new archetype or an extension of an existing one. Design architecture governance mechanisms (mandatory review scope, DoD architecture criteria) that scale.
- **Skills:** Represent architecture in ERC — advise on heritage matching for EO candidates, assess architecture readiness for new Engagements, and flag risks. Chair PAC Governance Mode discussions. Mentor Senior Architects on archetype ownership and evolution. Negotiate with Engineering leadership on inner source investment vs. Engagement velocity at the organizational level.
- **Competencies:** Maintain influence across all Engagements without being a bottleneck. Set architectural standards that are rigorous enough to protect platform integrity but flexible enough that EAs can adapt them to Engagement-specific contexts. Accept that you cannot personally review every architecture-significant decision — delegate through the Stream Architect pattern and trust the EA/AVA peer model.

### Roles Expected to Play and Challenges

- **EA** on the highest-complexity Engagements. **Architecture advisor** to ERC. **PAC chair or senior member.** May not play an Engagement role directly — influence is through standards, archetype ownership, and mentorship.
- **Challenge:** Staying connected to Engagement reality when much of your work is platform-level and organizational. Periodically take a direct EA assignment to stay grounded.
- **Challenge:** Resolving the tension between platform architecture evolution (long-term, investment-driven) and Engagement architecture adaptation (short-term, delivery-driven). You are the person who must hold both timelines in mind.

### How to Learn

- **On the job:** Own an archetype. Take responsibility for its evolution based on multi-Engagement feedback. Serve as the architecture member of ERC.
- **Feedback:** VP of Architecture evaluates impact on platform quality, archetype fitness, and organizational architecture maturity.
- **Knowledge sharing:** Author architecture standards and guidelines. Present cross-Engagement architecture insights to senior leadership.

---

## Architecture Management Branch

### Architecture Manager

- **Craft:** Manage architects on the functional axis. Evaluate architect growth across Engagement assignments — you see the full multi-Engagement architecture record.
- **Key model construct:** You provide the career continuity for architects rotating through EA and AVA roles. Track certification records (for AVA players), archetype contributions (for EA players), and multi-PL exposure.
- **Challenge:** Assessing an architect's growth when their Engagement output is mediated through EO and EPM feedback. Build direct relationships with EOs and ensure EA/AVA evaluation input flows reliably.

### Sr. Architecture Manager

- **Craft:** Own a segment of the Architecture function (e.g. architectures for a Product Line family). Shape architecture practice in coordination with PAC and Engineering leadership.
- **Key model construct:** Participate in ERC for heritage matching — identify which architects are ready for complex EA/AVA assignments and which need development assignments first.
- **Challenge:** Balancing the Architecture function's long-term investment (archetype evolution, variability governance) with Engagement-driven demand for architect availability. Neither can be sacrificed.

---

## Further Reading

| Resource | Why Relevant |
|----------|--------------|
| *Software Architecture in Practice* — Bass, Clements, Kazman, 4th ed. ([Pearson](https://www.pearson.com/en-us/subject-catalog/p/software-architecture-in-practice/P200000000111/9780137468218)) | Comprehensive architecture quality attributes and evaluation methods; directly applicable to EA gap analysis and multi-PL architecture |
| *Just Enough Software Architecture* — Fairbanks ([georgefairbanks.com](https://www.georgefairbanks.com/e-book/)) | Risk-driven thinking for calibrating architecture depth per Engagement — essential for EA role |
| *Solution Architecture Foundations* — Lovatt ([BCS](https://www.amazon.com/Solution-Architecture-Foundations-Mark-Lovatt/dp/1780175655)) | Solution architecture practice aligned with the EA's synthesis role (business + technical + operational) |
| *Solution vs. Software Architecture* — DZone ([dzone.com](https://dzone.com/articles/solution-architecture-vs-software-architecture)) | Concise distinction between solution and software architecture — helps architects articulate the difference to engineers |
| *Enterprise Integration Patterns* — Hohpe & Woolf ([enterpriseintegrationpatterns.com](https://www.enterpriseintegrationpatterns.com/)) | Integration pattern catalogue; directly applicable to the cross-PL integration designs EA must produce |
| *Software Product Line Engineering* — Pohl, Böckle, van der Linden ([Springer](https://link.springer.com/book/10.1007/978-3-662-03764-7)) | Rigorous PLE and variability management treatment; relevant to archetype design and variability documentation |
| *TOGAF Standard* — The Open Group ([opengroup.org](https://www.opengroup.org/togaf)) | Enterprise architecture framework; relevant to architecture governance (PAC) and portfolio-level architecture decisions |

---

[← Back to Career Guides](../README.md)
