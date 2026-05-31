# Governance Cadences — Phase 1 Program

How the **Foundry Platform build program** is steered. This is project-level governance — not the [Governance Workspace](../../ace/governance.md) or [Governance Track](../../ace/governance.md) inside a Workbench.

## Cadence overview

| Cadence | Frequency | Owner | Participants |
|---------|-----------|-------|--------------|
| Squad sync | Weekly | Each squad lead | Stream members |
| Integration standup | Weekly | Integration lead | Squad leads, platform architect |
| Milestone review | Per milestone (M0–M5) | Program lead | All squad leads, stakeholders |
| Architecture review | Bi-weekly | Platform architect | Control Plane, Execution Plane tech leads |
| Catalog review | Bi-weekly | Catalog steward | Track owners, Control Plane (WCM) |
| Program steering | Monthly | Program lead | Executive stakeholders, EMs |

## Squad sync

**Purpose:** Stream-internal progress, blockers, next-week commitments.

**Inputs:** Milestone checklist items for this stream ([milestones.md](milestones.md)).

**Outputs:** Blockers escalated to integration standup; no cross-stream commitments without contract gate check.

## Integration standup

**Purpose:** Cross-stream dependencies, contract gate status, tracer bullet progress.

**Agenda (30 min):**

1. Milestone burn-down — which gates are open?
2. Blockers from [dependency-graph.md](integration/dependency-graph.md)
3. Contract gates pending architect approval ([contract-gates.md](integration/contract-gates.md))
4. Demo readiness (within 4 weeks of M5 only)

**Escalation:** Unresolved blockers > 3 days → program lead.

## Milestone review

**Purpose:** Demo milestone DoD; go/no-go to next milestone.

**When:** End of each M0–M5 ([milestones.md](milestones.md)).

**Agenda:**

1. Live demo of milestone definition of done
2. Integration lead confirms E2E in integrated environment
3. Work Catalog steward confirms catalog deliverables for milestone
4. Value checkpoint sign-off ([value-checkpoints.md](value-checkpoints.md))
5. Program lead: proceed or hold

**Artifact:** Milestone sign-off recorded (date, attendees, open risks).

## Architecture review

**Purpose:** Module boundary integrity, contract gate approval, ACE/UPIM alignment.

**Owner:** Platform architect.

**Triggers for ad-hoc review:**

- New cross-module API or event
- Orchestrator action not in platform default workflow
- Deviation from [module-boundaries.md](phase-1/module-boundaries.md)

## Catalog review

**Purpose:** Work Catalog content quality and sequencing ahead of Orchestrator implementation.

**Owner:** Catalog steward.

**Participants:** Discovery, Build, Governance track owners; Control Plane (WCM + Orchestrator representative).

**Rules:**

- Catalog content for stage N must be reviewed **before** Control Plane implements handlers for stage N
- Indicative scenario YAML cannot ship as authoritative without track owner sign-off
- Cross-track handoff changes require all three track owners

## Program steering

**Purpose:** Budget (when available), scope drift, staffing, stakeholder alignment.

**Outputs:** Scope changes reflected in [phase-1-scope.md](phase-1/phase-1-scope.md) via change request; milestone dates updated in [milestones.md](milestones.md).

## Escalation path

```text
Squad lead → Integration standup → Program lead → Executive steering
Platform architect (parallel) for boundary/contract disputes
```

## Distinction from product governance

| This document | ACE Governance Workspace |
|---------------|--------------------------|
| Governs the **build program** | Governs **Product Intent transitions** in a Workbench |
| Program lead, EMs | Governance reviewers, release authority |
| Milestones, contract gates | Transition scenarios, evidence, verdicts |

## Read next

- [people-plan.md](people-plan.md) — roles
- [milestones.md](milestones.md) — milestone reviews
- [integration/contract-gates.md](integration/contract-gates.md) — architect approval
