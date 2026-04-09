# Developer Persona

**Model:** Definition Model
**Dimension / Track:** Dimension 6: Ecosystem & Extensibility (Platform)
**Owner:** Product Management (API/Platform), Developer Relations

## Definition

A Developer Persona is a named archetype representing the human who builds integrations, extensions, or applications using the product's programmatic surfaces. Developer Personas have fundamentally different concerns from Dim 4 User Personas — their interaction paradigm is programmatic/contractual (reading docs, writing code, testing in sandboxes, debugging error responses) rather than visual/experiential.

> **Role definition, not agent identity.** Developer Persona is a **role** in the Definition Model describing an external builder archetype. Individual developers (internal or external) who fulfill this role may be tracked in the Workforce Repository (WFR, for internal API consumers) or the External Stakeholder Registry (ESR, for external developers with sandbox access or partnership agreements). See DR-034.

## Purpose

Captures who the product's programmatic surfaces are designed for, enabling API design decisions, documentation strategy, SDK investment, and developer experience prioritization. Without Developer Personas, API design defaults to internal engineering convenience rather than external developer needs.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | Text | Archetype name (e.g., "Partner Integration Engineer," "Fintech App Developer") |
| Role Context | Text | What they do and why they interact with the product programmatically |
| Technical Proficiency | Enum | Junior / Intermediate / Senior / Expert |
| Primary Languages / Stacks | List | Languages and frameworks they typically work with |
| Integration Scenario | Text | What they are trying to build or connect |
| Key Concerns | List | What matters most (e.g., API ergonomics, docs quality, sandbox fidelity, error clarity, backward compatibility, time-to-first-call) |
| Frustrations | List | Current pain points with the programmatic surface |
| Primary API Module(s) | Reference(s) | Which API Modules they primarily consume |
| Preferred SDK(s) | Reference(s) | Which SDK/Library Modules they use |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Consumes | API Module (Dim 6) | Primary consumer of API surface |
| Consumes | SDK/Library Module (Dim 6) | Uses language-specific client |
| Consumes | Extension Module (Dim 6) | Builds extensions/plugins |
| Overlaps with | User Persona (Dim 4) | Same human may appear as Dim 4 Persona when using Developer Portal (Web + Self-serve) |
| Informs | API Operation (Dim 6) | Drives operation design and SLO targets |
| Referenced by | API Compatibility Contract (Dim 6) | Contract commitments are promises to this persona |
| Discovery | Research Task (Track 1) | Developer needs studied via research |
| Win | Win Activity (Track 4) | Developer community, partner enablement |

## Example

**"Partner Integration Engineer"** — Works at a co-branded card issuing partner. Intermediate-to-senior proficiency in Java and Python. Building integration between partner's card management system and the product's Card Issuing API Module. Key concerns: sandbox environment fidelity, clear error codes with actionable messages, semantic versioning stability, webhook reliability for real-time card events. Frustration: documentation examples don't cover edge cases for declined authorizations.

---
