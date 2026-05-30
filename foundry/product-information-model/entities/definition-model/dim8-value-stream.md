# Value Stream

**Model:** Definition Model
**Dimension:** Structural
**Owner:** Product Management, Enterprise Architecture

## Definition

An end-to-end sequence of activities — crossing multiple modules and capabilities — that delivers a complete unit of value to the customer. Value Streams represent *how value flows horizontally* across the product's vertical module structure (Product → Module → Capability → Feature).

## Purpose

Value Stream fills a critical gap in the structural model. The vertical decomposition (Product → Module → Capability → Feature) describes *what the product can do* but not *how it delivers end-to-end customer value*. Many customer outcomes require orchestrating activities across multiple modules — no single module "owns" the outcome. Value Stream captures this horizontal composition.

**Relationship to other structural entities:**
- **Capability** (Structural): What the product *can do* (a static ability). A point in the structure.
- **Value Stream** (Structural): How the product *delivers value* (a dynamic flow). A path through the structure.
- **User Journey** (User Experience): How the *user experiences* the flow (human perspective). A path through the UX.

Value Streams and User Journeys often align but are not identical — a Value Stream may include automated backend steps that no user ever sees, while a User Journey may include emotional/cognitive steps that are invisible to the system.

**Relationship to Value Proposition (Customer Value):**
- **Outcome-based Value Propositions** → map to Value Streams (because outcomes require end-to-end flows)
- **Ability-based Value Propositions** → map to Capabilities (because abilities are point promises)

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive name for the value stream |
| Trigger | Text | What initiates this value stream (user action, event, schedule) |
| Outcome | Text | What the customer/system achieves when the stream completes |
| Modules Traversed | List of References (Structural) | Which modules participate, in order |
| Capabilities Engaged | List of References (Structural) | Which capabilities are engaged at each step |
| Handoff Points | Text | Where work crosses module boundaries (critical for reliability) |
| End-to-End SLA | String | Expected total cycle time for the stream |
| _Additional fields deferred_ | | _Further fields (e.g., Criticality, Failure Modes, SLI Targets) are deferred to a future modeling session. Current structure is sufficient for initial Value Stream mapping (DR-035, D14)._ |

## Statuses

| Status | Description |
|---|---|
| Draft | Value stream is being mapped |
| Active | Value stream is operational |
| Optimizing | Value stream is being improved (e.g., bottleneck identified) |
| Retired | Value stream is no longer active |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Traverses | Module / Domain (Structural) | Value Stream traverses Module(s) |
| Engages | Capability (Structural) | Value Stream engages Capability(ies) at each step |
| Belongs to | Product (Structural) | Value Stream belongs to a Product |
| Mapped by | Value Proposition (Customer Value) | Outcome-based Value Propositions map to Value Stream(s) |
| Measured by | Customer Value Metric / ROI (Customer Value) | End-to-end flow metrics measure Value Stream performance |
| Experienced through | User Journey (User Experience) | Value Stream is experienced through User Journey(s) |
| Realized by | Interaction Flow(s) (Technical) | Value Stream's technical realization — how Systems communicate to fulfill this flow |
| Work Model | Modeling Task (Discovery) | Modeling Tasks map and refine Value Streams |

## Example

**"Cross-Border Payout Processing"**

| Step | Module | Capability | Activity |
|---|---|---|---|
| 1 | Invoice Module | Invoice Acceptance | Receive and validate payout instruction |
| 2 | FX Module | Automated Rate Locking | Lock FX rate for the transaction |
| 3 | Compliance Module | OFAC Screening | Screen beneficiary against sanctions lists |
| 4 | Payment Module | Payment Execution | Execute cross-border wire transfer |
| 5 | Settlement Module | Reconciliation | Match and reconcile settlement confirmation |

- **Trigger:** Approved payout instruction submitted via API or UI
- **Outcome:** Beneficiary receives funds, transaction reconciled in source system
- **End-to-End SLA:** <4 hours from instruction to reconciliation
- **Mapped by Value Proposition:** "Reduce cross-border payment cost by 60%"
