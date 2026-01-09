# Publisher Domain Operators

> **Status:** 🟡 Draft — Under active development

Publisher Domain Operators manage Hub infrastructure and tenant onboarding at the platform level. These operators are used by the **SRE Team** and **Win Team** personas in the Publisher realm.

---

## Overview

| Operator | Persona | Specifications Managed |
|----------|---------|------------------------|
| **SRE Operator** | SRE Team | Hub Cluster Deployment, System Resources, Blueprints, System Tools, Industry Knowledge |
| **Win Operator** | Win Team | Tenant Subscription |

---

## SRE Operator

The SRE Operator manages Hub platform infrastructure, including cluster deployments and system-scoped resources.

### Purpose

- Provision and manage Hub cluster deployments
- Configure system-wide resources shared across tenants
- Manage platform-level integrations and infrastructure

### Specifications

#### Hub Cluster Deployment Specification

Defines a Hub cluster deployment with all infrastructure components.

```yaml
apiVersion: hub.olympus.io/v1
kind: HubClusterDeployment
metadata:
  name: hub-prod-us-east
  labels:
    environment: production
    region: us-east-1
spec:
  # Cluster Identity
  cluster:
    name: hub-prod-us-east
    display_name: "Hub Production US East"
    region: us-east-1
    availability_zones:
      - us-east-1a
      - us-east-1b
      - us-east-1c

  # Infrastructure Provider
  infrastructure:
    provider: aws  # aws | azure | gcp | on-prem
    kubernetes_version: "1.28"
    node_pools:
      - name: system
        instance_type: m6i.xlarge
        min_nodes: 3
        max_nodes: 6
        labels:
          workload: system
      - name: workloads
        instance_type: m6i.2xlarge
        min_nodes: 5
        max_nodes: 20
        labels:
          workload: tenant

  # Hub Components
  components:
    signal_exchange:
      replicas: 3
      resources:
        cpu: "2"
        memory: "4Gi"
    
    request_management:
      replicas: 3
      storage:
        class: gp3
        size: 100Gi
    
    task_management:
      replicas: 2
    
    # Additional components...

  # Observability
  observability:
    logging:
      provider: datadog
      retention_days: 30
    metrics:
      provider: prometheus
      retention_days: 15
    tracing:
      provider: jaeger
      sampling_rate: 0.1

  # Security
  security:
    encryption:
      at_rest: true
      key_provider: aws-kms
      key_arn: "arn:aws:kms:us-east-1:..."
    network:
      vpc_cidr: "10.0.0.0/16"
      private_subnets: true
      nat_gateway: true

  # High Availability
  high_availability:
    multi_az: true
    backup:
      enabled: true
      schedule: "0 2 * * *"
      retention_days: 30
```

#### System Resource Specification

Defines system-scoped resources available to all tenants.

```yaml
apiVersion: hub.olympus.io/v1
kind: SystemResource
metadata:
  name: shared-knowledge-store
  labels:
    resource_type: knowledge_store
spec:
  # Resource Type
  type: knowledge_store  # knowledge_store | memory_store | data_store | cache

  # Provider Configuration
  provider:
    type: opensearch
    version: "2.11"
    endpoint: "https://shared-knowledge.hub.internal"
    
  # Capacity
  capacity:
    storage: 500Gi
    iops: 3000
    throughput: 250  # MB/s

  # Access Control
  access:
    mode: shared  # shared | dedicated
    tenant_isolation: namespace  # namespace | index | cluster
    
  # Quotas (per tenant)
  quotas:
    storage_per_tenant: 10Gi
    requests_per_second: 100

  # Availability
  availability:
    replicas: 3
    multi_az: true
```

#### Blueprint Specification

Defines reusable Workbench blueprints that tenants can instantiate. Blueprints are platform-provided templates for common business domains.

