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
| Decision authority | Who can approve, reject, defer, accept risk, or create exceptions |
| Outputs | Decisions, action items, findings, recognitions, approvals, exceptions, register entries |

Rituals should not be modeled as meetings alone. A ritual is a governed practice with inputs, authority, outputs, evidence, and follow-up.

## Governance policies

A Governance Policy defines a rule, standard, constraint, or invariant that should hold for work, artifacts, transitions, or evidence.

| Policy aspect | Description |
|---------------|-------------|
| Scope | Track, Workspace, transition, artifact, orchestration item, customer segment, compliance domain |
| Assertion | What must be true |
| Evidence requirement | What proof is required |
| Enforcement mode | Block, warn, allow-with-debt, allow-with-risk, require-exception |
| Exception rule | How and when the policy may be bypassed |
| Owner | Role accountable for policy definition and evolution |

Policy definitions are Operating Model entities. Evaluating a policy is Governance Enforcement work.

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

## Governance evolution loop

Governance practices evolve through the Evolve Track.

```text
Governance Ritual / Governance Enforcement
  -> Finding / trend / dashboard gap / recognition pattern
  -> Evolve Case
  -> Policy / ritual / report / dashboard / playbook update
```

Governance can identify that governance itself is ineffective. Evolve owns changes to policies, rituals, cadences, dashboards, reports, and playbooks.
