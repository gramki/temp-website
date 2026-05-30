# Kubernetes Integration

How Workspace Session Infrastructure connects to Foundry-admin-provided Kubernetes clusters.

## Cluster ownership model

The platform does **not** provision Kubernetes clusters. Each Foundry admin provides cluster connectivity in Foundry settings. Session Infrastructure consumes that configuration at provision time via the Metadata Service.

```
Foundry Admin
    │
    ├── Configures workspace_infrastructure.kubernetes in foundry.yaml
    │
    └── Validation module verifies endpoint reachability and RBAC
            │
            ▼
    Metadata Service (synced from Foundry Definition Repo)
            │
            ▼
    Session Infrastructure (queries config per provision request)
            │
            └── Creates resources in foundry-{id}-sessions namespace
```

## Configuration source

Cluster config is a top-level Foundry setting. See [foundry-management-integration.md](foundry-management-integration.md) for the full schema.

Session Infrastructure reads:

| Field | Usage |
|-------|-------|
| `kubernetes.endpoint` | API server URL |
| `kubernetes.auth` | Authentication method and credentials reference |
| `kubernetes.namespace_prefix` | Base namespace name (default: `foundry-{id}-sessions`) |
| `kubernetes.storage_class` | PVC StorageClass |
| `kubernetes.ingress_class` | Ingress class (informational — Coder proxy handles routing) |
| `kubernetes.ingress_domain` | Base domain for session URLs |
| `kubernetes.tls.issuer` | cert-manager ClusterIssuer for wildcard cert |
| `image_registry` | Base image pull location and secret |
| `resource_defaults` | CPU, memory, storage defaults |

## Authentication

Session Infrastructure supports three authentication modes against the cluster API:

| Type | Use case | Credential storage |
|------|----------|-------------------|
| **service-account** | Dedicated SA with namespace-scoped RBAC | `credentials_ref: vault://foundry/{id}/k8s-creds` |
| **oidc** | Enterprise identity federation | OIDC token exchange; short-lived tokens |
| **certificate** | Legacy or air-gapped clusters | Client cert + key in vault reference |

Credentials are resolved at runtime from the configured vault reference — never stored in Session Infrastructure's database or logs.

Required RBAC permissions for the provisioner identity:

```yaml
# Minimum Role in foundry-{id}-sessions namespace
rules:
  - apiGroups: [""]
    resources: ["pods", "services", "persistentvolumeclaims", "configmaps", "secrets"]
    verbs: ["create", "get", "list", "watch", "update", "delete"]
  - apiGroups: ["networking.k8s.io"]
    resources: ["ingresses"]
    verbs: ["create", "get", "list", "watch", "delete"]  # Only if not using Coder proxy
```

Namespace creation requires a ClusterRole binding if the namespace does not yet exist (WSI-FR-0007).

## Kubeconfig management

Session Infrastructure maintains an in-memory kubeconfig per Foundry, refreshed on credential rotation:

1. Resolve `foundry_id` from provision request
2. Fetch `workspace_infrastructure` block from Metadata Service
3. Resolve credentials from vault reference
4. Build REST config with appropriate auth provider
5. Verify connectivity with a lightweight `GET /api/v1/namespaces/{namespace}` before provisioning

Kubeconfig is **not** persisted to disk. Credential rotation triggers cache invalidation via Metadata Service change events.

## Multi-cluster routing

Each Foundry maps to exactly one cluster endpoint. Platform-wide fallback cluster (set by Platform Admin) applies only when a Foundry has not configured its own endpoint.

Session Infrastructure does not implement cross-cluster session migration — a session's PVC and pod are bound to the cluster where it was created.

## Coder cluster registration

Coder's workspace provisioner is registered against the same cluster endpoint. Session Infrastructure ensures Coder's Kubernetes provider credentials match the provisioner identity or a dedicated Coder service account with equivalent permissions.

→ [coder-on-kubernetes.md](coder-on-kubernetes.md) — Coder-specific configuration

## Validation requirements

Before a Foundry merge is accepted, Validation module checks (extends WSI-FR-0001):

| Check | Failure action |
|-------|----------------|
| Endpoint reachable | Block merge; surface error to Foundry admin |
| Credentials valid | Block merge |
| Namespace-creation permission | Block merge if auto-provision required |
| StorageClass exists | Warn if missing; block if strict mode |
| Wildcard DNS resolves to ingress | Warn at provision time if lookup fails |

## Related documentation

- [foundry-management-integration.md](foundry-management-integration.md) — Settings schema and cascade
- [multi-tenant-isolation.md](multi-tenant-isolation.md) — Namespace and RBAC setup
- [requirements.md](requirements.md) — WSI-FR-0001, WSI-FR-0006, WSI-FR-0007
