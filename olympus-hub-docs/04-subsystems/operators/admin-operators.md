# Admin Operators

> **Status:** 🟡 Draft — Under active development

Admin Operators manage infrastructure resources and foundational configurations within a tenant subscription. These operators are used by the **Tenant Admin** persona.

---

## Overview

| Operator | Specifications Managed |
|----------|------------------------|
| **Application Data Store Operators** | Ganymede (Relational), Callisto (Key-Value), Europa (Search/Analytics) |
| **Cognitive Services Operators** | Knowledge Bank Configuration, Memory Services Configuration |
| **workbench-admin-operator** | Environments, Machine Definitions, Machine Instances, Tool Definitions, Tool Instances |

---

## Data Architecture Alignment

Admin Operators align with Hub's layered data architecture:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    WORKBENCH-SCOPED DATA                                 │
│                                                                          │
│  ┌─────────────────────────────┐  ┌─────────────────────────────────┐   │
│  │  APPLICATION DATA STORES    │  │    COGNITIVE SERVICES           │   │
│  │  (Application-Managed)      │  │    (Hub-Managed)                │   │
│  │                             │  │                                  │   │
│  │  • Ganymede (Relational)    │  │  • Knowledge Bank               │   │
│  │  • Callisto (Key-Value)     │  │  • Memory Services              │   │
│  │  • Europa (Search/Analytics)│  │    (Enterprise, Agent, User)    │   │
│  └─────────────────────────────┘  └─────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
```

**Key Distinction:**
- **Application Data Stores** — Business domain entities, directly accessed by Hub Applications
- **Cognitive Services** — Hub-managed semantic stores with specific contracts and governance

---

## Application Data Store Operators

Application Data Store Operators provision workbench-scoped storage for business domain entities. These stores are optional and used at the developer's discretion.

### Purpose

- Provision Ganymede, Callisto, and Europa instances per workbench
- Configure capacity, access policies, and retention
- Manage schema lifecycle (DDL migrations for Ganymede)
- Support tenant isolation and workbench-scoped access

### Available Services

| Service | Type | Platform | Use Cases |
|---------|------|----------|-----------|
| **Ganymede** | Relational DBaaS | PostgreSQL-compatible | Business entities, complex relationships, transactions |
| **Callisto** | Key-Value Store | Distributed KV | Entity state, caching, fast lookups |
| **Europa** | Search/Analytics | OpenSearch (ELK) | Full-text search, log aggregation, analytics |

---

### Ganymede Specification (Relational DBaaS)

Provisions a PostgreSQL-compatible relational database for business domain entities.

```yaml
apiVersion: hub.olympus.io/v1
kind: GanymedeStore
metadata:
  name: dispute-entities-db
  namespace: acme-bank
  labels:
    workbench: dispute-operations
spec:
  # Identity
  store:
    name: dispute-entities
    display_name: "Dispute Entities Database"
    workbench_ref: dispute-operations

  # Capacity
  capacity:
    storage: 50Gi
    connections: 100
    iops: 3000
    compute_class: standard  # standard | high-memory | high-cpu

  # High Availability
  availability:
    replicas: 2
    multi_az: true
    read_replicas: 1  # Optional read replicas

  # Backup Configuration
  backup:
    enabled: true
    schedule: "0 3 * * *"  # Daily at 3 AM
    retention_days: 30
    point_in_time_recovery: true

  # Schema Management
  schema:
    # DDL files in workbench definition repository
    ddl_path: "./ddl/dispute-entities/"
    auto_migrate: true
    
    # Migration settings
    migration:
      strategy: versioned  # versioned | idempotent
      pre_deploy_validation: true
      rollback_on_failure: true

  # Access Control
  access:
    # Which workbenches can access (typically just the owning workbench)
    workbenches:
      - dispute-operations
    
    # Additional workbenches with read-only access
    read_only_workbenches:
      - fraud-investigation  # Can query for cross-reference
    
    # IAM roles with access
    roles:
      - dispute-analyst
      - dispute-supervisor

  # Connection Pooling
  connection_pool:
    min_connections: 5
    max_connections: 50
    idle_timeout_seconds: 300

  # Performance
  performance:
    query_timeout_seconds: 30
    statement_timeout_seconds: 60
    
  # Monitoring
  monitoring:
    slow_query_log:
      enabled: true
      threshold_ms: 1000
    metrics:
      - connections
      - query_latency
      - storage_usage
      - replication_lag
