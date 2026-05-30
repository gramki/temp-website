# Operational Persona

**Model:** Definition Model
**Dimension:** Operational
**Owner:** Engineering Leadership, Platform Engineering

## Definition

A functional archetype who operates the product — not an organizational role (those belong in the Operating Model) but a function the product's operational health depends on. Operational Personas are organized by the Operational Quality Taxonomy (Reliability, Security, Platform, Data), not by job titles. Whether an organization calls the Reliability Operator "SRE" or "DevOps Engineer" or "Infrastructure Lead" is an Operating Model concern; the Definition Model captures the functional archetype.

> **Role definition, not agent identity.** Operational Persona is a **role** in the Definition Model. Specific people or AI agents who fulfill this role are tracked in the Workforce Repository (WFR) with role bindings referencing this persona. See DR-034.

Distinct from User Persona (User Experience) and Developer Persona (Ecosystem) — different interaction paradigm, different quality criteria, different concerns. The same human may appear in multiple dimensions: a User Experience User Persona when using the Developer Portal, a Ecosystem Developer Persona when writing API integration code, a Operational Operational Persona when operating the monitoring dashboard.

## Purpose

Captures who operates the product and what their needs are, enabling operational tooling investment decisions, operational module design, and operational experience prioritization. Without Operational Personas:
- Operational tooling is built reactively ("we need a dashboard") rather than intentionally ("Reliability Operators need to diagnose incidents within SLO")
- Operational Pains have no persona to anchor to — they float without an endurer
- Product investment in operational capabilities lacks a demand signal from a defined persona

**Discovery process:** Operational Personas are identified through operational experience, surfaced as observations or research findings in Discovery, and formally documented in Operational through Modeling Tasks triggered by PDRs. Operational Personas are Signal *sources*, not entity authors — they contribute operational observations that become Signals.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | Text | Archetype name (e.g., "Reliability Operator," "Security Operator") |
| Quality Domain | Enum | Primary quality taxonomy area: `Reliability` / `Performance` / `Security` / `Compliance` / `Cost Efficiency` / `Observability` / `Scalability` / `Platform` / `Data` |
| Role Context | Text | What they do and why they interact with the product operationally |
| Key Concerns | List | What matters most (e.g., availability, incident MTTR, SLO compliance, cost control) |
| Operational Pain(s) | List of References (Operational) | Current operational suffering |
| Operational Job(s) | List of References (Operational) | What they need to accomplish |
| Primary Module(s) | List of References (Structural) | Which operational modules they primarily use |
| UX Channel(s) | List of References (User Experience) | How they access the product (Web, CLI, Email, Mobile, etc.) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Operates | Deployment Environment (Operational) | Operational Personas operate specific environments |
| Has | Operational Job (Operational) | Operational Personas have jobs to accomplish |
| Follows | Operational Journey (Operational) | Operational Personas follow journeys through operational modules |
| Endures | Operational Pain (Operational) | Operational Personas experience operational suffering |
| Responsible for | Operational Target (Operational) | Operational Personas own specific operational targets |
| Accesses via | UX Channel (User Experience) | Cross-dimensional: Operational Personas access the product through UX Channels |
| Uses | Module (Structural) | Operational Personas use operational modules (admin consoles, monitoring dashboards, CLIs) |
| Uses | Integration Module (Ecosystem) | Operational Personas use integration modules to third-party ops tools (Datadog, PagerDuty) |
| Discovery | Research Task (Discovery) | Operational needs studied via research |
| Signals | Signal (Strategy) | Operational observations become Signals |

## Quality-Taxonomy Archetypes

| Archetype | Quality Domain | Key Concerns | Typical Modules |
|---|---|---|---|
| **Reliability Operator** | Reliability, Observability | Availability, incident response, SLO compliance, error budgets, Post-Incident Reviews | Monitoring Dashboard, Alerting System, Incident Management Tool |
| **Security Operator** | Security, Compliance | Security posture, vulnerability management, access control, key management, audit trails | Security Console, Key Management Module, Audit Dashboard |
| **Platform Operator** | Platform, Scalability | Deployment infrastructure, CI/CD, environment provisioning, developer experience, capacity | Deployment Console, CI/CD Dashboard, Environment Manager |
| **Data Operator** | Data, Compliance | Data integrity, backup/restore, migration, schema management, data residency | Database Admin Console, Backup Manager, Migration Tool |

## Example

**"Reliability Operator"** — Quality Domain: Reliability + Observability. Owns availability and incident response for all production environments. Key concerns: SLO compliance (99.99% availability target), MTTR < 30 minutes for P1, zero undetected degradation. Uses: Monitoring Dashboard (Web + Self-serve), Alert System (Email + Self-serve, Voice/IVR for P1 escalation), Deployment Console (Web + Self-serve for rollbacks), Incident CLI (CLI + Self-serve). Operational Pain: "Alert fatigue — 40% of production alerts are false positives, causing SRE burnout and delayed response to real incidents."

---
