# Open Items — What This Guide Does Not Yet Cover

[← Back to Guide](README.md)

---

This document lists topics the guide acknowledges as gaps or future work, organized by stakeholder perspective. Each item describes what is needed and why it matters.

This list is maintained transparently so that practitioners know what they can reference from the guide today and what requires judgment, local practice, or future additions.

---

## Engineering Leads (ELs)

- **Squad-level Definition of Done template** — A referenceable DoD that incorporates EA/AVA mandatory review, inner source obligations, variability documentation contributions, and squad-specific quality criteria. Currently, the guide states that EA and AVA review are part of the DoD but does not provide a template.
- **Cross-squad coordination patterns** — How ELs from CP, Studio, and PL squads coordinate beyond EPM-mediated ceremonies and Scrum Master-facilitated processes. Patterns for shared dependencies, cross-squad blockers, and integration sequencing are not documented.
- **Squad onboarding playbook** — How to onboard engineers borrowed from Product Line Squads: context transfer, customer domain ramp-up, tooling setup, and squad norms. Currently left to individual EL judgment.

---

## Engagement Program Managers (EPMs)

- **Engagement Success function detail** — The guide defines Engagement Success as readiness, adoption, and value delivery, but does not describe how to measure readiness, what adoption tracking looks like in practice, how value delivery is assessed, or what "success" means at each lifecycle phase. This is the most significant gap for the EPM role.
- **Portfolio context from EPM's perspective** — How the EPM's Engagement fits in the broader portfolio, how priority conflicts with other Engagements are communicated and resolved from the EPM side (not just from PPM's view), and how EPMs share learnings across concurrent Engagements.
- **Multi-Engagement EPM guidance** — Practical patterns for EPMs serving multiple Engagements concurrently: how to manage context switching, where to delegate, what signals indicate overload.

---

## Engagement Architects (EAs) / Architecture Function

- **Archetype application walkthrough** — Step-by-step guidance for applying a blueprint, cookbook, and playbook to a new Engagement. The archetype framework is defined in PLE, but "how to actually use it during Discover and Build" is thin.
- **Variability documentation workflow** — Where and when to document configuration points, the review cadence, and the submission process to PAC. The obligation is stated; the workflow is not.
- **Architecture function structure** — The guide establishes Architecture as a separate functional track with its own leadership (VP or Director). The internal structure of the Architecture function — how architects are organized, how EA/AVA assignments are managed, how architecture career progression is evaluated — is not yet defined.
- **Cross-track jump criteria** — The guide describes cross-track jumps from Engineering, Product, and EM into Architecture. The specific assessment criteria, evaluation process, and readiness signals for a cross-track transition are not defined.

---

## Assembly Verification Architects (AVAs)

- **Verification module templates** — Starter templates for environment definitions (IaC), test suite structure, test data preparation scripts, and CI orchestration configurations. Currently the guide describes what the module contains but provides no starting point.
- **Certification record format** — What a certification record looks like, what fields it contains (assembly manifest, criteria status, known issues, risk assessment), and how it is versioned across increments.
- **Verification module estimation guidance** — How to estimate verification effort relative to assembly complexity (number of Product Lines, integration seams, squad count). Currently there is no sizing guidance for verification work.

---

## Scrum Masters

- **Multi-squad facilitation patterns** — The guide defines the Scrum Master as serving 1-3 squads, but does not describe how to manage competing ceremony schedules, how to adapt process to squads with different ELs and maturity levels, or when serving three squads becomes unsustainable.
- **Scrum Master onboarding for temporary squads** — How a Scrum Master establishes cadence in a newly assembled squad with engineers borrowed from different Product Line contexts. Patterns for rapid team norming are not provided.

---

## Engagement Product Owners (EPOs)

- **Requirements flow to Squad PMs** — The detailed handoff mechanism from EPO to Squad PMs: how requirements are decomposed, acceptance criteria format, prioritization protocol, and how requirements changes are communicated mid-Build.
- **Training and enablement playbook** — What customer training looks like at Transfer, materials structure, delivery format, feedback collection, and how training content relates to operating model choice (Fully Managed vs. Co-Managed vs. Customer-Operated).

---

## SRE Leads

- **Operational readiness checklist** — A per-operating-model checklist (Fully Managed, Co-Managed, Customer-Operated) that the SRE Lead works through from Discover to Transfer. The guide now defines release coordination as an SRE Lead responsibility (with AVA holding release authority), but does not provide a structured readiness checklist.
- **Operating model-specific handover guide** — What differs in the operational handover for each model: what artifacts are produced, who receives them, what ongoing responsibilities remain with Zeta.
- **Incident response planning template** — A baseline incident response structure for Engagements: escalation tiers, response time expectations, communication protocols, and how incident response integrates with the customer's own processes.

---

## Client Partners

- **Client Partner–EPM coordination protocol** — When and how the Client Partner and EPM align on customer-facing communication, escalation to the client, and commercial alignment. The guide defines both roles and the CP ↔ EO authority boundary but does not specify the day-to-day coordination rhythm.
- **Client Partner scaling for multi-Engagement clients** — When one Client Partner spans many Engagements, what triggers additional CPAs or a different support model. The guide states that multiple CPAs may be staffed for complex clients but does not define activation criteria.

---

## Engagement Owners (EOs)

- **EO heritage matching criteria** — The guide states that EO may be drawn from Architecture, Delivery, or Engineering heritage and that ERC considers complexity and risk. The specific criteria ERC uses to match EO heritage to Engagement profile (e.g. when to assign an Architect vs. a Delivery leader) are not defined.
- **EL functional-axis coordination mechanics** — How the EO/EPM (execution axis) and the EL's functional-axis leader coordinate on performance input, rotation timing, and workload. The dual-axis model is described; the operational mechanics are not.
- **Intervention framework** — When to intervene vs. let EPM/EA resolve; signals that indicate intervention is needed (e.g., repeated escalations, customer relationship deterioration, sustained delivery deviation). The guide defines the EO as the final escalation point but does not describe the judgment framework.
- **Portfolio-level decision patterns** — How EO decisions on one Engagement (scope changes, staffing priorities, timeline shifts) affect the broader portfolio. EOs need guidance on when their per-Engagement decisions require portfolio-level coordination.

---

## Sales and Account Management

- **Exploration-to-Engagement handoff detail** — What artifacts carry over from Exploration to Initiate, how context is preserved (especially when the Exploration Lead continues as CP Squad EL), and what Sales/AM should expect from the Engagement side after handoff.
- **Commercial alignment touchpoints** — When and how EPM communicates commercial-impacting changes during the lifecycle (scope changes, timeline shifts, resource changes that affect contract terms). The guide states EPM owns commercial alignment but does not define the touchpoint cadence.

---

## Cross-Cutting

- **Designation-to-complexity matching calibration** — [Engagement Formation](engagement-formation.md) provides an illustrative table for matching designation level to Engagement complexity. Calibration (how to tune this per organization, how ERC applies it in practice) is not defined.
- **Formation retrospective process** — How to capture and act on formation learnings (e.g. wrong designation level, scaling pattern activated too late). No formal retrospective or feedback loop for the formation process is described.
- **Tooling guidance** — The guide is currently tool-agnostic. Practitioners need clarity on expected project management, documentation, communication, and decision-logging tools. This may vary by organization and should be specified or explicitly left to Engagement-level choice.
- **Engagement sizing and estimation** — How to estimate Engagement duration, squad count, and complexity before or during Initiate. No guidance currently exists; sizing is left to EA and EPM judgment.
- **Operating model selection criteria** — How to choose between Fully Managed, Co-Managed, and Customer-Operated during Exploration. The operating model options are described in the [PLE guide](../product-line-engineering/framework/operating-models.md), but the decision framework (what factors drive the choice, who decides, how it's revisited) is absent.

---

[← Previous: Career Paths](career-paths.md)
