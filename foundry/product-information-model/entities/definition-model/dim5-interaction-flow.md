# Interaction Flow

**Model:** Definition Model
**Dimension:** Dimension 5: The Technical & Architectural Dimension (Engineering)
**Owner:** Tech Leads, Architects

## Definition

How Systems communicate to fulfill Value Streams (Dim 8). The technical realization of the functional flow — where Value Stream captures the business narrative ("Cross-Border Payout Processing traverses Invoice → FX → Compliance → Payment → Settlement"), Interaction Flow captures the technical narrative ("payment request enters via REST at payments-api → FX rate fetched via gRPC from fx-service → compliance check via async Kafka event → settlement confirmation via Kafka event"). Interaction Flows anchor sequence diagrams and data flow diagrams — the entity defines the flow; the diagram is a visualization artifact.

> **Renamed from Interaction Pattern:** "Pattern" connotes an abstract, reusable template — something you *could* apply. "Flow" conveys concrete, committed motion — what *actually happens* when a value stream is executed. The entity's structure (ordered steps, protocols, timeouts, error handling) describes sequential execution, not abstract patterns. Value Stream (Dim 8) describes the functional flow; Interaction Flow (Dim 5) describes the technical flow. Same motion, different lens.

## Purpose

Captures the technical communication architecture between Systems. Without Interaction Flows:
- Value Streams (Dim 8) describe functional flows but not how they are technically realized
- Integration architecture is implicit — sync vs. async, protocol choices, error handling strategies are undocumented
- Sequence diagrams and data flow diagrams have no Definition Model anchor — they exist as tribal knowledge or ad-hoc wiki pages
- Cross-system failure modes are invisible — "what happens when compliance-service doesn't respond within 5s?" has no structured answer

**Value Stream (Dim 8) vs. Interaction Flow (Dim 5):** Same flow, different lens. Value Stream is the functional narrative (for PMs — which capabilities are exercised in what order). Interaction Flow is the technical narrative (for architects — which systems communicate via what protocols with what error handling). A single Value Stream may have multiple Interaction Flows (e.g., a sync path for real-time and a batch path for bulk processing).

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Flow name (e.g., "Cross-Border Payout Processing Flow," "Batch Settlement Reconciliation") |
| Realizes | List of References (Dim 8) | Which Value Stream(s) this flow realizes (technical counterpart) |
| Participating Systems | Ordered List of References (Dim 5) | Which Systems participate, in sequence |
| Steps | Structured List | Each step: source System → target System, integration style, protocol, data format, timeout/SLA |
| Integration Style | Enum per step | `Sync request-reply` / `Async event` / `Async request-reply` / `Batch` / `RPC` / `Streaming` |
| Error Handling Strategy | Text | Retry policy, circuit breaker, compensation/saga, dead-letter queue, fallback behavior |
| Data Format | Enum | `JSON` / `Protobuf` / `Avro` / `CSV` / `XML` / `ISO20022` / `Mixed` |
| External Dependencies | List of References (Dim 5) | Dependencies involved in this flow (e.g., external APIs, bank networks) |

## Statuses

| Status | Description |
|---|---|
| Designed | Flow has been defined (ADR produced) but not yet implemented |
| Active | Flow is in production use |
| Deprecated | Flow is being replaced (new flow designed, migration in progress) |
| Retired | Flow has been fully replaced |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Realizes | Value Stream(s) (Dim 8) | Interaction Flow is the technical realization of a functional Value Stream |
| Involves | System(s) (Dim 5) | Systems participate in this flow |
| Uses | Dependency(ies) (Dim 5) | External dependencies involved in the flow |
| Decisions | ADR(s) (Dim 5) | Flow design decisions are recorded as ADRs |
| Context | Architecture Model (Dim 5) | Architecture Model's style determines available flow types |
| Related to | Operational Target(s) (Dim 7) | End-to-end latency/availability targets may apply to the entire flow |
| Realized by | Integration Epic (Track 2) | Integration Epics validate Interaction Flows end-to-end during build work |

## Examples

**"Cross-Border Payout Processing Flow" (real-time path)**
- Realizes: "Cross-Border Payout Processing" (Dim 8 Value Stream)
- Participating Systems: merchant-portal → payments-api → fx-service → compliance-service → bank-adapter → settlement-service
- Steps:
  1. merchant-portal → payments-api: REST POST /payments (sync, JSON, timeout 10s)
  2. payments-api → fx-service: gRPC GetRate (sync, Protobuf, timeout 500ms)
  3. payments-api → compliance-service: Kafka event `payment.screening.requested` (async, Avro, expect response within 5s)
  4. compliance-service → OFAC Screening Service (Dependency): REST POST /screen (sync, JSON, timeout 3s, circuit breaker)
  5. payments-api → bank-adapter: REST POST /execute (sync, JSON, timeout 30s, retry 2x with exponential backoff)
  6. bank-adapter → settlement-service: Kafka event `payment.executed` (async, Avro, at-least-once delivery)
- Error Handling: Compensating transaction on bank-adapter failure (reverse FX lock); dead-letter queue for compliance timeout (manual review); circuit breaker on OFAC with 30s open window
- Data Format: Mixed (JSON at boundaries, Protobuf internal, Avro for Kafka)

**"Batch Settlement Reconciliation" (batch path)**
- Realizes: "Cross-Border Payout Processing" (Dim 8 Value Stream — settlement reconciliation segment)
- Participating Systems: bank-adapter → settlement-service → analytics-service
- Steps:
  1. bank-adapter: SFTP pull settlement files from bank (batch, CSV/MT940, daily at 02:00 UTC)
  2. bank-adapter → settlement-service: Kafka event `settlement.file.received` (async, Avro)
  3. settlement-service: reconcile against payment records (internal processing)
  4. settlement-service → analytics-service: Kafka event `settlement.reconciled` (async, Avro)
- Error Handling: Unmatched settlements queued for manual review; file parsing failures logged and alerted
- Data Format: CSV/MT940 (inbound from bank), Avro (internal Kafka)

---