```

**When to use Ganymede:**
- Business entities with complex relationships
- Transactional integrity requirements (ACID)
- Complex queries with joins and aggregations
- Referential integrity constraints

---

### Callisto Specification (Key-Value Store)

Provisions a distributed key-value store for fast lookups and caching.

```yaml
apiVersion: hub.olympus.io/v1
kind: CallistoStore
metadata:
  name: dispute-state-cache
  namespace: acme-bank
  labels:
    workbench: dispute-operations
spec:
  # Identity
  store:
    name: dispute-state-cache
    display_name: "Dispute State Cache"
    workbench_ref: dispute-operations

  # Capacity
  capacity:
    memory: 8Gi
    max_keys: 10000000  # 10M keys
    max_key_size: 1KB
    max_value_size: 1MB

  # Collections (logical groupings)
  collections:
    - name: dispute-states
      description: "Current state of active disputes"
      ttl_seconds: 86400  # 24 hours default TTL
      
    - name: customer-context
      description: "Customer context for dispute processing"
      ttl_seconds: 3600  # 1 hour TTL
      
    - name: calculation-cache
      description: "Cached calculation results"
      ttl_seconds: 1800  # 30 minutes TTL

  # Persistence
  persistence:
    enabled: true
    mode: snapshot  # snapshot | append_only | hybrid
    snapshot_interval_seconds: 3600

  # Eviction Policy
  eviction:
    policy: lru  # lru | lfu | ttl | random
    max_memory_policy: volatile-lru  # Evict keys with TTL first

  # Replication
  replication:
    mode: async  # sync | async
    replicas: 2

  # Access Control
  access:
    workbenches:
      - dispute-operations
    roles:
      - dispute-analyst
      - dispute-supervisor

  # Performance
  performance:
    max_concurrent_connections: 1000
    operation_timeout_ms: 100
```

**When to use Callisto:**
- Fast entity lookups by key
- Caching entity state for UI responsiveness
- Session data (when application-specific)
- Flexible/evolving schemas
- High-throughput, low-latency access

---

### Europa Specification (Search/Analytics)

Provisions an OpenSearch-based service for full-text search and analytics.

```yaml
apiVersion: hub.olympus.io/v1
kind: EuropaStore
metadata:
  name: dispute-search
  namespace: acme-bank
  labels:
    workbench: dispute-operations