```yaml
apiVersion: hub.olympus.io/v1
kind: BlueprintSpec
metadata:
  name: dispute-resolution-blueprint
  labels:
    domain: dispute-resolution
    industry: banking
spec:
  # Identity
  blueprint:
    id: dispute-resolution
    name: "Dispute Resolution Blueprint"
    display_name: "Dispute Resolution Workbench Blueprint"
    version: "2.0.0"
    description: |
      A complete workbench blueprint for handling payment disputes, 
      chargebacks, and fraud claims in compliance with Regulation E 
      and card network rules.

  # Classification
  classification:
    domain: dispute-resolution
    industry: banking
    use_cases:
      - chargebacks
      - fraud-claims
      - service-disputes
    
    compliance_frameworks:
      - regulation-e
      - pci-dss
      - visa-core-rules
      - mastercard-chargeback-guide

  # Blueprint Components
  components:
    # Scenario templates
    scenarios:
      - id: standard-dispute
        name: "Standard Dispute Resolution"
        description: "Handle routine customer disputes"
        automation_runtime: seer
        
      - id: high-value-dispute
        name: "High Value Dispute"
        description: "Handle disputes over threshold amount"
        automation_runtime: seer
        
      - id: fraud-investigation
        name: "Fraud Investigation"
        description: "Investigate potential fraud cases"
        automation_runtime: rhea

    # Suggested roles
    roles:
      - id: dispute-analyst
        name: "Dispute Analyst"
        description: "Reviews and resolves disputes"
        suggested_skills:
          - dispute-resolution
          - customer-communication
          - card-network-rules
      
      - id: senior-analyst
        name: "Senior Analyst"
        description: "Handles escalated and complex disputes"
      
      - id: supervisor
        name: "Supervisor"
        description: "Manages team and approves high-value decisions"

    # Suggested task queues
    task_queues:
      - id: intake-queue
        name: "Intake Queue"
        allocation_algorithm: round_robin
      
      - id: resolution-queue
        name: "Resolution Queue"
        allocation_algorithm: skill_based

    # Required integrations
    integrations:
      required:
        - type: core_banking
          description: "Core banking system for transaction lookup"
        - type: card_network
          description: "Card network APIs for chargebacks"
      
      optional:
        - type: crm
          description: "CRM for customer history"
        - type: document_management
          description: "Evidence document storage"

    # Sample SOPs
    sample_sops:
      - id: dispute-handling-sop
        name: "Dispute Handling Procedure"
        template_path: "sops/dispute-handling.md"
      
      - id: regulation-e-sop
        name: "Regulation E Compliance"
        template_path: "sops/regulation-e.md"

    # Sample triggers
    sample_triggers:
      - id: dispute-submitted
        signal_type: "dispute.submitted"
        scenario: standard-dispute

  # Customization Points
  customization:
    # What tenants can customize
    customizable:
      - scenario_names
      - role_mappings
      - sla_targets
      - notification_templates
      - decision_thresholds
    
    # What is fixed in the blueprint
    fixed:
      - compliance_requirements
      - audit_controls
      - evidence_requirements

  # Prerequisites
  prerequisites:
    - "Core banking machine registered"
    - "Card network machine registered"
    - "At least 3 agents enrolled"

  # Metadata
  status: active  # active | deprecated | preview
  supported_regions:
    - us
    - eu
    - apac
```

#### System Tool Specification

Defines platform-provided tools available to all tenants.

