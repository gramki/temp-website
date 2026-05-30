# DR-019: Cross-Track Monitoring and Win Track Gap Remediation

**Status:** Accepted
**Date:** 2026-02-15

## Context

A gap analysis of the Win Track (and the Work Model generally) identified four areas where the stated purpose of the Win Track was not fully addressed by defined work entities:

1. **Continuous monitoring** — Every track has ongoing monitoring work that sits between periodic assessment (Reviews, Deliberations) and reactive work (Cases, Incidents). This work triggers downstream entities and feeds periodic reviews but was not modeled. The user requested monitoring as a work type in *each* track, not only the Win Track.

2. **Partner/channel work** — GTM and the lever portfolio mentioned "partnership execution" and "channel," but there were no work entities for partner-facing enablement or engagement. Products with partner/channel models have substantial Win Track work (partner onboarding, co-selling, partner enablement) that is distinct from internal sales enablement and customer engagement.

3. **Revenue realization** — The Revenue AAARRR stage had Expansion Engagement (upsell/cross-sell) but lacked (a) operational work to ensure revenue is collected (billing, invoicing, collections, renewal processing) and (b) explicit revenue monitoring. Revenue realization is an essential signal for Vendor Value; the Win Track is the right home for both commercial operations and revenue intelligence.

4. **PLG/self-service acknowledgment** — The model assumed human-mediated engagement. For segments where the Product lever dominates (self-service onboarding, free trial), the Win Track's role shifts from execution to monitoring + exception-based intervention. This needed to be acknowledged so that the same entities are interpreted correctly for PLG segments.

5. **Advocacy and customer education** — The question arose whether customer education was covered. It was concluded that CS Enablement and Segment Engagement already cover it (training materials, certification programs, webinars, workshops) under the advocacy umbrella; the plan was to make this explicit with examples rather than add new entities.

## Decisions

### 1. Introduce monitoring as a work entity in all four tracks

- **Discovery: Signal Monitoring** — Continuous tracking of signal pipeline health, discovery velocity, theme trends. Triggers: Prioritization re-evaluation, Signal creation, Deliberation scheduling.
- **Build: Build Monitoring** — Continuous tracking of build health, quality metrics, velocity. Triggers: Bug creation, Maintenance Task, Release Planning adjustment.
- **Run: System Monitoring** — Continuous tracking of infrastructure health, SLA/uptime, capacity. Triggers: Incident creation, Change Request, Capacity Planning adjustment.
- **Win: Win Monitoring** — Continuous tracking of customer health, revenue metrics, competitive intelligence, Customer Promise fulfillment. Includes revenue monitoring. Triggers: Win Activity creation, Win Case escalation, Win Review preparation.

Each monitoring entity has scope, metrics tracked, thresholds/alerts, cadence, owner, and produces Alert/Trigger and Report/Dashboard artifacts.

### 2. Add Partner Enablement and Partner Engagement to the Win Track

- **Partner Enablement** (subtype of Win Enablement) — Partner demo environments, co-marketing kits, partner training, certification programs, partner playbooks. Distinct from Sales Enablement (internal teams). Uses GTM lever.
- **Partner Engagement** (subtype of Win Activity) — Partner onboarding, co-selling, partner account management, partner pipeline management. Account-level (one partner). References external PRM.
- **Engagement Planning** scope extended to explicitly include partner prioritization and sequencing.

### 3. Add Revenue Operations Engagement and rely on Win Monitoring for revenue intelligence

- **Revenue Operations Engagement** (subtype of Win Activity) — Account-level, customer-facing work: invoicing/billing communication, collections, renewal processing, revenue recognition coordination. Advances Revenue Win Outcomes. Billing disputes remain Win Case (Complaint).
- **Revenue monitoring** — Covered by Win Monitoring (revenue metrics, pipeline, NRR, churn signals). When targets are missed, Win Monitoring surfaces the signal; Win Review or Feedback → Signal may follow.

### 4. Add PLG/self-service conceptual notes (no new entities)

- Win Activity entity and draft-work-model.md updated with a note: for segments where the Product lever dominates, engagement subtypes shift from human execution to monitoring + exception-based intervention; Win Monitoring becomes primary; Build Track delivers the in-product "Win" experience.

### 5. Clarify that advocacy encompasses customer education

- CS Enablement and Segment Engagement (and CS Planning) explicitly mention customer education/training, certification programs, knowledge bases, and training delivery. Examples added (e.g., "LATAM API integration certification program"). No new entities.

## Rationale

- **Monitoring in every track** — The same pattern (continuous vigilance → triggers reactive work, feeds periodic assessment) applies across Discovery, Build, Run, and Win. Making it explicit prevents the work from being invisible and clarifies how Incidents, Bugs, Win Activities, and Prioritization get triggered.
- **Partner work as subtypes** — Partners are intermediaries; they need enablement and engagement distinct from customers and from internal sales. Subtyping under existing parents keeps the model coherent and avoids a separate "partner track."
- **Revenue Operations as engagement** — Revenue realization work is account-level and customer-facing (invoicing, collections, renewals). It advances Revenue Win Outcomes. Modeling it as a Win Activity subtype is consistent with other account-level work; billing disputes stay in Win Case.
- **PLG as interpretation, not new structure** — The same subtypes apply; only the balance of human vs. product-mediated execution changes. A note suffices.
- **Education under advocacy** — Advocacy already included programs and materials; customer education (training, certification) fits as both enablement assets and segment engagement delivery. Explicit mention avoids a separate "customer education" entity.

## Consequences

### Positive
- All four tracks now model continuous monitoring; triggers and feeds are explicit.
- Partner/channel-heavy products can represent partner work without overloading the model.
- Revenue realization (operations + monitoring) is fully represented in the Win Track.
- PLG and self-service segments are correctly interpreted without new entities.
- Customer education is clearly in scope under advocacy.

### Negative
- Win Activity and Win Enablement have more subtypes; entity tables are longer.
- Monitoring entities are new and will need incremental detailing (artifacts, DoD) per the Work Execution Framework.
