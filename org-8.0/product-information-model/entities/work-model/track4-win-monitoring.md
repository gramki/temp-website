# Win Monitoring

**Model:** Work Model
**Track:** Track 4: The Win Track (Value Realization)
**Category:** Monitoring
**Owner:** Customer Success, Product Marketing, Sales Operations

## Definition

Continuous tracking of customer health (adoption, usage, NPS), revenue metrics (pipeline, NRR, churn signals), competitive intelligence, and Customer Promise fulfillment metrics. Win Monitoring sits between periodic assessment (Win Review) and reactive work (Win Case, Win Activity) — it surfaces at-risk accounts, expansion opportunities, competitive threats, and promise gaps before they become crises.

Win Monitoring is the Win Track's instantiation of the cross-track monitoring pattern. It includes **revenue monitoring** — tracking revenue metrics and surfacing signals when targets are missed — which feeds Win Review and may trigger Retention or Expansion Engagement.

## Purpose

Makes the continuous oversight of commercial and customer health explicit. Without Win Monitoring:
- At-risk accounts are discovered only when they churn or escalate
- Expansion opportunities are found only during periodic QBRs
- Competitive threats and Customer Promise gaps surface only through Win Cases
- Revenue target misses are visible only at review time

**Triggers downstream work:** Win Activity creation (Retention, Expansion), Win Case escalation, Win Review preparation, Feedback → Signal when patterns warrant Discovery investigation.

## Fields

| Field | Type | Description |
|---|---|---|
| Scope | Text | What is being monitored (e.g., "LATAM Enterprise — health and revenue", "All segments — pipeline and NRR") |
| Metrics Tracked | List (text or reference) | Customer health score, adoption/usage, NPS, pipeline value, NRR, churn indicators, Customer Value Metric status, competitive win/loss trends; **API SLO compliance**, **developer adoption metrics** (when product has Dim 6 surfaces) |
| Thresholds / Alerts | List (text) | When does monitoring trigger action (e.g., "Health score drop > 20 points", "Account inactive 30 days", "Pipeline stage stall > 45 days") |
| Cadence | Enum | `Continuous` / `Daily` / `Weekly` |
| Owner | String | Role/person responsible for watching |
| Customer Segment(s) | List of References (Dim 3) | Which segment(s) this monitoring covers |
| Initiative(s) | List of References (Dim 1) | Which Initiative(s) this monitoring supports |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Active | Monitoring is in effect; thresholds and cadence are defined |
| Paused | Monitoring is temporarily suspended |
| Retired | Monitoring scope is no longer relevant |

## Outputs / Artifacts

| Artifact | Category | Description | Downstream Consumer |
|---|---|---|---|
| Alert / Trigger | Evidence | When threshold is breached — prompts Win Activity, Win Case escalation, or Win Review | Win Activity, Win Review |
| Health / Revenue Report / Dashboard | Assessment | Periodic snapshot of customer health, revenue metrics, promise fulfillment | Win Review preparation, Initiative target tracking |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| May trigger | Win Activity (Track 4) | Monitoring surfaces need for Retention or Expansion engagement |
| May trigger | Win Case (Track 4) | Monitoring may surface need for case escalation |
| Feeds | Win Review (Track 4) | Dashboards and reports feed Win Review preparation |
| May produce | Feedback (Track 4) | Patterns may become Feedback and then Signal |
| References | Business KPI (Dim 2) | Revenue and cost metrics are tracked |
| References | Customer Value Metric (Dim 3) | Promise fulfillment metrics are tracked |
| References | API Operation (Dim 6) | Monitors API SLO compliance per operation (when product has API surfaces) |
| Scoped to | Customer Segment (Dim 3) | Monitoring is scoped to segment(s) |
| Aligned to | Initiative (Dim 1) | Monitoring supports Initiative target tracking |

## Example

"Monitor LATAM Enterprise accounts — daily health score and usage; alert on health drop > 15 points or 14 days inactive. Weekly revenue report: NRR, pipeline, churn risk. Owner: CS Manager. Triggers Retention Engagement; feeds QBR and Adoption Review."

"Monitor Cross-Border Payments API — API SLO compliance per operation (p99 latency, availability); developer adoption metrics (active integrations, time-to-first-call). Alert on SLO breach or adoption drop. Owner: API Platform PM. Feeds API adoption review."
