# Governance Enforcement

**Model:** Work Model
**Track:** Track 6: Governance (ACE extension)
**Category:** Orchestration
**Owner:** Role accountable for enforcement outcome follow-up
**Governance Admin:** Role that maintains the policy/control definition being enforced

## Definition

Governance Enforcement is a policy assertion orchestration item that evaluates a Governance Policy against an orchestration item, transition, artifact, evidence bundle, or state.

Enforcement may be automated, human-reviewed, or hybrid.

## Purpose

Governance Enforcement makes policy application explicit. It determines whether work can proceed, must be blocked, can proceed with warning, requires exception, or should create risk/debt/remediation follow-up.

## Fields

| Field | Type | Description |
|---|---|---|
| Enforcement ID | String | Unique enforcement instance identifier |
| Policy | Reference (Operating Model) | Governance Policy being asserted |
| Policy Control | Reference (Operating Model) | Specific control being evaluated |
| Control Objective | Reference (Operating Model) | Required outcome being asserted |
| Control Objective Indicator | Reference / Value | Measured or attested indicator being evaluated |
| Control Objective Threshold | Reference / Value | Effective threshold after inheritance |
| Effective Control Owner | Reference (WFR role binding) | Resolved accountability role for this control at this scope |
| Target Item | Reference | Orchestration item, Work Order, transition, artifact, evidence bundle, or state being evaluated |
| Trigger Event | Event / Reference | Event that caused enforcement |
| Enforcement Mode | Enum | Block, warn, allow-with-debt, allow-with-risk, require-exception, require-waiver |
| Evidence Evaluated | List | Evidence used to evaluate policy |
| Debt Allowed | Boolean | Whether Debt + Catch-Up is permitted for this control result |
| Debt / Catch-Up Plan | Reference | Debt Register Entry and Catch-Up Plan, if created |
| Exception / Waiver | Reference | Exception or Waiver Record, if requested/approved |
| Debt Approver | Reference | Role authorized to approve debt for this control |
| Exception Approver | Reference | Role authorized to approve exception/waiver for this control |
| Result | Enum | Pass, Warn, Hard Fail, Debt Required, Exception Required, Waiver Approved |
| Finding | Reference | Finding or violation produced, if any |
| Register Output | Reference | Risk/debt/compliance/deferred obligation entry, if any |
| Remediation Work | Reference | Follow-up Work Order or Evolve Case, if any |
| Status | Enum | Current lifecycle status |

## Statuses

| Status | Description |
|---|---|
| Triggered | Enforcement instance was created |
| Evaluating | Policy assertion is being evaluated |
| Awaiting Evidence | Required evidence is missing |
| Passed | Policy satisfied |
| Warning | Concern found but not blocking |
| Failed | Policy not satisfied |
| Debt Required | Control is in debt-eligible band and needs Debt + Catch-Up Plan |
| Exception Requested | Bypass requested |
| Exception Approved | Bypass approved with rationale |
| Waiver Approved | Control step waived with rationale, expiry, and conditions |
| Routed | Follow-up risk/debt/remediation work created |
| Closed | Enforcement instance complete |

## Outcome paths

| Result | Path | Next action |
|--------|------|-------------|
| Pass | — | Close enforcement |
| Warning | Advisory | Finding only; may still block per policy |
| Hard Fail | Block | Reject transition or require remediation before retry |
| Debt Required | Debt + Catch-Up | Create Debt Register Entry, Catch-Up Plan, due date, and remediation work |
| Exception Required | Exception / Waiver | Route to Exception Approver with rationale and target scope |
| Waiver Approved | Exception / Waiver | Record Waiver with approver, expiry, and conditions |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Evaluates | Governance Policy (Operating Model) | Enforcement applies a policy |
| Targets | Orchestration item / transition / artifact / evidence | Enforcement evaluates a specific target |
| May be contained in | Governance Ritual (Track 6) | Ritual may run enforcement |
| Produces | Governance Finding / Violation / Warning | Enforcement may produce findings |
| Produces | Risk / Debt / Compliance / Deferred Obligation entry | Enforcement may create register entries |
| May create | Remediation Work Order | Enforcement may create follow-up work |
| May trigger | Evolve Case (Track 5) | Repeated failures or policy gaps may trigger governance evolution |

## Examples

- Validate PDR finalization has PM alignment.
- Validate Product Intent Acceptance has required provenance.
- Validate PSD Approval has evidence and cross-dimensional review.
- Validate Release Readiness has QA evidence and approval records.
- Validate Discovery Support Product Intent is not included in customer release scope.
