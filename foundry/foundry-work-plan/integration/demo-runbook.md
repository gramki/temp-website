# Golden Path Demo Runbook — Phase 1

Operational guide for running the Phase 1 golden-path demo. Technical steps are in [../phase-1/golden-path.md](../phase-1/golden-path.md).

**Audience:** Integration lead, demo operator  
**Duration:** ~15 minutes (with fast-forward options)  
**Milestone:** M5

---

## Prerequisites

| Item | Owner | Verify |
|------|-------|--------|
| Foundry instance running | Control Plane | Health check passes |
| K8s cluster endpoint configured | Foundry admin | Session Infrastructure can spawn pod |
| Demo Workbench provisioned | Control Plane | M0 complete |
| Demo users: PM, builders per station | Program lead | Login works (Web App + IDE) |
| Platform default catalog published | Work Catalog steward | Build + Discovery workflows resolve |
| Seed data cleared or fresh Workbench | Integration lead | No stale OIs from prior runs |

**Example narrative:** *"Should we offer offline mode for mobile checkout?"*

---

## Roles during demo

| Role | Person | Actions |
|------|--------|---------|
| Demo operator | Integration lead | Drives script, narrates |
| PM | Product owner persona | Creates DC, approves PI, decision gate |
| Builders | Station owners or operators | Complete human tasks in IDE (or pre-staged) |
| Governance reviewer | PM or designated reviewer | Approve governance gates |

---

## Demo script

### 1. Discovery Case (3 min)

- [ ] PM opens Web App → creates Discovery Case with demo question
- [ ] Show OI entered `discovery-initiated`; framing WO created
- [ ] Builder (Product Specification) opens IDE → completes framing WO
- [ ] Show transition to `research-in-progress` and **four parallel WOs** (UX, Dev, QA, Release)

**Fast-forward:** Pre-complete research WOs if live agent tasks are slow; show completion events in Orchestrator log or Web App.

### 2. Synthesis and PDR (2 min)

- [ ] Show synthesis group WOs complete → `recommendations-ready`
- [ ] Product Specification records PDR
- [ ] Governance: `pdr-alignment-review` — approve
- [ ] PM opens decision gate → selects **proceed-to-build**

### 3. Handoff to Build (1 min)

- [ ] Show new Product Intent in Build track
- [ ] Show traceability link Discovery Case → Product Intent
- [ ] Discovery Case moves to `decision-made` → `end`

### 4. Build — approve and specify (2 min)

- [ ] PI at `draft-ready` — PM approves draft
- [ ] Trigger specification (milestone or manual per environment)
- [ ] Builder completes specification WO; governance spec review passes
- [ ] Show transition to `in-ux-design`

### 5. Build — UX through QA (4 min)

- [ ] UX design WO completes; governance UX review passes
- [ ] Show parallel dev + QA prep WOs at `specified`
- [ ] Development WO completes — show PR link; CI status (Release Engineering)
- [ ] QA test WO completes; governance coverage review passes
- [ ] OI at `ready-for-release`

**Fast-forward:** Pre-merge PR or use completed WO from rehearsal environment.

### 6. Release and traceability (3 min)

- [ ] Release acceptance WO → release package WO
- [ ] Governance: `customer-release-package-review` — **hard block** — approve
- [ ] OI transitions to `released`
- [ ] Web App: show full traceability chain (DC → PDR → PI → PSD → PR → test → package → verdicts)

---

## Failure handling

| Failure | Operator action |
|---------|-----------------|
| Session fails to start | Check WSI pod logs; fall back to pre-recorded session screenshot |
| WO stuck on agent task | Complete via human override or skip with pre-completed WO |
| Governance hard block | Use pre-approved reviewer account |
| CI not finished | Show CI running or last green run from rehearsal |
| Cross-track handoff missing | Stop demo; M3 not complete — do not improvise |

**Rule:** If a step fails twice, abort to recorded walkthrough rather than live debug in front of stakeholders.

---

## Post-demo checklist

- [ ] Log issues in tracker with milestone and gate ID ([contract-gates.md](contract-gates.md))
- [ ] Update [open-questions.md](../phase-1/open-questions.md) if new gaps found
- [ ] Capture traceability screenshot / export for value checkpoint sign-off

---

## Rehearsal schedule

| Rehearsal | Target | Participants |
|-----------|--------|--------------|
| Dry run 1 | T-2 weeks from M5 | Integration lead + squad leads |
| Dry run 2 | T-3 days from M5 | Full demo roles |
| Stakeholder demo | M5 date | Program lead invites |

---

## Read next

- [../phase-1/golden-path.md](../phase-1/golden-path.md) — technical step detail
- [../milestones.md](../milestones.md) — M5 definition of done
- [../value-checkpoints.md](../value-checkpoints.md) — sign-off criteria
