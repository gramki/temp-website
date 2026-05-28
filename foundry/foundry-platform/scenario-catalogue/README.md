# Scenario Catalogue

**Content type:** Reference scenario definitions — templates and examples organized by (Track, Workspace).

> **Note:** This is a **content folder**, not a platform module. The module that manages scenarios (schema, validation, storage) is [Scenario Management](../management/scenario-management/README.md), a subsystem of the Management module.

## What This Folder Contains

This folder contains **reference scenario definitions** that serve as:

- **Templates** — Starting points for Workshops defining their scenarios
- **Examples** — Illustrations of how to define scenarios for each Track/Workspace
- **Best practices** — Recommended patterns for common work types

These scenarios are not directly executed. They must be deployed to a Workshop Definition Repository to become active.

## Relationship to Scenario Management

| Concern | Owner |
|---------|-------|
| **Schema definition** | [Scenario Management](../management/scenario-management/README.md) |
| **Validation rules** | [Scenario Management](../management/scenario-management/README.md) |
| **Agent recommendations** | [Scenario Management](../management/scenario-management/README.md) |
| **Reference definitions (templates)** | **This folder** |
| **Runtime scenario storage** | Metadata Service (synced from Workshop repos) |
| **Scenario execution** | WO Runtime |

## Folder Structure

Scenarios are organized by **(Track, Workspace)** pairs:

```
scenario-catalogue/
├── discovery/           # Discovery Track
│   ├── product-specification/
│   ├── ux-design/
│   ├── development/
│   ├── qa/
│   ├── release/
│   └── governance/
├── build/               # Build Track
│   └── ...
├── run/                 # Run Track (out of Phase 1)
│   └── ...
├── win/                 # Win Track (out of Phase 1)
│   └── ...
├── evolve/              # Evolve Track (out of Phase 1)
│   └── ...
└── governance/          # Governance Track
    └── ...
```

### Track Folders

| Track | Folder | Phase 1? | Description |
|-------|--------|----------|-------------|
| Discovery | [discovery/](discovery/README.md) | Yes | Scenarios for exploring opportunities |
| Build | [build/](build/README.md) | Yes | Scenarios for building and releasing |
| Run | [run/](run/README.md) | No | Scenarios for operating products |
| Win | [win/](win/README.md) | No | Scenarios for market success |
| Evolve | [evolve/](evolve/README.md) | No | Scenarios for process improvement |
| Governance | [governance/](governance/README.md) | Yes | Governance scenarios at gates |

## Using This Catalogue

### For Workshop Admins

1. Browse the catalogue to find relevant scenarios
2. Copy scenario definitions to your Workshop Definition Repo
3. Customize as needed for your Workshop/Workbench
4. Scenarios become active after PR merge and sync

### For Foundry Admins

1. Maintain the catalogue with new scenario templates
2. Update scenarios following schema changes
3. Deprecate outdated scenarios with migration notes

### For Platform Developers

1. Use these scenarios to test Scenario Management validation
2. Reference examples when implementing new features
3. Ensure schema changes are reflected in catalogue examples

## Scenario Definition Format

Scenarios follow the schema defined in [Scenario Management](../management/scenario-management/scenario-schema.md):

```yaml
apiVersion: foundry/v1
kind: Scenario
metadata:
  name: <scenario-name>
  workspace: <workspace-type>
spec:
  description: <description>
  triggers:
    - <trigger-type>
  inputs:
    - <input-definition>
  outputs:
    - <output-definition>
  tasks:
    - <task-definition>
```

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Scenario** | A defined kind of work a Workspace knows how to execute |
| **Track** | Value stream context (Build, Discovery, etc.) |
| **Workspace** | Execution environment (Development, QA, etc.) |
| **Task** | Unit of work within a scenario (agent or human) |

## Design Principles

- **Scenarios are scoped to (Track, Workspace) pairs.** A scenario makes sense in a specific context.
- **Skills, Knowledge, Tools are declared per Scenario.** Each scenario specifies what it needs.
- **Scenarios are templates, not prescriptions.** Workshops can customize freely.
- **Governance scenarios are first-class.** They run at gates, not in separate governance systems.

## Read Next

- [../management/scenario-management/README.md](../management/scenario-management/README.md) — Scenario Management module
- [../management/scenario-management/scenario-schema.md](../management/scenario-management/scenario-schema.md) — Full YAML schema
- [../orchestrator/pi-journey.md](../orchestrator/pi-journey.md) — How scenarios are triggered in PI flow
- [../../ace/concepts.md](../../ace/concepts.md) — ACE Scenario definitions
- [../../ace/workspaces/](../../ace/workspaces/README.md) — Workspace types
