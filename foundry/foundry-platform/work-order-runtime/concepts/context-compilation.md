# Context Compilation

Context Compilation is the process of assembling hierarchical knowledge from multiple levels — Workshop, Workbench, Scenario, and Work Order — into a unified context that agents receive during execution.

## What it is

Agents don't operate in a vacuum. They need knowledge about the domain, the product, the conventions, and the specific work at hand. Context Compilation merges knowledge from the inheritance hierarchy into a single context payload that the Agent Spawner injects into the harness.

The hierarchy provides layered specialization:

| Level | Knowledge Type | Example |
|-------|---------------|---------|
| **Workshop** | Domain, practices, standards | "We use REST APIs with HATEOAS" |
| **Workbench** | Product architecture, conventions | "This app uses React + GraphQL" |
| **Scenario** | Task-specific guidance | "When implementing features, follow this pattern" |
| **Work Order** | WO-specific context | "This WO relates to PI-456, here's the PSD" |

Each level adds specificity. An agent working on a feature implementation receives Workshop standards, Workbench architecture docs, the implementation Scenario guide, and the specific Product Intent this WO addresses.

## Where it lives

| Component | Location |
|-----------|----------|
| **Context compilation** | Agent Spawner (WO Runtime Daemon) |
| **Workshop knowledge** | Workshop Definition Repository |
| **Workbench knowledge** | Workbench settings + linked repos |
| **Scenario knowledge** | Work Catalog Scenario definitions |
| **WO knowledge** | Orchestration item graph + linked artifacts |
| **Cached context** | Local SQLite `context_cache` table |

## Knowledge hierarchy

```
┌─────────────────────────────────────────┐
│  Work Order Context                     │  ← Most specific
│  (parent item, WO artifacts, state)     │
├─────────────────────────────────────────┤
│  Scenario Knowledge                     │
│  (task-specific guides, templates)      │
├─────────────────────────────────────────┤
│  Workbench Knowledge                    │
│  (product-context, architecture,        │
│   conventions, templates)               │
├─────────────────────────────────────────┤
│  Workshop Knowledge                     │  ← Most general
│  (domain, practices, standards)         │
└─────────────────────────────────────────┘
```

## Compilation process

```
Task ready for agent spawn
    │
    ├── 1. Fetch Workshop knowledge
    │       │
    │       └── From Workshop Definition Repo
    │               • domain-glossary.md
    │               • team-conventions.md
    │               • security-guidelines.md
    │
    ├── 2. Fetch Workbench knowledge
    │       │
    │       └── From Workbench settings + repos
    │               • product-architecture.md
    │               • api-documentation.md
    │               • component-catalog.md
    │
    ├── 3. Fetch Scenario knowledge
    │       │
    │       └── From Work Catalog Scenario definition
    │               • implement-feature-guide.md
    │               • coding-patterns.md
    │
    ├── 4. Fetch Work Order knowledge
    │       │
    │       └── From orchestration item graph
    │               • pi-456-context.md (Product Intent)
    │               • related-prs.md
    │               • design-decisions.md
    │
    └── 5. Merge into context payload
            │
            └── knowledge_context: { workshop: [...], workbench: [...], ... }
```

## Context injection

The compiled context is injected into the agent harness:

```yaml
knowledge_context:
  workshop:
    - foundry-standards.md
    - security-guidelines.md
    - domain-glossary.md
  workbench:
    - product-architecture.md
    - api-documentation.md
    - coding-conventions.md
  scenario:
    - implement-feature-guide.md
  work_order:
    - wo-567-context.md
    - pi-456-psd.md
    - related-prs.md
```

How this context reaches the agent depends on the Raw Agent:

| Agent | Injection method |
|-------|------------------|
| Cursor Agent | System prompt + rules |
| Claude Code | Context file parameter |
| Copilot | Workspace context |
| Codex CLI | Context file |

## Caching

Context is cached to avoid repeated fetches:

| Cache | TTL | Invalidation |
|-------|-----|--------------|
| Workshop knowledge | 1 hour | Manual refresh |
| Workbench knowledge | 30 minutes | Manual refresh |
| Scenario knowledge | Session lifetime | Session restart |
| WO knowledge | Per-task | Task restart |

The cache lives in the Local State Store (`context_cache` table).

## Merge rules

When the same file appears at multiple levels, the **more specific level wins** (WO > Scenario > Workbench > Workshop). This allows Workbench-specific conventions to override Workshop standards where appropriate.

Files don't merge content — the entire file from the closer level replaces the file from the farther level.

## Related concepts

- [Agent Spawner](agent-spawner.md) — Invokes context compilation
- [Local State Store](local-state-store.md) — Caches compiled context
- [Knowledge Hierarchy](../../concepts/knowledge-hierarchy.md) — Platform knowledge model
- [Skill](../../concepts/skill.md) — Skills also contribute context (rules, templates)

## Further reading

- [../platform-developer-guide/agent-spawning.md](../platform-developer-guide/agent-spawning.md) — Knowledge assembly details
- [../../management/platform-developer-guide/workshop-repository.md](../../management/platform-developer-guide/workshop-repository.md) — Workshop Definition Repository structure
