# Gate Enforcement

Gate Enforcement is the mechanism that blocks or allows orchestration item transitions based on governance verdicts, ensuring policy compliance before work advances.

## What it is

Gates are checkpoints in the orchestration workflow where work must pass governance review before proceeding. The Orchestrator invokes Governance Scenarios at these gates and uses the verdict to determine whether the transition is allowed.

Gate Enforcement implements the principle that **governance is distributed** — definition lives in Scenarios (Work Catalogues), enforcement lives in the Orchestrator, and evidence is captured in repositories. The Orchestrator doesn't decide policy; it executes the policy decisions made by governance definitions.

Two enforcement modes control gate behavior:

| Mode | Behavior |
|------|----------|
| `hard-block` | Transition cannot proceed until governance approves |
| `soft-block` | Transition requires manual override with recorded justification |

Hard blocks are for non-negotiable policy (security review before production release). Soft blocks are for advisory policy where business judgment may override (test coverage thresholds on urgent fixes).

## Where it lives

| Component | Location |
|-----------|----------|
| **Gate definitions** | OI Workflow YAML (`invoke-governance-scenario` actions) |
| **Governance invocation** | Action Executor |
| **Verdict handling** | Workflow Engine (matches `governance-completed` events) |
| **Override records** | Postgres `transition_history` (with justification) |

## Gate enforcement flow

```
Transition action with governance
    │
    ├── Action Executor creates governance WO
    │       │
    │       └── Governance Scenario executes
    │               │
    │               ├── Verdict: approved
    │               │       │
    │               │       └── Transition proceeds
    │               │
    │               └── Verdict: rejected
    │                       │
    │                       ├── hard-block: Transition blocked
    │                       │
    │                       └── soft-block: Override available
    │                               │
    │                               └── User overrides with justification
    │                                       │
    │                                       └── Transition proceeds (logged)
```

## Example workflow usage

```yaml
stages:
  - name: in-specification
    handlers:
      - when:
          event: work-order-completed
          params:
            wo-label: spec-wo
            status: completed
        then:
          - action: invoke-governance-scenario
            params:
              scenario: product-specification-review
              on-reject: soft-block
          - action: transition-orchestration-item
            params:
              to: specified

  - name: ready-for-release
    handlers:
      - when:
          event: work-order-completed
          params:
            wo-label: release-wo
            status: completed
        then:
          - action: invoke-governance-scenario
            params:
              scenario: customer-release-package-review
              on-reject: hard-block
          - action: transition-orchestration-item
            params:
              to: released
```

## Override handling

When a soft-blocked gate is overridden:

1. Authorized user requests override via Console or API
2. User provides mandatory justification
3. Orchestrator records override in `transition_history`:
   - Override timestamp
   - User identity
   - Justification text
   - Original governance verdict
4. Transition proceeds

Override authorization is role-based. Typically Workbench Managers can override soft-blocks within their Workbench; Program Managers can override for Release Intents.

## Governance verdicts

| Verdict | Hard-block behavior | Soft-block behavior |
|---------|---------------------|---------------------|
| `approved` | Transition proceeds | Transition proceeds |
| `rejected` | Transition blocked | Override available |
| `approved-with-findings` | Transition proceeds; findings logged | Transition proceeds; findings logged |
| `debt-registered` | May proceed per config | May proceed per config |

## Common gate patterns

| Gate | Stage | Typical mode |
|------|-------|--------------|
| Product specification review | in-specification → specified | soft-block |
| Test plan review | specified → in-qa | soft-block |
| Test coverage review | in-qa → ready-for-release | soft-block |
| Customer release package review | ready-for-release → released | hard-block |
| Security review | any → production-deployed | hard-block |

## Related concepts

- [Workflow Engine](workflow-engine.md) — Matches governance completion events
- [Action Executor](action-executor.md) — Executes `invoke-governance-scenario`
- [Dead Letter Queue](dead-letter-queue.md) — Governance failures may enter DLQ
- [Governance](../../concepts/governance.md) — Platform governance model
- [Scenario](../../concepts/scenario.md) — Governance Scenarios define the checks

## Further reading

- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Governance requirements (ORC-FR-0031 through ORC-FR-0035)
- [../user-guide/product-intent-journey.md](../user-guide/product-intent-journey.md) — See governance gates in action
- [../../ace/governance.md](../../ace/governance.md) — ACE governance model
