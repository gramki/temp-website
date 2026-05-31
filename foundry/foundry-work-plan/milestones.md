# Phase 1 Milestones

Vertical delivery slices for Phase 1. Each milestone is demoable and forces cross-stream integration. Dates are TBD — sequence is fixed.

**Build question:** See [phase-1/phase-1-scope.md](phase-1/phase-1-scope.md).

**Golden path reference:** [phase-1/golden-path.md](phase-1/golden-path.md).

---

## Overview

| Milestone | Demo | Primary streams |
|-----------|------|-----------------|
| [M0](#m0--workbench-exists) | Workbench provisioned; catalog resolves; Validation passes | Control Plane, Work Catalog steward |
| [M1](#m1--one-wo-runs) | One WO runs in session; tasks complete; Git branch | Execution Plane, Control Plane |
| [M2](#m2--build-oi-flows) | Product Intent Build workflow end-to-end | Control Plane, Work Catalog (Build), Execution, Experience |
| [M3](#m3--discovery--handoff) | Discovery Case + proceed-to-build handoff | Control Plane, Work Catalog (Discovery), all |
| [M4](#m4--governance--traceability) | All 7 governance gates; traceability query | Control Plane, Experience, Work Catalog (Governance) |
| [M5](#m5--golden-path-demo) | Full 15-min demo unattended | Integration lead, all |

**Rule:** No stream closes a milestone alone. Definition of done = integrated environment, not unit tests in isolation.

---

## M0 — Workbench exists

**Target date:** TBD

### Demo

- Foundry admin provisions a Workshop and Workbench
- Platform default Work Catalog resolves (Build + Discovery workflows visible)
- Validation module passes on Foundry-scope config repos

### Definition of done

- [ ] Workbench provisioning API completes (GitHub org / repo metadata stub acceptable for demo Workbench)
- [ ] Metadata Service assigns IDs for OI types
- [ ] WCM resolves `discovery-case` and `product-intent` workflows from platform defaults
- [ ] Validation gate runs on work-catalog config publish
- [ ] Catalog steward confirms indicative scenario YAML is documented as non-authoritative

### Streams

| Role | Stream |
|------|--------|
| Primary | Control Plane |
| Supporting | Work Catalog Authoring (steward only) |

### Work Catalog deliverables

- Steward: schema contract with WCM documented in [integration/contract-gates.md](integration/contract-gates.md)
- Track owners: acknowledge indicative defaults; no authoritative scenarios required yet

### Dependencies

- None (start here)

### Golden path

Preconditions for [Part A § A1](phase-1/golden-path.md#a1-create-discovery-case)

---

## M1 — One WO runs

**Target date:** TBD

### Demo

- Orchestrator (or manual trigger) creates a single Work Order
- Session Management provisions a session; WO Runtime executes task graph
- Human task completable in IDE; agent task runs (stub skill OK)
- `work-order-completed` event received by Orchestrator
- Development-style WO creates Git branch `wo/WO-{id}` under session volume

### Definition of done

- [ ] Session create/attach API works (WSSM + WSI)
- [ ] WO Runtime management-plane ack and heartbeat
- [ ] Task graph API surfaced in IDE (work orders panel minimum)
- [ ] WO completion event emitted with outputs
- [ ] Git per-WO branch per [git-infrastructure](../foundry-platform/management/platform-developer-guide/git-infrastructure.md) spec
- [ ] One authoritative scenario: e.g. `frame-discovery-case` (Catalog Discovery owner)

### Streams

| Role | Stream |
|------|--------|
| Primary | Execution Plane |
| Supporting | Control Plane, Builder Experience (IDE minimum), Work Catalog (Discovery owner) |

### Work Catalog deliverables

- **Discovery owner:** `frame-discovery-case` scenario authoritative (inputs, outputs, tasks)
- **Steward:** published and validated via WCM

### Dependencies

- M0 complete
- Contract gates G1–G4 in [integration/contract-gates.md](integration/contract-gates.md)

### Golden path

Supports [Part A § A2](phase-1/golden-path.md#a2-frame-the-case) and [Part C](phase-1/golden-path.md#part-c--builder-session-flow-any-wo)

---

## M2 — Build OI flows

**Target date:** TBD

### Demo

- Product Intent created (manual or seeded)
- Full Build workflow runs: draft-ready → … → released (or ready-for-release if release packaging deferred)
- Orchestrator creates WOs at each stage including parallel dev+QA prep group
- PM approves draft via user task

### Definition of done

- [ ] Product Intent entity API + lifecycle
- [ ] Orchestrator runs [product-intent/workflow.yaml](../foundry-platform/work-catalogues/platform-defaults/work-catalog/build/product-intent/workflow.yaml)
- [ ] All Build golden-path scenarios authoritative (Build track owner)
- [ ] Web App: create/list Product Intent, show OI stage
- [ ] IDE: builders execute WOs for spec, UX, dev, QA stations
- [ ] Release Engineering: CI runs on implementation PR (build/test)

### Streams

| Role | Stream |
|------|--------|
| Primary | Control Plane |
| Supporting | Execution Plane, Builder Experience, Work Catalog (Build), Release Engineering |

### Work Catalog deliverables

- **Build owner:** authoritative `product-intent/workflow.yaml` + all Build station scenarios on golden path
- **Governance owner:** Build transition governance scenarios (spec, UX, test plan, coverage, release package review)

### Dependencies

- M1 complete
- Contract gates G5–G7

### Golden path

[Part B — Build](phase-1/golden-path.md#part-b--build-product-intent) (Discovery handoff optional — seed PI directly)

---

## M3 — Discovery + handoff

**Target date:** TBD

### Demo

- PM creates Discovery Case in Web App
- Discovery workflow runs through research, synthesis, PDR, decision gate
- PM selects `proceed-to-build`
- New Product Intent appears with link to Discovery Case
- Discovery Case closes via governance closure review

### Definition of done

- [ ] Discovery Case entity API + lifecycle
- [ ] Orchestrator runs [discovery-case/workflow.yaml](../foundry-platform/work-catalogues/platform-defaults/work-catalog/discovery/discovery-case/workflow.yaml)
- [ ] Parallel WO groups (research, synthesis) work
- [ ] `create-orchestration-item` cross-track handoff implemented
- [ ] All Discovery golden-path scenarios authoritative (Discovery owner)
- [ ] Web App: create Discovery Case, decision gate UI

### Streams

| Role | Stream |
|------|--------|
| Primary | Control Plane |
| Supporting | All streams |

### Work Catalog deliverables

- **Discovery owner:** full Discovery Case workflow + all Discovery station scenarios on golden path
- **Steward:** cross-track handoff scenario contract documented

### Dependencies

- M2 complete (Build path must accept handoff PI)
- Contract gate G8 (cross-track handoff)

### Golden path

[Part A — Discovery](phase-1/golden-path.md#part-a--discovery) through [Part B § B1](phase-1/golden-path.md#b1-approve-pi-draft)

---

## M4 — Governance + traceability

**Target date:** TBD

### Demo

- All seven transition governance scenarios invoke and record verdicts
- Hard block on `customer-release-package-review` enforced
- Web App shows parent/child traceability: Discovery Case → PI → artifacts → governance verdicts

### Definition of done

- [ ] Governance invoke + verdict persistence
- [ ] Soft block vs hard block behavior per [governance-mvp.md](phase-1/governance-mvp.md)
- [ ] Traceability query API (minimum parent/child links)
- [ ] Governance owner: all seven scenarios authoritative with real check criteria
- [ ] Release Engineering: release package artifact produced

### Streams

| Role | Stream |
|------|--------|
| Primary | Control Plane, Builder Experience |
| Supporting | Work Catalog (Governance), Release Engineering |

### Work Catalog deliverables

- **Governance owner:** verdict inputs/outputs finalized for all seven scenarios

### Dependencies

- M3 complete
- Contract gate G9 (traceability query)

### Golden path

Governance columns in [Part A](phase-1/golden-path.md) and [Part B](phase-1/golden-path.md); [traceability section](phase-1/golden-path.md#traceability-phase-1-minimum)

---

## M5 — Golden path demo

**Target date:** TBD

### Demo

- Integration lead runs [integration/demo-runbook.md](integration/demo-runbook.md) end-to-end in under 15 minutes
- No manual database seeding mid-demo (except optional fast-forward for long WOs)
- All streams sign off

### Definition of done

- [ ] Demo runbook executed successfully twice (dry run + stakeholder demo)
- [ ] [phase-1-scope.md](phase-1/phase-1-scope.md) success criteria met
- [ ] [value-checkpoints.md](value-checkpoints.md) M5 checkpoint signed off
- [ ] Known gaps documented in [phase-1/open-questions.md](phase-1/open-questions.md) only if non-blocking

### Streams

| Role | Stream |
|------|--------|
| Primary | Integration lead (all streams on call) |
| Supporting | All |

### Work Catalog deliverables

- Steward + track owners: catalog signed off for Phase 1 platform defaults

### Dependencies

- M4 complete

### Golden path

Full [demo script](phase-1/golden-path.md#demo-script-15-minute-walkthrough)

---

## Read next

- [people-plan.md](people-plan.md) — stream ownership
- [integration/dependency-graph.md](integration/dependency-graph.md) — critical path
- [value-checkpoints.md](value-checkpoints.md) — value at each milestone
