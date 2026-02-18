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
│  Structured as 4 Tracks: Discovery, Build, Run, Win             │
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
| **Strategy & Intent** | Dim 1: Strategy | Portfolio context, strategic themes, objectives, initiatives (with lever mix and embedded targets), signals, ideas, decisions, specifications |
| **Business & Market** | Dim 2: Vendor Value (Why It Wins) | Win stakeholders, win outcomes (with achievement levers), delivery friction, business model (with lever portfolio), pricing tiers, value metrics, business KPIs, win barriers — across AAARRR lifecycle |
| | Dim 3: Customer Value | Customer segments, buying personas, outcomes, pains, promises, metrics, barriers |
| **Technical Execution** | Dim 4: User-Centric (Experience) | User personas, jobs (JTBD), UX channels (modality × engagement mode), user journeys. Touchpoints deprecated to work artifacts. |
| | Dim 5: Technical & Architectural | Subsystems, components, functions |
| | Dim 6: Ecosystem & Extensibility | Developer personas, programmatic user personas, API/Integration/Extension/SDK modules, API operations (Command/Query/Event/Callback/Batch with SLOs), API compatibility contracts. Deliberate extensibility strategy, not incidental APIs. |
| | Dim 7: Operational (Runtime) | Environments, clusters, containers |
| **Bridge (Taxonomy)** | Dim 8: Structural (Topology) | Products, modules, capabilities, features, value streams |
| | Dim 9: Data & Information | Data domains, entities, attributes, states |

**Reference document:** `draft-definition-model.md`

---

## The Work Model (4 Tracks)

The Work Model describes **what work exists** — the entities, artifacts, and state transitions that represent how maker roles organize their daily work to mutate the 9 Dimensions. Each track owns its own planning work alongside its core activities.

| Track | Goal | Primary Owner | Key Entities |
|---|---|---|---|
| **Track 1: Discovery** (Learning) | Set strategic direction, explore signals, validate ideas, author specifications | Product Management, UX Research | Objective Setting Task, Signal Exploration Task, Deliberation, Research Task, Experiment, Prototype/Spike, Specification Task, Modeling Task, Signal Monitoring |
| **Track 2: Build** (Construction) | Plan releases, write code, produce quality-gated artifacts | Tech Lead, Developers, QA | Epic, User Story, Technical Task, Bug, Module Version, Product Version, Build Monitoring |
| **Track 3: Run** (Stability) | Plan deployments, maintain SLA/uptime | DevOps, SRE | Deployment, Incident, Change Request, Maintenance Task, System Monitoring |
| **Track 4: Win** (Value Realization) | Plan, equip, execute, respond, assess, monitor across AAARRR lifecycle to achieve Win Outcomes | Customer Success, Product Marketing, Sales, Support | Win Planning (5 subtypes), Win Enablement (4 subtypes), Win Engagement (7 subtypes), Win Case, Win Review → Feedback, Win Monitoring |

**Reference document:** `draft-work-model.md`
**Execution framework:** `draft-work-execution-framework.md` — artifacts, definition of done, and guidance patterns for all work entities

---

## The Operating Model (Future)

The Operating Model describes **how the organization executes** — the coordination patterns and organizational design that enable the Work Model to function. It covers two entangled facets:

| Facet | What it covers | Examples |
|---|---|---|
| **Coordination** | Ceremonies, cadences, rituals, decision-making rhythms | Weekly Signal Review, Sprint Planning, Quarterly Prioritization Review, Architecture Review Board |
| **Organization** | Roles, team structures, compositions, skills, training, tools, resources | Cross-functional squads, PM skill profiles, tooling standards |

These facets are **co-designed** — every coordination choice implies organizational requirements, and every organizational reality constrains coordination options. They are not layered; they are entangled.

> **Status:** The Operating Model's internal structure (subdivision terminology, entity catalog) will emerge from the modeling work. The Definition Model has 9 Dimensions and the Work Model has 4 Tracks — the Operating Model's organizational pattern will earn its name when we build it out.

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
│   └── work-model/                   ← Entities from the 4 Tracks
│       ├── track1-*.md               ← Discovery Track entities
│       ├── track2-*.md               ← Build Track entities
│       ├── track3-*.md               ← Run Track entities
│       └── track4-*.md               ← Win Track entities
└── decisions/                        ← Decision records (ADR format)
    ├── README.md                     ← Decision record index
    └── DR-*.md                       ← Individual decision records
```

---

## Key Design Principles

1. **Definition vs. Work separation.** The Definition Model describes *what is*; the Work Model describes *what people do*. Entities like Idea and PSD are Definition Model entities (specifications), not Work Model entities (actions). Work Model entities (Research Task, Experiment) *mutate* Definition Model entities.

2. **Signal, not requirement.** Inputs to the Discovery Track are Signals — observations that warrant attention, not commitments to deliver. This fosters investigation over fulfillment. (See FAQ Q16, DR-006.)

3. **Each track owns its planning.** Rather than a separate "Plan Track," planning work is distributed — Discovery plans Objectives/Initiatives, Build plans Releases/Iterations, Run plans Deployments, Win plans GTM. (See DR-002.)

4. **Cross-dimensional specifications.** PSDs are cross-dimensional impact assessments, not just feature specs. Every PSD acknowledges implications across all 9 Dimensions. (See FAQ Q9.)

5. **Decision traceability.** The chain Signal → Idea → PDR → PSD provides full traceability from observation through reasoning to specification. No gaps, no implicit decisions. (See FAQ Q6, DR-013.)

6. **Initiative as cross-track coordination.** Initiatives drive work across all four tracks, not just Discovery → Build. They carry a lever mix (weighted from the Business Model's Lever Portfolio) and embedded targets (like OKR Key Results). This makes cross-track investment explicit. (See FAQ Q32, DR-017.)

7. **Operating Model deferred, not omitted.** Coordination and organizational design are explicitly scoped out of the Work Model — they belong to the Operating Model, which will be developed separately.

---

## Reference Example

All examples throughout the UPIM use a consistent reference product: **B2B Core Payment Gateway (Cross-Border Payouts)**.

---
