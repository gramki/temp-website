# Multi-Tenant Isolation

Namespace-per-Foundry model, NetworkPolicies, RBAC, pod security standards, and resource quotas.

## Isolation model

Each Foundry's sessions run in a dedicated Kubernetes namespace. Cross-Foundry traffic is denied by default — zero-trust network boundaries.

```
Cluster
├── foundry-acme-sessions/          ← Foundry "acme"
│   ├── session pods, PVCs, Services
│   └── NetworkPolicy: deny cross-namespace
│
├── foundry-globex-sessions/        ← Foundry "globex"
│   └── (isolated)
│
└── coder-system/                   ← Coder proxy (platform-managed)
```

**WSI-FR-0007:** Session Infrastructure creates the namespace if it does not exist and applies NetworkPolicies and RBAC.

**WSI-NFR-0003:** Cross-Foundry network traffic blocked by NetworkPolicy.

## Namespace provisioning

Namespace name follows `workspace_infrastructure.kubernetes.namespace_prefix`:

```
foundry-{foundry-id}-sessions
```

On first provision request for a Foundry:

1. Check namespace exists (`GET /api/v1/namespaces/{name}`)
2. Create if missing with labels: `foundry.io/foundry-id`, `foundry.io/managed-by: session-infrastructure`
3. Apply namespace-scoped resources: NetworkPolicy, ResourceQuota, Role, RoleBinding, ServiceAccount
4. Create image pull Secret from `image_registry.pull_secret_ref`

Namespace creation requires ClusterRole permission for the provisioner identity — validated at Foundry merge time.

## NetworkPolicy

Default-deny with explicit allowlist:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: session-isolation
  namespace: foundry-{foundry-id}-sessions
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
  ingress:
    # Allow from Coder proxy / ingress controller only
    - from:
        - namespaceSelector:
            matchLabels:
              foundry.io/component: coder-proxy
      ports:
        - protocol: TCP
          port: 8080
  egress:
    # Platform APIs (Session Management, Metadata Service, Agent Fabric)
    - to:
        - ipBlock:
            cidr: 0.0.0.0/0    # Restricted to platform API CIDRs in production
      ports:
        - protocol: TCP
          port: 443
    # DNS
    - to:
        - namespaceSelector: {}
      ports:
        - protocol: UDP
          port: 53
    # Container registry, Skill Registry
    - ports:
        - protocol: TCP
          port: 443
```

| Traffic | Policy |
|---------|--------|
| Ingress from other Foundry namespaces | **Denied** |
| Ingress from Coder proxy to port 8080 | **Allowed** |
| Egress to platform HTTPS APIs | **Allowed** |
| Egress to other session namespaces | **Denied** |
| WO Runtime port 9090 | **Not exposed externally** |

## RBAC

ServiceAccount per session pod with namespace-scoped Role:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: session-pod-sa
  namespace: foundry-{foundry-id}-sessions
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: session-pod-role
  namespace: foundry-{foundry-id}-sessions
rules:
  # Session pods do not need K8s API access in normal operation
  - apiGroups: [""]
    resources: ["configmaps"]
    resourceNames: ["foundry-session-config"]
    verbs: ["get"]
```

Session Infrastructure's provisioner identity (separate from pod SA) holds the create/delete permissions documented in [kubernetes-integration.md](kubernetes-integration.md).

## Pod security

Session pods run under the **Restricted** pod security standard:

| Control | Setting |
|---------|---------|
| Privileged containers | Not allowed |
| Root filesystem | Read-only (except `/workspace` mount) |
| Run as non-root | Required |
| Capabilities | All dropped |
| seccomp | RuntimeDefault |
| Host namespaces | Not shared |

The single `workspace` container runs supervisord as a non-root user. Writable paths are limited to `/workspace` (PVC) and `/tmp`.

## Resource quotas

**WSI-NFR-0007:** Concurrent sessions per Foundry limited by namespace ResourceQuota.

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: session-resource-quota
  namespace: foundry-{foundry-id}-sessions
spec:
  hard:
    pods: "50"                          # max concurrent sessions
    requests.cpu: "100"
    requests.memory: "200Gi"
    limits.cpu: "200"
    limits.memory: "400Gi"
    persistentvolumeclaims: "50"
    requests.storage: "1000Gi"
```

Foundry admin may request quota increases. Platform Admin sets ceiling per cluster capacity.

**WSI-FR-0012:** Per-pod resource limits (CPU, memory) are applied per workspace type and must fit within namespace quota.

## Image pull isolation

Private registry credentials are scoped to the Foundry namespace:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: registry-pull-secret
  namespace: foundry-{foundry-id}-sessions
type: kubernetes.io/dockerconfigjson
```

Only Session Infrastructure and session pods in that namespace can pull from the configured registry.

## Related documentation

- [kubernetes-integration.md](kubernetes-integration.md) — Provisioner RBAC requirements
- [networking.md](networking.md) — Internal port boundaries
- [pod-lifecycle.md](pod-lifecycle.md) — Pod security context in spec
- [storage.md](storage.md) — Storage quota
- [requirements.md](requirements.md) — WSI-FR-0007, WSI-FR-0012, WSI-NFR-0003, WSI-NFR-0007
