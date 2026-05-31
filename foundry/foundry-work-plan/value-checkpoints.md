# Value Checkpoints — Phase 1

How Phase 1 progress is measured against intended value — not just milestone completion.

## Build question

From [phase-1/phase-1-scope.md](phase-1/phase-1-scope.md):

> Can Foundry take a product-relevant discovery question, form Product Intent, refine it into buildable work, execute Workspace Work Orders, govern transitions, and publish Product Delivery with traceability?

Phase 1 value is **proven** when this question is answered **yes** in a live demo ([integration/demo-runbook.md](integration/demo-runbook.md)), not when individual modules ship in isolation.

## Checkpoint map

| Milestone | Value added | Evidence |
|-----------|-------------|----------|
| **M0** | Foundry can host a Workbench with executable catalog definitions | Workbench provisioned; catalog resolves; Validation passes |
| **M1** | Foundry can run work in a builder session | One WO completes; Git branch exists; completion advances state |
| **M2** | Foundry can orchestrate Build-track product evolution | Product Intent flows Specification → UX → Dev → QA → Release path |
| **M3** | Foundry connects discovery decisions to build execution | Discovery Case → PDR → proceed-to-build → Product Intent handoff |
| **M4** | Foundry governs transitions and preserves traceability | Seven gates enforced; chain queryable Discovery → release |
| **M5** | Foundry delivers the Phase 1 promise end-to-end | Golden-path demo succeeds; build question answered |

## M5 success criteria (Phase 1 complete)

All of the following must be true:

1. PM creates Discovery Case with a product question
2. Research executes across multiple workspace stations (parallel WOs)
3. PDR recorded; PM decides `proceed-to-build`
4. Product Intent created from Discovery Case with traceability link
5. PI progresses through full Build workflow with governance at transitions
6. Development WO produces PR with CI evidence
7. Release WO produces customer release package
8. Hard governance block on release enforced and satisfiable
9. Full parent/child traceability visible in Web App
10. Demo runbook completed without manual mid-demo database surgery

Source: [phase-1/phase-1-scope.md](phase-1/phase-1-scope.md) success criteria.

## Real vs mocked value

Value must be **real** on the golden path for:

- OI workflow execution
- WO creation and session execution
- Governance invoke and verdict (soft and hard block)
- Git branch/PR on Development WO
- Cross-track Discovery → Build handoff

Acceptable **mocked or partial** for Phase 1:

- Jira bidirectional sync
- TestRail / Figma
- Full governance admin (CO/COI, registers)
- Agent LLM depth (stub skills OK if human tasks prove flow)
- Multi-tenant production hardening

## Deferred value (explicitly not Phase 1)

| Value | Deferred to |
|-------|-------------|
| Run-track deployment and operational response | Post–Phase 1 |
| Win-track outcomes and Customer Release Intent orchestration | Post–Phase 1 |
| Evolve-track practice evolution | Post–Phase 1 |
| Governance Ritual catalog (cadence rituals) | Post–Phase 1 |
| Signal → Objective → Initiative automation | Post–Phase 1 |
| Executive Strategy Map and full traceability maps | Post–Phase 1 |
| Say/Do, velocity, cost KPIs | Post–Phase 1 |

## UPIM alignment (future value)

When Win and Run tracks arrive, value checkpoints should reference UPIM entities:

- Win Outcomes, Win Reviews, Initiative Targets ([product-information-model](../../product-information-model/README.md))

Phase 1 establishes traceability foundations only.

## Sign-off

| Checkpoint | Sign-off owner | Date |
|------------|----------------|------|
| M0 | Program lead | TBD |
| M1 | Integration lead | TBD |
| M2 | Program lead | TBD |
| M3 | Program lead | TBD |
| M4 | Program lead + platform architect | TBD |
| M5 (Phase 1 complete) | Program lead + executive stakeholder | TBD |

## Read next

- [milestones.md](milestones.md) — technical DoD per milestone
- [integration/demo-runbook.md](integration/demo-runbook.md) — M5 demo
- [phase-1/golden-path.md](phase-1/golden-path.md) — value narrative