```yaml
apiVersion: hub.olympus.io/v1
kind: SystemToolSpec
metadata:
  name: email-sender-tool
  labels:
    category: communication
spec:
  # Identity
  tool:
    id: system-email-sender
    name: "Email Sender"
    display_name: "Send Email"
    version: "1.0.0"
    description: "Send transactional emails through the platform email service"
    category: communication

  # Protocol
  protocol:
    type: openapi
    specification:
      openapi: "3.0.0"
      info:
        title: Email Sender API
        version: "1.0"
      paths:
        /send:
          post:
            summary: Send an email
            requestBody:
              content:
                application/json:
                  schema:
                    type: object
                    required:
                      - to
                      - subject
                      - body
                    properties:
                      to:
                        type: string
                        format: email
                      subject:
                        type: string
                      body:
                        type: string
                      template_id:
                        type: string
                      template_vars:
                        type: object
            responses:
              "200":
                description: Email sent
                content:
                  application/json:
                    schema:
                      type: object
                      properties:
                        message_id:
                          type: string
                        status:
                          type: string

  # Endpoint (platform-managed)
  endpoint:
    internal: true
    service: "platform://email-service"

  # Access Control
  access:
    default_availability: all_tenants
    requires_approval: false
    rate_limit:
      per_tenant: 1000  # per hour
      per_workbench: 100

  # Audit
  audit:
    log_invocations: true
    log_payloads: false  # PII concern

  # Documentation
  documentation:
    usage_guide: "https://docs.hub.olympus.io/tools/email-sender"
    examples:
      - name: "Simple email"
        request:
          to: "customer@example.com"
          subject: "Your request update"
          body: "Your request has been processed."
```

**Additional System Tools:**

```yaml
# Document Generation Tool
apiVersion: hub.olympus.io/v1
kind: SystemToolSpec
metadata:
  name: document-generator-tool
spec:
  tool:
    id: system-document-generator
    name: "Document Generator"
    display_name: "Generate Document"
    version: "1.0.0"
    description: "Generate PDF documents from templates"
    category: documents
  # ... specification details ...

---
# SMS Sender Tool
apiVersion: hub.olympus.io/v1
kind: SystemToolSpec
metadata:
  name: sms-sender-tool
spec:
  tool:
    id: system-sms-sender
    name: "SMS Sender"
    display_name: "Send SMS"
    version: "1.0.0"
    description: "Send SMS messages through platform SMS gateway"
    category: communication
  # ... specification details ...

---
# Currency Converter Tool
apiVersion: hub.olympus.io/v1
kind: SystemToolSpec
metadata:
  name: currency-converter-tool
spec:
  tool:
    id: system-currency-converter
    name: "Currency Converter"
    display_name: "Convert Currency"
    version: "1.0.0"
    description: "Convert between currencies using live exchange rates"
    category: utilities
  # ... specification details ...
```

#### Industry Knowledge Specification

Defines platform-provided industry knowledge bases available to tenants.

```yaml
apiVersion: hub.olympus.io/v1
kind: IndustryKnowledgeSpec
metadata:
  name: banking-regulations-knowledge
  labels:
    industry: banking
    region: us
spec:
  # Identity
  knowledge_base:
    id: banking-regulations-us
    name: "US Banking Regulations"
    display_name: "US Banking Regulations Knowledge Base"
    version: "2024.Q4"
    description: |
      Comprehensive knowledge base covering US banking regulations 
      including Regulation E, TILA, BSA/AML, and more.

  # Classification
  classification:
    industry: banking
    region: us
    categories:
      - consumer-protection
      - anti-money-laundering
      - electronic-funds
      - credit
      - privacy

  # Content Sources
  sources:
    - id: regulation-e
      name: "Regulation E (EFTA)"
      description: "Electronic Fund Transfer Act regulations"
      source_type: regulatory
      authority: CFPB
      effective_date: "2024-01-01"
      
      content:
        type: structured
        sections:
          - id: reg-e-error-resolution
            title: "Error Resolution Procedures"
            summary: "Requirements for investigating and resolving errors"
          - id: reg-e-provisional-credit
            title: "Provisional Credit Requirements"
            summary: "When and how to issue provisional credit"
          - id: reg-e-timelines
            title: "Investigation Timelines"
            summary: "Required timeframes for error resolution"

    - id: visa-core-rules
      name: "Visa Core Rules"
      description: "Visa dispute and chargeback rules"
      source_type: network_rules
      authority: Visa
      effective_date: "2024-10-01"
      
      content:
        type: document
        location: "platform://knowledge/visa-core-rules-2024.pdf"

    - id: mastercard-chargeback-guide
      name: "Mastercard Chargeback Guide"
      description: "Mastercard dispute management guidelines"
      source_type: network_rules
      authority: Mastercard
      effective_date: "2024-07-01"

  # Embeddings Configuration
  embeddings:
    model: text-embedding-3-small
    provider: platform  # Platform-managed embedding service
    chunk_size: 1000
    overlap: 100

  # Update Schedule
  updates:
    frequency: quarterly
    notification:
      - role: platform-admin
      - role: compliance-team
    review_required: true

  # Access Control
  access:
    availability: all_tenants
    regions:
      - us
    industries:
      - banking
      - credit_unions
      - fintech

  # Usage Tracking
  usage:
    track_queries: true
    track_citations: true

  # Metadata
  status: active
  last_updated: "2024-12-01"
  next_review: "2025-03-01"
```

