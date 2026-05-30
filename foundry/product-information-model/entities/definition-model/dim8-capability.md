# Capability

**Model:** Definition Model
**Dimension:** Structural
**Owner:** Enterprise Architects, Business Analysts

## Definition

A specific ability provided by a Module — a named, coherent function that the Module delivers to users or consuming systems. Capabilities are the primary unit that Product Managers specify in a PSD and that Architects map to Systems and Components.

## Purpose

Provides the mid-level taxonomy between Module and Feature. Capabilities represent "what the product can do" at a level meaningful to both business and technical stakeholders. A Capability has two independent attributes: Maturity (how proven it is) and Lifecycle Stage (where it sits in its usage lifecycle). PM authors Capability specifications using a Capability Template (Experience, Integration, or Processing). The Architect maps Capabilities to Systems and Components.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Capability name (e.g., "Real-Time FX Rate Lock," "Cross-Border B2B Payments") |
| Description | Text | What this Capability enables — outcome-focused, 1–3 sentences |
| Capability Template | Enum | PM specification guide for this Capability: `Experience` (user interaction focus) / `Integration` (programmatic API focus) / `Processing` (background computation focus). See psd-templates/ for template content. |
| Module | Reference (Structural) | The Module this Capability belongs to |
| Maturity | Enum | How proven this Capability is: `Alpha` (early, experimental) / `Beta` (limited availability, stabilizing) / `Gamma` (proven, stable). Independent of Lifecycle Stage. A GA Module may contain Alpha Capabilities. |
| Lifecycle Stage | Enum | Where in the usage lifecycle: `Planned` (not yet available) / `Available` (customers can use it) / `Deprecated` (available but actively discouraged, replacement exists) / `Retired` (no longer available). Independent of Maturity. |

## Statuses

> Capability state is described by two independent attributes: **Maturity** (`Alpha / Beta / Gamma`) and **Lifecycle Stage** (`Planned / Available / Deprecated / Retired`). Both are set independently. A GA Module may contain Alpha Capabilities.

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Module (Structural) | Capability belongs to a Module |
| Contains | Feature(s) (Structural) | Capability contains Features |
| Mapped to | System(s) (Technical) | Capability is mapped to one or more Systems by the Architect (many-to-many, Architect-defined — D12) |
| Engaged by | Value Stream(s) (Structural) | Value Streams engage Capabilities at steps in the flow |
| Specified in | Product Specification Document (Strategy) | PSDs add, modify, or retire this Capability |
| Templated by | Capability Template (psd-templates/) | PM uses a Capability Template to specify this Capability in a PSD |

## Example

"Real-Time FX Rate Lock" — Module: FX Module, Capability Template: Integration, Maturity: Gamma, Lifecycle Stage: Available. Mapped to: FX System (primary), Payments System (shared). Features: Rate Lock API, Rate Lock Expiry Notification, Rate Lock Audit Trail.

"Bulk Payment File Upload" — Module: Payments Module, Capability Template: Integration, Maturity: Beta, Lifecycle Stage: Available. Mapped to: Payments System.

"OFAC Sanctions Screening" — Module: Compliance Module, Capability Template: Processing, Maturity: Gamma, Lifecycle Stage: Available. Mapped to: Compliance System.
