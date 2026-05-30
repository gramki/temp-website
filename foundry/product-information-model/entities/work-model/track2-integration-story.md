# Integration Story

**Model:** Work Model
**Track:** Build
**Owner:** Tech Lead, Developers

## Definition

A unit of integration work within an Integration Epic. Integration Stories describe cross-System integration tasks that verify interoperability between Systems — API contract validation, event flow verification, data consistency checks, and end-to-end scenario testing. Integration Stories produce **integration contracts** (API schemas, event schemas) and **integration test suites**.

Integration Stories are implemented by Technical Tasks, just like regular Stories. The difference is scope: a regular Story is Module-scoped (one Module, potentially multiple Systems); an Integration Story is explicitly cross-System-scoped (validating interoperability between Systems that may belong to different Modules).

## Purpose

Decomposes Integration Epics into plannable and trackable units of integration work. Without Integration Stories:
- Integration Epics are too large to plan at sprint level
- Integration contracts and test suites have no traceable origin — they appear as ad hoc artifacts
- Sprint planning cannot assign cross-System integration work to specific iterations

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Descriptive title (e.g., "Validate gRPC contract: payments-service → fx-service GetRate") |
| Integration Epic | Reference (Build) | Parent Integration Epic |
| Systems Under Test | List of References (Technical) | Systems being integrated by this Story |
| Integration Type | Enum | `API Contract` / `Event Flow` / `Data Consistency` / `End-to-End Scenario` |
| Contract Specification | Text | API schema, event schema, or data contract being validated |
| Test Suite | Text / Reference | Integration test suite produced by this Story |
| Acceptance Criteria | Text | What must pass for this integration to be considered verified |
| Iteration | Reference (Build) | Which sprint/iteration this Integration Story is assigned to |

## Statuses

| Status | Description |
|---|---|
| Defined | Integration Story is written with contract specifications and acceptance criteria |
| Ready | Story is refined and ready for sprint assignment |
| In Progress | Technical Tasks are being worked on |
| Verified | Integration tests pass; contract validated |
| Done | Integration is verified and results documented |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Belongs to | Integration Epic (Build) | Integration Story is a unit within an Integration Epic |
| Tests | System(s) (Technical) | Integration Story tests interoperability between Systems |
| Implemented by | Technical Task(s) (Build) | Integration Story is implemented by Technical Tasks |
| Produces | Integration Contract(s) | API schemas, event schemas validated by this Story |
| Produces | Integration Test Suite | Test suite verifying the integration |
| Contributes to | System Version(s) (Build) | Integration Stories verify contracts for System Version assembly |
| Contributes to | Product Version (Build) | Cross-System stories contribute to Product Version certification |
| Assigned to | Iteration (Build) | Integration Story is assigned to a sprint |

## Examples

| Integration Story | Type | Systems | Integration Epic | Status |
|---|---|---|---|---|
| "Validate gRPC contract: payments→fx GetRate" | API Contract | payments-service, fx-service | Payments↔FX Rate Locking | Verified |
| "Verify Kafka event flow: payment.created → compliance.screening.requested" | Event Flow | payments-service, compliance-service | Payments↔Compliance Screening | In Progress |
| "End-to-end: cross-border payment with FX lock and OFAC screening" | End-to-End Scenario | payments-service, fx-service, compliance-service | Payments↔FX + Payments↔Compliance | Defined |
| "Validate settlement file generation for MT103 partner banks" | Data Consistency | settlement-service, bank-adapter | Settlement↔Bank Adapter | Defined |

---
