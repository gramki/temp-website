# Engagement Roles and Responsibilities

[← Back to Guide](README.md)

---

## Dual-Axis Reporting Model

Roles in the Engagement operating model operate on two independent axes:

- **Execution axis** (per-Engagement, temporary) — who you report to and work with during the Engagement. Established at Initiate; dissolved at Complete.
- **Functional/career axis** (permanent, spans Engagements) — who tracks your career growth, evaluates your multi-Engagement progression, manages your workload across concurrent assignments, and provides discipline-specific mentoring. This axis is unaffected by Engagement assignment.

Career progression is evaluated on the **functional axis**. Your functional-axis leader sees your full Engagement history and evaluates growth across assignments. The execution-axis leader (EO, EPM) evaluates your performance within the current Engagement and provides input to the functional-axis leader.

### Execution Axis

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

| Role | Reports to (execution axis) |
|------|----------------------------|
| Client Partner | Assigned by ERC; reports to AM leadership (functional axis) |
| CPA | Client Partner |
| EO | Client Partner |
| EPM, EA, AVA, EPO, SRE Lead | EO |
| ELs, Scrum Masters | EPM |
| Squad PMs, Engineers | EL (within squad) |
| Verification Squad engineers | AVA |

- **Client Partner** is the senior-most per-client role; EO reports to Client Partner. See [Client Partner ↔ EO authority boundary](#client-partner--eo-authority-boundary) below.
- **EO** directs EPM, EA, AVA, EPO, SRE Lead
- **EPM** directs ELs and Scrum Masters
- **AVA** directs the Verification Squad (the AVA is not an EL; authority comes from the architect role and certification responsibility)
- **ELs** direct engineers and Squad PMs within their functional squads
- **Scrum Masters** facilitate process across 1-3 squads; report to EPM, not to individual ELs
- **PL Squad ELs** have a dotted-line to EPM for coordination, but their primary reporting remains within the Product Line structure
- **Product Line Squad members** assigned to the Engagement retain their PL Squad Lead reporting line

### Functional/Career Axis

The functional axis is independent of any specific Engagement. It is where multi-Engagement experience becomes a seniority signal.

| Function | Functional-axis home | Typical Engagement roles |
|----------|---------------------|--------------------------|
| Engineering | Engineering leadership | EL, Engineers; may play EA/AVA on smaller Engagements |
| Architecture | Architecture leadership | EA, AVA |
| Product | Product leadership | EPO, Squad PM |
| Program / Delivery | Delivery leadership | EPM, Scrum Master, CPA (when from this function) |
| SRE / Operations | SRE / Platform Ops leadership | SRE Lead |
| Account Management | AM leadership | Client Partner, CPA (when from this function) |

Your functional-axis home is determined by your **function**, not your current Engagement role. A Staff Engineer playing EA remains in Engineering. An Architect playing EA is in Architecture. Each functional track is owned by a VP (or Director/Sr. Director, reporting to another VP, if org size does not warrant a VP per track). This guide does not prescribe the full organizational structure — what matters is that every person has a permanent functional home that tracks career growth across Engagements.

### Client Partner ↔ EO Authority Boundary

- **Client Partner** owns client-facing decisions: stakeholder management, commercial alignment, relationship strategy.
- **EO** retains full internal delivery authority: architecture, quality, squad execution.
- When delivery decisions affect client commitments → EO recommends; Client Partner decides.
- When client demands affect delivery feasibility → Client Partner brings to EO; EO assesses.
- **Client Partner cannot override AVA release-block authority.** AVA's certification and release-block decisions are independent of Client Partner.
- **ERC** is the escalation endpoint for Client Partner ↔ EO disagreements (ERC assigned both roles).

---

## Mandatory Architect Consultation

EA and AVA are peer architects who review the work of functional squads. Squads must consult the relevant architect:

- **EA mandatory review:** Architecture-significant changes — integration design, configuration approach, inner source decisions, platform boundary changes — require EA review before implementation. This is part of the squad's Definition of Done.
- **AVA mandatory review:** Assembly-impacting changes — anything that affects integration seams, cross-squad interfaces, configuration correctness, or deployment topology — require AVA review to assess verification impact. This is part of the squad's Definition of Done.
- **Ceremony attendance:** EA and AVA attend relevant squad planning and review ceremonies to maintain context and provide early guidance. Catching issues at planning is cheaper than catching them at review.
- **EL obligation:** ELs ensure that architecture-significant and assembly-impacting work is reviewed by EA and AVA respectively before completion.

---

## Client Partner

**Purpose:** The Client Partner is the **senior-most per-client role**, owning the strategic client relationship. The Client Partner may span multiple Engagements with the same client (bandwidth permitting). EO reports to Client Partner on the execution axis.

**Responsibilities:**

- Strategic client relationship — stakeholder mapping, executive alignment, relationship health
- Commercial and contract alignment — ensures delivery and commercial terms stay in sync; works with Account Management
- Client-facing governance — client-side governance meetings, executive briefings, escalation to client leadership when needed
- When delivery decisions affect client commitments, the Client Partner decides (with EO recommendation)
- When client demands affect delivery feasibility, the Client Partner brings to EO for assessment

**Authority:** Client-facing decisions (stakeholder management, commercial alignment, relationship strategy). Cannot override EO on internal delivery authority or AVA release-block authority.

**Key relationships:** Reports to Account Management leadership (functional axis); assigned by ERC. EO reports to Client Partner. Works with CPA(s), EPM (customer-facing coordination), Account Management.

**Staffing:** Per-client, not per-Engagement. One Client Partner per client; may span multiple Engagements with that client. ERC assigns. Supported by at least one Client Partner Associate (CPA).

**Typical challenges:**

- Balancing client expectations with delivery reality — the client wants more, faster; the EO owns what is feasible
- Spanning multiple Engagements with the same client — prioritization and context-switching across EOs
- Knowing when to escalate to client leadership vs. when to resolve internally with EO and EPM

---

## Client Partner Associate (CPA)

**Purpose:** The CPA is **generalist support for the Client Partner** — governance preparation, stakeholder coordination, commercial tracking, cross-Engagement alignment, executive briefings, and operational work. The role is defined by its operational accountability. CPA experience across multiple clients is a natural progression toward the Client Partner role, but the role is not a training position.

**Responsibilities:**

- Governance meeting preparation and follow-up (client-side governance)
- Stakeholder mapping and relationship tracking across the client organization
- Commercial alignment tracking (scope change impact, contract status)
- Cross-Engagement coordination for multi-Engagement clients (e.g. status consolidation across EOs)
- Executive briefing preparation and client communication drafting
- Internal coordination (ERC reporting, AM coordination)

**Reporting:** Reports to Client Partner (execution axis). Functional-axis home is Account Management or Program/Delivery, depending on the person's background.

**Staffing:** At least one CPA per Client Partner; more for multi-Engagement or complex clients. ERC ensures CPA support is in place as part of Client Partner assignment. CPAs are drawn from Account Management or Program/Delivery function.

**Typical challenges:**

- Juggling multiple workstreams (governance, commercial, cross-Engagement) without direct authority over delivery
- Building context quickly when joining a client with existing Engagements and stakeholders

---

## Engagement Owner (EO)

**Purpose:** The EO is a per-Engagement assignment of a **senior delivery leader** with overall accountability for the Engagement's success. The EO reports to the Client Partner on the execution axis and retains full internal delivery authority.

**Responsibilities:**

- Overall accountability for Engagement outcomes (delivery, quality, customer satisfaction)
- Strategic direction and alignment with organizational objectives
- Final escalation endpoint for all role-level disputes within the Engagement
- Ensure adequate resourcing and remove systemic blockers
- Sponsor Engagement-level decisions that exceed EPM or EA authority

**Authority:** Final decision-maker for Engagement-level disputes within the Engagement; may override any role-level decision when escalation reaches the EO level. EO retains full internal delivery authority; Client Partner cannot override EO on delivery execution.

**Key relationships:** Reports to Client Partner (execution axis); directs EPM, EA, AVA, EPO, SRE Lead; ELs report through EPM; receives escalations from all Engagement roles. Works with Client Partner on delivery–client trade-offs.

**Typical challenges:**

- Accountability without direct authority over most execution — EPM, EA, ELs do the work; the EO must lead through them, not around them
- Knowing when to intervene vs. when to let EPM or EA resolve — over-involvement undermines the role structure; under-involvement lets problems fester
- Balancing customer and commercial pressure with engineering integrity — the customer wants speed; the EA or AVA may say "not ready"
- Scope and timeline trade-offs that ripple across the portfolio — an EO decision on one Engagement may affect capacity for others

---

## Engagement Program Manager (EPM)

**Purpose:** The EPM is the **primary customer-facing contact** for the Engagement, responsible for the integrated progress/risk/dependency view, commercial alignment, and the **Engagement Success** function.

**Responsibilities:**

- Primary customer-facing contact — represents Zeta on delivery progress, risks, dependencies, and commercial matters
- Integrated progress view across all squads (CP, Studio, PL)
- Risk and dependency management across the Engagement
- Commercial view — ensures alignment between delivery scope and contract terms; keeps Account Management informed and verifies alignment
- **Engagement Success function** — drives readiness, adoption, and value delivery beyond engineering completion
- Serves ELs on staffing needs and rotation coordination
- Scope change management — ensures changes are aligned with AM and contracts

**Authority:** Customer-facing decisions on delivery communication and commercial alignment; resolves EA-vs-AVA and EPO-vs-EA disputes before escalation to EO.

**Key relationships:** Reports to EO (execution axis); directs CP Squad ELs and Studio Squad ELs; works with EA (architecture), AVA (verification), EPO (requirements), Account Management (commercial), SRE Lead (operations). Governed by ERC.

**Staffing:** One EPM per Engagement. A person may serve as EPM for multiple Engagements if bandwidth permits.

**Typical challenges:**

- Being the single customer-facing contact without having direct control over squads — the EPM depends on ELs and EA for information, but the customer expects answers from the EPM
- Synthesizing status from multiple squads into a coherent picture — squads operate at different cadences with different blockers; the "integrated view" is harder than it sounds
- Scope creep management at the contract-delivery intersection — customers always want more; contracts constrain; delivery teams have capacity limits. The EPM sits at the intersection of all three.
- Driving Engagement Success (adoption) when it depends on customer actions the EPM can influence but not control
- The commercial alignment role — keeping Account Management, contract terms, and delivery scope in sync without becoming a commercial negotiator

---

## Engagement Architect (EA)

**Purpose:** The EA owns **architecture across the entire Engagement span** — Customer Product, Studio Components, and their integration. The EA role is played by a member of the Architecture function (for complex Engagements) or a Staff/Principal Engineer from the Engineering function (for smaller Engagements). The person's functional-axis home does not change because of the EA role assignment.

**Responsibilities:**

- End-to-end solution architecture: Product Line selection, configuration approach, integration design, Studio Component architecture
- Archetype selection and adaptation
- Gap analysis — platform capability vs. customer need
- Co-define assembly acceptance criteria with AVA — the architecture determines what "correct assembly" means (integration seams, cross-platform interfaces, configuration correctness); EA must articulate these so AVA can design meaningful verification
- Design for verifiability — architecture decisions should be testable at the assembly level; EA and AVA jointly define the system-under-test boundary and identify which integration boundaries require assembly-level verification
- Variability documentation per [Variability Management](../product-line-engineering/framework/variability-management.md)
- Security in design — EA is responsible for ensuring security is addressed in the architecture
- **Engineering quality standards** — EA owns the quality standards across the Engagement: architecture decisions, coding standards for architecture-significant concerns, mandatory review in Definition of Done, inner source quality gates. ELs take responsibility for meeting these standards within their squads.
- Inner source debt and priority — maintains a view of inner source debt across the Engagement and prioritizes contributions
- Knowledge capture — decision log, archetype updates, pattern extraction
- Mandatory review of architecture-significant squad work (see [Mandatory Architect Consultation](#mandatory-architect-consultation))

**Authority:** Architectural decisions within Council and platform standards; proposes archetype updates; escalates to PAC when needed.

**Key relationships:** Peer architect to AVA — EA architects the functional system, AVA architects the verification system; peer to EPO (requirements-architecture boundary); reports to EO (execution axis); works with ELs, Squad PMs, Product Line Maintainers.

**Assessment framework:** EA effectiveness is assessed on Product Line leverage, gap anticipation, contribution back (inner source), and stakeholder effectiveness.

See [engagement-architect.md](../product-line-engineering/roles/engagement-architect.md) for the full role specification.

**Typical challenges:**

- Every gap is a hard decision: inner source (slow, dependent on PL Maintainers), custom build (risk of drift), or workaround (tech debt). There is rarely an obvious right answer.
- Architecture must be defined early, but gaps emerge late — the EA must anticipate what they can't yet see
- Ensuring architecture decisions are verifiable — if the AVA can't certify the assembly against the architecture, the architecture isn't done. This joint work with AVA is substantial.
- Working across multiple squads without direct authority — ELs own their squads; the EA advises and escalates, but cannot direct
- Variability documentation is easy to deprioritize under delivery pressure, but it's the primary mechanism for future Engagement leverage

---

## Assembly Verification Architect (AVA)

**Purpose:** The AVA is a **peer architect to the EA**. The EA architects the functional assembly; the AVA **architects, builds, and operates the verification system** that certifies it. The AVA certifies the assembled product at every increment and holds **independent authority to block release** when assembly quality criteria are not met. Like EA, the AVA role is played by a member of the Architecture function or a senior engineer from the Engineering function. AVA requires architecture-level breadth applied to the verification domain.

**Responsibilities:**

- Architect the verification system — design the system-under-test boundary (with EA), the test environment topology, the verification strategy, the test data model, and the CI orchestration. This is architecture work: the verification system is a complex, multi-component system in its own right.
- Co-design the verification strategy with EA — jointly define the system-under-test boundary, integration seams that need assembly-level testing, configuration correctness criteria
- Define assembly acceptance criteria jointly with EA — these criteria drive the verification module and become the basis for certification decisions
- Direct the Verification Squad — build and maintain the verification module (IaC environment definitions, test suites, test data preparation, CI orchestration) as a first-class artifact group of the Engagement Assembly. The AVA is not an EL; the Verification Squad has no EL. The AVA directs engineers through architectural authority, not through the EL role.
- Certify the integrated assembly (across CP, Studio, and PL contributions) at every increment
- Define and enforce assembly quality criteria
- Authority to block release when criteria are not met — this authority is independent and not overridable by EA, EL, or EPM
- Mandatory review of assembly-impacting squad work (see [Mandatory Architect Consultation](#mandatory-architect-consultation))
- Hand over the verification module (test suite, environment definitions, test data tooling) to the run team or customer at Transfer/Complete

**Authority:** Release authority — AVA approval is required for any release of the assembled product. AVA may block release independently.

**Key relationships:** Peer architect to EA — EA architects the functional system, AVA architects the verification system. Both require full-breadth understanding of the assembly, both work across all squads, and both make architecture-level design decisions. Works with ELs (squad testing integration), EPM (release coordination), SRE Lead (operational readiness verification).

**Staffing:** One AVA per Engagement. A person may be shared across Engagements if bandwidth permits. When scope warrants it, the AVA directs a dedicated Verification Squad (see [Verification and Certification](verification-and-certification.md)).

**Typical challenges:**

- Architecting a verification system for an assembly that has no single release version — this is architecture work, not test management
- Exercising release-block authority under customer and commercial pressure — saying "no" is the hardest part of the role, and the most important
- Keeping the verification module in sync with a multi-squad assembly that evolves every increment — the verification code must evolve alongside the functional code
- Defining the system-under-test boundary — what's inside the boundary (real deployed components), what's simulated at the edges, and keeping the boundary accurate as the assembly grows
- The same cross-domain breadth demanded of the EA, applied to verification — the AVA must understand the full technical breadth of the assembly to verify it

See [Verification and Certification](verification-and-certification.md) for the full verification model.

---

## Engagement Product Owner (EPO)

**Purpose:** The EPO drives **customer discovery, needs analysis, and requirements detailing**, translating customer needs into actionable requirements that squads can execute.

**Responsibilities:**

- Customer discovery — work with customers to understand their needs, pain points, and desired outcomes
- Needs analysis and requirements detailing — produce well-structured requirements
- Work with EA to translate requirements into architectural decisions
- Feed Squad PMs with requirements — Squad PMs pick and prioritize within their squad backlogs
- Own customer training and enablement — ensure customers understand and can use the delivered product

**Authority:** Requirements authority — EPO determines what the customer needs; Squad PMs determine how to prioritize and execute within their squads.

**Key relationships:** Peer to EA (requirements-architecture translation); reports to EO (execution axis); works with Squad PMs (requirements handoff), EPM (customer alignment), customers (discovery).

**Staffing:** One EPO per Engagement. A person may serve as EPO for multiple Engagements if bandwidth permits.

**Typical challenges:**

- Bridging customer language with engineering requirements — customers describe problems and outcomes; engineers need specifications and acceptance criteria
- Discovery depth vs. delivery velocity — spending too long in discovery delays delivery; too little means rework during Build
- Managing the requirements flow to multiple Squad PMs without becoming a bottleneck — if every requirement must go through the EPO, the EPO becomes a single point of failure
- Requirements change as the customer sees the product taking shape — managing this without creating chaos in squad backlogs
- Customer training and enablement is often deprioritized under delivery pressure but is critical for Engagement Success

---

## SRE Lead

**Purpose:** The SRE Lead ensures **operational readiness** for the Engagement, covering monitoring, alerting, runbooks, capacity planning, and the operational transition.

**Responsibilities:**

- Operational readiness planning from Discover (advisory) through Complete
- Monitoring and alerting configuration for the assembled product
- Runbook creation and maintenance
- Capacity planning for the production environment
- Operational transition management per the chosen operating model
- Incident response planning and escalation matrix
- **Release coordination** — owns the mechanics of getting a certified assembly into production: deployment sequencing, environment promotion, release notes, production cutover. AVA decides *whether* the assembly can be released (release authority); SRE Lead manages *how* it is released.

**Authority:** Operational readiness sign-off — SRE Lead must approve that operational criteria are met before Transfer. Release mechanics authority — SRE Lead owns the deployment process.

**Key relationships:** Reports to EO (execution axis); SRE / Platform Ops leadership (functional/career axis). Works with EA (architecture-operations alignment), AVA (release authority — AVA certifies, SRE Lead deploys), EPM (operational readiness communication), ELs (squad operational requirements).

**Staffing:** Named per Engagement, usually from the dominant Product Line's SRE team.

**Typical challenges:**

- Joining mid-Build but needing to influence decisions made earlier (architecture, infrastructure, deployment approach) — retrofitting operational readiness is harder than building it in
- Ensuring operational readiness isn't treated as an afterthought — build teams focus on building, not on running
- Building runbooks and monitoring for a system that's still evolving — the target keeps moving until late Build
- Different operating models (Fully Managed, Co-Managed, Customer-Operated) require very different operational handover approaches — the SRE Lead must adapt

---

## Engineering Lead (EL)

**Purpose:** The EL is the **per-squad role** responsible for squad commitments — engineering and tech leadership with delivery accountability.

**Responsibilities:**

- Primary responsible for squad delivery commitments (scope, timeline, quality)
- Engineering and technical leadership within the squad
- Coordinate squad members: engineers, Squad PM, and other functions
- **Meet EA's engineering quality standards** — EA sets the standards (architecture decisions, mandatory review, inner source quality); EL is responsible for meeting them within the squad
- Participate in cross-squad coordination with EPM and other ELs
- Execute inner source contributions prioritized by EA
- Ensure architecture-significant and assembly-impacting work is reviewed by EA and AVA respectively before completion — this is part of the squad Definition of Done
- Support rotation planning with EPM

**Authority:** Squad-level delivery decisions; technical decisions within squad scope; escalates to EA (architecture), EPM (cross-squad), or EO (Engagement-level) when needed.

**Key relationships:** Reports to EPM (execution axis); Engineering leadership (functional/career axis). Works with EA (architecture guidance, mandatory review, quality standards), AVA (assembly verification, mandatory review), EPO (requirements), Squad PM (prioritization), Scrum Master (process facilitation).

**Squad types:**

- **CP Squad EL** — leads the Customer Product squad; the Exploration Lead is the preferred candidate for this role
- **Studio Squad EL** — leads the Studio Components squad
- **PL Squad EL(s)** — leads Product Line squads contributing to the Engagement

**Typical challenges:**

- Managing a squad with engineers borrowed from Product Line Squads — varying familiarity with the customer context, different working styles, and awareness that people will rotate back
- Balancing delivery commitments with inner source expectations — EA prioritizes inner source, but the EL owns squad delivery and timeline
- For CP Squad EL transitioning from Exploration Lead: shifting from discovery mindset to delivery accountability
- Navigating between EA (architecture guidance), EPM (coordination), AVA (verification requirements), and squad autonomy — the EL is at the intersection of many authorities

---

## Portfolio Program Manager (PPM)

**Purpose:** The PPM is an **ERC function** — not a per-Engagement role — responsible for **cross-Engagement capacity coordination and staffing demand consolidation**. The PPM ensures that Engagements do not independently compete for Product Line engineers.

**Responsibilities:**

- Maintain the cross-Engagement portfolio view — which Engagements need what capacity, when
- Consolidate staffing demand from all Engagements and present a unified demand view to Product Line Squad leads
- Coordinate supply commitments from PL Squad leads so that ELs do not independently approach PL Squads
- Support ERC in prioritization decisions when multiple Engagements compete for the same capacity

**Key relationships:** Reports within ERC; works with ELs (receives staffing requests), PL Squad leads (capacity negotiation), EO and EPM (Engagement-level demand).

---

## Squad Product Manager (Squad PM)

**Purpose:** The Squad PM is a **product role** at the squad level — owning the squad backlog, prioritization, and requirements decomposition. The Squad PM is not a process role; process facilitation belongs to the Scrum Master.

**Responsibilities:**

- Pick and prioritize requirements from EPO's input into the squad backlog
- Own the squad backlog — all work items, their priority, and their acceptance criteria
- Requirements decomposition — break EPO-level requirements into squad-executable work items
- Set execution priorities within the squad in coordination with EL
- Communicate progress and blockers to EPM

**Reporting:** EL (execution axis, within squad); Product leadership (functional/career axis).

**Key relationships:** Works with EPO (receives requirements), EL (execution alignment), Scrum Master (process coordination), EPM (progress reporting).

**Typical challenges:**

- Prioritizing across competing inputs: EPO requirements, EA inner source work, AVA verification requirements, tech debt — everything is "important"
- Working within a temporary squad with unfamiliar team dynamics — building cadence quickly matters
- Balancing throughput with quality — delivery pressure is real, but AVA will block release if quality isn't there
- Distinguishing product decisions (what to build, in what order) from process decisions (how to run the sprint) — the Squad PM owns the former; the Scrum Master owns the latter

---

## Scrum Master

**Purpose:** The Scrum Master is a **process facilitation role** serving 1-3 squads within an Engagement. The Scrum Master owns ceremonies, impediment removal, cadence, and team health — enabling ELs to focus on engineering leadership and delivery.

**Responsibilities:**

- Facilitate squad ceremonies (standups, sprint planning, retrospectives, demos)
- Impediment removal — identify and escalate blockers that squads cannot resolve internally
- Cadence and rhythm — establish and maintain sprint cadence across the squads served
- Team health — monitor and surface team dynamics, workload balance, and collaboration issues
- Process consistency — ensure consistent agile practices across the squads served, adapted to each squad's context
- Cross-squad process coordination — when serving multiple squads, surface common impediments and alignment opportunities to EPM

**Reporting:** EPM (execution axis); Program / Delivery leadership (functional/career axis).

**Staffing:** One Scrum Master may serve 1-3 squads within an Engagement. The Verification Squad does not have a Scrum Master — the AVA directs through architectural authority.

**Relationship to EL:** The Scrum Master facilitates process for the EL's success but does not direct engineering work. The EL owns delivery commitments; the Scrum Master owns process health. Tension between EPM's process consistency expectations and EL's squad-level flexibility is healthy and expected; the escalation path is EL → EPM.

**Typical challenges:**

- Serving multiple squads with different ELs, different cadences, and different maturity levels — each squad needs adaptation, not uniformity
- Being process-oriented in a delivery-pressure environment — when delivery is behind, ceremonies and process feel like overhead, but they are how the squad recovers
- Building cadence quickly in a temporary squad — the squad may be newly assembled from different contexts; the Scrum Master must establish rhythm fast
- Balancing EPM's process expectations with EL preferences — the EPM wants consistency; ELs want autonomy. The Scrum Master navigates this daily.

---

## Security (Shared Team under ERC)

Security is not a standalone Engagement role but a shared capability:

- **EA** is responsible for security in design — ensuring the architecture addresses security requirements
- **Squads** implement security requirements as part of their engineering work — engineers incorporate security test cases into their testing work
- **Shared security team under ERC** performs VA/PT and security reviews — periodic or on-demand, not embedded per Engagement

---

[← Previous: Exploration](exploration.md) | [→ Next: Lifecycle](lifecycle.md)
