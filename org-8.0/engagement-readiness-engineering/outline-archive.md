# Engagement Readiness Engineering

## 1. Function Overview

**Engagement Readiness Engineering** is the function within ERC responsible for building and operating the systems, tools, and applications that make the Engagement lifecycle efficient, reliable, and consistent.

This function is distinct from **Engagement Engineering** (the discipline of assembling customer-specific product instantiations). Engagement Readiness Engineering builds the infrastructure that enables Engagement Engineering to be practiced at scale — the tools, platforms, and automation that prepare teams and customers for successful Engagements.

### Positioning

- **Reports to:** ERC (Engagement Readiness Council) — ERC's charter expands to include tooling governance
- **Serves:** Internal teams (Sales, EPM, EA, AVA, ELs, etc.) AND customers (via self-service portal)
- **Philosophy:** Pragmatic hybrid — configure existing platforms where commoditized (Jira, Confluence, etc.), build custom where differentiated
- **AI posture:** Both assistive (drafting, suggestions, Q&A) and automative (routine execution) depending on task complexity

---

## 2. Objectives

### 2.1 Operational Efficiency

Reduce friction and cycle time at every lifecycle phase:
- Exploration qualification → Engagement initiation
- Scope confirmation → staffing readiness
- Build → certification → go-live
- Transfer → steady state

### 2.2 Consistency and Repeatability

Enforce standards without stifling adaptation:
- Templatized artifacts that encode best practices
- Guided workflows that prevent drift from the operating model
- Automated validation against Engagement definition and archetype requirements

### 2.3 Knowledge Leverage

Maximize reuse and learning capture:
- Proposals, architectures, and patterns searchable and reusable
- Case studies automatically extracted from completed Engagements
- Lessons learned flow back to archetypes and Product Line roadmaps

### 2.4 Visibility and Governance

Provide leadership with actionable insight:
- Portfolio-level view of Engagement pipeline and health
- Real-time P&L visibility per Engagement
- Governance compliance dashboards (gates, certifications, escalations)

### 2.5 Customer Experience

Enable customers as informed partners:
- Self-service access to Engagement status, artifacts, and decisions
- Collaboration on reviews, approvals, and change requests
- Transparent progress tracking from Initiate through Complete

---

## 3. Systems and Tools

### 3.1 Presales Engineering Toolkit

Tools that enable Exploration and qualification — the period before customer commitment.

| System | Description | AI Role |
|--------|-------------|---------|
| **Proposal Kit** | Templated proposal builder with reusable sections, pricing tables, and compliance checklists | Assistive — drafts sections from past proposals and customer context |
| **RFI/RFP Kit** | Response management system — question parsing, answer library, compliance matrix, review workflows | Automative — auto-matches answers from library; flags gaps |
| **PoC App Builders** | Low-code environment for rapid proof-of-concept assembly using Product Line components | Assistive — suggests component configurations based on customer requirements |
| **Presentation Builder** | Branded slide generation with product visuals, architecture diagrams, and customer-specific data | Automative — generates draft decks from proposal content and archetype |
| **Proposal Repository** | Searchable archive of all proposals with outcome data (won/lost, reasons, reuse potential) | Assistive — surfaces relevant past proposals during new proposal creation |
| **Demo & Recording Library** | Indexed repository of demos, presentations, and workshop recordings with transcripts | Assistive — finds relevant clips, answers questions about product capabilities |
| **Estimation Workbench** | Effort estimation tool with historical calibration, archetype-based templates, and confidence ranges | Assistive — suggests estimates based on similar Engagements; flags outliers |

### 3.2 Delivery Engineering Toolkit

Tools that support the Engagement lifecycle from Initiate through Complete.

| System | Description | AI Role |
|--------|-------------|---------|
| **BRD Author & Validator** | Business requirements documentation with traceability to scope, Product Line capabilities, and archetype gaps | Assistive — drafts from discovery notes; validates completeness against archetype |
| **Estimation & Planning Suite** | Delivery estimation integrated with staffing demand and Product Line capacity models | Assistive — suggests staffing profiles; flags capacity conflicts |
| **PI Planning Suite** | Program Increment planning with cross-squad dependency tracking, objective alignment, and risk visualization | Assistive — identifies dependency conflicts; suggests sequencing |
| **Customer Meeting Suite** | Meeting scheduling, agenda templating, notes capture, action tracking, and decision logging | Automative — generates agendas from backlog; transcribes and extracts actions |
| **Engagement Bootstrap Kit** | Kickoff workflow — auto-creates Git repos and SharePoint folders, charter generation, role assignment checklist, operating model confirmation, environment provisioning requests | Automative — provisions repos/SharePoint from templates; generates charter from Exploration artifacts; tracks completeness |
| **Governance Prep Suite** | Gate readiness dashboards, artifact checklist enforcement, sign-off workflows | Assistive — flags missing artifacts; drafts gate review summaries |
| **Steering Committee Prep** | Executive-level reporting templates, risk summaries, decision request formatting | Assistive — drafts deck from project data; highlights decisions needed |
| **People Assignment Tracker** | Staffing assignments, rotation schedules, skill matching, and capacity visualization | Automative — suggests assignments based on skill fit and availability |
| **Engagement P&L Dashboard** | Real-time financial visibility — actuals vs. budget, burn rate, forecast to complete | Automative — pulls data from time/expense systems; alerts on variance |

