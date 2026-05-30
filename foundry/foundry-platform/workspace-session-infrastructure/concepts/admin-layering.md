# Admin Layering

Admin Layering is Layer 3 of the workspace layering model — Foundry-specific additions mounted into session pods at start time from the Foundry Definition Repository.

## What it is

Foundry admins customize workspace environments without modifying the platform base image or Workshop content. Additions live in the Foundry Definition Repo under `workspace-infrastructure/<workspace>/` and are applied as an overlay volume when Session Infrastructure provisions a pod.

Typical overlay contents:

| Path in overlay | Purpose |
|-----------------|---------|
| `extensions/` | Additional VS Code extensions beyond platform defaults |
| `bin/` | Custom CLI tools and scripts |
| `config/` | Environment defaults, editor settings |
| `features/` | devcontainer-feature-compatible install scripts |

Key characteristics:

| Aspect | Detail |
|--------|--------|
| **Scope** | Per Foundry, per workspace type |
| **When applied** | Session start — `admin-overlay` init container |
| **Source** | `foundry-{id}/workspace-infrastructure/{workspace-type}/` in Foundry Definition Repo |
| **Persistence** | Overlay is re-applied on every start; not stored on PVC |
| **Validation** | Validation module checks overlay structure before merge to Foundry |

## Overlay mechanism

The `admin-overlay` init container fetches overlay content from the Foundry Definition Repo (via Metadata Service or direct git clone) and writes it to the shared `merged-content` emptyDir volume:

```
foundry-{id}/
└── workspace-infrastructure/
    ├── development/
    │   ├── extensions/
    │   │   └── company-linter.vsix
    │   ├── bin/
    │   │   └── internal-cli
    │   └── config/
    │       └── settings.json
    ├── qa/
    │   └── bin/
    │       └── custom-test-runner
    └── release/
        └── features/
            └── signing-tool/
                └── install.sh
```

At pod start:

```
admin-overlay init container
    │
    ├── Resolve foundry_id + workspace_type from provision request
    │
    ├── Fetch workspace-infrastructure/{workspace_type}/ from Foundry Definition Repo
    │
    ├── Validate overlay manifest (allowed paths, size limits)
    │
    └── Write to /merged-content/admin-overlay/
            │
            └── Main container mounts at /workspace/.foundry/admin/
```

The main container startup script merges admin overlay into the active environment — installing extensions, adding `bin/` to PATH, applying config.

## Security boundaries

| Rule | Rationale |
|------|-----------|
| Workshop/Workbench cannot override cluster config | Cluster endpoint is a Foundry admin security boundary |
| Overlay cannot modify WO Runtime or Code Server binaries | Platform integrity — only additive content |
| Overlay size limit enforced at validation | Prevents storage exhaustion on init |
| No privileged operations in overlay scripts | Pod runs under Restricted pod security standard |

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Session Infrastructure** | Fetches and mounts overlay at session start |
| **Management / Validation** | Validates overlay structure in Foundry Definition Repo |
| **Foundry admin** | Authors overlay content |

Workshop and Workbench content (Layer 2) is separate — admin overlay does not replace `.devcontainer/` or Scenario definitions.

## Related concepts

- [Platform Base Image](platform-base-image.md) — Layer 1 platform image
- [Workspace Template](workspace-template.md) — Layer 2 Workshop/Workbench merge
- [Session Pod](session-pod.md) — Where overlay is mounted

## Further reading

- [../user-guide/customizing-workspace-images.md](../user-guide/customizing-workspace-images.md) — Admin guide with examples
- [../platform-developer-guide/foundry-management-integration.md](../platform-developer-guide/foundry-management-integration.md) — Settings model
