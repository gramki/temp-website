# Operational Persona

**Model:** Definition Model
**Dimension:** Dimension 7: The Operational Dimension (Runtime & DevOps)
**Owner:** Engineering Leadership, Platform Engineering

## Definition

A functional archetype who operates the product — not an organizational role (those belong in the Operating Model) but a function the product's operational health depends on. Operational Personas are organized by the Operational Quality Taxonomy (Reliability, Security, Platform, Data), not by job titles. Whether an organization calls the Reliability Operator "SRE" or "DevOps Engineer" or "Infrastructure Lead" is an Operating Model concern; the Definition Model captures the functional archetype.

Distinct from User Persona (Dim 4) and Developer Persona (Dim 6) — different interaction paradigm, different quality criteria, different concerns. The same human may appear in multiple dimensions: a Dim 4 User Persona when using the Developer Portal, a Dim 6 Developer Persona when writing API integration code, a Dim 7 Operational Persona when operating the monitoring dashboard.

## Purpose

Captures who operates the product and what their needs are, enabling operational tooling investment decisions, operational module design, and operational experience prioritization. Without Operational Personas:
- Operational tooling is built reactively ("we need a dashboard") rather than intentionally ("Reliability Operators need to diagnose incidents within SLO")
- Operational Pains have no persona to anchor to — they float without an endurer
- Product investment in operational capabilities lacks a demand signal from a defined persona

**Discovery process:** Operational Personas are identified through operational experience, surfaced as observations or research findings in Discovery, and formally documented in Dim 7 through Modeling Tasks triggered by PDRs. Operational Personas are Signal *sources*, not entity authors — they contribute operational observations that become Signals.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | Text | Archetype name (e.g., "Reliability Operator," "Security Operator") |
| Quality Domain | Enum | Primary quality taxonomy area: `Reliability` / `Performance` / `Security` / `Compliance` / `Cost Efficiency` / `Observability` / `Scalability` / `Platform` / `Data` |
| Role Context | Text | What they do and why they interact with the product operationally |
| Key Concerns | List | What matters most (e.g., availability, incident MTTR, SLO compliance, cost control) |
| Operational Pain(s) | List of References (Dim 7) | Current operational suffering |
| Operational Job(s) | List of References (Dim 7) | What they need to accomplish |
| Primary Module(s) | List of References (Dim 8) | Which operational modules they primarily use |
| UX Channel(s) | List of References (Dim 4) | How they access the product (Web, CLI, Email, Mobile, etc.) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Operates | Deployment Environment (Dim 7) | Operational Personas operate specific environments |
| Has | Operational Job (Dim 7) | Operational Personas have jobs to accomplish |
| Follows | Operational Journey (Dim 7) | Operational Personas follow journeys through operational modules |
| Endures | Operational Pain (Dim 7) | Operational Personas experience operational suffering |
| Responsible for | Operational Target (Dim 7) | Operational Personas own specific operational targets |
| Accesses via | UX Channel (Dim 4) | Cross-dimensional: Operational Personas access the product through UX Channels |
| Uses | Module (Dim 8) | Operational Personas use operational modules (admin consoles, monitoring dashboards, CLIs) |
| Uses | Integration Module (Dim 6) | Operational Personas use integration modules to third-party ops tools (Datadog, PagerDuty) |
| Discovery | Research Task (Track 1) | Operational needs studied via research |
| Signals | Signal (Dim 1) | Operational observations become Signals |

## Quality-Taxonomy Archetypes

| Archetype | Quality Domain | Key Concerns | Typical Modules |
|---|---|---|---|
| **Reliability Operator** | Reliability, Observability | Availability, incident response, SLO compliance, error budgets, post-mortems | Monitoring Dashboard, Alerting System, Incident Management Tool |
| **Security Operator** | Security, Compliance | Security posture, vulnerability management, access control, key management, audit trails | Security Console, Key Management Module, Audit Dashboard |
| **Platform Operator** | Platform, Scalability | Deployment infrastructure, CI/CD, environment provisioning, developer experience, capacity | Deployment Console, CI/CD Dashboard, Environment Manager |
| **Data Operator** | Data, Compliance | Data integrity, backup/restore, migration, schema management, data residency | Database Admin Console, Backup Manager, Migration Tool |

## Example

**"Reliability Operator"** — Quality Domain: Reliability + Observability. Owns availability and incident response for all production environments. Key concerns: SLO compliance (99.99% availability target), MTTR < 30 minutes for P1, zero undetected degradation. Uses: Monitoring Dashboard (Web + Self-serve), Alert System (Email + Self-serve, Voice/IVR for P1 escalation), Deployment Console (Web + Self-serve for rollbacks), Incident CLI (CLI + Self-serve). Operational Pain: "Alert fatigue — 40% of production alerts are false positives, causing SRE burnout and delayed response to real incidents."

---