### 3.3 Knowledge & Reuse Platform

Systems that capture, curate, and disseminate Engagement learnings.

| System | Description | AI Role |
|--------|-------------|---------|
| **Engagement Case Study Generator** | Semi-automated case study creation from Engagement artifacts, metrics, and retrospectives | Assistive — drafts case study; highlights differentiators and outcomes |
| **Pattern Library** | Curated repository of reusable architecture patterns, integration recipes, and Studio Component templates | Assistive — recommends patterns based on customer context; answers pattern questions |
| **Retrospective Synthesizer** | Aggregates retrospective findings across Engagements; identifies systemic issues and improvement opportunities | Automative — extracts themes; routes improvement suggestions to PAC or Product Lines |
| **Archetype Maintenance** | Feedback loop from Engagements to archetype definitions; tracks archetype health and coverage | Assistive — suggests archetype updates based on gap analysis patterns |

### 3.4 Customer Portal

Self-service portal enabling customers to participate in and observe their Engagement.

| Capability | Description |
|------------|-------------|
| **Engagement Dashboard** | Real-time status of lifecycle phase, milestones, and health indicators |
| **Artifact Access** | Secure access to delivered artifacts, documentation, and verification records |
| **Approval Workflows** | Customer sign-offs on scope changes, UAT, and go-live readiness |
| **Change Requests** | Submit and track scope change requests with impact visibility |
| **Meeting & Decision Log** | Searchable history of meetings, decisions, and action items |
| **Training & Enablement Hub** | Access to training materials, recorded sessions, and self-paced learning |

### 3.5 AI-Native Architecture

All tooling follows an **AI-native design principle**: agents are first-class participants, not bolted-on features.

#### Customer-Facing: Engagement Concierge

The Customer Portal is paired with an **Engagement Concierge** — an AI agent that:

- Answers customer questions about their Engagement (status, artifacts, decisions, next steps)
- Accepts requests (scope changes, meeting scheduling, artifact access) and routes to appropriate workflows
- Provides proactive notifications and guidance based on lifecycle phase
- Learns from customer interactions to improve response quality

The Concierge operates under the same progressive model: initially assistive (answers questions, explains status), evolving to automative (accepts and processes routine requests) as reliability is proven.

#### Internal: Specialized Drafting Agents

Every drafting use case is supported by **skill-specific agents** fine-tuned for that domain:

| Agent | Domain | Skills |
|-------|--------|--------|
| **Proposal Agent** | Presales | Drafts proposals from templates, past wins, and customer context |
| **Architecture Agent** | Solution design | Generates solution architectures from requirements and archetypes |
| **BRD Agent** | Requirements | Drafts BRDs from discovery notes; validates completeness |
| **Estimation Agent** | Planning | Generates estimates from historical data; flags outliers |
| **Governance Agent** | Compliance | Prepares gate review materials; checks artifact completeness |
| **Retrospective Agent** | Knowledge capture | Synthesizes learnings; extracts patterns; drafts case studies |

Agents share a common knowledge layer (Proposal Repository, Pattern Library, Case Studies) and are governed by the same progressive enforcement model.

### 3.6 Knowledge Engineering

Knowledge capture is not optional overhead — it is a **first-class function** within Engagement Readiness Engineering.

#### Ownership

| Role | Responsibility |
|------|----------------|
| **Knowledge Engineer** | Owns the knowledge base system, taxonomy, quality standards, and curation workflows |
| **Domain Stewards** (rotating) | SMEs from Engagements who validate and enrich domain-specific content |

This is not the whole team — it is 1-2 dedicated people who own the *system*, with contributions coming from across the organization.

#### Lifecycle-Embedded Capture

Knowledge artifacts are **required at each phase transition**, not captured post-hoc:

