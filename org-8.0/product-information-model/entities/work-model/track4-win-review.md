# Win Review

**Model:** Work Model
**Track:** Track 4: The Win Track (Value Realization)
**Category:** Review
**Owner:** Customer Success, Product Marketing, Sales

## Definition

A structured assessment activity that evaluates Win Track results across two dimensions — **vendor success** (Win Outcomes, Dim 2) and **customer promise fulfillment** (Customer Promises, Dim 3) — and produces two outputs: (1) qualitative Feedback observations and (2) quantitative target progress updates against Initiative targets. Win Review is the Win Track's parallel to Deliberation in the Discovery Track — both are structured assessment activities, but Win Review assesses market results while Deliberation assesses strategic evidence.

**Dual assessment scope:** Win Review assesses both sides of the commercial exchange. Keeping promises and winning are not the same thing — a product can keep every Customer Promise (99.9% uptime, sub-200ms latency) and still fail to achieve its Win Outcomes (CAC too high, Activation takes 90 days). Conversely, strong Win Outcomes with broken promises are a retention time bomb. Win Reviews surface both signals.

**Six Win Review types:**

1. **QBR (Quarterly Business Review)** — Account-level or segment-level review of customer health, value delivery, and expansion opportunities.
2. **Win/Loss Analysis** — Structured assessment of why a deal was won or lost, identifying patterns in competitive dynamics and sales effectiveness.
3. **Post-Implementation Review** — Assessment of onboarding and activation effectiveness after a customer goes live.
4. **Campaign/Program Review** — Evaluation of GTM campaigns, sales enablement programs, or CS programs against their intended outcomes.
5. **Case Pattern Review** — Analysis of Win Case patterns to identify systemic issues, recurring complaints, or cost-to-serve trends.
6. **Adoption Review** — Assessment of adoption-related Initiative target progress — are time-bound targets being met? What is driving or blocking adoption across AAARRR stages?

## Purpose

Provides structured reflection on Win Track results. Without Win Reviews:
- Customer health and value delivery are assessed informally without consistent structure
- Win/Loss patterns are not captured systematically
- The connection between Win Track execution and Initiative target progress is invisible
- Feedback is generated ad hoc rather than through a disciplined assessment process
- Case patterns accumulate without periodic analysis
- Customer Promise fulfillment is invisible to Win Teams — SLA breaches, unmet Value Propositions, and compliance gaps surface only through escalations rather than proactive assessment

**Two outputs, two destinations:**
1. **Feedback** (qualitative) — Observations recorded as Feedback artifacts. Feedback is a transitional artifact: it may be promoted to a Signal in Dim 1 if actionable, or archived if informational. May include observations about Customer Promise gaps.
2. **Target Progress** (quantitative) — Updates to Initiative target metrics. "Are we on track for the LATAM Acquisition target this quarter?" May include Customer Value Metric status alongside Business KPI status.

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Name of the review (e.g., "Q3 2026 LATAM Enterprise QBR") |
| Review Type | Enum | `QBR` / `Win-Loss Analysis` / `Post-Implementation Review` / `Campaign/Program Review` / `Case Pattern Review` / `Adoption Review` |
| Scope | Enum | `Account-level` / `Segment-level` |
| Customer / Segment | Reference (Dim 3) | Which customer or segment is being reviewed |
| Initiative(s) Assessed | List of References (Dim 1) | Which Initiative(s) this review assesses progress against |
| Participants | List of References (Dim 2) | Win Stakeholders participating in the review |
| Date | Date | When the review was conducted |
| Findings Summary | Text | Summary of key findings and observations |
| Target Progress | List (per Initiative target) | Quantitative assessment of progress against each Initiative target |
| Customer Promise(s) Assessed | List of References (Dim 3) | Which Customer Promises are assessed in this review (Value Propositions, Service Commitments, Compliance Posture) |
| Promise Fulfillment Status | List (per promise) | Assessment of whether each Customer Promise is being kept — references Customer Value Metrics for evidence |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Scheduled | Review is planned but not yet conducted |
| Conducted | Review has been held; findings are being documented |
| Findings Documented | Findings are recorded; Feedback artifacts created; target progress updated |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Produces | Feedback (Track 4) | Win Review produces Feedback artifacts (qualitative observations) |
| Assesses | Initiative (Dim 1) | Win Review assesses Initiative target progress and updates quantitative measures |
| Assesses | Win Engagement (Track 4) | Win Review assesses the results of Win Engagements |
| Assesses | Win Enablement (Track 4) | Campaign/Program Reviews assess enablement asset and program effectiveness |
| Assesses | Win Case (Track 4) | Case Pattern Reviews assess Win Case patterns |
| Assesses | Customer Promise (Dim 3) | Win Review assesses whether Customer Promises (Value Propositions, Service Commitments, Compliance Posture) are being fulfilled |
| References | Customer Value Metric (Dim 3) | Win Review references Customer Value Metrics as evidence of promise fulfillment |
| Participants are | Win Stakeholder (Dim 2) | Win Stakeholders participate in reviews |
| Scoped to | Customer Segment (Dim 3) | Win Review is scoped to a customer or segment |
| Assesses | API Module (Dim 6) | Win Review assesses API adoption, developer satisfaction, and SLO compliance |
| Assesses | API Compatibility Contract (Dim 6) | Win Review assesses contract compliance |

## Examples

| Review Type | Title | Scope | Customer/Segment | Initiative | Participants |
|---|---|---|---|---|---|
| QBR | "Q3 2026 LATAM Enterprise QBR" | Segment-level | LATAM Enterprise | LATAM Cross-Border Expansion | CS Manager, Account Executive, VP CS |
| Win/Loss Analysis | "Banco Nacional deal post-mortem" | Account-level | Banco Nacional (LATAM Enterprise) | LATAM Cross-Border Expansion | Account Executive, Pre-Sales Engineer, Sales VP |
| Post-Implementation Review | "GlobalPay SA activation review" | Account-level | GlobalPay SA (LATAM Enterprise) | LATAM Cross-Border Expansion | Implementation Consultant, CS Manager |
| Campaign/Program Review | "LATAM launch campaign effectiveness" | Segment-level | LATAM Enterprise | LATAM Cross-Border Expansion | Product Marketing, Demand Gen |
| Case Pattern Review | "Q3 LATAM support case pattern analysis" | Segment-level | LATAM Enterprise | LATAM Cross-Border Expansion | CS Manager, Support Lead |
| Adoption Review | "Q3 LATAM Activation target review" | Segment-level | LATAM Enterprise | LATAM Cross-Border Expansion | CS Manager, Product Marketing, VP CS |
| Adoption Review | "Q3 API adoption review: Cross-Border Payments API" | Segment-level | Developer segment | API Platform Initiative | CS Manager, Developer Relations, API Platform PM |
