# Appendix D — RACI Matrix & Role Readiness

Use this appendix to clarify who is Responsible, Accountable, Consulted, and Informed for core delivery processes, and to verify role readiness before program start. Cross‑reference: `studio-as-a-service/roles_reference.md`.

Legend
- R = Responsible (does the work)
- A = Accountable (final decision/ownership)
- C = Consulted (two‑way input)
- I = Informed (kept aware)

---

## D.1 RACI Matrix (core processes)

| Process / Decision | DPO | DPM | Delivery Manager | Eng Manager / Tech Lead | QA Lead | Integration Lead | Commercial Mgr | Studio Owner | EO (Engagement Owner) | Customer PO/PM | SCM |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| MAR definition (Sec 5.2) | A | R | I | C | C | C | I | I | I | C | I |
| RfP gate sign‑off (Sec 5.3) | A | R | I | C | C | C | I | I | I | C | I |
| Design/Impact addendum (Sec 5, 10) | A | R | I | R | C | R | I | I | I | C | I |
| Feature decomposition → Epics/Stories (Sec 5) | C | R | I | C | C | C | I | I | I | C | I |
| Quality gates & error budget policy (Sec 7) | C | I | A | C | R | C | I | C | I | I | I |
| Daily/Weekly/Monthly ritual facilitation (Sec 9) | I | C | A | R | C | C | C | C | I | I | I |
| Dependency register & readiness (Sec 5.10) | C | C | A | C | C | R | C | C | I | C | I |
| Commercial CR lifecycle (Sec 8A) | I | I | C | I | I | I | R | C | A | C | I |
| Capacity/mix changes (TCM) (Sec 8B) | I | I | C | C | I | I | C | A | A | C | I |
| Exception policy approval (Sec 10.9) | C | C | A | C | C | C | C | C | A | C | I |
| Continuous improvement cadences (Sec 11) | I | I | C | I | I | I | I | C | I | I | A |
| Manual versioning & release notes (Sec 11) | I | I | I | I | I | I | I | C | C | I | A |

Notes
- Steering is chaired by EO; material scope/cost/date/capacity or policy exceptions escalate there (Sections 8, 9, 10).
- The SCM maintains lifecycle tracking and the Manual Change Register (Section 11).

---

## D.2 Role Readiness Checklists (pre‑flight)

Use these checklists to verify each role is ready on Day 1. Reference `roles_reference.md` for detailed responsibilities.

### Delivery Product Owner (DPO)
- [ ] Solution intent documented; MAR/RfP criteria agreed with Customer PO
- [ ] Design/impact addendum template in place; Risk Surfaces defined
- [ ] Backlog triage cadence set with DPMs; traceability mapping confirmed

### Delivery Product Manager (DPM)
- [ ] Decomposition workflow (labels/statuses) configured in Jira (Sec 5)
- [ ] DoR checklist, AC templates, and RfP sign‑off path ready
- [ ] Integration readiness checklist wired (contracts/creds/env)

### Delivery Manager
- [ ] Ritual calendar (daily/weekly/monthly/Steering) published with owners
- [ ] Dashboards live (Reqs/Quality/Commercial/Operational); alert routes tested
- [ ] Decision log template and escalation ladders confirmed

### Engineering Manager / Tech Lead
- [ ] Quality gate enforcement (error budget, pass rate) automated (Sec 7)
- [ ] Debt register board and paydown reserve (10–20%) agreed (Sec 6, App T)
- [ ] Runbooks and on‑call/operability basics validated with Ops

### QA/Test Strategy Lead
- [ ] Critical path cataloged; SLOs and error budget policy agreed (Sec 7)
- [ ] Allure TestOps integration working; flake quarantine and hardening flow set
- [ ] Readiness of certification environment verified

### Integration Lead
- [ ] Interface contracts identified; contract‑first stubs available
- [ ] Dependency register fields complete (owner, funding, lead‑time, readiness)
- [ ] Cutover rehearsal plan sketched for first significant integration

### Commercial Manager
- [ ] FVS (SFM) / Capacity Health (TCM) widgets configured; variance slices ready
- [ ] CR lifecycle and decision rights documented; unfunded exposure widget live
- [ ] Idle‑time/standby protections agreed (TCM) with Account Manager

### Studio Council Member (SCM)
- [ ] Program retro cadence (milestones or quarterly) scheduled
- [ ] Manual Change Register created; discovery→decision→implementation→adoption audit lifecycle fields present
- [ ] Versioning plan defined (tags, release notes, approval forums)

### Studio Owner / EO (as applicable)
- [ ] Forum ownership labeled (Steering EO, CCB/Operational Studio); chairs assigned
- [ ] Guardrails/policy thresholds published with review frequency
- [ ] Escalation response SLAs acknowledged by participants

---

## D.3 Implementation Notes
- Keep the RACI table in your program workspace; link it on ritual invites.
- Review role readiness during Flight Check (Section 9.2); update gaps with owners/dates.
- Audit RACI drift monthly; SCM records changes and proposes updates to this manual if patterns persist.
