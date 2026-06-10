# Platform Base Image

The Platform Base Image is Layer 1 of the workspace layering model — the container image built at platform release time and shared across all Foundry instances.

## What it is

Every Workspace Session runs from a single platform-maintained base image. The image contains the runtime stack required before any Workshop or Foundry-specific content is applied:

| Component | Purpose |
|-----------|---------|
| **Coder Code Server** | Browser-accessible VS Code IDE |
| **WO Runtime binary** | In-session execution daemon |
| **Raw Agent binaries** | All platform-supported agent runtimes |
| **Platform IDE extensions** | Foundry Work Orders panel, agent chat, terminal integration |
| **Process supervisor** | supervisord managing Code Server, WO Runtime, and agent processes |
| **Activation scripts** | Workspace-type-specific tooling invoked at session start |

Key characteristics:

| Aspect | Detail |
|--------|--------|
| **Build owner** | Platform release pipeline |
| **Registry** | Platform or Foundry-configured private registry |
| **Size target** | Under 4GB (WSI-NFR-0005) |
| **Tagging** | Semantic version tied to platform release (e.g. `workspace:v1.2.3`) |
| **Variant strategy** | Single image + workspace-type activation — not six separate images |

## Workspace-type activation

Six workspace types share ~95% of image content. Differences are applied at session start via environment variable and activation script:

| Workspace type | Activation additions |
|----------------|---------------------|
| **product-specification** | Documentation tools, diagram renderers, spec linters |
| **ux-design** | Design tool CLIs, asset processors, preview servers |
| **development** | Language runtimes (Node, Python, Go, Java), build tools, debuggers |
| **qa** | Test frameworks, browser automation, coverage tools |
| **release** | Signing tools, artifact publishers, SBOM generators |
| **governance** | Policy scanners, audit log tools, compliance checkers |

Activation runs as part of the `workspace-merge` init container or as a supervised startup script before WO Runtime sends its liveness acknowledgment.

```
Session start
    │
    ├── Pull base image: registry.foundry.example.com/workspace:v1.2.3
    │
    ├── Set FOUNDRY_WORKSPACE_TYPE={type}
    │
    ├── Run activation script: /opt/foundry/activate-{type}.sh
    │   └── Installs type-specific packages from image cache (no network)
    │
    └── Start supervisord → code-server, wo-runtime
```

## What differs from Workshop and admin layers

| Concern | Platform Base Image | Workshop Template | Admin Overlay |
|---------|--------------------|--------------------|---------------|
| **Scope** | All Foundries, all sessions | Per Workbench | Per Foundry, per workspace type |
| **When** | Build time | Session start | Session start |
| **Examples** | WO Runtime, Code Server | `.devcontainer/`, Scenarios | Custom CLIs, extra extensions |
| **Update cadence** | Platform release | Workshop repo merge | Foundry Definition Repo merge |

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Session Infrastructure** | Defines image contents, build pipeline, activation scripts |
| **IDE** | Specifies extensions packaged into Layer 1 |
| **Agent Fabric** | Specifies Raw Agent binaries included |
| **Work Order Runtime** | Specifies WO Runtime binary version and health endpoint |
| **Release Tools** | Builds and publishes the image as part of platform release |

## Related concepts

- [Admin Layering](admin-layering.md) — Layer 3 Foundry admin additions
- [Workspace Template](workspace-template.md) — Layer 2 Workshop/Workbench merge
- [Session Pod](session-pod.md) — Pod that runs the base image
- [Workspace Session](../../concepts/workspace-session.md) — Platform-wide session definition

## Further reading

- [../platform-developer-guide/container-image-spec.md](../platform-developer-guide/container-image-spec.md) — Full image specification
- [../platform-developer-guide/design-discussions/architecture-choices.md](../platform-developer-guide/design-discussions/architecture-choices.md) — Single image vs six images decision
