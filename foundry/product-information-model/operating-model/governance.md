# Governance Operating Model

Governance is defined in the Operating Model and executed through Governance Track work. The Operating Model defines what governance is supposed to do: rituals, policies, evidence expectations, participant roles, decision authority, reports, dashboards, and registers.

The Work Model defines the orchestration items that execute governance:

- **Governance Ritual**
- **Governance Enforcement**

## Core model

```text
Operating Model
  Ritual Definition
  Governance Policy
  Evidence Requirement
  Cadence
  Participant Role
  Decision Authority
  Report / Dashboard
  Register Definition

Governance Track
  Governance Ritual
  Governance Enforcement

Work Artifacts / Registers
  Findings, approvals, evidence, audit records
  Risk, debt, compliance, kudos entries

Evolve Track
  Governance Evolution Case
  Policy / ritual / dashboard / playbook updates
```

## Governance in plain language

Governance is how the organization makes sure important work follows agreed rules, uses the right evidence, involves the right people, records decisions clearly, and learns from both violations and good practice.

Examples:

- Before release, prove the required QA evidence exists.
- If a control is below target but above the hard minimum, allow progress only with Debt + Catch-Up.
- If a policy does not apply to a specific case, request an Exception / Waiver.
- If a team demonstrates strong evidence discipline or excellent recovery, record recognition in the Kudos Register.

## Admin, owner, approver

Governance distinguishes configuration, accountability, and authorization.

```text
Admin configures.
Owner is accountable.
Approver authorizes.
```

| Term | Meaning |
|------|---------|
| **Governance Admin** | Configures governance settings and definitions at a scope. |
| **Owner** | Accountable for a control, policy, evidence contract, risk, or debt over time. |
| **Approver** | Authorized to approve debt, exception, waiver, risk acceptance, transition, or override. |

Scoped admin roles:

| Admin role | Meaning |
|------------|---------|
| **Foundry Governance Admin** | Configures Foundry-level governance defaults and override permissions. |
| **Workspace Governance Admin** | Configures Workspace-level governance where Foundry permits. |
| **Workbench Governance Admin** | Configures Workbench-level governance where Workspace permits. |

A Governance Admin is not automatically the Control Owner. An Admin can configure a control; the Control Owner is accountable for whether the control remains fit for purpose; an Approver authorizes a specific decision at enforcement or ritual time.

## Ritual definitions

A Ritual Definition describes a repeatable governance practice. Rituals can be cadence-based or event-triggered.

| Field | Description |
|-------|-------------|
| Purpose | Why the ritual exists |
| Cadence / trigger | Weekly, sprintly, release-bound, transition-triggered, quarterly, on-demand |
| Participants | Roles expected to attend or review |
| Entry criteria | What must be available before the ritual starts |
| Inputs | Reports, dashboards, metrics, evidence, cases, Product Intents, Work Orders, register items |
| Agenda / checklist | What must be reviewed |
| Decision authority | Approvers who can approve, reject, defer, accept risk, authorize debt with Catch-Up Plan, or grant Exception / Waiver |
| Control Owner | Role accountable for the ritual definition and its inputs remaining current |
| Outputs | Decisions, action items, findings, recognitions, approvals, exceptions, register entries |

Rituals should not be modeled as meetings alone. A ritual is a governed practice with inputs, authority, outputs, evidence, and follow-up.

## Governance policies

A Governance Policy defines a rule, standard, constraint, or invariant that should hold for work, artifacts, transitions, or evidence.

Each Governance Policy expresses a control through:

- **Control Objective** — the outcome the organization requires. In plain language: what must hold?
- **Control Objective Indicator** — an observable signal that indicates whether the objective is being met: a metric, evidence artifact, dashboard value, register state, or checklist item.
- **Control Objective Threshold** — the pass/warn/fail boundaries for an indicator at a given scope.

```text
Control Objective
  -> Control Objective Indicator(s)
    -> Control Objective Threshold(s)
```

Example:

```text
Control Objective:
  Unit test coverage should be healthy.

Control Objective Indicator:
  measured coverage = 72%

Threshold:
  minimum required = 60%
  target / enforcement threshold = 80%

Result:
  72% is not a hard fail, but requires Debt + Catch-Up if policy allows debt.
```

**BQO/BQI mapping:** A Build Quality Objective (BQO) is a Build-quality Control Objective. A Build Quality Indicator (BQI) is a Build-quality Control Objective Indicator. BQO/BQI are useful domain aliases, but the Operating Model uses Control Objective and Control Objective Indicator generically.

