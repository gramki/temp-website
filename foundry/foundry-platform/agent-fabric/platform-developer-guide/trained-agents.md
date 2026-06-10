# Trained Agents

## Overview

Trained Agents are declarative manifests that bind Raw Agents to Swarms with configured skills, guardrails, and identity. This specification covers the manifest schema, Swarm membership, identity model, and runtime resolution logic.

For conceptual background, see the [user guide: Trained Agents](../user-guide/trained-agents.md).

## ACE alignment

| ACE concept | Realization in this spec |
|-------------|-------------------------|
| [Agent](../../ace/concepts.md) | Trained Agent manifests configure how abstract agent capabilities are applied |
| [Skill](../../ace/concepts.md) | Skills referenced by name and version from the Skill Registry |
| [Guardrail](../../ace/concepts.md) | Behavioral constraints defined per Trained Agent |

## Folder Structure

Trained Agents are defined within Swarms in the `swarms/` directory at each scope:

```
swarms/
└── build-swarm/
    ├── swarm.yaml                    # Swarm definition
    └── trained-agents/
        ├── feature-implementer.yaml  # Trained Agent manifest
        ├── code-refactorer.yaml
        └── test-writer.yaml
```

Swarms live in a dedicated `swarms/` folder at each scope, separate from the Work Catalog:

```
# Foundry-level
foundry-{id}/
├── work-catalog/
└── swarms/
    └── build-swarm/
        ├── swarm.yaml
        └── trained-agents/

# Workshop-level
workshop-{id}/
├── work-catalog/
└── swarms/

# Workbench-level
workbench-{id}/
├── work-catalog/
└── swarms/

# Workspace-level
workbench-{id}/
└── workspaces/
    └── {workspace-type}/
        └── swarms/
```

## Trained Agent Manifest Schema

### Full Example

```yaml
name: feature-implementer
description: Implements features based on specifications and designs
swarm: build-swarm
raw-agent-ref: registry.foundry.io/raw-agents/codex:v2.4.1

identity:
  jid: feature-implementer@build-swarm.agents.acme.foundry.io

skills:
  - name: code-generator
    version: ^2.1.0
    registry: foundry
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
| `name` | string | Unique identifier within the Swarm |
| `description` | string | Human-readable description |
| `swarm` | string | Swarm this agent belongs to (exactly one) |
| `raw-agent-ref` | string | Raw Agent OCI URI with version (see [raw-agents.md](raw-agents.md)) |
| `identity.jid` | string | Service Principal JID (see Identity Model) |
| `skills` | list | Skill references (name + version + registry) |
| `skills[].name` | string | Skill package name |
| `skills[].version` | string | Version constraint (semver) |
| `skills[].registry` | string | `foundry` (default) or `global` |
| `guardrails` | list | Behavioral constraints (see below) |
| `evaluation.metrics` | list | Metrics to track |
| `evaluation.golden-datasets` | list | Paths to evaluation data |

## Identity Model

Each Trained Agent has a Service Principal identity using Jabber JID notation:

```
{agent}@{swarm}.agents.{tenant}.foundry.io
```

| Component | Example | Description |
|-----------|---------|-------------|
| `{agent}` | `feature-implementer` | Agent name (unique within Swarm) |
| `{swarm}` | `build-swarm` | Swarm the agent belongs to |
| `{tenant}` | `acme` | Tenant organization |
| Full JID | `feature-implementer@build-swarm.agents.acme.foundry.io` | Complete identity |

The JID serves as:

- **Service Principal** — IAM identity for the agent in the management plane
- **Addressing** — Unique identifier for inter-agent communication
- **Audit trail** — Immutable identity for attribution and compliance

When a Trained Agent is employed (instantiated at runtime), the JID is paired with a Delegation Token to form the Employed Agent's runtime identity. See [employed-agents.md](employed-agents.md) for the delegation model.

## Raw Agent Reference

The `raw-agent-ref` field specifies which OCI-packaged agent system to use:

```yaml
raw-agent-ref: registry.foundry.io/raw-agents/codex:v2.4.1
```

| Registry | URI Pattern | Source |
|----------|-------------|--------|
| Platform | `registry.foundry.io/raw-agents/{agent}:{version}` | Platform-shipped |
| Tenant | `registry.{tenant}.foundry.io/raw-agents/{agent}:{version}` | Tenant-added |

See [raw-agents.md](raw-agents.md) for available agent identifiers and [raw-agent-registry.md](raw-agent-registry.md) for the registry API.

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

1. WO Runtime collects skill references from Trained Agents in referenced Swarms
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

Trained Agents can be evaluated using defined metrics and golden datasets.

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

## Runtime Resolution

When WO Runtime processes a task:

1. Read the Scenario definition and its referenced Swarms
2. Identify the coordinator agent (`{swarm}/{agent}` notation)
3. Load the Trained Agent manifest from `swarms/{swarm}/trained-agents/{agent}.yaml`
4. Resolve the Raw Agent from `raw-agent-ref`
5. Check Raw Agent availability and credentials
6. Create [Employed Agent](employed-agents.md) with JID + Delegation Token

## Related documentation

- [Platform developer guide index](README.md)
- [Raw Agents](raw-agents.md) — available OCI-packaged agent systems
- [Raw Agent Registry](raw-agent-registry.md) — registry API and discovery
- [Swarm Registry](swarm-registry.md) — Swarm management and hierarchy
- [Skill Registry](skill-registry.md) — skill packaging, publishing, and CLI
- [Employed Agents](employed-agents.md) — how Trained Agents become running instances
- [Agent Fabric concepts](../README.md) — module boundaries and architecture
