# System

**Model:** Definition Model
**Dimension:** Dimension 5: The Technical & Architectural Dimension (Engineering)
**Owner:** Tech Leads, Engineering Leadership

## Definition

A named, independently deployable technical unit that implements one or more Dim 8 Modules. The technical counterpart to Module (Dim 8). Where Module captures the functional boundary ("Payments"), System captures the technical boundary ("payments-service"). The mapping is many-to-many: a Module may be implemented by multiple Systems; a shared System may serve multiple Modules. This reflects reality — functional decomposition and technical decomposition are independent.

Supersedes the original skeletal "Subsystem / Service" entity, which lacked technology stack fields, Module mapping, deployment references, and a full relationship set.

## Purpose

Captures the product's technical decomposition — what deployable units exist, what technology they use, and how they map to functional modules. Without Systems:
- The product's technical architecture is invisible in the Definition Model — only the functional view (Dim 8) exists
- Deployment Environments (Dim 7) have no technical unit to host — "deploy to production" has no artifact to deploy
- Dependencies have no consumer — "we depend on PostgreSQL" has no System that depends on it
- Architecture diagrams, sequence diagrams, and data flow diagrams have no anchoring entity

**Dim 8 / Dim 5 mapping:** The explicit many-to-many mapping between Systems and Modules makes the functional-to-technical relationship visible. This is critical for impact analysis: "if payments-service is down, which Modules are affected?" and "to add a Capability to the Payments Module, which Systems need to change?"

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | System name (e.g., "payments-service," "fx-engine," "notification-service") |
| Technology Stack — Language | String | Primary programming language(s) (e.g., "Java 21," "Python 3.12") |
| Technology Stack — Framework | String | Primary framework(s) (e.g., "Spring Boot 3.2," "FastAPI") |
| Technology Stack — Runtime | String | Runtime environment (e.g., "JVM 21," "Docker / ECS," "AWS Lambda") |
| Data Store(s) | List | Owned data stores with technology (e.g., "PostgreSQL 15 — transactional data," "Redis 7 — rate cache") |
| Communication Protocols | List | How this System communicates (e.g., "REST (inbound)," "gRPC (to fx-service)," "Kafka (produce/consume)") |
| Module Mapping | List of References (Dim 8) | Which Dim 8 Module(s) this System implements (many-to-many) |
| Purpose / Serving Persona(s) | List of References (Dim 4) | Which Persona(s) this System serves — determines the System's primary purpose. Product Systems serve End-User Personas (Dim 4) or Developer/Programmatic Personas (Dim 6). Operational Systems serve Operational Personas (Dim 7). A System may serve multiple Personas. |
| Repository Reference | String | Source code repository identifier |

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
| Implements | Module(s) (Dim 8) | System implements one or more functional Modules (many-to-many) |
| Contains | Component(s) (Dim 5) | System contains architectural Components |
| Depends on | Dependency(ies) (Dim 5) | System depends on external services and infrastructure resources |
| Deployed to | Deployment Environment(s) (Dim 7) | System is deployed to specific environments |
| Participates in | Interaction Flow(s) (Dim 5) | System participates in inter-system Interaction Flows |
| Has | Technical Knowledge Base (Dim 5) | System has a documentation coverage assessment |
| Decisions | ADR(s) (Dim 5) | Architectural decisions affecting this System are recorded as ADRs |
| Produces | System Version (Track 2) | Build Track produces versioned, quality-gated artifacts from this System |
| Discussed in | Design Deliberation (Track 2) | Architectural questions about this System are resolved through Design Deliberation |
| Serves | Persona(s) (Dim 4) / Operational Persona(s) (Dim 7) | System serves specific Personas — determines purpose |
| Context | Architecture Model (Dim 5) | System exists within the Architecture Model's frame |

## Examples

| System | Tech Stack | Data Store | Protocols | Implements (Dim 8) | Purpose / Serving Persona(s) | Status |
|---|---|---|---|---|---|---|
| payments-service | Java 21 / Spring Boot 3.2 | PostgreSQL 15 | REST (in), Kafka (produce/consume) | Payments Module (primary), Settlement Module (partial) | AP Clerk, Treasury Manager (End-User Personas) | Active |
| fx-service | Java 21 / Spring Boot 3.2 | Redis 7 (rate cache) | gRPC (in), REST (to rate providers) | FX Module | AP Clerk, Treasury Manager (End-User Personas) | Active |
| compliance-service | Java 21 / Spring Boot 3.2 | PostgreSQL 15 | Kafka (consume), REST (to screening providers) | Compliance Module | Compliance Officer (End-User Persona) | Active |
| notification-service | Python 3.12 / FastAPI | Redis 7 (queue) | Kafka (consume), SMTP, SMS API | Payments Module, Compliance Module, Onboarding Module (shared) | AP Clerk, Compliance Officer (End-User Personas) | Active |
| bank-adapter | Java 21 / Spring Boot 3.2 | — | REST (in/out), SFTP (batch files) | Payments Module, Settlement Module | AP Clerk (End-User Persona) | Active |
| analytics-service | Python 3.12 / FastAPI | ClickHouse | Kafka (consume), REST (out) | Analytics Module | Analyst (End-User Persona) | Active |
| payments-healthcheck | Go 1.22 | — | HTTP (out, synthetic probes) | Payments Module (operational) | SRE / Platform Operator (Operational Persona) | Active |
| payment-reconciler | Python 3.12 | — | Kafka (consume), PostgreSQL (read) | Payments Module (operational) | SRE / Platform Operator (Operational Persona) | Active |

> **Product Systems vs. Operational Systems.** Product Systems (payments-service, fx-service, etc.) serve end-user Personas — they deliver product functionality. Operational Systems (payments-healthcheck, payment-reconciler) serve Operational Personas (SRE, Platform Operator) — they deliver operational capability. Both are legitimate Systems with code, repos, CI/CD pipelines, tests, and System Versions. They differ in purpose (who they serve) and provenance (Build Track vs. Run Track engineering). The Purpose field makes this distinction explicit through Persona references rather than a static enum.

---
