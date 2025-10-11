# Roles Reference — Enterprise Delivery Projects

This reference catalogs key roles across Customer Team and Delivery Team, including responsibilities, key decisions, core artifacts, collaboration patterns, and governance participation. Use it to set up RACI, define meeting participants, and clarify decision rights.

---

## Customer Team Roles

### Executive Sponsor
- **Accountability**: Owns business outcomes, budget authority, executive alignment
- **Key Decisions**: Investment approvals, scope pivots, risk acceptance, escalation resolutions
- **Core Artifacts**: Executive vision, success criteria, business case
- **Collaboration**: Works with VP Delivery / Delivery Manager; chairs or attends Steering
- **Governance**: Steering Committee, major escalations, monthly/quarterly reviews

### Program Sponsor (Business Owner)
- **Accountability**: Program goals, funding and prioritization, benefits realization
- **Key Decisions**: Roadmap changes, trade-offs on scope/time/cost, CR approvals at threshold
- **Core Artifacts**: Program charter, KPIs/OKRs, prioritization backlog
- **Collaboration**: Product Owners, Delivery Manager, Commercial Manager
- **Governance**: Steering, Commercial Review

### Customer Product Owner (CPO)
- **Accountability**: Product value definition and acceptance on behalf of business
- **Key Decisions**: Feature priorities, acceptance criteria, release readiness for business
- **Core Artifacts**: Product vision, feature backlog, acceptance criteria
- **Collaboration**: Two-in-a-box with Delivery Product Owner; works with BAs, Customer PM
- **Governance**: Backlog Review, Sprint Review, Release Readiness, Steering (as needed)

### Customer Product Manager(s)
- **Accountability**: Primary responsibility to translate business requirements into product features; co-decompose with the Customer PO; ensure value alignment and business acceptance readiness
- **Key Decisions**: Feature definition and slicing priorities, acceptance scope, sequencing aligned to business value
- **Core Artifacts**: Feature specs, story maps, acceptance criteria, business value notes
- **Collaboration**: Customer Product Owner, Delivery Product Owner, Delivery Product Managers, SMEs
- **Governance**: Planning, refinement, change control inputs, release readiness

### Customer Project Manager / PMO Representative
- **Accountability**: Customer-side coordination, milestone alignment, risk/issue tracking
- **Key Decisions**: Scheduling commitments, dependency coordination, stakeholder comms
- **Core Artifacts**: Integrated plan, RAID log, status reports
- **Collaboration**: Delivery Manager, Customer PO, Architects, QA Lead
- **Governance**: Weekly status, risk reviews, change control board (CCB)

### Business Stakeholders / SMEs
- **Accountability**: Domain input, validation of requirements and UAT
- **Key Decisions**: Process decisions, policy interpretation, acceptance for domain areas
- **Core Artifacts**: Process maps, policy clarifications, UAT scenarios
- **Collaboration**: Product team, BAs, QA teams
- **Governance**: Workshops, UAT sign-off ceremonies

### Customer QA Lead
- **Accountability**: Acceptance testing quality, test strategy alignment
- **Key Decisions**: UAT scope, acceptance gates, defect triage decisions
- **Core Artifacts**: UAT plan, test cases, acceptance sign-offs
- **Collaboration**: Delivery QA Lead, Product Owners, SMEs
- **Governance**: Quality Council, release gates

### Customer Technical Lead / Enterprise Architect
- **Accountability**: Alignment to enterprise standards, integration guardrails
- **Key Decisions**: Integration patterns, non-functional requirements, architectural exceptions
- **Core Artifacts**: Interface contracts, standards, architecture decisions
- **Collaboration**: Solution Architect, Integration Lead
- **Governance**: Architecture Roundtable, design reviews

---

## Delivery Team Roles

### VP Delivery Leadership (Engagement Owner)
- **Accountability**: Strategic delivery posture, executive relationship, governance discipline; business owner of the delivery business for the firm; owns the engagement P&L
- **Key Decisions**: Escalation stance, guardrails, resourcing strategy, engagement model, Studio charter approvals, financial targets and rebaseline decisions
- **Core Artifacts**: Operating model, governance framework, executive comms, Studio charter, P&L reviews
- **Collaboration**: Executive Sponsor, Program Sponsor, Studio Owner, Delivery Manager
- **Governance**: Steering, monthly operational review, Studio performance reviews

