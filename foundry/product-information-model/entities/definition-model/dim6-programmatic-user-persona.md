# Programmatic User Persona

**Model:** Definition Model
**Dimension:** Ecosystem
**Owner:** Product Management (API/Platform), Solutions Architecture

## Definition

A Programmatic User Persona is a named archetype representing an application or system that consumes the product's API at runtime. These are non-human consumers — a customer's ERP, a partner's middleware, a third-party application — with throughput needs, SLA dependencies, integration requirements, and error-handling expectations. They cannot be modeled as User Experience User Personas.

> **Role definition, not agent identity.** Programmatic User Persona is a **role** in the Definition Model describing an application archetype. Specific consuming applications (e.g., "Banco Itau's Treasury System") are tracked in the External Stakeholder Registry (ESR) as external parties with API access scope and SLA requirements. See DR-034.

## Purpose

Captures the runtime consumption profile of programmatic consumers, enabling SLO design, capacity planning, rate limit tiering, and integration testing strategy. Without Programmatic User Personas, API design optimizes for developer convenience (Ecosystem Developer Persona) but may miss runtime production requirements.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | Text | Archetype name (e.g., "Customer Treasury Management System," "Partner Card Platform") |
| System Type | Text | What the consuming system does |
| Owner | Enum | Customer / Partner / Third-Party / Internal |
| Integration Pattern | Text | How the system interacts (synchronous API calls, event consumption, batch file exchange, mixed) |
| Volume Profile | Text | Expected throughput (e.g., "50K transactions/day," "10 API calls/minute," "weekly batch of 100K records") |
| Latency Sensitivity | Enum | Real-time / Near-real-time / Batch-tolerant |
| Availability Dependency | Text | What happens if the product's API is unavailable (e.g., "partner's checkout flow fails," "batch retries next cycle") |
| SLA Requirements | Text | Contractual performance expectations |
| Error Handling Strategy | Text | How the system handles failures (retry, fallback, queue, manual intervention) |
| Primary API Module(s) | Reference(s) | Which API Modules it consumes |
| Primary Operations | Reference(s) | Which API Operations it depends on most critically |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Consumes | API Module (Ecosystem) | Runtime consumer of API surface |
| Consumes | API Operation (Ecosystem) | Depends on specific operations and their SLOs |
| Maps to | Customer Segment (Customer Value) | Owner of this system belongs to a segment |
| Informs | API Operation SLOs (Ecosystem) | Volume and latency profiles drive SLO targets |
| Assessed by | Win Review (Win) | Integration health assessed in reviews |
| Monitored by | Win Monitoring (Win) | Runtime health tracked continuously |

## Example

**"Customer Treasury Management System"** — Operated by enterprise customers in the Financial Services segment. Submits cross-border payment batches via SFTP (50K transactions/day, weekly batch cycle). Consumes payment.settled events via webhook for reconciliation (requires at-least-once delivery, < 30 minute delivery latency). Batch-tolerant for submissions but near-real-time for settlement notifications. If API unavailable: batch queues locally and retries next cycle; webhook failures trigger manual reconciliation.

---
