# Phase 1 Open Questions

This document lists unanswered questions that block product and engineering teams from turning ACE/UPIM into Phase 1 build contracts for the Foundry Platform.

The questions are organized by logical build area. Each section should eventually graduate into one or more implementation docs under this folder.

---

## 1. Phase 1 scope and success criteria

- What exact end-to-end golden path must Phase 1 demonstrate?
- Is the minimum path Discovery Case -> PDR -> Product Intent -> PSD -> Work Orders -> QA -> Release -> Governance evidence?
- Which Tracks are in scope for implementation: Discovery, Build, Release-as-Build, Governance only, or partial Run/Win visibility too?
- Which orchestration items are fully supported in Phase 1?
  - Discovery Case?
  - Product Intent?
  - Governance Ritual?
  - Governance Enforcement?
  - Customer Release Intent visibility only?
- What is explicitly out of scope?
- What counts as "Phase 1 complete" from a platform/product standpoint?
- What demo should a builder be able to run at the end of Phase 1?
- What must be real versus mocked or manually seeded?


Discovery Track:
- Create Objectives and Initiatives by clustering Signals
- Create Product Intent based on Signals
- Create Product Intent based on Customer Requirement
- Create Customer Release Intent


Governance:
- Governance is modeled as Rituals with cadence or event triggers, plus Enforcement that asserts policies.
- Which Governance Rituals are in Phase 1?
  - Workbench Sprint / iteration ritual?
  - Monthly Workbench summary?
  - Workbench SLA adherence review?
  - Release Intent progress and risk review?
  - Intent retrospective?
  - Product Intent retrospective?
  - Team productivity / contribution review?
- Which Governance Enforcement scenarios are in Phase 1?
- Which reports and dashboards are required inputs to those rituals?
- Which ritual outputs are supported: action items, findings, risk/debt entries, recognitions, Evolve Cases?

---

## 2. Module ownership and boundaries

- Which module owns creation of a Discovery Case?
- Which module owns storage and lifecycle transitions for Discovery Case?
- Which module owns Product Intent creation and lifecycle?
- Which module owns PDR creation/finalization?
- Which module owns PSD metadata and PSD artifact registration?
- Which module owns Work Order creation?
- Which module owns Work Order execution?
- Which module owns Task lifecycle?
- Which module owns Scenario catalog CRUD?
- Which module owns Workspace Session lifecycle?
- Which module owns governance verdicts?
- Which module owns evidence attachment and retrieval?
- Which module owns traceability graph APIs?
- Which module owns ID generation for Discovery Case, PDR, Product Intent, Work Order, Scenario, Governance Ritual, and Governance Enforcement?
- Is Foundry Management the system of record for repository metadata only, or for entity records too?
- Is Orchestrator state stored by Orchestrator, Management, WR, or a shared service?

---

## 3. Golden path behavior

- What is the exact first user action in the golden path?
  - Open Discovery Case?
  - Capture Signal?
  - Create PDR?
  - Create Product Intent?
- Who is the actor for each step: PM, engineer, governance user, agent, system?
- What UI surface does each step happen in?
- What module handles each action?
- What entity changes at each step?
- What event is emitted at each step?
- Which repository is read/written at each step?
- Which Work Order is created at each step?
- Which governance check runs at each step?
- What is the happy-path sequence for:
  - Discovery Case creation
  - evidence collection
  - PDR finalization
  - Product Intent creation
  - PSD refinement
  - Development work
  - QA verification
  - Release publication
  - Release renewal

---

## 4. Orchestration model

- What is the canonical platform representation of an orchestration item?
- Does each orchestration item have a common interface?
- Which fields are common across Discovery Case, Product Intent, Run Case, Win Case, Evolve Case, Governance Ritual, and Governance Enforcement?
- How does Orchestrator know which Track an item belongs to?
- How does Orchestrator know which Workspaces participate for a given orchestration item?
- How are cross-track links represented?
  - Discovery Case -> Product Intent
  - Product Intent -> Governance Ritual / Governance Enforcement
  - Product Intent -> Run Case
  - Customer Release Intent -> Product Intent
