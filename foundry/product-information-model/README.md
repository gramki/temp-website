# Unified Product Information Model (UPIM)

The UPIM is a comprehensive framework for describing, managing, and evolving a software product. It provides a shared language across Product Management, Engineering, Operations, and Business stakeholders.

---

## Architecture: Three Models

The UPIM is structured as three models, each building on the one below:

```
┌─────────────────────────────────────────────────────────────────┐
│                      Operating Model                            │
│                                                                 │
│  How the organization EXECUTES                                  │
│                                                                 │
│  ┌─────────────────────┐     ┌─────────────────────────────┐   │
│  │   Coordination      │◄───►│      Organization           │   │
│  │                     │     │                              │   │
│  │   Ceremonies        │     │   Roles & responsibilities   │   │
│  │   Cadences          │     │   Team structures            │   │
│  │   Rituals           │     │   Skills & proficiency       │   │
│  │   Decision rhythms  │     │   Training                   │   │
│  │                     │     │   Tools & resources           │  │
│  └─────────────────────┘     └─────────────────────────────┘   │
│            ▲                             ▲                       │
│            └──────── entangled ──────────┘                       │
├─────────────────────────────────────────────────────────────────┤
│                       Work Model                                │
│                                                                 │
│  What work EXISTS — entities, artifacts, state transitions      │
│  Structured as 5 Tracks: Discovery, Build, Run, Win, Evolve     │
├─────────────────────────────────────────────────────────────────┤
│                    Definition Model                              │
│                                                                 │
│  What the product IS — its complete structural description       │
│  Structured as 9 Dimensions across 4 Tiers                      │
└─────────────────────────────────────────────────────────────────┘
```

### Dependency Direction

Each model depends on the one below — never the reverse:

| Layer | Depends on | Question it answers |
|---|---|---|
| **Operating Model** | Work Model | How does the org execute? (coordination + organization) |
| **Work Model** | Definition Model | What work exists? (entities, artifacts, state transitions) |
| **Definition Model** | — (foundation) | What is the product? (9 Dimensions) |

Reading bottom-to-top: **Define the product** → **Define what work moves the product** → **Define how the org executes that work**.

### Why Three Models, Not Four?

An earlier design explored separating "Coordination" (ceremonies, cadences) and "Organization" (roles, teams, skills) into two distinct models with a strict layering. This was rejected because the relationship between coordination and organization is **bidirectional and entangled**:

- Coordination choices shape organization: "We chose Scrum → we need a Scrum Master."
- Organization realities shape coordination: "We only have 3 PMs → we can't run 6 parallel Signal Reviews."

Strict layering implies one-way dependency. Since these two concerns co-constrain and co-evolve, they are modeled as **two entangled facets of a single Operating Model** rather than separate layers. See DR-014 for the full decision rationale.

---

## The Definition Model (9 Dimensions)

The Definition Model describes **what the product is** — its complete structural reality at any given moment. The 9 Dimensions are grouped into four tiers:

| Tier | Dimensions | What it covers |
|---|---|---|
| **Strategy & Intent** | Dim 1: Strategy | Portfolio context, strategic themes, objectives, initiatives (with lever mix and embedded targets), Customer Release Intents, signals, ideas, decisions, Product Intents, specifications |
| **Business & Market** | Dim 2: Vendor Value (Why It Wins) | Win stakeholders, win outcomes (with achievement levers), delivery friction, business model (with lever portfolio), pricing tiers, value metrics, business KPIs, win barriers — across AAARRR lifecycle |
| | Dim 3: Customer Value | Customer segments, buying personas, outcomes, pains, promises, metrics, barriers |
| **Technical Execution** | Dim 4: User-Centric (Experience) | User personas, jobs (JTBD), UX channels (modality × engagement mode), user journeys. Touchpoints deprecated to work artifacts. |
| | Dim 5: Technical & Architectural | Architecture model, systems (many-to-many with Dim 8 modules), components, dependencies, interaction flows, architecture decision records (ADR), technical knowledge base. Technical counterpart to Dim 8's functional view. See DR-024. |
| | Dim 6: Ecosystem & Extensibility | Developer personas, programmatic user personas, API/Integration/Extension/SDK modules, API operations (Command/Query/Event/Callback/Batch with SLOs), API compatibility contracts. Deliberate extensibility strategy, not incidental APIs. Integration Modules also serve Operational Personas (DR-023). |
| | Dim 7: Operational (Runtime & DevOps) | Infrastructure model, operational personas (quality-taxonomy archetypes), operational jobs, operational journeys, deployment environments, operational targets (SLOs with achievement levers), operational constraints, operational pains, operational readiness, operations decision records (ODR). Completes the PDR/ADR/ODR decision record triad. See DR-023, DR-025. |
| **Bridge (Taxonomy)** | Dim 8: Structural (Topology) | Products, modules, capabilities, features, value streams |
| | Dim 9: Data & Information | Data domains, entities, attributes, states |