### Delivery Manager (Engagement Program Head)
- **Accountability**: End-to-end delivery outcomes, schedule, scope, risk, stakeholder alignment; operates within the Studio organization
- **Key Decisions**: Delivery trade-offs, plan of record, escalation triggers
- **Core Artifacts**: Integrated plan, RAID, dashboards, comms plan
- **Collaboration**: Customer PM/PMO, Product Owners, Tech & QA leads, Commercial Manager, Studio Owner
- **Governance**: Daily/weekly rituals, risk reviews, Steering prep, CCB

### Delivery Product Owner (Two-in-a-Box with Customer Product Owner)
- **Accountability**: Co-owns product outcomes and backlog quality with the Customer PO; ensures product strategy is informed by technical and delivery feasibility; plays the Solution Architect role for end-to-end solution intent; is supported by Delivery Product Managers for decomposition and readiness
- **Key Decisions**: Backlog ordering with feasibility lens, acceptance readiness, release scope proposals, solution design trade-offs aligned to NFRs and enterprise constraints
- **Core Artifacts**: Joint product roadmap, refined backlog, acceptance criteria, release notes, solution intent and guardrails
- **Collaboration**: Pairs with Customer PO; supported by Delivery Product Managers; works with Technical Architects (as-needed), QA Lead
- **Org Placement**: Part of the Engagement Owner’s organization
- **Governance**: Backlog refinement, Sprint Review, Release Readiness, Architecture reviews (as owner), Steering inputs on scope trade-offs

### Delivery Product Manager(s)
- **Accountability**: Support the Delivery Product Owner; operationalize the translation of requirements to features driven primarily by Customer Product Managers; decompose features → epics → stories; ensure traceability and delivery feasibility; wear the Business Analyst hat where required (requirement discovery, clarification, documentation, taxonomy, traceability)
- **Key Decisions**: Story readiness (MAR), definition-of-ready gates, slicing strategy
- **Core Artifacts**: Requirement specs when acting as BA, epic/story maps, refinement notes, impact/risk notes, acceptance criteria drafts, traceability matrices
- **Collaboration**: Customer Product Managers, Customer Product Owner, Delivery Product Owner, Tech/QA leads
- **Org Placement**: Part of the Studio Owner’s organization
- **Governance**: Requirement gates (MAR, RfP), planning, refinement, change control inputs

<!-- Business Analyst role intentionally folded into Delivery Product Manager responsibilities -->

### Technical Architect (Supporting Role)
- **Accountability**: Provide technical depth and architectural support under the Delivery Product Owner’s solution intent
- **Key Decisions**: Recommend architecture patterns, technology choices, and risk mitigations for DPO decision
- **Core Artifacts**: Architecture diagrams, ADRs, NFR specs, integration blueprints
- **Collaboration**: Delivery Product Owner (as solution architect), Customer Enterprise Architect, Integration Lead, Tech Lead
- **Governance**: Participate in architecture reviews; advise on design sign-offs

### Integration Lead
- **Accountability**: Cross-system integration strategy and execution
- **Key Decisions**: Interface contracts, sequencing, dependency management
- **Core Artifacts**: Integration plans, interface catalogs, dependency maps
- **Collaboration**: Solution Architect, Customer Technical teams, Dev/QA
- **Governance**: Integration readiness, cutover rehearsals

### Technical Lead / Engineering Manager
- **Accountability**: Technical execution, code quality, engineering practices
- **Key Decisions**: Implementation approach, refactor vs build-new, design trade-offs
- **Core Artifacts**: Technical designs, review checklists, code quality metrics
- **Collaboration**: Developers, QA, Architects
- **Governance**: Engineering reviews, quality gates

### QA Lead / Test Strategy Lead
- **Accountability**: Test strategy, quality gates, leakage prevention
- **Key Decisions**: Coverage focus, automation boundaries, release readiness from QA
- **Core Artifacts**: Test strategy, test suites, quality dashboards (SLIs/SLOs)
- **Collaboration**: Customer QA Lead, Dev, Product, Ops
- **Governance**: Quality Council, release gates

