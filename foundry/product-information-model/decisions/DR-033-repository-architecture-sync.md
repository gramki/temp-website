# DR-033: Repository Architecture — OPR, ESR, WFR, PIR Rename, PFR Subdivision

**Status:** Accepted
**Date:** 2026-04-06

## Context

The Foundry repository architecture was originally designed around the "Agent-Native Product Engineering System" framing with 11 repositories (PIR, DKB, DAR, CAR, QVS, PEIR, PPR, POR, PFR, WR, AWR). As the UPIM evolved — introducing 9 Dimensions, 5 Tracks, incident management, deployment workflows, and the FIR universal intake pattern — several gaps emerged:

1. PIR's name ("Product Idea Repository") understated its expanded scope (strategy, business model, customer value, signals, ideas, Product Intents, PSDs)
2. AWR's name ("Agent & Workforce Repository") implied AI-agent focus; the repository actually tracks all internal workers (human + AI)
3. CAR held deployment and operational artifacts alongside code — conflating build-time and run-time concerns
4. PFR was monolithic — feedback from Win, Run, and Build tracks had different ownership and lifecycle needs
5. No repository existed for external stakeholders (customers, partners, prospects) frequently referenced in work items
6. No clear separation between code quality evidence (build-time) and deployment quality evidence (run-time)

## Decisions

### D1: PIR renamed to Product Intent Repository

The scope of PIR expands to be the comprehensive ledger of strategic direction, business models, customer value propositions, and product evolution ideas. Internal structure: Strategy (Dim 1 strategic entities), Business Model (Dim 2), Customer Value (Dim 3), Signals & Ideas (Dim 1 flowing items), Product Intents (routable bridge items), Specifications (PSDs that refine Product Intent).

**Rationale:** "Product Idea Repository" implied PIR held only ideas. The repository actually holds the product's strategic intent across three dimensions. "Product Intent Repository" accurately reflects this scope while retaining the PIR abbreviation.

### D2: AWR renamed to WFR (Workforce Repository)

AWR is renamed to WFR. Scope: internal agents only (human + AI) who are enrolled to pick up work across tracks. "Workforce" naturally encompasses both human and AI workers without privileging either category.

**Rationale:** "Agent" in current discourse is heavily associated with AI agents, which could mislead readers into thinking AWR is an AI orchestration system. "Workforce" communicates the intent more clearly: this repository tracks everyone (human or AI) who does work. The internal structure (Role Model, Agent Registry, Capability Profiles, Governance) already handles heterogeneity.

### D3: ESR (External Stakeholder Registry) introduced

A new repository for external parties — customers, partners, prospects, developers — who are referenced in work items but are not internal workers. ESR is a **reference layer** (projection), not a system of record. The system of record for customer data remains the organization's CRM/subscription management system; ESR holds the minimum identity and reference pointers needed by the UPIM.

**Rationale:** External stakeholders are referenced extensively across the model (FIR reporters, Win Case customers, Incident affected tenants, Customer Release targets). Without ESR, these references are scattered and inconsistent. ESR provides a single, UPIM-internal reference point. Keeping it as a reference layer avoids duplicating CRM data.

### D4: OPR (Operations Repository) introduced

A new repository for Run Track artifacts — deployment descriptors (SDD/MDD/PDD), deployment records, incidents (system of record), Post-Incident Reports, operational artifact versions (Module/Product Package Versions), and deployment verification evidence.

**Rationale:** CAR (Code Artifact Repository) should hold source code and build artifacts only. Deployment descriptors, incident records, and operational artifact versions are run-time concerns with different ownership (SRE/DevOps vs. developers), different lifecycle (deployment progression vs. build progression), and different governance (change management vs. CI/CD). OPR gives Run Track artifacts a dedicated home.

### D5: PFR sub-partitioned into PFR-Win, PFR-Run, PFR-Build

PFR is divided into three sub-partitions based on the personas managing the feedback and the track affinity:

