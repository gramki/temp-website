# Governance Enforcement

**Model:** Work Model
**Track:** Track 6: Governance (ACE extension)
**Category:** Orchestration
**Owner:** Governance, Compliance, Security, Product Operations, or delegated policy owner

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
| Target Item | Reference | Orchestration item, Work Order, transition, artifact, evidence bundle, or state being evaluated |
| Trigger Event | Event / Reference | Event that caused enforcement |
| Enforcement Mode | Enum | Block, warn, allow-with-debt, allow-with-risk, require-exception |
| Evidence Evaluated | List | Evidence used to evaluate policy |
| Result | Enum | Pass, Warn, Fail, Exception Requested, Exception Approved |
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
| Exception Requested | Bypass requested |
| Exception Approved | Bypass approved with rationale |
| Routed | Follow-up risk/debt/remediation work created |
| Closed | Enforcement instance complete |

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