### DevOps / Platform Engineer
- **Accountability**: CI/CD, environments, observability, operational readiness
- **Key Decisions**: Pipeline gates, deployment strategies, rollback plans
- **Core Artifacts**: Pipeline configs, runbooks, monitoring dashboards
- **Collaboration**: Tech Lead, QA, Operations, Security
- **Governance**: Release governance, operational reviews

### Commercial Manager (EO Org)
- **Accountability**: Commercial health, CR process, funding visibility, contract alignment; manages commercial risk posture for the engagement
- **Key Decisions**: CR bundling, threshold approvals, re-baselining proposals, commercial escalation triggers
- **Core Artifacts**: Commercial health dashboard, CR register, funding visibility score, variance summaries
- **Collaboration**: Engagement Owner (EO), Account Manager, Program Sponsor, Finance, Delivery Manager, Studio Owner
- **Org Placement**: Part of the Engagement Owner’s organization
- **Governance**: Commercial review, Steering inputs

### Governance Coordinator / Operations Lead
- **Accountability**: Rituals, dashboards, alerts, playbook upkeep
- **Key Decisions**: Cadence/agenda tuning, alert thresholds, audience mapping
- **Core Artifacts**: Operational playbook, dashboards, alert matrix
- **Collaboration**: All leads, Customer PMO
- **Governance**: Daily/weekly/monthly governance

### Account Manager (Business Development & GTM Org)
- **Accountability**: Owns the client commercial relationship; receives and resolves escalations from the Commercial Manager; leads SoW amendments and contracting for additional scope or deviations
- **Key Decisions**: Contract changes, pricing and terms proposals, escalation handling and resolution paths
- **Core Artifacts**: SoWs, contract amendments, commercial correspondence, negotiation records
- **Collaboration**: Engagement Owner, Commercial Manager, Program Sponsor/Customer Procurement, Legal, Delivery Manager
- **Org Placement**: Part of the Business Development & GTM organization
- **Governance**: Commercial review, Steering (as needed), contract governance forums

### Studio Owner
- **Accountability**: Heads the Studio organization delivering the program; accountable to the Engagement Owner to deliver the project; owns delivery operations across roles, rituals, resourcing, and performance; manages the cost center and ensures budget deviations are tracked and reported to the Engagement Owner via the Delivery Manager
- **Key Decisions**: Studio resourcing, operating cadence, performance management, cross-engagement standards, risk posture, budget adherence actions
- **Core Artifacts**: Studio operating handbook, capacity plan, performance dashboards, resourcing roster, variance reports
- **Collaboration**: Engagement Owner (VP Delivery), Delivery Manager (Engagement Program Head), Product/Tech/QA leads, Commercial Manager, Finance
- **Governance**: Studio operating reviews, monthly operational review, financial variance reviews; Steering inputs via Delivery Manager

### Developers / Engineers
- **Accountability**: Build features with quality and traceability
- **Key Decisions**: Implementation details within design guardrails
- **Core Artifacts**: Code, tests, design notes, change logs
- **Collaboration**: Tech Lead, QA, Product, DevOps
- **Governance**: Code reviews, quality gates

### Release Manager (optional role or shared)
- **Accountability**: Release coordination, cutover, communications
- **Key Decisions**: Go/No-Go packaging, rollback readiness
- **Core Artifacts**: Release plans, cutover runbooks, comms
- **Collaboration**: Delivery Manager, QA, DevOps, Customer PM
- **Governance**: Release readiness reviews, CAB/CCB

---

## Two-in-a-Box Model: Customer PO × Delivery PO
- **Purpose**: Pair business ownership with delivery/technical feasibility to evolve product strategy without surprises.
- **Working Agreement**:
  - Joint backlog ownership; one voice to the teams
  - Weekly roadmap sync; shared definition of value and feasibility
  - Co-authored acceptance criteria; Delivery PO ensures testable, feasible slices
  - Shared representation in Steering for scope/benefit trade-offs
  - Customer Product Managers lead translation of requirements into features; Delivery Product Managers support by decomposing into epics/stories and ensuring definition-of-ready
- **Anti-Patterns to Avoid**:
  - Competing backlogs; contradictory priorities
  - Skipping feasibility checks before commitments
  - Diffuse acceptance authority causing late churn

---

