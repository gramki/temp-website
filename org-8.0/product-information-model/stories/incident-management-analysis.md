# Incident Management in the UPIM: Analysis and Guide

## Why ITSM-Aligned Incident Management Matters

For enterprise SaaS products — particularly in regulated domains like fintech — incident management is not optional operational hygiene. It is a compliance requirement (PCI-DSS, SOC 2), a contractual obligation (SLA commitments), and a product quality signal. Customers evaluate products partly on *how incidents are handled*: transparency, speed, learning, and prevention.

The UPIM needs an incident management design that:

1. **Separates observation from response from learning** — so each can be assessed independently
2. **Provides structured severity classification** — so the organization responds proportionally
3. **Enables incident correlation** — so a single root cause isn't counted as N incidents
4. **Closes feedback loops** — to Run Track planning, Discovery, Build, Win, and the Definition Model
5. **Tracks SLA performance** — so Customer Promises (Dim 3) are evidenced, not assumed

## The Artifact/Entity Separation

The foundational design decision is that an Incident is a **work artifact** (an observation record), not a work entity (work to be done). This parallels the Deployment pattern established in DR-029:

| Pattern | Work Entity | Work Artifact |
|---|---|---|
| Deployment | Deployment Task (applies descriptor) | Deployment (record of what was applied) |
| Incident | Incident Response Task (triage, resolve) | Incident (record of what happened) |

Three work entities handle the incident lifecycle:

### 1. Incident Response Task

The primary response entity. Triage, investigate, mitigate, resolve. Its Definition of Done is deliberately narrow: **service restored to SLO-compliant state**. Root cause elimination is downstream work — a Bug for the Build Track, a Run Epic for operational tooling, a Signal for Discovery.

This narrow DoD is critical. Without it, incident response tasks stay open until a permanent fix ships, which conflates two fundamentally different timelines: "restore service now" (hours) and "fix the root cause" (days/weeks). The Incident Response Task captures the workaround applied, preliminary root cause assessment, and resolution summary — then hands off.

### 2. Post-Incident Review

The learning entity. Parallels Deliberation (Track 1) and Win Review (Track 4). PIR produces the Post-Incident Report (durable knowledge artifact) and routes corrective actions to appropriate tracks.

The PIR mandate — SEV-0, SEV-1, and SEV-2 incidents require PIR — is a Work Model default. The Operating Model can adjust: require PIR for all SEV-3 incidents in a mission-critical module, or waive PIR for SEV-2 incidents resolved within 15 minutes with no customer impact.

PIR is **blameless by design**. The entity structure captures "Contributing Factors" (systemic conditions) rather than "Who caused this." This is a modeling choice that the Operating Model reinforces through ceremony design.

### 3. Customer Communication Task

The communication entity. Status page updates, affected-tenant notifications, resolution summaries. Run Track owns this because SRE/DevOps has real-time technical context. Win Track consumes summarized views.

## The SEV-Based Severity Model

| Severity | Scope | Workaround | PIR | Example |
|---|---|---|---|---|
| SEV-0 | Total service outage; all tenants | None | Required | Complete payment processing failure across all environments |
| SEV-1 | Major degradation; significant tenant impact | Limited or none | Required | FX API latency 5000ms; cross-border payments timing out |
| SEV-2 | Partial degradation; subset of tenants/capabilities | Available | Required | Settlement file generation delayed 4 hours; manual export works |
| SEV-3 | Minor degradation; limited customer-visible impact | Available | Operating Model decision | Dashboard loading slowly (8s vs. 2s) |
| SEV-4 | Minimal degradation; no customer-visible impact | N/A | No | Background reconciliation running 20% slower |

Why SEV-0..4 instead of P1/P2? P1/P2 is overloaded — some organizations use P for priority, others for severity. SEV-N is unambiguous. SEV-0 provides a level above SEV-1 for total outages.

## Cross-Track Feedback Loops

Incidents are not contained within the Run Track. They produce structured outputs that flow across the entire UPIM:

### From Incident Response Task

- **Bug (Track 2)** — root cause is a product defect; provenance: Run; carries Workaround field for Known Error documentation
- **Signal — Problem (Track 1)** — recurring or systemic issue surfaced for Discovery
- **Emergency Change Request (Track 3)** — SEV-0/SEV-1 requiring immediate deployment fix

### From Post-Incident Review

- **Post-Incident Report** — durable knowledge artifact
- **Bug (Track 2)** — deeper root cause identified during RCA
- **Run Epic (Track 3)** — operational tooling gap (e.g., missing probes, manual failover)
- **Signal (Track 1)** — systemic product issue for Discovery
- **ODR (Dim 7)** — operational decision (e.g., "multi-AZ deployment required for stateful services")
- **Evolve Finding (Track 5)** — process gap (e.g., "runbook was outdated", "escalation policy unclear")
- **Maintenance Task (Track 3)** — corrective maintenance

## Incident-to-Planning Feedback

Beyond PIR and Discovery, incidents inform Run Track planning:

| Planning Entity | What Incident History Provides |
|---|---|
| **Deployment Planning Task** | Risk assessment input — a module with recent SEV-1 incidents may warrant cautious deployment (canary, drill) or block promotion at a Station |
| **Capacity Planning Task** | Capacity forecasting input — incidents caused by resource saturation, throttling, or scaling failures directly inform infrastructure planning |
| **Run Epic scoping** | Prioritization input — "3 SEV-2 incidents from manual cert rotation" justifies an automation Run Epic directly, without waiting for Discovery |

