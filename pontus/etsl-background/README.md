# ETSL Documentation Index
## Enterprise Truth & Semantics Layer — Reader's Guide

**Welcome.** This folder contains the complete guidance corpus for the **Enterprise Truth & Semantics Layer (ETSL)** — a framework for making enterprise truth explicit, governed, and reusable.

Whether you are a CIO evaluating the approach, an architect designing ETSL artifacts, or an engineer implementing data applications, this guide will help you navigate the material efficiently.

---

## How This Documentation Is Organized

The ETSL corpus is structured in **layers of depth**:

| Layer | Purpose | Start Here If... |
|-------|---------|------------------|
| **Introduction** | Why ETSL exists, what problem it solves | You're new to ETSL or need to explain it to others |
| **Terminology** | Precise definitions that govern all ETSL work | You need to use ETSL vocabulary correctly |
| **Conceptual Foundations** | Deep dives into key distinctions (ontology vs truth, facts vs events) | You're designing ETSL artifacts or resolving architectural debates |
| **Building ETSL** | How to build ETSL Semantic and Data Artifacts | You're an architect or engineer implementing ETSL |
| **Building Data Products** | How to build products that consume ETSL correctly | You're building analytics, features, or consumer-facing products |

---

## Reader Journeys by Persona

### 🎯 CIOs, CDOs, and Executive Leaders

**Your goal:** Understand what ETSL is, why it matters, and what it changes.

**Recommended path:**
1. **Start here:** [ETSL Purpose and Story](ETSL_Purpose_and_Story.md) — The "why" before the "how"
2. **Quick reference:** [ETSL One-Page Onboarding Primer](etsl_one_page_onboarding_primer.md) — Core concepts in 5 minutes
3. **Optional depth:** Sections 11–12 of the Purpose doc for compounding benefits and closing vision

**Time investment:** 30–45 minutes

**Key takeaway:** ETSL makes truth explicit so teams can build faster without re-arguing meaning.

---

### 🏗️ Enterprise Architects and Data Architects

**Your goal:** Design ETSL artifacts, model authority, and integrate ETSL into enterprise data architecture.

**Recommended path:**
1. **Foundation:** [ETSL Purpose and Story](ETSL_Purpose_and_Story.md) — Full read for context
2. **Terminology:** [Tier-1 ETSL Canonical Terminology](Tier1_ETSL_Canonical_Terminology.md) — Normative definitions (memorize these)
3. **Classifications:** [Tier-2 ETSL Canonical Classifications](Tier2_ETSL_Canonical_Classifications.md) — Behavioral classifications
4. **Conceptual clarity:**
   - [Ontology vs ETSL](etsl-vs-ontology.md) — When to use each
   - [Ontology vs Semantic Artifacts vs Data Artifacts](artifacts__ontology_vs_etsl_semantic_vs_etsl_data.md) — Three-layer distinction
   - [Facts vs Events](events-vs-facts.md) — Critical modeling distinction
5. **Physical architecture:** [ETSL Physical Layers](etsl-physical-layers.md) — How ETSL maps to storage
6. **Building ETSL:**
   - [Semantic Model Guidance for Architects](building-etsl/semantic-model/etsl_semantic_model_guidance_for_architects.md)
   - [Authority Modeling Guidance](building-etsl/semantic-model/etsl_authority_modeling_guidance_for_architects.md)
   - [Data Modeling Guidance](building-etsl/semantic-model/data-modeling-guidance.md)
   - [State Modeling](building-etsl/semantic-model/state-modelling.md)
   - [Building ETSL Data Artifacts](building-etsl/data-artifacts/Building_ETSL_Data_Artifacts_in_a_Large_Enterprise.md)
   - [State Engineering](building-etsl/data-artifacts/state-engineering.md)
7. **Co-existence:** [ETSL and Data Mesh Coexistence](building-etsl/data-artifacts/etsl_and_data_mesh_coexistence_guidance.md)

**Time investment:** 4–6 hours for full depth; 2 hours for essential path

**Key takeaway:** ETSL is a semantic layer you can implement incrementally without disrupting existing systems.

---

### 👩‍💻 Data Engineers

**Your goal:** Implement Data Applications that execute ETSL semantics correctly.

**Recommended path:**
1. **Quick start:** [ETSL One-Page Onboarding Primer](etsl_one_page_onboarding_primer.md) — Core vocabulary
2. **Terminology:** [Tier-1 ETSL Canonical Terminology](Tier1_ETSL_Canonical_Terminology.md) — Definitions you must not drift
3. **Classifications:** [Tier-2 ETSL Canonical Classifications](Tier2_ETSL_Canonical_Classifications.md) — Know your Data Application type
4. **Conceptual clarity:**
   - [Ontology vs Semantic Artifacts vs Data Artifacts](artifacts__ontology_vs_etsl_semantic_vs_etsl_data.md) — Understand the three layers
   - [Facts vs Events](events-vs-facts.md) — What to model and how
