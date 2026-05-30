# Knowledge Hierarchy

This document specifies the inheritance model and resolution rules for Domain and Practices knowledge across Foundry, Workshop, and Workbench levels.

## Overview

Knowledge follows a hierarchical model where more specific levels override more general levels:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Knowledge Resolution                                 │
│                                                                              │
│    Foundry ────────► Workshop ────────► Workbench                           │
│    (base)           (override)          (override)                          │
│                                                                              │
│    At each level:                                                            │
│    universal ────────► {workspace-type}                                     │
│    (base)              (override)                                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Hierarchy Levels

### Level 1: Foundry

Organization-wide knowledge that applies to all Workshops and Workbenches.

| Repository | Location |
|------------|----------|
| Domain | `foundry-{id}/domain/` |
| Practices | `foundry-{id}/practices/` |

**Examples:**
- Company glossary
- Organization-wide security standards
- Corporate coding conventions
- Regulatory compliance frameworks

### Level 2: Workshop

Division or unit-specific knowledge that applies to all Workbenches in the Workshop.

| Repository | Location |
|------------|----------|
| Domain | `workshop-{id}/domain/` |
| Practices | `workshop-{id}/practices/` |

**Examples:**
- Division-specific terminology
- Team coding standards (more specific than Foundry)
- Division review policies
- Business unit regulatory requirements

### Level 3: Workbench

Product-specific knowledge that applies only to this Workbench.

| Repository | Location |
|------------|----------|
| Domain | `workshop-{id}/workbenches/{product-code}/domain/` |
| Practices | `workshop-{id}/workbenches/{product-code}/practices/` |
| Ontology | `workshop-{id}/workbenches/{product-code}/ontology/` |

**Examples:**
- Product-specific terminology
- Product architecture conventions
- Product-specific testing requirements
- Product structure and capabilities (Ontology)

## Workspace Scope

At each hierarchy level, knowledge can be scoped to apply universally or to specific workspace types.

### Scope Types

| Scope | Folder | Applies To |
|-------|--------|------------|
| **Universal** | `universal/` | All six workspace types |
| **Workspace-specific** | `{workspace-type}/` | Only the named workspace type |

### Workspace Types

The six workspace types are:

| Workspace Type | Folder Name |
|----------------|-------------|
| Product Specification | `product-specification/` |
| UX Design | `ux-design/` |
| Development | `development/` |
| QA | `qa/` |
| Release | `release/` |
| Governance | `governance/` |

### Folder Structure

```
domain/                      # or practices/
├── universal/               # Applies to ALL workspaces
│   ├── glossary.md
│   └── business-rules.md
├── product-specification/   # Only Product Specification workspace
│   └── requirement-terminology.md
├── development/             # Only Development workspace
│   └── api-naming-conventions.md
├── qa/                      # Only QA workspace
│   └── defect-classification.md
└── ...
```

## Resolution Algorithm

When resolving knowledge for a specific context (Workbench + Workspace Type), the resolution follows this algorithm:

```
Input: (workbench_id, workspace_type, knowledge_type, path)

1. Collect candidates from all levels:
   - Foundry/universal/{path}
   - Foundry/{workspace_type}/{path}
   - Workshop/universal/{path}
   - Workshop/{workspace_type}/{path}
   - Workbench/universal/{path}
   - Workbench/{workspace_type}/{path}

2. Apply resolution rules:
   a. Closer level wins (Workbench > Workshop > Foundry)
   b. More specific scope wins (workspace-type > universal)

3. Return the most specific match
```

### Resolution Priority (Highest to Lowest)

| Priority | Source |
|----------|--------|
| 1 (highest) | Workbench/{workspace-type}/ |
| 2 | Workbench/universal/ |
| 3 | Workshop/{workspace-type}/ |
| 4 | Workshop/universal/ |
| 5 | Foundry/{workspace-type}/ |
| 6 (lowest) | Foundry/universal/ |

## Resolution Examples

### Example 1: Coding Standards for Development Workspace

**Query:** `practices/coding-standards.md` for Development workspace in Workbench `checkout`

**Available files:**
```
foundry-zeta/practices/universal/coding-standards.md         # Priority 6
foundry-zeta/practices/development/coding-standards.md       # Priority 5
workshop-payments/practices/development/coding-standards.md  # Priority 3
```

**Resolution:** `workshop-payments/practices/development/coding-standards.md` (Priority 3)

### Example 2: Glossary for QA Workspace

**Query:** `domain/glossary.md` for QA workspace in Workbench `checkout`

**Available files:**
```
foundry-zeta/domain/universal/glossary.md                    # Priority 6
workshop-payments/domain/universal/glossary.md               # Priority 4
```

**Resolution:** `workshop-payments/domain/universal/glossary.md` (Priority 4)