| Phase Transition | Required Knowledge Artifact | Owner |
|------------------|----------------------------|-------|
| Exploration → Initiate | Exploration summary, qualification rationale | Exploration Lead |
| Discover → Build | Solution architecture, gap analysis, archetype decisions | EA |
| Build → Transfer | Variability documentation, inner source contributions | EA + ELs |
| Transfer → Complete | Retrospective, lessons learned, pattern candidates | EPM |
| Complete (exit) | Case study draft, reusable artifacts tagged | EPM + Knowledge Engineer |

#### Tooling Principles

| Principle | How It Works |
|-----------|--------------|
| **Capture at the source** | Knowledge is a byproduct of work — Meeting Suite transcribes and extracts decisions; BRD Author prompts "What's generalizable here?" |
| **AI-assisted drafting** | Agents propose knowledge artifacts from work products; humans review and approve |
| **Quality gates** | Completeness, reusability score, findability (tagging), freshness (periodic review) |
| **Contribution metrics** | Visible at individual, team, and portfolio levels |

#### Pattern Curator Agent

An AI agent that continuously:

- Scans new artifacts for pattern candidates
- Identifies duplicates and suggests consolidation
- Flags gaps ("No case studies for [archetype X] in 6 months")
- Proposes taxonomy updates based on emerging themes
- Answers questions by synthesizing across the knowledge base

### 3.7 Document Governance

All Engagement and Exploration documentation follows a **strict governance model** that separates customer-facing documents from internal working documents.

#### Core Principle

| Document Type | Location | Format | Examples |
|---------------|----------|--------|----------|
| **Shared BY customer** | SharePoint | Office (Word, Excel, PPT) | Customer requirements docs, RFPs, data files, contracts |
| **Shared WITH customer** | SharePoint | Office (Word, Excel, PPT) | Proposals, SOWs, status reports, presentations |
| **Internal working documents** | Git | Markdown | Requirements analysis, architecture decisions, planning docs, meeting notes |

#### Naming Convention

| Construct | Repo Names | Example |
|-----------|------------|---------|
| **Engagement** | `ENG-{CODE}-requirements`, `ENG-{CODE}-project` | `ENG-NXTORBIT-requirements`, `ENG-NXTORBIT-project` |
| **Exploration** | `EXP-{CODE}-exploration` | `EXP-NXTORBIT-exploration` |

#### Engagement Repos

Each Engagement gets **two Git repos**:

**1. `ENG-{CODE}-requirements`** — Requirements and change requests

```
├── README.md                    # Overview, links to SharePoint
├── customer-inputs/
│   └── README.md                # Index of customer docs (in SharePoint, linked by URL)
├── requirements/
│   ├── functional/
│   │   └── {feature-area}.md
│   ├── non-functional/
│   │   ├── performance.md
│   │   ├── security.md
│   │   └── ...
│   └── constraints.md
├── change-requests/
│   ├── README.md                # CR process, status summary
│   ├── CR-001-{title}.md
│   └── ...
├── gap-analysis/
│   ├── platform-gaps.md
│   ├── archetype-gaps.md
│   └── inner-source-candidates.md
├── decisions/
│   └── ADR-001-{title}.md       # Architecture Decision Records
└── traceability/
    └── requirements-matrix.md
```

**2. `ENG-{CODE}-project`** — Planning, PIs, updates (SAFe terminology)

```
├── README.md                    # Engagement overview, quick links
├── charter/
│   └── engagement-charter.md
├── operating-model/
│   ├── roles-raci.md
│   ├── governance.md
│   └── escalation.md
├── roadmap/
│   ├── program-roadmap.md
│   └── release-plan.md
├── staffing/
│   ├── team-composition.md
│   ├── rotation-schedule.md
│   └── skill-matrix.md
├── pi/
│   ├── PI-1/
│   │   ├── README.md            # PI summary, dates, theme
│   │   ├── pi-objectives.md     # Committed objectives (accepted scope)
│   │   ├── pi-backlog.md        # Features/stories planned
│   │   ├── program-board.md     # Dependencies, milestones
│   │   ├── pi-risks.md          # ROAM: Resolved, Owned, Accepted, Mitigated
│   │   ├── confidence-vote.md   # Team confidence scores
│   │   ├── staffing.md          # PI-specific staffing
│   │   ├── decisions/
│   │   │   └── {decision}.md
│   │   ├── iterations/
│   │   │   ├── iteration-1.md
│   │   │   └── ...
│   │   └── pi-retrospective.md
│   └── PI-2/
│       └── ...
├── updates/
│   ├── README.md
│   ├── weekly/
│   │   └── {date}-update.md
│   └── steering-committee/
│       └── {date}-update.md
├── meetings/
│   ├── pi-planning/
│   ├── sync-meetings/
│   └── steering-committee/
├── risks/
│   └── risk-register.md
├── retrospectives/
│   └── engagement-retro.md
└── handover/
    ├── knowledge-transfer.md
    └── runbooks/
```

