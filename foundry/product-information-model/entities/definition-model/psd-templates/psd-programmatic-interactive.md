# Integration Capability Template

**Type:** Capability Template
**Model:** Definition Model — Dimension 1 (PSD)
**Applies to:** Capabilities consumed programmatically by external systems, customer applications, or partner integrations — REST APIs, event streams, webhooks, batch/file exchange.
**Used by:** Product Manager (PM-authored zone of the PSD — Product Draft phase)

---

## Purpose

This template guides a PM in specifying an **Integration Capability** within a PSD. An Integration Capability is one where the primary consumer is a system or application (not a human) — the capability is accessed programmatically via an API, event, or file interface.

The PM specifies the business intent of the integration — what the capability does, who consumes it, and what commitments it carries. The Architect maps to specific Systems and Components in the Technical Review phase.

---

## Capability Specification Fields (PM-authored)

### Capability Identity

| Field | Type | Guidance |
|---|---|---|
| Capability Name | String | What integration does this capability enable? e.g., "Payment Initiation API" |
| Capability Template | Enum | `Integration` (selected) |
| Maturity (target) | Enum | `Alpha` / `Beta` / `Gamma` |
| Lifecycle Stage (target) | Enum | `Planned → Available` or `Available → Deprecated` |

### Integration Specification

| Field | Type | Guidance |
|---|---|---|
| Consumer Persona(s) | References (Ecosystem) | Who/what consumes this capability? Reference Ecosystem Developer Persona or Programmatic User Persona. |
| Consumer Use Case | Text | What does the consumer do with this capability? Why do they need it? |
| Interface Type | Enum | REST API / gRPC / Event Stream (Kafka/SNS) / Webhook / Batch File (SFTP/S3) / GraphQL / Other |
| API Intent | Text | What operations does this capability need to support? (e.g., "initiate a payment, check payment status, cancel a pending payment"). Do NOT specify endpoints or payloads — that is a Build Track artifact. |
| Contract Shape | Text | High-level shape of the contract: key input fields and output fields (business terms, not technical types). e.g., "Takes: payer, payee, amount, currency, reference. Returns: payment ID, status, estimated settlement date." |
| SLO Targets | Text | Latency P95/P99 targets, availability SLA, throughput per second/per tenant |
| Backward Compatibility | Text | Is this a new contract, an extension of existing, or a breaking change? What is the versioning strategy? |
| Error Handling Expectations | Text | Key error scenarios the consumer must handle; business-level error vocabulary (not HTTP codes) |

### Capability Acceptance Criteria (PM-authored)

| Criterion | Type | Guidance |
|---|---|---|
| Contract Completeness | Text | All specified operations are available and return the specified outputs |
| SLO Achievement | Text | Meets specified latency, availability, and throughput targets |
| Backward Compatibility | Text | Existing consumers are not broken (for extensions/refinements) |
| Error Clarity | Text | Error responses are clear and actionable for the consuming developer |
| Documentation | Text | API reference documentation available before GA |

---

## Notes for the Architect (Technical Review phase)

The Architect maps this Integration Capability to Systems and Components in Section 5 of the PSD. Common System contributions for Integration Capabilities:

- An **API Service** Component implements the synchronous endpoints
- A **Gateway** Component may handle routing, authentication, rate limiting
- An **Integration Adapter** Component connects to external partner systems
- An **Event-Driven Worker** Component handles async processing behind webhook notifications

---

## Example

**Capability:** "Payment Initiation API"
**Module:** Payments Module (Record)
**Template:** Integration

| Field | Value |
|---|---|
| Consumer Persona | Programmatic User Persona: Customer ERP System (Ecosystem) |
| Consumer Use Case | Customer's ERP submits cross-border payment instructions in bulk via API; ERP polls for status updates |
| Interface Type | REST API |
| API Intent | Initiate payment, batch-initiate payments, get payment status, cancel pending payment, list payments by date range |
| Contract Shape | Input: payer account, payee bank details, amount, currency, reference. Output: payment ID, status (Initiated/Processing/Cleared/Settled/Failed), estimated settlement date, FX rate applied |
| SLO Targets | P95 < 200ms (initiate), P99 < 500ms; 99.95% availability; 1000 req/min per tenant |
| Backward Compatibility | New capability — no existing contract |
