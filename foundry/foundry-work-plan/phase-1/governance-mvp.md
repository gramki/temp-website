# Phase 1 Governance MVP

Governance behavior required for Phase 1. Full Governance Ritual catalog, registers, and Control Objective infrastructure are **deferred** — see [phase-1-scope.md](phase-1-scope.md).

## What Phase 1 governs

Phase 1 implements **transition governance** only: Orchestrator invokes Governance-station scenarios at OI workflow transitions. No cadence-based Governance Rituals (sprint review, SLA review, etc.).

## Governed transitions

| Transition | Governance scenario | Block mode | Track |
|------------|---------------------|------------|-------|
| PDR recorded | `pdr-alignment-review` | soft block | Discovery |
| Discovery Case closing | `discovery-closure-review` | soft block | Discovery |
| Specification complete | `product-specification-review` | soft block | Build |
| UX design complete | `ux-design-review` | soft block | Build |
| Dev + QA prep complete | `test-plan-review` | soft block | Build |
| QA test complete | `test-coverage-review` | soft block | Build |
| Release package ready | `customer-release-package-review` | **hard block** | Build |

**Soft block** — rejection creates findings and may stall the OI; builder/PM can address and retry.

**Hard block** — rejection prevents transition to `released`; release authority must explicitly approve.

## What each gate checks (minimum)

| Scenario | Minimum check |
|----------|---------------|
| `pdr-alignment-review` | PDR recommendation traceable to research evidence; aligned with strategy |
| `discovery-closure-review` | Decision recorded; handoff PI well-formed if proceed-to-build |
| `product-specification-review` | PSD complete; traceable to Product Intent |
| `ux-design-review` | Design covers specified scope; accessibility baseline |
| `test-plan-review` | Test plan covers specification and risk areas |
| `test-coverage-review` | Pass rate and open defects meet quality bar |
| `customer-release-package-review` | Package complete; versioning; release notes; policy compliance |

Detailed scenario definitions: [scenario-catalog.md](scenario-catalog.md).

## Actors

| Role | Phase 1 |
|------|---------|
| **Governance reviewer** | Human assigned to governance scenario WO or verdict task |
| **Release authority** | Human with hard-block approve on `customer-release-package-review` |
| **Governance Admin** | Deferred — no CO/COI admin UI in Phase 1 |

Phase 1 demo may collapse governance reviewer and PM into the same person.

## Verdict model

| Field | Description |
|-------|-------------|
| `decision` | `approved` or `rejected` |
| `findings` | List of issues to address if rejected |
| `reviewer` | Human who recorded verdict |
| `timestamp` | When verdict recorded |
| `oi_id` | Parent orchestration item |
| `transition` | Which transition was gated |

Verdicts are persisted as governance events and linked to the OI traceability chain.

## Evidence

Phase 1 requires evidence **references**, not a full Evidence Repository implementation:

- Research outputs linked to Discovery Case
- PSD, design package, PR, test run, release package linked to Product Intent
- Governance verdicts linked to each transition

Full Evidence Repository, Compliance Register, and Risk Register are deferred.

## Explicitly deferred

- Governance Ritual definitions (cadence, inputs, outputs)
- Control Objectives / Control Objective Indicators (BQO/BQI)
- Debt Register, Catch-Up Plans, Exception / Waiver lifecycle
- Release Readiness Review control families (Build Quality, SRE, Security, GTM, etc.) as formal rituals
- Governance Admin roles and Authority Matrix UI
- Kudos / recognition register
- Governance consoles beyond basic verdict visibility

## Read next

- [golden-path.md](golden-path.md) — where gates appear in the demo
- [../../ace/governance.md](../../ace/governance.md) — ACE governance model
- [open-questions.md](open-questions.md) — remaining governance decisions
