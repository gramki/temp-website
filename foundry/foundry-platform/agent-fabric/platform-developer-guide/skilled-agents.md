# Skilled Agents

## Overview

Skilled Agents are declarative manifests that bind Capable Agents to specific (Workspace Type, Scenario) contexts with configured skills and guardrails. This specification covers the folder structure, `agent.yaml` schema, inheritance model, and runtime selection logic.

For conceptual background, see the [user guide: Skilled Agents](../user-guide/skilled-agents.md).

## ACE alignment

| ACE concept | Realization in this spec |
|-------------|-------------------------|
| [Agent](../../ace/concepts.md) | Skilled Agent manifests configure how abstract agent capabilities are applied |
| [Skill](../../ace/concepts.md) | Skills referenced by name and version from the Skill Registry |
| [Guardrail](../../ace/concepts.md) | Behavioral constraints defined per Skilled Agent |

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

**Note:** Skills are NOT stored in the repository. Skills are fetched from the [Skill Registry](skill-registry.md) at Workspace Session start.

## Inheritance Model

Skilled Agents follow the Workshop → Workbench inheritance model:

| Level | Path | Purpose |
|-------|------|---------|
| **Workshop** | `workspaces/{workspace}/scenarios/{scenario}/skilled-agent/` | Base definition |
| **Workbench** | `workbenches/{product-code}/workspaces/{workspace}/scenarios/{scenario}/skilled-agent/` | Override |

Workbench-level definitions override Workshop-level definitions entirely (no merge).

## agent.yaml Schema

### Full Example

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

### Schema Reference

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | Unique identifier for this skilled agent |
| `description` | string | Human-readable description |
| `compatible-capable-agents` | list | Capable agents and models (in fallback order) |
| `compatible-capable-agents[].agent` | string | Capable agent identifier (see [capable-agents.md](capable-agents.md)) |
| `compatible-capable-agents[].models` | list | Supported models (in preference order) |
| `skills` | list | Skill references (name + version + registry) |
| `skills[].name` | string | Skill package name |
| `skills[].version` | string | Version constraint (semver) |
| `skills[].registry` | string | `foundry` (default) or `global` |
| `guardrails` | list | Behavioral constraints (see below) |
| `evaluation.metrics` | list | Metrics to track |
| `evaluation.golden-datasets` | list | Paths to evaluation data |

## Compatible Capable Agents

The `compatible-capable-agents` list defines which agent systems can execute this Skilled Agent. Order matters—agents are selected by preference.

```yaml
compatible-capable-agents:
  - agent: cursor-agent
    models:
      - claude-opus      # 1st preference
      - claude-sonnet    # Fallback
  - agent: copilot
    models:
      - gpt-5-thinking
```

See [capable-agents.md](capable-agents.md) for available agent identifiers.

## Skills References

Skills are published packages fetched from the [Skill Registry](skill-registry.md). The manifest references skills by name and version:

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

At task start, WO Runtime resolves version constraints and records the resolved versions in task metadata.

### Skill Installation

Skills are installed to the Workspace Session at session start:

1. WO Runtime collects skill references from all enabled Skilled Agents
2. Resolves versions against Foundry then Global registry
3. Downloads to `~/.foundry/skills/{skill}@{version}/`
4. Sets `FOUNDRY_SKILLS_PATH` environment variable

See [skill-registry.md](skill-registry.md) for skill packaging and publishing.

## Guardrails Schema

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

Golden datasets provide reference inputs and expected outputs:

```
eval/
└── implementation-cases/
    ├── case-001.jsonl    # Input: spec, Expected: implementation
    ├── case-002.jsonl
    └── ...
```

## Runtime Selection

When WO Runtime processes a task:

1. Read the Scenario definition
2. Check if Scenario has a `skilled-agent/` folder
3. If yes, load `agent.yaml`
4. Select Capable Agent from `compatible-capable-agents` based on:
   - Availability (is this agent enabled in the Workbench?)
   - User preference (if configured)
   - First available in list (default)
5. Select Model based on preference order
6. Create [Employed Agent](employed-agents.md) with selected configuration

## Related documentation

- [Platform developer guide index](README.md)
- [Capable Agents](capable-agents.md) — available agent systems
- [Skill Registry](skill-registry.md) — skill packaging, publishing, and CLI
- [Employed Agents](employed-agents.md) — how Skilled Agents become running instances
- [Agent Fabric concepts](../README.md) — module boundaries and architecture
- [Workshop Repository](../../management/platform-developer-guide/workshop-repository.md) — where Skilled Agents are stored