spec:
  # Identity
  store:
    name: dispute-search
    display_name: "Dispute Search & Analytics"
    workbench_ref: dispute-operations

  # Capacity
  capacity:
    storage: 100Gi
    shards: 3
    replicas: 2
    data_nodes: 3

  # Index Templates
  index_templates:
    - name: dispute-history
      description: "Searchable dispute history"
      template_path: "./indices/dispute-history.json"
      retention_days: 365  # 1 year
      
      # Index settings
      settings:
        number_of_shards: 3
        number_of_replicas: 1
        refresh_interval: "5s"
      
      # Field mappings
      mappings:
        properties:
          dispute_id:
            type: keyword
          customer_id:
            type: keyword
          transaction_id:
            type: keyword
          description:
            type: text
            analyzer: english
          amount:
            type: double
          status:
            type: keyword
          created_at:
            type: date
          resolved_at:
            type: date
          tags:
            type: keyword
          full_text:
            type: text
            analyzer: standard
    
    - name: dispute-audit-logs
      description: "Audit logs for dispute operations"
      template_path: "./indices/audit-logs.json"
      retention_days: 2555  # 7 years for compliance
      
      # Time-series optimized
      settings:
        number_of_shards: 1
        number_of_replicas: 1
      
      mappings:
        properties:
          timestamp:
            type: date
          action:
            type: keyword
          actor:
            type: keyword
          request_id:
            type: keyword
          details:
            type: text

    - name: dispute-metrics
      description: "Time-series metrics for analytics"
      retention_days: 90
      
      # Rollover policy for time-series
      rollover:
        enabled: true
        max_age: "7d"
        max_size: "10gb"

  # Snapshots
  snapshots:
    enabled: true
    schedule: "0 2 * * *"  # Daily at 2 AM
    repository: s3
    retention_days: 30

  # Access Control
  access:
    workbenches:
      - dispute-operations
    
    # Role-based index access
    index_permissions:
      - index: dispute-history
        roles:
          - dispute-analyst
          - dispute-supervisor
        permissions:
          - read
          - write
      
      - index: dispute-audit-logs
        roles:
          - dispute-supervisor
          - auditor
        permissions:
          - read
      
      - index: dispute-metrics
        roles:
          - dispute-supervisor
        permissions:
          - read

  # Analytics
  analytics:
    dashboards_enabled: true
    dashboard_templates:
      - name: dispute-overview
        template_path: "./dashboards/dispute-overview.json"
```

**When to use Europa:**
- Full-text search across entities
- Log aggregation and analysis
- Time-series data and metrics
- Analytics dashboards
- Audit trail searchability

---

## Cognitive Services Operators

Cognitive Services are Hub-managed with specific semantics. Admins configure access and resource allocation, but Hub governs the structure and lifecycle.

### Knowledge Bank Configuration

Configures access to Knowledge Bank for a workbench.

```yaml
apiVersion: hub.olympus.io/v1
kind: KnowledgeBankConfig
metadata:
  name: dispute-knowledge-config
  namespace: acme-bank
  labels:
    workbench: dispute-operations
spec:
  # Workbench Reference
  workbench_ref: dispute-operations

  # Knowledge Sources
  knowledge_sources:
    # Tenant-scoped knowledge stores
    tenant_stores:
      - name: dispute-policies
        display_name: "Dispute Resolution Policies"
        description: "Product policies and dispute handling rules"
        
        # Ingestion pipeline
        ingestion:
          sources:
            - type: sharepoint
              location: "https://acme.sharepoint.com/sites/policies/disputes"
              sync_schedule: "0 0 * * *"  # Daily
            - type: git
              repository: "https://github.com/acme-bank/dispute-policies"
              branch: main
              path: "/docs"
        
        # Embedding configuration
        embeddings:
          model: text-embedding-3-small
          provider: bedrock
          dimensions: 1536
        
        # Chunking strategy
        chunking:
          strategy: semantic  # semantic | fixed | paragraph
          max_chunk_size: 1000
          overlap: 100

      - name: regulatory-compliance
        display_name: "Regulatory Compliance"
        description: "Regulation E, card network rules"
        
        ingestion:
          sources:
            - type: manual
              description: "Uploaded by compliance team"
        
        embeddings:
          model: text-embedding-3-small
          provider: bedrock
          dimensions: 1536

    # Reference to system-scoped knowledge (read-only)
    system_stores:
      - name: banking-regulations
        access: read

  # Retrieval Configuration
  retrieval:
    default_top_k: 5
    similarity_threshold: 0.7
    reranking:
      enabled: true
      model: cross-encoder

  # Access Control
  access:
    # Who can query
    query_roles:
      - dispute-analyst
      - dispute-supervisor
    
    # Who can update/curate
    curator_roles:
      - dispute-supervisor
      - knowledge-curator
```

### Memory Services Configuration

Configures Memory Services (Enterprise, Agent, User Memory) for a workbench.

```yaml
apiVersion: hub.olympus.io/v1
kind: MemoryServicesConfig
metadata:
  name: dispute-memory-config
  namespace: acme-bank
  labels:
    workbench: dispute-operations