## Governance Forums and Typical Participants
- **Steering Committee (EO-owned; Chair: Engagement Owner)**: Executive Sponsor, Program Sponsor, VP Delivery, Delivery Manager, Customer PO/Delivery PO, Commercial Manager, Account Manager (as needed), Architects (as needed)
- **Change Control Board — CCB (Studio-owned; Chair: Delivery Manager)**: Delivery Manager, Customer PM/PMO, Product Owners, Commercial Manager, Account Manager (as needed), QA Lead, Architect(s)
- **Quality Council (Studio-owned; Chair: QA Lead)**: QA Leads (Customer & Delivery), Test Engineers, Product Owners, Tech Lead
- **Architecture Roundtable (Studio-owned; Chair: Delivery PO/Technical Architect)**: Delivery PO (as solution architect), Customer Enterprise Architect, Integration Lead, Tech Lead
- **Operational Review — Monthly (Studio-owned; Chair: Delivery Manager)**: Delivery Manager, Governance Coordinator, Product/Tech/QA leads, Commercial Manager; outputs feed Steering

---

## Escalation Paths

Escalate within 24–48 hours of threshold breach. Always include evidence (dashboards, ledgers, CR register) and a proposed decision.

### Operational Delivery Issues (schedule, scope, dependencies)
- Tier 1: Team Lead → Delivery Product Manager
- Tier 2: Delivery Product Manager → Delivery Manager (daily/weekly rituals)
- Tier 3: Delivery Manager → Studio Owner (monthly operational review or ad hoc)
- Tier 4: Studio Owner → Engagement Owner (Steering) when cross-org decisions or rebaseline are needed

Typical Triggers:
- Critical path slippage > 10% or milestone at risk in next sprint
- Unblocked dependency aging > 5 business days
- Capacity shortfall > 15% over two sprints

### Quality & Risk Issues (defect leakage, SLO breach)
- Tier 1: QA Engineer → QA Lead (Quality Council)
- Tier 2: QA Lead → Delivery Manager (gate decision) and Delivery PO (scope impact)
- Tier 3: Delivery Manager → Studio Owner (stabilization plan)  
- Tier 4: Studio Owner → Engagement Owner (Steering) if release criteria unmet or error budget exhausted

Typical Triggers:
- Error budget consumed or leakage rate exceeds threshold for release
- Automation coverage below agreed floor on critical paths
- Repeated gate failures across two consecutive sprints

### Commercial & Contractual Issues (budget variance, CR funding)
- Tier 1: Delivery Manager → Commercial Manager (variance, CR exposure)
- Tier 2: Commercial Manager → Account Manager (customer contracting) and Studio Owner (cost actions)
- Tier 3: Account Manager → Engagement Owner (deal posture) and Program Sponsor/Procurement (customer)
- Tier 4: Engagement Owner → Steering for rebaseline/approval

Typical Triggers:
- Unfunded CR exposure > 10% of current budget
- Forecast variance > 8% for two consecutive cycles
- Payment risk/events or contractual non-compliance detected

### Architecture & Integration Issues (design risk, external constraints)
- Tier 1: Developer/Integrator → Technical Architect / Delivery PO (architecture roundtable)
- Tier 2: Delivery PO → Delivery Manager (plan impact) and Customer Enterprise Architect (standards)
- Tier 3: Delivery Manager → Studio Owner (resource/sequence changes)
- Tier 4: Studio Owner → Engagement Owner (Steering) for exception approvals

Typical Triggers:
- NFR violations (performance, security, compliance) without feasible mitigation in-scope
- Third-party dependency changes blocking delivery > 5 business days

### Behavioral / Governance Breakdown (process bypass, decision deadlock)
- Tier 1: Role-to-role resolution (e.g., PO ↔ Tech Lead) using principles
- Tier 2: Delivery Manager facilitates neutral decision; document rationale
- Tier 3: Studio Owner adjudicates and sets temporary guardrail
- Tier 4: Engagement Owner escalates to Steering for binding decision

Documentation Requirements (for any escalation):
- Current status snapshot and variance vs baseline
- Options with impact (scope/time/cost/risk) and recommended choice
- Owner and time-bound next steps; requested decision and forum

---