#### Exploration Repo

Each Exploration gets **one Git repo**: `EXP-{CODE}-exploration`

```
├── README.md                        # Overview, qualification status, key dates
├── customer-context/
│   └── README.md                    # Index of customer docs (SharePoint URLs)
│
├── rfi-rfp/                         # RFI/RFP response work
│   ├── README.md                    # RFI/RFP summary, deadlines, status
│   ├── original/
│   │   └── README.md                # Links to original RFI/RFP in SharePoint
│   ├── questions/
│   │   ├── questions-parsed.md      # Extracted questions from RFI/RFP
│   │   └── question-assignments.md  # Who owns which questions
│   ├── responses/
│   │   ├── section-{n}.md           # Draft responses by section
│   │   └── ...
│   ├── compliance-matrix.md         # Requirement-to-response mapping
│   ├── assumptions.md               # Assumptions and clarifications
│   └── review-notes.md              # Internal review feedback
│
├── discovery/
│   ├── stakeholder-map.md
│   ├── pain-points.md
│   ├── requirements-sketch.md
│   └── meeting-notes/
│       └── {date}-{topic}.md
│
├── solution/
│   ├── preliminary-architecture.md
│   ├── archetype-fit.md
│   ├── gap-assessment.md
│   └── poc/
│       ├── poc-plan.md
│       ├── poc-scope.md
│       └── poc-results.md
│
├── commercial/
│   ├── estimation.md
│   ├── pricing-model.md
│   ├── risk-assessment.md
│   └── assumptions.md               # Commercial assumptions
│
├── qualification/
│   ├── qualification-checklist.md
│   ├── go-no-go-decision.md
│   └── lessons-learned.md           # Capture learnings even if no-go
│
└── proposal/
    ├── proposal-outline.md          # Structure and ownership
    ├── proposal-draft.md            # Working draft (final → SharePoint)
    ├── executive-summary.md
    ├── technical-approach.md
    ├── team-structure.md
    ├── timeline.md
    └── review-feedback.md           # Internal review notes
```

#### SharePoint Structure

Each Customer gets a SharePoint site with folders per Exploration/Engagement:

```
{Customer Name}/
├── EXP-{CODE}/
│   ├── Customer-Provided/
│   ├── Proposals/
│   └── Contracts/
└── ENG-{CODE}/
    ├── Customer-Provided/
    │   ├── Requirements/
    │   ├── Data/
    │   └── Approvals/
    ├── Deliverables/
    │   ├── Status-Reports/
    │   ├── Presentations/
    │   └── Documentation/
    └── Contracts/
```

#### Governance Rules

| Rule | Policy |
|------|--------|
| **Auto-provisioning** | Engagement Bootstrap Kit creates repos + SharePoint folders from templates |
| **Cross-references** | Git docs reference SharePoint via URLs |
| **Archival** | Repos become **read-only** on Engagement completion |
| **Access control** | Exploration repos: access per Exploration team; Engagement repos: role-based access |

#### PI Artifacts (SAFe)

| Artifact | SAFe Concept | Content |
|----------|--------------|---------|
| `pi-objectives.md` | PI Objectives | Committed business and technical objectives; SMART format |
| `pi-backlog.md` | Program Backlog (PI slice) | Features, enablers, stories planned |
| `program-board.md` | Program Board | Delivery timeline, dependencies, milestones |
| `pi-risks.md` | ROAM Board | Risks: Resolved, Owned, Accepted, Mitigated |
| `confidence-vote.md` | Confidence Vote | Squad-by-squad confidence (1-5) |
| `iterations/` | Iteration Plans | Per-sprint stories, capacity, goals |
| `pi-retrospective.md` | Inspect & Adapt | What worked, what didn't, improvements |

### 3.8 Content Bridge

Tools that bridge the **Git (Markdown)** and **Office (SharePoint)** ecosystems, enabling seamless flow of content while maintaining the governance model.

#### Git → Office (Export & Templating)

| Tool | Function | AI Role |
|------|----------|---------|
| **Template Renderer** | Converts markdown to branded Office documents (Word, PPT, Excel) using standardized professional templates | Automative — renders on demand or batch |
| **Proposal Exporter** | Generates final proposal documents from `proposal/` folder | Assistive — suggests formatting, flags incomplete sections |
| **Status Report Generator** | Creates steering committee decks from `updates/` and PI data | Automative — pulls data, generates deck |
| **Batch Exporter** | Exports multiple docs for gate reviews or customer handoffs | Automative — packages all required artifacts |

**Template Library:** Standardized, professionally designed templates for:
- Proposals and SOWs
- Status reports and steering committee decks
- Requirements documents
- Architecture documents
- Handover packages

