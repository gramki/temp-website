# Engagement Lifecycle — Phase by Phase

[← Back to Guide](README.md)

The Engagement lifecycle has five phases: **Initiate → Discover → Build → Transfer → Complete**. Each phase has defined objectives, activities, active roles, inputs/outputs, and decision gates.

See [engagement-lifecycle.md](../product-line-engineering/processes/engagement-lifecycle.md) for detailed activity-level process.

The lifecycle begins at customer commitment. For the pre-Engagement phase, see [Exploration](exploration.md).

---

## Initiate

**Objective:** Assign Engagement-level roles, kick off the Engagement, confirm scope, agree on the operating model, and select the archetype.

**Key activities:**

- Engagement-level role assignment (see [Engagement Formation](engagement-formation.md)):
  - **ERC** assigns **Client Partner** (per-client, may already be in place), **EO**, **EPM**, **EA**, **AVA**, and ensures **CPA** support for the Client Partner
  - **EO** assigns **ELs**, **EPO**, **SRE Lead**
- Engagement kickoff with customer and internal stakeholders
- Scope confirmation based on Exploration artifacts
- Operating model agreement (selected during Exploration, confirmed here)
- Archetype selection or adaptation (EA-led)
- Commercial and contract confirmation (EPM + Account Management)

**Roles active:** Client Partner, CPA, ERC, EO, EPM, EA, AVA, EPO, ELs

**Inputs:** Exploration artifacts (scope outline, preliminary architecture, archetype assessment, commercial terms, operating model choice)

**Outputs:**

- Engagement charter with named Engagement-level roles
- Archetype selection and adaptation plan
- Initial squad activation plan
- Confirmed commercial terms

**Decision gate:** Engagement-level roles assigned; scope and operating model confirmed with customer; Engagement charter signed off.

---

## Discover

**Objective:** Staff squads with engineers, detail requirements, design the solution architecture, analyze gaps, and begin test strategy.

**Key activities:**

- ELs submit staffing requests to ERC Portfolio Program Manager (PPM); PPM consolidates demand across Engagements
- PPM presents consolidated demand to Product Line Squad leads; PL Squad leads check capacity and commit engineers
- Detailed requirements analysis (EPO-led)
- Solution architecture design (EA-led) — platforms, integrations, extensions, Studio Components
- Gap analysis (EA) — platform capability vs. customer need; plan inner source contributions or custom components
- AVA begins test strategy and cross-squad test suite planning
- SRE Lead begins operational readiness assessment

**Roles active:** EO, EPM, EA, AVA, EPO, ELs, Squad PMs, SRE Lead (advisory)

**Inputs:** Engagement charter with named roles, archetype (blueprint, cookbook, playbook), customer requirements, Product Line capacity

**Outputs:**

- Detailed requirements document
- Solution architecture document
- Work Model v1 and declarative specifications (EA, with EPO) — refined from the Exploration first cut
- Induction map (EA) — which existing customer systems enroll under Tool Contracts as Machines, at what effort
- Staffing plan with named individuals and rotation dates
- Gap analysis and inner source plan
- Test strategy (AVA)
- RACI and escalation path

**Decision gate:** Squads staffed and committed; solution architecture reviewed; requirements baselined; test strategy agreed.

---

## Build

**Objective:** Configure platforms, build extensions and integrations, assemble Studio Components, test, and progress toward production readiness.

**Key activities:**

- Platform provisioning and base configuration
- Configuration per archetype and customer
- Extension development within platform boundaries
- Integration development (customer systems, data, etc.)
- Induction execution per the induction map — existing customer systems wrapped in Tool Contracts and registered as Machines in the Work Model
- Studio Component development (UIs, workflows, applications)
- Composition and creation against the Work Model — gaps filled from Product Lines where capability exists, built where it does not
- Agent Swarm training and evaluation against the Work Model (agent definitions, authority grants, guardrail configurations)
- Inner source contributions — consult Product Line Maintainers, implement, submit PRs
- AVA certifies the assembly at every increment; the Verification Squad builds and maintains the verification module (IaC environment definitions, test suites, test data preparation, CI orchestration)
- Variability documentation (EA)
- Testing and validation (squads + Verification Squad)
- SRE Lead drives operational readiness: monitoring, alerting, runbooks, capacity planning

**Roles active:** EO, EPM, EA, AVA, EPO, ELs, Squad PMs, SRE Lead

**Inputs:** Staffed teams, solution architecture, archetype artifacts, platform access, customer access

**Outputs:**

- Configured and integrated assembly (Customer Product + Studio Components)
- Trained and evaluated Agent Swarm (agent definitions, evaluation records, authority grants, guardrail configurations)
- Variability documentation
- Test results and AVA certification
- Operational readiness artifacts (runbooks, escalation matrix, monitoring config)
- Merged inner source PRs and tech debt tickets

**Decision gate:** Go-live criteria met; AVA certifies assembly; SRE Lead confirms operational readiness; EPM confirms customer alignment.

---

## Transfer

**Objective:** Hand over the assembled product per operating model; capture knowledge; prepare for steady state.

**Key activities:**

- Handover per operating model:
  - **Fully Managed:** to Zeta run team; playbooks, escalation, access
  - **Co-Managed:** to Zeta run team and customer per contract; responsibility matrix
  - **Customer-Operated:** to customer with documentation, runbooks, escalation path
- EPO owns customer training and enablement
- Transfer of **command of the workforce** (EPO leads enablement; EA supports) — the customer's team trained to operate the Agent Swarm, author its guardrails, hold dial authority, and design escalations. Regulators require the customer to govern its own agents without the vendor; this applies across operating models — under Fully Managed, Zeta operates the Swarm, but the customer still holds guardrail and dial authority
- AVA hands over the verification module (test suites, environment definitions, test data tooling, CI orchestration, certification records) to run team or customer
- SRE Lead ensures operational readiness criteria are met
- EA finalizes variability documentation and proposes archetype updates
- Knowledge capture: retrospective, decision log, archetype updates, pattern extraction

**Roles active:** EO, EPM, EA, AVA, EPO, ELs, SRE Lead

**Inputs:** Assembled product in production, operational readiness artifacts, operating model

**Outputs:**

- Handover complete per operating model
- Verification module handed over (AVA) — test suites, environment definitions, test data tooling, certification records
- Training materials delivered (EPO)
- Knowledge capture artifacts (retrospective, decision log, archetype updates)
- Operational runbooks finalized (SRE Lead)

**Decision gate:** Handover criteria met per operating model; knowledge capture complete; SRE Lead signs off on operational readiness.

---

## Complete

**Objective:** Stabilize in production, release squads, close the Engagement, drive adoption and value delivery.

**Key activities:**

- Post-go-live stabilization and monitoring
- Resolution of remaining defects or transition issues
- EPM drives Engagement Success: adoption tracking, value delivery assessment
- Squad members released per plan
- Inner source repatriation — ensure Engagement-specific work that proved reusable is contributed back to Product Lines
- Engagement formally closed; final status communicated
- Retrospective and archetype updates submitted to PAC Practice Mode

**Roles active:** EO, EPM, EA (advisory), AVA (advisory), SRE Lead

**Inputs:** Production system, stabilization observations, open item list

**Outputs:**

- Engagement formally closed
- Squad members released
- Final retrospective and lessons learned
- Inner source contributions completed
- Engagement Success metrics captured

**Decision gate:** Stabilization criteria met; no critical open items; Engagement closed; Engagement Success metrics reviewed.

---

[← Previous: Roles and Responsibilities](roles.md) | [→ Next: Engagement Formation](engagement-formation.md)
