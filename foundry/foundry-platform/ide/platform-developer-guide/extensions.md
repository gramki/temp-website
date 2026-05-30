# IDE extensions

## Overview

The Foundry IDE includes extensions that provide Work Order execution UI and Work Catalog authoring capabilities. This document covers plugin architecture and implementation details for platform developers.

## WO Runtime Plugin

The IDE includes a **WO Runtime Plugin** that provides the user interface for Work Order execution:

| Component | Purpose |
|-----------|---------|
| **Work Orders Panel** | Tree view of assigned WOs and task trees with status |
| **Agent Chat Tabs** | Chat interface for agent-user interaction |
| **Agent Terminal Windows** | Terminal interface for CLI agents |

The plugin is a UI layer only — VS Code does not mediate agent I/O. Agents communicate directly with users through the UI components.

See [../../work-order-runtime/platform-developer-guide/ide-integration.md](../../work-order-runtime/platform-developer-guide/ide-integration.md) for full plugin architecture, data flows, and WO Runtime Daemon protocol.

## Extension packaging

Foundry IDE extensions are **not installed at runtime** — they ship pre-installed in the session container image.

| Layer | Who owns it | IDE content |
|-------|-------------|-------------|
| **Layer 1 (base image)** | [Session Infrastructure](../../workspace-session-infrastructure/README.md) | WO Runtime Plugin, Scenario Editor Extension, platform IDE extensions |
| **Layer 3 (admin overlay)** | Foundry admin via `workspace-infrastructure/<workspace>/` | Additional VS Code extensions, CLI tools |

Extension versions are tied to platform release. Session Infrastructure rebuilds the base image when platform extensions change.

Foundry admins can add extensions via the admin layering mechanism documented in [../../workspace-session-infrastructure/user-guide/customizing-workspace-images.md](../../workspace-session-infrastructure/user-guide/customizing-workspace-images.md).

## Integration dependencies

| Module | Relationship |
|--------|--------------|
| [Session Infrastructure](../../workspace-session-infrastructure/README.md) | Packages extensions into base image |
| [Session Management](../../workspace-session-management/README.md) | IDE available only when session is Active |
| [WO Runtime](../../work-order-runtime/README.md) | Plugin protocol for panels and agent chat |

## Scenario Editor Extension

The IDE includes a **Scenario Editor Extension** for authoring and testing Work Catalog content:

| Feature | Description |
|---------|-------------|
| **Schema-aware YAML editing** | Autocomplete, validation, and hover docs for Scenario and OI Workflow schemas |
| **Effective catalog browser** | Browse resolved catalog for current Workbench context |
| **Dry-run execution** | Test scenarios with mock inputs before publishing |
| **Preview effective catalog** | See how changes affect the merged catalog |
| **Publish CLI integration** | Publish to User catalog or create PRs to team catalogs |

### Schema Support

| Schema | Features |
|--------|----------|
| **Scenario schema** | Field completion, skill reference validation, scope hints |
| **OI Workflow schema** | Stage completion, action templates, event suggestions |

### Authoring Workflow

1. **Create/edit YAML file** — Schema-aware editor with real-time validation
2. **Preview in catalog** — See where the item fits in the hierarchy
3. **Dry-run test** — Execute with mock inputs, observe behavior
4. **Publish** — Push to User catalog (direct) or create PR (team catalogs)

### Publish Targets

| Target | Method | Who |
|--------|--------|-----|
| **User catalog** | Direct push | All builders |
| **Workbench catalog** | PR to Workshop repo | Workbench Members |
| **Workshop catalog** | PR to Workshop repo | Workshop Members |
| **Foundry catalog** | PR to Foundry repo | Foundry Members |

See [../../work-catalogues/user-guide/authoring-scenarios.md](../../work-catalogues/user-guide/authoring-scenarios.md) for the builder-facing authoring guide.

## Publish CLI