This three-consumer model (PIR looks backward, Discovery looks at systemic patterns, Run planning looks forward operationally) ensures incident data is fully utilized.

## Definition Model Assessment Patterns

Incidents are evidence against the product's promises. The UPIM makes these assessment connections explicit:

### Dim 3: Customer Value Dimension

- **Customer Promise (Service Commitment)** — every SEV-0/1/2 incident *tests* whether Service Commitments are being met. The Incident artifact's SLA Breach field records which commitments were tested and whether they held.
- **Customer Value Metric (Service Level Metric)** — incident response/resolution times feed the actual performance data. "SEV-1 MTTR this quarter: 3.2 hours vs. 4-hour SLA" is derived from Incident artifacts.
- **Customer Promise (Compliance Posture)** — incidents involving data breaches or audit-trail gaps may constitute compliance violations.

### Dim 7: Operational Dimension

- **Operational Target (SLO)** — incidents consume error budget. Every incident erodes the margin between current performance and the target.
- **Operational Readiness** — incident patterns per System x Environment reveal readiness gaps. "payments-service has 3 SEV-1s in LATAM but zero in NA" indicates LATAM-specific readiness issues.
- **Operational Pain** — recurring incident patterns are concrete evidence for Operational Pains. "Manual certificate rotation causes 2 SEV-1 incidents per quarter" is a documented Operational Pain with measurable impact.
- **Operational Constraint** — incidents may reveal undocumented constraints (e.g., "compliance freeze prevented hotfix during incident").

### Dim 5: Technology & Architecture

- **System** — incidents are scoped to affected Systems. System-level incident rates inform Build Track quality gate evolution.
- **Interaction Flow** — incidents often reveal failure points in cross-system flows. The Post-Incident Report references which Interaction Flow failed and where.

## Known Error / Workaround Pattern

When an Incident is resolved with a workaround (not a permanent fix), the resulting Bug carries the workaround description in its `Workaround` field. This makes the workaround discoverable for future incidents of the same type — the Bug serves as the Known Error registry until the permanent fix ships. No new entity is needed; the pattern reuses the existing Bug entity.

## Incident Correlation

### Parent-Child Incidents

A single root cause (database failover) can trigger multiple symptoms (FX latency spike, payment timeouts, settlement delays). The Parent Incident field prevents counting 4 incidents when there is 1 root cause with 3 symptoms. Impact assessment is centralized on the parent; child incidents reference it.

### Related Incidents (Recurrence)

When the same type of incident occurs repeatedly, the Related Incidents field links them. This makes recurrence queryable before a formal PIR pattern analysis. "This is the third SEV-2 from cert expiration in 6 months" is visible from the Incident artifact itself.

### Change-Caused Incidents

The Caused By field references a Deployment (artifact) or Change Request when the incident was caused by a deployment. This closes the deployment-to-incident feedback loop:

- Deployment quality assessment: "What percentage of deployments cause incidents?"
- Verification Task effectiveness: "Are our post-deployment checks catching problems?"
- Deployment Train governance: "Should we tighten promotion criteria for this module?"

## Escalation Within Response

The Incident Response Task captures escalation as fields (Escalation Level: L1/L2/L3/Vendor; Escalated To). The escalation *policy* — who gets called at each level — is an Operating Model concern. Similarly, Major Incident coordination (Incident Commander role, war-room ceremonies) is Operating Model territory; the Incident Response Task's timeline and decision fields capture the coordination artifacts.

## Pros and Cons

### Pros

1. **Clear separation of concerns** — observation, response, learning, and communication are distinct entities with appropriate fields and statuses
2. **ITSM alignment** — familiar to practitioners; maps cleanly to ServiceNow, PagerDuty, and other ITSM tooling
3. **No entity proliferation** — Known Error reuses Bug; no new entity for workarounds, escalation tracking, or incident coordination
4. **Rich Definition Model connections** — incidents are evidence, not noise; they test Customer Promises, consume error budgets, reveal readiness gaps
5. **Planning feedback** — incident history is a first-class input to Run Track planning, not an afterthought
6. **Correlation prevents overcounting** — parent/child and related incidents give accurate root cause counts

### Cons

1. **More entities to maintain** — 3 new work entities + 1 refactored artifact adds model complexity
2. **"Reviewed" terminal status requires discipline** — organizations must close the loop from incident to PIR to "Reviewed" status
3. **SEV calibration** — SEV-0..4 scale requires organizational agreement on severity definitions
4. **PIR mandate creates work** — requiring PIR for SEV-0/1/2 creates scheduled work that teams may resist; the Operating Model override mitigates this

### Do's and Don'ts

| Do | Don't |
|---|---|
| Use SEV labels consistently across all UPIM documents | Mix SEV and P-level terminology |
| Close the Incident to "Reviewed" after PIR or planning absorption | Leave incidents in "Resolved" indefinitely |
| Link change-caused incidents to their Deployment via Caused By | Treat post-deployment incidents as unrelated to the deployment |
| Capture workarounds on the Bug's Workaround field | Create a separate Known Error entity |
| Let PIR route corrective actions to appropriate tracks | Keep all follow-up work within the Run Track |
| Use Parent Incident for multi-symptom root causes | Count each symptom as a separate root cause incident |

---
