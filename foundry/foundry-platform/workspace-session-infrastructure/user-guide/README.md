# Workspace Session Infrastructure user guide

This guide covers cluster configuration, workspace image customization, and the in-session CLI for Foundry admins and builders.

## Audience

| Role | Primary interest |
|------|------------------|
| Foundry admins | Kubernetes cluster config, workspace image overlays, resource quotas |
| Builders | In-session CLI for tasks, agents, and Work Order status |

## Guide contents

| Document | Description |
|----------|-------------|
| [customizing-workspace-images.md](customizing-workspace-images.md) | Add tools and extensions via Foundry Definition Repo overlay |
| [foundry-workspace-cli.md](foundry-workspace-cli.md) | `foundry workspace` CLI reference for in-session use |

## Quick start paths

**"I want to add custom tools or extensions to our workspace environments"**
→ Start with [customizing-workspace-images.md](customizing-workspace-images.md)

**"I want to check Work Order status or spawn an agent from the terminal"**
→ Start with [foundry-workspace-cli.md](foundry-workspace-cli.md)

**"I need to configure our Kubernetes cluster for Foundry sessions"**
→ Configure `workspace_infrastructure` in Foundry settings — see [../platform-developer-guide/foundry-management-integration.md](../platform-developer-guide/foundry-management-integration.md)

## How sessions start (overview)

Sessions are provisioned automatically when needed — builders do not manually start pods.

1. Orchestrator requests a session via Session Management
2. Session Infrastructure creates a pod on your Foundry's Kubernetes cluster
3. Init containers apply Workshop content and your admin overlay
4. WO Runtime acknowledges liveness; session becomes Active
5. Builder opens the session URL in a browser — IDE is ready

→ [../platform-developer-guide/sequence-diagrams.md](../platform-developer-guide/sequence-diagrams.md) — Full creation flow

## Related documentation

- [Module README](../README.md) — scope, layering model, boundaries
- [Foundry Platform developer guide](../platform-developer-guide/) — implementation specs
- [Workspace Session Management user guide](../../workspace-session-management/user-guide/) — session lifecycle admin tasks
