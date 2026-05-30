# Knowledge Hierarchy

The Knowledge Hierarchy is the Foundry → Workshop → Workbench inheritance model for Domain, Practices, and Ontology knowledge — determining how agents and humans receive context during work execution.

## What it is

Knowledge exists at multiple organizational levels. A coding standard might be organization-wide, but a specific testing methodology might only apply to QA workspaces in a particular product. The Knowledge Hierarchy resolves this complexity.

Three ACE repositories contain knowledge managed through this hierarchy:

| Repository | Scope | Content |
|------------|-------|---------|
| **Domain** | Foundry → Workshop → Workbench | Glossaries, business rules, regulatory frameworks, domain ontologies |
| **Ontology** | Workbench only | Product structure, capabilities, features, maturity states |
| **Practices** | Foundry → Workshop → Workbench | Standards, templates, policies, verification thresholds |

The hierarchy model:

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

At each level, knowledge can be:

| Scope | Folder | Applies To |
|-------|--------|------------|
| **Universal** | `universal/` | All workspace types |
| **Workspace-specific** | `{workspace-type}/` | Only that workspace type |

The six workspace types are: `product-specification`, `ux-design`, `development`, `qa`, `release`, `governance`.

**Resolution rules:**
- Closest wins: Workbench → Workshop → Foundry
- Within a level: workspace-specific → universal
- Ontology is Workbench-only (product structure doesn't inherit)

When WO Runtime assembles agent context, it queries the Knowledge Resolution Service, which merges knowledge from all applicable levels and scopes.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Knowledge Management** (Management subsystem) | Repository provisioning, inheritance resolution, query APIs |
| **Metadata Service** | Stores resolved knowledge, serves queries |
| **Workshop Sync** | Processes knowledge changes from Git |
| **WO Runtime** | Queries knowledge for agent context |

Storage locations:

| Level | Git Repository | Path |
|-------|---------------|------|
| Foundry | `foundry-{id}/` | `domain/`, `practices/` |
| Workshop | `workshop-{id}/` | `domain/`, `practices/` |
| Workbench | `workshop-{id}/` | `workbenches/{product-code}/ontology/`, `domain/`, `practices/` |

## ACE/UPIM alignment

| ACE Repository | Foundry Platform Realization |
|----------------|------------------------------|
| [Domain Repository](../../ace/repositories.md#domain-repository) | Domain knowledge at all levels |
| [Ontology Repository](../../ace/repositories.md#ontology-repository) | Per-Workbench Ontology Service |
| [Practices Repository](../../ace/repositories.md#practices-repository) | Practices at all levels |

From ACE: "Repositories are how a Workshop persists what it knows, what it produces, and what it remembers."

Knowledge Hierarchy operationalizes three of the 15 canonical repositories with hierarchical inheritance appropriate to organizational structure.

## Related concepts

- [Containment Hierarchy](containment-hierarchy.md) — The organizational structure knowledge inherits through
- [Repositories](repositories.md) — All 15 repository types
- [Work Catalog](work-catalog.md) — Similar hierarchy pattern for work definitions
- [Metadata Service](metadata-service.md) — Where resolved knowledge is served from
- [Workspace Session](workspace-session.md) — Where agents consume knowledge

## Further reading

- [../management/platform-developer-guide/knowledge-management/README.md](../management/platform-developer-guide/knowledge-management/README.md) — Subsystem overview
- [../management/platform-developer-guide/knowledge-management/knowledge-hierarchy.md](../management/platform-developer-guide/knowledge-management/knowledge-hierarchy.md) — Detailed resolution rules
- [../management/platform-developer-guide/knowledge-management/knowledge-apis.md](../management/platform-developer-guide/knowledge-management/knowledge-apis.md) — API specifications
- [../../ace/repositories.md](../../ace/repositories.md) — ACE repository definitions
