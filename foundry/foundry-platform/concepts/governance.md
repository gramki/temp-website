# Governance

Governance is the discipline of transition validation, evidence capture, and policy enforcement — ensuring every governed transition invokes appropriate checks, records decisions, and maintains audit trails.

## What it is

In ACE, governance is **not a stage gate at the end of a pipeline**. It is **a property of motion** — a discipline that runs on every transition of orchestration items, not just the QA → Release edge.

> Every governed transition invokes Governance Enforcement, and may invoke Governance Rituals when human review, cadence, or decision authority is required.

The Governance Workspace does not own the work being governed. It owns the **discipline of the handoff**: validation that preconditions are met, evidence is captured, policy applies, rituals occur when needed, and transitions are recorded.

Governance operates through two primary orchestration items:

| Item | Purpose | Example |
|------|---------|---------|
| **Governance Ritual** | Cadence-based or event-triggered practice bringing participants, evidence, and decision authority together | Release readiness review, sprint retrospective governance checkpoint |
| **Governance Enforcement** | Policy assertion/control execution against items, transitions, artifacts, or states | "PSD must reference Product Intent", "Coverage threshold met" |

Governance work produces:

- Pass/fail/warn/exception verdicts
- Findings and violations
- Risk, debt, and compliance register entries
- Remediation Work Orders
- Audit records
- Recognition entries (kudos for good practice)

When Enforcement returns a blocked transition, it can proceed via two paths:

| Path | Description |
|------|-------------|
| **Debt + Catch-Up** | Temporary deviation allowed; debt registered with repayment date |
| **Exception / Waiver** | Non-applicability or alternate control approved by Approver; time/scope-bound |

Controls inherit through ACE's operating structure:

```
Foundry controls
  → Workspace controls
    → Workbench controls
```

Child scopes may add controls or tighten inherited controls. They may override only where the parent scope permits.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Orchestrator** | Invokes Governance Enforcement at transitions; enforces gates |
| **WO Runtime** | Executes Governance Scenarios (same mechanics as any Workspace) |
| **Work Catalog** | Stores Governance Scenarios in `governance/{track}/` paths |
| **Repositories** | Evidence, findings, register entries stored in appropriate repos |
| **Web App** | Governance console for rituals, findings, registers |

The Governance Workspace has Scenarios just like any other Workspace. Governance Rituals and Governance Enforcement are orchestration items that execute through these Scenarios.

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Governance Workspace](../../ace/concepts.md#governance-workspace) | Sixth workspace type with governance-specific Scenarios |
| [Governance Track](../../ace/governance.md) | ACE extends UPIM with Governance as a Track |
| Governance Ritual / Enforcement | Orchestration items for the Governance Track |
| Operating Model | UPIM source for policies, rituals, roles, evidence requirements |

From ACE: "If governance were a stage gate, it would sit between specific workspaces. But every edge in the Product Evolution Cycle needs validation... ACE chooses a different model: a Governance Track whose orchestration items execute through the Governance Workspace."

UPIM's Operating Model captures governance policies, ritual definitions, participant roles, and evidence requirements. Governance Track work executes those definitions.

## Related concepts

- [Track](track.md) — Governance as a first-class Track
- [Orchestration Item](orchestration-item.md) — Governance Ritual and Enforcement items
- [Scenario](scenario.md) — How Governance work executes
- [Containment Hierarchy](containment-hierarchy.md) — Control inheritance through levels
- [Repositories](repositories.md) — Where evidence and findings are stored

## Further reading

- [../../ace/governance.md](../../ace/governance.md) — Full ACE governance model
- [../../ace/governance-rituals.md](../../ace/governance-rituals.md) — Recommended rituals
- [../orchestrator/README.md](../orchestrator/README.md) — Gate enforcement
- [../work-catalogues/platform-defaults/work-catalog/governance/](../work-catalogues/platform-defaults/work-catalog/governance/) — Platform default governance scenarios