#### Office/PDF → Git (Import & Extraction)

| Tool | Function | AI Role |
|------|----------|---------|
| **RFI/RFP Parser** | Extracts questions from RFP documents (Word/PDF) into structured markdown in `rfi-rfp/questions/` | Automative — parses and structures; flags ambiguities |
| **Requirements Extractor** | Parses customer requirements docs into structured format in `requirements/` | Assistive — proposes structure; human validates |
| **Contract Analyzer** | Extracts key terms, SLAs, obligations, milestones from contracts | Assistive — highlights key clauses; human reviews |
| **PDF → Markdown** | General-purpose extraction for reference documents | Automative — best-effort conversion |

#### Teams Integration

| Tool | Function | AI Role |
|------|----------|---------|
| **Transcript Processor** | Extracts decisions, action items, key points from Teams meeting transcripts | Automative — extracts; routes to `meetings/` folder |
| **Recording Summarizer** | AI-generated summary of meeting recordings | Assistive — generates summary; human approves |
| **Auto-file to Repo** | Routes meeting notes to correct folder based on meeting type and participants | Automative — files based on calendar metadata |
| **Speaker Attribution** | Identifies who said what; maps to stakeholder roles | Assistive — proposes attribution; human confirms |

#### Outlook Plugin

| Capability | Function | AI Role |
|------------|----------|---------|
| **Engagement Tagger** | Tag/categorize emails to specific Exploration or Engagement (`EXP-NXTORBIT`, `ENG-NXTORBIT`) | Assistive — suggests tag based on participants, subject; user confirms |
| **Export to SharePoint** | One-click export of email + attachments to Engagement SharePoint folder | Automative — exports to correct folder |
| **SharePoint → Git Trigger** | Triggers extraction pipeline when new customer doc arrives in SharePoint | Automative — notifies relevant parser |
| **Thread Summarizer** | AI summary of email thread; option to create meeting note or decision record | Assistive — proposes summary; user edits and saves |
| **Action Extractor** | Identifies commitments/action items in emails; prompts to create tasks | Assistive — highlights actions; user confirms |

#### Integration with Existing Tools

| Existing Tool | Content Bridge Enhancement |
|---------------|---------------------------|
| **RFI/RFP Kit** | Uses RFI/RFP Parser for intake; Template Renderer for final response |
| **BRD Author** | Uses Requirements Extractor for customer docs; exports to Word for customer review |
| **Customer Meeting Suite** | Uses Transcript Processor and Recording Summarizer |
| **Governance Prep Suite** | Uses Batch Exporter for gate review packages |
| **Engagement Bootstrap Kit** | Configures Outlook Plugin with Engagement tags on creation |
| **Steering Committee Prep** | Uses Status Report Generator and Template Renderer |

### 3.9 Markdown Style Guide

Standardized conventions for writing project documentation in markdown. All ERE tools enforce and validate these conventions.

#### Status Indicators

| Indicator | Status | Use For |
|-----------|--------|---------|
| 🟢 **On Track** | Proceeding as planned | Milestones, objectives, deliverables |
| 🟡 **At Risk** | May miss target without intervention | Milestones, objectives, deliverables |
| 🔴 **Blocked** | Cannot proceed; requires escalation | Milestones, objectives, deliverables |
| ⏸️ **On Hold** | Deliberately paused | Milestones, work items |
| ✅ **Complete** | Done | Tasks, milestones, deliverables |
| ❌ **Cancelled** | Will not be done | Tasks, milestones |

#### ROAM Risk Status (SAFe)

| Indicator | Status | Definition |
|-----------|--------|------------|
| ✅ `[R]` | **Resolved** | Risk eliminated; root cause addressed |
| 🔶 `[O]` | **Owned** | Owner assigned; mitigation in progress |
| 🤝 `[A]` | **Accepted** | Conscious decision to accept; no action planned |
| 🛡️ `[M]` | **Mitigated** | Actions taken; residual risk reduced |

**Transition rules:**
- New risks start as 🔶 `[O]` — every risk needs an owner
- 🔶 `[O]` → 🛡️ `[M]` when mitigation actions complete
- 🔶 `[O]` → ✅ `[R]` when risk is eliminated
- 🔶 `[O]` → 🤝 `[A]` when team decides to accept (requires documented rationale)
- 🤝 `[A]` risks reviewed each PI — still valid to accept?

#### Priority / Severity

| Indicator | Level | Meaning |
|-----------|-------|---------|
| 🔥 **P0** | Critical | Immediate action required |
| 🔶 **P1** | High | Address this PI |
| 🔷 **P2** | Medium | Address next PI |
| ⬜ **P3** | Low | Backlog |

