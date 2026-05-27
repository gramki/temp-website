# Skilled Agents

Skilled Agents are agent definitions that combine a Capable Agent with specific Skills, Guardrails, and Evaluation criteria for a particular (Workspace Type, Scenario) context.

## Definition

A **Skilled Agent** is an agent definition that specifies:

- **Compatible Capable Agents** — Which agent systems and models can execute this definition
- **Skills** — Skill packages that define what the agent can do
- **Guardrails** — Constraints on agent behavior
- **Evaluation** — Metrics and criteria for assessing agent performance

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
                ├── agent.yaml          # Agent definition
                └── skills/             # Skills this agent uses
                    ├── code-generator/
                    │   ├── SKILL.md
                    │   └── ...
                    └── test-writer/
                        ├── SKILL.md
                        └── ...
```

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
      - claude-opus      # Primary - best for complex implementation
      - claude-sonnet    # Fallback - faster, cheaper
  - agent: copilot
    models:
      - gpt-5-thinking   # For deep analysis
      - gpt-5            # For quick implementation

skills:
  - code-generator
  - test-writer
  - documentation-updater

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
| `compatible-capable-agents` | list | Capable agents and models that can run this |
| `compatible-capable-agents[].agent` | string | Capable agent identifier |
| `compatible-capable-agents[].models` | list | Supported models (in preference order) |
| `skills` | list | Skill package names to include |
| `guardrails` | list | Behavioral constraints |
| `evaluation.metrics` | list | Metrics to track |
| `evaluation.golden-datasets` | list | Paths to evaluation data |

## Skills

Skills are reusable packages that define agent capabilities. Each skill is a folder containing:

```
skills/
└── code-generator/
    ├── SKILL.md                    # Main definition (YAML frontmatter + instructions)
    ├── rules/                      # Rule files referenced by SKILL.md
    │   ├── coding-standards.md
    │   └── security-rules.md
    ├── templates/                  # Output templates
    │   └── commit-message.md
    ├── examples/                   # Few-shot examples
    │   ├── good-implementation.md
    │   └── bad-implementation.md
    └── eval/                       # Evaluation harness
        ├── golden-dataset.jsonl
        └── eval-config.yaml
```

### SKILL.md Format

Skills follow the [Agent Skills specification](https://agentic.ai/):

```yaml
---
name: code-generator
description: Generate production-quality code from specifications
---

# Code Generator

## Role

You are a code generation agent that implements features based on specifications.

## Workflow

1. Analyze the specification
2. Identify affected files
3. Generate implementation
4. Generate tests
5. Update documentation

## Rules

See [rules/coding-standards.md](rules/coding-standards.md) for coding standards.

## Task Creation

When breaking down work, use the task creation tool:

```
create_task(
  title="Implement {component}",
  scenario="implement-component",
  parent_task=current_task,
  dependencies=[...]
)
```
```

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

- [capable-agents.md](capable-agents.md) — What Capable Agents are available
- [employed-agents.md](employed-agents.md) — How Skilled Agents become Employed Agents
- [../work-order-runtime/agent-spawning.md](../work-order-runtime/agent-spawning.md) — How agents are spawned with skills
- [../management/workshop-repository.md](../management/workshop-repository.md) — Where Skilled Agents are stored
