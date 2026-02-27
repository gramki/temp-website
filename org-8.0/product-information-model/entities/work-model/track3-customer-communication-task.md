# Customer Communication Task

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Category:** Work Entity (Reactive)
**Owner:** SRE, DevOps, Engineering Leadership

## Definition

The work of communicating incident status, impact, and resolution to affected parties — including status page updates, affected-tenant notifications, internal stakeholder updates, and resolution summaries. Customer Communication Task runs in parallel with Incident Response Task; the Run Track owns incident communication because the communicators need real-time access to technical context (blast radius, mitigation progress, ETA).

> **Run Track ownership, Win Track consumption.** The Run Track produces incident communications because the SRE/DevOps team has the technical context. The Win Track consumes summarized or enhanced views of incidents in their regular communication routines — Win Reviews, QBRs, and proactive customer outreach. The Win Track does not duplicate incident communication; it references Run Track outputs.

## Purpose

Makes incident communication visible as structured work. Without Customer Communication Task:
- Communication during incidents is ad hoc and inconsistent
- There is no record of what was communicated, when, and to whom
- The effectiveness of communication cannot be assessed in Post-Incident Review
- Status page updates, tenant notifications, and internal updates are invisible work that competes with response effort
- The handoff from Run Track communication to Win Track follow-up is informal

## Fields

| Field | Type | Description |
|---|---|---|
| Incident | Reference (Track 3) | The Incident artifact this communication addresses |
| Incident Response Task | Reference (Track 3) | The associated response task (for coordination) |
| Communication Channel(s) | List (Enum) | `Status Page` / `Tenant Notification` / `Internal Slack/Teams` / `Email` / `Phone` / `Customer Portal` |
| Audience | Enum | `All Tenants` / `Affected Tenants` / `Internal Stakeholders` / `Specific Customers` |
| Updates Issued | List (timestamp + channel + content summary) | Chronological record of communications sent |
| Resolution Summary (External) | Text | Customer-facing summary of what happened and what was done — sanitized for external consumption |
| Follow-up Committed | Text | Any commitments made to customers during communication (e.g., "we will provide a full RCA within 48 hours") |

## Statuses

| Status | Description |
|---|---|
| Active | Incident is ongoing; communications are being issued |
| Resolved | Incident is resolved; resolution summary has been communicated |
| Closed | All committed follow-ups have been delivered (e.g., RCA shared, credits applied) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Communicates | Incident (Track 3) | Communicates the status and resolution of an Incident |
| Coordinates with | Incident Response Task (Track 3) | Runs in parallel; communication content depends on response progress |
| Assessed by | Post-Incident Review (Track 3) | PIR evaluates communication effectiveness (timeliness, accuracy, coverage) |
| Consumed by | Win Review (Track 4) | Win Track consumes summarized incident communication in reviews |
| Consumed by | Win Activity (Track 4) | Win Track may reference communication outputs in proactive customer engagement |
| May reference | Service Commitment (Dim 3) | Communication may acknowledge SLA breach and reference remedies |

## Examples

| Incident | Channels | Audience | Key Updates | Status |
|---|---|---|---|---|
| INC-2026-0849 "Database cluster failover" | Status Page, Tenant Notification, Internal Slack | All Tenants + Internal | "14:30 — Investigating degradation across all services", "14:45 — Root cause identified: AZ failure; failover in progress", "15:10 — Services restored; monitoring for stability", "15:30 — All clear; full RCA to follow within 48h" | Closed |
| INC-2026-0850 "Post-deployment error rate" | Tenant Notification, Internal Slack | Affected Tenants (LATAM) + Internal | "16:00 — Elevated error rate in LATAM payments; investigating", "16:20 — Deployment rolled back; service restored", "16:30 — No data loss confirmed; RCA in progress" | Resolved |
| INC-2026-0851 "Compliance dashboard stale" | Email | Specific Customers (reporter) | "Acknowledged; cache issue identified and resolved. Dashboard now showing current data." | Closed |

---
