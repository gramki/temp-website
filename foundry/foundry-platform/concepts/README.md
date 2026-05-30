# Foundry Platform Concepts

This folder contains platform-wide concept definitions for the Foundry Platform. Each concept file provides a single authoritative definition that modules can reference, ensuring consistent terminology across documentation.

## How to use these concepts

- **Reference, don't duplicate.** Link to these definitions rather than restating them in module docs.
- **Concepts are definitions.** Implementation details belong in module specifications.
- **Each concept has one home.** If a concept spans modules, it lives here; module-specific details live in modules.

## Concept Index

### Structure & Organization

| Concept | Definition |
|---------|------------|
| [Containment Hierarchy](containment-hierarchy.md) | Foundry → Workshop → Workbench → Workspace nesting structure |
| [Repositories](repositories.md) | The 15 canonical repository types that persist Workshop state |
| [Knowledge Hierarchy](knowledge-hierarchy.md) | Foundry → Workshop → Workbench inheritance for domain, practices, and ontology |
| [Metadata Service](metadata-service.md) | Central configuration store serving platform consumers |

### Tracks & Work

| Concept | Definition |
|---------|------------|
| [Track](track.md) | Value stream organizing work (Build, Discovery, Run, Win, Evolve, Governance) |
| [Orchestration Item](orchestration-item.md) | Track-level coordination token (Product Intent, Discovery Case, etc.) |
| [Work Catalog](work-catalog.md) | Hierarchical collection of OI Workflows and Scenarios |
| [Scenario](scenario.md) | Ingress contract defining what work a Workspace accepts |
| [Task](task.md) | Unit of work completed by human-agent teams |
| [Work Order](work-order.md) | Instantiation of a Scenario for execution |
| [Workspace Session](workspace-session.md) | Ephemeral development environment for Work Order execution |

### Agents & Skills

| Concept | Definition |
|---------|------------|
| [Agent Model](agent-model.md) | Three-tier agent hierarchy (Capable → Skilled → Employed) |
| [Skill](skill.md) | Reusable capability package for agents |
| [Delegation](delegation.md) | Authority transfer from human to agent via tokens |

### Governance

| Concept | Definition |
|---------|------------|
| [Governance](governance.md) | Discipline of transition validation, evidence capture, and policy enforcement |

## Relationship to ACE and UPIM

These concepts are **Foundry Platform's realization** of ACE model constructs. Where a concept originates in ACE, the concept file cites the ACE source. Where a concept extends or specializes an ACE construct, the file documents the extension.

- **ACE** ([../ace/](../../ace/README.md)) defines the architectural model.
- **UPIM** ([../product-information-model/](../../product-information-model/README.md)) provides the formal information schema.
- **Foundry Platform** implements both via these operational concepts.

## Contributing

When adding a new platform-wide concept:

1. Create `{concept-name}.md` following the template structure
2. Add the concept to the appropriate table in this index
3. Link from module documentation to the concept file
4. Ensure ACE/UPIM alignment section is complete

### Template structure

Each concept file follows this structure:

```markdown
# {Concept Name}

{One-sentence definition.}

## What it is

{2-3 paragraphs explaining the concept, its purpose, and why it matters.}

## Where it lives in Foundry

{Table or description of which modules own/use this concept.}

## ACE/UPIM alignment

{How this concept relates to ACE constructs and UPIM entities, with links.}

## Related concepts

{Links to other concept files that interact with this one.}

## Further reading

{Links to module documentation for implementation details.}
```

## Read next

- [containment-hierarchy.md](containment-hierarchy.md) — Start with the foundational structure
- [track.md](track.md) — Understand how work is organized
- [work-catalog.md](work-catalog.md) — Learn how work definitions are stored
- [../../ace/README.md](../../ace/README.md) — The ACE model these concepts realize