| Policy aspect | Description |
|---------------|-------------|
| Scope | Track, Workspace, transition, artifact, orchestration item, customer segment, compliance domain |
| Control Objective | What must be true — the required outcome |
| Control Objective Indicators | Metrics, evidence checks, dashboard fields, or register signals that show objective status |
| Control Objective Thresholds | Effective pass/warn/fail boundaries after inheritance |
| Evidence requirement | What proof is required |
| Enforcement mode | Block, warn, allow-with-debt (Debt + Catch-Up), allow-with-risk, require-exception (Exception / Waiver) |
| Debt eligibility rule | Whether temporary non-compliance can be handled with Debt + Catch-Up |
| Exception rule | How and when the policy may be bypassed via Exception / Waiver |
| Control Owner | Role accountable for the control objective, indicators, evidence contract, and evolution |
| Governance Admin | Role permitted to author or change this policy definition |
| Decision Authority | Role(s) permitted to approve exceptions, waivers, debt, or risk acceptance |

Policy definitions are Operating Model entities. Evaluating a policy is Governance Enforcement work.

## Control inheritance and overrides

Governance controls inherit downward. Enforcement evaluates the effective control at the narrowest matching scope.

```text
Foundry-level control
  -> Workspace-level configuration
    -> Workbench-level configuration
```

| Level | Governance Admin | Typical content |
|-------|------------------|-----------------|
| **Foundry** | Foundry Governance Admin | Organization baselines, regulatory minima, default thresholds, core Ritual Definitions |
| **Workspace** | Workspace Governance Admin | Workspace-specific defaults and allowed override rules |
| **Workbench** | Workbench Governance Admin | Product/engagement-specific thresholds, additional indicators, local ritual cadence |

Rules:

1. Lower scopes inherit controls from upper scopes.
2. Lower scopes may override only where the parent scope permits.
3. Children may tighten thresholds unless an explicit Exception / Waiver allows relaxation.
4. Children may add indicators; they may not silently remove parent-mandated indicators.
5. Effective values are resolved at enforcement time and recorded in the Audit Record.
6. Exception and debt requests route to the effective Control Owner or delegated Approver.

## Debt + Catch-Up vs Exception / Waiver

When governance does not pass, the Operating Model distinguishes remediation debt from approved deviation.

| Path | Use when | Durable records |
|------|----------|-----------------|
| **Debt + Catch-Up** | The control still applies, progress is allowed temporarily, and remediation is required. | Debt Register Entry + Catch-Up Plan |
| **Exception / Waiver** | The policy does not apply, an alternate control is accepted, or a one-time bypass is approved. | Exception Record / Waiver |

Debt + Catch-Up requires:

- Debt Owner;
- Debt Approver;
- Catch-Up Plan;
- repayment date;
- repayment evidence;
- re-evaluation or ritual closure.

Exception / Waiver requires:

- scoped target;
- rationale;
- Approver;
- expiry or review condition;
- compensating control where applicable.

Use Debt + Catch-Up by default for temporary deviations that must be remediated. Use Exception / Waiver for non-applicability, alternate controls, or bounded bypass.

## Reports and dashboards

Reports and dashboards are operating artifacts that support rituals and enforcement. They are not incidental UI; they are part of the governance operating model.

Examples:

- Ritual Dashboard
- Governance Compliance Dashboard
- Risk / Debt Dashboard
- Evidence Completeness Report
- Release Readiness Report
- Discovery Readiness Report
- Product Intent Governance Status
- Governance Trend Report
- Kudos / Recognition Summary

Dashboards can be ritual inputs and ritual outputs. Trends in dashboards may trigger Evolve Cases.

## Registers

Registers are durable management records. They may be created by rituals or enforcement.

- Risk Register
- Debt Register
- Compliance Register
- Deferred Obligation Register
- Kudos / Recognition Register

The Kudos Register is the positive counterpart to risk and debt registers. Governance should recognize good practice, not only police bad practice.

## Repository mapping

Governance definitions and outputs map to semantic UPIM repositories, not implementation services.

| Item | Repository |
|------|------------|
| Governance Policy | PPR |
| Policy Control | PPR |
| Ritual Definition | PPR |
| Evidence Requirement | PPR |
| Control Objective | PPR |
| Threshold Configuration | PPR |
| Governance Authority Matrix | WFR + PPR |
| Governance Finding | WR while active; PEIR when closed |
| Risk Register Entry | WR while active; PEIR for history |
| Debt Register Entry | WR while active; PEIR for history |
| Catch-Up Plan | WR |
| Deferred Obligation | WR |
| Exception Request | WR |
| Exception Record / Waiver | WR while active; PEIR for audit |
| Approval / Rejection Record | PEIR |
| Evidence Bundle | Source-specific repo + PEIR index |
| Audit Record | PEIR |
| Compliance Register Entry | WR while active; PEIR historical |
| Kudos / Recognition Entry | WFR; PEIR trace |
| Reusable Practice Candidate | PPR / Evolve |

The Foundry Platform may implement these through any service design, but UPIM names the semantic repository ownership.

## Governance evolution loop

Governance practices evolve through the Evolve Track.

```text
Governance Ritual / Governance Enforcement
  -> Finding / trend / dashboard gap / recognition pattern
  -> Evolve Case
  -> Policy / ritual / report / dashboard / playbook update
```

Governance can identify that governance itself is ineffective. Evolve owns changes to policies, rituals, cadences, dashboards, reports, and playbooks.
