# Customizing Workspace Images

For Foundry admins: how to add layers via `workspace-infrastructure/<workspace>/` in the Foundry Definition Repository.

## Prerequisites

- Foundry Admin role
- Access to Foundry Definition Repository
- Understanding of [admin layering](../concepts/admin-layering.md) (Layer 3)

## Folder structure

```
foundry-{id}/
└── workspace-infrastructure/
    ├── development/
    │   ├── extensions/              # VS Code extensions (.vsix or marketplace IDs)
    │   ├── tools/                   # Custom CLI binaries or scripts
    │   └── devcontainer-features/   # devcontainer feature definitions
    ├── qa/
    ├── release/
    └── ...
```

Each subdirectory corresponds to a workspace type. Content is mounted as an overlay at session start.

## Examples

### Add a custom CLI tool

```
workspace-infrastructure/development/tools/my-linter
```

The init container copies `tools/` to `/usr/local/bin/` in the session container.

### Add an IDE extension

```
workspace-infrastructure/development/extensions/
└── my-company-extension-1.2.0.vsix
```

Extensions are installed into Code Server at session start.

### Add a language runtime via devcontainer feature

```
workspace-infrastructure/development/devcontainer-features/
└── install-rust/
    └── devcontainer-feature.json
```

Merged with Workshop `.devcontainer/` config during init container run.

## Expected outcome

After merge to Foundry Definition Repo and Validation pass, new sessions of the configured workspace type include your customizations. Existing Active sessions are unaffected until restarted.

## Read next

- [../platform-developer-guide/foundry-management-integration.md](../platform-developer-guide/foundry-management-integration.md) — settings and validation
- [../concepts/platform-base-image.md](../concepts/platform-base-image.md) — what ships in Layer 1
