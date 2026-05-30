# Knowledge Management

**Subsystem scope:** Manage Domain, Ontology, and Practices repositories with hierarchical inheritance and workspace-scoped resolution.

## Purpose

Knowledge Management handles the three ACE knowledge repositories that provide context to agents and humans during work execution. Without proper knowledge management, agents would lack the domain understanding, standards, and product context needed to produce quality work.

The subsystem solves a key problem: knowledge exists at multiple organizational levels (Foundry, Workshop, Workbench) and applies differently to different workspace types. A coding standard might be organization-wide, but a specific testing methodology might only apply to QA workspaces in a particular product. Knowledge Management resolves this complexity by providing a clear inheritance model and serving the right knowledge to the right context.

Primary consumers are WO Runtime (which assembles agent context) and the agents themselves (which query for domain and practice knowledge during task execution).

## What this subsystem does

- **Repository Provisioning** — create Domain/Practices folders at each level; provision Ontology Service per Workbench
- **Inheritance Resolution** — merge knowledge from Foundry → Workshop → Workbench levels
- **Workspace Scope Resolution** — resolve universal vs workspace-specific knowledge
- **Query APIs** — serve resolved knowledge to WO Runtime and agents via Metadata Service

## What this subsystem does NOT do

| Boundary | Owned By |
|----------|----------|
| Author knowledge content | Workshop/Workbench teams (via Git) |
| Assemble agent context at runtime | WO Runtime |
| Store knowledge embeddings | Evolution Repository |
| Define ACE repository taxonomy | ACE documentation |

## Knowledge Repositories

Three ACE repositories contain knowledge that this subsystem manages:

| Repository | Scope | Content |
|------------|-------|---------|
| **Domain** | Foundry → Workshop → Workbench | Glossaries, business rules, regulatory frameworks, domain ontologies |
| **Ontology** | Workbench only | Product structure, capabilities, features, maturity states |
| **Practices** | Foundry → Workshop → Workbench | Standards, templates, policies, verification thresholds |

### Domain Repository

Domain knowledge provides semantic grounding for all work:

| Content Type | Examples |
|--------------|----------|
| Glossaries | Business terminology, acronyms, definitions |
| Business Rules | Validation logic, constraints, policies |
| Regulatory Frameworks | GDPR, SOC2, HIPAA, PCI-DSS requirements |
| Domain Models | Entity relationships, event definitions |

### Ontology Repository

Ontology defines the product structure (Workbench-level only):

| Content Type | Examples |
|--------------|----------|
| Product Structure | Modules, components, systems hierarchy |
| Capability Catalog | What the product can do |
| Feature Hierarchy | Features organized by capability |
| Maturity States | Beta, GA, Deprecated status |

### Practices Repository

Practices establish standards for how work is done:

| Content Type | Examples |
|--------------|----------|
| Standards | Coding standards, design guidelines, documentation conventions |
| Templates | PRD templates, test case templates, runbook templates |
| Policies | Review policies, approval workflows, evidence requirements |
| Verification | Coverage thresholds, quality gates, compliance checks |

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Knowledge Management                                 │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │                    Knowledge Resolution Service                         │ │
│  │                                                                         │ │
│  │    ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐      │ │
│  │    │    Foundry      │  │    Workshop     │  │   Workbench     │      │ │
│  │    │    Knowledge    │──│    Knowledge    │──│   Knowledge     │      │ │
│  │    │    Loader       │  │    Loader       │  │   Loader        │      │ │
│  │    └─────────────────┘  └─────────────────┘  └─────────────────┘      │ │
│  │              │                  │                    │                 │ │
│  │              └──────────────────┴────────────────────┘                 │ │
│  │                                 │                                       │ │
│  │                    ┌────────────┴────────────┐                         │ │
│  │                    │   Resolution Engine     │                         │ │
│  │                    │   (hierarchy + scope)   │                         │ │
│  │                    └────────────┬────────────┘                         │ │
│  └─────────────────────────────────┼───────────────────────────────────────┘ │
│                                    │                                         │
│  ┌─────────────────────────────────┼───────────────────────────────────────┐ │
│  │                         Metadata Service                                │ │
│  │                    (stores resolved knowledge)                          │ │
│  └─────────────────────────────────┼───────────────────────────────────────┘ │
└────────────────────────────────────┼────────────────────────────────────────┘
                                     │
                                     ▼
                    ┌────────────────┴────────────────┐
                    │                                 │
                    ▼                                 ▼
            ┌─────────────┐                  ┌─────────────┐
            │ WO Runtime  │                  │   Agents    │
            │(context     │                  │  (queries)  │
            │ assembly)   │                  │             │
            └─────────────┘                  └─────────────┘
