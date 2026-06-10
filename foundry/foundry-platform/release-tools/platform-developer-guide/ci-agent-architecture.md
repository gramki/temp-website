# CI Agent Architecture

This document specifies how Release Tools spawns agents within CI pipelines, independent of WO Runtime.

> **Key principle:** CI agents operate within Release Tools' domain. They are job-scoped, ephemeral, and pipeline-embedded. They do not share the WO Runtime harness or Jira-polling architecture.

## Separation from WO Runtime

| Aspect | WO Runtime Harness | CI Agent Harness |
|--------|-------------------|------------------|
| **Scope** | Session-scoped (Workspace Session lifetime) | Job-scoped (pipeline step lifetime) |
| **Trigger** | Jira WO assignment + polling | Pipeline trigger (commit, PR, schedule) |
| **Lifecycle** | Long-running daemon + spawned agents | Ephemeral process per pipeline step |
| **Workspace** | Coder-based Workspace Session | CI runner workspace (ephemeral checkout) |
| **State** | Persistent session state, resumable | Stateless between jobs |
| **Owner** | Session owner (human) | Pipeline identity / service account |

### Why Independent?

1. **Different lifecycles** — CI jobs are ephemeral; WO Runtime sessions are persistent
2. **Different triggers** — CI responds to code events; WO Runtime responds to Jira events
3. **Different ownership** — CI runs as pipeline identity; WO Runtime delegates from human session owner
4. **Different guarantees** — CI needs deterministic timing; WO Runtime accommodates human interaction latency

## CI Agent Lifecycle

```
Pipeline Trigger (commit, PR, schedule, manual)
    │
    ├── Pipeline Orchestrator starts job
    │
    ├── CI Agent Step begins
    │   │
    │   ├── Clone/checkout workspace
    │   │
    │   ├── Resolve agent configuration
    │   │   ├── Raw Agent (from Workbench CI config)
    │   │   ├── Skills (from Workbench CI config)
    │   │   └── Model (from Workbench CI config)
    │   │
    │   ├── Fetch Delegation Token
    │   │   └── CI-scoped token (pipeline identity, limited scope)
    │   │
    │   ├── Spawn agent process
    │   │   ├── Inject skills from Agent Fabric
    │   │   ├── Configure MCP connectors (limited set)
    │   │   └── Execute agent task
    │   │
    │   ├── Agent completes
    │   │   └── Exit code + artifacts
    │   │
    │   └── Step ends (agent process terminates)
    │
    └── Pipeline continues (or fails)
```

## Relationship with Agent Fabric

CI agents consume Agent Fabric definitions but bypass WO Runtime:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Agent Fabric                                                                │
│                                                                              │
│  ┌────────────────────┐  ┌────────────────────┐  ┌────────────────────┐    │
│  │  Raw Agents        │  │  Skill Registry    │  │  Access Gateway    │    │
│  │  Registry          │  │                    │  │  (quota, routing)  │    │
│  └─────────┬──────────┘  └─────────┬──────────┘  └─────────┬──────────┘    │
└────────────┼──────────────────────┼──────────────────────────┼──────────────┘
             │                      │                          │
             │ spawn config         │ skill packages           │ model calls
             │                      │                          │
             ▼                      ▼                          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  Release Tools CI                                                            │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  CI Agent Spawner                                                   │    │
│  │                                                                     │    │
│  │  • Reads Workbench CI config for agent settings                    │    │
│  │  • Fetches Raw Agent spawn config from registry                    │    │
│  │  • Fetches skills from Skill Registry                              │    │
│  │  • Requests CI-scoped Delegation Token                             │    │
│  │  • Spawns ephemeral agent process                                  │    │
│  │  • Routes model calls through Access Gateway                       │    │
│  └────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘

Not involved:
┌─────────────────────────────────────────────────────────────────────────────┐
│  WO Runtime                                                                  │
│                                                                              │
│  • No Jira polling                                                          │
│  • No session daemon                                                        │
│  • No task scheduling                                                       │
│  • No human session owner delegation                                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### What Agent Fabric Provides to CI

| Component | CI Usage |
|-----------|----------|
| **Raw Agent Registry** | Spawn configuration for agent processes |
| **Skill Registry** | Skill packages (content, rules, templates) for injection |
| **Access Gateway** | Model routing with quota enforcement |
| **Delegation Token** | CI-scoped token for pipeline identity |

### What Agent Fabric Does NOT Provide to CI

| Component | Why Not |
|-----------|---------|
| **Trained Agent manifests** | CI uses Workbench CI config, not WO-assigned agents |
| **Jira MCP** | CI does not interact with Jira WOs (separate concern) |
| **Session-scoped credentials** | CI uses pipeline identity, not human delegation |

## CI Agent Configuration

CI agent settings are defined in Workbench configuration:

