# System

**Model:** Definition Model
**Dimension:** Dimension 5: The Technical & Architectural Dimension (Engineering)
**Owner:** Tech Leads, Engineering Leadership, SRE

## Definition

A named operational grouping of Components — versioned as a whole and deployed as a whole by SRE/ops. The System is the operational deployment boundary: when SRE deploys "Payments System v3.1," they apply a composed deployment of all its Components. A System maps many-to-many to Dim 8 Modules — a Module may be realized by multiple Systems; a shared System may serve multiple Modules.

> **Supersedes DR-024 D3 (amended by DR-035):** System is no longer defined as "independently deployable technical unit" at microservice granularity. System is the **operational deployment grouping** of Components. Component is the atomic deployable artifact. See DR-035 Decision D10.

> **Vocabulary note (DR-035 D15):** In organizational usage, engineers sometimes use "module" informally for what the UPIM calls "System" — a deployable technical grouping. The UPIM reserves "Module" for Dim 8 (the functional grouping that customers recognize: "Payments Module," "FX Module") and uses "System" for the Dim 5 operational deployment grouping. When an engineer says "the payments module is deploying," they mean "the Payments System is deploying" in UPIM terms.

## Purpose

Captures the product's technical deployment topology — what operational groupings exist, how they map to functional modules, and what Components they contain. Without Systems:
- The product's technical architecture is invisible in the Definition Model
- Deployment Environments (Dim 7) have no technical unit to host
- Impact analysis ("which modules are affected if this System is down?") has no anchor
- SRE/ops has no versioning and deployment unit to operate

**Dim 8 / Dim 5 mapping:** The many-to-many mapping between Systems and Modules makes the functional-to-technical relationship visible. This is critical for: impact analysis, capability-to-implementation tracing, and change planning.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | System name — typically a product domain noun in kebab-case (e.g., "payments-system," "fx-system," "compliance-system," "customer-portal") |
| Module Mapping | List of References (Dim 8) | Which Dim 8 Module(s) this System realizes (many-to-many; Architect-defined) |
| Purpose / Serving Persona(s) | List of References (Dim 4 / Dim 7) | Who this System serves — End-User or Programmatic Personas (Dim 4) or Operational Personas (Dim 7); distinguishes product-facing from operational Systems within Product Specification (DR-036 D9) |
| Owner | Reference (WFR) | Engineering team or Tech Lead responsible for this System |
| Deployment Specification Reference | Reference (Track 3) | Link to System Deployment Specification — environment-specific deployment configuration |
| Repository Reference | String | Source code repository identifier (e.g., GitHub org/repo) |
| Technology Stack — Language | String | Primary programming language(s) (e.g., "Java 21," "Python 3.12") |
| Technology Stack — Framework | String | Primary framework(s) (e.g., "Spring Boot 3.2," "FastAPI") |
| Technology Stack — Runtime | String | Runtime environment (e.g., "JVM 21," "Docker / ECS," "AWS Lambda") |

## Statuses

| Status | Description |
|---|---|
| Planned | System has been designed (ADR produced) but not yet built |
| In Development | System is being built (Build Track work in progress) |
| Active | System is deployed and operational in at least one environment |
| Deprecated | System is being phased out (replacement identified, migration in progress) |
| Retired | System has been fully decommissioned |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Realizes | Module(s) (Dim 8) | System realizes one or more functional Modules (many-to-many; Architect-defined) |
| Contains | Component(s) (Dim 5) | System contains one or more Components (deployable artifacts) |
| Depends on | Dependency(ies) (Dim 5) | System depends on external services and infrastructure resources |
| Deployed to | Deployment Environment(s) (Dim 7) | System is deployed to specific environments |
| Participates in | Interaction Flow(s) (Dim 5) | System participates in inter-system Interaction Flows |
| Has | Technical Knowledge Base (Dim 5) | System has a documentation coverage assessment |
| Decisions | ADR(s) (Dim 5) | Architectural decisions affecting this System are recorded as ADRs |
| Produces | System Version (Track 2) | Build Track produces versioned, quality-gated System Versions — each System Version is a composed snapshot of its Components' Component Versions |
| Described by | System Deployment Specification (Track 3) | System Deployment Specification defines environment-specific deployment configuration for a System Version |
| Included in | Product Specification (Dim 5) | System is listed in its Product's Product Specification (product-facing and operational Systems equally) |
| Context | Architecture Model (Dim 5) | System exists within the Architecture Model's frame |

## Examples

| System | Realizes (Dim 8 Module) | Components | Tech Stack | Status |
|---|---|---|---|---|
| payments-system | Payments Module (primary), Settlement Module (partial) | payments-service (API Service), payment-reconciler (Batch Job), payment-notification-worker (Event-Driven Worker) | Java 21 / Spring Boot 3.2 | Active |
| fx-system | FX Module | fx-engine (API Service), fx-rate-cache (Data Store) | Java 21 / Spring Boot 3.2 | Active |
| compliance-system | Compliance Module | compliance-service (API Service), ofac-screening-adapter (Integration Adapter), compliance-event-consumer (Event-Driven Worker) | Java 21 / Spring Boot 3.2 | Active |
| bank-connectivity-system | Payments Module, Settlement Module | bank-adapter (Integration Adapter), bank-file-generator (Batch Job) | Java 21 / Spring Boot 3.2 | Active |
| customer-portal-system | Customer Portal Module | portal-web-app (Web Application), portal-bff (API Service) | TypeScript / React, Java 21 | Active |

> **Operational deployment example:** When SRE deploys "Payments System v3.1," they apply a System Deployment Specification that composes Component Versions: payments-service v2.3.1, payment-reconciler v1.4.0, payment-notification-worker v1.2.0 into that System Version. These three Components are deployed together as a unit — not individually to production.
