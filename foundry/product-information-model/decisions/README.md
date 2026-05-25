# UPIM Decision Records

This folder contains decision records for significant design choices made during the development of the Unified Product Information Model (UPIM). Each record documents the context, decision, rationale, and consequences.

## Format

Decision records follow a lightweight Architecture Decision Record (ADR) format:

- **Status:** Proposed | Accepted | Superseded | Deprecated
- **Context:** What situation or problem prompted the decision
- **Decision:** What was decided
- **Rationale:** Why this choice was made over alternatives
- **Consequences:** What follows from the decision (both positive and negative)

## Naming Convention

Files are named: `DR-<NNN>-<short-description>.md` (e.g., `DR-001-strategic-entities.md`).

## Index

| ID | Title | Status | Date |
|---|---|---|---|
| DR-001 | Add Strategic Entities (Objective, Initiative) to Dimension 1 | Accepted | 2026-02-15 |
| DR-002 | Distribute Planning Work Across All Four Tracks | Accepted | 2026-02-15 |
| DR-003 | Customer Release Intent as Named Business Delivery Target | Accepted | 2026-02-15 |
| DR-004 | Three-Layer Versioning: System Version, Module Version, Product Version (updated by DR-026) | Accepted | 2026-02-15 |
| DR-005 | Deployment Tracked Per-Environment, Not as Version Status (updated by DR-026) | Accepted | 2026-02-15 |
| DR-006 | "Signal" as Collective Term for Problem, Need, Opportunity | Accepted | 2026-02-15 |
| DR-007 | Restructure Dimension 3 as the Customer Value Dimension | Accepted | 2026-02-15 |
| DR-008 | Introduce Value Stream as a Dim 8 Entity | Accepted | 2026-02-15 |
| DR-009 | Introduce Modeling Task as a Discovery Track Work Entity | Accepted | 2026-02-15 |
| DR-010 | Split Research Task into Signal Exploration Task and Research Task | Accepted | 2026-02-15 |
| DR-011 | Introduce Deliberation as a Discovery Track Entity | Accepted | 2026-02-15 |
| DR-012 | Dimension 3 Comprehensiveness Refinements — Buying Committee, Pain, Barrier Types | Accepted | 2026-02-15 |
| DR-013 | Dimension 1 Comprehensiveness Refinements — Theme, Signal Lifecycle, Idea/PDR Fields | Accepted | 2026-02-15 |
| DR-014 | Three-Model Architecture — Definition, Work, Operating (consolidation of 4 to 3) | Accepted | 2026-02-15 |
| DR-015 | Restructure Dim 2 as The Vendor Value Dimension (Why It Wins) — AAARRR lens, Win entities | Accepted | 2026-02-15 |
| DR-016 | Win Track Restructure — Six Categories, Initiative-Embedded Targets, Win Review, Win Case | Accepted | 2026-02-16 |
| DR-017 | Initiative Evolves to Cross-Track Coordination Construct with Lever Mix and Embedded Targets | Accepted | 2026-02-16 |
| DR-018 | Introduce Work Execution Framework — Artifacts, Definition of Done, and Guidance Patterns | Accepted | 2026-02-15 |
| DR-019 | Cross-Track Monitoring and Win Track Gap Remediation | Accepted | 2026-02-15 |
| DR-020 | Dimension 4 Expansion — User-Centric Dimension with JTBD, UX Channel, and Touchpoint Deprecation | Accepted | 2026-02-15 |
| DR-021 | Dimension 6 Expansion — Ecosystem & Extensibility with Personas, Module Types, and Deliberate Extensibility | Accepted | 2026-02-15 |
| DR-022 | Track 5: Evolve (Process Evolution) and Artifact Type Catalog | Accepted | 2026-02-19 |
| DR-023 | Dimension 7 Expansion — Operational Dimension with 9 Entities, Tenant in Run Track, Scope Widenings | Accepted | 2026-02-15 |
| DR-024 | Dimension 5 Expansion — Technical & Architectural Dimension with 7 Entities, ADR, Dim 8/Dim 5 Duality | Accepted | 2026-02-15 |
| DR-025 | Operations Decision Record (ODR) — Completing the Decision Record Triad (PDR/ADR/ODR) | Accepted | 2026-02-15 |
| DR-026 | Build Track Detailing — Work Entity/Artifact Distinction, Scoping Corrections, Three-Tier Versioning | Accepted | 2026-02-15 |
| DR-027 | Composition Levels, Module Package, and Run Track Engineering (refined by DR-029) | Accepted | 2026-02-15 |
| DR-028 | Deployment Descriptors — SDD, MDD, PDD (refined by DR-029) | Accepted | 2026-02-15 |
| DR-029 | Change-to-Deployment Workflow Redesign — Deployment Train, Station, Change Request, Package Specs, Deployment Task/Artifact Split | Accepted | 2026-02-15 |
| DR-030 | Incident Management Refactor — ITSM-Aligned Artifact/Entity Separation, SEV Model, PIR, Communication, Correlation | Accepted | 2026-02-25 |
| DR-031 | Hotfix / Emergency Fix Path — P0 Sprint Bypass, Emergency Gate Profile, Deferred-Gate Obligation | Accepted | 2026-02-25 |
| DR-032 | FIR (First Information Report) — Universal Intake Pattern | Accepted | 2026-04-06 |
| DR-033 | Repository Architecture — OPR, ESR, WFR, PIR Rename, PFR Subdivision | Accepted | 2026-04-06 |
| DR-034 | Role vs. Agent Separation — Definition Model Roles, WFR Agents, ESR External Stakeholders | Accepted | 2026-04-06 |
| DR-035 | Dim 8 & PSD Structural Decisions — Module Functional Classification, Capability Templates, System/Component Redefinition, PSD Authorship Split | Accepted | 2026-05-19 |
| DR-036 | Versioning and Deployment Simplification — Component/System/Product Version Chain, Deployment Specifications, Package Removal | Accepted | 2026-05-19 |
| DR-037 | Product Intent as Hybrid Bridge Entity | Accepted | 2026-05-24 |
| DR-038 | Customer Release Intent and PI Console Formation Views | Accepted | 2026-05-25 |

**Note:** DR-036 amends DR-004, DR-026, DR-027, DR-028, and DR-029 for operational deployment and versioning semantics. Historical bodies of those records are preserved with superseded banners; DR-036 is authoritative for current modeling.

---