spec:
  # Workbench Reference
  workbench_ref: dispute-operations

  # Enterprise Memory Configuration
  enterprise_memory:
    enabled: true
    
    # Memory types to enable
    memory_types:
      semantic:  # Decisions, rationale, precedents
        enabled: true
        retention_days: 2555  # 7 years for compliance
        governance:
          require_evidence: true
          require_rationale: true
      
      episodic:  # Events, interactions
        enabled: true
        retention_days: 365
      
      procedural:  # Skills, patterns learned
        enabled: true
        retention_days: 730  # 2 years

    # Sharing with other workbenches
    sharing:
      enabled: true
      shared_with:
        - workbench: fraud-investigation
          memory_types:
            - semantic  # Share decisions
          access: read
    
    # CAF Integration (Cognitive Audit Fabric)
    caf_integration:
      decision_records:
        enabled: true
        schema_ref: standard-decision-record
      evidence_bundles:
        enabled: true
        storage_ref: evidence-storage
      explanation_service:
        enabled: true

  # Agent Memory Configuration
  agent_memory:
    enabled: true
    
    # Session-scoped memory
    session_memory:
      enabled: true
      max_context_tokens: 8000
    
    # Working memory
    working_memory:
      enabled: true
      ttl_hours: 24

  # User Memory Configuration
  user_memory:
    enabled: true
    
    # What to remember about users/subjects
    memory_types:
      preferences:
        enabled: true
        retention_days: 365
      
      interaction_history:
        enabled: true
        retention_days: 90
        max_entries: 100
    
    # Decay policy
    decay:
      enabled: true
      strategy: time_weighted  # time_weighted | access_based
      half_life_days: 180

  # Access Control
  access:
    # Who can read memory
    read_roles:
      - dispute-analyst
      - dispute-supervisor
    
    # Who can write/curate
    write_roles:
      - dispute-analyst
      - dispute-supervisor
    
    # Who can configure governance
    admin_roles:
      - dispute-supervisor
```

---

## Workbench Admin Operator

The `workbench-admin-operator` manages foundational Workbench configurations including environments, machines, and tools.

### Purpose

- Define environments for workbench operations
- Register machine definitions (abstract templates)
- Provision machine instances (concrete endpoints)
- Register tool definitions and instances

### Specifications

#### Environment Specification

Defines an operational environment for a workbench.

```yaml
apiVersion: hub.olympus.io/v1
kind: EnvironmentSpec
metadata:
  name: dispute-prod-environment
  namespace: acme-bank
  labels:
    workbench: dispute-operations
spec:
  # Identity
  environment:
    name: dispute-prod
    display_name: "Dispute Operations - Production"
    type: production  # development | staging | production

  # Variables (available to all machines/tools in this environment)
  variables:
    region: us-east-1
    tenant_id: acme-bank
    log_level: info

  # Secrets (Vault references)
  secrets:
    - name: core_banking_oauth
      vault_path: "secrets/acme/core-banking/oauth"
    - name: card_network_api_key
      vault_path: "secrets/acme/visa/api-key"

  # Network Configuration
  network:
    egress_allowed:
      - "*.acme-bank.internal"
      - "api.visa.com"
      - "api.mastercard.com"
    proxy:
      enabled: true
      url: "http://proxy.acme-bank.internal:3128"

  # Application Data Store Bindings
  application_data_stores:
    ganymede: dispute-entities-db      # Reference to GanymedeStore
    callisto: dispute-state-cache       # Reference to CallistoStore
    europa: dispute-search              # Reference to EuropaStore

  # Cognitive Services Bindings
  cognitive_services:
    knowledge_bank: dispute-knowledge-config    # Reference to KnowledgeBankConfig
    memory_services: dispute-memory-config      # Reference to MemoryServicesConfig
```

#### Machine Definition Specification

Defines an abstract machine type (template).

```yaml
apiVersion: hub.olympus.io/v1
kind: MachineDefinition
metadata:
  name: temenos-core-banking
  namespace: acme-bank
