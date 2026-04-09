# Foundry Repository Architecture -- Unified Product Information Model

## Table of Contents

- [Introduction](#introduction)
- [Repository Landscape Overview](#repository-landscape-overview)
- [Product Intent Repository (PIR)](#product-intent-repository-pir)
- [Domain Knowledge Base (DKB)](#domain-knowledge-base-dkb)
- [Design & Architecture Repository (DAR)](#design--architecture-repository-dar)
- [Code Artifact Repository (CAR)](#code-artifact-repository-car)
- [Quality & Verification Store (QVS)](#quality--verification-store-qvs)
- [Operations Repository (OPR)](#operations-repository-opr)
- [Product Feedback Repository (PFR)](#product-feedback-repository-pfr)
- [Product Evolution & Impact Repository (PEIR)](#product-evolution--impact-repository-peir)
- [Product Practitioner Repository (PPR)](#product-practitioner-repository-ppr)
- [Product Ontology Repository (POR)](#product-ontology-repository-por)
- [Work Repository (WR)](#work-repository-wr)
- [Workforce Repository (WFR)](#workforce-repository-wfr)
- [External Stakeholder Registry (ESR)](#external-stakeholder-registry-esr)
- [End-to-End Information & Value Flow](#end-to-end-information--value-flow)


---

## Introduction

This guide defines the repository architecture for the Foundry -- the knowledge infrastructure that supports the Unified Product Information Model (UPIM). These 15 repositories (including PFR sub-partitions) are the collaborative foundation for both AI and human agents throughout the product lifecycle. Each section summarizes a repository's **intent**, **contents**, **best practices**, **information flow**, and UPIM mapping.

> **Terminology:** See DR-033 for the decisions behind repository naming, scope, and the introduction of OPR, ESR, and the PIR/WFR renames. See DR-034 for the Role vs. Agent separation that shapes WFR and ESR scope.

---

## Repository Landscape Overview

| Abbreviation | Full Name | Scope | UPIM Mapping |
|---|---|---|---|
| PIR | Product Intent Repository | Strategy, Business Model, Customer Value, Signals, Ideas, PSDs | Dim 1, 2, 3 |
| DKB | Domain Knowledge Base | Domain knowledge, glossaries, ontologies, business rules | Dim 9 |
| DAR | Design & Architecture Repository | Architecture, API models, infrastructure, operational specs | Dim 5, 6, 7 (definitions) |
| POR | Product Ontology Repository | Product structure, capabilities, features, maturity | Dim 8 |
| CAR | Code Artifact Repository | Source code, build artifacts | Track 2 + Track 3 engineering code |
| QVS | Quality & Verification Store | Test cases, acceptance tests, build-time quality evidence | Track 2 quality verification |
| OPR | Operations Repository | Deployment descriptors/records, incidents, PIR reports, operational artifact versions | Track 3 artifacts |
| PFR-Win | Product Feedback -- Win | FIRs (universal intake), Win Cases, customer communication records | Track 4 reactive inputs |
| PFR-Run | Product Feedback -- Run | Incident mirrors (references OPR), operational observation summaries | Track 3 feedback view |
| PFR-Build | Product Feedback -- Build | Bug report mirrors (references WR), technical debt observations | Track 2 feedback view |
| PPR | Product Practitioner Repository | Standards, templates, practices, verification policies | Operating Model + Track 5 |
| WR | Work Repository | All live work instances across all 5 tracks | Work Model instances |
| WFR | Workforce Repository | Internal agents (human + AI), role bindings, skills, availability, governance | Operating Model |
| ESR | External Stakeholder Registry | Customer/partner/prospect identity, contacts, communication preferences (reference layer) | Cross-cutting |
| PEIR | Product Evolution & Impact Repository | Lineage, impact graphs, historical metrics, cross-repo knowledge graph | Traceability |

---

## Product Intent Repository (PIR)

**UPIM Mapping:** Dimension 1 (Strategy & Intent), Dimension 2 (Vendor Value), Dimension 3 (Customer ROI)

**Intent:** The comprehensive ledger of strategic direction, business models, customer value propositions, signals, ideas, and product specifications.

**Contents (organized by PIR section):**

| PIR Section | UPIM Mapping | Content |
|---|---|---|
| **Strategy** | Dim 1 (Strategic entities) | Strategic Themes, Objectives, Initiatives, Customer Releases, Lever Mix definitions |
| **Business Model** | Dim 2 (Vendor Value) | Business Model, Pricing Tiers/Packages, Value Metrics, Lever Portfolio, Business KPIs, Cost KPIs, Win Outcomes, Win Barriers, Delivery Frictions, Win Stakeholder role definitions |
| **Customer Value** | Dim 3 (Customer ROI) | Customer Promises (Value Propositions, Service Commitments, Compliance Posture), Customer Value Metrics, Buying Personas, Business Outcomes, Customer Segments |
| **Signals & Ideas** | Dim 1 (flowing items) | Problems, Needs, Opportunities (routed from FIRs or created directly), Ideas (Hypotheses), PDRs |
| **Specifications** | Dim 1 (PSDs) | Product Specification Documents, PSD templates by module archetype |

**Purpose:** Central workspace for product intent, empowering agents to evaluate opportunities, model business value, and define customer promises.

> **Renamed from Product Idea Repository.** PIR's scope now encompasses strategy (Dim 1), vendor economics (Dim 2), and customer value (Dim 3). See DR-033 D1.

**Best Practices**
- **Do:**
  - Keep Signals lightweight until validated through Discovery
  - Track version history as standing definitions evolve
  - Use standing vs. flowing classification to manage content lifecycle
- **Don't:**
  - Include design/implementation details (DAR)
  - Store customer complaints or FIRs (PFR-Win)
  - Store deployment or operational artifacts (OPR)


---

## Domain Knowledge Base (DKB)

**UPIM Mapping:** Dimension 9 (Domain Knowledge)

**Intent:** Establish a shared, canonical understanding of the business and domain.

**Contents:**
- Glossaries, ontologies, taxonomies
- Business rules, models, event definitions
- Regulatory and policy frameworks
- Contextual and background knowledge

**Purpose:** Stabilizes semantic grounding for requirements and architecture.

**Best Practices**
- **Do:**
  - Keep definitions canonical and domain-wide
  - Use structured formats (e.g. ontologies)
- **Don't:**
  - Store product-specific requirements or implementation artifacts

---

## Design & Architecture Repository (DAR)

**UPIM Mapping:** Dimension 5 (Technical), Dimension 6 (Ecosystem & Extensibility), Dimension 7 (Operational) -- definitions only

**Intent:** Capture the structural and behavioral design blueprints.

**Contents:**
- Architecture diagrams (C4, layered, events, data flow)
- Sequence diagrams
- Component & API models (Dim 5 System/Component definitions, Dim 6 API Module/Operation/Contract definitions)
- Data/event models
- UX flow artifacts
- Architecture decision records (ADRs)
- Interface definitions
- Infrastructure models and operational specifications (Dim 7 Deployment Environment, Deployment Train, Module/Product Package specifications)

**Purpose:** Reference for Architect, Developer, API, and Verifier Agents. Holds the "what it is" definitions across Dim 5, 6, and 7.

**Best Practices**
- **Do:**
  - Align architecture with PIR and DKB
  - Record decisions in ADRs
- **Don't:**
  - Store code or test cases (CAR, QVS)
  - Store deployment records or runtime artifacts (OPR)

---

## Code Artifact Repository (CAR)

**UPIM Mapping:** Track 2 (Build Track) + Track 3 (Run Track) engineering code

**Intent:** Store the system's implementation artifacts -- source code and build-time artifacts only.

**Contents:**
- Source code (scaffolds, stubs)
- Developer test code (unit and module tests; excludes Product Acceptance Tests)
- Local code embeddings indices for this sub-repository (non-authoritative; for developer tooling)
- Build scripts, local configs
- Generated code artifacts
- Service mocks/stubs
- CI pipeline definitions for non-release builds (feature/dev branches)

> **Note:** CAR contains only build-time and development-time artifacts. All runtime concerns (deploy configs, SLOs, production rollout, deployment descriptors) are managed by OPR.
>
> **Note:** CAR hosts unit and module tests required for developer workflows. Product Acceptance Tests and release CI pipelines are governed by QVS. QVS defines coverage policies and gates that apply to CAR tests and consumes their coverage evidence.
>
> **Note:** CAR embeddings are intended for local code intelligence (IDE/agent tooling) within this sub-repository. PEIR owns the cross-repo knowledge graph, global embedding registry, and aggregated vector indices.

**Best Practices**
- **Do:**
  - Make code modular and traceable to design
  - Maintain semantic code embeddings for agent comprehension
- **Don't:**
  - Store deployment/runtime configs or deployment descriptors (OPR)
  - Store acceptance test artifacts or release pipeline definitions (QVS is source of truth for acceptance tests, verification policies, and release CI)
  - Store incident records or operational artifact versions (OPR)

---

## Quality & Verification Store (QVS)

**UPIM Mapping:** Track 2 quality verification (build-time evidence)

**Intent:** The authoritative source for build-time software correctness and compliance evidence.

**Contents:**
- Acceptance test code (automated Product Acceptance Tests)
- Test cases/test suites
- Auto-generated tests
- Test coverage reports
- Static analysis results
- Security/compliance scans
- Performance benchmarks
- Linting rules
- Review & audit logs
- Policy manifests pinned from PPR (verification policies, thresholds, gates)
- Release CI pipeline definitions (build, test, quality gates) consuming PPR policies

> **Note:** PPR is the source of truth for verification policy specifications and thresholds. QVS consumes and pins policy versions from PPR, executes gates in release CI, and stores evidence/results. Unit and module tests live in CAR for developer workflows; QVS enforces gates and consumes their coverage and results as evidence.

> **Verification evidence split:** QVS owns build-time quality evidence (tests, scans, benchmarks). OPR owns run-time quality evidence (deployment verification results, post-deployment SLA checks). See DR-033 D6.

**Best Practices**
- **Do:**
  - Align all tests to intent from PIR and design from DAR
  - Ensure verification logic is fully machine-readable
  - Define coverage thresholds and quality gates; enforce them in release CI pipelines
- **Don't:**
  - Store production telemetry/logs (OPR)
  - Store deployment verification evidence (OPR)

---

## Operations Repository (OPR)

**UPIM Mapping:** Track 3 (Run Track) artifacts

**Intent:** Store all Run Track artifacts -- deployment descriptors, deployment records, incidents (system of record), Post-Incident Reports, operational artifact versions, and deployment verification evidence.

**Contents:**
- Deployment descriptors (SDD/MDD/PDD versions)
- Deployment records (which descriptor applied, where, when, by whom, verification results)
- Incident records (system of record -- SEV-0 through SEV-4)
- Post-Incident Reports (timeline, RCA, corrective actions)
- Operational artifact versions (Module Package Versions, Product Package Versions)
- Deployment verification evidence (post-deployment SLA checks, verification results)
- Deployment runbooks and operational procedures

> **Separation from CAR.** CAR holds source code and build artifacts only. Deployment descriptors, incident records, and operational artifact versions have different ownership (SRE/DevOps vs. developers), lifecycle, and governance. See DR-033 D4.

> **Verification evidence split.** QVS owns build-time quality evidence (tests, scans); OPR owns run-time quality evidence (deployment verification). See DR-033 D6.

> **Incident system of record.** OPR owns the authoritative incident records. PFR-Run holds references/mirrors for the feedback perspective. See DR-033 D5.

**Best Practices**
- **Do:**
  - Maintain strict versioning on all deployment descriptors and operational artifacts
  - Link incident records to affected systems, modules, environments, and tenants
  - Record deployment verification results alongside deployment records
- **Don't:**
  - Store source code or build artifacts (CAR)
  - Store build-time test results or security scans (QVS)
  - Store customer-facing feedback or FIRs (PFR-Win)

---

## Product Feedback Repository (PFR)

**UPIM Mapping:** Track 4 (Win Track) reactive inputs, Track 3/Track 2 feedback views

**Intent:** Capture, categorize, and route real-world product-in-operation feedback. PFR is sub-partitioned by track affinity and team ownership.

### PFR-Win (Primary -- Universal Intake)

**Contents:**
- **FIRs (First Information Reports)** -- the primary entity; universal intake for all product-in-operation feedback (DR-032)
- Win Cases (Queries, Service Requests, Complaints, Escalations) -- always sub-items of FIRs
- Customer communication records
- NPS/CSAT data
- Qualitative customer input (chat/email transcripts)

**Owner:** Win Team (Customer Support, Customer Success)

### PFR-Run (Operational Feedback View)

**Contents:**
- Incident mirrors -- references to OPR Incidents (OPR is the system of record)
- Operational observation summaries
- Run-team-created FIR references (FIRs created by Run teams reside in PFR-Win; PFR-Run holds the feedback/customer-impact view)

**Owner:** SRE, DevOps (OPR owns the records; PFR-Run provides the feedback perspective)

### PFR-Build (Quality Feedback View)

**Contents:**
- Bug report mirrors -- references to WR/Track 2 Bugs (WR is the system of record)
- Technical debt observations
- Quality regression reports

**Owner:** QA, Engineering (WR owns the records; PFR-Build provides the feedback perspective)

> **PFR-Discovery removed.** Signals are routed directly from FIRs (via triage) into PIR. See DR-033 D5.

**Purpose:** Feed the quality-improvement loop -- detects pain points, drives updates to intents (PIR) and test plans (QVS/WR). PFR-Win is the comprehensive origination point for all operational feedback.

**Best Practices**
- **Do:**
  - Enforce FIR-first: every feedback event starts as an FIR in PFR-Win (DR-032)
  - Use consistent tagging/categorization for agent triage
  - Maintain references (not copies) for PFR-Run and PFR-Build mirrors
- **Don't:**
  - Store product intents or architecture change records (PIR, DAR)
  - Store deployment artifacts (OPR)
  - Duplicate incident or bug data -- PFR-Run and PFR-Build hold references only

---

## Product Evolution & Impact Repository (PEIR)

**UPIM Mapping:** Traceability (cross-cutting)

**Intent:** Ensure traceability, lineage, and change impact reasoning.

**Contents:**
- Knowledge graph (product, design, code, tests, issues)
- Change history (intent, architecture, code diffs)
- Release lineage
- Impact/downstream effect graphs
- Agent reasoning and decision logs
- Regression histories
- Negative learning ("regret logs")
- Global embedding registry (artifact URIs to vector metadata, provenance, model/version pins)
- Cross-repo vector indices and semantic graph projections (authoritative, queryable)
- Embeddings for all product-evolution artifacts across repositories (PIR, DKB, DAR, CAR, QVS, PPR, POR, PFR, WR, WFR, OPR, ESR, PEIR)

**Purpose:** Acts as time-aware, causal memory for agents -- enabling continuity and avoidance of regressions.

**Best Practices**
- **Do:**
  - Enforce strict versioning and artifact lineage
  - Maintain consistency of artifact relationships
  - Record immutable lineage snapshots and edges; corrections use "supersedes/corrects" relations
  - Ingest evidence as references (e.g., to QVS reports) rather than storing binaries
  - Compute durable historical metrics (cycle time, rework) from lineage
- **Don't:**
  - Store speculative/early ideas (should reside in PIR)
  - Store mutable operational state (WR is the source of truth for live state)

---

## Product Practitioner Repository (PPR)

**UPIM Mapping:** Operating Model + Track 5 (Evolve Track)

**Intent:** Curate reusable standards, templates, and professional practices.

**Contents:**
- Best practices/playbooks
- Prompt/UX/component templates
- Architecture templates
- Boilerplate code scaffolds
- Coding/testing/design standards
- Verification policy specifications and reusable policy templates (coverage thresholds, gate definitions, evidence contracts)
- Editorial/documentation conventions

**Purpose:** Houses reusable, domain-agnostic professional knowledge (practices), distinct from domain content in DKB.

**Best Practices**
- **Do:**
  - Keep artifacts general-purpose and reusable
- **Don't:**
  - Store product/domain-specific rules

---

## Product Ontology Repository (POR)

**UPIM Mapping:** Dimension 8 (Structural Topology)

**Intent:** Define the structure, capabilities, and maturity states of the shipped product.

**Contents:**
- Formal ontology of shipped products
- Capability catalog and feature hierarchy
- Maturity stages (e.g. Beta, GA, Deprecated)
- Dependency mapping (capabilities & features)
- Customer-facing specifications
- Internal feature models (variants, constraints, entitlements)
- Value Stream definitions

**Purpose:** Serves as canonical source for product structure -- supports agent reasoning for product evolution, entitlement, and configuration.

**Best Practices**
- **Do:**
  - Maintain a single canonical product ontology
- **Don't:**
  - Store detailed requirements (these belong in PIR)

---

## Work Repository (WR)

**UPIM Mapping:** All 5 Tracks (Work Model instances)

**Intent:** Represent all actual work performed by human and AI agents across all tracks.

### A. Work Objects
- Epics, stories, tasks, subtasks (Track 2)
- Run Epics, Run Stories, Deployment Tasks, Change Requests, Maintenance Tasks (Track 3)
- Signal Exploration, Deliberation, Research, Experiments (Track 1)
- Win Cases, Win Reviews, Win Engagements (Track 4)
- Evolve Reviews, Evolve Definition Tasks (Track 5)
- Automated and human-assigned tasks
- Cross-team work items

### B. Work Breakdown & Planning
- Task decomposition and dependency graphs
- Critical paths, assigned agent(s), required artifacts
- Deliverables, time estimates/SLAs
- Workflows, sequences

### C. Execution State
- Status (planned, in-progress, blocked, completed, etc.)
- Timestamps (start, finish, update cadence) in UTC
- Artifacts produced (store canonical URIs to artifacts; no binaries)
- Verification outcomes
- Effort logs, failure modes, retries, escalations

### D. Responsibility & Attribution
- Internal agents (human + AI) assigned from WFR
- Role bindings referenced from Definition Model

### E. Workflow Memory
- Origin/rationale for tasks
- Decomposition/decision history
- Lessons learned
- Feedback integration (into PFR)

**Best Practices**
- **Do:**
  - Make all task structures machine-readable
  - Maintain bi-directional traceability to PIR, DAR, CAR, QVS, OPR
- **Don't:**
  - Embed code, binaries, or design artifacts directly (store URIs only)
  - Use WR as a long-term archive (apply rolling retention; lineage is archived in PEIR)

> **Notes:**
> - WR is the system of record for live, mutable operational state.
> - PEIR holds immutable lineage snapshots of WR changes; corrections in PEIR are modeled via "supersedes/corrects."
> - Evidence (e.g., QVS test reports) is referenced by URI from WR; binaries remain in their source repositories.

---

## Workforce Repository (WFR)

**UPIM Mapping:** Operating Model (internal workforce)

> **Renamed from Agent & Workforce Repository (AWR).** "Workforce" naturally encompasses both human and AI workers without privileging either category. See DR-033 D2.

### 1. Purpose

WFR is the system of record for all internal human and AI agent identities, capabilities, role bindings, governance, and workforce planning -- enabling scalable, governed human-AI collaboration.

> **Role vs. Agent separation:** Roles are defined in the Definition Model (Win Stakeholder in Dim 2, User Persona in Dim 4, Developer/Programmatic Persona in Dim 6, Operational Persona in Dim 7). WFR agents reference these role definitions via role bindings. WFR does not define roles -- it assigns agents to roles defined elsewhere. See DR-034.

### 2. Scope

Covers these conceptual areas:
- **Agent Registry:** All internal agent identities (AI and human)
- **Role Binding:** Assignment of agents to Definition Model role definitions (Dim 2, 4, 6, 7)
- **Responsibility Allocation Ledger:** Assignment traceability
- **Workforce Allocation:** Loads, availability, assignment rules
- **Behavioral & Performance Metrics:** Telemetry, drift, quality
- **Governance & Safety:** Permissions, escalation, boundaries

### 3. Agent Registry Model

WFR tracks:

**For AI Agents:**
- Agent ID/version/description
- Underlying model identity (e.g. LLM version)
- Capabilities/tools
- Repository access permissions
- Safety and operational constraints
- Workload quotas, behavioral metrics, drift and health data

**For Human Agents:**
- Role-based (non-PII) identity
- Skills and expertise matrix
- Functional domain (engineering, QA, PM, etc.)
- Proficiency tier
- Availability windows
- Assignment and review authorities

### 4. Role Binding Model

Maps agents to Definition Model roles:
- **Win Stakeholder roles** (Dim 2): Pre-Sales Engineer, CS Manager, Account Executive, etc.
- **User Persona roles** (Dim 4): Internal testers, dogfood participants
- **Developer/Programmatic Persona roles** (Dim 6): Internal API consumers
- **Operational Persona roles** (Dim 7): SRE, Platform Engineer, Security Operator, etc.
- Track access: which tracks the agent can pick up work in
- Governance: permissions, escalation authority, delegation rules

### 5. Responsibility Allocation Ledger

Stores, for every work item:
- Assigned agent(s)
- Responsibility type (plan/execute/verify/approve)
- Execution logs (timestamped)
- Delegation/escalation chains
- Approvals and verification signatures
- Outcome summaries and quality stats

*Integrates with WR for full traceability.*

### 6. Workforce Allocation Model

Tracks and allocates:
- Workload per agent
- Active assignments, idle capacity
- Overutilization alerts
- Skill-based and SLA-driven assignment rules
- Human-AI workload balancing

### 7. Behavioral & Performance Metrics

WFR aggregates:
- Task success/rework rates
- Quality scores (from QVS)
- Collaboration effectiveness
- Reliability, drift, and human agent growth

### 8. Governance & Safety Framework

Implements:
- Role-based access control (RBAC)
- Per-agent repository permissions
- Restricted/oversight domains
- Segregation-of-duties enforcement
- Escalation and override protocols
- Audit policies and explainability requirements

### 9. Integration with Other Repositories

WFR orchestrates agent interaction and access throughout the system:
- **PIR:** Assigns PM/Planner for idea refinement
- **DKB:** Aligns access with roles/capabilities
- **DAR:** Identifies authorized Architect/Designer
- **CAR:** Controls Developer agent permissions
- **QVS:** Defines QA/SDET roles for verification
- **OPR:** Controls SRE/DevOps agent permissions for operational artifacts
- **WR:** Manages all agent work assignments
- **PFR:** Routes feedback to responsible agents (FIR triage assignments)
- **PEIR:** Links agent identity to lineage/impact records
- **POR:** Controls ontology/capability access per role
- **ESR:** WFR agents reference ESR for external stakeholder identity when processing work items

### 10. Information Flow Involving WFR

1. New task enters WR
2. WR queries WFR for eligible agents (role binding, skills, availability, safety)
3. WFR assigns the task
4. Agent executes and updates WR/QVS/OPR
5. WFR logs responsibility, updates metrics
6. Changes propagate to PEIR for lineage/history
7. Governance / safety checks run

---

## External Stakeholder Registry (ESR)

**UPIM Mapping:** Cross-cutting (reference layer)

> **New repository.** ESR is introduced as a reference layer for external parties. See DR-033 D3 and DR-034 D4.

### 1. Purpose

ESR provides a single, UPIM-internal reference point for external stakeholders -- customers, partners, prospects, and third-party developers -- who are referenced in work items but are not internal workers.

### 2. Nature: Reference Layer, Not System of Record

ESR is a **projection** (reference layer), not a system of record. The system of record for customer data remains the organization's CRM/subscription management system. ESR holds the minimum identity and reference pointers needed by the UPIM:

- **Customer identity:** Organization name, segment classification (Dim 3), primary contacts
- **Partner identity:** Partner name, partnership type, integration scope
- **Prospect identity:** Prospect name, engagement stage
- **Developer identity:** External developers with sandbox access or partnership agreements (Dim 6)
- **Communication preferences:** Preferred channels, notification subscriptions
- **CRM/Source system reference:** Pointer back to the authoritative external system

### 3. Why Not WFR?

External parties are *consumers* of the product, not agents in the product organization's work model. They do not pick up work across tracks. Mixing them with internal workers in WFR would conflate workforce management with customer/partner management. See DR-034 D4.

### 4. Cross-References from Other Repositories

ESR is referenced by:
- **PFR-Win:** FIR reporters, Win Case customers
- **OPR:** Incident affected tenants (via Tenant -> Customer -> ESR)
- **PIR:** Need requesting customers, Customer Segment instances
- **WR:** Work item customer/partner references

### 5. Best Practices
- **Do:**
  - Keep ESR lightweight -- minimum identity required for UPIM references
  - Maintain CRM/source system reference pointers for authoritative data
  - Synchronize periodically with source systems
- **Don't:**
  - Duplicate full CRM data into ESR
  - Track internal agents (WFR)
  - Use ESR as a billing or subscription management system

---

## End-to-End Information & Value Flow

```mermaid
graph TB
    %% Nodes
    subgraph Strategy_Definition ["Strategy & Definition"]
        DKB[("DKB<br/>(Domain Knowledge)")]
        PIR[("PIR<br/>(Product Intent)")]
        POR[("POR<br/>(Product Ontology)")]
    end

    subgraph Engineering_Core ["Engineering Core (Value Stream)"]
        DAR[("DAR<br/>(Design & Arch)")]
        CAR[("CAR<br/>(Code Artifacts)")]
        QVS[("QVS<br/>(Quality & Verify)")]
    end

    subgraph Operations ["Operations & Feedback"]
        OPR[("OPR<br/>(Operations)")]
        PFR[("PFR<br/>(Feedback:<br/>Win/Run/Build)")]
    end

    subgraph Work_Orchestration ["Work & Practices"]
        PPR[("PPR<br/>(Practices & Policies)")]
        WR[("WR<br/>(Work & Tasks)")]
    end

    subgraph Foundation ["Governance, Workforce & Memory"]
        WFR[("WFR<br/>(Workforce)")]
        ESR[("ESR<br/>(External Stakeholders)")]
        PEIR[("PEIR<br/>(Evolution & Lineage)")]
    end

    %% Main Value Flow (Solid Thick Lines)
    PIR ==>|Intent/Reqs| DAR
    DAR ==>|Blueprints/Specs| CAR
    CAR ==>|Implementation| QVS
    QVS ==>|Verification Results| WR
    CAR ==>|Deploy Descriptors| OPR

    %% Support & Context Flows (Dotted)
    DKB -.->|Context/Feasibility| PIR
    DKB -.->|Domain Rules| DAR
    POR -.->|Capabilities| PIR
    PPR -.->|Templates| DAR
    PPR -.->|Scaffolds| CAR
    PPR -.->|Policies/Gates| QVS

    %% Feedback Loops
    PFR -->|FIR-routed Signals| PIR
    PFR -->|FIR-routed Bugs| WR
    PFR -->|Incident Mirrors| OPR

    %% Governance & Work Orchestration
    WFR -->|Assigns Agents| WR
    ESR -.->|Stakeholder Refs| PFR
    ESR -.->|Customer Refs| PIR
    WR -->|Orchestrates Work| PIR
    WR -->|Orchestrates Work| DAR
    WR -->|Orchestrates Work| CAR
    WR -->|Orchestrates Work| QVS
    WR -->|Orchestrates Work| OPR

    %% Memory & Lineage (The Central Sink)
    PIR & DKB & DAR & CAR & QVS & WR & PFR & PPR & POR & WFR & OPR & ESR -.->|Lineage/Embeddings| PEIR

    %% Styling
    classDef storage fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef ops fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    classDef foundation fill:#f3e5f5,stroke:#4a148c,stroke-width:2px;

    class PIR,DKB,POR,DAR,CAR,QVS,PFR,PPR,WR storage;
    class OPR,ESR ops;
    class WFR,PEIR foundation;
```

### Value Flow Narrative

1. Product intent (Signals, Ideas, PSDs) is captured in **PIR**
2. **DKB** checks domain feasibility and provides business rules
3. **DAR** produces architectural blueprints, API models, and infrastructure specifications
4. **CAR** implements design as code
5. **QVS** verifies code correctness with build-time quality evidence
6. **OPR** receives deployment descriptors and records deployments; stores run-time verification evidence and incident records
7. **PFR** ingests product-in-operation feedback via FIRs (PFR-Win), with mirrors in PFR-Run (incidents) and PFR-Build (bugs)
8. **PEIR** logs evolution and relationships across all repositories
9. **PPR** provides reusable standards/practices influencing all design/code/verification
10. **WR** coordinates, executes, and tracks agent work through the lifecycle across all 5 tracks
11. **WFR** assigns internal agents (human + AI) to work based on role bindings, skills, and availability
12. **ESR** provides external stakeholder references for FIR reporters, Win Case customers, and Incident-affected tenants

---

## Landscape Topology & Discovery

**Scope:** All repositories are scoped to a Landscape.

### Definition (C4-inspired)
A Landscape is the C4 System Landscape boundary for a product/program within an enterprise. It encompasses the people and software systems (internal and external) that collaborate to deliver the product's capabilities. The Landscape serves as the highest-level context boundary for repositories, policies, identities, and lineage in this guide.

- Purpose: provide a coherent semantic, architectural, and governance scope for a product/program.
- Boundaries: aligns with C4 System Landscape; external systems are modeled as dependencies but remain outside the Landscape boundary.
- Isolation: repositories, policies, and identities default to Landscape-local scope; cross-landscape links require explicit URIs and approvals.
- Identity: all artifact URIs are prefixed with `<landscape>` to ensure global uniqueness and traceability.

### Mono vs Poly within a Landscape
- Mono-repos (one per repo-type per landscape): `PIR`, `DKB`, `DAR`, `PEIR`, `PPR`, `POR`, `PFR`, `WFR`, `OPR`, `ESR`
- Poly-repos (multiple per repo-type per landscape): `CAR`, `QVS`, `WR`

### Discovery Index
- Maintain a per-landscape discovery index mapping:
  - `<repo-type> -> <repo-id> -> location, owners, ACL class`
  - Exposed as a machine-readable manifest (YAML/JSON) and registered in PEIR for lineage.
- Constraints:
  - `<repo-id>`: DNS-safe kebab-case, unique within `<repo-type>` in the landscape.
  - URIs MUST include `<landscape>` to avoid collisions across landscapes.

### Policy Distribution
- Verification policy specifications live in `PPR` (SoT), versioned and reusable across the landscape.
- `QVS` repos pin specific `PPR` policy versions and execute gates; evidence flows back to `QVS` and lineage to `PEIR`.

## Global Identity & Referencing

**Purpose:** Provide a universal, stable way to reference any artifact across repositories to enable unambiguous traceability, policy enforcement, and automation.

### URI Scheme

Use canonical artifact URIs for all cross-repository references. Repositories are scoped to a Landscape, and multiple sub-repositories can exist under each repo-type:

```text
artifact://<landscape>/<repo-type>/<repo-id>/<artifact-type>/<artifact-name>|<artifact-id>@<version>
# Components
# - <landscape>: the landscape identifier (e.g., 'eon')
# - <repo-type>: one of PIR, DKB, DAR, CAR, QVS, PEIR, PPR, POR, PFR, WR, WFR, OPR, ESR
# - <repo-id>: identifier of the sub-repository within that type (e.g., 'core', 'payments', 'platform')
# - <artifact-type>: repo-defined category (e.g., adr, api, test, capability, policy, work-item, fir, incident, agent)
# - <artifact-name>|<artifact-id>: human-readable name OR opaque stable id (prefer name + stable id when available)
# - @<version>: semantic version or immutable revision hash; omit only if strictly immutable
```

### Rules
- Every artifact that can be referenced MUST have a stable identity; prefer semantic versioning for human-authored specs and immutable digests for generated outputs.
- Cross-repo links MUST use canonical URIs (no relative paths). WR, PEIR, QVS, and OPR MUST reference artifacts via URIs.
- Repo types own their `<artifact-type>` taxonomy. Each sub-repo MUST document its taxonomy in its README and register `<repo-id>` in a discovery index.
- `<repo-id>` MUST be unique within a `<repo-type>` namespace and resolvable via the discovery index.
- PEIR MUST record lineage edges using URIs and include timestamps in UTC, provenance, and justification.

### Examples
- DAR ADR (core designs):
  `artifact://eon/DAR/DAR-core/adr/choose-message-bus@1.2.0`
- QVS Test Case (checkout test suite):
  `artifact://eon/QVS/QVS-checkout/test/payment-declined@3.1.0`
- CAR Service API (payments service):
  `artifact://eon/CAR/CAR-payments/api/payments-service@2.4.1`
- POR Capability (global ontology):
  `artifact://eon/POR/POR-global/capability/checkout/payment-processing@1.0.0`
- WR Work Item (program code 'pushpa' repo):
  `artifact://eon/WR/WR-pushpa/work-item/EPIC-1234@2025.12.10`
- OPR Incident (operations):
  `artifact://eon/OPR/OPR-core/incident/INC-2026-0847@1`
- OPR Deployment Record:
  `artifact://eon/OPR/OPR-core/deployment/DEP-2026-0312@1`
- PFR FIR (Win feedback):
  `artifact://eon/PFR/PFR-win/fir/FIR-2026-04291@1`
- WFR Agent:
  `artifact://eon/WFR/WFR-core/agent/sre-john-doe@1`
- ESR Customer:
  `artifact://eon/ESR/ESR-core/customer/globalpay-sa@1`

### PEIR Lineage Record (fields)
- from_uri, to_uri, relation (e.g., derives_from, verifies, implements, routes_to, originates_from)
- version_info (both ends)
- timestamp_utc
- source (pipeline/agent)
- rationale (short text or pointer)

---

## Embeddings & Knowledge Graph: Ownership and Synchronization

**Objective:** Eliminate ambiguity between local, developer-facing embeddings and the authoritative, cross-repo knowledge graph and indices.

### Ownership
- **CAR (per `<repo-type>/<repo-id>`):**
  - Generates and stores local embeddings for source code, API specs, and developer docs within that sub-repo.
  - Purpose: accelerate IDE and agent-local features (navigation, autocomplete, local semantic search).
  - Scope: non-authoritative; limited to sub-repo content; versioned with code.
- **PEIR (global):**
  - Owns the cross-repo knowledge graph and the authoritative embedding registry.
  - Aggregates embeddings across all repositories and artifact types; builds queryable vector indices keyed by canonical artifact URIs.
  - Records provenance: model identity, parameters, source commit(s), creation timestamp (UTC), and toolchain version.

### Artifact Scope (PEIR)
- Product intents, strategy, business models (PIR)
- Domain ontologies, glossaries, rules (DKB)
- Architecture artifacts: ADRs, diagrams (textual sources), models (DAR)
- Source code and APIs (CAR)
- Tests, policies, coverage/evidence (QVS)
- Deployment descriptors, incidents, operational artifacts (OPR)
- Practitioner templates and standards (PPR)
- Product ontology and capabilities (POR)
- Feedback, FIRs, Win Cases (PFR)
- Work items, decomposition, decision summaries (WR)
- Agent roles, metrics, governance specs (WFR)
- External stakeholder references (ESR)
- Lineage records and reasoning logs (PEIR)

### Modalities & Extractors
- Text-first embeddings from canonical textual forms (Markdown, YAML/JSON, code).
- Diagrams/graphics: embed textual sources (e.g., PlantUML/Mermaid); for binaries, extract structured captions/labels before embedding.
- Ontologies/graphs: embed concept labels and relation phrases; retain structured graph in PEIR for hybrid search.
- Policies/tests: embed descriptions and assertions while preserving executable sources as artifacts.

### Synchronization & Events
- Triggers:
  - CAR code changes merged to main -> emit event to PEIR to (re)ingest and refresh global indices.
  - New or updated artifacts in any repo (PIR, DKB, DAR, QVS, POR, PFR, WR, WFR, OPR, ESR) -> emit ingestion events to PEIR.
  - Model/policy changes in PEIR (e.g., new embedding model) -> PEIR schedules reindex jobs and records new versions.
- Mechanism:
  - Event payloads MUST include canonical URIs, commit SHAs, and embedding manifest references.
  - Idempotent ingestion: PEIR deduplicates by (URI, version, model-id, params-hash).

### Versioning & Reproducibility
- Embeddings MUST be tied to the artifact URI including `@<version>`.
- Embedding manifests MUST include:
  - `artifact_uri`, `artifact_version`
  - `model_id`, `model_version`, `parameters_hash`
  - `source_commit`, `toolchain_version`, `created_at_utc`
- PEIR keeps historical embeddings for lineage; the "active" index is the latest policy-compliant version.

### Security & Governance
- WFR governs access to embeddings and indices by role; sensitive artifacts MUST be excluded or redacted upstream.
- CAR MUST avoid embedding PII or restricted content; PEIR enforces redaction policies during ingestion.
- Export controls: cross-tenant export disabled by default; audit logs recorded in PEIR.

### File & Location Conventions
- CAR:
  - Store manifests under `artifact://<landscape>/CAR/<repo-id>/embedding-manifest/<name>|<id>@<version>`
  - Store local indices under `artifact://<landscape>/CAR/<repo-id>/embedding-index/<name>|<id>@<version>`
- PEIR:
  - Register global entries under `artifact://<landscape>/PEIR/global-embedding-registry/<artifact-id>@<version>`
  - Expose queryable indices under `artifact://<landscape>/PEIR/vector-index/<domain>|<scope>@<version>`

---

## WR <-> PEIR Boundaries and Defaults

**Source of Truth**
- WR: live, mutable operational state (status, assignee, ETA, notes, current artifact URIs).
- PEIR: immutable lineage snapshots and edges; corrections via "supersedes/corrects."

**Snapshot Cadence**
- Event-driven deltas emitted on: create, assignment/status change, PR merge, QVS gate pass/fail, reopen/close.
- Nightly full snapshot for reconciliation.

**Granularity**
- One node per WR work item, plus per-change lineage edges in PEIR.

**Identity & Versioning**
- WR maintains a mutable record with internal revision.
- PEIR snapshot URIs: `artifact://WR/<repo-id>/work-item/<key>@<event-seq>`
  (one version per emitted event).

**Evidence & Attachments**
- QVS is source of truth for build-time reports/logs; OPR is source of truth for run-time reports. WR stores URIs only.
- PEIR references evidence via edges; no binaries stored.

**Timestamps (UTC)**
- WR: `created_at`, `updated_at`, `due_at`.
- PEIR: `event_at` (primary), `snapshot_at`, `ingested_at`.
- Ordering by (`event_at`, sequence); tolerate minor clock skew.

**Corrections & Deletions**
- WR edits and soft-deletes allowed.
- PEIR never deletes; uses "terminated" edges and "corrects/supersedes" relations.

**Access Control**
- WR writes by assignees/leads under WFR.
- PEIR writes only via ingestion pipeline; backfills require WFR-approved roles.

**Retention**
- WR: rolling 12-24 months (configurable).
- PEIR: long-term archival and regulated retention policies.

**Event Model & Idempotency**
- Payload includes artifact URI, previous/new version, change-set hash, actor, `event_at`.
- Idempotency key: (URI, version/hash); retries deduplicated.

**Linking to Other Repositories**
- WR stores only canonical URIs.
- PEIR materializes edges to PIR, DKB, DAR, CAR, QVS, POR, PFR, WFR, OPR, ESR.

**Metrics Ownership**
- WR: live dashboards.
- PEIR: durable historical metrics (cycle time, rework, DORA-like), recomputed on late events.

**Embeddings**
- WR stores no vectors.
- PEIR embeds WR titles/descriptions/decision notes on significant updates.

---

## Future Clarifications

- WFR-driven ACL reconciliation across poly repos (CAR/QVS/WR): Automate repo ACLs from WFR role model; periodic reconciliation and audit attestations.
- Cross-repo events & automation: Standardize event types (PR merge, policy update, test results, FIR creation, incident creation), payload schema (URIs, versions, hashes, event_at), handlers, retries, and idempotency keys.
- File formats & schemas: Mandate canonical machine-readable formats per repo and publish minimal JSON Schemas (PIR items, DAR ADRs/models, CAR artifact manifests, QVS test metadata/policies, OPR deployment records/incidents, WR work items, WFR agent profiles, ESR stakeholder references, PEIR lineage edges).
- Quality gates & policy linkage: Author verification policies in PPR; define linkage to POR capabilities and PIR intents; QVS pins versions and executes build-time gates; OPR executes run-time gates.
- Access & approval matrix: Define WFR roles -> repo write/approve rights -> gate responsibilities; derive branch protections from matrix.
- Time & retention defaults: Confirm UTC-only timestamps everywhere; define per-repo retention and archival (WR rolling; PEIR long-term; OPR incident archival); reconcile clock skew rules.
- Security & compliance: Classification levels, redaction policies (especially for PEIR ingestion), export controls, and WFR-governed access patterns.
- Golden path lifecycle: End-to-end example with PR sequence, artifact URIs, gate checks, event emissions, and lineage snapshots.
- POR <-> DAR mapping: Enforce mapping of architecture elements to POR capabilities; validate in CAR CI and record mapping edges in PEIR.
- OPR <-> WR boundary: Define which Track 3 entities are work items (WR) vs. artifacts/records (OPR). See OperatingModel.TODO.
- PFR-Run mirror synchronization: Define the reference mechanism from PFR-Run to OPR incidents. See OperatingModel.TODO.
- ESR synchronization: Define periodic sync mechanism from CRM/source systems to ESR projections.
