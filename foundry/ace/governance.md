# Governance in ACE

> **TODO — Introduce Governance as a Track at the ACE layer.** UPIM defines five Tracks (Discovery, Build, Run, Win, Evolve). ACE extends this set by introducing a **Governance Track** as a first-class value stream, in addition to the Governance Workspace described below. The Track captures governance work as a flow (transition validations, evidence capture, policy application, audit-trail production) with its own work entities and lifecycle; the Workspace remains the station where that work is executed. The two framings need to be reconciled across [concepts.md](concepts.md), [repositories.md](repositories.md), and [relationships.md](relationships.md) — including the relationship between the Governance Track and UPIM's Operating Model.

## The rule

> Every transition of Product Intent invokes Scenarios in the Governance Workspace.

This single sentence — adapted from [ace-model.md](ace-model.md) line 62 — is the entire governance discipline of ACE. It is a stronger statement than it looks.

## What it means

Governance in ACE is **not a stage gate at the end of a pipeline**. It is **a property of motion**. Every time Product Intent moves between two workspaces — Release to Specification, Specification to UX, Specification to Development, Specification to QA, Development to QA, QA to Release, Development or QA back to Specification — that transition is a first-class event, and the Governance Workspace responds to it with Scenarios of its own.

The Governance Workspace does not own the work being transitioned. It owns the **discipline of the handoff**: validation that the right preconditions are met, that the right evidence is captured, that the right policy applies, and that the transition is recorded.

## Why governance is a workspace, not a pipeline stage

If governance were a stage gate, it would sit between specific workspaces (e.g. between QA and Release). But every edge in the [Product Evolution Cycle](product-evolution-cycle.md) needs validation, including the bidirectional Specification ↔ UX edge and the optional return paths from Development and QA back to Specification. A stage-gate model would either miss those edges or apply heavy machinery to all of them. ACE chooses a different model: a workspace whose Scenarios are designed to validate transitions, invoked uniformly.

The practical consequence is that governance is composable: new transition types (e.g. when Engagement Engineering extends the system for client delivery) can declare their own governance scenarios without rewriting the workspace topology.

## What a governance scenario does

A governance scenario, when invoked on a transition, is responsible for:

1. **Verifying preconditions** — does the source workspace's output meet the contract for the transition?
2. **Applying policy** — what rules govern this kind of transition (security, compliance, release, audit), and do they pass?
3. **Capturing evidence** — what artifacts, records, or signals must be persisted for audit and traceability? Where do they go in the repositories?
4. **Recording the transition** — the transition itself is a recordable event in the workshop's history.

Scenarios in the Governance Workspace, like scenarios in any other workspace, decompose into Tasks completed by the workspace's Human–Agent Team. Some governance scenarios will be heavily automated; some will require human judgment. The workspace runs the same way either way.

## Relationship to security, compliance, audit

The Foundry Platform engineers security, compliance, audit, monitoring, and logging as first-class concerns of the Foundry Specification. Source: [../foundry-platform/platform.TODO](../foundry-platform/platform.TODO) lines 1-9.

Governance is the **operational layer** that consumes those facilities. A compliance requirement (e.g. that release artifacts include an evidence pack) is expressed as a governance scenario invoked on the QA → Release transition. The platform provides the substrate; governance scenarios provide the discipline.

Governance also applies when Discovery decisions establish or update Product Intent and when PSD changes refine an existing Product Intent record. Those transitions are part of the same governed motion: intent is not considered ready to move simply because a document exists.

In Engagement contexts, evidence requirements multiply (Customer Product Artifacts, Verification Artifacts, Documentation Artifacts, Evidence Artifacts, Knowledge Base — see [../engagement-engineering/1.TODO](../engagement-engineering/1.TODO) lines 17-26). Governance scenarios are how those requirements are enforced without spreading their logic across every workspace.

## Relationship to UPIM

UPIM's Operating Model captures coordination patterns (ceremonies, cadences, decision rhythms) and organizational design. Governance scenarios are *implementations* of operating-model coordination patterns — invoked on transitions, completed by the Governance Workspace's team, recorded in the operating-model–shaped repositories (Practitioner Repository, Workforce Repository).

The Practitioner Repository (PPR) and the Workforce Repository (WFR) are the relevant homes for governance content. PPR holds the standards, templates, practices, and verification policies; WFR holds the role bindings and skills (human and agent) that complete governance scenarios. See [repositories.md](repositories.md) and [../product-information-model/README.md](../product-information-model/README.md).

## What governance is not

- **Not a separate approval workflow.** Governance is invoked on transitions; it does not require a parallel ticketing system.
- **Not a final gate.** Governance runs on every transition, including bidirectional and return transitions, not only the QA → Release edge.
- **Not a substitute for security or compliance engineering.** The platform provides those facilities; governance scenarios apply them at handoffs.
- **Not optional.** A workspace that emits intent without invoking governance on the transition has not completed the transition; intent has not actually moved.

## Implementation expectations

For the Foundry Platform, the governance rule implies:

- The platform **must hook** into every intent transition, not selectively.
- The platform **must support governance scenarios as first-class scenarios** in the Governance Workspace, with the same Scenarios → Tasks → Human–Agent Team mechanics as any other workspace.
- The platform **must persist evidence** in the appropriate repositories at the time of the transition, not after.
- The platform **must support extension**: when Engagement Engineering or other extensions add transition types, the governance machinery must accommodate them without code changes to the base workspaces.

These expectations are realized under "Governance Workspace Engineering" in [../foundry-platform/platform.TODO](../foundry-platform/platform.TODO) and module specifications under [../foundry-platform/](../foundry-platform/README.md) over time.

## Worked example (illustrative)

Consider a Specification → Development transition.

- **Source workspace:** Product Specification, holding a specification ready to be built.
- **Target workspace:** Development.
- **Governance scenario invoked:** "Validate Specification → Development handoff."
- **Tasks** generated by the scenario might include: confirm specification meets the cross-dimensional impact assessment standard (a UPIM property of PSDs), confirm the impacted modules are identified, confirm the relevant repositories (Source, Quality & Verification) are prepared for the work, capture the transition record in the Product Evolution Repository, attach evidence artifacts to the work item.
- **Outcome:** the transition is either allowed and recorded, or returned to Specification with reasons.

Each task in this list is completed by the Governance Workspace's Human–Agent Team. Some tasks are fully automated; others may require a human practitioner to certify a judgment.

This example is illustrative, not normative. The exact set of tasks for any transition is the responsibility of the governance scenarios defined in the workshop, which in turn reference policies from the Practitioner Repository.