spec:
  # Identity
  definition:
    name: temenos-core-banking
    version: "2.1.0"
    display_name: "Temenos T24 Core Banking"
    vendor: Temenos

  # Type
  type: external  # internal | external | saas | gateway

  # Capabilities
  capabilities:
    produces_signals: true
    accepts_commands: true
    provides_data: true

  # Tool Protocols (abstract tools)
  tool_protocols:
    - id: get-account
      name: "Get Account Details"
      protocol_type: openapi
      specification:
        openapi: "3.0.0"
        info:
          title: Account API
          version: "1.0"
        paths:
          /accounts/{accountId}:
            get:
              summary: Get account details
              parameters:
                - name: accountId
                  in: path
                  required: true
                  schema:
                    type: string
              responses:
                "200":
                  description: Account details
                  content:
                    application/json:
                      schema:
                        $ref: "#/components/schemas/Account"
        servers:
          - url: "{{base_url}}"
      variables:
        - name: base_url
          description: "Base URL for the API"
          required: true

    - id: post-payment
      name: "Initiate Payment"
      protocol_type: openapi
      specification:
        # OpenAPI spec for payment initiation
        # ...

  # Signal Schemas
  signal_schemas:
    - type: event
      name: account-balance-changed
      schema:
        type: object
        properties:
          account_id:
            type: string
          previous_balance:
            type: number
          new_balance:
            type: number
          timestamp:
            type: string
            format: date-time
```

#### Machine Instance Specification

Defines a concrete machine instance with actual endpoints.

```yaml
apiVersion: hub.olympus.io/v1
kind: MachineInstance
metadata:
  name: acme-core-banking
  namespace: acme-bank
  labels:
    environment: dispute-prod
spec:
  # Reference to Definition
  definition_ref:
    name: temenos-core-banking
    version: "2.1.0"

  # Environment
  environment_ref: dispute-prod-environment

  # Connection Details
  connection:
    endpoint: "https://core.acme-bank.com/api/v2"
    protocol: REST
    auth:
      type: oauth2
      credentials_ref: core_banking_oauth  # Reference to environment secret

  # Variable Bindings
  variables:
    base_url: "https://core.acme-bank.com/api/v2"
    tenant_id: acme
    region: us-east-1

  # Access Policies
  access_policies:
    allowed_workbenches:
      - dispute-operations
      - payment-operations
    allowed_roles:
      - operator
      - analyst
    requires_approval: false

  # Tool Instances (concrete tools from protocols)
  tools:
    - id: acme-get-account
      protocol_ref: get-account
      access_policies:
        allowed_roles:
          - operator
          - analyst
          - auditor
      flow_control:
        rate_limit: 100
        burst_limit: 150
        timeout_ms: 5000
        retry:
          max_attempts: 3
          backoff_ms: 1000

    - id: acme-post-payment
      protocol_ref: post-payment
      access_policies:
        requires_approval: true
        allowed_roles:
          - operator
      flow_control:
        rate_limit: 10
        timeout_ms: 30000
```

#### Tool Definition Specification

Defines a standalone tool (not part of a machine).

```yaml
apiVersion: hub.olympus.io/v1
kind: ToolDefinition
metadata:
  name: fraud-detection-ml
  namespace: acme-bank
spec:
  # Identity
  definition:
    name: fraud-detection-ml
    version: "1.0.0"
    display_name: "Fraud Detection ML Model"
    category: analytics

  # Protocol
  protocol_type: openapi
  specification:
    openapi: "3.0.0"
    paths:
      /predict:
        post:
          summary: Predict fraud probability
          requestBody:
            content:
              application/json:
                schema:
                  $ref: "#/components/schemas/TransactionInput"
          responses:
            "200":
              description: Fraud prediction
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/FraudPrediction"
    servers:
      - url: "{{endpoint}}"

  # Variables
  variables:
    - name: endpoint
      required: true
    - name: model_version
      required: false
      default: "latest"

  # Input/Output Schemas
  schemas:
    input:
      type: object
      properties:
        transaction_id:
          type: string
        amount:
          type: number
        merchant_category:
          type: string
    output:
      type: object
      properties:
        fraud_probability:
          type: number
        risk_factors:
          type: array
          items:
            type: string
