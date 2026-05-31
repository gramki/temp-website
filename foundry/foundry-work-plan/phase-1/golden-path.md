# Phase 1 Golden Path

End-to-end happy path from a discovery question to customer release. This is the demo Phase 1 must support.

**Example narrative:** A Product Manager asks *"Should we offer offline mode for mobile checkout?"* Foundry runs discovery, records a Go decision, builds the feature, and publishes a release package — with traceability at every step.

## Overview

```text
Discovery Case                    Build: Product Intent
─────────────────                 ─────────────────────
Frame case                        Draft → PO approval
Parallel research (4 stations)    Specification
Synthesize + validate evidence    UX design
Record PDR + decision gate        Development + QA prep (parallel)
  └─ proceed-to-build ──────────▶ QA test
                                  Release accept + package
                                  Governance at each transition
```

Platform default workflows: [Discovery Case](../../foundry-platform/work-catalogues/platform-defaults/work-catalog/discovery/discovery-case/workflow.yaml), [Product Intent](../../foundry-platform/work-catalogues/platform-defaults/work-catalog/build/product-intent/workflow.yaml).

---

## Actors

| Actor | Role in golden path |
|-------|---------------------|
| **Product Owner (PM)** | Creates Discovery Case, approves PI draft, decides proceed-to-build / park / drop |
| **Builder (Product Specification)** | Frames case, synthesizes evidence, records PDR, creates specification |
| **Builder (UX Design)** | Conducts user research |
| **Builder (Development)** | Assesses feasibility, implements feature |
| **Builder (QA)** | Assesses testability, validates evidence, executes tests |
| **Builder (Release)** | Assesses rollout feasibility, accepts and packages release |
| **Governance reviewer** | Approves/rejects at transition gates (may be same person as PM in demo) |
| **Agents** | Execute agent tasks within Work Orders per scenario skills |
| **Orchestrator** | System — drives OI stages, creates WOs, invokes governance |
| **WO Runtime** | System — executes tasks in Workspace Sessions |

---

## Part A — Discovery

### A1. Create Discovery Case

| | |
|---|---|
| **Actor** | Product Owner |
| **Surface** | Foundry Web App — Track Console or Orchestration Console |
| **Module** | Management (track route: create Work Item) → Orchestrator (OI created event) |
| **Entity** | `DiscoveryCase` with `title`, `description`; optional `sourceRefs[]`; OI enters `start` → `discovery-initiated` |
| **Repository** | Work Repository (Work Item) + Intent Repository (charter artifact, optional) |

### A2. Frame the case

| | |
|---|---|
| **Trigger** | OI enters `discovery-initiated` |
| **Orchestrator** | Creates WO: `product-specification` / `frame-discovery-case` |
| **Builder action** | Opens WO in IDE; completes framing tasks (question, hypotheses, success criteria) |
| **WO completes** | OI transitions to `research-in-progress` |
| **Repository** | Intent Repository — discovery charter artifact |

### A3. Parallel research

| | |
|---|---|
| **Trigger** | OI enters `research-in-progress` |
| **Orchestrator** | Creates WO group `discovery-research`: |
| | — UX Design / `conduct-user-research` |
| | — Development / `assess-technical-feasibility` |
| | — QA / `assess-testability` |
| | — Release / `assess-rollout-feasibility` (low priority) |
| **Builder action** | Each station's builder opens their WO in a Workspace Session; agents assist |
| **WO group completes** | OI transitions to `insights-synthesized` |

### A4. Synthesize evidence

| | |
|---|---|
| **Trigger** | OI enters `insights-synthesized` |
| **Orchestrator** | Creates WO group `synthesis`: |
| | — Product Specification / `synthesize-evidence` |
| | — QA / `validate-experiment-evidence` |
| **WO group completes** | OI transitions to `recommendations-ready` |

### A5. Record PDR and decide

| | |
|---|---|
| **Trigger** | OI enters `recommendations-ready` |
| **Orchestrator** | Creates WO: Product Specification / `record-product-decision` |
| **WO completes** | Invokes governance: `pdr-alignment-review` (soft block) |
| | Creates user task: decision gate (proceed-to-build / park / drop) |
| **PM action** | Reviews PDR; selects **proceed-to-build** |
| **Orchestrator** | Creates Product Intent (Build track), seeded from Discovery Case |
| | OI transitions to `decision-made` |
| **Repository** | PDR recorded; cross-track link Discovery Case → Product Intent |

### A6. Close Discovery Case

| | |
|---|---|
| **Trigger** | OI enters `decision-made` |
| **Orchestrator** | Invokes governance: `discovery-closure-review` (soft block) |
| **OI** | Transitions to `end` |

