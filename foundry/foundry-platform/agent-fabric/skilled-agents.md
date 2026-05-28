# Skilled Agents

Skilled Agents are **local manifests** that combine Capable Agents with Skills and Guardrails for a particular (Workspace Type, Scenario) context.

## Key Distinction: Manifests vs Packages

| Concept | What It Is | Where It Lives |
|---------|------------|----------------|
| **Skill** | Reusable capability package | [Skill Registry](skill-registry.md) (published) |
| **Skilled Agent** | Manifest referencing skills | Workshop/Workbench repo (local) |

**Skills are packages; Skilled Agents are manifests.** This is analogous to:
- Skills = npm packages
- Skilled Agent = `package.json` (declares which packages to use)

## Definition

A **Skilled Agent** manifest specifies:

- **Compatible Capable Agents** — Which agent systems and models can execute
- **Skills** — References to published skill packages (name + version)
- **Guardrails** — Constraints on agent behavior
- **Evaluation** — Metrics for assessing agent performance

Skilled Agents represent the "persona" — what an agent *should* do for a specific context.

## Scope

Skilled Agents are defined per:

- **Workspace Type** — Product Specification, UX Design, Development, QA, Release, Governance
- **Scenario** — A specific type of work (e.g., `implement-feature`, `code-review`, `write-tests`)

## Folder Structure

Skilled Agents are defined within Scenarios in the Workshop Definition Repository:

```
workspaces/
└── development/
    └── scenarios/
        └── implement-feature/
            ├── scenario.yaml           # Scenario definition
            └── skilled-agent/          # Skilled Agent for this scenario
                ├── agent.yaml          # Manifest (references skills from registry)
                ├── guardrails/         # Guardrail definitions (optional overrides)
                │   └── custom-rules.yaml
                └── eval/               # Evaluation data (optional)
                    └── golden-dataset.jsonl
```

**Note:** Skills are NOT stored in the repository. Skills are fetched from the [Skill Registry](skill-registry.md) at Workspace Session start. The `agent.yaml` manifest references skills by name and version.

Skilled Agents follow the same inheritance model as other workspace content:

- **Workshop level** (`workspaces/{workspace}/scenarios/{scenario}/skilled-agent/`) — Base definition
- **Workbench level** (`workbenches/{product-code}/workspaces/{workspace}/scenarios/{scenario}/skilled-agent/`) — Override

## Agent Definition Schema

### agent.yaml

```yaml
name: feature-implementation-agent
description: Implements features based on specifications and designs

compatible-capable-agents:
  - agent: cursor-agent
    models:
      - claude-opus      # 1st preference
      - claude-sonnet    # 2nd preference (fallback)
  - agent: copilot
    models:
      - gpt-5-thinking   # 3rd preference
      - gpt-5            # 4th preference

skills:
  - name: code-generator
    version: ^2.1.0
    registry: foundry           # or 'global'
  - name: test-writer
    version: ~1.5.0
    registry: global
  - name: documentation-updater
    version: latest

guardrails:
  - no-force-push
  - require-tests-for-new-code
  - max-file-changes: 50
  - no-modification-outside-scope

evaluation:
  metrics:
    - code-quality-score
    - test-coverage-delta
    - review-approval-rate
  golden-datasets:
    - eval/implementation-cases/
```

### Schema Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | Unique identifier for this skilled agent |
| `description` | string | Human-readable description |
| `compatible-capable-agents` | list | Capable agents and models (in fallback order) |
| `compatible-capable-agents[].agent` | string | Capable agent identifier |
| `compatible-capable-agents[].models` | list | Supported models (in preference order) |
| `skills` | list | Skill references (name + version + registry) |
| `skills[].name` | string | Skill package name |
| `skills[].version` | string | Version constraint (semver) |
| `skills[].registry` | string | `foundry` (default) or `global` |
| `guardrails` | list | Behavioral constraints |
| `evaluation.metrics` | list | Metrics to track |
| `evaluation.golden-datasets` | list | Paths to evaluation data |

