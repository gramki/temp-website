# Foundry Management Integration

How `workspace_infrastructure` configuration integrates with the Foundry settings model.

## Settings placement

`workspace_infrastructure` is a **new top-level Foundry setting** alongside existing `identity`, `agents`, and `integrations` blocks in the Foundry Definition Repository.

| Aspect | Detail |
|--------|--------|
| **Set by** | Foundry Admin (not Platform Admin) |
| **Storage** | `foundry.yaml` in Foundry Definition Repo → Metadata Service |
| **Validation** | Validation module before merge |
| **Consumer** | Session Infrastructure at provision time |

Each Foundry brings its own Kubernetes cluster. The platform does not provision clusters.

## Configuration schema

```yaml
# foundry.yaml — top-level Foundry setting
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
  image_registry:
    url: "registry.foundry.example.com"
    pull_secret_ref: "vault://foundry/{id}/registry-creds"
```

### Field reference

| Field | Required | Description |
|-------|----------|-------------|
| `kubernetes.endpoint` | Yes | Kubernetes API server URL |
| `kubernetes.auth.type` | Yes | Authentication method |
| `kubernetes.auth.credentials_ref` | Yes | Vault reference for credentials |
| `kubernetes.namespace_prefix` | No | Default: `foundry-{id}-sessions` |
| `kubernetes.storage_class` | Yes | StorageClass for session PVCs |
| `kubernetes.ingress_class` | No | Informational when using Coder proxy |
| `kubernetes.ingress_domain` | Yes | Base domain for session URLs |
| `kubernetes.tls.issuer` | Yes | cert-manager ClusterIssuer for wildcard cert |
| `resource_defaults.*` | No | Per-pod defaults; platform defaults apply if omitted |
| `image_registry.url` | Yes | Container registry for base image |
| `image_registry.pull_secret_ref` | Yes | Vault reference for registry credentials |

## Setting cascade

| Level | Who sets | What |
|-------|----------|------|
| **Platform Admin** | Platform-wide defaults | Fallback cluster endpoint, default resource limits, platform registry |
| **Foundry Admin** | Foundry-specific overrides | Cluster endpoint, namespace, ingress domain, quotas |
| **Workshop/Workbench** | — | **Cannot override** cluster config (security boundary) |

Foundry Admin settings override Platform Admin defaults. Workshop and Workbench definitions cannot specify cluster endpoints — session infrastructure is a Foundry-level concern.

## Validation requirements

The Validation module checks before Foundry merge is accepted:

| Check | Requirement | Failure action |
|-------|-------------|----------------|
| Endpoint reachable | TCP/TLS connect to API server | Block merge |
| Credentials valid | Authenticated API call succeeds | Block merge |
| Namespace creation permission | Provisioner can create namespace | Block merge if auto-provision required |
| StorageClass exists | Named StorageClass present in cluster | Warn; block in strict mode |
| Wildcard DNS | `*.sessions.{domain}` resolves | Warn at provision time |
| Resource quota feasible | Requested limits fit cluster capacity | Warn |

Validation uses the same credentials Session Infrastructure will use at runtime.

## Metadata Service sync

```
Foundry Definition Repo (foundry.yaml)
    │
    ├── Merge to main
    │
    ├── Validation module checks workspace_infrastructure
    │
    └── Metadata Service syncs settings
            │
            ▼
    Session Infrastructure reads on provision:
    GET /api/v1/foundries/{foundry-id}/settings/workspace_infrastructure
```

Session Infrastructure caches settings per Foundry. Metadata Service change events invalidate the cache.

Credential references are resolved at runtime from vault — never stored in Metadata Service or Session Infrastructure database.

## Relationship to session_management settings

Session lifecycle policies (idle timeout, max lifetime) are configured separately under `session_management` and consumed by Session Management — not Session Infrastructure.

| Setting block | Consumer | Scope |
|---------------|----------|-------|
| `workspace_infrastructure` | Session Infrastructure | K8s cluster, images, storage, networking |
| `session_management` | Session Management | Idle timeout, max lifetime, multi-session policy |

## Platform Admin fallback cluster

Platform Admin may configure a platform-wide fallback cluster for Foundries that have not yet configured their own endpoint:

```yaml
# Platform settings (not foundry.yaml)
platform_defaults:
  workspace_infrastructure:
    kubernetes:
      endpoint: "https://platform-k8s.example.com:6443"
      # ...
```

Fallback applies only when a Foundry's `workspace_infrastructure.kubernetes.endpoint` is absent. Production Foundries should always configure their own cluster.

## Related documentation

- [kubernetes-integration.md](kubernetes-integration.md) — How Session Infrastructure consumes config
- [multi-tenant-isolation.md](multi-tenant-isolation.md) — Namespace and quota setup
- [requirements.md](requirements.md) — WSI-FR-0001, WSI-FR-0006, WSI-FR-0007
- [../../management/platform-developer-guide/](../../management/platform-developer-guide/) — Foundry settings model