## Studio Model and Role Relationships
- **Engagement Owner (VP Delivery Leadership)**: Owns the business relationship and overall delivery business; charters Studios and holds Studio Owners accountable; owns the engagement P&L.
- **Studio Owner**: Leads the Studio (delivery organization) executing the engagement; accountable to the Engagement Owner; ensures delivery operations are performant and staffed; manages the cost center; partners with the Delivery Manager for day-to-day execution; routes budget deviation reports through the Delivery Manager to the Engagement Owner.
- **Delivery Manager (Engagement Program Head)**: Runs the program within the Studio; primary interface to Customer PM/PMO; drives execution against plan; escalates via Studio Owner/Engagement Owner as needed.
- **Org Alignment**: Delivery Product Owners sit in the Engagement Owner’s org; Delivery Product Managers sit in the Studio Owner’s org.

### Studio Council Member (New)
- **Accountability**: Institutional learning and playbook evolution across engagements; ensures program retrospectives occur on cadence and that systemic improvements are tracked to closure; owns versioning of this manual and integrates learnings from across programs into published updates
- **Key Decisions**: What lessons become policy/threshold/template changes; prioritization of improvement items into governance forums (Operational Review, CCB, Steering); when to publish a new manual version and what changes are included
- **Core Artifacts**: Manual Change Register, improvement backlog, program retrospective notes, proposal papers for policy/threshold updates, manual release notes and version tags
- **Collaboration**: Delivery Manager, Delivery Product Owner, Governance Coordinator, QA/Tech/Integration Leads, EO Commercial
- **Org Placement**: Part of the Studio Owner’s organization; independent from any single program for objectivity
- **Governance**: Attends program retrospectives; owns the cadence (milestone‑based and/or 8–12 week periodic); curates updates to dashboards (Section 9.13), thresholds (Sections 5, 7, 9), and contract appendices (Section 8); maintains lifecycle tracking for each improvement (discovery → decision → implementation → adoption audit) and reports status/exceptions at Monthly Operational Review, with escalations to Steering as needed; publishes manual version updates with release notes after approvals

---

## Quick Mapping to Artifacts
- **Backlog & Roadmap**: Customer PO, Delivery PO, Delivery PM(s)
- **Requirements & Traceability**: Customer Product Managers, Delivery PM(s), QA Lead
- **Architecture & Integrations**: Delivery PO (as solution architect), Technical Architect (supporting), Integration Lead, Customer Technical Lead
- **Quality & Gates**: QA Lead(s), Tech Lead, Delivery Manager
- **Commercial Health**: Commercial Manager, Program Sponsor, Delivery Manager
- **Operations & Dashboards**: Governance Coordinator, Delivery Manager, Leads

---

## Organizations and Roles (At-a-Glance)

### Business Development & GTM Org
- Account Manager

### Engagement Owner Org
- VP Delivery Leadership (Engagement Owner)
- Delivery Product Owner(s)
- Commercial Manager

### Studio Org
- Studio Owner
- Delivery Manager (Engagement Program Head)
- Delivery Product Manager(s)
- Governance Coordinator / Operations Lead
- Technical Architect (Supporting Role)
- Technical Lead / Engineering Manager
- Integration Lead
- QA Lead / Test Strategy Lead
- DevOps / Platform Engineer
- Release Manager (optional or shared)
- Developers / Engineers
- Studio Council Member (New)

### Customer Org
- Executive Sponsor
- Program Sponsor (Business Owner)
- Customer Product Owner (CPO)
- Customer Product Manager(s)
- Customer Project Manager / PMO Representative
- Customer QA Lead
- Customer Technical Lead / Enterprise Architect
- Business Stakeholders / Subject Matter Experts
- End Users

---

## Governance Responsibilities by Organization
- **Studio Organization (Operational & Tactical Governance)**
  - Owns day-to-day operating rhythm: daily/weekly rituals, risk reviews, QA councils, metrics dashboards, alerts
  - Runs monthly operational reviews and prepares materials for executive forums
  - Maintains the operational playbook, debt/quality/commercial dashboards, and alert matrices

- **Engagement Owner Organization (Governance & Steering)**
  - Owns governance posture and the Steering forum (agenda, decisions, escalation paths)
  - Sets guardrails, approves rebaselining, and adjudicates cross-functional escalations
  - Oversees commercial governance with Commercial Manager and Account Manager


