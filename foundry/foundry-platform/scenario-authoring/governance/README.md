# Governance Track — Scenarios

**Track:** Governance — transition validation, evidence capture, policy application, audit-trail production, and management reporting.

> **Note:** Governance is introduced at the ACE layer as a Track that extends UPIM's set.

## Structure

Unlike other Tracks, the **Governance Track has scenarios only in the Governance Workspace**. Other Workspaces do not execute Governance Track scenarios — they are the *subjects* of governance, not the executors.

The active folder is:

| Workspace | Folder | Status |
|-----------|--------|--------|
| Governance | [governance/](governance/) | Active — all Governance scenarios live here |
| Product Specification | — | Not applicable |
| UX Design | — | Not applicable |
| Development | — | Not applicable |
| QA | — | Not applicable |
| Release | — | Not applicable |

## How Governance Scenarios work

Governance Scenarios are **invoked by the [Orchestrator](../../orchestrator/README.md) through Governance Rituals or Governance Enforcement at trigger points**. A Governance Scenario corresponds to a trigger — a point in the flow where ritual work, validation, evidence capture, recognition, or policy enforcement is required.

**Trigger points include:**
- Workspace Work Order creation on an orchestration item
- Work Order state transitions
- Orchestration-item movement between Workspaces (including Product Intent and other primary items)
- Cadence-based or event-triggered Governance Rituals
- Policy assertion through Governance Enforcement
- Artifact promotion (e.g., from build to release)
- Gate checkpoints (quality gates, approval gates)
- Track transitions

**What a Governance Scenario does:**
- Validates that work meets policy requirements
- Captures evidence of compliance (writes to repositories)
- Produces audit trails
- Returns a verdict (pass/fail/warn) that the Orchestrator uses to allow or block the transition

## Scope of Governance

Beyond transition validation, Governance includes **management reporting and analytics**:

### Work Analytics
- Work Order throughput, cycle time, lead time
- Work in progress (WIP) by Track, Workspace, team
- Bottleneck identification
- Say/Do metrics (planned vs delivered)

### Human Analytics
- Task completion rates by builder
- Time-to-pickup for Human Tasks
- Skill utilization
- Capacity and availability

### Agent Analytics
- Agent efficiency (tasks completed, time per task)
- Agent effectiveness (quality of outputs, rework rates)
- Skill coverage (which scenarios have capable agents)
- Cost per Work Order

### Compliance & Audit
- Policy adherence rates
- Gate pass/fail rates
- Evidence completeness
- Audit trail integrity

## Example Scenarios

| Scenario | Trigger | What it does |
|----------|---------|--------------|
| Validate Build Evidence | Artifact promotion | Checks that build artifacts have required evidence (tests passed, scans clean) |
| Enforce Quality Gate | Work Order completion | Validates quality criteria before allowing state transition |
| Run Product Intent Review Ritual | Cadence / on-demand | Reviews Product Intent status, evidence gaps, decisions, action items, and recognitions |
| Capture Release Approval | Release publish | Records approval evidence, signs artifacts |
| Validate Discovery to Build Handoff | Discovery Case closure → Product Intent acceptance | Confirms evidence, PDR, Product Intent purpose, and PM alignment are present |
| Register Governance Finding | Enforcement warning/failure | Creates finding, risk/debt entry, exception, recognition, or remediation work |
| Evaluate Control Objective | Governance Enforcement | Evaluates Control Objective Indicators and thresholds against target evidence |
| Create Debt and Catch-Up Plan | Enforcement allow-with-debt | Creates Debt Register Entry, Catch-Up Plan, due date, and remediation Work Order |
| Review Exception or Waiver Request | Enforcement require-exception | Routes request to Approver and records Exception/Waiver outcome |
| Generate Compliance Report | Scheduled / on-demand | Produces compliance reports for management |
| Calculate Velocity Metrics | Work Order completion | Updates velocity and throughput dashboards |
| Audit Agent Effectiveness | Periodic | Analyzes agent performance across scenarios |

## Adding Scenarios

Governance scenario definitions live in [governance/](governance/). A scenario definition includes:

- Scenario name and trigger point
- Policies evaluated
- Evidence captured
- Repositories written to
- Verdict logic (pass/fail/warn criteria)
- Report outputs (if applicable)
- Control Objective / Control Objective Indicator references
- Governance Authority Matrix row or resolution rule
- Debt + Catch-Up outputs, if applicable
- Exception / Waiver outputs, if applicable
- Register outputs and audit-record requirements

## Read next

- [../README.md](../README.md) — Scenario Authoring module overview
- [../../../ace/governance.md](../../../ace/governance.md) — Governance in ACE
- [../../orchestrator/README.md](../../orchestrator/README.md) — how Orchestrator invokes Governance Scenarios
