# Integration Epic

**Model:** Work Model
**Track:** Build
**Owner:** Tech Lead, Integration Architect

## Definition

A large body of cross-System integration work that emerges during Build Track planning (Release Planning). Integration Epics are distinct from PSD-derived Epics: where regular Epics deliver functional capability within a Module, Integration Epics deliver **verified interoperability between Systems** that implement different Modules (or different parts of the same Module).

Integration Epics are identified during Release Planning when the planner recognizes that PSD-derived Epics in different Modules require their Systems to communicate — through APIs, events, shared data, or coordinated workflows. The Integration Epic references the PSD-derived Epic(s) and Story(ies) it integrates.

> **Why separate from regular Epics?** Integration work has different characteristics: it spans multiple Systems (Technical) that may belong to different Modules (Structural), it requires Interaction Flows (Technical) to be validated end-to-end, and it produces integration contracts and integration test suites rather than feature code. Conflating integration work into feature Epics hides the cross-cutting nature of the work and makes it invisible to planning. See DR-026.

## Purpose

Makes cross-System integration work explicit and plannable. Without Integration Epics:
- Integration work hides inside feature Epics — it surfaces late as "integration issues" that delay releases
- Cross-team coordination has no structured work entity — integration becomes ad hoc
- Interaction Flows (Technical) have no work entity that validates them end-to-end
- System Version assembly and Product Version certification have no traceable path from integration work

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Descriptive title (e.g., "Integrate Payments↔FX Rate Locking Flow") |
| Epics Integrated | List of References (Build) | PSD-derived Epics being integrated |
| Stories Integrated | List of References (Build) | Specific Stories from those Epics that require integration |
| Interaction Flow | Reference (Technical) | Which Interaction Flow(s) this Integration Epic validates |
| Systems Involved | List of References (Technical) | Systems that must interoperate |
| Integration Contracts | Text | API schemas, event schemas, data contracts to be verified |
| Acceptance Criteria | Text | What must be true for the integration to be considered verified |
| Target Milestone | Reference (Build) | Which Milestone this Integration Epic targets |

## Statuses

| Status | Description |
|---|---|
| Identified | Integration need recognized during Release Planning |
| Defined | Integration contracts and acceptance criteria drafted |
| In Progress | Integration Stories and Technical Tasks are underway |
| Verified | All integration tests pass; integration contracts validated |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| References | Epic(s) (Build) | Integration Epic references the PSD-derived Epics it integrates |
| References | Story(ies) (Build) | Integration Epic references specific Stories requiring integration |
| Validates | Interaction Flow(s) (Technical) | Integration Epic validates end-to-end Interaction Flows |
| Spans | System(s) (Technical) | Integration Epic spans multiple Systems |
| Contains | Integration Story(ies) (Build) | Integration Epic contains Integration Stories |
| Identified by | Release Planning Task (Build) | Integration Epics are identified during Release Planning |
| Targeted by | Milestone (Build) | Integration Epic may be gated by a Milestone |
| Contributes to | System Version(s) (Build) | Integration work verifies cross-System contracts within and across Systems |
| Contributes to | Product Version (Build) | Cross-System Integration Epics contribute to Product Version certification |

## Examples

| Integration Epic | Epics Integrated | Systems Involved | Interaction Flow | Status |
|---|---|---|---|---|
| "Integrate Payments↔FX Rate Locking" | FX Rate Locking Epic, Payment Execution Epic | payments-service, fx-service | "Cross-Border Payment with FX Lock" | In Progress |
| "Integrate Payments↔Compliance Screening" | Payment Execution Epic, LATAM OFAC Epic | payments-service, compliance-service | "Payment Screening Flow" | Defined |
| "Integrate Settlement↔Bank Adapter" | Settlement Reconciliation Epic | settlement-service, bank-adapter | "Bank Settlement File Generation" | Identified |

---
