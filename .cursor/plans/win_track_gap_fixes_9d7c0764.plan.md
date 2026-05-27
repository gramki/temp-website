---
name: Win Track Gap Fixes
overview: "Address four Win Track gaps: (1) add Continuous Monitoring as a work entity across all four tracks, (2) model Partner/Channel work, (3) strengthen Revenue Realization, (4) add PLG acknowledgment — plus clarify advocacy/education coverage."
todos:
  - id: gap-1
    content: Create cross-track monitoring entities (4 new entity files, one per track) and update draft-work-model.md with monitoring sections
    status: completed
  - id: gap-2
    content: Add Partner Enablement + Partner Engagement subtypes to Win Track entities and draft-work-model.md
    status: completed
  - id: gap-3
    content: Add Revenue Operations Engagement subtype to Win Activity and draft-work-model.md
    status: completed
  - id: gap-4
    content: Add PLG/self-service conceptual notes to Win Activity and draft-work-model.md
    status: completed
  - id: gap-5
    content: Clarify advocacy/education coverage in CS Enablement and Segment Engagement with explicit examples
    status: completed
  - id: gap-6
    content: Create DR-019, add narrative seeds, add FAQs Q38-Q40, update README and entity catalog
    status: completed
isProject: false
---

# Win Track Gap Remediation Plan

## 1. Continuous Monitoring — New Cross-Track Work Entity

**The insight:** Every track has continuous monitoring work that sits between periodic assessment (Reviews/Deliberations) and reactive work (Cases/Incidents). This monitoring *triggers* reactive work and *feeds* periodic assessments, but the work itself is currently invisible.

**Design:** Define a common monitoring pattern, then instantiate per track with track-specific scope.

**Per-track monitoring entities:**