5. **Modeling and implementation:**
   - [Assertion Guidance for Data Engineers](building-etsl/semantic-model/etsl_semantic_model_assertion_guidance_for_data_engineers.md)
   - [Data Modeling Guidance](building-etsl/semantic-model/data-modeling-guidance.md)
   - [State Modeling](building-etsl/semantic-model/state-modelling.md)
   - [Building ETSL Data Artifacts](building-etsl/data-artifacts/Building_ETSL_Data_Artifacts_in_a_Large_Enterprise.md) — Comprehensive engineering guide
   - [State Engineering](building-etsl/data-artifacts/state-engineering.md)
6. **Physical implementation:** [ETSL Physical Layers](etsl-physical-layers.md)
7. **Context:** [ETSL and Data Mesh Coexistence](building-etsl/data-artifacts/etsl_and_data_mesh_coexistence_guidance.md) — How ETSL fits with Data Mesh

**Time investment:** 3–4 hours

**Key takeaway:** You implement Data Applications that *execute* semantics—you do not define truth.

---

### 📊 Product Managers and Domain Leaders

**Your goal:** Understand how ETSL affects data products and domain ownership.

**Recommended path:**
1. **Start here:** [ETSL Purpose and Story](ETSL_Purpose_and_Story.md) — Focus on Sections 8–9
2. **Quick reference:** [ETSL One-Page Onboarding Primer](etsl_one_page_onboarding_primer.md)
3. **Data products:** [Building Data Products using ETSL Data Artifacts](building-data-products/Building_Data_Products_using_ETSL_Data_Artifacts.md) — Comprehensive guidance
4. **Comparison:** [ETSL vs Other Data Product Approaches](building-data-products/etsl-data-prodcuts-vs-other-approaches.md)

**Time investment:** 1–2 hours

**Key takeaway:** ETSL does not take away domain ownership—it removes the burden of re-arguing enterprise truth in every initiative.

---

### 🔬 ETSL Semantic Model Architects

**Your goal:** Design and govern ETSL Semantic Artifacts with precision.

**Recommended path (in order):**
1. **Foundation:** [ETSL Purpose and Story](ETSL_Purpose_and_Story.md)
2. **Terminology:** [Tier-1](Tier1_ETSL_Canonical_Terminology.md) and [Tier-2](Tier2_ETSL_Canonical_Classifications.md) — Normative
3. **Conceptual depth:**
   - [Ontology vs ETSL](etsl-vs-ontology.md)
   - [Ontology vs Semantic vs Data Artifacts](artifacts__ontology_vs_etsl_semantic_vs_etsl_data.md)
   - [Facts vs Events](events-vs-facts.md) (including Appendix on Provenance)
4. **Semantic modeling:**
   - [Semantic Model Guidance for Architects](building-etsl/semantic-model/etsl_semantic_model_guidance_for_architects.md)
   - [Semantic Model Representation](building-etsl/semantic-model/etsl-semantic-model-representation.md)
   - [Data Modeling Guidance](building-etsl/semantic-model/data-modeling-guidance.md)
   - [Relationships Modeling Guidance](building-etsl/semantic-model/relationships-modeling-gudiance.md)
   - [State Modeling](building-etsl/semantic-model/state-modelling.md)
5. **Authority modeling:** [Authority Modeling Guidance](building-etsl/semantic-model/etsl_authority_modeling_guidance_for_architects.md)
6. **Industry anchors:** [Banking Industry Reference Models](etsl_banking_industry_reference_models_for_semantic_modeling.md)

**Time investment:** Full corpus (6–8 hours)

**Key takeaway:** Semantics are specified once and executed many times. Precision here prevents downstream chaos.

---

## Document Catalog

### Introduction and Purpose

| Document | Purpose | Audience |
|----------|---------|----------|
| [ETSL Purpose and Story](ETSL_Purpose_and_Story.md) | Why ETSL exists, what it solves, executive framing | All; especially leaders |
| [ETSL One-Page Onboarding Primer](etsl_one_page_onboarding_primer.md) | Core vocabulary in 5 minutes | All |

### Terminology (Normative)

| Document | Purpose | Audience |
|----------|---------|----------|
| [Tier-1 ETSL Canonical Terminology](Tier1_ETSL_Canonical_Terminology.md) | Semantic primitives that must not drift | All |
| [Tier-2 ETSL Canonical Classifications](Tier2_ETSL_Canonical_Classifications.md) | Behavioral and architectural classifications | Architects, Engineers |

### Conceptual Foundations

| Document | Purpose | Audience |
|----------|---------|----------|
| [Ontology vs ETSL](etsl-vs-ontology.md) | When to use ontology vs ETSL; common misconceptions | Architects, Senior Engineers |
| [Ontology vs Semantic vs Data Artifacts](artifacts__ontology_vs_etsl_semantic_vs_etsl_data.md) | Three-layer artifact distinction | Architects, Engineers |
| [Facts vs Events](events-vs-facts.md) | Critical modeling distinction with provenance guidance | Architects, Engineers |
| [ETSL Physical Layers](etsl-physical-layers.md) | How ETSL maps to physical storage architecture | Architects, Engineers |
| [Banking Industry Reference Models](etsl_banking_industry_reference_models_for_semantic_modeling.md) | Using BIAN, FIBO, ISO 20022 with ETSL | Semantic Model Architects |

