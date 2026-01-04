# Environment Registry

> **Status:** 🔴 Stub — Placeholder for expansion

The Environment Registry catalogs **Environments and Sandboxes**—the contexts in which operations execute and agents operate.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Define and manage operational environments |
| **Contents** | Environment definitions, sandbox configurations |
| **Scope** | Tenant-specific environment definitions |
| **Integration** | Workbenches, Cipher IAM, Automation Runtimes |

---

## What is an Environment?

From the ontology:

> An Environment is a bounded operational context that contains Machines, defines access policies, and scopes agent authority.

---

## Environment Schema

```yaml
environment:
  # Identity
  id: string
  name: string
  type: enum  # production | staging | uat | development | sandbox
  
  # Description
  display_name: string
  description: string
  
  # Machines
  machines:
    - machine_id: string
      connection_profile: string  # environment-specific connection
  
  # Access Control
  access_control:
    allowed_roles: array
    allowed_groups: array
    requires_approval: boolean
  
  # Agent Authority
  agent_authority:
    max_autonomy_level: enum  # advisory | collaborative | autonomous
    require_human_approval: array  # action types requiring approval
  
  # Secrets & Credentials
  secrets:
    vault_path: string
    credential_sets: array
  
  # Metadata
  owner_team: string
  status: enum  # active | maintenance | decommissioned
  parent_environment: string  # for inheritance
```

---

## Environment Types

| Type | Purpose | Characteristics |
|------|---------|-----------------|
| **Production** | Live operations | Real data, real consequences |
| **Staging** | Pre-production testing | Production-like, isolated |
| **UAT** | User acceptance testing | Controlled test data |
| **Development** | Development and testing | Flexible, developer access |
| **Sandbox** | Isolated experimentation | Safe for exploration |

---

## Sandbox Concept

Sandboxes are isolated environments for:
- Agent training and testing
- New workflow development
- Customer-specific isolation
- Regulatory separation

---

## Workbench-Environment Binding

Each Workbench operates in one or more environments:

```yaml
workbench:
  id: "dispute-ops"
  environments:
    - environment_id: "prod"
      is_default: true
    - environment_id: "staging"
      is_default: false
```

---

## Cipher Integration

Environments integrate with Cipher for:
- User access to environments
- Agent enrollment per environment
- Environment-scoped permissions

---

## Related Documentation

- [Registry Services Overview](./README.md)
- [Machine Registry](./machine-registry.md)
- [Cipher IAM](../supporting-systems/cipher-iam.md)

---

*TODO: Detailed design — environment provisioning, secrets integration, inheritance model*

