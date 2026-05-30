# Operational Job

**Model:** Definition Model
**Dimension:** Operational
**Owner:** Engineering Leadership, Platform Engineering, DevOps Leadership

## Definition

What the Operational Persona needs to accomplish through the product's operational tooling — the operational "job to be done." Operational Jobs bridge operational intent (Operational) to product structure (Structural): they explain WHY operational modules exist and WHAT capabilities they must provide. Independent from Job (JTBD) in User Experience — same analytical pattern (persona → job → journey), different domain (operational reality vs. user experience).

The Run Track work entities (Deployment, Incident, Change Request, Maintenance Task) are the instantiation of Operational Jobs — individual deployments, individual incident resolutions. The Definition Model captures the job definition and its structural enablers; the Work Model captures the work of executing them.

## Purpose

Without Operational Jobs:
- Operational modules are built without traceability to operational needs — "we built a monitoring dashboard" but can't explain what job it serves
- The product's operational capability investment is invisible — no entity traces from operational need → structural capability → feature
- Operational journey design has no anchor — you can't design a journey if you don't know what job it accomplishes

**Discovery process:** Operational Jobs are identified through operational experience, field research with Operational Personas, and analysis of Run Track work patterns. They are formally documented in Operational through Modeling Tasks.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | Text | Job statement (verb-led, outcome-focused, e.g., "Deploy a release safely to production") |
| Quality Domain | Enum | Primary quality taxonomy area this job serves |
| Pursued by | List of References (Operational) | Which Operational Persona(s) pursue this job |
| Enabled by | List of References (Structural) | Which Value Stream(s) or Capability(ies) enable this job |
| Measured against | List of References (Operational) | Which Operational Target(s) define success for this job |
| Run Track Instantiation | Text | Which Run Track work entity type corresponds to this job (e.g., Deployment, Incident) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Pursued by | Operational Persona (Operational) | Operational Personas pursue this job |
| Accomplished through | Operational Journey (Operational) | Operational Jobs are accomplished through journeys |
| Enabled by | Value Stream / Capability (Structural) | Structural entities that deliver this operational capability |
| Measured against | Operational Target (Operational) | Operational Targets define success criteria for this job |
| Instantiated by | Run Track work entities (Run) | Deployment, Incident, Change Request, Maintenance Task are instances |
| Work Model | Modeling Task (Discovery) | Operational Jobs are documented through Modeling Tasks |

## Examples

| Operational Job | Quality Domain | Pursued by | Enabled by (Structural) | Measured against | Run Track Entity |
|---|---|---|---|---|---|
| "Deploy a release safely to production without service disruption" | Platform | Platform Operator | Release Management (Value Stream), Canary Deployment (Capability) | Zero-downtime deployments; rollback within 5 min | Deployment |
| "Diagnose and resolve a SEV-1 incident within SLO" | Reliability | Reliability Operator | Incident Management (Value Stream), Root Cause Analysis (Capability) | MTTR < 30 min for SEV-1; zero cascading failures | Incident Response Task |
| "Rotate encryption keys without downtime" | Security | Security Operator | Key Management (Capability), Automated Key Rotation (Capability) | Zero expired certificates; rotation < 5 min | Maintenance Task |
| "Scale infrastructure for expected load within budget" | Scalability, Cost | Platform Operator | Capacity Management (Value Stream), Auto-Scale (Capability) | Cost growth < 1.5x traffic growth; no capacity-induced outages | Capacity Planning |
| "Restore service from backup within RTO" | Reliability | Data Operator, Reliability Operator | Disaster Recovery (Value Stream), Point-in-Time Recovery (Capability) | RTO < 4 hours; RPO < 1 hour; data integrity verified | Maintenance Task |

---