#### Task Lists

```markdown
- [x] Completed task
- [ ] Pending task
- [ ] ~Cancelled task~ (strikethrough)
```

#### Callouts (GitHub-supported)

```markdown
> [!NOTE]
> Useful information the reader should know.

> [!TIP]
> Helpful advice for better outcomes.

> [!IMPORTANT]
> Key information the reader must not miss.

> [!WARNING]
> Potential issue that needs attention.

> [!CAUTION]
> Risk of negative consequences.
```

#### Requirements Language (RFC 2119)

| Keyword | Meaning |
|---------|---------|
| **MUST** / **REQUIRED** | Absolute requirement |
| **MUST NOT** | Absolute prohibition |
| **SHOULD** / **RECOMMENDED** | Strong preference; valid exceptions exist |
| **SHOULD NOT** | Strong preference against |
| **MAY** / **OPTIONAL** | Truly optional |

#### Cross-References

```markdown
Internal links:
- See [CR-001](../change-requests/CR-001-title.md)
- Relates to [ADR-003](../decisions/ADR-003-title.md)
- Per [PI-2 Objectives](../pi/PI-2/pi-objectives.md)

External links (SharePoint):
- Customer requirements: [Link](https://sharepoint.com/sites/...)
- Original RFP: [Link](https://sharepoint.com/sites/...)
```

#### Tables

Use tables for structured data. Align columns for readability:

```markdown
| ID | Item | Status | Owner | Due |
|----|------|--------|-------|-----|
| 001 | Requirements review | 🟢 On Track | @jane | 2024-03-15 |
| 002 | Architecture sign-off | 🟡 At Risk | @bob | 2024-03-20 |
```

#### Dates

Use ISO 8601 format: `YYYY-MM-DD` (e.g., `2024-03-15`)

#### File Naming

- Lowercase with hyphens: `pi-objectives.md`, `CR-001-api-change.md`
- Prefix with number for ordering: `01-introduction.md`, `02-scope.md`
- Include identifier in name: `ADR-003-database-choice.md`

---

## 4. Governance Enforcement

The function enforces governance through a **progressive model**: tools initially guide and assist, with mandatory gates introduced as adoption matures and tooling proves reliable.

### 4.1 Progressive Enforcement Model

| Stage | Behavior | Example |
|-------|----------|---------|
| **Guidance** | Tools suggest; compliance is optional | Estimation Workbench suggests staffing; EPM can override |
| **Assistance** | Tools actively help; non-compliance is flagged | BRD Validator flags incomplete sections; Engagement can proceed with documented exceptions |
| **Mandatory Gate** | Tools enforce; Engagement cannot proceed without compliance | AVA certification must pass in Governance Prep Suite before go-live |

This model applies uniformly to:
- **Delivery gates** — lifecycle phase transitions
- **Knowledge capture gates** — required artifacts at each transition
- **AI agent autonomy** — agents progress from assistive to automative based on proven reliability

### 4.2 Gates and Checkpoints

Tools will enforce (progressively) the following governance moments:

| Lifecycle Phase | Delivery Gate | Knowledge Gate | Enforced By |
|-----------------|---------------|----------------|-------------|
| Exploration → Initiate | Qualification criteria met; Exploration artifacts complete | Exploration summary and qualification rationale captured | Proposal Repository + Estimation Workbench |
| Initiate | Charter signed; roles assigned; operating model confirmed | — | Engagement Bootstrap Kit |
| Discover | Solution architecture reviewed; staffing committed; test strategy agreed | Architecture decisions documented; gap analysis captured | BRD Validator + People Assignment Tracker |
| Build | Increment certification; go-live criteria met | Variability documentation complete; inner source PRs submitted with learning notes | Governance Prep Suite + AVA integration |
| Transfer | Handover checklist complete; verification module delivered | Retrospective captured; lessons learned documented | Governance Prep Suite + Customer Portal |
| Complete | Stabilization criteria met; inner source complete | Case study draft submitted; reusable patterns tagged | Retrospective Synthesizer + Case Study Generator |

**Knowledge gates follow the same progressive model:** initially flagged (Assistance), evolving to blocking (Mandatory Gate) as tooling matures.

### 4.3 AI Agent Governance

AI agents operate under explicit governance controls:

| Control | Description |
|---------|-------------|
| **Autonomy levels** | Each agent has a defined autonomy level (Assistive, Automative) that determines what actions require human approval |
| **Escalation triggers** | Agents escalate to humans when confidence is low, request is out-of-scope, or stakes are high (e.g., customer-facing commitments) |
| **Audit trail** | All agent actions are logged with context, decision rationale, and outcome |
| **Feedback loop** | Human corrections feed back into agent training; systematic errors trigger autonomy review |
| **Periodic review** | ERC reviews agent performance quarterly; autonomy levels adjusted based on accuracy and adoption metrics |

