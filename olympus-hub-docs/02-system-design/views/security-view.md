# Security View

> **How the system is secured**

---

## Audience

- Security Architects
- Auditors
- Compliance Officers

---

## Overview

This view presents the security architecture of Olympus Hub, covering identity and access management, data protection, audit capabilities, and compliance considerations.

---

## Security Layers

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         SECURITY LAYERS                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   PERIMETER                                                                  │
│   ─────────                                                                  │
│   • WAF, DDoS protection                                                     │
│   • TLS termination                                                          │
│   • Rate limiting                                                            │
│                                                                              │
│   AUTHENTICATION                                                             │
│   ──────────────                                                             │
│   • Human: SSO (SAML/OIDC) via Cipher IAM                                   │
│   • AI Agent: SPIFFE identity                                                │
│   • Machine: mTLS, API keys                                                  │
│                                                                              │
│   AUTHORIZATION                                                              │
│   ─────────────                                                              │
│   • Human: RBAC scoped to Workbenches                                        │
│   • AI Agent: Fine-grained entity/action permissions                         │
│   • Cross-agent: Delegation with explicit consent                            │
│                                                                              │
│   DATA PROTECTION                                                            │
│   ───────────────                                                            │
│   • Encryption at rest (AES-256)                                            │
│   • Encryption in transit (TLS 1.3)                                          │
│   • Tenant/Subscription/Workbench isolation                                  │
│                                                                              │
│   AUDIT                                                                      │
│   ─────                                                                      │
│   • Complete action audit trail                                              │
│   • Decision records (Cognitive Audit Fabric)                                │
│   • Evidence bundles for AI decisions                                        │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Identity and Access Management

### Human Agent IAM

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  HUMAN AGENT IAM                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   AUTHENTICATION                          AUTHORIZATION                      │
│   ──────────────                          ─────────────                      │
│                                                                              │
│   Enterprise IdP                          Cipher IAM                         │
│        │                                       │                             │
│        │ SAML/OIDC                            │ RBAC                         │
│        ▼                                       ▼                             │
│   ┌───────────────┐                     ┌───────────────────────────────┐   │
│   │ Cipher IAM    │                     │ Permissions scoped to:         │   │
│   │               │                     │   • Tenant                     │   │
│   │ • SSO         │                     │   • Subscription               │   │
│   │ • Session     │                     │   • Workbench                  │   │
│   │ • MFA         │                     │   • Scenario                   │   │
│   └───────────────┘                     └───────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### AI Agent IAM

| Aspect | Mechanism |
|--------|-----------|
| **Identity** | SPIFFE-based workload identity |
| **Authentication** | mTLS with SPIFFE ID |
| **Authorization** | Fine-grained permissions per entity/action |
| **Tool Access** | OAuth-like consent flows |
| **Secrets** | Secure vault, short-lived tokens |

### Cross-Agent Authorization

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Delegation** | Human grants specific permissions to AI | "Process disputes under $100" |
| **Impersonation** | AI acts on behalf with consent | Customer service scenarios |
| **Scope Limiting** | Time or entity bounded | "This session only" |

---

## Multi-Tenancy Isolation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ISOLATION BOUNDARIES                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   TENANT BOUNDARY (Strongest)                                                │
│   ───────────────────────────                                                │
│   • Separate IAM configuration                                               │
│   • Separate credentials                                                     │
│   • No cross-tenant data access                                              │
│                                                                              │
│   SUBSCRIPTION BOUNDARY                                                      │
│   ─────────────────────                                                      │
│   • Separate container registries                                            │
│   • Separate Git repositories                                                │
│   • Separate credentials                                                     │
│   • No credential sharing between DEV and PROD                               │
│                                                                              │
│   WORKBENCH BOUNDARY                                                         │
│   ──────────────────                                                         │
│   • Separate data stores                                                     │
│   • No direct cross-workbench data access                                    │
│   • Explicit "Workbench as Machine" for integration                          │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Audit and Compliance

### Audit Trail

| Layer | What's Audited |
|-------|----------------|
| **Access** | All authentication events, failed attempts |
| **Configuration** | All CRD changes (Git history) |
| **Operations** | All requests, tasks, decisions |
| **Data** | Access to sensitive entities |

### Cognitive Audit Fabric (CAF)

For AI decision auditability:

| Component | Purpose |
|-----------|---------|
| **Decision Records** | Complete record of AI decisions |
| **Evidence Bundles** | Context used for decision |
| **Explanation Service** | Human-readable explanation |
| **Compliance Reporting** | Regulatory audit support |

---

## Data Protection

### Encryption

| Scope | Mechanism |
|-------|-----------|
| **At Rest** | AES-256, customer-managed keys optional |
| **In Transit** | TLS 1.3 everywhere |
| **Secrets** | HashiCorp Vault or equivalent |

### Data Classification

| Classification | Handling |
|----------------|----------|
| **PII** | Encrypted, access-logged, retention policies |
| **Sensitive Business** | Encrypted, role-restricted |
| **Operational** | Standard protection |

---

## Credential Management

| Credential Type | Management |
|-----------------|------------|
| **User passwords** | Enterprise IdP (not Hub) |
| **API keys** | Cipher IAM, rotatable |
| **AI Agent tokens** | Short-lived, automatically rotated |
| **Machine certificates** | mTLS, automated renewal |

---

## Compliance Considerations

| Requirement | How Hub Addresses |
|-------------|-------------------|
| **SOC 2** | Audit trails, access controls, encryption |
| **GDPR** | Data isolation, consent management, CAF |
| **PCI-DSS** | Encryption, access controls, audit logs |
| **Industry Regs** | CAF for decision explainability |

---

## Related Documentation

- [Cognitive Audit Fabric](../implementation-concepts/cognitive-audit-fabric.md)
- [Persona](../implementation-concepts/persona.md)
- [Subscription](../implementation-concepts/subscription.md)

