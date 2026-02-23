# Module / Domain

**Model:** Definition Model
**Dimension:** Dimension 8: The Structural Dimension (Topology)
**Owner:** Enterprise Architects, Business Analysts

## Definition

A major bounded context within the product — a logically cohesive area of functionality.

> **Flat Module structure is a deliberate choice.** Modules are direct children of Product — there is no Module-within-Module nesting. The hierarchy is strictly Product → Module → Capability → Feature. If a functional area feels too large for a single Module (e.g., "Payments" containing both domestic and cross-border concerns), the correct decomposition is into peer Modules ("Domestic Payments Module," "Cross-Border Payments Module"), not into parent-child Modules. This keeps the composition model clean: Module Version composes System Versions within one Module; Product Version composes Module Versions. Nesting Modules would introduce a fourth composition tier (child Module Version → parent Module Version) and complicate the versioning, integration verification, and communication-bridge semantics. If organizational grouping is needed beyond flat Modules, it belongs in the Operating Model (team structure, domain ownership) — not in the Definition Model hierarchy. See FAQ Q96.

## Purpose

Provides the primary decomposition boundary below the Product level. Modules contain Capabilities, are implemented by Systems (Dimension 5, many-to-many mapping), and align with Data Domains (Dimension 9).

## Fields

| Field | Type | Description |
|---|---|---|
| _To be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| _To be refined._ | |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Product (Dim 8) | Module belongs to a Product |
| Contains | Capability (Dim 8) | Module contains Capabilities |
| Implemented by | System(s) (Dim 5) | Module is implemented by one or more Systems (many-to-many — functional boundary ≠ technical boundary) |

## Example

Invoice & Payout Processing.
