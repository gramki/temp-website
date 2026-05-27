# Governance Artifacts and Registers

Governance Rituals and Governance Enforcement produce durable outputs. These outputs are not the work itself; they are records, artifacts, and register entries created by governance work.

## Governance artifacts

| Artifact | Classification | Notes |
|----------|----------------|-------|
| Governance Finding | Work Artifact | Durable record of issue, gap, concern, or observation found during ritual/enforcement. |
| Violation | Finding subtype | Policy was not satisfied. |
| Warning | Finding subtype | Concern exists but does not block. |
| Exception Record | Work Artifact | Time-bound authorized policy deviation for a specific target. Subtype: Waiver when the deviation is a skipped or abbreviated control step. |
| Approval Record | Work Artifact | Durable record that gate/transition was approved. |
| Rejection Record | Work Artifact | Durable record that gate/transition was rejected and why. |
| Evidence Bundle | Work Artifact | Collection of evidence used to satisfy policy or ritual review. |
| Audit Record | Work Artifact | Immutable record of governance action, actor, timestamp, input, and verdict. |
| Catch-Up Plan | Work Artifact | Scheduled remediation for debt or deferred control; links Debt Register Entry, indicators, due date, and remediation Work Orders. |
| Waiver Record | Work Artifact | Approved skip or abbreviation of a control step; includes rationale, approver, expiry, and linked target. |

## Register artifacts

| Register entry | Classification | Notes |
|----------------|----------------|-------|
| Risk Register Entry | Register Artifact | Tracks exposure, severity, Risk Owner, mitigation, and due date. |
| Debt Register Entry | Register Artifact | Tracks accepted non-compliance with mandatory Catch-Up Plan reference, Debt Owner, indicator snapshot, and due date. |
| Compliance Register Entry | Register Artifact | Tracks compliance obligation, control status, and audit readiness. |
| Deferred Obligation | Register Artifact | Deprecated term — use Debt Register Entry + Catch-Up Plan. Legacy alias for debt accepted with future remediation. |
| Recognition Entry | Workforce Register Artifact | Evidence-backed appreciation or recognition surfaced through a ritual or governance work; stored in WFR because it recognizes people, teams, or agents. |

## Debt + Catch-Up vs Exception / Waiver

When a control is not fully satisfied, enforcement mode determines which durable outcome path applies. These are not interchangeable.

| Path | Enforcement mode | Meaning | Primary artifacts | Work may proceed? |
|------|------------------|---------|-------------------|-------------------|
| **Debt + Catch-Up** | `allow-with-debt`, `allow-with-risk` when debt is recorded | Objective not met, but progress is permitted with a tracked obligation to remediate. | Debt Register Entry, Catch-Up Plan, optional Governance Finding | Yes, with due date and repayment evidence |
| **Exception / Waiver** | `require-exception` -> approved | Time-bounded, approver-granted deviation from the control for a specific target. A waiver is an authorized exception for a skipped/abbreviated control step. | Exception Record / Waiver Record | Yes, only after approval |

Use Debt + Catch-Up when the objective still applies and remediation is planned. Use Exception / Waiver when policy allows a formal deviation for bounded time or scope. Block when neither path is permitted.

## Workforce Recognition / Kudos Register

The **Kudos Register** records positive operating behavior surfaced through rituals, governance reviews, delivery recovery, incident handling, or cross-functional collaboration.

Kudos is a positive output of governance, but its system of record is the **Workforce Repository (WFR)** because it recognizes people, teams, and agents. Governance records the ritual or enforcement context; WFR stores the recognition; PEIR preserves traceability; Evolve may promote reusable practices into PPR.

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
Governance Ritual
  -> Recognition Entry
  -> WFR
  -> PEIR trace
  -> Evolve Case, if reusable practice identified
  -> PPR playbook / standard / dashboard update
```

This keeps governance from being purely punitive. Governance should reinforce the operating model by recognizing practices worth repeating.
