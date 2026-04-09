# Integration Module

**Model:** Definition Model
**Dimension / Track:** Dimension 6: Ecosystem & Extensibility (Platform)
**Owner:** Product Management (API/Platform), Solutions Architecture

## Definition

An Integration Module is a pre-built bridge between the product and a specific external system or system category. It includes not just APIs but also data mappings, protocol translations, workflow adapters, and connectors that translate between the product's model and the target system's model. An Integration Module is structurally a Dim 8 Module carrying Dim 6 concerns.

Integration Modules serve **all persona types** — Developer Personas and Programmatic User Personas (Dim 6) for customer/partner system integrations, AND **Operational Personas (Dim 7)** for third-party ops tooling integrations. When the product ships a Datadog exporter, PagerDuty webhook integration, or Terraform provider, those are Integration Modules deliberately built for the Operations team — no different from an SAP connector built for a customer's ERP team. See DR-023.

The distinction from API Module: API Module says "here's our programmatic interface"; Integration Module says "here's a ready-made bridge between us and your system." If a product doesn't ship connectors to specific external systems, it has API Modules but no Integration Modules — a valid product decision.

## Purpose

Reduces integration effort for customers, partners, and the operations team by providing pre-built connectors to specific external systems. The "external system" may be a customer's system (SAP, Salesforce), a partner's middleware, or a third-party operational tool (Datadog, PagerDuty, Terraform, Grafana). Without Integration Modules, every consumer — including the vendor's own operations team — must build their own translation layer.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | Text | Module name (e.g., "SAP ERP Integration," "Salesforce Connector") |
| Target System(s) | Text | Specific external system or system category this bridges to |
| Bridge Direction | Enum | Inbound / Outbound / Bidirectional |
| Data Mappings | Text | Summary of entity/field mappings between product and target system |
| Protocol Support | List | Protocols used for target system communication (BAPI, IDoc, REST, SOAP, etc.) |
| Relies On | Reference(s) | API Module(s) and other Dim 8 Module(s) whose capabilities this composes |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Is a | Module (Dim 8) | Structurally a Dim 8 Module with Dim 6 connector concerns |
| Relies on | API Module (Dim 6) | Uses API Module operations for product-side interaction |
| Relies on | Module(s) (Dim 8) | Composes capabilities from underlying modules |
| Serves | Developer Persona (Dim 6) | Developers configuring or extending the connector |
| Serves | Programmatic User Persona (Dim 6) | Target system consuming/providing data at runtime |
| Serves | Operational Persona (Dim 7) | Operations team using third-party ops tools via this connector |
| Referenced by | Operational Journey (Dim 7) | Operational Journeys may traverse integration modules to third-party ops tools |
| Governed by | API Compatibility Contract (Dim 6) | Connector versioning and stability commitments |
| Assessed by | Win Review (Track 4) | Integration health and adoption reviewed |

## Example

**"SAP ERP Integration Module"** (customer-facing) — Provides pre-built data mappings between product payment entities and SAP FI document types. Includes BAPI adapters for real-time posting and IDoc templates for batch exchange. Bidirectional: inbound (SAP payment instructions → product) and outbound (product settlement confirmations → SAP). Relies on Cross-Border Payments API Module for product-side operations. Target system: SAP S/4HANA and ECC 6.0. Serves: Developer Persona, Programmatic User Persona.

**"Datadog Observability Integration Module"** (operations-facing) — Exports product metrics, traces, and logs to Datadog for centralized observability. Includes pre-built Datadog dashboards for key SLIs, alert templates for Operational Targets, and service catalog integration. Outbound: product metrics/traces → Datadog. Relies on Monitoring Module (Dim 8) for metric collection. Target system: Datadog. Serves: Reliability Operator (Dim 7). Referenced by Operational Journey "Diagnose and resolve a SEV-1 incident."

---
