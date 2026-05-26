# Governance Artifacts and Registers

Governance Rituals and Governance Enforcement produce durable outputs. These outputs are not the work itself; they are records, artifacts, and register entries created by governance work.

## Governance artifacts

| Artifact | Classification | Notes |
|----------|----------------|-------|
| Governance Finding | Work Artifact | Durable record of issue, gap, concern, or observation found during ritual/enforcement. |
| Violation | Finding subtype | Policy was not satisfied. |
| Warning | Finding subtype | Concern exists but does not block. |
| Exception Record | Work Artifact | Approved deviation from policy with rationale, approver, expiry, and conditions. |
| Approval Record | Work Artifact | Durable record that gate/transition was approved. |
| Rejection Record | Work Artifact | Durable record that gate/transition was rejected and why. |
| Evidence Bundle | Work Artifact | Collection of evidence used to satisfy policy or ritual review. |
| Audit Record | Work Artifact | Immutable record of governance action, actor, timestamp, input, and verdict. |

## Register artifacts

| Register entry | Classification | Notes |
|----------------|----------------|-------|
| Risk Register Entry | Register Artifact | Tracks exposure, severity, owner, mitigation, and due date. |
| Debt Register Entry | Register Artifact | Tracks accepted or deferred non-compliance, quality debt, process debt, technical debt, or governance debt. |
| Compliance Register Entry | Register Artifact | Tracks compliance obligation, control status, and audit readiness. |
| Deferred Obligation | Register Artifact | Commitment to remediate later after allowing progress. |
| Recognition Entry | Register Artifact | Evidence-backed appreciation or recognition surfaced through a ritual or governance work. |

## Kudos Register

The **Kudos Register** records positive operating behavior surfaced through rituals, governance reviews, delivery recovery, incident handling, or cross-functional collaboration.

Recognition entries may capture:

- recognized person, team, or agent;
- originating ritual;
- linked Product Intent, Discovery Case, Work Order, incident, or release;
- behavior demonstrated;
- evidence reference;
- recognition type;
- nominator;
- visibility;
- whether the behavior should become a reusable practice pattern.

Recognition types may include:

- high-quality decision;
- strong evidence discipline;
- excellent collaboration;
- effective incident handling;
- strong technical judgment;
- reusable pattern discovered;
- governance excellence;
- delivery recovery;
- risk surfaced early;
- effective agent use.

## Relationship to Evolve

Some recognition entries should trigger Evolve work:

```text
Recognition Entry
  -> reusable practice identified
  -> Evolve Case
  -> playbook / standard / dashboard update
```

This keeps governance from being purely punitive. Governance should reinforce the operating model by recognizing practices worth repeating.
