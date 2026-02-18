# API Module

**Model:** Definition Model
**Dimension / Track:** Dimension 6: Ecosystem & Extensibility (Platform)
**Owner:** Product Management (API/Platform), Engineering

## Definition

An API Module is a named, versioned, protocol-agnostic programmatic surface designed for external consumption. It encompasses all delivery mechanisms — REST, gRPC, batch/file (SFTP), event streams (Kafka), webhooks, GraphQL — as transport variations within a single module. Its identity is defined by the use case it serves and the contract it commits to, not the wire protocol.

An API Module is structurally a Dim 8 Module — it participates in the Product → Module → Capability → Feature hierarchy, has a bounded context, archetype classification, Dim 5 internals, and Build Track versioning. What makes it a Dim 6 module is: (1) its purpose is externally-facing extensibility, (2) its capabilities are often compositional — curating capabilities from other Dim 8 modules for a use-case-oriented surface, and (3) it carries Dim 6-specific concerns (Developer Personas, Programmatic Personas, API contracts, SLOs).

## Purpose

Captures a deliberate product strategy to make capabilities externally consumable. An API Module exists only when there is a demand-driven decision to serve well-understood external use cases — not as a byproduct of distributed architecture.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | Text | Module name (e.g., "Cross-Border Payments API") |
| Purpose | Text | Use case this API surface serves |
| Supported Protocols | List | Delivery mechanisms available (REST, gRPC, Kafka, SFTP, Webhook, GraphQL) |
| Version | Text | Current version (follows API Compatibility Contract) |
| Composes From | Reference(s) | Dim 8 Module(s) whose capabilities this module curates |
| Default SLOs | Structured | Module-level baseline SLOs (operations may override) |
| Authentication | Text | Auth mechanism(s) (OAuth 2.0, API Key, mTLS) |
| Rate Limiting | Text | Default rate limits and tiering |
| Documentation | Reference | Link to developer documentation |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Is a | Module (Dim 8) | Structurally a Dim 8 Module with Dim 6 concerns |
| Composes from | Module(s) (Dim 8) | Curates capabilities from underlying modules |
| Serves | Developer Persona (Dim 6) | Designed for these developers |
| Serves | Programmatic User Persona (Dim 6) | Consumed by these systems at runtime |
| Contains | API Operation(s) (Dim 6) | Named contractual operations within this module |
| Governed by | API Compatibility Contract (Dim 6) | Versioning and stability commitments |
| Wrapped by | SDK/Library Module (Dim 6) | Language-specific clients wrap this surface |
| Bridged by | Integration Module (Dim 6) | Connectors may use this module's operations |
| Assessed by | Win Review (Track 4) | API adoption and health reviewed |
| Monitored by | System Monitoring (Track 3) | Runtime performance monitored |

## Example

**"Cross-Border Payments API"** — Exposes cross-border payment processing capabilities for external consumption. Composes capabilities from Payment Processing Module, FX Rate Module, and Compliance Screening Module. Supported Protocols: REST (synchronous operations), Kafka (command submission and event streaming), SFTP (batch file exchange), Webhooks (settlement notifications). Contains operations: Create Payment (Command), Get Rate Quote (Query), payment.settled (Event), Upload Payment File (Batch), Daily Settlement Report (Batch). Default SLOs: 99.95% availability, p99 < 1s for synchronous operations. Authentication: OAuth 2.0 with API Key fallback. Rate Limit: 10K requests/minute (Standard tier), 100K/minute (Enterprise tier).

---