**Additional Industry Knowledge Bases:**

```yaml
# EU Banking Regulations
apiVersion: hub.olympus.io/v1
kind: IndustryKnowledgeSpec
metadata:
  name: eu-banking-regulations
spec:
  knowledge_base:
    id: banking-regulations-eu
    name: "EU Banking Regulations"
    version: "2024.Q4"
  classification:
    industry: banking
    region: eu
    categories:
      - psd2
      - gdpr
      - aml
  # ... content details ...

---
# Insurance Industry Knowledge
apiVersion: hub.olympus.io/v1
kind: IndustryKnowledgeSpec
metadata:
  name: insurance-regulations-us
spec:
  knowledge_base:
    id: insurance-regulations-us
    name: "US Insurance Regulations"
    version: "2024.Q4"
  classification:
    industry: insurance
    region: us
  # ... content details ...

---
# Healthcare Compliance Knowledge
apiVersion: hub.olympus.io/v1
kind: IndustryKnowledgeSpec
metadata:
  name: healthcare-compliance-us
spec:
  knowledge_base:
    id: healthcare-hipaa
    name: "HIPAA Compliance"
    version: "2024.Q4"
  classification:
    industry: healthcare
    region: us
  # ... content details ...
```

---

### Reconciliation Behavior

| Specification | Create | Update | Delete |
|---------------|--------|--------|--------|
| HubClusterDeployment | Provision cluster | Rolling update | Drain and decommission |
| SystemResource | Provision resource | Update configuration | Migrate tenants, then delete |
| BlueprintSpec | Register blueprint | Version update | Deprecate, check usage |
| SystemToolSpec | Register tool | Version update | Deprecate, check usage |
| IndustryKnowledgeSpec | Index knowledge base | Re-index content | Archive, remove access |

---

## Win Operator

The Win Operator manages tenant subscription provisioning, bridging sales/onboarding with technical deployment.

### Purpose

- Provision new tenant subscriptions
- Configure initial tenant resources and quotas
- Manage subscription lifecycle (activation, suspension, termination)

### Specifications

#### Tenant Subscription Specification

Defines a complete tenant subscription with all initial configurations.