### Building ETSL Artifacts

| Document | Purpose | Audience |
|----------|---------|----------|
| **Semantic Model** | | |
| [Semantic Model Guidance for Architects](building-etsl/semantic-model/etsl_semantic_model_guidance_for_architects.md) | How to design ETSL Semantic Artifacts | Architects |
| [Authority Modeling Guidance](building-etsl/semantic-model/etsl_authority_modeling_guidance_for_architects.md) | Modeling authority explicitly | Architects |
| [Assertion Guidance for Data Engineers](building-etsl/semantic-model/etsl_semantic_model_assertion_guidance_for_data_engineers.md) | Engineering assertions correctly | Engineers |
| [Semantic Model Representation](building-etsl/semantic-model/etsl-semantic-model-representation.md) | How to represent semantic models | Architects, Engineers |
| [Data Modeling Guidance](building-etsl/semantic-model/data-modeling-guidance.md) | ETSL-specific data modeling patterns | Architects, Engineers |
| [Relationships Modeling Guidance](building-etsl/semantic-model/relationships-modeling-gudiance.md) | Modeling relationships in ETSL | Architects, Engineers |
| [State Modeling](building-etsl/semantic-model/state-modelling.md) | Deriving state from facts and events | Architects, Engineers |
| **Data Artifacts** | | |
| [Building ETSL Data Artifacts](building-etsl/data-artifacts/Building_ETSL_Data_Artifacts_in_a_Large_Enterprise.md) | Comprehensive guide to Data Artifact engineering | Architects, Engineers |
| [ETSL and Data Mesh Coexistence](building-etsl/data-artifacts/etsl_and_data_mesh_coexistence_guidance.md) | How ETSL and Data Mesh work together | All |
| [State Engineering](building-etsl/data-artifacts/state-engineering.md) | Engineering state derivation | Architects, Engineers |

### Building Data Products

| Document | Purpose | Audience |
|----------|---------|----------|
| [Building Data Products using ETSL Data Artifacts](building-data-products/Building_Data_Products_using_ETSL_Data_Artifacts.md) | How to build products that consume ETSL correctly | Product teams, Architects |
| [ETSL vs Other Data Product Approaches](building-data-products/etsl-data-prodcuts-vs-other-approaches.md) | Comparison with DW, Data Mesh, Feature Stores, etc. | Architects, Product Managers |

---

## Quick Reference: Document Relationships

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           ETSL Purpose and Story                            │
│                     (Why ETSL exists — start here)                          │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          ▼                         ▼                         ▼
┌──────────────────┐    ┌───────────────────┐    ┌────────────────────────┐
│  Tier-1 & Tier-2 │    │  One-Page Primer  │    │  Conceptual Foundations│
│   Terminology    │    │  (Quick Start)    │    │  (Ontology, Facts,     │
│   (Definitions)  │    │                   │    │   Events, Physical)    │
└────────┬─────────┘    └─────────┬─────────┘    └───────────┬────────────┘
         │                        │                          │
         └────────────────────────┼──────────────────────────┘
                                  │
         ┌────────────────────────┴────────────────────────┐
         ▼                                                 ▼
┌────────────────────────────┐              ┌────────────────────────────────┐
│    Building ETSL           │              │    Building Data Products      │
│    (Semantic Models,       │              │    (Consuming ETSL correctly,  │
│     Data Artifacts)        │◄────────────►│     Product engineering)       │
└────────────────────────────┘              └────────────────────────────────┘
```

---

## Principles for Using This Documentation

1. **Start with purpose, not mechanics.** Read the Purpose and Story before diving into technical guidance.

2. **Master the vocabulary.** Tier-1 terminology is non-negotiable. If these terms drift, ETSL collapses.

3. **Understand the distinctions.** The difference between ontology and ETSL, between facts and events, between semantic and data artifacts—these are not academic. They prevent real architectural failures.

4. **Match depth to role.** Not everyone needs every document. Use the persona paths above.

5. **Refer, don't restate.** When building artifacts or products, reference these documents—don't create local glossaries that drift.

---

## A Note on Document Status

| Status | Meaning |
|--------|---------|
| **Architectural Guidance Document** | Production-ready, reviewed, suitable for broad use |
| **Phase-1 Draft** | Early draft, subject to revision |
| **Appendix** | Supplementary material, typically attached to a primary document |

Most documents in this folder are **Architectural Guidance Documents**. Phase-1 drafts, where they exist, are being progressively enriched.

---

## Getting Help

If you encounter:
- **Terminology confusion** → Consult Tier-1 and Tier-2 documents
- **Architectural debates** → Refer to the relevant conceptual foundation document
- **Implementation questions** → Start with the relevant "Building" guide

If a concept is unclear or seems to conflict across documents, escalate to the ETSL architecture team. Semantic coherence across this corpus is actively maintained.

---

## Final Reminder

> **ETSL decides what is true.  
> Everything else decides how to use it.**

Welcome to the ETSL corpus. Start with what matters to your role, and go as deep as you need.

---