- Are orchestration item graphs DAGs, cyclic graphs, or typed relationship graphs?
- Can one Work Order belong to more than one orchestration item?
- Can one orchestration item spawn Work Orders in parallel Workspaces?
- How does Orchestrator handle bidirectional Specification <-> UX routing?
- How does Orchestrator handle return from Development/QA to Product Specification?
- How are retries, rejections, and returns represented?

---

## 5. Discovery Case contract

- What are the minimum required fields for Discovery Case?
- Who can create a Discovery Case?
- What authorization is required for non-PM functions to create one?
- What are the Phase 1 Discovery Case statuses?
- Are `Opened`, `Scoped`, `In Progress`, `In Deliberation`, `Decided`, `Routed`, `Closed`, `Parked`, `Dismissed`, and `Superseded` all needed in Phase 1?
- Which origin types are supported in Phase 1?
- Is Signal optional in the API and UI?
- Can Discovery Case create or link Signals after the case is opened?
- How are participating functions tracked?
- How is accountable PM assigned?
- What constitutes PM alignment?
- How is PM alignment recorded for PDR finalization?
- Can a Discovery Case create a Discovery Support Product Intent before PDR?
- What governance applies to opening, routing, and closing Discovery Cases?
- What is the minimum Discovery Case UI?

---

## 6. Product Intent contract

- What are the minimum required fields for Product Intent?
- Which Product Intent purposes are supported in Phase 1?
  - Evolution / Delivery
  - Discovery Support
  - Technical Validation
  - Internal / Enabling
  - Operational Enablement
  - Release Renewal
- Are "Evolution" and "Delivery" separate values or one value?
- Can Discovery Support Product Intent exist without a PDR?
- What authorizes Discovery Support Product Intent?
- What lifecycle states are required per Product Intent purpose?
- Which purposes can create PSD Work Orders?
- Which purposes can enter Release Planning?
- Which purposes imply customer-committed delivery?
- Which purposes require Customer Release Intent linkage?
- How does UI show "not customer-committed delivery"?
- How does Product Intent link to PDR, Discovery Case, Customer Release Intent, PSD, Work Orders, governance events, and evidence?
- What is the API for creating, accepting, parking, superseding, cancelling, or closing Product Intent?

---

## 7. PDR and product decision contract

- What is the minimal PDR schema for Phase 1?
- What decision types are supported?
- How is `Product Direction Change` determined?
- Who can mark Product Direction Change true or false?
- What is PM alignment?
- Is PM alignment a field, approval event, signature, comment, or governance verdict?
- Can PDR be finalized without PM alignment if Product Direction Change is false?
- Can a PDR create multiple Product Intents?
- How is the PDR -> Product Intent mapping represented?
- What happens for Kill PDRs?
- What happens for Pivot PDRs?
- What governance scenario validates PDR finalization?

---

## 8. Scenario catalog MVP

- What is the minimal Phase 1 scenario set?
- What scenario IDs and names should be standardized?
- Which Track and Workspace owns each scenario?
- What are the inputs and outputs of each scenario?
- Which scenarios can be agent-executed?
- Which scenarios require human tasks?
- Which scenarios create follow-on Work Orders?
- Which scenarios emit orchestration events?
- Which governance scenarios are required?

Candidate Phase 1 scenarios:

| Track | Workspace | Scenario |
|-------|-----------|----------|
| Discovery | Product Specification | Open Discovery Case |
| Discovery | Product Specification | Frame Discovery Case |
| Discovery | Product Specification | Finalize PDR |
| Discovery | Product Specification | Create Product Intent |
| Build | Product Specification | Refine Product Intent to PSD |
| Build | UX Design | Design for Product Intent |
| Build | Development | Implement Product Intent |
| Build | QA | Prepare verification |
| Build | QA | Verify Product Intent |
| Build | Release | Publish Product Delivery |
| Governance | Governance | Validate transition |
| Governance | Governance | Capture evidence |

