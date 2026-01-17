# Cipher IAM — Infrastructure Integration

> **Status:** 🔴 Stub — Placeholder for expansion

## Overview

**Cipher** is Zeta's Identity and Access Management (IAM) platform that provides identity, authentication, authorization, and audit services for Olympus Hub. This document covers the infrastructure integration aspects; for subsystem-level integration, see [Cipher IAM Subsystem](../04-subsystems/supporting-systems/cipher-iam.md).

---

## Purpose in Olympus Hub

Cipher provides:

- **Identity Management** — User, service, and agent identities
- **Authentication** — JWT, OIDC, SAML, mTLS authentication
- **Authorization** — Role-based and attribute-based access control
- **Audit** — Comprehensive audit logging service
- **Workload Identity** — SPIFFE/SPIRE for service identity

---

## SPIFFE/SPIRE Integration

### SPIFFE (Secure Production Identity Framework for Everyone)

SPIFFE provides cryptographic identity to every workload:

- **SPIFFE ID** — Unique identity URI (e.g., `spiffe://olympus.hub/workload/signal-exchange`)
- **SVID** — SPIFFE Verifiable Identity Document (X.509 or JWT)

### SPIRE (SPIFFE Runtime Environment)

SPIRE is the reference implementation:

- **SPIRE Server** — Issues and manages SVIDs
- **SPIRE Agent** — Runs on each node, attests workloads
- **Workload API** — SDK for applications to obtain SVIDs

---

## Identity Types

### Service Identity

Every Hub service receives a SPIFFE identity:

```
spiffe://olympus.hub/service/<namespace>/<service-name>
```

Examples:
- `spiffe://olympus.hub/service/hub-core/signal-exchange`
- `spiffe://olympus.hub/service/hub-runtime/atlantis`

### Application Identity

Hub Applications receive delegated identities:

```
spiffe://olympus.hub/app/<tenant-id>/<workbench-id>/<app-name>
```

### Agent Identity (Bot Identity)

Autonomous agents have **two-layer identity**:

#### 1. Deployment Identity (SPIFFE)

Infrastructure-level identity of the running agent pod:

```
spiffe://olympus.hub/seer/tenant/<tenant-id>/workbench/<workbench-id>/agent/<agent-id>
```

- **Purpose**: mTLS, service mesh authentication (infrastructure-level)
- **OAuth Analogy**: OAuth Client — proves "this request is coming from this specific agent deployment"
- **Provisioned by**: SPIRE Agent during pod startup
- **Lifetime**: Tied to deployment lifecycle (created on deploy, rotated hourly, revoked on undeploy)

#### 2. Agent Persona

Business-level identity derived from Scenario:

- **Source**: Scenario provides the agent's human-like personality and business role
- **Storage**: Registered in Cipher IAM (Scenario references it)
- **Purpose**: Business identity for app-to-app interactions, authority delegation, audit attribution
- **Lifetime**: Tied to Scenario lifecycle (survives redeployments)
- **OAuth Analogy**: OAuth Principal — the business entity on whose behalf actions are taken

**Identity Relationship**:
```
Scenario
    │
    │ defines
    ▼
Agent Persona (business identity)
    │
    │ is deployed as
    ▼
Employed Agent Instance
    │
    │ has
    ▼
Deployment Identity (SPIFFE)
```

**Delegation Access Tokens** include both identities:
- `client_id`: Deployment Identity (SPIFFE)
- `sub`: Agent Persona (business identity)
- `delegated_by`: Source of authority (Scenario Profile or Business User)

> **See**: [ADR-0129: Agent Identity Model](../decision-logs/0129-agent-identity-model.md) for the complete two-layer identity model.

---

## Authentication Flows

### Service-to-Service (mTLS)

```
┌─────────────┐                    ┌─────────────┐
│  Service A  │──── mTLS + SVID ───│  Service B  │
│  (X.509)    │                    │  (X.509)    │
└─────────────┘                    └─────────────┘
```

### User Authentication

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    User     │────►│   Heracles  │────►│   Cipher    │
│             │     │  (Gateway)  │     │   (OIDC)    │
└─────────────┘     └─────────────┘     └─────────────┘
                          │
                          ▼
                    JWT with claims
```

### Tool Authorization

For tool providers requiring user delegation:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  mcp-orch   │────►│   Cipher    │────►│   User      │
│             │     │  (consent)  │     │  (approval) │
└─────────────┘     └─────────────┘     └─────────────┘
        │
        ▼
  X-Tool-Authorization JWT
```

---

## Domain Architecture

### Publisher Domain (Zeta)

- Hub System users (SRE, Customer Success)
- Platform services
- Managed by Zeta

### Tenant Domains

- Tenant-specific users and groups
- Workbench access controls
- Managed by Tenant Administrators

---

## JWT Claims

Standard claims in Hub JWTs:

| Claim | Description |
|-------|-------------|
| `sub` | Subject identifier |
| `aud` | Audience (service) |
| `iss` | Issuer (Cipher) |
| `tenant_id` | Tenant identifier |
| `roles` | Assigned roles |
| `scope` | Authorization scopes |
| `session_id` | Authentication session |

---

## Audit Service Integration

Cipher's Audit Service captures:

- **Authentication events** — Login, logout, token refresh
- **Authorization decisions** — Access grants and denials
- **Administrative actions** — User/role management
- **API access** — Resource access logs

Hub services integrate via:
- Cipher Audit SDK
- Async audit event submission
- Structured audit payloads

---

## High Availability

- **Multi-region deployment** — Active-active Cipher clusters
- **Token caching** — Local JWKS caching at gateways
- **Graceful degradation** — Offline token validation
- **Certificate rotation** — Automated SVID rotation

---

## Related Documentation

- [Cipher IAM Subsystem](../04-subsystems/supporting-systems/cipher-iam.md) — Subsystem integration
- [User Management](../04-subsystems/user-management/README.md) — User personas and scopes
- [Domain Management](../04-subsystems/user-management/domain-management.md) — Publisher and Tenant domains
- [MCP Router](./mcp-orchestrator.md) — Tool authorization flows

---

## References

- [SPIFFE Specification](https://spiffe.io/)
- [SPIRE Documentation](https://spiffe.io/docs/latest/spire-about/)

---

*Expand this document with deployment topology, certificate management, and disaster recovery procedures.*

