# Networking

Session URL generation, TLS termination, DNS naming, WebSocket support, and internal communication boundaries.

## URL scheme

Each active session receives a deterministic HTTPS URL:

```
https://{session-id}.sessions.{ingress-domain}
```

Example: `https.sessions.foundry.example.com` with session `sess-abc123`:

```
https://sess-abc123.sessions.foundry.example.com
```

**WSI-FR-0008:** URLs are unique per session and deterministic from `session_id` + `ingress_domain`.

**WSI-NFR-0002:** URL accessible within 10 seconds of pod readiness.

## Routing architecture

Session Infrastructure uses **Coder's built-in wildcard proxy** rather than per-session Ingress objects:

```
User browser
    │
    ▼
*.sessions.foundry.example.com  (wildcard DNS → Coder proxy / ingress controller)
    │
    ▼
Coder proxy (routes by workspace name = session-id)
    │
    ▼
Pod Service svc-session-{session-id}:8080
    │
    ▼
code-server (port 8080)
```

| Aspect | Design |
|--------|--------|
| **DNS** | Wildcard A record `*.sessions.{ingress-domain}` → ingress controller |
| **TLS** | Wildcard cert via cert-manager ClusterIssuer; one cert covers all sessions |
| **Routing** | Coder proxy maps hostname to workspace pod |
| **Ingress count** | Zero per-session Ingress objects when using Coder proxy |
| **Fallback** | Without Coder: single wildcard Ingress + ExternalDNS service discovery |

→ [design-discussions/architecture-choices.md](design-discussions/architecture-choices.md) — Wildcard subdomain decision

## TLS termination

**WSI-FR-0011:** All session URLs terminate TLS at the ingress/proxy layer.

```yaml
# Wildcard certificate (cluster-level, not per-session)
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: sessions-wildcard
  namespace: foundry-{foundry-id}-sessions
spec:
  secretName: tls-sessions-wildcard
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
  dnsNames:
    - "*.sessions.foundry.example.com"
    - "sessions.foundry.example.com"
```

Foundry admin configures `workspace_infrastructure.kubernetes.tls.issuer` to select the ClusterIssuer.

## WebSocket support

Code Server and IDE extensions require long-lived WebSocket connections. Ingress/proxy annotations:

```yaml
annotations:
  nginx.ingress.kubernetes.io/proxy-read-timeout: "3600"
  nginx.ingress.kubernetes.io/proxy-send-timeout: "3600"
  nginx.ingress.kubernetes.io/proxy-http-version: "1.1"
  nginx.ingress.kubernetes.io/upstream-hash-by: "$host"
```

When using Coder's proxy, equivalent timeout settings are configured in Coder's ingress template.

## Internal communication

Ports and exposure boundaries:

| Port | Service | External exposure |
|------|---------|-------------------|
| **8080** | Code Server | Yes — via session URL |
| **9090** | WO Runtime API | No — pod-internal and cluster-internal only |
| **—** | Capable Agent processes | No — localhost only |

WO Runtime reaches the management plane (Session Management, Orchestrator events) via **cluster-external HTTPS endpoints** — not through the session URL.

NetworkPolicy allows egress to:
- Platform API endpoints (Session Management, Metadata Service, Agent Fabric)
- Skill Registry, container registry
- LLM gateway (via Access Gateway)
- Jira MCP (if configured)

Denies egress to other Foundry session namespaces (WSI-NFR-0003).

## Per-session Service

Even with Coder proxy, each pod has a ClusterIP Service for routing:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: "svc-session-{session-id}"
  namespace: "foundry-{foundry-id}-sessions"
spec:
  selector:
    foundry.io/session-id: "{session-id}"
  ports:
    - port: 8080
      targetPort: 8080
      name: code-server
```

Coder's proxy resolves workspace name to this Service.

## Fallback: per-session Ingress

If Coder proxy is unavailable, Session Infrastructure can create per-session Ingress resources:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: "session-{session-id}"
  namespace: "foundry-{foundry-id}-sessions"
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "3600"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "3600"
spec:
  ingressClassName: nginx
  tls:
    - hosts: ["{session-id}.sessions.foundry.example.com"]
      secretName: "tls-session-{session-id}"
  rules:
    - host: "{session-id}.sessions.foundry.example.com"
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: "svc-session-{session-id}"
                port:
                  number: 8080
```

This path is documented for escape hatch only — production deployments use Coder proxy to avoid thousands of Ingress objects.

## Related documentation

- [coder-on-kubernetes.md](coder-on-kubernetes.md) — Coder proxy configuration
- [multi-tenant-isolation.md](multi-tenant-isolation.md) — NetworkPolicy rules
- [requirements.md](requirements.md) — WSI-FR-0008, WSI-FR-0011, WSI-NFR-0002, WSI-NFR-0003
