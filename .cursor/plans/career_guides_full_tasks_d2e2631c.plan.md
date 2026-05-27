---
name: Career Guides Full Tasks
overview: "Consolidated, actionable plan covering every deliverable in the career-guides folder: README, templates, 6 function coaching docs (each by seniority level), 11 role coaching docs, and integration with the main engagement guide. All grounded in the operating model with curated references."
todos:
  - id: scaffolding
    content: Create career-guides/README.md (with grounding policy, anti-platitude rules, curated reference policy), FUNCTION-TEMPLATE.md, and ROLE-TEMPLATE.md
    status: completed
  - id: func-engineering
    content: "Create functions/engineering.md — levels: Junior through Principal + EL/EM branch; craft, roles, challenges, how to learn per level; further reading"
    status: completed
  - id: func-architecture
    content: "Create functions/architecture.md — levels: Architect through Principal Architect + Arch Manager; architecture vs technical architecture; craft, roles, challenges per level; further reading"
    status: completed
  - id: func-product
    content: "Create functions/product-management.md — levels: Associate PM through Senior PM + Director/VP; craft, roles, challenges per level; further reading"
    status: completed
  - id: func-delivery
    content: "Create functions/program-delivery.md — levels: Coordinator through Senior PM + Director/VP; craft, roles, challenges per level; further reading"
    status: completed
  - id: func-sre
    content: "Create functions/sre-operations.md — levels: SRE through SRE Manager + Director/VP; craft, roles, challenges per level; further reading"
    status: completed
  - id: func-am
    content: Create functions/account-management.md — levels leading to Client Partner and CPA; craft, roles, challenges per level; further reading
    status: completed
  - id: role-client-partner
    content: Create roles/client-partner.md — success, interactions/tensions, escalation dos and donts, further learning
    status: completed
  - id: role-cpa
    content: Create roles/cpa.md — success, interactions/tensions, escalation dos and donts, further learning
    status: completed
  - id: role-eo
    content: Create roles/engagement-owner.md — success, interactions/tensions, escalation dos and donts, further learning
    status: completed
  - id: role-epm
    content: Create roles/epm.md — success, interactions/tensions, escalation dos and donts, further learning
    status: completed
  - id: role-ea
    content: Create roles/ea.md — success, interactions/tensions (incl architecture vs technical), escalation dos and donts, further learning
    status: completed
  - id: role-ava
    content: Create roles/ava.md — success, interactions/tensions (incl release-block), escalation dos and donts, further learning
    status: completed
  - id: role-epo
    content: Create roles/epo.md — success, interactions/tensions, escalation dos and donts, further learning
    status: completed
  - id: role-sre-lead
    content: Create roles/sre-lead.md — success, interactions/tensions, escalation dos and donts, further learning
    status: completed
  - id: role-el
    content: Create roles/engineering-lead.md — success, interactions/tensions, escalation dos and donts, further learning
    status: completed
  - id: role-squad-pm
    content: Create roles/squad-pm.md — success, interactions/tensions, escalation dos and donts, further learning
    status: completed
  - id: role-scrum-master
    content: Create roles/scrum-master.md — success, interactions/tensions, escalation dos and donts, further learning
    status: completed
  - id: integration
    content: Update engagement README.md and career-paths.md to link to career-guides
    status: completed
isProject: false
---

# Career Guides — Full Implementation Plan

## Location

`org-8.0/engagement/career-guides/` — engagement-scoped.

## Policy (embedded in README and templates)

All coaching docs must follow these rules (from the grounding and learning-refs addenda):