**Reference document:** `draft-definition-model.md`

---

## The Work Model (5 Tracks)

The Work Model describes **what work exists** — the entities, artifacts, and state transitions that represent how maker roles organize their daily work to mutate the 9 Dimensions — and to evolve the Work Model and Operating Model themselves. Each track owns its own planning work alongside its core activities.

| Track | Goal | Primary Owner | Key Entities |
|---|---|---|---|
| **Track 1: Discovery** (Learning) | Set strategic direction, open Discovery Cases, explore signals/questions, validate ideas, create Product Intent, refine intent into specifications | Cross-functional; Product Management owns product alignment | Objective Setting Task, Discovery Case, Signal Exploration Task, Deliberation, Research Task, Experiment, Prototype/Spike, Specification Task, Modeling Task, Signal Monitoring |
| **Track 2: Build** (Construction) | Plan releases, decompose PSDs into Module-scoped Epics and System-scoped Tasks, produce three-tier versioned artifacts (Component → System → Product) | Tech Lead, Developers, QA | Epic, Story, Technical Task, Bug, Integration Epic, Integration Story, Design Deliberation, Component Version, System Version, Product Version, Technical Debt Item, Build Monitoring |
| **Track 3: Run** (Stability) | Plan deployments, manage tenants, maintain SLA/uptime | DevOps, SRE | Deployment, Incident, Change Request, Maintenance Task, Tenant, System Monitoring, System Deployment Specification, Product Deployment Specification |
| **Track 4: Win** (Value Realization) | Plan, equip, execute, respond, assess, monitor across AAARRR lifecycle to achieve Win Outcomes | Customer Success, Product Marketing, Sales, Support | Win Planning (5 subtypes), Win Enablement (4 subtypes), Win Activity (7 subtypes), Win Case, Win Review → Feedback, Win Monitoring |
| **Track 5: Evolve** (Process Evolution) | Assess, define, and refine Work Model and Operating Model — entity definitions, artifact types, DoD criteria, guidance structures | Process Leads, Product Ops, Engineering Managers | Evolve Planning, Evolve Review → Evolve Findings, Evolve Definition Task, Evolve Monitoring |

**Reference document:** `draft-work-model.md`
**Execution framework:** `draft-work-execution-framework.md` — artifacts, artifact type catalog with assessment criteria, definition of done, and guidance patterns for all work entities

---

## The Operating Model (Future)

The Operating Model describes **how the organization executes** — the coordination patterns and organizational design that enable the Work Model to function. It covers two entangled facets:

| Facet | What it covers | Examples |
|---|---|---|
| **Coordination** | Ceremonies, cadences, rituals, decision-making rhythms | Weekly Signal Review, Sprint Planning, Quarterly Prioritization Review, Architecture Review Board |
| **Organization** | Roles, team structures, compositions, skills, training, tools, resources | Cross-functional squads, PM skill profiles, tooling standards |

These facets are **co-designed** — every coordination choice implies organizational requirements, and every organizational reality constrains coordination options. They are not layered; they are entangled.

