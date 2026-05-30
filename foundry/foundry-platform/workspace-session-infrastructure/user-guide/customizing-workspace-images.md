# Customizing Workspace Images

How Foundry admins add tools, extensions, and configuration to workspace environments without modifying the platform base image.

## Overview

Foundry admins customize workspace environments through **Layer 3 — Admin Layering**. Additions live in the Foundry Definition Repository and are applied automatically when Session Infrastructure provisions a session pod.

You do not build or publish container images. The platform base image (Layer 1) is maintained by the platform release pipeline. Your overlay (Layer 3) is mounted at session start alongside Workshop content (Layer 2).

→ [../concepts/admin-layering.md](../concepts/admin-layering.md) — Overlay mechanism
→ [../concepts/platform-base-image.md](../concepts/platform-base-image.md) — What the base image already includes

## Directory structure

Place overlay content under `workspace-infrastructure/<workspace-type>/` in your Foundry Definition Repo:

```
foundry-{your-foundry}/
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

Supported overlay paths:

| Path | Purpose |
|------|---------|
| `extensions/` | Additional VS Code extensions (`.vsix` files) |
| `bin/` | Custom CLI tools and scripts (added to `PATH`) |
| `config/` | Editor settings, environment defaults |
| `features/` | devcontainer-feature-compatible install scripts |

## Examples

### Adding a custom CLI tool

Place your binary in `bin/`:

```
workspace-infrastructure/development/bin/internal-cli
```

The `admin-overlay` init container copies it to `/usr/local/bin/` in the session pod. Builders can run `internal-cli` from the integrated terminal.

Ensure the binary is compiled for the platform base image architecture (linux/amd64 or linux/arm64).

### Adding a VS Code extension

Place a `.vsix` file in `extensions/`:

```
workspace-infrastructure/development/extensions/company-linter.vsix
```

Extensions are installed into Code Server at session start. Platform-default extensions (Work Orders panel, agent chat) are already included in the base image — your overlay adds to them, not replaces them.

### Adding editor settings

Create `config/settings.json`:

```json
{
  "editor.tabSize": 2,
  "editor.rulers": [100],
  "company-linter.enabled": true
}
```

Settings merge with platform defaults and Workshop `.devcontainer/` settings. Conflicting keys follow precedence: admin overlay overrides Workshop, Workshop overrides platform defaults.

### Adding a language runtime via feature script

For tooling not in the base image activation cache, use a feature install script:

```
workspace-infrastructure/development/features/custom-runtime/install.sh
```

```bash
#!/bin/bash
set -euo pipefail
# Install custom runtime from internal artifact repository
curl -fsSL https://artifacts.internal.example.com/runtime/install.sh | bash
```

Feature scripts run during the `admin-overlay` init container. Keep scripts idempotent and fast — session start time includes init container execution (target: pod ready within 90 seconds).

## Per-workspace-type customization

Each of the six workspace types has its own overlay directory:

| Workspace type | Typical admin additions |
|----------------|------------------------|
| product-specification | Spec linters, internal doc templates |
| ux-design | Design system CLI, asset validators |
| development | Internal SDKs, company git hooks |
| qa | Custom test runners, internal test data tools |
| release | Signing keys (via vault mount), release scripts |
| governance | Policy scanners, audit exporters |

Overlay content applies only to sessions of that workspace type. A development overlay does not affect QA sessions.

## Validation

The Validation module checks overlay structure before your Foundry Definition Repo merge is accepted:

| Check | Limit |
|-------|-------|
| Total overlay size per workspace type | 500 MB |
| Individual file size | 100 MB |
| Allowed paths | `extensions/`, `bin/`, `config/`, `features/` only |
| Executable binaries | Must be ELF binaries or shell scripts with shebang |

Fix validation errors before merging. Invalid overlays block Foundry configuration updates.

## What you cannot customize via overlay

| Concern | Where to configure |
|---------|-------------------|
| Kubernetes cluster endpoint | `workspace_infrastructure.kubernetes` in Foundry settings |
| CPU, memory, storage limits | `workspace_infrastructure.resource_defaults` |
| Session idle timeout | `session_management.idle_timeout_minutes` |
| Platform base image contents | Platform release — request via Platform Admin |
| Workshop scenarios and skills | Workshop Definition Repo |

## Testing your overlay

1. Merge overlay changes to your Foundry Definition Repo
2. Start a new session (or restart a stopped session — overlay re-applies on every start)
3. Verify tools: run `which internal-cli` in the terminal
4. Verify extensions: check Extensions panel in Code Server
5. Check init container logs if something fails: Session Management admin view or kubectl logs in your cluster

Stopped sessions retain workspace files on the PVC but re-apply overlay on resume. You do not need to rebuild anything — merge and start a session.

## Related documentation

- [../concepts/admin-layering.md](../concepts/admin-layering.md) — Technical overlay mechanism
- [../platform-developer-guide/foundry-management-integration.md](../platform-developer-guide/foundry-management-integration.md) — Foundry settings for cluster config
- [foundry-workspace-cli.md](foundry-workspace-cli.md) — In-session CLI