```

## Hierarchy Model

Knowledge follows a three-level hierarchy with workspace scope at each level:

```
Foundry
├── Domain (universal + per-workspace-type)
└── Practices (universal + per-workspace-type)
    │
    └── Workshop
        ├── Domain (universal + per-workspace-type)
        └── Practices (universal + per-workspace-type)
            │
            └── Workbench
                ├── Ontology (product-wide, no workspace scope)
                ├── Domain (universal + per-workspace-type)
                └── Practices (universal + per-workspace-type)
```

### Level Scope

| Level | Scope | Storage |
|-------|-------|---------|
| **Foundry** | Organization-wide | `foundry-{id}/` repo |
| **Workshop** | Division/unit-wide | `workshop-{id}/` repo |
| **Workbench** | Product-specific | `workshop-{id}/workbenches/{product-code}/` |

### Workspace Scope

At each level, knowledge can be:

| Scope | Folder | Applies To |
|-------|--------|------------|
| **Universal** | `universal/` | All workspace types |
| **Workspace-specific** | `{workspace-type}/` | Only that workspace type |

The six workspace types are: `product-specification`, `ux-design`, `development`, `qa`, `release`, `governance`.

→ [knowledge-hierarchy.md](knowledge-hierarchy.md) for detailed inheritance and resolution rules

## Storage Model

### Git Repository Locations

| Level | Git Repository | Path |
|-------|---------------|------|
| Foundry | `foundry-{id}/` | `domain/`, `practices/` |
| Workshop | `workshop-{id}/` | `domain/`, `practices/` |
| Workbench | `workshop-{id}/` | `workbenches/{product-code}/ontology/`, `domain/`, `practices/` |

### Folder Structure

```
# Foundry repo
foundry-{id}/
├── domain/
│   ├── universal/
│   └── {workspace-type}/
└── practices/
    ├── universal/
    └── {workspace-type}/

# Workshop repo
workshop-{id}/
├── domain/
│   ├── universal/
│   └── {workspace-type}/
├── practices/
│   ├── universal/
│   └── {workspace-type}/
└── workbenches/
    └── {product-code}/
        ├── ontology/          # Workbench-only
        ├── domain/
        │   ├── universal/
        │   └── {workspace-type}/
        └── practices/
            ├── universal/
            └── {workspace-type}/
```

→ [../foundry-definition-repository.md](../foundry-definition-repository.md) for Foundry repo details
→ [../workshop-repository.md](../workshop-repository.md) for Workshop repo details

## Integration with Other Services

### Workshop Sync Service

When knowledge content changes in Git:
1. PR opened → Validation module validates structure
2. PR merged → Workshop Sync Service processes webhook
3. Sync Service writes to Metadata Service
4. Metadata Service makes knowledge queryable

### Metadata Service

Stores resolved knowledge indexed by:
- Foundry ID
- Workshop ID (optional)
- Workbench ID (optional)
- Workspace type (optional)
- Knowledge type (domain, practices, ontology)

### WO Runtime

At task execution:
1. WO Runtime queries Metadata Service for resolved knowledge
2. Resolution considers: Workbench → Workshop → Foundry, workspace-type → universal
3. Resolved knowledge injected into agent context

→ [knowledge-apis.md](knowledge-apis.md) for API specifications

## ACE Concepts Realized

| Concept | How Knowledge Management realizes it |
|---------|--------------------------------------|
| **Domain Repository** | Manages domain knowledge at all levels |
| **Practices Repository** | Manages practices at all levels |
| **Ontology Repository** | Provisions and manages per-Workbench Ontology Service |
| **Knowledge Hierarchy** | Implements Foundry → Workshop → Workbench inheritance |

## Key Design Decisions

- **Three repositories, one subsystem.** Domain, Ontology, and Practices are managed together because they share the same inheritance and resolution model.
- **Git as source of truth.** Knowledge lives in Git repos; Metadata Service is the serving layer.
- **Workspace scope is explicit.** Universal vs workspace-specific is a folder structure choice, not metadata.
- **Ontology is Workbench-only.** Product structure doesn't inherit; each product defines its own ontology.
- **Resolution at query time.** Knowledge is resolved when queried, not pre-computed.

## Open Questions

- Knowledge versioning and rollback
- Cross-Workbench knowledge references
- Knowledge search and discovery UX
- Knowledge change impact analysis

## Module Documents

| Document | Content |
|----------|---------|
| [knowledge-hierarchy.md](knowledge-hierarchy.md) | Inheritance model and resolution rules |
| [knowledge-apis.md](knowledge-apis.md) | REST API specifications |

## Read Next

- [../foundry-definition-repository.md](../foundry-definition-repository.md) — Foundry repo structure
- [../workshop-repository.md](../workshop-repository.md) — Workshop repo structure
- [../services/metadata-service.md](../services/metadata-service.md) — Where knowledge is served from
- [../../work-order-runtime/README.md](../../work-order-runtime/README.md) — How agents consume knowledge