```yaml
# workbench.yaml (excerpt)
ci:
  agent:
    raw_agent: cursor-agent    # Which agent to spawn
    model: claude-sonnet           # Model for CI tasks
    skills:                        # Skills for CI agent
      - code-reviewer
      - test-generator
    timeout: 600                   # Max seconds per agent step
    
  quality_gates:
    - name: pr-review
      agent_enabled: true
      skill: code-reviewer
    - name: test-coverage
      agent_enabled: true
      skill: test-generator
```

## CI Delegation Token

CI agents receive a **CI-scoped Delegation Token** distinct from WO Runtime tokens:

| Property | WO Runtime Token | CI Token |
|----------|------------------|----------|
| **Identity** | Session owner (human) | Pipeline identity |
| **Scope** | Session-scoped tools and models | CI-scoped tools and models |
| **Lifetime** | Session duration | Pipeline job duration |
| **Quota pool** | Session owner's allocation | Workbench CI allocation |
| **Attribution** | Charged to session owner | Charged to Workbench CI budget |

### CI Token Generation

```
Pipeline step starts
    │
    ├── Release Tools CI requests token from Agent Fabric
    │   ├── Workbench ID
    │   ├── Pipeline identity
    │   ├── Job ID
    │   └── Requested scopes (model, limited tools)
    │
    ├── Agent Fabric validates
    │   ├── Pipeline identity authorized for Workbench
    │   ├── CI quota available
    │   └── Requested scopes permitted
    │
    └── Agent Fabric issues CI-scoped token
        ├── Short expiry (job duration)
        ├── Limited scope (no Jira, no user tools)
        └── CI quota attribution
```

## CI Agent Use Cases

### Quality Gate: Code Review

```yaml
pipeline_step:
  name: agent-code-review
  type: foundry-ci-agent
  config:
    skill: code-reviewer
    input:
      diff: ${PR_DIFF}
      context: ${CODEBASE_CONTEXT}
    output:
      review_comments: review.json
    gate:
      fail_on: critical_issues > 0
```

### Quality Gate: Test Generation

```yaml
pipeline_step:
  name: agent-test-generation
  type: foundry-ci-agent
  config:
    skill: test-generator
    input:
      changed_files: ${CHANGED_FILES}
      existing_tests: ${TEST_DIR}
    output:
      generated_tests: generated_tests/
    gate:
      fail_on: coverage_delta < 0
```

### Evidence Collection

```yaml
pipeline_step:
  name: agent-evidence-pack
  type: foundry-ci-agent
  config:
    skill: evidence-collector
    input:
      commit: ${COMMIT_SHA}
      pr: ${PR_NUMBER}
    output:
      evidence_pack: evidence/
```

## Harness Comparison: CI vs WO Runtime

| Harness Aspect | CI Agent | WO Runtime Agent |
|----------------|----------|------------------|
| **Environment** | CI runner env vars | Workspace Session env vars |
| **MCP connectors** | Limited (GitHub, build tools) | Full (Jira, GitHub, Foundry) |
| **Skills** | CI-specific subset | Full skill set per manifest |
| **Knowledge** | Limited (repo context) | Full hierarchy (Foundry → WO) |
| **Delegation Token** | CI-scoped | Session-scoped |
| **Model routing** | Same Access Gateway | Same Access Gateway |

### Shared Infrastructure

Both CI and WO Runtime agents share:

- **Raw Agent Registry** — Same spawn configurations
- **Skill Registry** — Same skill packages (but CI uses subset)
- **Access Gateway** — Same model routing and quota enforcement
- **Delegation Token format** — Same format, different scopes

### Independent Infrastructure

CI agents have dedicated:

- **CI Spawner** — Release Tools owns spawning, not WO Runtime daemon
- **CI quota pool** — Workbench CI budget, separate from session owner budgets
- **CI pipelines** — Trigger and lifecycle managed by CI orchestrator

## Implementation Notes

### Why Not Reuse WO Runtime Harness?

1. **No daemon needed** — CI steps are ephemeral; WO Runtime daemon adds overhead
2. **No Jira polling** — CI triggers are code events, not Jira state changes
3. **Simpler lifecycle** — CI: spawn → execute → exit; WO Runtime: spawn → poll → execute → monitor → report
4. **Different identity model** — CI runs as pipeline; WO Runtime runs as human delegate

### Shared Code Opportunities

Despite architectural separation, implementation can share:

- Skill installation logic (fetch from registry, install to workspace)
- Delegation Token request/validation
- Access Gateway client
- Agent spawn configuration parsing

## Read Next

- [ci/README.md](ci/README.md) — CI module overview
- [../agent-fabric/platform-developer-guide/raw-agents.md](../../agent-fabric/platform-developer-guide/raw-agents.md) — Raw Agent registry
- [../agent-fabric/platform-developer-guide/skill-registry.md](../../agent-fabric/platform-developer-guide/skill-registry.md) — Skill Registry
- [../work-order-runtime/platform-developer-guide/agent-spawning.md](../../work-order-runtime/platform-developer-guide/agent-spawning.md) — WO Runtime spawning (for comparison)