```yaml
apiVersion: hub.olympus.io/v1
kind: TenantSubscription
metadata:
  name: acme-bank-subscription
  labels:
    tenant: acme-bank
    tier: enterprise
spec:
  # Tenant Identity
  tenant:
    id: acme-bank
    name: "ACME Bank"
    legal_name: "ACME Banking Corporation"
    industry: banking
    region: us-east

  # Subscription Details
  subscription:
    id: sub-acme-001
    tier: enterprise  # starter | professional | enterprise
    start_date: "2026-01-01"
    billing_cycle: annual
    
  # Contract Terms
  contract:
    max_workbenches: 10
    max_agents: 500
    max_requests_per_month: 1000000
    sla_tier: platinum  # bronze | silver | gold | platinum

  # Initial Administrators
  administrators:
    primary:
      email: admin@acme-bank.com
      name: "John Smith"
      phone: "+1-555-0100"
    secondary:
      email: backup-admin@acme-bank.com
      name: "Jane Doe"

  # Identity Provider
  identity:
    provider: saml  # saml | oidc | local
    saml:
      metadata_url: "https://idp.acme-bank.com/metadata.xml"
      entity_id: "acme-bank-hub"
    domain_allowlist:
      - acme-bank.com
      - acme-group.com

  # Initial Resources
  resources:
    # Dedicated resources for this tenant
    dedicated:
      - type: data_store
        name: acme-primary-store
        provider: postgresql
        capacity:
          storage: 100Gi
          connections: 100
      
      - type: memory_store
        name: acme-memory
        provider: redis
        capacity:
          memory: 16Gi

    # Shared resources (quotas within system resources)
    shared:
      - resource_ref: shared-knowledge-store
        quota:
          storage: 20Gi
          requests_per_second: 200

  # Branding
  branding:
    primary_color: "#003366"
    logo_url: "https://assets.acme-bank.com/logo.svg"
    favicon_url: "https://assets.acme-bank.com/favicon.ico"

  # Integrations
  integrations:
    notification_service:
      provider: cipher-cns
      tenant_id: acme-bank
    
    ms_teams:
      enabled: true
      tenant_id: "acme-bank-365"

  # Compliance
  compliance:
    data_residency: us
    encryption:
      customer_managed_keys: true
      key_arn: "arn:aws:kms:us-east-1:acme:key/..."
    audit_retention_days: 2555  # 7 years
```

### Subscription Lifecycle States

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│ Pending  │ ──► │  Active  │ ──► │Suspended │ ──► │Terminated│
└──────────┘     └──────────┘     └──────────┘     └──────────┘
                       │                │
                       │                │
                       └───────◄────────┘
                        Reactivation
```

| State | Description |
|-------|-------------|
| **Pending** | Subscription created, awaiting provisioning |
| **Active** | Fully provisioned and operational |
| **Suspended** | Temporarily disabled (billing, compliance) |
| **Terminated** | Permanently decommissioned |

### Reconciliation Behavior

| Action | Behavior |
|--------|----------|
| **Create** | Provision namespace, resources, administrators, send welcome email |
| **Update** | Update quotas, resources, administrators (non-destructive) |
| **Suspend** | Disable access, pause workloads, retain data |
| **Terminate** | Export data, decommission resources, archive audit logs |

---

## Operator Configuration

### SRE Operator Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sre-operator
  namespace: hub-operators
spec:
  replicas: 2
  selector:
    matchLabels:
      app: sre-operator
  template:
    spec:
      containers:
        - name: operator
          image: hub/sre-operator:v1.0.0
          env:
            - name: CLOUD_PROVIDER
              value: "aws"
            - name: RECONCILE_INTERVAL
              value: "5m"
          resources:
            requests:
              cpu: "500m"
              memory: "512Mi"
```

### Win Operator Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: win-operator
  namespace: hub-operators
spec:
  replicas: 2
  selector:
    matchLabels:
      app: win-operator
  template:
    spec:
      containers:
        - name: operator
          image: hub/win-operator:v1.0.0
          env:
            - name: NOTIFICATION_WEBHOOK
              value: "https://notifications.hub.internal/welcome"
            - name: RECONCILE_INTERVAL
              value: "1m"
```

---

## Integration Points

| Integration | SRE Operator | Win Operator |
|-------------|--------------|--------------|
| **Cloud Provider APIs** | ✅ | ✅ |
| **Kubernetes API** | ✅ | ✅ |
| **Cipher IAM** | ✅ | ✅ |
| **Vault (Secrets)** | ✅ | ✅ |
| **Notification Service** | ❌ | ✅ |
| **Billing System** | ❌ | ✅ |

---

## Related Documentation

- [Operators Overview](./README.md)
- [Subscription Management](../subscription-management/README.md)
- [Tenant Subscription Lifecycle](../subscription-management/tenant-subscription-lifecycle.md)

---

*Publisher Domain Operators enable Infrastructure-as-Code for Hub platform management, ensuring consistent and auditable provisioning.*