> **Status:** The Operating Model's internal structure (subdivision terminology, entity catalog) will emerge from the modeling work. The Definition Model has 9 Dimensions and the Work Model has 5 Tracks — the Operating Model's organizational pattern will earn its name when we build it out. Track 5 (Evolve) is the structural bridge between the Work Model and Operating Model — it is the only track whose outputs directly modify both models.

---

## Folder Structure

```
product-information-model/
├── README.md                         ← This file (PIM architecture overview)
├── draft-definition-model.md         ← Definition Model reference document
├── draft-work-model.md               ← Work Model reference document
├── draft-work-execution-framework.md ← Work execution dimensions: artifacts, DoD, guidance
├── draft-modeling-faqs.md            ← Design decisions and rationale (Q&A format)
├── narrative-seeds.md                ← Connective insights and perspectives for future narrative docs
├── entities/                         ← One file per entity (canonical detail)
│   ├── README.md                     ← Entity catalog structure and conventions
│   ├── definition-model/             ← Entities from the 9 Dimensions
│   │   ├── dim1-*.md                 ← Strategy Dimension entities
│   │   ├── dim2-*.md                 ← Vendor Value (Why It Wins) entities
│   │   ├── dim3-*.md                 ← Customer Value entities
│   │   ├── dim4-*.md through dim9-*.md
│   │   └── psd-templates/            ← PSD templates by module archetype
│   └── work-model/                   ← Entities from the 5 Tracks
│       ├── track1-*.md               ← Discovery Track entities
│       ├── track2-*.md               ← Build Track entities
│       ├── track3-*.md               ← Run Track entities
│       ├── track4-*.md               ← Win Track entities
│       └── track5-*.md               ← Evolve Track entities
└── decisions/                        ← Decision records (ADR format)
    ├── README.md                     ← Decision record index
    └── DR-*.md                       ← Individual decision records
```

---

## Key Design Principles

1. **Definition vs. Work separation.** The Definition Model describes *what is*; the Work Model describes *what people do*. Entities like Idea and PSD are Definition Model entities (specifications), not Work Model entities (actions). Work Model entities (Research Task, Experiment) *mutate* Definition Model entities.

2. **Signal, not requirement.** Inputs to the Discovery Track are Signals — observations that warrant attention, not commitments to deliver. This fosters investigation over fulfillment. (See FAQ Q16, DR-006.)

3. **Each track owns its planning.** Rather than a separate "Plan Track," planning work is distributed — Discovery plans Objectives/Initiatives, Build plans Releases/Iterations, Run plans Deployments, Win plans GTM, Evolve plans process evolution cycles. (See DR-002.)

4. **Cross-dimensional specifications.** PSDs are cross-dimensional impact assessments, not just feature specs. Every PSD acknowledges implications across all 9 Dimensions. (See FAQ Q9.)

5. **Decision traceability.** The chain Signal → Idea → PDR → Product Intent → PSD provides full traceability from observation through reasoning, routable intent, and specification. No gaps, no implicit decisions. (See FAQ Q6, DR-013.)

6. **Initiative as cross-track coordination.** Initiatives drive work across all five tracks, not just Discovery → Build. They carry a lever mix (weighted from the Business Model's Lever Portfolio) and embedded targets (like OKR Key Results). This makes cross-track investment explicit. (See FAQ Q32, DR-017.)

7. **Strategy is decision-grade direction, not raw intake.** Strategy contains Themes, Objectives, Initiatives, Customer Release Intents, commitments, constraints, PDRs, and Product Intents. Raw requests, untriaged Signals, tasks, bugs, incidents, PSD body content, and deployment records may inform strategy, but they are not strategy themselves. (See DR-038.)

8. **Operating Model deferred, not omitted.** Coordination and organizational design are explicitly scoped out of the Work Model — they belong to the Operating Model, which will be developed separately.

9. **Self-evolving model.** The Work Model explicitly accounts for its own evolution through Track 5: Evolve. A model that cannot evolve is dead. Track 5 is the only track whose outputs directly modify both the Work Model and the Operating Model. (See FAQ Q62, DR-022.)

---

## Reference Example

All examples throughout the UPIM use a consistent reference product: **B2B Core Payment Gateway (Cross-Border Payouts)**.

---