#### Agent Autonomy Progression

| Agent | Initial State | Progression Criteria | Target State |
|-------|---------------|---------------------|--------------|
| **Engagement Concierge** | Answers questions; routes requests to humans | 90%+ accuracy on Q&A; <5% escalation rate on routine requests | Processes routine requests autonomously |
| **Proposal Agent** | Drafts sections for human review | 80%+ acceptance rate on drafts; positive user feedback | Generates complete first drafts |
| **Governance Agent** | Flags missing artifacts | 95%+ accuracy on completeness checks | Auto-generates gate review summaries |

### 4.4 Knowledge Contribution Governance

Knowledge capture is governed with the same rigor as delivery:

| Metric | What It Measures | Target | Visibility |
|--------|------------------|--------|------------|
| **Contribution rate** | # of knowledge artifacts contributed per Engagement | 100% of phase transitions have required artifacts | EPM dashboard, ERC portfolio view |
| **Reuse rate** | # of times contributed artifacts are reused in other Engagements | Increasing trend | Individual recognition, team metrics |
| **Coverage** | % of archetypes/domains with adequate knowledge artifacts | >80% coverage | Knowledge Engineer dashboard |
| **Quality score** | Average quality rating (completeness, reusability, findability) | >4.0/5.0 | Contributor profiles |
| **Freshness** | % of knowledge artifacts reviewed within policy period | >90% current | Knowledge Engineer dashboard |

**Accountability:**
- **EPM** is accountable for knowledge capture within their Engagement (contribution rate)
- **Knowledge Engineer** is accountable for knowledge base health (coverage, quality, freshness)
- **ERC** reviews aggregate knowledge metrics quarterly

### 4.5 Compliance Dashboards

ERC gains visibility into governance health through:

**Delivery Compliance:**
- **Gate pass rate** — percentage of Engagements passing gates without exception
- **Exception frequency** — volume and reasons for documented exceptions
- **Time at gates** — cycle time blocked at each gate (identifies friction points)
- **Tool adoption** — usage metrics by tool, role, and Engagement

**Knowledge Compliance:**
- **Capture completion** — % of required knowledge artifacts captured at each gate
- **Contribution leaderboard** — individuals and teams ranked by contribution rate and reuse
- **Gap alerts** — domains or archetypes with insufficient coverage

**AI Agent Compliance:**
- **Agent accuracy** — % of agent outputs accepted without modification
- **Escalation rate** — % of requests escalated to humans
- **Autonomy utilization** — % of automative capacity actually used

---

## 5. Team Structure and Evolution

### 5.1 Initial State: Dedicated Squad(s)

The function starts with dedicated product and engineering capacity:

| Role | Responsibility |
|------|----------------|
| **Product Manager** | Roadmap, prioritization, stakeholder alignment |
| **Engineering Lead** | Technical direction, architecture, delivery |
| **Engineers** | Build and maintain systems |
| **Designer** | UX for internal tools and customer portal |
| **Knowledge Engineer** | Knowledge base system, taxonomy, quality standards, curation workflows |
| **AI/ML Engineer** | Agent development, fine-tuning, performance monitoring |

Squad(s) report into ERC leadership and operate as an internal product team with clear OKRs.

### 5.2 Mature State: Rotating Contributors

As tooling matures and patterns stabilize:

- **Core team** maintains platform, high-complexity components, and AI agents
- **Knowledge Engineer** + **Domain Stewards** (rotating SMEs) maintain knowledge base
- **Engineers rotating from Engagements** contribute:
  - Bug fixes and incremental improvements
  - New templates and patterns from their Engagement experience
  - Feedback-driven enhancements
  - Knowledge artifacts (case studies, pattern candidates)
- Contribution model mirrors inner source: structured PRs, reviews by core team

### 5.3 Capacity Allocation

| Activity | % of Engagement Capacity | Accountability |
|----------|--------------------------|----------------|
| **Knowledge capture** | 5-10% | EPM ensures time is budgeted; ERC reviews aggregate |
| **Tool feedback/contribution** | Included in inner source budget | ELs track; reported to ERC |

This is visible in staffing plans — not hidden overhead.

### 5.4 Success Metrics

