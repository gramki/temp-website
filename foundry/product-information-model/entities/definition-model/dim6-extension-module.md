# Extension Module

**Model:** Definition Model
**Dimension / Track:** Dimension 6: Ecosystem & Extensibility (Platform)
**Owner:** Product Management (API/Platform), Engineering

## Definition

An Extension Module is a framework enabling third parties to extend the product's behavior through plugins, hooks, custom workflows, or custom rules. It provides governed extensibility points from one or more Dim 8 Modules, with controls for isolation, permissions, and lifecycle management. An Extension Module is structurally a Dim 8 Module carrying Dim 6 concerns.

## Purpose

Enables customers and partners to customize and extend product behavior without forking or modifying the core product. Captures the product's deliberate extensibility surface — which behaviors can be customized, what governance applies, and how extensions are managed.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | Text | Module name (e.g., "Compliance Workflow Extension," "Custom Rules Engine") |
| Extension Model | Text | What can be extended (plugins, hooks, custom workflows, custom rules, custom UI components) |
| Extensibility Points | List | Named hooks/extension points exposed (e.g., "pre-payment-screening," "post-settlement-notification") |
| Governance Model | Text | How extensions are reviewed, approved, and published (marketplace, admin-approval, self-service) |
| Sandboxing | Text | Isolation mechanism (separate runtime, resource limits, permission boundaries) |
| Permission Model | Text | What resources/data an extension can access |
| Composes From | Reference(s) | Dim 8 Module(s) whose extensibility points this surfaces |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Is a | Module (Dim 8) | Structurally a Dim 8 Module with Dim 6 extensibility concerns |
| Composes from | Module(s) (Dim 8) | Surfaces extensibility points from underlying modules |
| Serves | Developer Persona (Dim 6) | Developers building extensions |
| Governed by | API Compatibility Contract (Dim 6) | Extension API stability commitments |
| Assessed by | Win Review (Track 4) | Extension adoption and ecosystem health reviewed |

## Example

**"Compliance Workflow Extension"** — Enables customers to inject custom screening rules and approval chains into the payment processing pipeline. Extensibility Points: "pre-payment-screening" (custom compliance checks before payment initiation), "post-screening-action" (custom actions on screening results), "approval-chain-override" (custom approval workflow). Governance: admin-approval (extensions reviewed by product compliance team before activation). Sandboxing: separate runtime with 30-second execution timeout, no direct database access. Permission Model: read access to payment and customer profile data, write access to screening result annotations only.

---
