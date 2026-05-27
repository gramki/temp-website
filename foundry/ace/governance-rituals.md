# Governance Rituals in ACE

This document defines the recommended governance ritual catalog for an enterprise software factory using ACE.

It distinguishes **Governance Rituals** from normal **Work / Team Operating Cadences**. Governance does not own every team ceremony. Governance defines controls over adherence, evidence, outputs, and trends from those cadences.

## What counts as a Governance Ritual

A Governance Ritual is a cadence-based or event-triggered review, decision, or control practice. It consumes reports, dashboards, metrics, evidence, orchestration items, Work Orders, and register entries. It produces decisions, action items, findings, approvals, exceptions, debt/catch-up outcomes, recognition, and sometimes Evolve Cases.

User-facing labels may use "Review", "Forum", or "Cadence" for familiarity; the model term is **Governance Ritual**.

## What is not a Governance Ritual

Daily and sprint ceremonies are primarily Work / Team Operating Cadences:

- Daily Flow Review
- Sprint / Iteration Planning
- Sprint / Iteration Review
- Sprint / Iteration Retrospective

Governance may assert controls over these cadences:

- cadence occurred;
- required outputs were recorded;
- action items are tracked;
- severe blockers are escalated;
- repeated retrospective items trigger Evolve Cases;
- recognition is captured where appropriate.

## Recommended Governance Rituals

### Product Intent Review

**Cadence:** Weekly or biweekly
**Scope:** Workbench / Product

**Purpose:** Review Product Intent formation, progression, and blockers.

**Control Objectives:**
- Product Intents have decision provenance.
- Product Intent purpose is correct.
- Delivery intents link to Customer Release Intent where required.
- Stalled intents are addressed.
- Governance findings are visible.

**Control Objective Indicators:**
- Product Intent status.
- Product Intent purpose.
- PDR linkage.
- missing Customer Release Intent link.
- age in status.
- open findings.
- active debt/exceptions.

### Discovery Case Decision Review

**Cadence:** Weekly or biweekly
**Scope:** Workbench / Product

**Purpose:** Review Discovery Cases for decision readiness.

**Control Objectives:**
- Discovery Cases have clear origin and question.
- Evidence is sufficient for decision.
- PM alignment is recorded where product direction changes.
- Cases do not age indefinitely.

**Control Objective Indicators:**
- case age.
- evidence completeness.
- PDR readiness.
- PM alignment status.
- cases without recent activity.
- cases awaiting deliberation.

### Architecture Decision Review

**Cadence:** Weekly, biweekly, or event-triggered
**Scope:** Product, Workbench, platform, or architecture forum

**Purpose:** Review architecture decisions, technical ideas, and refactoring proposals.

**Control Objectives:**
- Architecture work is tied to Product Intent or Discovery Case.
- ADR exists for significant decisions.
- Refactors outside Product Intent are routed properly.
- Architecture risks are visible.

**Control Objective Indicators:**
- architecture concerns without Discovery Case.
- ADR completeness.
- technical validation intents.
- open architecture risks.
- refactoring debt.
- unresolved design decisions.

### Build Quality Review

**Cadence:** Weekly or per release candidate
**Scope:** Workbench / Build Track

**Purpose:** Review build/release quality controls.

**Control Objectives:**
- Build quality controls are met.
- Hard fails block.
- Debt + Catch-Up is approved only where allowed.
- Repeated failures trigger remediation or Evolve.

**Control Objective Indicators:**
- Control Objective compliance.
- Control Objective Indicator trends.
- hard-fail count.
- debt-required count.
- overdue debt.
- test pass rate.
- security scan status.
- coverage trend.
- critical defect count.

### Release Readiness Review

**Cadence:** Per release / event-triggered
**Scope:** Product Intent / Customer Release Intent

**Purpose:** Decide whether Product Delivery or Customer Release Intent realization is ready.

Release Readiness is multi-dimensional. It is not only QA or build quality.