- **PFR-Win:** FIRs (universal intake), Win Cases, customer communication records, NPS/CSAT data. Primary entity: FIR.
- **PFR-Run:** Incident mirrors (references to OPR Incidents), operational observation summaries. OPR is the system of record; PFR-Run holds the feedback/customer-impact view.
- **PFR-Build:** Bug report mirrors (references to WR/Track 2 Bugs), technical debt observations, quality regression reports. WR is the system of record; PFR-Build holds the feedback view.

PFR-Discovery is removed. Signals are routed directly from FIRs (via triage) into PIR.

**Rationale:** Different teams manage different feedback streams with different lifecycles. Win team manages customer-facing feedback (PFR-Win). Run team manages operational observations (PFR-Run). Build team manages quality observations (PFR-Build). Sub-partitioning aligns repository ownership with team responsibility.

### D6: Verification evidence split — QVS for code quality, OPR for deployment quality

QVS owns evidence about code quality (test results, coverage, security scans, performance benchmarks — build-time verification). OPR owns evidence about deployment quality (deployment verification results, post-deployment SLA checks — run-time verification).

**Rationale:** Code quality and deployment quality have different ownership, different verification methods, and different lifecycle. Build Track verifies code; Run Track verifies deployments. Evidence should reside with the verifying track's repository.

## Consequences

**Positive:**
- Repository names accurately reflect UPIM scope and terminology
- Clear separation of build-time (CAR/QVS) and run-time (OPR) artifacts
- PFR sub-partitions align with team ownership
- ESR provides consistent external stakeholder references across all tracks
- WFR naming avoids AI-agent connotation

**Negative:**
- Existing references to PIR, AWR, PFR throughout the codebase need updating
- OPR and ESR are new repositories requiring definition and implementation
- PFR-Run mirror synchronization mechanism must be defined in the Operating Model
- 13 repositories (up from 11) increases the repository landscape complexity

## Revised Repository Landscape

| Abbreviation | Full Name | Scope | UPIM Mapping |
|---|---|---|---|
| PIR | Product Intent Repository | Strategy, Business Model, Customer Value, Signals, Ideas, Product Intents, PSDs | Dim 1, 2, 3 |
| DKB | Domain Knowledge Base | Domain knowledge, glossaries, ontologies, business rules | Dim 9 |
| DAR | Design & Architecture Repository | Architecture, API models, infrastructure, operational specs | Dim 5, 6, 7 (definitions) |
| POR | Product Ontology Repository | Product structure, capabilities, features, maturity | Dim 8 |
| CAR | Code Artifact Repository | Source code, build artifacts | Track 2 + Track 3 engineering code |
| QVS | Quality & Verification Store | Test cases, acceptance tests, build-time quality evidence | Track 2 quality verification |
| OPR | Operations Repository | Deployment descriptors/records, incidents, PIR reports, operational artifact versions | Track 3 artifacts |
| PFR-Win | Product Feedback — Win | FIRs (universal intake), Win Cases, customer communication records | Track 4 reactive inputs |
| PFR-Run | Product Feedback — Run | Incident mirrors (references OPR), operational observation summaries | Track 3 feedback view |
| PFR-Build | Product Feedback — Build | Bug report mirrors (references WR), technical debt observations | Track 2 feedback view |
| PPR | Product Practitioner Repository | Standards, templates, practices, verification policies | Operating Model + Track 5 |
| WR | Work Repository | All live work instances across all 5 tracks | Work Model instances |
| WFR | Workforce Repository | Internal agents (human + AI), role bindings, skills, availability, governance | Operating Model |
| ESR | External Stakeholder Registry | Customer/partner/prospect identity, contacts, communication preferences (reference layer) | Cross-cutting |
| PEIR | Product Evolution & Impact Repository | Lineage, impact graphs, historical metrics, cross-repo knowledge graph | Traceability |
