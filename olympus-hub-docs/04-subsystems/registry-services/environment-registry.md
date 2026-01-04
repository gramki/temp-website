# Environment Registry

> **Status:** 🔴 Stub — Placeholder for expansion

The Environment Registry catalogs **Environments**—the real operational settings of an enterprise where Machines are deployed and produce Signals.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Define connection profiles and access mechanisms for Machines |
| **Contents** | Endpoints, access credentials, event topics, file stores |
| **Scope** | Tenant-specific environment definitions |
| **Integration** | Machine Registry, I/O Gateways, Workbenches, Cipher IAM |

---

## What is an Environment?

From the ontology:

> An Environment is the *real* operational setting of an enterprise, including:
> - Endpoints (HTTP/TCP) where systems are deployed
> - Access mechanisms (tokens, secrets, certificates)
> - Event buses/topics to publish/subscribe
> - File drops / object stores for batch I/O

An Environment hosts real I/O and produces Signals. It is **not** a deployment stage (like Production/Staging/UAT) but rather a logical grouping of connection infrastructure.

---

## Environment Schema

```yaml
environment:
  # Identity
  id: string
  name: string
  display_name: string
  description: string
  
  # Endpoints
  endpoints:
    http_tcp:
      - name: string
        url: string
        protocol: enum  # REST | SOAP | gRPC
    event_buses:
      - name: string
        type: enum  # kafka | rabbitmq | sns
        connection: string  # topic/queue URI
    file_stores:
      - name: string
        type: enum  # s3 | sftp | webdav
        location: string
  
  # Access Mechanisms
  access:
    oauth_credentials:
      - name: string
        vault_ref: string  # path to secrets
    api_keys:
      - name: string
        vault_ref: string
    certificates:
      - name: string
        vault_ref: string
        type: enum  # mtls | signing
    vault_path: string  # base path for all secrets
  
  # Machines in this Environment
  machines:
    - machine_id: string
      connection_profile:
        endpoint: string  # reference to endpoints entry
        credentials: string  # reference to access entry
  
  # Access Control
  access_control:
    allowed_workbenches: array
    allowed_roles: array
    requires_approval: boolean
  
  # Agent Authority
  agent_authority:
    max_autonomy_level: enum  # advisory | collaborative | autonomous
    require_human_approval: array  # action types requiring approval
  
  # Metadata
  owner_team: string
  status: enum  # active | maintenance | decommissioned
```

---

## Environment Examples

| Environment | Description | Typical Contents |
|-------------|-------------|------------------|
| **Core Banking** | Primary banking system access | Account APIs, Transaction topics, Statement files |
| **Card Network Integration** | Visa/Mastercard connectivity | Network APIs, Auth events, Settlement files |
| **CRM Integration** | Customer management system | Customer APIs, Event subscriptions |
| **Payment Gateway** | Payment processing systems | Payment APIs, Webhook endpoints |
| **Regulatory Reporting** | Compliance and reporting systems | Report endpoints, Submission portals |

---

## Key Characteristics

| Aspect | Description |
|--------|-------------|
| **Endpoints** | HTTP/TCP URLs where systems are deployed |
| **Access Mechanisms** | OAuth, API keys, mTLS certificates, tokens |
| **Event Buses** | Kafka topics, RabbitMQ queues for pub/sub |
| **File Stores** | S3 buckets, SFTP locations for batch I/O |
| **Secrets** | Credentials stored in secure vault, referenced by path |

---

## Workbench-Environment Binding

Workbenches reference Environments to access their Machines:

```yaml
workbench:
  id: "dispute-ops"
  environments:
    - environment_id: "card-network-integration"
      machines: [visa-gateway, mastercard-gateway]
    - environment_id: "core-banking"
      machines: [account-service, transaction-service]
```

---

## Connection Profile Resolution

When a Workbench accesses a Machine, the connection is resolved:

```
Workbench → Machine → Environment → Endpoint + Credentials
```

Example:
- Workbench: Dispute Operations
- Machine: visa-gateway
- Environment: card-network-integration
- Resolved: https://api.visa.com/v1 + OAuth credentials from vault

---

## Cipher Integration

Environments integrate with Cipher for:
- Secrets management (vault access)
- mTLS certificate management
- Agent identity scoping per environment

---

## Related Documentation

- [Registry Services Overview](./README.md)
- [Machine Registry](./machine-registry.md)
- [Cipher IAM](../supporting-systems/cipher-iam.md)
- [Ontology: Perception Layer](../../01-concepts/ontology-1-perception-layer.md#environment)

---

*TODO: Detailed design — secrets integration, connection pooling, environment inheritance*

