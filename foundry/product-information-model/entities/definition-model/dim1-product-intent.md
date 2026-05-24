# Product Intent

**Model:** Definition Model and Work Model bridge
**Dimension:** Dimension 1: The Strategy Dimension
**Owner:** Product Management

## Definition

Product Intent is the hybrid bridge entity that translates a product decision into downstream product evolution work. It records the committed direction — what the product intends to change, for whom, and why — after a Go or Pivot product decision, and it is the ACE-routable item that triggers work across Product Specification, UX Design, Development, QA, Release, and Governance.

Product Intent is produced by Discovery Track outcomes, typically a Go or Pivot Product Decision Record (PDR). A Product Specification Document (PSD) refines Product Intent into a module-scoped build contract; the PSD does not create Product Intent.

## Purpose

Product Intent prevents the model from using a PSD as both the decision output and the execution trigger. The PDR records why a decision was made. Product Intent records the evolution commitment that should move through the product system. PSDs then refine that intent into specifications for affected modules.

This gives the product organization a traceable handoff:

```text
Signal -> Idea -> PDR / Product Decision -> Product Intent -> PSD(s) -> Epic(s)
```

One product decision may create multiple Product Intents. For example, a Go decision for "LATAM Enterprise Market Entry" may create separate intents for currency support, data residency, onboarding, pricing, and reporting.

## Hybrid Nature

Product Intent belongs to both model planes:

| Aspect | Meaning |
|---|---|
| **Definition Model** | Product Intent carries product meaning: decision provenance, intended outcome, target customers, affected promises, and strategic context. |
| **Work Model** | Product Intent has lifecycle state, triggers Specification Tasks and downstream Work Orders, and is tracked through execution. |
| **ACE routing** | Product Intent is the token ACE routes through Workspaces; every transition invokes governance scenarios. |

## Fields

| Field | Type | Description |
|---|---|---|
| Product Intent ID | String | Unique identifier, e.g. `PI-042` |
| Title | String | Concise name of the intended product evolution |
| Summary | Text | What change is intended and why |
| Source Decision(s) | List of References | PDRs or other product decision records that authorize the intent |
| Source Signal(s) | List of References | Problems, Needs, or Opportunities that contributed to the decision |
| Source Idea(s) | List of References | Hypotheses validated or pivoted by the decision |
| Objective(s) | List of References | Objectives this intent advances, if any |
| Initiative(s) | List of References | Initiatives this intent advances, if any |
| KRA / SLA Context | List of References | KRAs, SLAs, compliance commitments, operational targets, or customer promises that drove the decision |
| Intended Outcome | Text | Expected product, customer, vendor, or operational outcome |
| Affected Dimensions | List | UPIM dimensions expected to be touched by specification or modeling work |
| Status | Enum | Current lifecycle status |
| Current Workspace | Enum / Reference | ACE workspace currently holding or acting on the intent |
| PSD References | List of References | PSDs refining this intent |
| Work Order References | List of References | Work Orders created from this intent across Workspaces |
| Governance Events | List of References | Transition validations and evidence records |

## Statuses

| Status | Description |
|---|---|
| Formed | A product decision has produced a candidate Product Intent |
| Accepted | Product Intent is recognized as valid downstream evolution work |
| Parked | Valid intent, but execution is deferred |
| In Specification | Product Specification Workspace is refining the intent through Specification Tasks and PSDs |
| Specified | Required PSD refinement is approved for downstream execution |
| In Evolution | UX, Development, QA, or Release work is underway |
| Delivered | Release has produced Product Delivery for this intent |
| Closed | Outcome is assessed or archived |
| Superseded | Replaced by another Product Intent due to pivot or new evidence |
| Cancelled | Abandoned with rationale before delivery |

**State Diagram:**

```text
Formed -> Accepted -> In Specification -> Specified -> In Evolution -> Delivered -> Closed
              |              |                 |              |
              v              v                 v              v
            Parked      Cancelled          Superseded      Superseded
```

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Product Decision Record (Dim 1) | A Go or Pivot PDR may create one or more Product Intents |
| Upstream | Problem / Need / Opportunity (Dim 1) | Product Intent traces to source Signals through its decision chain |
| Upstream | Idea (Dim 1) | Product Intent may trace to one or more validated or pivoted Ideas |
| Context | Objective (Dim 1) | Product Intent may advance Objective(s) |
| Context | Initiative (Dim 1) | Product Intent may advance Initiative(s), but it is not limited to Initiative-sourced decisions |
| Context | Customer Release (Dim 1) | Product Intent may contribute to a Customer Release |
| Context | Business / Customer Value entities (Dims 2-3) | Product Intent may target Win Outcomes, Business KPIs, Customer Promises, or Customer Value Metrics |
| Downstream | PSD (Dim 1) | PSDs refine Product Intent into module-scoped build contracts |
| Work Model | Specification Task (Track 1) | Specification Tasks refine Product Intent by authoring or revising PSDs |
| Work Model | Epic (Track 2) | Approved PSDs decompose into Epics that execute the intent |
| ACE | Workspace transitions | Product Intent is routed across Workspaces and governed on every transition |

## Source Decisions

Product Intent maps to product decisions, not only to Initiatives. Decisions may arise from:

- Initiative investment decisions.
- KRA or planning-cycle decisions.
- SLA or customer-promise commitments.
- Compliance or regulatory decisions.
- Operational-readiness decisions.
- Strategic pivots or product council decisions.
- Release learnings that renew intent for the next cycle.

## PSD Refinement Boundary

PSD is a refinement of Product Intent. It specifies how an accepted Product Intent affects a particular module, capability, feature, user journey, API, system, operational target, or data entity. A PSD references the PDR for justification and references the Product Intent it refines.

The correct ordering is:

```text
Product decision -> Product Intent -> PSD refinement -> Build execution
```

not:

```text
Product decision -> PSD -> Product Intent
```

## ACE Routing Role

ACE uses Product Intent as the routed item in the Product Evolution Cycle. Arrival of Product Intent at a Workspace triggers that Workspace's Scenarios. Movement of Product Intent between Workspaces invokes Governance Workspace scenarios.

Discovery Track work establishes or updates Product Intent. Release may renew Product Intent for the next cycle using delivery evidence, feedback, and learnings.

## Example

PDR-017 records a Go decision for real-time FX rate locking based on customer interviews, a fake-door test, and a feasibility spike. That decision creates two Product Intents:

- PI-042: "Real-Time FX Rate Lock in Invoice Flow"
- PI-043: "FX Rate Audit Trail for Enterprise Reporting"

Each Product Intent enters the Product Specification Workspace. PI-042 is refined by a PSD scoped to the Invoice & Payout Module. PI-043 is refined by a PSD scoped to the FX Module. Both PSDs reference PDR-017 and preserve traceability to the original Problems and Needs.
