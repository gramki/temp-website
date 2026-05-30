# Container Image Specification

Base image contents, registry configuration, tagging strategy, and workspace-type activation.

## Image strategy

Session Infrastructure ships a **single base image + workspace-type activation** at session start. Six workspace types share ~95% of content; type-specific tooling is activated via init container scripts, not separate image builds.

→ [design-discussions/architecture-choices.md](design-discussions/architecture-choices.md) — Image variant decision
→ [../concepts/platform-base-image.md](../concepts/platform-base-image.md) — Layer 1 concept

## Base image contents

| Component | Path / version | Source module |
|-----------|----------------|---------------|
| Coder Code Server | `/usr/bin/code-server` | Platform release |
| WO Runtime | `/opt/foundry/wo-runtime` | Work Order Runtime |
| Capable Agent binaries | `/opt/foundry/agents/` | Agent Fabric |
| Platform IDE extensions | `/opt/foundry/extensions/` | IDE |
| Process supervisor | `/usr/bin/supervisord` | Platform release |
| Activation scripts | `/opt/foundry/activate-{type}.sh` | Session Infrastructure |
| Init container tooling | `workspace-init` image (separate) | Session Infrastructure |

### Init container image

The `workspace-init` image is a lightweight companion used by init containers only:

| Tool | Purpose |
|------|---------|
| `foundry-workspace-merge` | Fetches and merges Workshop/Workbench content |
| `foundry-admin-overlay` | Applies Foundry admin layers |
| Git client | Clones Workshop and Foundry Definition Repos |
| devcontainer CLI | Interprets `.devcontainer/` features |

Tagged alongside the base image: `workspace-init:v1.2.3`.

## Workspace-type activation

Activation scripts install type-specific packages from a pre-baked cache inside the image — no network fetch at activation time:

| Workspace type | Activation script | Additional tooling |
|----------------|-------------------|-------------------|
| product-specification | `activate-product-specification.sh` | Pandoc, Mermaid CLI, spec linters |
| ux-design | `activate-ux-design.sh` | Figma CLI, asset optimizers |
| development | `activate-development.sh` | Node, Python, Go, Java runtimes; build tools |
| qa | `activate-qa.sh` | Playwright, pytest, coverage tools |
| release | `activate-release.sh` | Cosign, Syft, artifact publishers |
| governance | `activate-governance.sh` | Policy scanners, audit tools |

Activation is triggered by `FOUNDRY_WORKSPACE_TYPE` environment variable set in the pod spec.

**WSI-FR-0005:** All six workspace types supported via activation layer on the single base image.

## Registry and tagging

| Aspect | Specification |
|--------|---------------|
| **Registry** | `workspace_infrastructure.image_registry.url` (Foundry-specific or platform default) |
| **Pull secret** | `image_registry.pull_secret_ref` — vault reference, namespace-scoped |
| **Base image tag** | `workspace:{platform-version}` (e.g. `workspace:v1.2.3`) |
| **Init image tag** | `workspace-init:{platform-version}` |
| **Immutability** | Tags are immutable; patch releases get new tags |
| **Size target** | Under 4GB (WSI-NFR-0005) |

Foundry admin may mirror the platform image to a private registry. Session Infrastructure pulls from the configured registry at provision time.

## Image layers

```
┌─────────────────────────────────────────┐
│  Layer 1: Platform base image (build)   │
│  code-server, wo-runtime, agents,       │
│  extensions, supervisord, activation    │
│  cache for all workspace types          │
├─────────────────────────────────────────┤
│  Layer 2: Workshop merge (init container)│
│  .devcontainer/, scenarios, skills      │
├─────────────────────────────────────────┤
│  Layer 3: Admin overlay (init container) │
│  workspace-infrastructure/<workspace>/  │
└─────────────────────────────────────────┘
```

Layers 2 and 3 are not baked into the image — they are applied at session start. See [../concepts/admin-layering.md](../concepts/admin-layering.md) and [../concepts/workspace-template.md](../concepts/workspace-template.md).

## Build pipeline

Platform release builds and publishes:

1. Build base image with all activation caches
2. Build init container image
3. Scan for vulnerabilities (block on critical CVEs)
4. Push to platform registry with version tag
5. Update Coder template image references
6. Publish manifest to Release Tools artifact store

Foundry admins do not build Layer 1 images. Customization is via Layer 3 overlay only.

## Process supervision layout

The base image includes `/etc/supervisord.conf`:

```ini
[program:code-server]
command=/usr/bin/code-server --bind-addr 0.0.0.0:8080 /workspace
autorestart=true
priority=10

[program:wo-runtime]
command=/opt/foundry/wo-runtime --port 9090
autorestart=true
priority=20
startsecs=5
```

Capable Agent processes are spawned on demand by WO Runtime via supervisor API — not pre-started.

## Health endpoint

WO Runtime exposes `GET /health` on port 9090. Included in base image; used by Kubernetes readiness and liveness probes.

## Related documentation

- [../concepts/platform-base-image.md](../concepts/platform-base-image.md) — Layer 1 concept
- [pod-lifecycle.md](pod-lifecycle.md) — Image reference in pod spec
- [coder-on-kubernetes.md](coder-on-kubernetes.md) — Template image parameters
- [../user-guide/customizing-workspace-images.md](../user-guide/customizing-workspace-images.md) — Admin overlay (Layer 3)
- [requirements.md](requirements.md) — WSI-FR-0005, WSI-NFR-0005