---

## 9. Work Order contract

- What is the minimal Work Order schema?
- Does every Work Order require:
  - parent orchestration item type and ID?
  - Track?
  - Workspace?
  - Scenario?
  - input artifact references?
  - expected output references?
  - governance policy references?
- What are the Phase 1 Work Order statuses?
- Who can create a Work Order manually?
- Which Work Orders are Orchestrator-created?
- Can Work Orders be attached to Workspace Sessions later?
- Can multiple Work Orders attach to one Workspace Session?
- How are Work Orders ordered or prioritized?
- How are dependencies between Work Orders represented?
- What event is emitted when a Work Order completes?
- What is the difference between Work Order completion and orchestration item transition?

---

## 10. Event contracts

- What event bus or event interface is used in Phase 1?
- Are events synchronous API calls, async events, or both?
- What is the canonical event envelope?
- What are required IDs and correlation fields?
- What are the event names?

Candidate events:

```text
DiscoveryCase.Opened
DiscoveryCase.Scoped
DiscoveryCase.Routed
PDR.Finalized
ProductIntent.Created
ProductIntent.Accepted
ProductIntent.Parked
ProductIntent.ReadyForSpecification
PSD.DraftCreated
PSD.Approved
WorkOrder.Created
WorkOrder.Started
WorkOrder.Completed
Transition.Requested
GovernanceCase.Opened
Governance.Approved
Governance.Rejected
Evidence.Attached
Release.Published
ProductIntent.Renewed
```

- Which module emits each event?
- Which module consumes each event?
- Which events are persisted?
- Which events are visible in audit history?
- Which events can be replayed?

---

## 11. Orchestrator rules

- What rules create Work Orders from orchestration item events?
- Are rules hardcoded, scenario-authored, or configurable?
- Where are rules stored?
- What is the first Orchestrator rule implemented?
- How does Orchestrator determine the next Workspace?
- How does Orchestrator enforce parallel fan-out?
- How does Orchestrator handle Work Order failure?
- How does Orchestrator handle governance rejection?
- How does Orchestrator reopen or return Product Intent to Product Specification?

Candidate rule examples:

```text
ProductIntent.Accepted
  -> create WorkOrder(Build, Product Specification, RefineIntentToPSD)

PSD.Approved
  -> create WorkOrder(Build, UX Design, DesignForIntent)
  -> create WorkOrder(Build, Development, ImplementIntent)
  -> create WorkOrder(Build, QA, PrepareVerification)

WorkOrder.Completed(QA.VerifyProductIntent)
  -> create WorkOrder(Build, Release, PublishProductDelivery)
```

---

## 12. Repository and storage contracts

- Which repository stores each Phase 1 entity?
- Which service owns persistence for each entity?
- Which records are Git-backed?
- Which records are database-backed?
- Which records are external-system references?
- What is the minimal schema for:
  - Discovery Case
  - PDR
  - Product Intent
  - PSD metadata
  - Work Order
  - Task
  - Scenario
  - Governance Ritual / Governance Enforcement
  - Evidence
  - Workspace Session
- What ID format should each entity use?
- What search/indexing is required?
- What cross-reference integrity must be enforced?
- How is history/versioning represented?
- How is Confluence/Git sync related to repository services, if at all?

---

## 13. API surface

- What APIs must exist for Phase 1?
- Which module owns each API?
- Which APIs are internal only?
- Which APIs are called by Web App?
- Which APIs are called by IDE?
- Which APIs are called by Orchestrator?
- Which APIs are called by Work Order Runtime?

Candidate API groups:

```text
DiscoveryCase API
PDR API
ProductIntent API
WorkOrder API
Scenario API
Governance API
Evidence API
Repository API
WorkspaceSession API
Traceability API
```

- What are the request/response schemas?
- What authorization applies?
- What idempotency is required?
- What pagination/filtering is required?

---

## 14. UI-to-module contracts

