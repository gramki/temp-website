# Governance in ACE

> **TODO — Introduce Governance as a Track at the ACE layer.** UPIM defines five Tracks (Discovery, Build, Run, Win, Evolve). ACE extends this set by introducing a **Governance Track** as a first-class value stream, in addition to the Governance Workspace described below. The Track captures governance work as a flow (transition validations, evidence capture, policy application, audit-trail production) with its own work entities and lifecycle; the Workspace remains the station where that work is executed. The two framings need to be reconciled across [concepts.md](concepts.md), [repositories.md](repositories.md), and [relationships.md](relationships.md) — including the relationship between the Governance Track and UPIM's Operating Model.

## The rule

> Every governed transition invokes Governance Enforcement, and may invoke Governance Rituals when human review, cadence, or decision authority is required.

The original ACE model said every transition of Product Intent invokes Scenarios in the Governance Workspace. That remains true at the ACE Workspace execution layer, but it is now refined: **Governance Ritual** and **Governance Enforcement** are the Governance Track orchestration items; **Scenarios** are how the Governance Workspace executes them.

## What it means

Governance in ACE is **not a stage gate at the end of a pipeline**. It is **a property of motion** and of operating rhythm. Every time an orchestration item moves across a governed boundary — for example Product Intent moving from Specification to Development, a Discovery Case closing into Product Intent, a Release readiness decision, or a policy exception request — that transition is a first-class event.

The Governance Workspace does not own the product/build/run/win/evolve work being governed. It owns the **discipline of the handoff and operating practice**: validation that the right preconditions are met, that the right evidence is captured, that the right policy applies, that the right ritual has occurred when needed, and that the transition or decision is recorded.

Governance operates through two primary orchestration items:

- **Governance Ritual** — cadence-based or event-triggered governance practice that brings participants, reports, dashboards, evidence, and decision authority together.
- **Governance Enforcement** — policy assertion/control execution against an orchestration item, transition, artifact, evidence bundle, or state.

Governance Case is reserved for complex investigations/escalations, not every governance action.

## Why governance is a workspace, not a pipeline stage

If governance were a stage gate, it would sit between specific workspaces (e.g. between QA and Release). But every edge in the [Product Evolution Cycle](product-evolution-cycle.md) needs validation, including the bidirectional Specification ↔ UX edge and the optional return paths from Development and QA back to Specification. A stage-gate model would either miss those edges or apply heavy machinery to all of them. ACE chooses a different model: a Governance Track whose orchestration items execute through the Governance Workspace.

The practical consequence is that governance is composable: new transition types (e.g. when Engagement Engineering extends the system for client delivery) can declare their own rituals, enforcement policies, and Governance Workspace scenarios without rewriting the workspace topology.

## How rituals and enforcement work

Governance Rituals consume reports, dashboards, metrics, evidence, orchestration items, Work Orders, and register entries. They produce decisions, action items, approvals, rejections, exceptions, findings, risk/debt/compliance entries, recognition entries, and sometimes Evolve Cases.

Governance Enforcement consumes policies, target items, transitions, artifacts, and evidence. It produces pass/fail/warn/exception verdicts, findings, violations, warnings, risk/debt entries, remediation Work Orders, and audit records.

Rituals may contain enforcement. Enforcement may trigger rituals. Both may trigger Evolve Cases when governance practice itself needs improvement.

Recommended rituals and release-readiness control families are described in [governance-rituals.md](governance-rituals.md).

## Governance in plain language

Governance is how ACE makes sure important work follows agreed rules, uses the right evidence, involves the right people, records decisions clearly, and learns from both violations and good practice.

Useful shorthand:

```text
Admin configures.
Owner is accountable.
Approver authorizes.
Enforcement evaluates.
Registers remember.
Evolve improves.
```

## Control hierarchy

Controls inherit through ACE's operating structure:

```text
Foundry controls
  -> Workspace controls
    -> Workbench controls
```

Foundry-level controls define baseline expectations. Workspace and Workbench scopes may add controls or tighten inherited controls. They may override only where the parent scope permits. Exception and debt requests route to the effective Control Owner or delegated Approver after inheritance is resolved.

## Control Objective and Indicator

A **Control Objective** states what must hold. A **Control Objective Indicator** is the observable metric, evidence, dashboard field, or register state used to evaluate whether it holds.

Build Quality Objectives and Indicators are specializations of this general model:

- Build Quality Objective = Build-quality Control Objective.
- Build Quality Indicator = Build-quality Control Objective Indicator.

## Debt + Catch-Up vs Exception / Waiver

- **Debt + Catch-Up** is for temporary deviations that still need remediation. Progress is allowed, but the debt is registered, assigned, given a repayment date, and closed only with repayment evidence.
- **Exception / Waiver** is for non-applicability, alternate control, or bounded bypass approved by the relevant Approver. It is time-bound or scope-bound and does not silently erase the control.

## Kudos and recognition

Governance should not only find problems. Rituals may produce Kudos / Recognition entries when teams, people, or agents demonstrate strong evidence discipline, excellent collaboration, early risk surfacing, effective recovery, or reusable practice patterns.

## Work cadences vs governance rituals

Daily Flow Review, Sprint / Iteration Planning, Sprint / Iteration Review, and Sprint / Iteration Retrospective are primarily Work or team operating cadences. Governance does not own those cadences. Governance may define controls that require evidence that those cadences occurred, produced expected outputs, escalated blockers, and routed repeated issues to Evolve.

Cost, velocity, and efficiency are governance indicators of operating health, not individual surveillance metrics. Raw data may appear in Progress, Team, Agent, and Track consoles; Governance uses those metrics as Control Objective Indicators in rituals and operating reviews.

## What governance work does

Governance work, when invoked by a ritual or enforcement item, is responsible for:

