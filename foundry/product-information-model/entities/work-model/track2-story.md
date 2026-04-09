# Story

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction)
**Owner:** Tech Lead, Developers, QA

## Definition

A unit of work within an Epic, representing a functional increment within the Epic's Module (Dim 8). Stories describe *what* needs to be built in Module/Capability language — not necessarily user-facing. A Story may be technical ("Set up Kafka consumer for payment events") or user-facing ("Lock FX rate for 24 hours"). Stories are implemented by Technical Tasks scoped to Systems and Components (Dim 5).

> **Renamed from User Story:** Not all Stories are written from a user's perspective. Technical stories, infrastructure stories, and data migration stories are equally valid. "Story" is the more general term. The Story inherits its Module scope from its parent Epic.

## Purpose

Translates Epics into deliverable increments of functionality within a Module. Without Stories:
- Epics are too large to plan and track at sprint level
- The functional-to-technical bridge is missing — Stories express Module-level intent; Technical Tasks express System-level implementation
- Sprint planning has no right-sized work unit

**Module vs. System scoping:** Stories speak the Module language ("implement rate locking capability"). Their child Technical Tasks speak the System language ("add gRPC endpoint in fx-service," "add rate lock client in payments-service"). A single Story may spawn Technical Tasks in multiple Systems because the Module-to-System mapping is many-to-many.

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Descriptive title |
| Epic | Reference (Track 2) | Parent Epic this Story belongs to |
| Module | Reference (Dim 8) | Inherited from parent Epic — the Module this Story advances |
| Capability | Reference (Dim 8) | Which Capability this Story contributes to (optional, more specific than Module) |
| Description | Text | What needs to be built — acceptance criteria, functional requirements |
| Story Type | Enum | `Functional` / `Technical` / `Enablement` |
| Effort Estimate | String | Story points or time estimate |
| Priority | Enum | `Must Have` / `Should Have` / `Could Have` |
| Iteration | Reference (Track 2) | Which sprint/iteration this Story is assigned to |

## Statuses

| Status | Description |
|---|---|
| Defined | Story is written with acceptance criteria |
| Ready | Story is refined, estimated, and ready for sprint assignment |
| In Progress | Story's Technical Tasks are being worked on |
| In Review | Story implementation is complete, under review |
| Done | All acceptance criteria met, all Technical Tasks complete |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Belongs to | Epic (Track 2) | Story is a unit within an Epic |
| Scoped to | Module (Dim 8) | Story represents work within a Module (inherited from Epic) |
| Maps to | Capability (Dim 8) | Story may map to a specific Capability |
| Implemented by | Technical Task(s) (Track 2) | Story is implemented by Technical Tasks in System(s) |
| Assigned to | Iteration (Track 2) | Story is assigned to a sprint via Iteration Planning |
| May contain | Bug(s) (Track 2) | Bugs may be discovered during Story implementation |

## Examples

| Story | Type | Epic | Module | Technical Tasks (Systems) |
|---|---|---|---|---|
| "Lock FX rate for 24 hours" | Functional | Build Real-Time FX Rate Locking | FX Module | TT1: gRPC endpoint in fx-service, TT2: rate lock client in payments-service, TT3: rate cache TTL in fx-service (Redis) |
| "Set up Kafka consumer for payment events" | Technical | Build Cross-Border API | Payments Module | TT1: Kafka consumer config in payments-service, TT2: event schema definition in payments-service |
| "Generate bank-specific settlement files" | Functional | Build Settlement Processing | Settlement Module | TT1: MT103 generator in bank-adapter, TT2: ISO20022 generator in bank-adapter |

---
