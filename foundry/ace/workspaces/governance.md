# Governance Workspace

## Purpose

Validate **every transition** of Product Intent. The Governance Workspace is invoked on each handoff between any two workspaces in the Product Evolution Cycle. It does not own the work being transitioned; it owns the discipline of the handoff. Source: [`../ace-model.md`](../ace-model.md) line 62.

**Primary human personas:** Engineering Managers (primary), with Product Operations and audit roles participating where applicable.

The full discipline is documented in [`../governance.md`](../governance.md). This file describes the workspace itself; the rule and its rationale are documented separately because the rule is invoked across all workspaces.

## Metrics and signals (TBD)

**DORA-style** and related delivery-health signals (lead time, deployment frequency, change-fail rate, recovery time, and aligned governance KPIs) are expected to surface through Governance Workspace engineering, observability, and cross-workshop reporting. Detail will be specified alongside Governance Workspace platform work — see [`../../foundry-platform/platform.TODO`](../../foundry-platform/platform.TODO) line 24.

## Inbound and outbound intent

The Governance Workspace's relationship to intent is different from the other five workspaces:

- It does not produce intent.
- It does not consume intent in the way Product Specification or Development does.
- It is **invoked on every transition** of intent between any two workspaces in the cycle.

Practically, the workspace receives transition events (with the intent and its source/target context attached), runs scenarios on those events, and decides whether the transition is valid.

## Primary scenarios (illustrative)

This workspace owns scenarios such as:

- Validating that the source workspace's output meets the contract for the transition.
- Applying policy (security, compliance, release readiness, audit) to the transition.
- Capturing evidence and persisting it in the appropriate repositories.
- Recording the transition itself in the workshop's history.

Concrete scenario catalogs live in [`../../foundry-platform/`](../../foundry-platform/) under "Governance Workspace Engineering" (see [`../../foundry-platform/platform.TODO`](../../foundry-platform/platform.TODO) line 24).

## Repositories touched

- **Practitioner Repository (PPR)** — read. The standards, templates, and verification policies a transition is validated against.
- **Workforce Repository (WFR)** — read. Role bindings (human and agent) authorized for governance scenarios.
- **Product Evolution & Impact Repository (PEIR)** — write. Transition records and impact lineage.
- **Quality & Verification Repository (QVS)** — write (evidence captured at transition time).
- **Product Intent Repository (PIR)** — read.
- **Work Repository (WR)** — write.

See [`../repositories.md`](../repositories.md).

## Why governance is a workspace, not a stage gate

A stage-gate model would sit between specific workspaces (e.g. between QA and Release). The Product Evolution Cycle has many transitions — including the bidirectional Specification ↔ UX edge and the optional return paths from Development and QA back to Specification. A workspace whose Scenarios are designed to validate transitions, invoked uniformly, is more composable than a fixed set of gates. See [`../governance.md`](../governance.md) for the full argument.

## See also

- [`../governance.md`](../governance.md) — the governance discipline.
- [`../product-evolution-cycle.md`](../product-evolution-cycle.md) — the transitions this workspace validates.
- [`../../foundry-platform/platform.TODO`](../../foundry-platform/platform.TODO) — Governance Workspace Engineering.
