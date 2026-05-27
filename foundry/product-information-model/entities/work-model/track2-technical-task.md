# Technical Task

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction)
**Owner:** Developers

## Definition

A granular engineering step scoped to a specific System (Dim 5) and optionally a Component (Dim 5). Technical Tasks represent the actual developer-level work: writing code, writing tests, configuring infrastructure, implementing contracts, fixing defects, or producing bounded spike evidence. Build Track Technical Tasks serve Stories, Integration Stories, or Discovery Support / Technical Validation Product Intents. See DR-026 and DR-039.

> **Technical Task is a per-track concept.** Each engineering track has its own Technical Tasks with the same entity structure but distinct track ownership. The Build Track's Technical Tasks serve Stories and Integration Stories (product engineering). The Run Track has its own Technical Tasks serving Run Stories (operational engineering). The Win Track may have Technical Tasks in the future (win engineering automation). This avoids cross-track borrowing and keeps ownership clean.

> **Sprint bypass for P0 Bugs.** Technical Tasks serving P0 Bugs inherit sprint-bypass priority — they are allocated immediately outside normal sprint capacity. No structural field change is needed; the urgency is derived from the parent Bug's P0 priority. The resulting System Version may use the Emergency gate profile. See DR-031 D1.

**System/Component scope, not Module scope:** Technical Tasks speak the System language ("Implement gRPC endpoint in fx-service," "Add Kafka consumer in payments-service"). They are the bridge from functional intent (Stories, Module-scoped) to technical implementation (Systems, Dim 5). A single Story may spawn Technical Tasks in multiple Systems because the Module-to-System mapping is many-to-many. See DR-026.

## Purpose

Captures the actual engineering work that produces System Versions. Without Technical Tasks:
- Stories have no engineering decomposition — "lock FX rate for 24 hours" has no implementation plan
- System-level work assignment is impossible — developers work on Systems, not Modules
- System Versions have no traceability to the work they contain
- The functional-to-technical boundary is invisible

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Descriptive title (e.g., "Implement gRPC GetRate endpoint in fx-service") |
| Product Intent | Reference (Dim 1) | Parent Product Intent that authorizes this work |
| Story | Reference (Track 2) | Parent Story (or Integration Story) this Task implements |
| System | Reference (Dim 5) | Which System this Task is implemented in |
| Component | Reference (Dim 5) | Which Component within the System (optional, for complex Systems) |
| Task Type | Enum | `Code` / `Test` / `Config` / `Documentation` / `Spike` |
| Effort Estimate | String | Time estimate (hours or story points) |
| Assignee | String | Developer assigned |
| Branch / PR | String | Source control reference |

## Statuses

| Status | Description |
|---|---|
| To Do | Task is defined but not yet started |
| In Progress | Developer is actively working on this Task |
| In Review | Code is written, awaiting review |
| Done | Task is complete, code merged, tests passing |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Implements | Story (Track 2) | Technical Task implements a Story |
| Implements | Integration Story (Track 2) | Technical Task implements an Integration Story |
| Authorized by | Product Intent (Dim 1) | Technical Task is subordinate to Product Intent orchestration |
| Scoped to | System (Dim 5) | Task is implemented within a specific System |
| Scoped to | Component (Dim 5) | Task may target a specific Component within the System (optional) |
| Included in | System Version (Track 2) | Completed Task is included in the next System Version |
| Belongs to | Epic (Track 2) | Task belongs to an Epic (via Story) |

## Examples

| Task | Type | Story | System | Component |
|---|---|---|---|---|
| "Implement gRPC GetRate endpoint" | Code | "Lock FX rate for 24 hours" | fx-service | FX Rate Calculator |
| "Add rate lock client call" | Code | "Lock FX rate for 24 hours" | payments-service | — |
| "Write integration test: rate lock flow" | Test | "Lock FX rate for 24 hours" | fx-service | — |
| "Add Kafka consumer for payment.screening.requested" | Code | "Add LATAM OFAC screening" | compliance-service | OFAC Screening Adapter |
| "Spike: evaluate bank-adapter batch throughput" | Spike | "Generate settlement files" | bank-adapter | Bank File Generator |

---