## Skills

Skills are published packages fetched from the [Skill Registry](skill-registry.md). The Skilled Agent manifest references skills by name and version:

```yaml
skills:
  - name: code-generator
    version: ^2.1.0         # Semver constraint
    registry: foundry       # foundry (private) or global (public)
```

### Version Resolution

| Constraint | Meaning |
|------------|---------|
| `2.1.3` | Exact version |
| `^2.1.0` | Compatible (≥2.1.0, <3.0.0) |
| `~2.1.0` | Patch only (≥2.1.0, <2.2.0) |
| `latest` | Latest published |

At task start, WO Runtime resolves version constraints and records the resolved versions in task metadata. See [skill-registry.md](skill-registry.md) for full details on skill packaging and publishing.

### Skill Installation

Skills are installed to the Workspace Session at session start:

1. WO Runtime collects skill references from all enabled Skilled Agents
2. Resolves versions against Foundry then Global registry
3. Downloads to `~/.foundry/skills/{skill}@{version}/`
4. Sets `FOUNDRY_SKILLS_PATH` environment variable

## Guardrails

Guardrails constrain agent behavior for safety and compliance.

### Guardrail Types

| Type | Example | Enforcement |
|------|---------|-------------|
| **Prohibition** | `no-force-push` | Blocks specific actions |
| **Requirement** | `require-tests-for-new-code` | Requires certain outputs |
| **Limit** | `max-file-changes: 50` | Caps resource usage |
| **Scope** | `no-modification-outside-scope` | Restricts operational area |

### Guardrail Definition

```yaml
guardrails:
  - name: no-force-push
    type: prohibition
    description: Never use git push --force
    
  - name: require-tests-for-new-code
    type: requirement
    description: All new code must have corresponding tests
    
  - name: max-file-changes
    type: limit
    value: 50
    description: Maximum files that can be modified in one task
    
  - name: no-modification-outside-scope
    type: scope
    description: Only modify files related to the assigned work
```

## Evaluation

Skilled Agents can be evaluated using defined metrics and golden datasets.

### Evaluation Metrics

| Metric | Description |
|--------|-------------|
| `code-quality-score` | Static analysis score of generated code |
| `test-coverage-delta` | Change in test coverage |
| `review-approval-rate` | Percentage of PRs approved without changes |
| `time-to-completion` | Average time to complete tasks |
| `false-positive-rate` | Incorrect outputs flagged by evaluation |

### Golden Datasets

Golden datasets provide reference inputs and expected outputs for evaluation:

```
eval/
└── implementation-cases/
    ├── case-001.jsonl    # Input: spec, Expected: implementation
    ├── case-002.jsonl
    └── ...
```

## Skilled Agent Selection

When WO Runtime processes a task:

1. Read the Scenario definition
2. Check if Scenario has a `skilled-agent/` folder
3. If yes, load `agent.yaml`
4. Select Capable Agent from `compatible-capable-agents` based on:
   - Availability (is this agent enabled in the Workbench?)
   - User preference (if configured)
   - First available in list (default)
5. Select Model based on preference order
6. Create Employed Agent with selected configuration

## Scenarios Without Skilled Agents

If a Scenario does not have a `skilled-agent/` folder:

- The task is queued for human completion
- Task appears in the Workspace Console and IDE Work Orders Panel
- Session owner picks up and completes the task manually

## Read Next

- [skill-registry.md](skill-registry.md) — Skill packaging, publishing, and CLI tooling
- [capable-agents.md](capable-agents.md) — What Capable Agents are available
- [employed-agents.md](employed-agents.md) — How Skilled Agents become Employed Agents
- [../work-order-runtime/agent-spawning.md](../work-order-runtime/agent-spawning.md) — How agents are spawned with skills
- [../management/workshop-repository.md](../management/workshop-repository.md) — Where Skilled Agents are stored