```

#### Tool Instance Specification

Creates a concrete tool instance.

```yaml
apiVersion: hub.olympus.io/v1
kind: ToolInstance
metadata:
  name: acme-fraud-detector
  namespace: acme-bank
spec:
  # Reference
  definition_ref:
    name: fraud-detection-ml
    version: "1.0.0"

  # Environment
  environment_ref: dispute-prod-environment

  # Connection
  connection:
    endpoint: "https://ml.acme-bank.internal/fraud/v1"
    auth:
      type: api_key
      credentials_ref: ml_platform_key

  # Variables
  variables:
    endpoint: "https://ml.acme-bank.internal/fraud/v1"
    model_version: "v2.3.1"

  # Access
  access_policies:
    allowed_workbenches:
      - dispute-operations
      - fraud-investigation
    allowed_roles:
      - analyst
      - operator

  # Flow Control
  flow_control:
    rate_limit: 50
    timeout_ms: 10000
```

---

## Reconciliation Behavior

### Application Data Store Operators

| Specification | Create | Update | Delete |
|---------------|--------|--------|--------|
| GanymedeStore | Provision PostgreSQL, execute DDL | Update capacity, run migrations | Backup, archive, delete |
| CallistoStore | Provision KV store, create collections | Update capacity, TTL policies | Flush and delete |
| EuropaStore | Provision OpenSearch, create indices | Update mappings, retention | Snapshot and delete |

### Cognitive Services Operators

| Specification | Create | Update | Delete |
|---------------|--------|--------|--------|
| KnowledgeBankConfig | Configure access, set up ingestion | Update sources, embeddings | Remove access |
| MemoryServicesConfig | Enable memory types, configure CAF | Update retention, sharing | Disable services |

### Workbench Admin Operator

| Specification | Create | Update | Delete |
|---------------|--------|--------|--------|
| EnvironmentSpec | Create environment | Update variables/secrets | Cascade check, delete |
| MachineDefinition | Register definition | Version update | Deprecate |
| MachineInstance | Create instance, test connection | Update endpoint/config | Remove from workbenches |
| ToolDefinition | Register definition | Version update | Deprecate |
| ToolInstance | Create instance, test connection | Update endpoint/config | Remove from workbenches |

---

## Validation Rules

### Dependency Validation

| Specification | Dependencies |
|---------------|--------------|
| MachineInstance | MachineDefinition, EnvironmentSpec |
| ToolInstance | ToolDefinition, EnvironmentSpec |
| EnvironmentSpec | GanymedeStore, CallistoStore, EuropaStore (if referenced) |
| KnowledgeBankConfig | Workbench must exist |
| MemoryServicesConfig | Workbench must exist |

### Connection Validation

On create/update of Machine or Tool instances:
1. Validate endpoint reachability
2. Validate credentials work
3. Optionally run health check endpoint

### Schema Validation

For GanymedeStore:
1. DDL files must be syntactically valid
2. Migration sequence must be complete (no gaps)
3. Destructive operations require explicit approval

For EuropaStore:
1. Index templates must be valid OpenSearch mappings
2. Retention policies must comply with tenant compliance settings

---

## Related Documentation

- [Operators Overview](./README.md)
- [Registry Services](../registry-services/README.md)
- [Machine Registry](../registry-services/machine-registry.md)
- [Tool Registry](../registry-services/tool-registry.md)
- [Environment Registry](../registry-services/environment-registry.md)
- [Data Architecture](../../07-data-architecture/README.md)
- [Application Data Stores](../../07-data-architecture/application-data-stores.md)
- [Storage Architecture](../../07-data-architecture/storage-architecture.md)
- [Memory Services](../memory-services/README.md)
- [Knowledge Services](../knowledge-services/README.md)

---

*Admin Operators enable declarative management of tenant infrastructure, application data stores, and cognitive services.*

