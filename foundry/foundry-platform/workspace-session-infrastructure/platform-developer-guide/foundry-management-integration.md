# Foundry Management Integration

How `workspace_infrastructure` configuration integrates with the existing Foundry settings model.

## Settings placement

`workspace_infrastructure` is a **new top-level Foundry setting** alongside existing `identity`, `agents`, and `integrations` blocks in `foundry.yaml`.

Set by **Foundry Admin** (not Platform Admin) — each Foundry brings its own Kubernetes cluster.

```yaml
# In foundry.yaml or Foundry Settings UI
workspace_infrastructure:
  kubernetes:
    endpoint: "https://k8s.example.com:6443"
    auth:
      type: "service-account" | "oidc" | "certificate"
      credentials_ref: "vault://foundry/{id}/k8s-creds"
    namespace_prefix: "foundry-{id}-sessions"
    storage_class: "gp3"
    ingress_class: "nginx"
    ingress_domain: "sessions.foundry.example.com"
    tls:
      issuer: "letsencrypt-prod"
  resource_defaults:
    cpu_request: "2"
    cpu_limit: "4"
    memory_request: "4Gi"
    memory_limit: "8Gi"
    storage_size: "20Gi"
  resource_quota:
    max_pods: 50
    max_storage: "2Ti"
  image_registry:
    url: "registry.foundry.example.com"
    pull_secret_ref: "vault://foundry/{id}/registry-creds"
```

## Setting cascade

| Level | Who sets | What |
|-------|----------|------|
| **Platform Admin** | Platform-wide defaults | Fallback cluster endpoint, default resource limits, base image registry |
| **Foundry Admin** | Foundry-specific overrides | Cluster endpoint, credentials, ingress domain, quotas |
| **Workshop/Workbench** | — | Cannot override cluster config (security boundary) |

Platform defaults apply when a Foundry has not configured `workspace_infrastructure.kubernetes.endpoint`.

## Validation

The Validation module validates `workspace_infrastructure` before Foundry merge:

| Check | Requirement |
|-------|-------------|
| Endpoint reachable | TCP/TLS handshake to `kubernetes.endpoint` |
| Credentials valid | Auth succeeds against cluster API |
| Namespace permission | Identity can create namespace or target namespace exists |
| StorageClass exists | Named `storage_class` available in cluster |
| Ingress domain resolvable | DNS lookup for `*.sessions.{ingress_domain}` (warning if fails) |

Validation failure blocks merge to Foundry Definition Repo.

## Storage and sync

| Store | Role |
|-------|------|
| **Foundry Definition Repo** | Source of truth — `foundry.yaml` with `workspace_infrastructure` block |
| **Metadata Service** | Synced copy queried by Session Infrastructure at provision time |
| **Session Infrastructure cache** | In-memory kubeconfig per Foundry; invalidated on Metadata change events |

Session Infrastructure does **not** store cluster credentials in its own database — resolves from vault reference on each provision request.

## Foundry admin workflow

```
Foundry Admin
    │
    ├── Provision K8s cluster (customer-managed)
    │
    ├── Create service account with namespace-scoped RBAC
    │
    ├── Store credentials in vault; reference in foundry.yaml
    │
    ├── Configure wildcard DNS: *.sessions.{domain} → ingress
    │
    ├── Merge foundry.yaml to Foundry Definition Repo
    │
    └── Validation runs → Session Infrastructure can provision
```

## Platform admin workflow

Platform Admin sets platform-wide defaults in platform config (not per-Foundry):

```yaml
platform_defaults:
  workspace_infrastructure:
    image_registry:
      url: "registry.platform.foundry.io"
    resource_defaults:
      cpu_request: "2"
      cpu_limit: "4"
      memory_request: "4Gi"
      memory_limit: "8Gi"
      storage_size: "20Gi"
```

Foundry admin overrides any field in their `foundry.yaml`.

## Security boundaries

| Rule | Rationale |
|------|-----------|
| Workshop cannot set cluster endpoint | Prevents arbitrary cluster access from Workshop repos |
| Workbench cannot override ingress domain | Session URL integrity |
| Credentials via vault reference only | No secrets in git |
| Foundry admin role required | Cluster access is org-level decision |

## Related documentation

- [kubernetes-integration.md](kubernetes-integration.md) — How WSI consumes config
- [../../management/platform-developer-guide/foundry-management/README.md](../../management/platform-developer-guide/foundry-management/README.md) — Foundry settings model
- [../user-guide/customizing-workspace-images.md](../user-guide/customizing-workspace-images.md) — Admin overlay (separate from cluster config)
