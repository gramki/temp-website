# Discovery Case

**Model:** Work Model
**Track:** Discovery
**Category:** Orchestration
**Owner:** Product Management for product alignment; originating and participating functions may vary

## Definition

A Discovery Case is the Discovery Track orchestration item that organizes cross-functional discovery work around a product-relevant question, concern, bet, obligation, opportunity, technical idea, architectural concern, operational insight, or product-manager judgment until a decision or routing outcome is reached.

Discovery Case is signal-optional. A Signal may start a case, be added to a case, be produced by a case, or be absent entirely.

## Purpose

Discovery Case prevents Discovery from being modeled as only customer-Signal processing or Product Manager-only work. It provides a case envelope for cross-functional learning, evidence gathering, deliberation, modeling, and routing decisions.

Discovery Case is the Track 1 counterpart to FIR's envelope pattern in the Win Track: FIR coordinates reactive product-in-operation feedback; Discovery Case coordinates proactive and cross-functional product learning.

## Origin Types

| Origin type | Typical source | Example |
|---|---|---|
| Signal | PM, Support, CS, customer/prospect | "Three customers need batch payout upload." |
| Signal Cluster | PM, Product Ops, agent | "Multiple onboarding friction Signals point to one root cause." |
| Product judgment | Product Manager | "Re-evaluate the FX pricing model before LATAM launch." |
| Objective / KRA / SLA | Product leadership | "Activation target is not achievable with current onboarding." |
| Customer commitment | Sales, CS, executive sponsor | "Contract commits to API v2 readiness by Q3; feasibility unknown." |
| Customer Promise gap | Product, CS, Governance | "Promise says self-serve onboarding; product requires implementation support." |
| Customer Release Intent | PM, Release, Win | "LATAM Expansion scope needs discovery before release planning." |
| Technical idea | Engineering | "Explore a unified adapter framework." |
| Architecture concern | Architect / ARB | "Current module boundary blocks API extensibility." |
| Technical debt | Engineering | "Settlement engine cannot support projected volume." |
| QA concern | QA | "Verification gaps make SLA evidence impossible." |
| Operational insight | SRE / Run | "Incident pattern suggests need for circuit-breaker strategy." |
| Release learning | Release / PM | "Delivered feature exposed adoption friction." |
| Governance / compliance concern | Governance, Security, Compliance | "Audit evidence cannot support compliance posture." |
| Executive direction | Leadership | "Explore embedded finance market entry." |
| Agent / monitoring observation | Authorized agent or monitor | "Trend detection flags rising failed activation attempts." |

## Fields

| Field | Type | Description |
|---|---|---|
| Discovery Case ID | String | Unique identifier |
| Title | String | Concise statement of the discovery question |
| Origin Type | Enum | One of the origin types above |
| Originator | Person / Agent | Who opened the case |
| Originating Function | Enum | Product, UX, Engineering, Architecture, QA, Run, Win, Governance, Executive, Agent |
| Accountable PM | Person / Role | Product owner accountable for product alignment |
| Participating Functions | List | Functions participating in the case |
| Source References | List | Signals, Objectives, KRAs, SLAs, incidents, customer commitments, technical proposals, or other source records |
| Discovery Question | Text | What the case is trying to learn or decide |
| Expected Decision Type | Enum | Go, Kill, Pivot, Model Update, Route Elsewhere, Evidence Only |
| Status | Enum | Current lifecycle status |
| Evidence References | List | Research, Experiment, Prototype/Spike, Deliberation, or Build evidence |
| PDR References | List | PDRs produced by the case |
| Product Intent References | List | Product Intents produced or requested by the case |
| Routing Outcome | Enum / Text | Closed outcome: dismissed, parked, Product Intent, Run Case, Win Case, Evolve Case, Governance Ritual / Enforcement, etc. |

## Statuses

| Status | Description |
|---|---|
| Opened | Case has been created but not yet scoped |
| Scoped | Discovery question, participants, and expected outcome are defined |
| In Progress | Discovery sub-work is underway |
| In Deliberation | Evidence is being evaluated or a decision is being formed |
| Decided | PDR or routing outcome has been recorded |
| Routed | Follow-on Product Intent, Modeling Task, or cross-track case has been created |
| Closed | Case is complete |
| Parked | Valid case, deferred for future consideration |
| Dismissed | Case judged not worth pursuing or out of scope |
| Superseded | Replaced by another Discovery Case |

## Sub-Work

A Discovery Case may contain or coordinate:

- Signal Exploration Tasks
- Research Tasks
- Experiments
- Prototypes / Spikes
- Deliberations
- Modeling Tasks
- Discovery Support Product Intents for bounded Build evidence

## Outcomes

| Outcome | Meaning |
|---|---|
| Dismissed | No further action |
| Parked | Valid but deferred |
| Kill PDR | Explicit decision not to pursue |
| Go / Pivot PDR | Product decision recorded |
| Product Intent | Evolution Product Intent created |
| Multiple Product Intents | One decision decomposed into multiple evolution threads |
| Discovery Support Product Intent | Build work requested to produce evidence |
| Modeling Task | Definition Model update required |
| Run Case | Operational follow-up required |
| Win Case | Reactive customer/prospect work required |
| Evolve Case | Process/model/practice change required |
| Governance Ritual / Enforcement | Governance/evidence/approval issue requires handling |

## Product Alignment

Discovery Case creation is cross-functional. Any authorized function may originate a case. PDRs that materially change product direction require Product Management alignment before they reach Final status.

Technical ADRs and operational ODRs do not substitute for PM alignment on product-direction decisions.

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| May include | Signal (Strategy) | Case may originate from or later collect Signals |
| Produces | Idea (Strategy) | Case may synthesize Ideas |
| Produces | Product Decision Record (Strategy) | Case may produce PDRs |
| May request | Product Intent (Strategy) | Case may create Discovery Support Product Intent for Build evidence |
| May create | Product Intent (Strategy) | Go/Pivot PDR from case may create Evolution Product Intent |
| Contains | Signal Exploration / Research / Experiment / Prototype / Deliberation / Modeling Task | Discovery sub-work belongs to the case |
| May route to | Run Case / Win Case / Evolve Case / Governance Ritual / Governance Enforcement | Case may close by routing to another track |

## Examples

- "Discovery Case: assess event-sourcing for audit trail" — origin: Architecture Concern, no Signal filed. Produces technical spike evidence and PDR.
- "Discovery Case: LATAM onboarding friction" — origin: Signal Cluster. Produces Ideas and a Product Intent for self-serve onboarding.
- "Discovery Case: committed API v2 readiness for Customer X" — origin: Customer Commitment. Requests Discovery Support Product Intent for feasibility Build work before final PDR.
