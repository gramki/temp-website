# Module / Domain

**Model:** Definition Model
**Dimension:** Structural
**Owner:** Enterprise Architects, Business Analysts

## Definition

A major bounded context within the product — a logically cohesive area of functionality.

> **Flat Module structure is a deliberate choice.** Modules are direct children of Product — there is no Module-within-Module nesting. The hierarchy is strictly Product → Module → Capability → Feature. If a functional area feels too large for a single Module (e.g., "Payments" containing both domestic and cross-border concerns), the correct decomposition is into peer Modules ("Domestic Payments Module," "Cross-Border Payments Module"), not into parent-child Modules. **Versioning (DR-036):** Module (Structural) is a functional boundary, not an operational versioning tier. Product Version composes System Versions directly; capability availability is traced Module → System → System Version in the Product Version BOM. Nesting Modules would complicate functional decomposition without adding deployment semantics. If organizational grouping is needed beyond flat Modules, it belongs in the Operating Model (team structure, domain ownership) — not in the Definition Model hierarchy. See FAQ Q96; DR-036 D3, D12.

## Purpose

Provides the primary decomposition boundary below the Product level. Modules contain Capabilities, are implemented by Systems (Dimension 5, many-to-many mapping), and align with Data Domains (Dimension 9).

## Fields

| Field | Type | Description |
|---|---|---|
| Module Code | String | Short unique identifier within the Product (e.g., PAY, FX, COMP) |
| Name | String | Module name (e.g., "Payments Module," "FX Module") |
| Functional Classification | Enum | The customer-value category of this Module, drawn from the Twelve System Types: `Record` / `Enforcement` / `Data` / `Engagement` / `Action` / `Intelligence` / `Identity` / `Influence` / `Memory` / `Product` / `Innovation` / `Integration`. See draft-archetypes.md for definitions. |
| Tenancy Model | Enum | `Single-Tenant` / `Multi-Tenant`. Must be consistent with parent Product's Tenancy Model (a Multi-Tenant Product requires Multi-Tenant Modules). |
| Lifecycle Status | Enum | `Incubating` / `Preview (Beta)` / `GA` / `Maintenance` / `End-of-Life` — same lifecycle as Product (D2) |
| Owner | Reference (WFR) | PM / Domain Lead responsible for this Module |

> **Vocabulary note (D15):** In the UPIM, "Module" (Structural) refers to the *functional grouping* — what the product does for the customer. "System" (Technical) refers to the *operational deployment grouping* — how it deploys. Engineers who use "module" informally for deployment units should use "System" in UPIM-aligned communication. See DR-035.

## Statuses

| Status | Description |
|---|---|
| Incubating | Module is in early formation — not yet available to customers |
| Preview (Beta) | Module is available to a limited customer set for validation |
| GA | Module is generally available |
| Maintenance | Module is no longer actively extended; only critical fixes shipped |
| End-of-Life | Module is retired; customers migrated to replacement |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Product (Structural) | Module belongs to a Product |
| Contains | Capability (Structural) | Module contains Capabilities |
| Packaged by | Pricing Tier (Vendor Value) | Module is packaged and included in a Pricing Tier (entitlement boundary — D7) |
| Implemented by | System(s) (Technical) | Module is realized by one or more Systems (many-to-many — functional boundary ≠ technical boundary; Architect-defined — D11) |
| Aligns to | Data Domain (Data) | Module aligns to one or more Data Domains |
| Specified by | Product Specification Document (Strategy) | PSDs specify changes to this Module's Capabilities and Features |

## Example

"Payments Module" — Code: PAY, Functional Classification: Record, Tenancy Model: Multi-Tenant, Lifecycle: GA, Owner: PM-Payments. Realized by: Payments System (primary), Notification System (shared). Packaged by: Standard Tier, Enterprise Tier.
