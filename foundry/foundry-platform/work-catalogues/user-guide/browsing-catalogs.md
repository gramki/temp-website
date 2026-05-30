# Browsing Work Catalogs

This guide covers how to view available OI Workflows and Scenarios in the Web App and IDE.

## Web App: Resources > Work Catalogs

Access the Work Catalog browser from any Workbench console:

**Navigation:** Console > Resources > Work Catalogs

### Effective Catalog View

The default view shows the **effective catalog** — the merged result of all catalog levels (Platform → Foundry → Workshop → Workbench → User).

```
Work Catalog                                               [Show Sources ▼]
├── build/
│   └── product-intent/
│       ├── workflow.yaml                                  [Platform]
│       ├── product-specification/
│       │   └── scenarios/
│       │       └── create-product-specification.yaml      [Platform]
│       ├── development/
│       │   └── scenarios/
│       │       ├── implement-feature.yaml                 [Workshop]
│       │       └── implement-bugfix.yaml                  [Workbench] ◀ override
│       └── qa/
│           └── scenarios/
│               └── test-feature.yaml                      [Platform]
```

### Source Indicators

Each item shows its source level:

| Badge | Meaning |
|-------|---------|
| `[Platform]` | Shipped with platform, not overridden |
| `[Foundry]` | Defined at Foundry level |
| `[Workshop]` | Defined at Workshop level |
| `[Workbench]` | Defined at Workbench level |
| `[User]` | Your personal catalog (if activated) |
| `◀ override` | This definition shadows a higher-level one |

### Viewing Source Details

Click any item to see details:

- **Definition source:** Which repository contains this definition
- **Override chain:** What this definition overrides (if any)
- **Schema version:** Which scenario/workflow schema version
- **Required skills:** For scenarios, what skills are needed
- **Recent usage:** How often this item has been used

### Filtering

Filter the catalog view by:

- **Track:** Build, Discovery, Run, Win, Evolve, Governance
- **Workspace:** Development, QA, Release, etc.
- **Source level:** Show only Platform defaults, or only overrides
- **Scope:** Show only workspace-ingress (external) or workspace-internal scenarios

## IDE: Work Catalog Explorer

The Work Catalog Explorer extension provides browsing directly in the IDE.

### Opening the Explorer

- **Command Palette:** "Work Catalog: Open Explorer"
- **Activity Bar:** Click the Work Catalog icon
- **Keyboard:** `Cmd+Shift+W` / `Ctrl+Shift+W`

### Explorer Features

**Tree View**
```
WORK CATALOG
├── build
│   └── product-intent
│       ├── workflow.yaml
│       └── development
│           └── scenarios
│               ├── implement-feature.yaml ★
│               └── implement-bugfix.yaml
└── discovery
    └── discovery-case
        └── workflow.yaml
```

The ★ indicates scenarios you've modified (in your User catalog).

**Quick Actions**

Right-click any item for:
- **Open Definition** — View the YAML in editor
- **Show Source** — Open the source repository
- **Copy Path** — Copy the scenario path for use in workflows
- **Test Scenario** — Run a dry-run test (see [testing-scenarios.md](testing-scenarios.md))

### Hover Information

Hover over any scenario to see:

```
┌─────────────────────────────────────────────────┐
│ implement-feature                               │
│ Workspace: development                          │
│ Scope: workspace-ingress                        │
│                                                 │
│ Required Skills:                                │
│   • code-generation                             │
│   • test-writing                                │
│   • git-operations                              │
│                                                 │
│ Source: Workshop (checkout-workshop)            │
│ Overrides: Platform default                     │
└─────────────────────────────────────────────────┘
```

## Viewing Inheritance

Both Web App and IDE can show the inheritance chain for any item.

**Web App:** Click "Show Inheritance" on any item

**IDE:** Right-click > "Show Override Chain"

Example inheritance view:

```
implement-feature.yaml — Override Chain

Level        | Status      | Repository
-------------|-------------|----------------------------------
User         | (none)      | -
Workbench    | ★ Active    | checkout-team/checkout-workbench
Workshop     | Shadowed    | checkout-workshop/work-catalog
Foundry      | Shadowed    | foundry-{id}/work-catalog
Platform     | Shadowed    | platform-defaults/work-catalog/build/...
```

The ★ marks which level is currently active (winning in resolution).

## Comparing Versions

To see what changed between levels:

**Web App:** Click "Compare to Parent" on any overridden item

**IDE:** Right-click > "Diff with Parent Level"

This opens a diff view showing what the override changed from its parent level.

## Workspace-Specific View

When working in a Workspace Session, the catalog view can be scoped to that workspace:

**Session Panel > Available Scenarios**

Shows only scenarios relevant to the current workspace:
- Scenarios in the workspace's folder
- Scenarios with matching workspace type
- Scope indicators (ingress vs internal)

## Searching the Catalog

### Web App Search

Use the search bar to find by:
- Scenario name: `implement-feature`
- Required skill: `skill:code-generation`
- Workspace: `workspace:development`
- Scope: `scope:workspace-ingress`

### IDE Search

**Command Palette:** "Work Catalog: Find Scenario"

Supports fuzzy matching and filters:
```
> implement dev ingress
  implement-feature (development, workspace-ingress)
  implement-bugfix (development, workspace-ingress)
```

## Refreshing the Catalog

Catalogs are cached for performance. To force a refresh:

**Web App:** Click the refresh icon in the Work Catalogs header

**IDE:** Command Palette > "Work Catalog: Refresh"

The cache is automatically invalidated when:
- You publish a scenario
- A PR is merged to any catalog repository you have access to
- The catalog sync service detects changes