| Category | Metric | What It Measures |
|----------|--------|------------------|
| **Efficiency** | Cycle time reduction | Improvement in phase durations (Exploration → Initiate, Build → Go-live) |
| **Reuse** | Reuse ratio | % of proposals/architectures derived from existing artifacts |
| **Compliance** | Gate pass rate | Engagements passing gates (delivery + knowledge) on first attempt |
| **Adoption** | Tool adoption | Active usage by tool, role, and phase |
| **Customer** | Portal NPS | Customer satisfaction with self-service portal |
| **Customer** | Concierge resolution rate | % of customer queries resolved by Engagement Concierge without escalation |
| **Knowledge** | Capture completion | % of required knowledge artifacts captured at each gate |
| **Knowledge** | Reuse rate | # of times contributed artifacts are reused |
| **Knowledge** | Coverage | % of archetypes/domains with adequate knowledge artifacts |
| **AI** | Agent accuracy | % of agent outputs accepted without modification |
| **AI** | Autonomy progression | # of agents advanced from Assistive to Automative |

---

## 6. Roadmap Sketch (Not a Timeline)

### Phase 1: Foundation

**Tools:**
- Proposal Kit and RFP Kit (Presales)
- Engagement Bootstrap Kit and People Assignment Tracker (Delivery)
- Basic Customer Portal (status visibility)

**AI:**
- Proposal Agent (Assistive) — drafts proposal sections
- Basic Q&A capability in Customer Portal

**Knowledge:**
- Knowledge base infrastructure (taxonomy, storage, search)
- Manual capture workflows at phase transitions

### Phase 2: Workflow Automation

**Tools:**
- PI Planning Suite and Customer Meeting Suite
- Governance Prep Suite (guidance mode)
- Estimation Workbench with historical calibration

**AI:**
- BRD Agent and Estimation Agent (Assistive)
- Meeting Suite auto-transcription and action extraction
- Engagement Concierge (Assistive) — answers customer questions

**Knowledge:**
- Capture at the source — templates prompt for reusable insights
- Quality gates (completeness, tagging)

### Phase 3: Knowledge Leverage

**Tools:**
- Pattern Library and Case Study Generator
- Retrospective Synthesizer
- Archetype Maintenance loop

**AI:**
- Pattern Curator Agent — scans for patterns, flags gaps
- Retrospective Agent — synthesizes learnings
- Governance Agent (Assistive) — flags missing artifacts

**Knowledge:**
- Knowledge gates at phase transitions (Assistance mode)
- Contribution metrics visible to individuals and teams

### Phase 4: Full Enforcement

**Tools:**
- Governance Prep Suite (mandatory gate mode)
- Full Customer Portal (self-service)
- Compliance dashboards for ERC

**AI:**
- Engagement Concierge (Automative) — processes routine requests
- Governance Agent (Automative) — auto-generates gate summaries
- Agent autonomy governance in place

**Knowledge:**
- Knowledge gates mandatory
- Domain Steward rotation program operational
- Coverage targets enforced

---

## 7. Open Questions

### Integration & Data
- **Integration points:** Which existing systems (Jira, Confluence, Salesforce, ERP) must these tools integrate with? What's the integration strategy?
- **Data model:** Is there a unified Engagement data model across tools, or will each tool own its data?
- **Knowledge base platform:** Build custom or configure existing (Confluence, Notion, custom wiki)?

### Security & Access
- **Customer portal isolation:** Per-Engagement isolation, role-based access within Engagement, audit logging requirements?
- **AI agent data access:** What data can agents access? How is sensitive information protected?

### Adoption & Migration
- **Migration:** How do existing Engagements onboard to these tools? Grandfather clause or mandatory transition?
- **Training:** What enablement is required for each role to adopt the tools and work with AI agents?
- **Resistance:** How do we handle teams that prefer existing workflows?

### AI-Specific
- **Agent training data:** What data is used to fine-tune agents? How is data quality ensured?
- **Agent accountability:** When an agent makes an error with customer impact, who is accountable?
- **Autonomy escalation:** What is the process to advance an agent from Assistive to Automative?

### Knowledge-Specific
- **Incentives:** Beyond metrics, how do we incentivize knowledge contribution? Recognition programs? Career impact?
- **Curation burden:** How do we prevent the Knowledge Engineer from becoming a bottleneck?
- **Stale content:** What is the policy for archiving or retiring outdated knowledge?

---

## Appendix: Original Tool Inventory

*Preserved from initial brainstorm for reference.*

### Presales Engineering Toolkit

- Proposal Kit
- RFI and RFP Kit
- PoC App Builders
- Presentation Builders
- Proposal Repository
- Demo, Presentations, and Workshop recordings
- Estimation Helpers

### Engagement Case Studies

### Delivery Engineering

- BRD Authors and Validators
- Estimation
- PI Planning Suite
- Customer Meeting Management Suite
- Engagement Kick-off, Bootstrap Suite
- Governance Preparation Suite
- Steering Committee Preparation Suite
- People Assignment Tracking Suite
- Engagement P&L Visibility
