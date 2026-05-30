# Workspace Session Infrastructure Concepts

This folder contains module-specific concept definitions for Workspace Session Infrastructure. Each concept file provides a single authoritative definition within this module's domain, linking back to platform-wide concepts where appropriate.

## How to use these concepts

- **Reference, don't duplicate.** Link to these definitions rather than restating them in module docs.
- **Module-specific scope.** These concepts specialize infrastructure provisioning; lifecycle control lives in [Workspace Session Management](../../workspace-session-management/); in-session execution lives in [Work Order Runtime](../../work-order-runtime/).
- **Implementation details elsewhere.** Concepts are definitions; K8s specs and requirements live in `platform-developer-guide/`.

## Concept Index

| Concept | Definition |
|---------|------------|
| [Platform Base Image](platform-base-image.md) | Layer 1 container image: Code Server, WO Runtime, agents, IDE extensions |
| [Admin Layering](admin-layering.md) | Layer 3 Foundry admin overlay from Foundry Definition Repo |
| [Workspace Template](workspace-template.md) | Layer 2 Coder template and Workshop/Workbench merge |
| [Session Pod](session-pod.md) | Kubernetes pod as the unit of session infrastructure |

## Relationship to Platform Concepts

| Platform Concept | Session Infrastructure Specialization |
|------------------|---------------------------------------|
| [Workspace Session](../../concepts/workspace-session.md) | Session Pod + URL + PVC = the session runtime |
| [Agent Model](../../concepts/agent-model.md) | Capable Agent binaries ship in Platform Base Image |
| [Workspace](../../ace/concepts.md#workspace) | Workspace type drives activation layer and resource defaults |

## Three-layer model

```
Layer 1 (build time)     Platform Base Image
        │
Layer 2 (session start)  Workspace Template → init container: workspace-merge
        │
Layer 3 (session start)  Admin Layering → init container: admin-overlay
        │
        ▼
                   Session Pod (running container)
```

## Read next

- [platform-base-image.md](platform-base-image.md) — What ships in the container image
- [session-pod.md](session-pod.md) — Pod anatomy and lifecycle mapping
- [../README.md](../README.md) — Module scope and boundaries
- [../../concepts/workspace-session.md](../../concepts/workspace-session.md) — Platform-wide definition
