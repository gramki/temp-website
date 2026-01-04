# Machine Registry

> **Status:** 🔴 Stub — Placeholder for expansion

The Machine Registry catalogs **Machines (systems) in the environment**—the information systems that manage business entities and produce signals.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Catalog machines with capabilities and connections |
| **Contents** | Enterprise systems, external services, I/O gateways |
| **Scope** | Tenant-specific machine registrations |
| **Integration** | I/O Gateways, Command Registry, Workbenches |

---

## What is a Machine?

From the ontology:

> A Machine is an entity in the Environment that manages business entities, executes commands, and/or produces signals.

Examples:
- Core Banking System
- Payment Gateway
- CRM System
- ERP Modules
- Custom Applications

---

## Machine Registration Schema

```yaml
machine:
  # Identity
  id: string
  name: string
  type: enum  # internal | external | saas | gateway
  
  # Description
  display_name: string
  description: string
  vendor: string
  
  # Capabilities
  capabilities:
    produces_signals: boolean
    accepts_commands: boolean
    provides_data: boolean
  
  # Signal Configuration (if produces_signals)
  signals:
    types: array  # event, exception, observation
    gateway: string  # which I/O gateway receives signals
    topics: array    # event bus topics
  
  # Command Configuration (if accepts_commands)
  commands:
    registry_namespace: string  # namespace in Command Registry
    endpoints: object           # connection configuration
  
  # Data Access (if provides_data)
  data:
    entities: array    # business entity types
    access_method: string  # api, database, file
  
  # Connection
  connection:
    protocol: string
    endpoint: string
    auth: object
  
  # Metadata
  owner_team: string
  status: enum  # active | maintenance | deprecated
  environments: array  # which environments this machine is in
```

---

## Machine Types

| Type | Description | Examples |
|------|-------------|----------|
| **Internal** | Organization-owned systems | Core banking, custom apps |
| **External** | Third-party systems | Payment networks, credit bureaus |
| **SaaS** | Cloud services | Salesforce, ServiceNow |
| **Gateway** | I/O Gateways (implicit machines) | Atropos, Heracles, Dia |

---

## Machine Capabilities

### Signal Production
- Which signal types the machine produces
- How signals are delivered (event bus, API, file)
- Signal schemas and formats

### Command Acceptance
- What commands the machine can execute
- Command schemas and protocols
- Response patterns

### Data Provision
- What business entities the machine manages
- How data is accessed (API, direct, file)
- Data refresh patterns

---

## Workbench Integration

Each Workbench defines:
- **Machines in Scope** — Which machines are relevant
- **Signal Subscriptions** — Which machine signals trigger scenarios
- **Command Access** — Which machine commands are available

---

## Related Documentation

- [Registry Services Overview](./README.md)
- [Environment Registry](./environment-registry.md)
- [I/O Gateways](../signal-providers/README.md)

---

*TODO: Detailed design — connection management, health monitoring, capability discovery*

