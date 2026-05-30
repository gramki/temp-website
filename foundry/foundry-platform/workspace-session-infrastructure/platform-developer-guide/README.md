# Workspace Session Infrastructure — Foundry Platform developer guide

This guide contains implementation specifications for engineers building **Workspace Session Infrastructure** — Kubernetes session provisioning, container images, networking, Coder integration, and multi-tenant isolation.

## Implementation overview

Session Infrastructure receives provision requests from Session Management, creates session pods on Foundry-admin-provided Kubernetes clusters, applies three-layer workspace content, generates session URLs via Coder's wildcard proxy, and reports pod readiness or failure events.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|----------------------------|
| [Workspace Session](../../concepts/workspace-session.md) | Provisions K8s pod, PVC, and URL |
| [Workspace](../../ace/concepts.md#workspace) | Workspace type drives activation and resource defaults |
| [IDE](../../ace/concepts.md#ide) | Code Server and extensions in platform base image |

## Specification index

| Document | Scope |
|----------|-------|
| [requirements.md](requirements.md) | WSI-FR-0001 through WSI-FR-0012, WSI-NFR-0001 through WSI-NFR-0007 |
| [kubernetes-integration.md](kubernetes-integration.md) | Cluster connectivity, kubeconfig, authentication |
| [pod-lifecycle.md](pod-lifecycle.md) | Creation, probes, graceful shutdown, eviction |
| [networking.md](networking.md) | Session URLs, TLS, WebSocket, DNS |
| [storage.md](storage.md) | PVC lifecycle, ephemeral volumes |
| [coder-on-kubernetes.md](coder-on-kubernetes.md) | Coder workspace provider, template registration |
| [multi-tenant-isolation.md](multi-tenant-isolation.md) | Namespace, NetworkPolicy, RBAC, quotas |
| [container-image-spec.md](container-image-spec.md) | Base image contents, registry, tagging |
| [interface-contracts.md](interface-contracts.md) | APIs and events with Session Management |
| [failure-modes.md](failure-modes.md) | Failure scenarios and recovery |
| [foundry-management-integration.md](foundry-management-integration.md) | `workspace_infrastructure` settings |
| [sequence-diagrams.md](sequence-diagrams.md) | Creation, stop, pod crash recovery flows |
| [design-discussions/architecture-choices.md](design-discussions/architecture-choices.md) | Coder, single container, wildcard ingress, image strategy |

## Dependencies

| Module / foundation | Integration |
|---------------------|-------------|
| [Workspace Session Management](../workspace-session-management/) | Provision requests; pod-ready/failed events |
| [Work Order Runtime](../work-order-runtime/) | Runs in pod; `/health` for probes |
| [Management](../management/platform-developer-guide/) | Foundry settings, Metadata Service |
| [IDE](../ide/) | Extensions in base image |
| Coder | Workspace provisioner and URL proxy |

## Related documentation

- [Module concepts](../README.md) — scope, layering model, boundaries
- [User guide](../user-guide/) — admin customization and in-session CLI
- [Foundry Platform README](../../README.md) — platform-wide module map