- Which module APIs does PI Console call?
- Which module APIs does Workspaces Console call?
- Which module APIs does Track Console call?
- Which module APIs does Governance Console call?
- Which module APIs does Repositories & Tools call?
- Which actions are available in Phase 1 UI?
- Which views are read-only in Phase 1?
- Which UI states must display loading, partial, failed, or stale data?

PI Console likely needs:

```text
listDiscoveryCases()
createDiscoveryCase()
listPDRs()
finalizePDR()
createProductIntent()
listProductIntents()
transitionProductIntent()
listTraceabilityMap()
```

Workspaces Console likely needs:

```text
listWorkOrders(workspace, parentItem)
createWorkspaceSession()
attachWorkOrderToSession()
completeTask()
```

---

## 15. Governance MVP

- Which Phase 1 transitions are governed?
- Which are blocking vs advisory?
- What evidence is required for each transition?
- What is the minimum Governance Ritual schema?
- What is the minimum Governance Enforcement schema?
- Which Governance Policies are implemented in Phase 1?
- Which Ritual Definitions are implemented in Phase 1?
- Which cadences are required versus deferred?
- Which reports/dashboards are required as ritual inputs?
- Who can approve or reject?
- What happens on rejection?
- How are policy exceptions handled?
- Where are governance verdicts stored?
- How are governance verdicts shown in UI?
- Which Governance Scenarios are required in Phase 1?
- What audit trail is mandatory?
- Are Risk Register, Debt Register, Compliance Register, and Kudos Register in scope?
- How are Governance Findings stored?
- Which governance outputs trigger Evolve Cases?
- How are recognitions / Kudos captured and surfaced?

Candidate governed transitions:

```text
PDR.Finalized
ProductIntent.Accepted
PSD.Approved
ProductIntent.Specified
ProductIntent.ReadyForRelease
Release.Published
```

---

## 16. Workspace Runtime and IDE contracts

- What is the minimum Workspace Session lifecycle?
- How is a Session created?
- How is a Work Order attached to a Session?
- Can Work Orders be moved between Sessions?
- What context is injected into a Session?
- What skills are injected?
- How does IDE show Human Tasks?
- How does IDE show parent orchestration item context?
- How does IDE submit outputs or completion?
- How does Runtime notify Orchestrator?

---

## 17. Traceability and maps

- What graph shape is required for Phase 1?
- Which relationships are mandatory?
- Which traceability maps are Phase 1?
- Is Executive Strategy Map in scope?
- Is Product Manager Intent Map in scope?
- Is Delivery Execution Map in scope?
- Is Governance Evidence Map in scope?
- Is Release Renewal Map in scope?
- What graph API powers them?
- Are maps computed on demand or materialized?

---

## 18. Security, access, and tenancy

- Who can create Discovery Cases?
- Who can finalize PDRs?
- Who can create Product Intents?
- Who can transition Product Intent state?
- Who can create Work Orders?
- Who can approve governance transitions?
- What tenant/workshop/workbench boundaries apply?
- How are customer-bank users scoped?
- How do agent permissions differ from human permissions?
- What audit records are required for permissioned actions?

---

## 19. Observability and audit

- What logs are required per module?
- What metrics are required for Orchestrator?
- What metrics are required for Work Order Runtime?
- What metrics are required for Web App usage?
- What audit trail is required for:
  - Discovery Case
  - PDR
  - Product Intent
  - Work Order
  - Governance Ritual / Governance Enforcement
  - Evidence
- What dashboards are needed for Phase 1?
- How do we trace one Product Intent from creation to delivery?

---

## 20. Open product decisions

- Should Discovery Support Product Intent be allowed before PDR, and what lightweight authorization is required?
- Are Evolution and Delivery Product Intent separate purposes or one value?
- Is Customer Release Intent in Phase 1 read-only context or actively managed?
- Are Run/Win/Evolve orchestration items implemented or only named for future compatibility?
- Are Governance Ritual and Governance Enforcement first-class persisted entities in Phase 1?
- What is the minimum traceability map set?
- What does "ready for Phase 1 engineering" mean for each module?