- **Grounded in the Engagement Operating Model:** Every section references concrete constructs (Engagement, lifecycle phases, formation stages, ERC, dual-axis, squad types, artifact groups, inner source, verification/certification, Client Partner → EO, etc.).
- **Grounded in business context:** Why this model exists (assembly not services, extend don't fork, platforms as accelerators, Engagement Success).
- **No platitudes:** Every piece of advice tied to a specific interaction, decision, artifact, or governance path; no standalone generic statements.
- **Learning / Further reading in both function and role docs:** Internal links (roles.md, career-paths.md, governance.md, formation, etc.) plus external references from the curated set only. Each external entry has a stable link and a one-line "why relevant to this model."

---

## Deliverables

### 1. Scaffolding

- **README.md** — Purpose, audience, link to career-paths and roles, policy/rules (grounding, anti-platitude, curated references), list of all function and role docs with one-line descriptions.
- **FUNCTION-TEMPLATE.md** — Template for function coaching: section structure for each seniority level (Required craft/skills/competencies; Roles to play and challenges; How to learn), plus Further reading section.
- **ROLE-TEMPLATE.md** — Template for role coaching: Success in the role (first 90 days, what good looks like, key relationships, performance input); Expected interactions, tensions, and how to navigate; Escalation dos and don'ts; Further learning.

### 2. Function Coaching Docs (functions/)

Each doc covers every level in the designation ladder from [career-paths.md](org-8.0/engagement/career-paths.md). For each level: (A) Required craft, skills, competencies (B) Roles expected to play and challenges to be ready for (C) How to learn. Ends with a Further reading section.

**2a. engineering.md**
Levels: Junior Engineer, Engineer, Senior Engineer, Staff Engineer (PE-1), Principal Engineer; management branch: EL, Engineering Manager, Sr. Engineering Manager.
Key model constructs: CP/Studio/Verification/PL squad contexts, one engineering ladder, rotation, inner source, EA mandatory review and DoD, no QA/SDET titles, EL delivery accountability under EPM.
References: PLE (Clements/Northrop), Inner source (Cooper/Stol; Oram; ISC Patterns), Team Topologies.

**2b. architecture.md**
Levels: Architect, Senior Architect, Principal Architect; management branch: Architecture Manager, Sr. Architecture Manager.
Key model constructs: Architecture vs technical architecture distinction, EA and AVA as roles played from this function, cross-track jumps into Architecture, archetype/variability, solution-level thinking (not just technical), EA-AVA co-design, certification, inner source prioritisation by EA, PAC.
References: Solution vs Software Architecture (DZone), Software Architecture in Practice (Bass), Just Enough Software Architecture (Fairbanks), Solution Architecture Foundations, Solution Architecture Patterns for Enterprise, TOGAF, Enterprise Integration Patterns, PLE (Pohl).

**2c. product-management.md**
Levels: Associate PM, Product Manager, Senior PM; leadership: Director of Product, Sr. Director, VP.
Key model constructs: EPO and Squad PM roles, customer discovery in platform context (gap between "what's in the box" and what customer needs), requirements as input to EA architecture and Squad PM backlog, Engagement Success (EPM owns, but EPO drives training/enablement), operating model choice impact on product scope.
References: Inspired (Cagan), Continuous Discovery Habits (Torres).

**2d. program-delivery.md**
Levels: Program Coordinator, Program Manager, Senior PM; leadership: Director of Delivery, Sr. Director, VP.
Key model constructs: EPM and Scrum Master roles, Engagement Success as EPM-owned function, multi-squad coordination, dual-axis feedback, staffing via PPM, scope change management, commercial alignment with AM, Stream DL scaling, Client Partner coordination.
References: Agile and Lean Program Management (Rothman), Nexus Framework (Bittner), Team Topologies, Practical Customer Success Management (Adams), Making the Matrix Work (Hall).

**2e. sre-operations.md**
Levels: SRE, Senior SRE, SRE Lead (designation), SRE Manager; leadership: Director of SRE, Sr. Director, VP.
Key model constructs: SRE Lead role, operational readiness from Discover through Transfer, release coordination (AVA certifies, SRE Lead deploys), runbooks, operating model handover (Fully Managed / Co-Managed / Customer-Operated), monitoring and alerting, incident response.
References: Site Reliability Engineering (Google, free), SRE Workbook (Google, free).

**2f. account-management.md**
Levels: (to be defined per org; guide covers the career progression leading to Client Partner and CPA roles).
Key model constructs: Client Partner as senior-most per-client role, CPA as generalist support, Client Partner → EO authority boundary, ERC assignment, per-client scope, commercial alignment, cross-Engagement coordination, governance preparation.
References: Handbook of Strategic Account Management (Wilson/Woodburn), The Trusted Advisor (Maister/Green/Galford), Practical Customer Success Management (Adams).

### 3. Role Coaching Docs (roles/)

Each doc covers: (1) Success in the role (2) Expected interactions, tensions, how to navigate (3) Escalation dos and don'ts (4) Further learning. All grounded in model constructs.

**3a. client-partner.md**
Key constructs: Senior-most per-client; EO reports to CP; authority boundary (client-facing vs internal delivery); ERC as escalation for CP ↔ EO; spans multiple Engagements; CPA support; governance with AM, EPM, EO.
Interactions/tensions: CP ↔ EO (delivery vs client expectations), CP ↔ EPM (who says what to client), CP ↔ AM (commercial vs relationship).
References: Trusted Advisor, Strategic Account Management.

**3b. cpa.md**
Key constructs: Generalist for Client Partner; governance prep, stakeholder coordination, commercial tracking, cross-Engagement alignment; from AM or Program/Delivery; natural progression toward Client Partner.
Interactions/tensions: CPA ↔ Client Partner (delegation and trust), CPA ↔ EPMs across Engagements (status consolidation), CPA ↔ ERC (reporting).
References: Strategic Account Management.

**3c. engagement-owner.md**
Key constructs: Per-Engagement; reports to Client Partner; assigned by ERC (heritage matching); retains full internal delivery authority; final escalation within Engagement; directs EPM/EA/AVA/EPO/SRE Lead; portfolio impact.
Interactions/tensions: EO ↔ Client Partner (delivery vs client), EO ↔ EPM (integrated view vs squad detail), EO ↔ EA/AVA (architecture vs delivery pressure), EO ↔ ERC (capacity, priority).
References: Making the Matrix Work, Agile and Lean Program Management.

**3d. epm.md**
Key constructs: Primary customer-facing contact; Engagement Success (readiness, adoption, value); integrated view; commercial alignment with AM; staffing via PPM; scope change; directs ELs and Scrum Masters; reports to EO.
Interactions/tensions: EPM ↔ EO (escalation, intervention), EPM ↔ Client Partner (customer-facing communication split), EPM ↔ ELs (squad commitments vs integrated view), EPM ↔ EA (inner source impact on timeline), EPM ↔ AM (commercial alignment).
References: Practical Customer Success Management (Adams), Agile and Lean Program Management (Rothman), Making the Matrix Work (Hall).

**3e. ea.md**
Key constructs: Architecture across entire span; archetype selection/adaptation; gap analysis (inner source vs custom); co-design with AVA (SUT boundary, verification); mandatory review in DoD; engineering quality standards; variability documentation; PAC; knowledge capture. Architecture vs technical architecture distinction.
Interactions/tensions: EA ↔ AVA (architecture vs verification scope), EA ↔ ELs (mandatory review vs squad autonomy), EA ↔ EPM (inner source timeline impact), EA ↔ PL Maintainers (contribution review).
References: Software Architecture in Practice, Just Enough Software Architecture, Solution Architecture Foundations, Solution vs Software Architecture (DZone), TOGAF, Enterprise Integration Patterns, PLE (Pohl), Inner source (Cooper/Stol).

**3f. ava.md**
Key constructs: Peer architect to EA; verification architecture; system-under-test boundary; certification; release-block authority (independent, cannot be overridden by Client Partner, EO, EPM, or EA); Verification Squad (no EL); verification module as deliverable; handover at Transfer. Architecture vs technical architecture distinction (verification architecture is architecture, not test management).
Interactions/tensions: AVA ↔ EA (co-design, verification criteria), AVA ↔ EPM (release block under commercial pressure), AVA ↔ ELs (assembly-impacting work review), AVA ↔ SRE Lead (release coordination: AVA certifies, SRE deploys).
References: Software Architecture in Practice, Just Enough Software Architecture, SRE Book (Google), Solution Architecture Foundations.

**3g. epo.md**
Key constructs: Customer discovery; requirements detailing; feeds Squad PMs; training/enablement at Transfer; works with EA on requirements-architecture translation; operating model impact on product scope.
Interactions/tensions: EPO ↔ EA (requirements vs architecture), EPO ↔ Squad PMs (requirements flow, prioritisation), EPO ↔ EPM (customer alignment), EPO ↔ Client Partner (customer access).
References: Inspired (Cagan), Continuous Discovery Habits (Torres).

**3h. sre-lead.md**
Key constructs: Operational readiness from Discover through Complete; release coordination (mechanics: deployment sequencing, environment promotion, production cutover; AVA holds release authority); runbooks, monitoring, alerting; operating model handover; incident response planning.
Interactions/tensions: SRE Lead ↔ AVA (AVA certifies, SRE deploys — authority vs mechanics), SRE Lead ↔ EA (architecture-operations alignment), SRE Lead ↔ EPM (operational readiness communication), SRE Lead ↔ ELs (squad operational requirements).
References: SRE Book (Google, free), SRE Workbook (Google, free).

**3i. engineering-lead.md**
Key constructs: Per-squad delivery accountability; meets EA quality standards and DoD (mandatory review); inner source planned into squad capacity; works with Scrum Master (process) and Squad PM (product); dual-axis reporting (EPM execution, Engineering functional); rotation from PL.
Interactions/tensions: EL ↔ EPM (commitments vs integrated view), EL ↔ EA (mandatory review, inner source bar), EL ↔ AVA (assembly-impacting work review), EL ↔ Squad PM (product vs delivery priority), EL ↔ Scrum Master (process vs squad autonomy).
References: Team Topologies, Inner source (Cooper/Stol; ISC Patterns), PLE (Clements/Northrop).

**3j. squad-pm.md**
Key constructs: Product role at squad level; backlog, prioritisation, requirements decomposition from EPO; not a process role (Scrum Master owns process); reports to EL within squad; functional-axis home is Product.
Interactions/tensions: Squad PM ↔ EPO (requirements flow), Squad PM ↔ EL (delivery alignment), Squad PM ↔ Scrum Master (product vs process), Squad PM ↔ EA (inner source and AVA verification requirements competing for backlog).
References: Inspired (Cagan), Continuous Discovery Habits (Torres).

**3k. scrum-master.md**
Key constructs: Process facilitation across 1-3 squads; reports to EPM (not EL); ceremonies, impediment removal, cadence, team health; Verification Squad has no Scrum Master; from Program/Delivery function.
Interactions/tensions: SM ↔ EL (process consistency vs squad flexibility), SM ↔ EPM (process expectations), SM ↔ Squad PM (process vs product decisions), SM across multiple squads with different ELs.
References: Nexus Framework (Bittner), Agile and Lean Program Management (Rothman).

### 4. Integration with main guide

- In [README.md](org-8.0/engagement/README.md): add career-guides to Guide Contents or Companion Documents.
- In [career-paths.md](org-8.0/engagement/career-paths.md): add a "See also" at the end pointing to career-guides for coaching by function and role.

