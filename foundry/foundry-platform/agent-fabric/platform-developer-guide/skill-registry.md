# Skill Registry

The Skill Registry is a two-tier package distribution system for agent skills.

## Overview

Skills are reusable capability packages that follow the [Agent Skills specification](https://agentic.ai/). They are published to registries and referenced by Skilled Agent manifests.

```
┌─────────────────────────────────────────────────────────────────┐
│  Global Skill Registry (public, cross-Foundry)                  │
│  - Community skills                                             │
│  - Vendor-provided skills                                       │
│  - Open source skills                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ pull / fork
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Foundry Skill Registry (private, org-scoped)                   │
│  - Internal skills                                              │
│  - Forked/modified community skills                             │
│  - Proprietary skills                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ reference (name + version)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Skilled Agent Manifest (in Workshop/Workbench repo)            │
│  agent.yaml:                                                    │
│    skills:                                                      │
│      - name: code-generator                                     │
│        version: ^2.1.0                                          │
│        registry: foundry                                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ install at session start
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Workspace Session                                              │
│  ~/.foundry/skills/code-generator@2.1.3/                        │
└─────────────────────────────────────────────────────────────────┘
```

## Two-Tier Registry

### Global Registry

| Aspect | Detail |
|--------|--------|
| **Scope** | Public, accessible by all Foundries |
| **Contents** | Community skills, vendor skills, open source |
| **Publishing** | Open (with review) or vendor accounts |
| **Namespacing** | `@vendor/skill-name` or `skill-name` |

### Foundry Registry

| Aspect | Detail |
|--------|--------|
| **Scope** | Private, accessible only within one Foundry |
| **Contents** | Internal skills, forked skills, proprietary |
| **Publishing** | Foundry members with publish permissions |
| **Namespacing** | `skill-name` (no vendor prefix needed) |

### Resolution Order

When a Skilled Agent references a skill:

```
1. Check Foundry registry for exact name
2. If not found, check Global registry
3. If version constraint specified, resolve to matching version
4. Download and cache in Foundry registry (for global skills)
```

## Skill Package Format

A skill package contains:

```
skill-name/
├── SKILL.md              # Main definition (YAML frontmatter + instructions)
├── package.yaml          # Package metadata (name, version, dependencies)
├── rules/                # Rule files referenced by SKILL.md
│   └── *.md
├── templates/            # Output templates
│   └── *.md
├── examples/             # Few-shot examples
│   └── *.md
├── tools/                # Skill-specific MCP tools (optional)
│   └── *.py
└── eval/                 # Evaluation harness (optional)
    ├── golden-dataset.jsonl
    └── eval-config.yaml
```

### package.yaml

```yaml
name: code-generator
version: 2.1.3
description: Generate production-quality code from specifications
author: platform-team
license: MIT

keywords:
  - code-generation
  - implementation
  - development

dependencies:
  - name: test-writer
    version: ^1.5.0

compatible-capable-agents:
  - cursor-agent
  - copilot
  - claude-code

min-foundry-version: 1.2.0
```

## CLI Tooling

All skill operations are available as `gh` (GitHub CLI) extensions.

### Installation

```bash
gh extension install foundry/gh-foundry-skill
```

### Commands

#### Initialize a new skill

```bash
gh foundry-skill init my-skill
# Creates scaffold with SKILL.md, package.yaml, etc.
```

#### Build and validate

```bash
gh foundry-skill build
# Validates SKILL.md format, checks dependencies, lints
```

#### Run evaluation

```bash
gh foundry-skill test
# Runs evaluation harness against golden dataset
# Reports accuracy, coverage metrics
```

#### Package for distribution

```bash
gh foundry-skill package
# Creates my-skill-2.1.3.tar.gz
```

#### Publish to registry

```bash
# Publish to Foundry registry (default)
gh foundry-skill publish

# Publish to Global registry
gh foundry-skill publish --registry global
```

#### Install to workspace

```bash
# Install specific version
gh foundry-skill install code-generator@2.1.3

# Install from Skilled Agent manifest
gh foundry-skill install --from agent.yaml
```

#### Search and list

```bash
# Search across registries
gh foundry-skill search "code generation"

# List installed skills
gh foundry-skill list --installed

# List available versions
gh foundry-skill list code-generator --versions
```

## Version Resolution

Skills use semantic versioning. Skilled Agents can specify version constraints:

| Constraint | Meaning |
|------------|---------|
| `2.1.3` | Exact version |
| `^2.1.0` | Compatible with 2.1.0 (≥2.1.0, <3.0.0) |
| `~2.1.0` | Approximately 2.1.0 (≥2.1.0, <2.2.0) |
| `>=2.0.0` | At least 2.0.0 |
| `latest` | Latest published version |

### Version Pinning at Runtime

When WO Runtime starts a task:

1. Read Skilled Agent manifest
2. Resolve skill versions from constraints
3. Record resolved versions in WO/task metadata
4. Install resolved versions to Workspace Session
5. Task executes with pinned versions

If skill versions change mid-WO, earlier tasks use their pinned versions; new tasks use newly resolved versions.

## Installation to Workspace

At Workspace Session start:

```
1. WO Runtime reads Skilled Agent manifests for enabled Scenarios
2. Collects all skill references (name + version constraints)
3. Resolves versions against registries
4. Downloads skills not in local cache
5. Installs to ~/.foundry/skills/{skill}@{version}/
6. Sets FOUNDRY_SKILLS_PATH environment variable
```

Skills are installed once per session, not per task.

## Publishing Workflow

### Internal Skill (Foundry Registry)

```bash
# 1. Develop skill
gh foundry-skill init my-internal-skill
# ... edit SKILL.md, add rules, templates ...

# 2. Test locally
gh foundry-skill test

# 3. Build and validate
gh foundry-skill build

# 4. Publish to Foundry registry
gh foundry-skill publish
# Published my-internal-skill@1.0.0 to foundry registry
```

### Community Skill (Global Registry)

```bash
# 1. Fork or create skill
gh foundry-skill init my-community-skill

# 2. Develop with comprehensive evaluation
gh foundry-skill test --coverage

# 3. Submit for review
gh foundry-skill publish --registry global --submit-review
# Submitted for review. Track at: https://skills.foundry.dev/reviews/12345

# 4. After approval, skill is publicly available
```

## Skill Discovery

### Catalog View

The Skill Registry provides a browsable catalog:

- **By category** — Code generation, testing, documentation, review
- **By capable agent** — Skills compatible with Cursor, Copilot, etc.
- **By workspace** — Skills for Development, QA, Release workspaces
- **By popularity** — Download counts, ratings

### Automation Gap Analysis

Compare Scenarios to available skills:

```bash
gh foundry-skill coverage --workshop workshop-abc
# Scenarios without Skilled Agents:
#   development/manual-deployment (no matching skill)
#   qa/exploratory-testing (no matching skill)
# 
# Suggested skills:
#   deployment-automator (global) - 85% match for manual-deployment
```

## Security

### Skill Signing (Future)

- Publishers sign packages with GPG keys
- Foundry verifies signatures before installation
- Unsigned skills require explicit approval

### Dependency Scanning

- Skills declaring dependencies are scanned for vulnerabilities
- Deprecated dependencies flagged at publish time
- Security advisories propagated to dependent skills

### Sandbox Execution

- Skills run in Workspace Session sandbox
- MCP tools are capability-restricted
- File system access scoped to workspace

## Read Next

- [skilled-agents.md](skilled-agents.md) — How Skilled Agents reference skills
- [capable-agents.md](capable-agents.md) — Compatible capable agent configuration
- [../work-order-runtime/platform-developer-guide/agent-spawning.md](..//work-order-runtime/platform-developer-guide/agent-spawning.md) — Skill installation at runtime