No QA-specific glossary exists, so universal at Workshop level wins.

### Example 3: Testing Methodology

**Query:** `practices/testing-methodology.md` for QA workspace in Workbench `checkout`

**Available files:**
```
foundry-zeta/practices/qa/testing-methodology.md             # Priority 5
checkout/practices/qa/testing-methodology.md                 # Priority 1
```

**Resolution:** `checkout/practices/qa/testing-methodology.md` (Priority 1)

Workbench-specific QA practices override Foundry-level.

### Example 4: No Override at Lower Levels

**Query:** `practices/security-standards.md` for Development workspace

**Available files:**
```
foundry-zeta/practices/universal/security-standards.md       # Priority 6
```

**Resolution:** `foundry-zeta/practices/universal/security-standards.md`

Only Foundry-level exists; it applies everywhere.

## Merge vs Override Semantics

Knowledge resolution uses **file-level override semantics**, not content merging:

| Behavior | Description |
|----------|-------------|
| **Override** | If a file exists at a more specific level, it completely replaces the less specific version |
| **No Merge** | Content from different levels is NOT merged together |
| **Inheritance** | If a file doesn't exist at a more specific level, the less specific version is used |

### Why Override, Not Merge?

1. **Predictability** — Easy to understand which content applies
2. **Auditability** — Clear chain of what overrides what
3. **Simplicity** — No complex merge logic for different content types
4. **Intentionality** — If you override, you own the full content

### Handling Partial Overrides

If you want to extend rather than replace, the recommended pattern is:

```markdown
# Product-Specific Coding Standards

This document extends the [Workshop coding standards](../../practices/development/coding-standards.md).

## Additional Standards

[Product-specific content here]
```

The reference to the parent document is explicit rather than implicit.

## Ontology: No Inheritance

Ontology is an exception to the inheritance model:

| Characteristic | Behavior |
|----------------|----------|
| **Level** | Workbench only |
| **Inheritance** | None — each Workbench defines its own |
| **Workspace Scope** | None — product-wide |

Ontology defines the product structure (capabilities, features, modules), which is inherently product-specific. There's no meaningful "default" product structure to inherit.

## Context Assembly

When WO Runtime assembles context for an agent, it resolves knowledge in this order:

```
1. Determine context: (workbench_id, workspace_type)

2. Resolve Domain knowledge:
   - List all domain files needed
   - For each file, apply resolution algorithm
   - Collect resolved files

3. Resolve Practices knowledge:
   - List all practice files needed
   - For each file, apply resolution algorithm
   - Collect resolved files

4. Load Ontology (if applicable):
   - Load from Workbench/ontology/

5. Assemble into agent context
```

## Listing Available Knowledge

When listing what knowledge is available for a context, the resolution shows the effective set:

**API:** `GET /knowledge/{workbench_id}/{workspace_type}/domain`

**Response:**
```json
{
  "files": [
    {
      "path": "glossary.md",
      "source": "workshop",
      "scope": "universal",
      "location": "workshop-payments/domain/universal/glossary.md"
    },
    {
      "path": "api-conventions.md",
      "source": "workbench",
      "scope": "development",
      "location": "checkout/domain/development/api-conventions.md"
    }
  ]
}
```

## Validation Rules

The [Validation module](../validation/README.md) enforces knowledge rules via **KnowledgeValidator**:

| Rule | Validation |
|------|------------|
| **Valid workspace types** | Folders must be `universal/` or a valid workspace type |
| **No unknown folders** | No arbitrary folders at the scope level |
| **Valid content** | Markdown files must be valid; YAML files must parse |
| **No circular references** | References to parent knowledge must not create cycles |

## Edge Cases

### Same File in Universal and Workspace-Specific

If both exist at the same level:
- `workshop/domain/universal/glossary.md`
- `workshop/domain/development/glossary.md`

For Development workspace: workspace-specific wins.
For QA workspace: universal is used (no QA-specific exists).

### Missing Intermediate Levels

If Foundry has knowledge but Workshop doesn't:
- Workbench inherits directly from Foundry
- No requirement for knowledge at every level

### Empty Folders

Empty scope folders are allowed and simply mean "no knowledge at this scope."

## Performance Considerations

- **Caching** — Resolved knowledge is cached in Metadata Service
- **Invalidation** — Cache invalidated on Workshop Sync
- **Lazy Loading** — Knowledge loaded on-demand, not pre-computed

## Read Next

- [knowledge-apis.md](knowledge-apis.md) — API specifications for querying knowledge
- [README.md](README.md) — Knowledge Management overview
- [../validation/README.md](../validation/README.md) — Validation module (KnowledgeValidator)
- [../foundry-definition-repository.md](../foundry-definition-repository.md) — Foundry repo structure
- [../workshop-repository.md](../workshop-repository.md) — Workshop repo structure
