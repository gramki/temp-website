# Domain Management

> **Status:** 🔴 Stub — Placeholder for expansion

Domain Management defines how user domains are organized across the Hub system, from the Publisher Domain to Tenant Domains.

---

## Overview

| Aspect | Description |
|--------|-------------|
| **Purpose** | Organize and isolate user populations |
| **Publisher Domain** | Hub system operators (Zeta) |
| **Tenant Domains** | Tenant-specific user populations |
| **IAM** | All domains managed through Cipher |

---

## Domain Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                     PUBLISHER DOMAIN                             │
│                        (Zeta)                                    │
│                                                                  │
│   Identity Provider: Zeta Corporate IdP                         │
│   Users: SREs, Customer Success Executives                      │
│   Isolation: Complete isolation from tenant data                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ (Manages)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     TENANT DOMAIN(S)                             │
│                                                                  │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                  Tenant: Acme Bank                       │   │
│   │                                                          │   │
│   │   ┌─────────────────┐  ┌─────────────────────────────┐  │   │
│   │   │ Corporate Domain│  │    Customer Domain          │  │   │
│   │   │                 │  │                             │  │   │
│   │   │ • Admins        │  │ • Self-Serve Customers     │  │   │
│   │   │ • Architects    │  │                             │  │   │
│   │   │ • Developers    │  │                             │  │   │
│   │   │ • Auditors      │  │                             │  │   │
│   │   │ • Agents        │  │                             │  │   │
│   │   │ • Supervisors   │  │                             │  │   │
│   │   └─────────────────┘  └─────────────────────────────┘  │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                  │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                  Tenant: Beta Insurance                  │   │
│   │                                                          │   │
│   │   ┌─────────────────────────────────────────────────┐   │   │
│   │   │           Single Domain (Unified)                │   │   │
│   │   │                                                  │   │   │
│   │   │ • All tenant personas in one domain             │   │   │
│   │   │ • Includes customer self-serve users            │   │   │
│   │   └─────────────────────────────────────────────────┘   │   │
│   └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Publisher Domain

The **Publisher Domain** is exclusively for Zeta (the creator of Olympus Hub):

| Aspect | Description |
|--------|-------------|
| **Owner** | Zeta |
| **Identity Provider** | Zeta's corporate IdP |
| **Users** | SRE, Customer Success Executive |
| **Isolation** | Complete isolation from tenant operations |
| **Cross-Tenant Access** | For support purposes only, fully audited |

### Publisher Domain Configuration

```yaml
domain:
  id: "publisher"
  name: "Zeta Publisher Domain"
  type: "publisher"
  
  identity_provider:
    type: "corporate_idp"
    provider: "zeta-okta"
    
  users:
    - persona: "sre"
      group: "hub-sre-team"
    - persona: "customer_success"
      group: "hub-cs-team"
      
  isolation:
    access_tenant_data: false
    access_tenant_config: true  # For support
    cross_tenant_audit: required
```

---

## Tenant Domains

Tenants have flexibility in organizing their domains:

### Pattern 1: Single Domain

All tenant personas in one domain:

```yaml
tenant_domains:
  - domain_id: "acme-unified"
    tenant_id: "acme-bank"
    type: "unified"
    
    identity_provider:
      type: "federated"
      provider: "acme-azure-ad"
      
    personas:
      - administrators
      - process_architects
      - developers
      - auditors
      - agents
      - supervisors
      - customers
```

### Pattern 2: Separated Domains

Different domains for different user groups:

```yaml
tenant_domains:
  - domain_id: "acme-corporate"
    tenant_id: "acme-bank"
    type: "corporate"
    
    identity_provider:
      type: "federated"
      provider: "acme-azure-ad"
      
    personas:
      - administrators
      - process_architects
      - developers
      - auditors
      - agents
      - supervisors
      
  - domain_id: "acme-customers"
    tenant_id: "acme-bank"
    type: "customer"
    
    identity_provider:
      type: "federated"
      provider: "acme-customer-auth"
      
    personas:
      - customers
```

### Pattern 3: Multi-Domain

Complex organizations with multiple internal domains:

```yaml
tenant_domains:
  - domain_id: "acme-it"
    type: "internal"
    personas: [administrators, developers]
    
  - domain_id: "acme-ops"
    type: "internal"
    personas: [process_architects, agents, supervisors]
    
  - domain_id: "acme-compliance"
    type: "internal"
    personas: [auditors]
    
  - domain_id: "acme-customers"
    type: "customer"
    personas: [customers]
```

---

## Domain Isolation

| Isolation Level | Description |
|-----------------|-------------|
| **Publisher ↔ Tenant** | Complete isolation, no operational data access |
| **Tenant ↔ Tenant** | Complete isolation, no cross-tenant visibility |
| **Domain ↔ Domain (within tenant)** | Configurable, typically workbench-scoped |

---

## Federation Support

| Protocol | Support |
|----------|---------|
| **SAML 2.0** | Full support |
| **OIDC** | Full support |
| **SCIM** | User provisioning |

---

## Related Documentation

- [User Management Overview](./README.md)
- [Cipher IAM](../supporting-systems/cipher-iam.md)
- [Subscription Management](../subscription-management/README.md)

---

*TODO: Detailed design — federation configuration, cross-domain permissions, domain lifecycle*