See [Release Readiness control families](#release-readiness-control-families).

### Monthly Workbench Governance Review

**Cadence:** Monthly
**Scope:** Workbench

**Purpose:** Review operating health of the Workbench.

**Control Objectives:**
- cost, velocity, efficiency, and predictability are within expected bands;
- risks, debt, exceptions, and findings are under control;
- team/agent operating health is understood;
- recognition and reusable practices are surfaced.

**Control Objective Indicators:**
- cost per Work Order.
- cost per Product Intent.
- cycle time.
- throughput.
- velocity trend.
- rework rate.
- debt aging.
- exception aging.
- risk aging.
- agent intervention rate.
- recognition trends.
- action item closure rate.

These indicators are governance signals of operating health, not individual surveillance metrics.

### Quarterly Governance / Operating Model Review

**Cadence:** Quarterly
**Scope:** Foundry, Workshop, portfolio, or Workbench group

**Purpose:** Improve governance practices and the Operating Model.

**Control Objectives:**
- governance policies remain relevant;
- rituals are effective;
- dashboards support decisions;
- repeated findings trigger Evolve Cases;
- positive patterns become reusable practices.

**Control Objective Indicators:**
- repeated findings.
- policy update requests.
- ritual completion rate.
- action item closure rate.
- governance cycle time.
- Evolve Cases opened/closed.
- reusable practice candidates.
- audit readiness.

### Exception / Debt Review

**Cadence:** Weekly, monthly, or due-date driven
**Scope:** Workbench / governance domain

**Purpose:** Review exceptions, waivers, active debt, and catch-up plans.

**Control Objectives:**
- all debt has Catch-Up Plans;
- exceptions have expiry/conditions;
- overdue debt is escalated;
- repeated debt triggers Evolve.

**Control Objective Indicators:**
- active debt count.
- overdue debt.
- debt age.
- expiring exceptions.
- catch-up completion rate.
- repeated debt by control.

### Compliance Evidence Review

**Cadence:** Monthly, quarterly, audit-period, or event-triggered
**Scope:** Compliance domain / Workbench / Foundry

**Purpose:** Review audit and compliance readiness.

**Control Objectives:**
- required compliance evidence exists;
- evidence is current;
- audit package is complete;
- exceptions/debt affecting compliance are visible.

**Control Objective Indicators:**
- evidence completeness.
- stale evidence count.
- missing approval records.
- audit readiness score.
- compliance control status.

## Work and team operating cadences governed by controls

These are Work / Workforce operating cadences. Governance controls their adherence and outputs; governance does not own the cadence itself.

| Cadence | Governance controls |
|---------|---------------------|
| **Daily Flow Review** | Blockers captured; aging WIP reviewed; severe blockers escalated. |
| **Sprint / Iteration Planning** | Commitments recorded; capacity considered; dependencies identified. |
| **Sprint / Iteration Review** | Completed work evidenced; carryover explained; outcomes recorded. |
| **Sprint / Iteration Retrospective** | Action items captured; repeated issues routed to Evolve; recognition captured. |

## Release Readiness control families

### 1. Build Quality Readiness

Indicators:
- tests passed;
- coverage threshold;
- critical bugs;
- static analysis;
- security scan;
- artifact signing;
- provenance.

### 2. Documentation Readiness

Indicators:
- release notes;
- customer-facing docs;
- admin guide;
- user guide;
- developer/API docs;
- migration guide;
- support knowledge base;
- known limitations.

### 3. SRE / Operational Readiness

Indicators:
- deployment runbook;
- rollback plan;
- monitoring dashboards;
- alerts;
- SLIs/SLOs;
- capacity validation;
- on-call readiness;
- incident response path;
- operational readiness assessment.

### 4. Security Readiness

Indicators:
- vulnerability scan;
- threat model;
- secrets/config review;
- access control review;
- data classification;
- compliance controls.

### 5. Evidence Readiness

Indicators:
- PDR linked;
- Product Intent linked;
- PSD approved;
- QA evidence;
- release evidence pack;
- approval records;
- open debt/exception reviewed;
- audit trail.

### 6. Customer Readiness

Indicators:
- Customer Release Intent linked;
- rollout plan;
- customer communication;
- support briefing;
- training material;
- customer promise impact.

### 7. GTM Readiness

Indicators:
- pricing/package updates;
- sales enablement;
- CS enablement;
- partner communication;
- launch messaging;
- Win outcomes / KPIs.

### 8. Data / Migration Readiness

Indicators:
- migration plan;
- backfill plan;
- rollback plan;
- data quality checks;
- retention impact;
- schema changes validated.

### 9. Dependency Readiness

Indicators:
- upstream/downstream readiness;
- third-party integration validation;
- feature flags;
- environment dependencies;
- cross-system compatibility.

## Phase maturity

| Maturity | Ritual guidance |
|----------|-----------------|
| Phase 1 | Release Readiness Review, Build Quality Review, Product Intent Review, basic Exception / Debt Review |
| Phase 2 | Discovery Case Decision Review, Architecture Decision Review, Monthly Workbench Governance Review |
| Phase 3 | Quarterly Governance / Operating Model Review, richer compliance evidence review, governance trend rituals |
