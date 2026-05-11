# FIR (First Information Report) — Universal Intake Analysis

## Overview

The First Information Report (FIR) is the UPIM's universal intake entity for all product-in-operation feedback. Every piece of feedback — whether from an external customer, an SRE detecting a monitoring alert, or a QA engineer observing a regression — enters the system as an FIR. This document analyzes why universal intake matters, how the FIR triage-and-route pattern works, and what the consequences are for the broader product information model.

## Why Universal Intake Matters

### The Problem Without FIR

In a typical product organization, feedback arrives through fragmented channels:
- A customer emails support about latency. Support creates a ticket in the CRM.
- An SRE sees a monitoring alert. They create an incident in PagerDuty.
- A QA engineer finds a regression. They file a bug in Jira.
- A PM notices a capability gap during a customer call. They add a note to a backlog.

These four events may describe the same underlying issue — a deployment caused a latency regression that the customer felt, the monitoring system detected, QA noticed in test environments, and the PM heard about qualitatively. But they exist in four disconnected systems with four different lifecycles, four different owners, and no common parent. Nobody can answer:

1. **"How many feedback events did we receive this month?"** — you'd need to aggregate across CRM, PagerDuty, Jira, and ad-hoc notes.
2. **"Given this customer complaint, what internal work was done?"** — you'd need to manually trace from the CRM ticket to the incident to the bug to the fix.
3. **"Given this bug fix, where did the defect report come from?"** — the bug may say "found in production" but the chain back to the customer is lost.
4. **"Was the customer notified when the issue was resolved?"** — impossible to know without a reporter-facing lifecycle.

### The ITSM Single-Point-of-Contact Principle

ITIL and ITSM frameworks establish the principle of a "single point of contact" (SPOC) for all service interactions. Every interaction with the service desk starts with a record — regardless of whether it becomes an incident, a service request, a change, or just a question. The record ensures nothing is lost, everything is traceable, and the reporter has a consistent experience.

FIR adapts this principle for the UPIM context, extending it beyond the Run Track (incidents) to encompass all tracks: Win (complaints, queries), Build (bugs from customers), and Discovery (signals from product-in-operation feedback).

## The FIR Triage-and-Route Pattern

### Creation

An FIR is created when product-in-operation feedback arrives from any source:

| Source | Provenance | Typical Channel | Example |
|---|---|---|---|
| Customer | External | Portal, Email, Chat, Phone | "Your FX API was down for 3 hours during our peak" |
| Partner | External | Portal, Email | "Our integration is returning 500 errors since yesterday" |
| SRE | Run | Monitoring Alert, Internal Observation | "P95 latency spiked to 5000ms on fx-service" |
| QA | Build | Internal Observation | "Regression in payment timeout handling in staging" |
| Support (proactive) | Internal | Internal Observation | "Three customers mentioned settlement delays this week" |
| Monitoring System | Run | Monitoring Alert | "Health check failure on payments-service in prod-latam" |

### Triage

The Win team's customer support function triages FIRs. Triage involves:

1. **Understand the report:** Read the original description, correlate with monitoring data, check for duplicate FIRs.
2. **Categorize:** Assign a pre-triage category (Service Degradation, Defect, Missing Capability, Question, Request, Dissatisfaction, Observation).
3. **Assess priority:** Critical / High / Medium / Low.
4. **Route:** Create sub-items in the appropriate tracks.
5. **Record:** Document the Triage Assessment with routing rationale.

### Routing Outcomes

| FIR Category | Typical Routing | Track | Entity |
|---|---|---|---|
| Service Degradation | Incident + Win Case (complaint) | Track 3 + Track 4 | Incident artifact + Win Case |
| Defect | Bug | Track 2 | Bug (provenance: Win or Run) |
| Missing Capability | Signal (Need) | Dim 1 | Need |
| Dissatisfaction | Win Case (complaint) + possibly Signal (Problem) | Track 4 + Dim 1 | Win Case + Problem |
| Question | Direct resolution (zero sub-items) | — | — |
| Request | Win Case (service request) | Track 4 | Win Case |
| Observation | Signal (Problem or Opportunity) | Dim 1 | Problem or Opportunity |

### Direct Resolution

Trivial inquiries ("What currencies do you support?") can be resolved at triage with zero sub-items. The FIR transitions Created -> Triaged -> Resolved -> Closed. The Triage Assessment captures the response. This prevents noise in downstream tracks while still recording the interaction for volume metrics.

## The Always-FIR-First Principle

**Win Cases cannot be created independently.** Every Win Case is a sub-item of an FIR. This is the most consequential design decision in DR-032.

### Why So Strict?

If Win Cases can exist without an FIR, there is a bypass path that breaks the traceability chain. A CS Manager creates a complaint directly during a QBR — it has no FIR parent, no record of the original report, and doesn't count toward FIR volume metrics. The "universal" in universal intake is no longer universal.

The overhead of creating an FIR for every interaction is minimal:
- For customer-initiated interactions (email, portal, chat), the FIR is created as part of the standard intake workflow.
- For proactive observations (QBR findings, field observations), the Win team member logs an FIR and routes from it.
- For trivial inquiries, the FIR is resolved at triage in seconds.