1. **Verifying preconditions** — does the source workspace's output meet the contract for the transition?
2. **Evaluating controls** — for each applicable control, does the Control Objective hold as shown by its Control Objective Indicators? Outcome: pass, warn, block, Debt + Catch-Up, or Exception / Waiver per enforcement mode.
3. **Capturing evidence** — what artifacts, records, or signals must be persisted for audit and traceability? Where do they go in the repositories?
4. **Recording the transition** — the transition itself is a recordable event in the workshop's history.
5. **Producing outputs** — decisions, findings, approvals, rejections, exceptions, register entries, recognition entries, remediation Work Orders, or Evolve Cases.

Scenarios in the Governance Workspace, like scenarios in any other workspace, decompose into Tasks completed by the workspace's Human–Agent Team. They are the execution mechanism for Governance Rituals and Governance Enforcement. Some governance scenarios will be heavily automated; some will require human judgment. The workspace runs the same way either way.

Scenarios are ACE Workspace definitions. They are not UPIM entities; UPIM supplies the policies, artifacts, register records, orchestration items, and evidence that governance scenarios read or write.

## Relationship to security, compliance, audit

The Foundry Platform engineers security, compliance, audit, monitoring, and logging as first-class concerns of the Foundry Specification. Source: [../foundry-platform/platform.TODO](../foundry-platform/platform.TODO) lines 1-9.

Governance is the **operational layer** that consumes those facilities. A compliance requirement (e.g. that release artifacts include an evidence pack) is expressed as a Governance Enforcement policy assertion, and may also be reviewed through a Governance Ritual such as release readiness. The platform provides the substrate; governance orchestration provides the discipline.

Governance also applies when Discovery decisions establish or update Product Intent and when PSD changes refine an existing Product Intent record. Those transitions are part of the same governed motion: intent is not considered ready to move simply because a document exists.

In Engagement contexts, evidence requirements multiply (Customer Product Artifacts, Verification Artifacts, Documentation Artifacts, Evidence Artifacts, Knowledge Base — see [../engagement-engineering/1.TODO](../engagement-engineering/1.TODO) lines 17-26). Governance Enforcement and Governance Rituals are how those requirements are applied without spreading their logic across every workspace; Governance Workspace scenarios execute the required work.

## Relationship to UPIM

UPIM's Operating Model captures coordination patterns (ritual definitions, cadences, decision rhythms), governance policies, evidence requirements, participant roles, decision authority, reports, dashboards, and register definitions. Governance Rituals and Governance Enforcement execute those Operating Model definitions. Governance Workspace Scenarios are the ACE execution mechanism used to run the ritual/enforcement work.

The Practitioner Repository (PPR) and the Workforce Repository (WFR) are the relevant homes for governance content. PPR holds the standards, templates, practices, verification policies, ritual definitions, and guidance; WFR holds the role bindings and skills (human and agent) that execute governance work. See [repositories.md](repositories.md) and [../product-information-model/README.md](../product-information-model/README.md).

The Operating Model now owns governance policies, ritual definitions, cadence, participant roles, decision authority, evidence requirements, reports/dashboards, and register definitions. Governance Track work executes those definitions. Evolve Track changes them when governance itself needs to improve.

## What governance is not

- **Not only an approval workflow.** Governance includes rituals, policy enforcement, evidence capture, findings, registers, recognition, and evolution of governance practice.
- **Not a final gate.** Governance runs on every transition, including bidirectional and return transitions, not only the QA → Release edge.
- **Not a substitute for security or compliance engineering.** The platform provides those facilities; governance enforcement and rituals apply them at handoffs and cadences.
- **Not optional.** A workspace that emits intent without invoking governance on the transition has not completed the transition; intent has not actually moved.

## Implementation expectations

For the Foundry Platform, the governance rule implies:

- The platform **must hook** into every governed orchestration-item transition, not selectively.
- The platform **must create Governance Enforcement items** for policy assertions on transitions, artifacts, evidence, and states.
- The platform **must support Governance Ritual items** for cadence-based and event-triggered reviews.
- The platform **must support governance scenarios as ACE Workspace execution mechanisms** in the Governance Workspace, with the same Scenarios → Tasks → Human–Agent Team mechanics as any other workspace.
- The platform **must persist evidence, findings, verdicts, exceptions, register entries, audit records, and recognition entries** in the appropriate repositories/registers at the time governance work runs, not after.
- The platform **must support extension**: when Engagement Engineering or other extensions add transition types, the governance machinery must accommodate new rituals, policies, enforcement items, and scenarios without code changes to the base workspaces.

These expectations are realized under "Governance Workspace Engineering" in [../foundry-platform/platform.TODO](../foundry-platform/platform.TODO) and module specifications under [../foundry-platform/](../foundry-platform/README.md) over time.

## Worked example (illustrative)

Consider a Specification → Development transition.

- **Source workspace:** Product Specification, holding a specification ready to be built.
- **Target workspace:** Development.
- **Governance orchestration item:** Governance Enforcement for "Validate Specification → Development handoff."
- **Policy assertions:** PSD references Product Intent and PDR; cross-dimensional impact assessment exists; impacted modules are identified; Source and Quality repositories are prepared; required evidence is present.
- **Governance Workspace scenarios:** evaluate policy, capture evidence, record verdict, create finding/register entry if needed.
- **Outcome:** the transition passes; warns; blocks; proceeds with Debt + Catch-Up; or proceeds with Exception / Waiver.

Each task in this list is completed by the Governance Workspace's Human–Agent Team. Some tasks are fully automated; others may require a human practitioner to certify a judgment.

This example is illustrative, not normative. The exact set of tasks for any transition is determined by the Governance Enforcement item, the applicable Operating Model policies, and the Governance Workspace scenarios defined for the Workbench.