The Publish CLI provides command-line tooling for publishing Scenarios and OI Workflows to Work Catalogs. The Scenario Editor extension wraps these commands, but they are also available directly.

### CLI Commands

| Command | Description |
|---------|-------------|
| `foundry catalog validate <path>` | Validate a Scenario or Workflow YAML against schema |
| `foundry catalog dry-run <path>` | Execute with mock inputs, report results |
| `foundry catalog publish <path>` | Publish to User catalog (direct push) |
| `foundry catalog publish <path> --target <tier>` | Create PR to team catalog |
| `foundry catalog preview <path>` | Show effective catalog with proposed change |
| `foundry catalog list` | List catalog items visible in current context |

### Publish Protocol

```
foundry catalog publish <path> --target workbench
    │
    ├── 1. Validate YAML against schema
    │       └── Fail fast if invalid
    │
    ├── 2. Resolve effective catalog
    │       └── Check for conflicts/shadowing
    │
    ├── 3. Create branch in Workshop repo
    │       └── Branch: catalog/<user>/<item-name>
    │
    ├── 4. Commit catalog item to branch
    │       └── Path: catalogs/workbench/<workbench-id>/<item>.yaml
    │
    ├── 5. Create Pull Request
    │       └── Title: "Add <item-type>: <name>"
    │       └── Body: Auto-generated from YAML metadata
    │
    └── 6. Return PR URL
```

### Target Resolution

The `--target` flag determines the publish destination:

| Target | Repository | Catalog Path | Required Role |
|--------|------------|--------------|---------------|
| `user` | (local storage) | `~/.foundry/catalogs/user/` | Any builder |
| `workbench` | Workshop repo | `catalogs/workbench/<id>/` | Workbench Member |
| `workshop` | Workshop repo | `catalogs/workshop/` | Workshop Member |
| `foundry` | Foundry repo | `catalogs/foundry/` | Foundry Member |

### Validation Rules

The CLI validates:

| Check | Failure Mode |
|-------|--------------|
| **Schema conformance** | YAML must match Scenario or Workflow schema |
| **Skill references** | Referenced skills must exist in effective catalog |
| **Scope validity** | Scopes must be valid for target tier |
| **Name uniqueness** | Cannot shadow same-tier item with same name |
| **Permission check** | User must have required role for target |

### Dry-Run Execution

Dry-run executes the Scenario with mock inputs:

```
foundry catalog dry-run my-scenario.yaml
    │
    ├── Parse and validate YAML
    ├── Resolve skill bindings
    ├── Generate mock input from schema
    ├── Execute Scenario (sandbox mode)
    │   └── Agent calls are recorded, not executed
    └── Report:
        ├── Resolved task tree
        ├── Skill → Capable Agent bindings
        └── Estimated execution path
```

### Extension Integration

The Scenario Editor extension invokes CLI commands via:

```typescript
import { exec } from 'child_process';

async function publishCatalogItem(path: string, target: string): Promise<string> {
  return new Promise((resolve, reject) => {
    exec(`foundry catalog publish ${path} --target ${target}`, (err, stdout) => {
      if (err) reject(err);
      else resolve(stdout); // PR URL or success message
    });
  });
}
```

The extension provides UI wrappers:

| UI Action | CLI Command |
|-----------|-------------|
| "Validate" button | `foundry catalog validate <path>` |
| "Dry Run" button | `foundry catalog dry-run <path>` |
| "Publish to User" menu | `foundry catalog publish <path>` |
| "Create PR" menu | `foundry catalog publish <path> --target <tier>` |

## Related

- [Foundry Platform developer guide index](README.md)
- [Work Order Runtime: IDE integration](../../work-order-runtime/platform-developer-guide/ide-integration.md) — plugin architecture and daemon protocol
- [IDE user guide: workspace sessions](../user-guide/workspace-sessions.md) — builder experience
- [Work Catalogues: authoring scenarios](../../work-catalogues/user-guide/authoring-scenarios.md) — builder-facing authoring guide
