# Product Specification

**Model:** Definition Model
**Dimension:** Dimension 5: The Technical & Architectural Dimension (Engineering)
**Owner:** Tech Leads, Engineering Leadership, Enterprise Architects

## Definition

The technical composition specification for a Product — the Dim 5 counterpart to Product (Dim 8). A Product Specification declares which Systems compose the product. There is exactly one Product Specification per Product (1:1).

All Systems declared in a Product Specification are structurally equal: tenant-serving product Systems (payments-system, fx-system, customer-portal-system) and operational/SRE-facing Systems (payments-monitoring-system, payment-reconciler-system) alike. The distinction between product-facing and operational Systems is expressed through each System's `Purpose / Serving Persona(s)` field — not through a separate Package or extension layer.

> **Supersedes Dim 7 Package model (DR-036):** Module Package Specification and Product Package Specification are removed. Operational Systems are ordinary members of the Product Specification. See DR-036 D4, D7, D9.

## Purpose

Provides the static technical blueprint for what constitutes the product at the System level — independent of any specific version or environment. Without a Product Specification:
- The product's full technical footprint (including operational Systems) is implicit
- Product Version has no Definition Model anchor for "which Systems belong to this product"
- SRE-introduced operational Systems have no formal place in the product composition
- Impact analysis ("what Systems exist for this product?") requires tribal knowledge

**Dim 8 / Dim 5 pairing:** Product (Dim 8) describes what the product is for customers and the market. Product Specification (Dim 5) describes how it is technically composed from Systems.

## Fields

| Field | Type | Description |
|---|---|---|
| Product | Reference (Dim 8) | The Product this specification is the technical twin of |
| Systems | List of References (Dim 5) | All Systems composing this product — product-facing and operational |
| Status | Enum | Specification lifecycle status (see Statuses) |

## Statuses

| Status | Description |
|---|---|
| Draft | Specification is being authored; System composition is incomplete |
| Active | Specification is the current definition for Product Versions |
| Superseded | A newer specification has replaced this one |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Technical twin of | Product (Dim 8) | Product Specification is the Dim 5 counterpart of Product |
| Composes | System(s) (Dim 5) | Product Specification declares which Systems compose the product |
| Instantiated by | Product Version(s) (Track 2) | Product Version is a versioned, certified composition of System Versions for this product |
| Context | Architecture Model (Dim 5) | Product Specification exists within the Architecture Model's frame |
| Decisions | ADR(s) (Dim 5) | Architectural decisions affecting product composition are recorded as ADRs |

## Example

### Core Payment Gateway Product Specification

```
Product Specification: Core Payment Gateway
├── Product: Core Payment Gateway (Dim 8)
├── Status: Active
└── Systems:
    ├── payments-system          [End-User Personas: AP Clerk, Treasury Manager]
    ├── fx-system                [End-User Personas: AP Clerk, Treasury Manager]
    ├── compliance-system        [End-User Persona: Compliance Officer]
    ├── bank-connectivity-system [End-User Persona: AP Clerk]
    ├── customer-portal-system   [End-User Personas: AP Clerk, Treasury Manager]
    ├── payments-monitoring-system   [Operational Persona: SRE / Platform Operator]
    ├── settlement-reconciler-system [Operational Persona: SRE / Platform Operator]
    └── cross-border-smoke-probe-system [Operational Persona: SRE / Platform Operator]
```

> **All Systems are Build Track Systems.** Each System in the Product Specification is versioned via System Version (composed of Component Versions). Operational Systems are not a separate artifact category — they are Systems whose primary consumers are Operational Personas.

---
