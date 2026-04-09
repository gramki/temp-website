# Win Case

**Model:** Work Model
**Track:** Track 4: The Win Track (Value Realization)
**Category:** Reactive
**Owner:** Customer Success, Sales, Support

## Definition

Reactive, customer-initiated work of Win Teams — queries, requests, complaints, and escalations initiated by customers and prospects. Win Cases capture the responsive dimension of Win Track work: things the customer brings to the vendor, as opposed to proactive engagement the vendor initiates.

> **Always originates from an FIR.** Every Win Case is a sub-item of a First Information Report (FIR). Win Cases cannot be created independently — the FIR is the universal intake envelope that ensures complete traceability from initial report through resolution. Even when a Win team member discovers a complaint during a QBR or proactive engagement, they log an FIR first and route the Win Case from it. See DR-032.

**Four Win Case types:**

1. **Query** — Customer or prospect seeking information (e.g., "What currencies do you support for LATAM corridors?")
2. **Service Request** — Customer asking for a specific action (e.g., "Please add a new approver to our payout workflow")
3. **Complaint** — Customer expressing dissatisfaction with a product capability or commercial process. Complaints test Service Commitments from Dim 3 — they reveal whether Customer Promises are being met.
4. **Escalation** — Issue requiring elevated attention due to severity, customer importance, or unresolved prior cases.

**Distinction from Run Track:** Win Cases are customer-facing and commercial. Run Track entities (Incident, Change Request) are infrastructure- and system-facing. A system outage is a Run Track Incident; a customer calling to ask about it is a Win Case.

## Purpose

Makes the reactive, responsive work of Win Teams visible in the model. Without Win Cases:
- Customer-initiated interactions have no structured representation
- Complaint patterns that test Service Commitments are invisible to product strategy
- There is no mechanism to assess cost-to-serve at the case level
- The reactive workload of Win Teams cannot be measured or optimized
- The connection between case patterns and Win Reviews is missing

## Fields

| Field | Type | Description |
|---|---|---|
| ID | String | Unique identifier for the case |
| Title | String | Brief description of the case |
| Type | Enum | `Query` / `Service Request` / `Complaint` / `Escalation` |
| Originating FIR | Reference (Track 4) | **Required.** The FIR from which this Win Case was routed. Every Win Case is a sub-item of an FIR (DR-032). |
| Customer / Prospect | Reference (ESR) | Customer or prospect who initiated the case — references External Stakeholder Registry |
| Customer Segment | Reference (Dim 3) | Which segment the case pertains to |
| Priority | Enum | `Critical` / `High` / `Medium` / `Low` |
| Description | Text | Detailed description of the customer's query, request, complaint, or escalation |
| Assigned Win Stakeholder | Reference (Dim 2) | Which Win Stakeholder is handling this case |
| CRM Reference | String (external) | Link to the case in the external CRM system |
| Resolution | Text | How the case was resolved |
| SLA Target | Duration | The target resolution time based on case type, priority, and segment |
| SLA Actual | Duration | The actual resolution time |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| New | Case has been created but not yet assessed |
| Triaged | Case has been assessed, prioritized, and assigned |
| In Progress | Case is being actively worked on |
| Resolved | Case has been resolved; awaiting customer confirmation |
| Closed | Case is fully closed; customer has confirmed resolution or closure period elapsed |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Scoped to | Customer Segment (Dim 3) | Win Case pertains to a specific segment |
| Assigned to | Win Stakeholder (Dim 2) | Win Case is handled by a Win Stakeholder |
| Tests | Service Commitment / Customer Promise (Dim 3) | Complaints test whether Service Commitments are being met |
| Measured by | Business KPI (Dim 2) | Win Case volume and resolution contribute to Cost-to-Serve KPIs |
| Assessed by | Win Review (Track 4) | Case patterns are assessed by Win Reviews (Case Pattern Review type) |
| May generate | Feedback (Track 4) | Patterns or individual cases may produce Feedback that enters the Signal pipeline |
| References | API Operation (Dim 6) | Cases may relate to specific API operations (SLO breaches, contract issues) |
| May correspond to | Incident (Track 3, artifact) | A Win Case Complaint about service degradation may have a corresponding Incident record in the Run Track — the Win Case is customer-facing, the Incident is system-facing |
| Originates from | FIR (Track 4) | Every Win Case is a sub-item of an FIR — the universal intake envelope (DR-032) |
| May produce | Bug (Track 2) | Complaints/escalations may reveal product defects (provenance: Win) |

## Examples

| Type | Title | Customer | Segment | Priority | Assigned To |
|---|---|---|---|---|---|
| Query | "What currencies are supported for LATAM corridors?" | Fintech Corp | LATAM Enterprise | Low | Pre-Sales Engineer |
| Service Request | "Add new approver to our multi-sig payout workflow" | Banco Nacional | LATAM Enterprise | Medium | CS Manager |
| Complaint | "FX rate-lock expired during our approval flow — we lost $12K" | GlobalPay SA | LATAM Enterprise | Critical | CS Manager |
| Complaint | "Create Payment API p99 latency exceeded 2s for 6 hours — breached SLO" | API Consumer (Enterprise) | LATAM Enterprise | Critical | CS Manager |
| Escalation | "Third complaint about FX rate-lock — requesting VP-level review" | GlobalPay SA | LATAM Enterprise | Critical | VP Customer Success |
