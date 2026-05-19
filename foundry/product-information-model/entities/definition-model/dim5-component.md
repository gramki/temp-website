# Component

**Model:** Definition Model
**Dimension:** Dimension 5: The Technical & Architectural Dimension (Engineering)
**Owner:** Tech Leads, Developers

## Definition

An individual deployable artifact within a System — independently buildable with its own artifact version (container image, Lambda package, frontend bundle, JAR, etc.), but **not independently deployed to production**. Components are deployed as part of their parent System via the System's System Deployment Specification. A Component has a Component Archetype that classifies its deployment artifact type.

> **Supersedes DR-024 D8 (amended by DR-035):** Component is no longer "significant architectural building block within a System" (FX Rate Calculator, Payment State Machine). Component is the **atomic deployable artifact** within a System — a container image, Lambda package, frontend bundle, or equivalent. Code-level building blocks (processing engines, rule evaluators, adapters embedded within a single artifact) are below the Definition Model waterline. See DR-035 Decision D10.

## Purpose

Captures the deployable composition of a System — which artifacts exist, how they are typed, and how they map to product Capabilities. Without Components:
- The internal structure of a System is opaque
- CI/CD pipelines have no UPIM anchor (each Component has its own build pipeline, image tag, version)
- Capability-to-artifact tracing is missing — "which artifact implements Real-Time FX Rate Lock?"
- Build Track System Version has no constituent artifact list

Components are the units that CI/CD pipelines build and tag. Each Component is versioned as a **Component Version** (Track 2). Component Versions compose into their parent System's **System Version** — the System Version is the composed snapshot of all constituent Component Versions.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Component name — lowercase kebab-case artifact identifier (e.g., "payments-service," "fx-engine," "portal-web-app") |
| Archetype | Enum | Deployment artifact type — see Component Archetypes below |
| Parent System | Reference (Dim 5) | The System this Component belongs to |
| Tech Stack | String | Technology stack (e.g., "Java 21 / Spring Boot 3.2," "TypeScript / React") — specify when different from parent System |
| Repository Reference | String | Source code repository identifier (e.g., GitHub org/repo) |
| Artifact Reference | String | Container registry / package registry path (e.g., "ghcr.io/org/payments-service") |
| Capability Mapping | List of References (Dim 8) | Which Dim 8 Capabilities this Component implements or contributes to (Architect-defined) |

## Component Archetypes

| Archetype | Description | Examples |
|---|---|---|
| `API Service` | Synchronous request-response service exposed via REST, gRPC, or GraphQL | payments-service, fx-engine, compliance-service, portal-bff |
| `Web Application` | Browser-served frontend application | portal-web-app, admin-dashboard |
| `Event-Driven Worker` | Consumes events or messages from a queue or stream | payment-notification-worker, compliance-event-consumer |
| `Batch Job` | Runs on schedule or trigger; processes data in bulk | payment-reconciler, bank-file-generator, daily-fx-snapshot |
| `Data Store` | A managed data store artifact (e.g., schema package, cache config) | fx-rate-cache, audit-db-schema |
| `Integration Adapter` | Connects to an external system via its protocol or file format | bank-adapter, ofac-screening-adapter, swift-connector |
| `Gateway` | Proxy, router, or API gateway managing traffic across components | api-gateway, payments-gateway |
| `CLI/SDK` | Command-line tool or language-specific library distributed to developers/operators | payments-cli, fx-sdk-java |

## Statuses

_Inherits from parent System — Components do not have an independent lifecycle. A Component is Active when its parent System is Active._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Belongs to | System (Dim 5) | Component is contained by a System |
| Maps to | Capability(ies) (Dim 8) | Component implements or contributes to specific Capabilities (Architect-defined) |
| Decisions | ADR(s) (Dim 5) | Architectural decisions affecting this Component are recorded as ADRs |
| Versioned as | Component Version (Track 2) | Build Track produces versioned, quality-gated Component Versions per artifact |
| Composes into | System Version (Track 2) | Component Versions from all Components in a System compose that System's System Version |

## Examples

| Component | Archetype | Parent System | Tech Stack | Maps to (Dim 8 Capability) |
|---|---|---|---|---|
| payments-service | API Service | payments-system | Java 21 / Spring Boot 3.2 | Cross-Border B2B Payments, Domestic Payment Initiation |
| payment-reconciler | Batch Job | payments-system | Python 3.12 | Settlement Reconciliation |
| payment-notification-worker | Event-Driven Worker | payments-system | Java 21 / Spring Boot 3.2 | Payment Status Notifications |
| fx-engine | API Service | fx-system | Java 21 / Spring Boot 3.2 | Real-Time FX Rate Lock |
| fx-rate-cache | Data Store | fx-system | Redis 7 | Real-Time FX Rate Lock |
| compliance-service | API Service | compliance-system | Java 21 / Spring Boot 3.2 | OFAC Sanctions Screening |
| ofac-screening-adapter | Integration Adapter | compliance-system | Java 21 / Spring Boot 3.2 | OFAC Sanctions Screening |
| bank-adapter | Integration Adapter | bank-connectivity-system | Java 21 / Spring Boot 3.2 | Bank Payment Execution |
| bank-file-generator | Batch Job | bank-connectivity-system | Java 21 / Spring Boot 3.2 | Batch Settlement File Generation |
| portal-web-app | Web Application | customer-portal-system | TypeScript / React | Payment Dashboard, FX Rate Monitor |
| portal-bff | API Service | customer-portal-system | Java 21 / Spring Boot 3.2 | Payment Dashboard, FX Rate Monitor |

> **Build pipeline example:** `payments-service` has its own Dockerfile and GitHub Actions workflow. CI/CD produces **Component Version** `payments-service:2.3.1` (image `ghcr.io/org/payments-service:2.3.1`). Sibling Components likewise produce Component Versions (`payment-reconciler:1.4.0`, `payment-notification-worker:1.2.0`). The Build Track assembles **System Version** Payments System v3.1 from those Component Versions. The System Deployment Specification references that System Version composition for deployment.
