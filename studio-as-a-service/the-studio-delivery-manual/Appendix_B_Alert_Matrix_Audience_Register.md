# Appendix B — Alert Matrix & Audience Register

This appendix defines how alerts are routed, who owns them, how they escalate, and the expected tone and evidence for each audience. Use this with Appendix A (dashboards) and Appendix T (tunable thresholds).

---

## B.1 Alert Matrix (by domain)

Guiding notes
- Keep alerts actionable: include signal, threshold, current value, owner, forum/date, and options if escalation is needed.
- Prefer few, strong alerts over many noisy ones. Tune quarterly (see Appendix T). 
- Tone guidance: neutrally state the variance, attach evidence, propose options; avoid alarmist language.

### Requirements & Planning
- %RfP below target
  - Signal: %RfP (next increment) < 70%
  - Owner: Delivery Product Owner / Delivery Product Managers
  - Forum: Weekly Health & Risk Review (Section 9.4)
  - Escalation: CCB → Steering if planning at risk
- RfP shelf‑life breach
  - Signal: Median shelf‑life > 2 sprints
  - Owner: DPO/DPMs
  - Forum: Weekly Review
  - Escalation: CCB
- Volatility spike
  - Signal: Volatility > 20% over 2 weeks
  - Owner: DPO
  - Forum: Weekly Review
  - Escalation: Steering if release plan impacted

### Quality & Readiness
- Error budget low
  - Signal: Error budget < 20%
  - Owner: QA/Test Lead
  - Forum: Weekly Review → Sprint‑end Stabilization (Section 9.5)
  - Escalation: Steering to pause new intake if persistent
- Critical‑path pass rate
  - Signal: < 95%
  - Owner: QA/Test Lead
  - Forum: Quality Council → Weekly Review
  - Escalation: Block release; Steering if date at risk
- Flake rate high
  - Signal: > 5% (7‑day)
  - Owner: QA/Test Lead
  - Forum: Weekly Review
  - Escalation: Delivery Manager → mini‑hardening window

### Commercial
- Funding Visibility Score (SFM)
  - Signal: FVS < 60
  - Owner: Commercial Manager
  - Forum: Operational Review → Steering
  - Escalation: Steering to fund/de‑scope/re‑sequence
- Capacity Health (TCM)
  - Signal: < 60
  - Owner: Delivery Manager
  - Forum: Operational Review → Steering
  - Escalation: Steering for mix/ramp or demand action
- Unfunded exposure
  - Signal: > 10% of forecast
  - Owner: Commercial Manager
  - Forum: CCB → Steering
  - Escalation: Freeze net‑new scope until funded

### Operational & Dependencies
- Dependency variance sustained
  - Signal: > threshold for 2 cycles
  - Owner: Integration Lead / Ops owner on register
  - Forum: Weekly Review (add Dependency Huddle if spiking)
  - Escalation: Steering for workaround/funding
- Integration readiness incomplete
  - Signal: Contracts/creds/env not ready within 2 sprints of planned start
  - Owner: DPO / Integration Lead
  - Forum: Weekly Review → RfP Workshop
  - Escalation: CCB/Steering to re‑sequence
- Idle time (TCM)
  - Signal: > 10% rolling 4 weeks
  - Owner: Delivery Manager
  - Forum: Operational Review
  - Escalation: Steering for demand/standby protections

### Governance & Leadership
- Executive turnover (leadership change event)
  - Signal: Senior exec change (CIO/CTO/CRO/CEO) announced affecting program scope/governance
  - Owner: Delivery Manager (continuity pack), DPO (RfP/feature revalidation), Commercial Manager (funding exposure)
  - Forum: Monthly Operational Review → Executive Steering (decision re‑affirmation)
  - Escalation: Steering to re‑affirm/replace prior decisions; freeze material scope changes until written re‑confirmation

---

## B.2 Audience Register (who, tone, evidence)

- Steering Committee (EO‑owned)
  - Purpose: choose among options with scope/date/capacity/cost impacts
  - Tone: options with quantified impacts; decision request, not status
  - Evidence: dashboard snapshots, decision paper, risk register links

- CCB / Commercial Review (Studio‑owned)
  - Purpose: approve changes within guardrails; route material ones to Steering
  - Tone: concise deltas; link to CRs and funding
  - Evidence: CR form, forecast vs actual, unfunded exposure

- Operational Review (Studio‑owned)
  - Purpose: synthesize trends; recommend Steering decisions; policy updates
  - Tone: trend‑first; list top 3 risks with owners/actions
  - Evidence: weekly packs, incident post‑mortems, dependency register

- Weekly Health & Risk Review (Studio‑owned)
  - Purpose: decide sequencing and risk treatments; queue CCB/Steering items
  - Tone: breach‑first; owner/action/date
  - Evidence: %RfP/volatility, error budget/flake, FVS/Capacity, dependency variance

- Quality Council (Studio‑owned)
  - Purpose: govern gates and stabilization; focus on critical paths
  - Tone: SLO/error‑budget framing
  - Evidence: pass rate by journey, leakage trend, MTTR, flake list

- Architecture Roundtable (Studio‑owned)
  - Purpose: approve integration patterns and exceptions
  - Tone: contract‑first; impact and blast radius
  - Evidence: interface contracts, impact addendum, Risk Surfaces

- Customer PMO / Product forums
  - Purpose: align on planning readiness and acceptance scope
  - Tone: clarity over speed; commitment criteria
  - Evidence: RfP, AC, design addenda

---

## B.3 Escalation ladders (by domain)

- Operational delivery
  - Team Lead → DPM → Delivery Manager → Studio Owner → Engagement Owner/Steering
- Quality & risk
  - QA Engineer → QA Lead → Delivery Manager + DPO → Studio Owner → Engagement Owner/Steering
- Commercial & contractual
  - Delivery Manager → Commercial Manager → Account Manager → Engagement Owner/Steering
- Architecture & integrations
  - Developer/Integrator → Tech Architect/DPO → Delivery Manager → Studio Owner → Engagement Owner/Steering
- Behavioral/governance
  - Role‑to‑role (principles) → Delivery Manager → Studio Owner → Engagement Owner/Steering

---

## B.4 Thresholds & tuning (see Appendix T)

- Provide per‑program tuning for %RfP, shelf‑life, volatility, pass rate, error budget, flake, FVS/Capacity Health, unfunded exposure, dependency variance, idle time.
- Document chosen thresholds with date and owner; store in the Manual Change Register (SCM).

---

## B.5 Implementation notes

- Wire dashboards per Appendix A; alerts route to forums with owners
- Index items with labels (e.g., `process-exception`, `decomposition`, `integration-risk`, `dependency/*`)
- The Studio Council Member audits adoption and proposes quarterly tune‑ups in Operational Review
