# CI Agent Harness

The CI Agent Harness is the job-scoped, ephemeral agent execution environment within Release Tools CI pipelines — distinct from the WO Runtime harness used for Work Order execution.

## What it is

When agents execute in CI pipelines, they need a harness that matches CI semantics: ephemeral, stateless, triggered by code events. The CI Agent Harness provides this without the overhead of WO Runtime's long-running daemon and Jira polling architecture.

Key characteristics:

| Aspect | CI Agent Harness | WO Runtime Harness |
|--------|------------------|-------------------|
| **Scope** | Job-scoped (pipeline step lifetime) | Session-scoped (Workspace Session lifetime) |
| **Trigger** | Pipeline events (commit, PR, schedule) | Jira WO assignment + polling |
| **Lifecycle** | Spawn → execute → exit | Spawn → poll → execute → monitor → report |
| **Workspace** | CI runner workspace (ephemeral checkout) | Coder-based Workspace Session |
| **State** | Stateless between jobs | Persistent session state, resumable |
| **Owner** | Pipeline identity / service account | Session owner (human) |

The CI Agent Harness lifecycle:

```
Pipeline step starts
    │
    ├── Clone/checkout workspace
    │
    ├── Resolve agent configuration
    │   ├── Raw Agent (from Workbench CI config)
    │   ├── Skills (from Workbench CI config)
    │   └── Model (from Workbench CI config)
    │
    ├── Fetch CI Delegation Token
    │   └── Pipeline-scoped, limited scope
    │
    ├── Spawn agent process
    │   ├── Inject skills from Agent Fabric
    │   ├── Configure MCP connectors (limited set)
    │   └── Execute agent task
    │
    ├── Agent completes
    │   └── Exit code + artifacts
    │
    └── Step ends (agent process terminates)
```

The harness consumes Agent Fabric components but bypasses WO Runtime entirely:

| Agent Fabric Component | CI Usage |
|------------------------|----------|
| **Raw Agent Registry** | Spawn configuration for agent processes |
| **Skill Registry** | Skill packages for injection (CI-appropriate subset) |
| **Access Gateway** | Model routing with quota enforcement |
| **Delegation Token Service** | CI-scoped tokens for pipeline identity |

What the harness does **not** use:

| Component | Why Not |
|-----------|---------|
| WO Runtime daemon | CI steps are ephemeral; daemon overhead unnecessary |
| Jira polling | CI triggers are code events, not Jira state changes |
| Session-scoped credentials | CI uses pipeline identity, not human delegation |
| Full MCP connector set | CI has limited integration surface |

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Release Tools** | Owns the CI Agent Harness; spawns and manages CI agents |
| **Agent Fabric** | Provides registries and gateway consumed by harness |
| **WO Runtime** | Not involved — independent lifecycle |
| **Workbench config** | Defines CI agent settings (raw agent, skills, model) |

CI agent configuration in Workbench:

```yaml
ci:
  agent:
    raw_agent: cursor-agent
    model: claude-sonnet
    skills:
      - code-reviewer
      - test-generator
    timeout: 600
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Agent Model](../../concepts/agent-model.md) | CI spawns Raw Agents with injected Skills |
| Build Track | CI pipelines serve the Build Track |
| [Release Workspace](../../ace/workspaces/release.md) | CI executes in Release context |

The CI Agent Harness is an operational detail, not an ACE concept. ACE defines the Agent Model and Workspace types; Foundry Platform implements multiple harnesses for different execution contexts.

## Related concepts

- [CI Delegation Token](ci-delegation-token.md) — Authority tokens for CI agents
- [Quality Gates](quality-gates.md) — Governance checkpoints that may use agents
- [Agent Model](../../concepts/agent-model.md) — Platform-wide agent architecture
- [Workspace Session](../../concepts/workspace-session.md) — WO Runtime's harness (contrast)
- [Delegation](../../concepts/delegation.md) — Authority transfer pattern CI adapts

## Further reading

- [../platform-developer-guide/ci-agent-architecture.md](../platform-developer-guide/ci-agent-architecture.md) — Full harness specification
- [../../agent-fabric/README.md](../../agent-fabric/README.md) — Agent Fabric components
- [../../work-order-runtime/platform-developer-guide/agent-spawning.md](../../work-order-runtime/platform-developer-guide/agent-spawning.md) — WO Runtime harness (for comparison)