### Cross-Track Traceability

The FIR-first principle enables full cross-track traceability chains:

```
FIR-2026-04291 (Customer: "FX API was down for 3 hours")
  ├── INC-2026-0847 (Track 3: Service degradation - SRE investigating)
  │     └── BUG-2026-0893 (Track 2: Root cause fix - provenance: Run)
  │           └── SV-payments-v3.2.1 (Track 2: System Version with fix)
  │                 └── DEP-2026-0315 (Track 3: Deployment to production)
  ├── WC-2026-1203 (Track 4: Complaint - customer communication)
  └── SIG-2026-0412 (Dim 1: Problem signal - "FX cache invalidation fragile")
        └── IDEA-2026-0089 (Dim 1: "Replace FX cache with event-driven refresh")
```

Every node in this chain carries references back to the parent FIR. Win Reviews can assess the entire chain: "From initial report to resolution, how long did it take? How many tracks were involved? Was the customer notified at each stage?"

## Auto-Routing for Monitoring Alerts

When a monitoring system detects an alert, an FIR can be auto-created and auto-routed. The FIR still exists as the intake record, but triage is automated rather than human.

**How it works:**
1. Monitoring system detects alert (e.g., P95 > 500ms threshold).
2. FIR is auto-created: Provenance: Run, Reporter Type: Monitoring System, Category: Service Degradation.
3. Auto-routing rules (defined in the Operating Model) create an Incident in Track 3.
4. If the alert affects customer-facing services, the auto-routing may also create a Win Case for proactive customer notification.

**Why allow automation?** Requiring human triage for every monitoring alert would create unsustainable overhead. The Provenance field distinguishes auto-routed FIRs from human-triaged ones, enabling separate quality assessment and metric tracking.

**Risk:** Incorrect auto-routing. The Operating Model must define which categories and provenances permit auto-routing and establish escalation paths when auto-routing produces incorrect results.

## PFR-Win as the Comprehensive Origination Point

With FIR-first in place, PFR-Win becomes the single, comprehensive origination point for all product-in-operation feedback:

- Every customer complaint starts as an FIR in PFR-Win.
- Every monitoring alert that creates an FIR starts in PFR-Win (even though the Incident lives in OPR).
- Every QA regression report that creates an FIR starts in PFR-Win (even though the Bug lives in WR).
- Every operator observation that creates an FIR starts in PFR-Win.

PFR-Run and PFR-Build hold references (mirrors) back to OPR Incidents and WR Bugs respectively, providing the feedback perspective without duplicating data.

## Pros

1. **Complete traceability** from initial report through resolution across all tracks.
2. **Accurate volume metrics** — FIR count is the authoritative measure of total feedback burden.
3. **Reporter-facing lifecycle** — the reporter interacts with FIR status (notified on triage, progress, resolution) while internal sub-items are invisible to them.
4. **Cross-track correlation** — the same FIR producing Incident + Win Case + Signal reveals that these are facets of one event, not three independent issues.
5. **Win Review intelligence** — Win Reviews can assess triage quality, routing patterns, resolution quality, and FIR-to-resolution time.
6. **Pattern detection** — FIR volume trends by category, customer, channel, and module reveal systemic issues before they become crises.

## Cons

1. **Process overhead** — every feedback interaction requires an FIR, adding a step to existing workflows.
2. **Auto-routing complexity** — rules must be carefully designed to avoid incorrect routing; poorly designed rules create noise.
3. **Operating Model dependency** — FIR triage process, escalation protocols, Run team FIR creation ceremony, and resolution notification must all be defined in the Operating Model.
4. **Cultural adoption** — teams accustomed to creating Incidents or Bugs directly must adapt to the FIR-first workflow.

## Dos and Don'ts

**Do:**
- Create an FIR for every piece of product-in-operation feedback, no matter how trivial.
- Use direct resolution for trivial inquiries — don't force sub-item creation.
- Maintain bidirectional references between FIR and all sub-items.
- Track FIR volume, resolution time, and routing patterns in Win Monitoring.
- Periodically assess triage quality and auto-routing accuracy in Win Reviews.

**Don't:**
- Allow Win Cases, Incidents, or Bugs to be created without an FIR parent (when the feedback originated from product-in-operation observation).
- Conflate FIR with Feedback — FIR is reactive event-driven intake; Feedback is synthesized assessment from Win Reviews.
- Auto-route categories that require human judgment (e.g., Dissatisfaction, Missing Capability).
- Use FIR as a replacement for Build Track bug discovery — Bugs found during development/testing (provenance: Build) don't need FIRs, only Bugs originating from product-in-operation feedback do.

## Related Decisions and Entities

- **DR-032:** FIR and Universal Intake Pattern (6 decisions)
- **Entity:** `track4-fir.md` — full field, status, relationship definitions
- **Entity:** `track4-win-case.md` — updated with required Originating FIR field
- **Narrative Seed 8:** FIR — Universal Intake
