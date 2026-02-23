# Component

**Model:** Definition Model
**Dimension:** Dimension 5: The Technical & Architectural Dimension (Engineering)
**Owner:** Tech Leads, Developers

## Definition

A significant architectural building block within a System — processing engines, adapters, rule evaluators, schedulers, queue consumers, gateways. Components appear in architecture diagrams and represent internally significant subsystems within a deployable unit. They are always contained by a System and transitively map to Dim 8 Modules through their parent System. Not code-level (not classes or functions) — architectural-level.

## Purpose

Captures the internal architecture of a System at a level that is meaningful for architectural comprehension without descending to code-level detail. Without Components:
- Systems are black boxes — "payments-service" exists but its internal architecture is invisible
- Capability-to-implementation mapping is coarse — "Real-Time FX Rate Locking" maps to fx-service but not to the specific calculator component within it
- Architecture diagrams lack anchoring entities within Systems

Components are optional — simple Systems with a single responsibility may not need Component-level decomposition. Components are warranted when a System has internally significant architectural boundaries (e.g., a processing engine, an adapter layer, a rules engine).

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Component name (e.g., "FX Rate Calculator," "OFAC Screening Adapter," "Payment State Machine") |
| Type | Enum | `Engine` / `Adapter` / `Calculator` / `Scheduler` / `Consumer` / `Gateway` / `Processor` / `Evaluator` / `Cache` / `Other` |
| Parent System | Reference (Dim 5) | Which System contains this Component |
| Technology Stack | String | When different from parent System (e.g., "embedded Python rules engine within Java service") |
| Responsibility | Text | What this Component does within the System |
| Capability Mapping | List of References (Dim 8) | Which Dim 8 Capability(ies) this Component implements or contributes to |

## Statuses

_Inherits from parent System — Components do not have an independent lifecycle._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Belongs to | System (Dim 5) | Component is contained by a System |
| Maps to | Capability(ies) (Dim 8) | Component may implement or contribute to specific Capabilities |
| Decisions | ADR(s) (Dim 5) | Architectural decisions affecting this Component are recorded as ADRs |

## Examples

| Component | Type | Parent System | Responsibility | Maps to (Dim 8) |
|---|---|---|---|---|
| FX Rate Calculator | Calculator | fx-service | Fetches rates from multiple providers, applies margin rules, caches for TTL | Real-Time FX Rate Locking (Capability) |
| OFAC Screening Adapter | Adapter | compliance-service | Translates payment data to OFAC screening format, manages screening provider API | OFAC Compliance Screening (Capability) |
| Payment State Machine | Engine | payments-service | Manages payment lifecycle state transitions (Initiated → Processing → Cleared → Settled) | Cross-Border B2B Payments (Capability) |
| Bank File Generator | Processor | bank-adapter | Generates bank-specific file formats (MT103, ISO20022) for batch settlement | Settlement Processing (Capability) |
| Alert Router | Gateway | notification-service | Routes notifications to appropriate channels (email, SMS, webhook) based on rules | — (cross-cutting) |

---
