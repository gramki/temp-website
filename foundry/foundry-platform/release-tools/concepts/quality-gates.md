# Quality Gates

Quality Gates are governance checkpoints embedded in CI pipelines — automated checks that invoke [Governance](../../concepts/governance.md) Scenarios to validate artifacts, transitions, and evidence before pipelines proceed.

## What it is

In Foundry, governance is not a stage gate at the end of a pipeline — it is a property of motion. Quality Gates operationalize this principle within CI by embedding governance checkpoints at critical pipeline stages.

A Quality Gate:

1. **Invokes a Governance Scenario** — Executes validation logic (potentially with agents)
2. **Produces a verdict** — Pass, fail, warn, or exception
3. **Controls pipeline flow** — Blocks, allows, or flags depending on verdict and policy
4. **Captures evidence** — Records findings in Evidence Packs for audit

Example gates in a release pipeline:

| Gate | Trigger | Governance Check |
|------|---------|------------------|
| **Code Review** | PR opened | Code reviewer agent reviews diff, checks coverage |
| **Test Coverage** | Tests complete | Coverage threshold enforcement |
| **Security Scan** | Build artifact produced | Vulnerability assessment |
| **License Compliance** | Dependencies resolved | License policy validation |
| **Release Readiness** | Release candidate tagged | Evidence pack completeness |

Quality Gates can be:

| Type | Behavior |
|------|----------|
| **Blocking** | Pipeline fails if gate fails |
| **Advisory** | Pipeline continues with findings attached |
| **Exception-aware** | Allows passage if valid exception/waiver exists |

Gate configuration in Workbench:

```yaml
ci:
  quality_gates:
    - name: pr-review
      agent_enabled: true
      skill: code-reviewer
      blocking: true
      
    - name: test-coverage
      agent_enabled: true
      skill: test-generator
      blocking: true
      threshold: coverage_delta >= 0
      
    - name: security-scan
      agent_enabled: false
      blocking: true
```

Gates produce evidence that flows to Governance:

| Artifact | Purpose |
|----------|---------|
| **Verdict record** | Pass/fail/warn with rationale |
| **Findings** | Specific issues discovered |
| **Evidence pack** | Artifacts proving compliance |
| **Audit entry** | Who/what/when for traceability |

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Release Tools** | Embeds gates in pipelines; executes gate steps |
| **Governance Workspace** | Owns Governance Scenarios that gates invoke |
| **Work Catalogues** | Stores gate Scenarios in `governance/build/` paths |
| **Agent Fabric** | Provides agents for agent-enabled gates |
| **Evidence Repo** | Stores evidence packs produced by gates |

Quality Gates participate in the governance inheritance model:

```
Foundry governance policies
  → Workshop quality requirements
    → Workbench gate configuration
      → Pipeline gate execution
```

Gates can add checks or tighten inherited requirements. They cannot loosen Foundry-level governance policies.

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Governance](../../concepts/governance.md) | Gates invoke Governance Enforcement |
| Governance Enforcement | The orchestration item type gates trigger |
| Build Track | Gates serve Build Track governance needs |
| Evidence | Gates produce evidence for audit |

From ACE: "Every governed transition invokes Governance Enforcement, and may invoke Governance Rituals when human review, cadence, or decision authority is required."

Quality Gates are Governance Enforcement invocations within pipelines. When a gate requires human decision (e.g., exception approval), it may block the pipeline pending ritual completion.

Gate findings flow to governance registers:

| Finding Type | Register |
|--------------|----------|
| Violations | Violation Register |
| Risks discovered | Risk Register |
| Debt created | Debt Register |
| Exceptions granted | Exception Register |

## Related concepts

- [Governance](../../concepts/governance.md) — Platform governance discipline
- [CI Agent Harness](ci-agent-harness.md) — Executes agent-enabled gates
- [CI Delegation Token](ci-delegation-token.md) — Authority for gate agent actions
- [Track](../../concepts/track.md) — Gates serve Build and Governance Tracks

## Further reading

- [../README.md](../README.md) — Release Tools scope including governance
- [../../concepts/governance.md](../../concepts/governance.md) — Full governance model
- [../../ace/governance.md](../../ace/governance.md) — ACE governance architecture
- [../platform-developer-guide/ci-agent-architecture.md](../platform-developer-guide/ci-agent-architecture.md) — Agent-enabled gate implementation