---

## Part B — Build (Product Intent)

The new Product Intent enters the Build workflow at `start` → `draft-ready`.

### B1. Approve PI draft

| | |
|---|---|
| **Trigger** | Product Intent created (from Discovery handoff or direct) |
| **Orchestrator** | OI: `start` → `draft-ready`; creates user task `draft-approval` |
| **PM action** | Approves PI draft |
| **OI** | Transitions to `ready-for-specification` |

### B2. Trigger specification

| | |
|---|---|
| **Trigger** | Release Intent milestone reached (or manual trigger in demo) |
| **Orchestrator** | Creates WO: Product Specification / `create-product-specification` |
| **OI** | Transitions to `in-specification` |
| **Builder action** | Refines PI into PSD with acceptance criteria and backlog decomposition |
| **WO completes** | Governance: `product-specification-review` → OI transitions to `in-ux-design` |

### B3. UX design

| | |
|---|---|
| **Orchestrator** | Creates WO: UX Design / `design-user-experience` |
| **Builder action** | Produces flows, wireframes, high-fidelity design |
| **WO completes** | Governance: `ux-design-review` → OI transitions to `specified` |

### B4. Development and QA prep (parallel)

| | |
|---|---|
| **Orchestrator** | Creates WO group `dev-and-qa-prep`: |
| | — Development / `implement-product-specification` |
| | — QA / `prepare-test-suite-for-product-specification` |
| **Builders** | Dev implements (PR opened); QA prepares test plan and suite |
| **Group completes** | Governance: `test-plan-review` → OI transitions to `in-qa` |

### B5. QA execution

| | |
|---|---|
| **Orchestrator** | Creates WO: QA / `test-developed-feature` |
| **Builder action** | Executes test suite; raises defects if needed |
| **WO completes (success)** | Governance: `test-coverage-review` → OI transitions to `ready-for-release` |
| **WO completes (failure)** | Creates fix WO in Development; retries QA (loop) |

### B6. Release

| | |
|---|---|
| **Orchestrator** | Creates WO: Release / `accept-completed-product-intent` |
| **Builder action** | Verifies acceptance criteria; accepts or rejects |
| **Acceptance succeeds** | Creates WO: Release / `prepare-customer-release` |
| **Release WO completes** | Governance: `customer-release-package-review` (**hard block**) |
| **OI** | Transitions to `released` → `end` |

---

## Part C — Builder session flow (any WO)

Applies to every Work Order above:

1. **Orchestrator** assigns WO; queries/creates Workspace Session via Session Management
2. **WO Runtime** starts in session; compiles context from OI graph and repositories
3. **Builder** opens IDE; sees WO in Work Orders panel, task graph, employed agents
4. **Agent tasks** run via Agent Fabric skills; **human tasks** surface in IDE
5. **Builder** completes human tasks; agent tasks complete
6. **WO Runtime** publishes `work-order-completed` to Atropos (`/{foundry-id}/foundry.wo-runtime.work-order-completed`)
7. **Orchestrator** receives callback; advances OI per workflow handlers

Git: Development WO clones repos under `work-orders/WO-{id}/repos/` on branch `wo/WO-{id}`; pushes and opens PR on terminal success.

---

## Traceability (Phase 1 minimum)

At end of golden path, the following links must be queryable:

```text
Discovery Case
  └─ PDR
  └─ research outputs (per station)
  └─ Product Intent (handoff)
       └─ PSD
       └─ UX design package
       └─ implementation PR
       └─ test run
       └─ release package
       └─ governance verdicts (per transition)
```

Full graph maps (Executive Strategy Map, etc.) are deferred — see [open-questions.md](open-questions.md).

---

## Demo script (15-minute walkthrough)

1. PM creates Discovery Case: *"Should we offer offline mode?"*
2. Show framing WO completing; research group fanning out to four stations
3. Show synthesis + PDR recorded; PM selects proceed-to-build
4. Show Product Intent appearing in Build track with link back to Discovery Case
5. PM approves draft; specification WO runs
6. Walk through UX → Dev+QA prep → QA test → Release (can fast-forward long-running WOs)
7. Show governance verdict at release (hard block)
8. Show release package + traceability chain in Web App

---

## Read next

- [event-contracts.md](event-contracts.md) — Atropos event transport
- [phase-1-scope.md](phase-1-scope.md) — what is and is not included
- [scenario-catalog.md](scenario-catalog.md) — scenario IDs and stations
- [module-boundaries.md](module-boundaries.md) — which module owns each step
- [governance-mvp.md](governance-mvp.md) — gate details