- **Track 1: Signal Monitoring** — Continuous tracking of signal pipeline health, trend analysis across Signals, discovery velocity metrics. Surfaces when signal backlog grows, when themes shift, when discovery capacity is mismatched. Triggers: Prioritization Task re-evaluation, new Signal creation.
- **Track 2: Build Monitoring** — Continuous tracking of build health (CI/CD pipeline), quality metrics (test coverage, defect rates, tech debt), velocity trends. Surfaces when quality degrades, when builds destabilize, when technical debt accumulates. Triggers: Bug creation, Maintenance Task, Release Planning adjustment.
- **Track 3: System Monitoring** — Continuous tracking of infrastructure health, SLA/uptime metrics, capacity utilization, performance baselines. Surfaces when thresholds are breached, when capacity is strained, when SLAs are at risk. Triggers: Incident creation, Change Request, Capacity Planning adjustment. (Run Track's most established monitoring practice — now explicitly modeled.)
- **Track 4: Win Monitoring** — Continuous tracking of customer health (adoption, usage, NPS), revenue metrics (pipeline, NRR, churn signals), competitive intelligence, Customer Promise fulfillment metrics. Surfaces at-risk accounts, expansion opportunities, competitive threats, promise gaps. Triggers: Win Activity creation, Win Case escalation, Win Review preparation.

**Common monitoring entity structure:**

```
## Fields
- Scope (what is being monitored)
- Metrics/Indicators tracked (references to KPIs, Value Metrics, or other measurement entities)
- Thresholds/Alerts (when does monitoring trigger action)
- Cadence (continuous, daily, weekly scans)
- Owner (who is responsible for watching)

## Outputs
- Alert/Signal (when threshold is breached → triggers downstream work)
- Dashboard/Report (periodic snapshot → feeds Review/Deliberation preparation)
```

**Files to create/update:**

- Create `entities/work-model/track1-signal-monitoring.md`
- Create `entities/work-model/track2-build-monitoring.md`
- Create `entities/work-model/track3-system-monitoring.md`
- Create `entities/work-model/track4-win-monitoring.md`
- Update [draft-work-model.md](org-8.0/product-information-model/draft-work-model.md) — add monitoring section to each track
- Update [entities/README.md](org-8.0/product-information-model/entities/README.md) — add monitoring entities to catalog
- Update [draft-work-execution-framework.md](org-8.0/product-information-model/draft-work-execution-framework.md) — add monitoring row to each track's artifact inventory

---

## 2. Partner/Channel Work — Win Track Extension

**Design:** Partners are intermediaries in the AAARRR journey (primarily Awareness + Acquisition). They need distinct enablement and engagement, separate from internal sales enablement and customer-facing engagement.

**New subtypes (not new parent entities):**

- **Partner Enablement** → new subtype under **Win Enablement** — Partner demo environments, co-marketing kits, partner training, certification programs, partner playbooks. Distinct from Sales Enablement (which equips *internal* teams).
- **Partner Engagement** → new subtype under **Win Activity** — Partner onboarding, co-selling, partner account management, partner pipeline management. Account-level granularity (one partner). References external PRM (Partner Relationship Management) records.
- **Partner Planning** → extend **Engagement Planning** scope (already cross-lever) to explicitly include partner prioritization and sequencing.

**Files to update:**

- Update [track4-win-enablement.md](org-8.0/product-information-model/entities/work-model/track4-win-enablement.md) — add Partner Enablement as 4th subtype
- Update [track4-win-activity.md](org-8.0/product-information-model/entities/work-model/track4-win-activity.md) — add Partner Engagement as 6th subtype
- Update [track4-win-planning.md](org-8.0/product-information-model/entities/work-model/track4-win-planning.md) — extend Engagement Planning scope to include partners
- Update [draft-work-model.md](org-8.0/product-information-model/draft-work-model.md) — add partner subtypes to Win Enablement and Win Activity descriptions

---

## 3. Revenue Realization — Strengthening the Revenue AAARRR Stage

**The insight:** Revenue Realization is an essential signal for Dim 2. The Win Track has Expansion Engagement for upsell/cross-sell, but the operational work of *actually collecting revenue* (billing, invoicing, collections) and the monitoring work of *tracking revenue metrics* are absent.

**Design — two additions:**

### 3a. Revenue Operations (new Win Track entity or Win Activity subtype)

Operational, customer-facing work to ensure revenue is realized:

- **Invoicing/Billing** — generating invoices, communicating billing changes, managing billing cycles
- **Collections** — following up on unpaid invoices, managing payment terms, account-level financial health
- **Renewal Processing** — administrative renewal work (distinct from Retention Engagement, which is relationship-driven)
- **Revenue Recognition coordination** — coordinating with Finance on recognition timing, contract terms

This is the Win Track analog of Run Track's Maintenance Task — routine operational work that must happen for the business to function. Customer-facing (not back-office accounting, which is Operating Model territory).

**Recommendation:** Model as a new **Win Activity subtype** called "Revenue Operations Engagement" under the Revenue AAARRR stage, since this work is account-level, customer-facing, and advances Revenue Win Outcomes.

Billing disputes are already covered by Win Case (Complaint type).

### 3b. Revenue Monitoring (covered by Win Monitoring)

Win Monitoring (from item 1) covers continuous tracking of revenue metrics — NRR, pipeline health, churn signals, expansion signals, billing health. When revenue targets are missed, Win Monitoring surfaces the signal, which may trigger:

- Win Review (Adoption Review type) for assessment
- Feedback → Signal for Discovery investigation
- Win Activity (Retention or Expansion) for intervention

**Files to update:**

- Update [track4-win-activity.md](org-8.0/product-information-model/entities/work-model/track4-win-activity.md) — add Revenue Operations as subtype
- Update [draft-work-model.md](org-8.0/product-information-model/draft-work-model.md) — add Revenue Operations to Win Activity description
- Revenue monitoring covered by `track4-win-monitoring.md` (from item 1)

---

## 4. PLG / Self-Service Segment Acknowledgment

**Design:** Add a conceptual note (not a new entity) that acknowledges how Win Track work entities operate differently when the Product lever dominates.

**Key points to capture:**

- For PLG/self-service segments, Win Activity subtypes shift from human execution to monitoring + exception-based intervention
- "Implementation/Onboarding" becomes in-product self-service; Win Track monitors completion funnels and intervenes on stuck accounts
- "Pre-sales Engagement" becomes free trial/sandbox experience; Win Track monitors conversion and intervenes on high-value prospects
- The Build Track effectively does "Win" work for these segments (building self-service onboarding, in-product upsell prompts)
- Win Monitoring becomes the primary Win Track activity for PLG segments (continuous funnel monitoring), with human engagement reserved for exceptions

**Files to update:**

- Update [track4-win-activity.md](org-8.0/product-information-model/entities/work-model/track4-win-activity.md) — add PLG/self-service note
- Update [draft-work-model.md](org-8.0/product-information-model/draft-work-model.md) — add note to Win Track preamble

---

## 5. Advocacy / Customer Education Clarification

**Conclusion:** Customer education is already covered implicitly. Make it explicit with examples and scope clarification — no new entities needed.

- **CS Enablement** already builds education assets (training materials, certification programs, knowledge bases, learning paths)
- **Segment Engagement** already delivers education (webinars, capability workshops, training sessions)
- **CS Planning** already plans education programs (as part of advocacy programs)

**Files to update:**

- Update [track4-win-enablement.md](org-8.0/product-information-model/entities/work-model/track4-win-enablement.md) — explicitly mention customer education/training in CS Enablement scope and examples
- Update [track4-win-activity.md](org-8.0/product-information-model/entities/work-model/track4-win-activity.md) — explicitly mention customer training in Segment Engagement scope and examples
- Update [draft-work-model.md](org-8.0/product-information-model/draft-work-model.md) — clarify advocacy scope includes customer education

---

## 6. Supporting Documents

- **Decision Record:** Create `decisions/DR-019-cross-track-monitoring-and-win-track-gaps.md`
- **Narrative Seeds:** Add session seeds to [narrative-seeds.md](org-8.0/product-information-model/narrative-seeds.md) covering:
  - Cross-track monitoring as invisible but essential work
  - Partner/channel as a distinct engagement model
  - Revenue realization as Win Track operational work
  - PLG segments shift Win Track from execution to monitoring
  - Advocacy encompasses customer education
- **FAQs:** Add Q38-Q40 to [draft-modeling-faqs.md](org-8.0/product-information-model/draft-modeling-faqs.md)
- **README updates:** Update [README.md](org-8.0/product-information-model/README.md) Win Track description with monitoring and partner/channel work

