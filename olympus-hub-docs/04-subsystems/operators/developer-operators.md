# Developer Operators

> **Status:** 🟡 Draft — Under active development

Developer Operators manage **Automation Specifications** and **Deployment Specifications** that codify how normative requirements are implemented. These operators are used by the **Developer** persona.

---

## Overview

| Operator | Specifications Managed |
|----------|------------------------|
| **workbench-developer-operator** | Workbench Deployment Specification |
| **scenario-developer-operator** | Trigger Specification, Scenario Automation Specification, Scenario Deployment Specification |
| **hub-application-operator** | Hub Application Specification |
| **composite-application-operator** | Hub Composite Application Specification (validation) |
| **composite-deployment-operator** | Hub Composite Application Deployment (child creation, routing table) |
| **workbench-apm-operator** | Log Alerts, Metric Alerts, Probes, SLO Alerts |
| **workbench-as-a-machine-operator** | Exposes Workbench as a Machine for other Workbenches |
| **scenario-as-a-tool-operator** | Exposes Scenario as a Tool |
| **scenario-as-an-agent-operator** | Exposes Scenario as an Agent |
| **workbench-ms-teams-operator** | MS Teams integration for Workbench |

---

## Specification Layer Context

Developer specifications span the **Automation Layer** and **Execution Layer**:

```
┌─────────────────────────────────────────────────────────────────────┐
│                      AUTOMATION LAYER                                │
│                                                                      │
│   "How is it codified?" — Applications, Triggers, Tools             │
│                                                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │  Scenario Automation Specification                           │   │
│   │  • Hub Application binding                                   │   │
│   │  • Trigger definitions                                       │   │
│   │  • Tool bindings                                             │   │
│   │  • Runtime selection                                         │   │
│   │  • Integration configurations                                │   │
│   └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      EXECUTION LAYER                                 │
│                                                                      │
│   "How is it operationalized?" — Deployment, Resources, SLAs        │
│                                                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │  Workbench Deployment Specification                          │   │
│   │  • Resource allocations                                      │   │
│   │  • Integration endpoints                                     │   │
│   │  • Deployment targets                                        │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │  Scenario Deployment Specification                           │   │
│   │  • Task queue mappings                                       │   │
│   │  • Agent enrollment                                          │   │
│   │  • SLA parameters                                            │   │
│   │  • Activation settings                                       │   │
│   └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Workbench Developer Operator

### Workbench Deployment Specification

Defines deployment configuration for a workbench.

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchDeploymentSpec
metadata:
  name: dispute-operations-deployment
  namespace: acme-bank
  labels:
    workbench: dispute-operations
spec:
  # Reference to Normative Spec
  normative_ref:
    name: dispute-operations-normative
    version: "1.0.0"

  # Deployment Target
  deployment:
    environment: production  # development | staging | production
    region: us-east-1
    replicas: 3

  # Resource Allocations
  resources:
    data_store_ref: dispute-operations-db
    memory_store_ref: agent-memory-cache
    knowledge_store_ref: compliance-knowledge

  # Integration Endpoints
  integrations:
    signal_exchange:
      enabled: true
      subscription_id: sub-dispute-ops-001
    
    notification_service:
      enabled: true
      provider: cipher-cns
    
    ms_teams:
      enabled: true
      team_id: "dispute-ops-team"
    
    external_systems:
      - name: core-banking
        machine_ref: acme-core-banking
        enabled: true
      - name: card-network
        machine_ref: acme-visa-gateway
        enabled: true

  # UX Channels
  channels:
    agent_desk:
      enabled: true
      theme: dispute-theme
    
    mcp:
      enabled: true
      personas:
        - agent
        - supervisor
    
    rest_api:
      enabled: true
      rate_limit: 1000

  # Observability
  observability:
    logging:
      level: info
      retention_days: 30
    
    metrics:
      enabled: true
      custom_metrics:
        - dispute_count
        - resolution_time
        - sla_compliance
    
    tracing:
      enabled: true
      sampling_rate: 0.1

  # Security
  security:
    data_encryption: true
    pii_redaction:
      enabled: true
      fields:
        - customer_name
        - account_number
        - ssn
```

---

## Scenario Developer Operator

### Trigger Specification

Defines signal-to-scenario bindings with matching conditions and transformations. Triggers are referenced by Scenario Automation Specifications.

```yaml
apiVersion: hub.olympus.io/v1
kind: TriggerSpec
metadata:
  name: dispute-submitted-trigger
  namespace: acme-bank
  labels:
    workbench: dispute-operations
    scenario: standard-dispute
spec:
  # Identity
  trigger:
    id: dispute-submitted
    name: "Dispute Submitted"
    display_name: "Customer Dispute Submitted"
    description: "Triggered when a customer submits a dispute through any channel"
    workbench_ref: dispute-operations

  # Signal Source
  signal_source:
    type: io_gateway  # io_gateway | signal_provider
    gateway_ref: heracles-api-gateway
    
    # Optional: filter to specific endpoints/events
    filter:
      paths:
        - "/api/v1/disputes"
      methods:
        - POST

  # Signal Matching Conditions
  conditions:
    # All conditions must match (AND logic)
    match_all:
      - field: "signal_header.signal_type"
        operator: equals
        value: "dispute.submitted"
      
      - field: "payload.data.dispute_type"
        operator: in
        values: ["chargeback", "fraud", "service_not_received", "duplicate_charge"]
    
    # Optional: OR conditions within groups
    match_any:
      - field: "payload.data.amount"
        operator: greater_than
        value: 0

  # Context Transformation
  transformation:
    type: javascript  # javascript | jsonata | mapping
    
    # JavaScript transformation function
    script: |
      (signal) => ({
        // Core identifiers
        dispute_id: signal.payload.data.dispute_id,
        customer_id: signal.payload.data.customer_id,
        transaction_id: signal.payload.data.transaction_id,
        
        // Business context
        amount: signal.payload.data.amount,
        currency: signal.payload.data.currency || "USD",
        dispute_type: signal.payload.data.type,
        dispute_reason: signal.payload.data.reason,
        
        // Timestamps
        submitted_at: signal.signal_header.timestamp,
        transaction_date: signal.payload.data.transaction_date,
        
        // Channel info
        submission_channel: signal.metadata.source_system || "api",
        
        // Customer context
        customer_tier: signal.payload.data.customer_tier || "standard"
      })
    
    # Optional: static enrichments
    static_fields:
      source: "trigger:dispute-submitted"
      version: "1.0"

  # Request Creation Settings
  request_settings:
    # Subject binding
    subject:
      type: customer
      id_path: "customer_id"
      
    # Object binding (optional)
    object:
      type: transaction
      id_path: "transaction_id"
    
    # TTL for the request
    ttl_days: 120
    
    # Priority calculation
    priority:
      type: calculated  # static | calculated
      rules:
        - condition: "amount > 10000"
          priority: critical
        - condition: "customer_tier == 'platinum'"
          priority: high
        - default: normal

  # Behavior
  behavior:
    # How to handle the signal
    create_or_update: create_new  # create_new | update_existing | create_or_update
    
    # Idempotency
    idempotency:
      enabled: true
      key_fields:
        - "dispute_id"
      window_hours: 24
    
    # Multi-match handling (if signal matches multiple triggers)
    multi_match_policy: first_match  # first_match | all_matches | error

  # Correlation (for update_existing or create_or_update)
  correlation:
    # How to find existing request
    strategy: attribute  # attribute | header | custom
    attribute: "dispute_id"
    signal_path: "payload.data.dispute_id"

  # Status
  status: active  # draft | active | suspended | deprecated
```

#### Trigger Examples

**Event-based Trigger (Atropos):**

```yaml
apiVersion: hub.olympus.io/v1
kind: TriggerSpec
metadata:
  name: merchant-response-trigger
spec:
  trigger:
    id: merchant-response
    name: "Merchant Response Received"
    workbench_ref: dispute-operations

  signal_source:
    type: io_gateway
    gateway_ref: atropos-event-bus
    filter:
      topics:
        - "merchant.chargeback.response"

  conditions:
    match_all:
      - field: "signal_header.signal_type"
        operator: equals
        value: "merchant.chargeback.response"

  transformation:
    type: mapping
    mappings:
      - source: "payload.data.dispute_id"
        target: "dispute_id"
      - source: "payload.data.merchant_response"
        target: "response"
      - source: "payload.data.evidence_urls"
        target: "merchant_evidence"

  request_settings:
    # This is an update, not a new request
    subject:
      type: customer
      resolve_from_request: true

  behavior:
    create_or_update: update_existing

  correlation:
    strategy: attribute
    attribute: "dispute_id"
    signal_path: "payload.data.dispute_id"
```

**Scheduled Trigger (Kale):**

```yaml
apiVersion: hub.olympus.io/v1
kind: TriggerSpec
metadata:
  name: daily-reconciliation-trigger
spec:
  trigger:
    id: daily-reconciliation
    name: "Daily Reconciliation"
    workbench_ref: dispute-operations

  signal_source:
    type: io_gateway
    gateway_ref: kale-scheduler
    filter:
      schedule_id: "dispute-daily-recon"

  conditions:
    match_all:
      - field: "signal_header.signal_type"
        operator: equals
        value: "schedule.triggered"

  transformation:
    type: javascript
    script: |
      (signal) => ({
        reconciliation_date: signal.payload.data.scheduled_time,
        batch_id: `recon-${signal.payload.data.scheduled_time.split('T')[0]}`
      })

  request_settings:
    subject:
      type: system
      id: "reconciliation-job"
    ttl_days: 7

  behavior:
    create_or_update: create_new
    idempotency:
      enabled: true
      key_fields:
        - "batch_id"
      window_hours: 48
```

---

### Scenario Automation Specification

Defines how a scenario is automated — the application, triggers, tools, and runtime. References TriggerSpec for signal-to-scenario bindings.

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAutomationSpec
metadata:
  name: standard-dispute-automation
  namespace: acme-bank
  labels:
    workbench: dispute-operations
    scenario: standard-dispute
spec:
  # Reference to Normative Spec
  normative_ref:
    name: standard-dispute-normative
    version: "1.2.0"

  # Hub Application Binding
  application:
    # Option 1: Single app (existing)
    ref: standard-dispute-application
    version: "2.0.0"
    runtime: seer  # seer | rhea | atlantis | chronoshift
    
    # Option 2: Composite (new - mutually exclusive with ref)
    # composite_ref:
    #   name: dispute-investigation-composite
    #   version: "1.0.0"

  # Trigger References (defined separately in TriggerSpec)
  triggers:
    - ref: dispute-submitted-trigger      # Reference to TriggerSpec
      required: true                       # Scenario requires this trigger
    
    - ref: merchant-response-trigger       # Reference to TriggerSpec
      required: false                      # Optional trigger for updates
  
  # Notification Template References (defined in NotificationTemplateSpec)
  notification_templates:
    - ref: dispute-notification-templates  # Reference to NotificationTemplateSpec

  # Tool Bindings
  tools:
    # Machine tools
    - id: get-transaction
      tool_ref: acme-get-transaction
      description: "Retrieve transaction details from core banking"
      permissions:
        - read
      
    - id: post-provisional-credit
      tool_ref: acme-post-provisional-credit
      description: "Issue provisional credit"
      permissions:
        - write
      requires_approval:
        condition: "amount > 5000"
        approver_role: approval-agent
    
    - id: initiate-chargeback
      tool_ref: acme-visa-chargeback
      description: "Initiate chargeback with card network"
      permissions:
        - write
    
    # Hub native utilities
    - id: create-task
      tool_ref: hub://task-management/create-task
      description: "Create a task for an agent"
    
    - id: add-memo
      tool_ref: hub://request-management/add-memo
      description: "Add memo to request"
    
    - id: search-knowledge
      tool_ref: hub://knowledge-services/search
      description: "Search compliance knowledge base"
      parameters:
        index: compliance-knowledge

  # State Machine (for workflow runtimes)
  state_machine:
    initial_state: intake
    states:
      - id: intake
        name: "Intake"
        transitions:
          - to: investigation
            condition: "intake_complete"
          - to: rejected
            condition: "invalid_dispute"
      
      - id: investigation
        name: "Investigation"
        transitions:
          - to: awaiting_merchant
            condition: "merchant_contacted"
          - to: resolution
            condition: "no_merchant_contact_needed"
      
      - id: awaiting_merchant
        name: "Awaiting Merchant Response"
        timeout:
          duration: "P5D"  # 5 days
          transition_to: resolution
        transitions:
          - to: resolution
            condition: "merchant_responded OR timeout"
      
      - id: resolution
        name: "Resolution"
        transitions:
          - to: completed
            condition: "decision_made"
          - to: escalated
            condition: "needs_escalation"
      
      - id: escalated
        name: "Escalated"
        transitions:
          - to: resolution
            condition: "escalation_resolved"
      
      - id: completed
        name: "Completed"
        terminal: true
      
      - id: rejected
        name: "Rejected"
        terminal: true

  # AI Agent Configuration (for Seer runtime)
  ai_agent:
    model:
      provider: bedrock
      model_id: anthropic.claude-3-sonnet
    
    system_prompt_ref: "prompts://dispute-ops/standard-dispute-agent"
    
    guardrails:
      - id: pii-redaction
        enabled: true
      - id: decision-bounds
        config:
          max_approval_amount: 5000
    
    memory:
      conversation_memory: true
      working_memory: true
      entity_memory: true

  # Integration Hooks
  hooks:
    on_request_created:
      - action: notify
        target: intake-agent
        template: new_dispute_notification
    
    on_state_change:
      - action: log_to_caf
        details: full
    
    on_tool_call:
      - action: audit_log
        filter:
          tool_ids:
            - post-provisional-credit
            - initiate-chargeback

  # Error Handling
  error_handling:
    on_tool_failure:
      strategy: retry_with_backoff
      max_retries: 3
      escalate_on_failure: true
    
    on_timeout:
      strategy: escalate
      escalate_to: supervisor
```

### Scenario Deployment Specification

Defines operational deployment settings for a scenario.

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioDeploymentSpec
metadata:
  name: standard-dispute-deployment
  namespace: acme-bank
  labels:
    workbench: dispute-operations
    scenario: standard-dispute
spec:
  # Reference to Automation Spec
  automation_ref:
    name: standard-dispute-automation
    version: "1.0.0"

  # Activation Settings
  activation:
    status: active  # draft | active | suspended | retired
    effective_from: "2026-01-01T00:00:00Z"
    effective_to: null  # null = no end date

  # Task Queue Mappings
  task_queues:
    - task_type: initial-review
      queue_ref: dispute-intake-queue
      priority_override: null  # Use default from queue
    
    - task_type: investigation
      queue_ref: dispute-resolution-queue
    
    - task_type: resolution-decision
      queue_ref: dispute-resolution-queue
    
    - task_type: high-value-review
      queue_ref: dispute-senior-queue

  # SLA Parameters
  sla:
    overall:
      target_hours: 240  # 10 business days
      warning_threshold_hours: 192  # 8 days
      critical_threshold_hours: 216  # 9 days
    
    per_task:
      - task_type: initial-review
        target_hours: 4
      - task_type: investigation
        target_hours: 48
      - task_type: resolution-decision
        target_hours: 8

  # Agent Enrollment
  agent_enrollment:
    auto_enroll:
      - role: dispute-analyst
        task_types:
          - initial-review
          - investigation
      - role: senior-analyst
        task_types:
          - investigation
          - resolution-decision
          - high-value-review
    
    enrollment_mode: role_based  # role_based | explicit | self_service

  # Capacity Planning
  capacity:
    expected_daily_volume: 500
    peak_multiplier: 2.0
    
    scaling:
      auto_scale_ai_agents: true
      min_ai_agents: 2
      max_ai_agents: 10

  # Feature Flags
  features:
    ai_assistance: true
    auto_categorization: true
    predictive_routing: false  # Coming soon
    
  # A/B Testing (optional)
  experiments:
    - id: ai-first-pass
      description: "Test AI doing first-pass review"
      traffic_percentage: 20
      variant: ai_intake
```

---

## Hub Application Operator

### Hub Application Specification

Defines a Hub Application with its code, configuration, and dependencies.

#### Naming Conventions

| Runtime | Resource Name Pattern | Display Name Pattern |
|---------|----------------------|---------------------|
| **Seer (Trained Agent)** | `{agent-name}` | `"{Name} (Trained Agent)"` |
| **Rhea** | `{workflow-name}-app` | `"{Name} Application"` |
| **Atlantis** | `{service-name}-app` | `"{Name} Application"` |

#### Labels for Seer Trained Agents

```yaml
labels:
  hub.olympus.io/workbench: {workbench-name}
  hub.olympus.io/runtime: seer
  seer.olympus.io/resource-type: trained-agent  # Indicates this is a Trained Agent
  seer.olympus.io/agent-type: {case-worker|orchestrator|specialist}
```

#### Example: Seer Trained Agent (Canonical Pattern)

For Seer AI agents, use `seerTrainingRef` to reference a `TrainingSpec`:

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: dispute-triage-agent
  namespace: acme-disputes
  labels:
    hub.olympus.io/workbench: acme-disputes
    hub.olympus.io/runtime: seer
    seer.olympus.io/resource-type: trained-agent
    seer.olympus.io/agent-type: case-worker
  annotations:
    seer.olympus.io/training-spec: "dispute-triage-agent-v1"
    seer.olympus.io/raw-agent: "dispute-analyst-base:^2.0.0"
spec:
  # Identity
  application:
    name: dispute-triage-agent
    display_name: "Dispute Triage Agent (Trained Agent)"  # Convention: include type
    version: "1.0.0"
    description: "AI agent for routine dispute triage - Trained Agent for Seer runtime"

  # Runtime
  runtime:
    type: seer
    version: "1.0.0"

  # CANONICAL: Reference to Seer TrainingSpec
  # Use seerTrainingRef for formally trained agents
  seerTrainingRef:
    name: dispute-triage-agent-v1
    namespace: acme-disputes
    version: "1.0.0"

  # Hub-side tool protocol references (normative)
  # These are resolved to operative bindings at deployment time
  dependencies:
    tools:
      - protocol: case-lookup
      - protocol: document-request
      - protocol: refund-processor
    
    knowledge_stores:
      - dispute-policies-kb
      - refund-rules-kb
    
    memory_stores:
      - case-dialog-store

  # Configuration (environment-agnostic)
  configuration:
    env_vars:
      LOG_LEVEL: info
```

> **Note**: For Seer agents, `seerTrainingRef` is the canonical pattern. It references a `TrainingSpec` CRD managed by Seer Operator. The `TrainingSpec` contains prompts, knowledge bindings, guardrails, and behavioral configuration.

#### Example: Rhea Workflow Application

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: dispute-workflow-app
  namespace: acme-disputes
  labels:
    hub.olympus.io/workbench: acme-disputes
    hub.olympus.io/runtime: rhea
spec:
  application:
    name: dispute-workflow-app
    display_name: "Dispute Resolution Workflow Application"
    version: "2.0.0"
    description: "BPMN workflow for dispute resolution"

  runtime:
    type: rhea
    version: "1.0.0"

  # Rhea-specific configuration
  rheaConfig:
    workflow_definition:
      type: file
      path: "workflows/main.yaml"
    
    activities:
      - name: review_dispute
        handler: activities.review_dispute
      - name: contact_merchant
        handler: activities.contact_merchant

  dependencies:
    tools:
      - acme-get-transaction
      - acme-post-provisional-credit
```

#### Example: Atlantis Container Application

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: dispute-handler-app
  namespace: acme-disputes
  labels:
    hub.olympus.io/workbench: acme-disputes
    hub.olympus.io/runtime: atlantis
spec:
  application:
    name: dispute-handler-app
    display_name: "Dispute Handler Application"
    version: "1.5.0"
    description: "Custom business logic for dispute handling"

  runtime:
    type: atlantis
    version: "1.0.0"

  # Container source
  source:
    type: git
    repository: "https://github.com/acme-bank/dispute-applications"
    branch: main
    path: "dispute-handler/"

  dependencies:
    tools:
      - acme-get-transaction
      - acme-visa-chargeback

  configuration:
    env_vars:
      LOG_LEVEL: info
      MERCHANT_TIMEOUT_DAYS: "5"
    
    secrets:
      - name: API_KEY
        vault_ref: secrets/dispute-app/api-key

  health:
    endpoint: /health
    interval_seconds: 30
    timeout_seconds: 5
```

---

## Composite Application Operator

### Hub Composite Application Specification

Manages `HubCompositeApplicationSpec` CRDs that group multiple Hub Applications to participate in the same Request.

#### Responsibilities

- Validates composite structure (no circular references)
- Validates OPA filter syntax
- Ensures all referenced applications exist
- No deployment logic (validation only)

#### Example: Dispute Investigation Composite

```yaml
apiVersion: hub.olympus.io/v1
kind: HubCompositeApplicationSpec
metadata:
  name: dispute-investigation-composite
  namespace: acme-disputes
  labels:
    hub.olympus.io/workbench: acme-disputes
spec:
  display_name: "Dispute Investigation Composite"
  description: "Multi-agent composite for dispute resolution"
  
  applications:
    - name: risk-agent
      ref:
        name: risk-assessment-agent
        version: "1.0.0"
      opa_filter:
        policy: |
          package composite.filter
          default allow = false
          allow { input.update_type == "REQUEST_CREATED" }
          allow { input.update_type == "DOCUMENT_UPLOADED" }
    
    - name: compliance-agent
      ref:
        name: compliance-check-agent
        version: "1.0.0"
      opa_filter:
        policy: |
          package composite.filter
          default allow = false
          allow { input.update_type in ["REQUEST_CREATED", "RISK_ASSESSMENT_COMPLETE"] }
    
    # Nested composite
    - name: customer-service-composite
      composite_ref:
        name: customer-service-composite
        version: "1.0.0"
  
  metadata:
    topology_pattern: "blackboard"
```

#### Validation Rules

1. **No Circular References**: Composite cannot reference itself (directly or indirectly)
2. **OPA Filter Syntax**: All inline Rego policies must be valid
3. **Reference Existence**: All `ref` and `composite_ref` targets must exist
4. **Mutual Exclusivity**: Each application entry must have exactly one of `ref` or `composite_ref`

---

## Composite Deployment Operator

### Hub Composite Application Deployment

Manages `HubCompositeApplicationDeployment` CRDs that represent running composite instances.

#### Responsibilities

1. **Recursive Resolution**: Flattens nested composites to union of all apps
2. **Child Deployment Creation**: Creates `HubApplicationDeployment` for each constituent app
3. **Ownership Management**: Sets `ownerReference` on child deployments
4. **Status Aggregation**: Aggregates child status → composite status
5. **Routing Table Population**: Populates routing table with flattened app list + OPA filters

#### Resolution Algorithm

```
resolveComposite(compositeSpec):
  apps = []
  for each app in compositeSpec.applications:
    if app.ref exists:
      apps.append({
        name: app.name,
        spec: lookupHubApplicationSpec(app.ref),
        opa_filter: app.opa_filter
      })
    else if app.composite_ref exists:
      nested = lookupCompositeSpec(app.composite_ref)
      apps.extend(resolveComposite(nested))
  return apps
```

#### Deployment Flow

```
ScenarioDeploymentSpec (with composite_ref)
  └── Composite Deployment Operator
        ├── Resolve composite recursively
        ├── Create HubCompositeApplicationDeployment
        ├── For each app:
        │     ├── Create HubApplicationDeployment (with ownerRef)
        │     └── Compile OPA filter
        └── Populate routing table:
              scenario_id → [App1 (+ filter), App2 (+ filter), ...]
```

#### All-or-Nothing Deployment

- If any child `HubApplicationDeployment` fails, mark composite as Failed
- Rollback all child deployments
- Composite status reflects worst child status

#### Example: Composite Deployment

```yaml
apiVersion: hub.olympus.io/v1
kind: HubCompositeApplicationDeployment
metadata:
  name: dispute-investigation-composite-sandbox
  namespace: acme-disputes
  labels:
    hub.olympus.io/workbench-instance: acme-disputes-sandbox
spec:
  compositeRef:
    name: dispute-investigation-composite
    version: "1.0.0"
  workbenchInstance:
    name: acme-disputes-sandbox

status:
  phase: Running
  applicationDeployments:
    - name: risk-agent
      deploymentRef: risk-agent-deployment-sandbox
      phase: Running
    - name: compliance-agent
      deploymentRef: compliance-agent-deployment-sandbox
      phase: Running
```

---

## Workbench APM Operator

The `workbench-apm-operator` manages observability and monitoring configurations for Hub Applications and Scenarios. It enables developers to define alerts, probes, and SLO targets using declarative specifications.

### Purpose

- Define log-based alerts for application events and errors
- Configure metric-based alerts for performance monitoring
- Set up probes for health and availability monitoring
- Establish SLO targets with alerting policies

### Integration with Olympus Watch

All APM specifications integrate with **Olympus Watch** — the unified observability platform:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    WORKBENCH APM OPERATOR                            │
│                                                                      │
│   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐    │
│   │  Log Alerts     │  │  Metric Alerts  │  │  SLO Alerts     │    │
│   └────────┬────────┘  └────────┬────────┘  └────────┬────────┘    │
│            │                    │                    │              │
│            └────────────────────┼────────────────────┘              │
│                                 │                                    │
│                                 ▼                                    │
│                        ┌─────────────────┐                          │
│                        │  Olympus Watch  │                          │
│                        │  (Observability │                          │
│                        │   Platform)     │                          │
│                        └─────────────────┘                          │
│                                 │                                    │
│                                 ▼                                    │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │  Notification Channels: PagerDuty, Slack, Email, Webhook    │   │
│   └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Log Alert Specification

Defines alerts based on log patterns, error rates, or specific log events.

```yaml
apiVersion: hub.olympus.io/v1
kind: LogAlertSpec
metadata:
  name: dispute-app-error-alert
  namespace: acme-bank
  labels:
    workbench: dispute-operations
    application: standard-dispute-application
spec:
  # Identity
  alert:
    name: dispute-app-error-alert
    display_name: "Dispute Application Error Alert"
    description: "Alerts when error rate exceeds threshold or critical errors occur"
    severity: critical  # critical | high | medium | low | info
    workbench_ref: dispute-operations

  # Log Source
  source:
    type: application  # application | scenario | workbench
    application_ref: standard-dispute-application
    # Optional: filter to specific log streams
    log_streams:
      - stderr
      - application

  # Alert Rules
  rules:
    # Pattern-based alert
    - id: critical-error-pattern
      name: "Critical Error Detection"
      type: pattern
      pattern:
        query: 'level:error AND (message:"OutOfMemory" OR message:"ConnectionTimeout" OR message:"DatabaseError")'
        threshold: 1
        window_minutes: 5
      
      notification:
        channels:
          - pagerduty-critical
          - slack-dispute-ops
        template: critical_error_alert

    # Rate-based alert
    - id: error-rate-spike
      name: "Error Rate Spike"
      type: rate
      rate:
        query: 'level:error'
        threshold_per_minute: 10
        comparison: greater_than
        window_minutes: 5
        baseline_window_hours: 24  # Compare against 24h baseline
        deviation_multiplier: 3   # Alert if 3x baseline
      
      notification:
        channels:
          - slack-dispute-ops
        template: error_rate_alert

    # Absence alert (no logs = problem)
    - id: heartbeat-missing
      name: "Application Heartbeat Missing"
      type: absence
      absence:
        query: 'message:"heartbeat" AND level:info'
        expected_interval_minutes: 5
        alert_after_missing: 2  # Alert after 2 missed heartbeats
      
      notification:
        channels:
          - pagerduty-high
        template: heartbeat_missing_alert

  # Suppression Rules
  suppression:
    # Don't alert during maintenance windows
    maintenance_windows:
      - schedule: "0 2-4 * * SUN"  # Sundays 2-4 AM
    
    # Don't re-alert for same issue
    deduplication:
      window_minutes: 30
      key_fields:
        - error_type
        - component

  # Auto-Resolution
  auto_resolve:
    enabled: true
    resolve_after_minutes: 15  # Auto-resolve if no matching logs for 15 min
```

---

### Metric Alert Specification

Defines alerts based on application and infrastructure metrics.

```yaml
apiVersion: hub.olympus.io/v1
kind: MetricAlertSpec
metadata:
  name: dispute-app-performance-alerts
  namespace: acme-bank
  labels:
    workbench: dispute-operations
    application: standard-dispute-application
spec:
  # Identity
  alert:
    name: dispute-app-performance-alerts
    display_name: "Dispute Application Performance Alerts"
    description: "Monitors application performance metrics"
    workbench_ref: dispute-operations

  # Metric Source
  source:
    type: application
    application_ref: standard-dispute-application

  # Alert Rules
  rules:
    # Latency alert
    - id: high-latency
      name: "High Request Latency"
      severity: high
      metric:
        name: request_duration_seconds
        aggregation: p95
        filters:
          endpoint: "/api/disputes/*"
      
      condition:
        operator: greater_than
        threshold: 5  # 5 seconds
        for_duration_minutes: 5
      
      notification:
        channels:
          - slack-dispute-ops
        template: latency_alert

    # Throughput alert
    - id: low-throughput
      name: "Low Request Throughput"
      severity: medium
      metric:
        name: requests_total
        aggregation: rate
        rate_window_minutes: 5
      
      condition:
        operator: less_than
        threshold: 10  # Less than 10 req/sec
        for_duration_minutes: 10
        # Only during business hours
        time_filter:
          days: ["MON", "TUE", "WED", "THU", "FRI"]
          hours: "08:00-18:00"
          timezone: "America/New_York"
      
      notification:
        channels:
          - slack-dispute-ops
        template: throughput_alert

    # Resource utilization
    - id: high-memory
      name: "High Memory Utilization"
      severity: high
      metric:
        name: memory_usage_bytes
        aggregation: max
      
      condition:
        operator: greater_than
        threshold_percent: 85  # 85% of allocated
        for_duration_minutes: 10
      
      notification:
        channels:
          - slack-dispute-ops
          - pagerduty-high
        template: resource_alert

    # Queue depth (business metric)
    - id: task-queue-buildup
      name: "Task Queue Buildup"
      severity: high
      metric:
        name: pending_tasks_count
        aggregation: current
        filters:
          queue: dispute-intake-queue
      
      condition:
        operator: greater_than
        threshold: 100
        for_duration_minutes: 15
      
      notification:
        channels:
          - slack-dispute-ops
        template: queue_buildup_alert
        # Also notify supervisor
        additional_recipients:
          - role: supervisor

  # Composite Alerts (multiple conditions)
  composite_rules:
    - id: degraded-service
      name: "Service Degraded"
      severity: critical
      description: "Multiple indicators suggest service degradation"
      
      conditions:
        operator: AND
        rules:
          - metric: request_duration_seconds
            aggregation: p95
            operator: greater_than
            threshold: 3
          - metric: error_rate
            aggregation: rate
            operator: greater_than
            threshold: 0.05  # 5% error rate
      
      for_duration_minutes: 5
      
      notification:
        channels:
          - pagerduty-critical
          - slack-dispute-ops
        template: service_degraded_alert
```

---

### Probe Specification

Defines health checks and availability probes for applications and dependencies.

```yaml
apiVersion: hub.olympus.io/v1
kind: ProbeSpec
metadata:
  name: dispute-app-probes
  namespace: acme-bank
  labels:
    workbench: dispute-operations
    application: standard-dispute-application
spec:
  # Identity
  probe_set:
    name: dispute-app-probes
    display_name: "Dispute Application Probes"
    description: "Health and availability probes for dispute application"
    workbench_ref: dispute-operations

  # Application Probes
  probes:
    # Liveness probe
    - id: app-liveness
      name: "Application Liveness"
      type: liveness
      target:
        type: application
        application_ref: standard-dispute-application
        endpoint: /health/live
      
      schedule:
        interval_seconds: 30
        timeout_seconds: 5
      
      success_criteria:
        http_status: 200
        response_time_ms: 1000
      
      failure_threshold: 3  # Failures before alerting
      
      on_failure:
        severity: critical
        notification:
          channels:
            - pagerduty-critical
        action: restart_application  # Optional auto-remediation

    # Readiness probe
    - id: app-readiness
      name: "Application Readiness"
      type: readiness
      target:
        type: application
        application_ref: standard-dispute-application
        endpoint: /health/ready
      
      schedule:
        interval_seconds: 15
        timeout_seconds: 5
      
      success_criteria:
        http_status: 200
        json_path:
          path: "$.status"
          expected: "ready"
      
      failure_threshold: 2
      
      on_failure:
        severity: high
        notification:
          channels:
            - slack-dispute-ops

    # Dependency probe (external system)
    - id: core-banking-connectivity
      name: "Core Banking Connectivity"
      type: dependency
      target:
        type: machine
        machine_ref: acme-core-banking
        endpoint: /health
      
      schedule:
        interval_seconds: 60
        timeout_seconds: 10
      
      success_criteria:
        http_status: 200
      
      failure_threshold: 2
      
      on_failure:
        severity: high
        notification:
          channels:
            - slack-dispute-ops
            - pagerduty-high
          template: dependency_failure_alert

    # Database probe
    - id: ganymede-connectivity
      name: "Database Connectivity"
      type: dependency
      target:
        type: data_store
        store_ref: dispute-entities-db
        query: "SELECT 1"
      
      schedule:
        interval_seconds: 30
        timeout_seconds: 5
      
      success_criteria:
        query_success: true
        response_time_ms: 500
      
      failure_threshold: 3
      
      on_failure:
        severity: critical
        notification:
          channels:
            - pagerduty-critical

    # Synthetic transaction probe
    - id: end-to-end-flow
      name: "End-to-End Flow Check"
      type: synthetic
      target:
        type: scenario
        scenario_ref: dispute-health-check  # Special health-check scenario
      
      schedule:
        interval_seconds: 300  # Every 5 minutes
        timeout_seconds: 60
      
      synthetic_transaction:
        steps:
          - name: "Create test dispute"
            action: create_request
            payload:
              type: health_check
              test: true
          - name: "Verify processing"
            action: wait_for_state
            expected_state: completed
            timeout_seconds: 30
          - name: "Cleanup"
            action: cancel_request
      
      success_criteria:
        all_steps_pass: true
        total_duration_seconds: 45
      
      failure_threshold: 2
      
      on_failure:
        severity: critical
        notification:
          channels:
            - pagerduty-critical
          template: synthetic_failure_alert

  # Probe Groups (for aggregate health)
  probe_groups:
    - id: critical-dependencies
      name: "Critical Dependencies"
      probes:
        - core-banking-connectivity
        - ganymede-connectivity
      
      aggregate_health:
        strategy: all_healthy  # all_healthy | majority_healthy | any_healthy
      
      on_group_failure:
        severity: critical
        notification:
          channels:
            - pagerduty-critical
```

---

### SLO Alert Specification

Defines Service Level Objectives and alerting based on error budgets.

```yaml
apiVersion: hub.olympus.io/v1
kind: SLOAlertSpec
metadata:
  name: dispute-app-slos
  namespace: acme-bank
  labels:
    workbench: dispute-operations
    application: standard-dispute-application
spec:
  # Identity
  slo_set:
    name: dispute-app-slos
    display_name: "Dispute Application SLOs"
    description: "Service Level Objectives for dispute resolution application"
    workbench_ref: dispute-operations

  # SLO Definitions
  slos:
    # Availability SLO
    - id: availability
      name: "Service Availability"
      description: "Application should be available 99.9% of the time"
      
      sli:
        type: availability
        good_events:
          metric: requests_total
          filter: 'status_code < 500'
        total_events:
          metric: requests_total
      
      objective:
        target: 99.9  # 99.9% availability
        window: rolling_30d  # 30-day rolling window
      
      error_budget:
        # 0.1% of 30 days = 43.2 minutes downtime allowed
        burn_rate_alerts:
          - name: "Fast Burn"
            description: "Consuming error budget too quickly (2h window)"
            burn_rate: 14.4  # 14.4x normal = budget exhausted in 2 hours
            window_minutes: 60
            severity: critical
            notification:
              channels:
                - pagerduty-critical
          
          - name: "Slow Burn"
            description: "Elevated error rate (6h window)"
            burn_rate: 6  # 6x normal = budget exhausted in 5 days
            window_minutes: 360
            severity: high
            notification:
              channels:
                - slack-dispute-ops
        
        # Budget consumption alerts
        consumption_alerts:
          - threshold_percent: 50
            severity: medium
            notification:
              channels:
                - slack-dispute-ops
          
          - threshold_percent: 80
            severity: high
            notification:
              channels:
                - slack-dispute-ops
                - pagerduty-high
          
          - threshold_percent: 100
            severity: critical
            notification:
              channels:
                - pagerduty-critical

    # Latency SLO
    - id: latency
      name: "Request Latency"
      description: "95% of requests should complete within 2 seconds"
      
      sli:
        type: latency
        metric: request_duration_seconds
        threshold: 2  # 2 seconds
        percentile: 95
      
      objective:
        target: 95  # 95% of requests under threshold
        window: rolling_7d
      
      error_budget:
        burn_rate_alerts:
          - name: "Latency Degradation"
            burn_rate: 10
            window_minutes: 60
            severity: high
            notification:
              channels:
                - slack-dispute-ops

    # Throughput SLO (business SLO)
    - id: dispute-resolution-time
      name: "Dispute Resolution Time"
      description: "90% of disputes should be resolved within SLA"
      
      sli:
        type: custom
        good_events:
          query: |
            count(dispute_resolution_duration_hours < 240)  # Within 10 days
        total_events:
          query: |
            count(dispute_status == "completed")
      
      objective:
        target: 90  # 90% within SLA
        window: rolling_30d
      
      error_budget:
        consumption_alerts:
          - threshold_percent: 75
            severity: high
            notification:
              channels:
                - slack-dispute-ops
              additional_recipients:
                - role: supervisor

    # Error Rate SLO
    - id: error-rate
      name: "Error Rate"
      description: "Error rate should be below 1%"
      
      sli:
        type: error_rate
        error_events:
          metric: requests_total
          filter: 'status_code >= 500'
        total_events:
          metric: requests_total
      
      objective:
        target: 99  # 99% success = 1% error rate
        window: rolling_7d
      
      error_budget:
        burn_rate_alerts:
          - name: "Error Spike"
            burn_rate: 10
            window_minutes: 30
            severity: critical
            notification:
              channels:
                - pagerduty-critical

  # SLO Dashboard
  dashboard:
    enabled: true
    include_slos:
      - availability
      - latency
      - error-rate
      - dispute-resolution-time
    
    # Display settings
    display:
      show_burn_rate: true
      show_budget_remaining: true
      show_trend: true
      forecast_exhaustion: true

  # Reporting
  reporting:
    weekly_report:
      enabled: true
      recipients:
        - role: supervisor
        - email: dispute-ops-team@acme-bank.com
      schedule: "0 9 * * MON"  # Monday 9 AM
    
    monthly_report:
      enabled: true
      recipients:
        - role: supervisor
        - role: manager
      schedule: "0 9 1 * *"  # 1st of month
```

---

### Notification Channels

APM specifications reference notification channels configured at the workbench or tenant level.

```yaml
apiVersion: hub.olympus.io/v1
kind: NotificationChannelConfig
metadata:
  name: dispute-ops-notification-channels
  namespace: acme-bank
spec:
  workbench_ref: dispute-operations
  
  channels:
    - id: pagerduty-critical
      type: pagerduty
      config:
        service_key_ref: vault://secrets/pagerduty/dispute-ops
        severity_mapping:
          critical: P1
          high: P2
    
    - id: pagerduty-high
      type: pagerduty
      config:
        service_key_ref: vault://secrets/pagerduty/dispute-ops
        severity_mapping:
          high: P2
          medium: P3
    
    - id: slack-dispute-ops
      type: slack
      config:
        webhook_url_ref: vault://secrets/slack/dispute-ops-webhook
        channel: "#dispute-ops-alerts"
        mention_on_critical: "@dispute-oncall"
    
    - id: email-ops-team
      type: email
      config:
        recipients:
          - dispute-ops@acme-bank.com
        subject_template: "[{{severity}}] {{alert_name}}"
```

---

## Composite Pattern Operators

These operators enable advanced patterns where Hub constructs are exposed as reusable building blocks.

### Workbench as a Machine Operator

Exposes a Workbench as a Machine that can be accessed by other Workbenches. This enables cross-workbench tool invocation where one workbench exposes its capabilities (Scenarios as Tools, Standalone Tools, Machine Tools) as a cohesive Machine interface.

> **See Also:** [Workbench as a Machine Pattern](../../09-composite-systems-and-patterns/workbench-as-a-machine.md) for detailed architecture and usage guide.

#### Tool Types That Can Be Exposed

| Tool Type | Description | Source |
|-----------|-------------|--------|
| **Scenarios as Tools** | Entire Scenarios with HTTP signals exposed as operations | Scenario Automation Spec |
| **Standalone Tools** | Hub Applications registered as standalone tools | ToolInstance with machine.type: standalone |
| **Machine Tools** | Tools from external machines (transitive exposure) | ToolInstance with external machine_ref |
| **Decision Tools** | Stateless decision/prediction tools | Decision/Prediction Tool Specs |

#### WorkbenchAsMachine CRD

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchAsMachine
metadata:
  name: dispute-ops-machine
  namespace: acme-bank
spec:
  # Source Workbench
  workbench_ref: dispute-operations

  # Machine Identity
  machine:
    id: dispute-operations
    display_name: "Dispute Operations Service"
    version: "2.0.0"
    description: "Dispute resolution capabilities for enterprise use"

  # Machine Capabilities
  capabilities:
    produces_signals: false    # Machine doesn't emit signals to consumers
    accepts_commands: true     # Machine can receive tool invocations
    provides_data: true        # Machine can return data

  # Tools to Expose
  exposed_tools:
    
    # Scenario as Tool (entire scenario with operations)
    scenarios:
      - scenario_ref: standard-dispute
        tool:
          name: dispute-resolution
          display_name: "Dispute Resolution"
          description: "Create and manage disputes"
        operations:
          - signal_type: dispute.submitted
            operation_name: create
            description: "Create a new dispute"
            input_mapping:
              customer_id: "{{input.customer_id}}"
              transaction_id: "{{input.transaction_id}}"
              amount: "{{input.amount}}"
              type: "{{input.dispute_type}}"
            output_mapping:
              dispute_id: "{{request.id}}"
              status: "{{request.state}}"
              
          - signal_type: dispute.evidence.submitted
            operation_name: add-evidence
            description: "Add evidence to existing dispute"
              
          - signal_type: dispute.status.query
            operation_name: get-status
            description: "Get dispute status"
    
    # Standalone Tools (Hub Applications as tools)
    standalone_tools:
      - tool_ref: fraud-detection-tool
        exposed_name: fraud-check
        description: "Check transaction for fraud risk"
        
      - tool_ref: eligibility-check-tool
        exposed_name: dispute-eligibility
        description: "Check if transaction is eligible for dispute"
    
    # Machine Tools (transitive exposure)
    machine_tools:
      - tool_ref: core-banking/get-transaction
        exposed_name: get-transaction
        description: "Get transaction details"
    
    # Decision Tools
    decision_tools:
      - tool_ref: dispute-classification-rules
        exposed_name: classify-dispute
        description: "Classify dispute type based on transaction"

  # Access Control
  access_control:
    allowed_workbenches:
      - customer-service
      - fraud-investigation
      - mobile-banking
    allowed_roles:
      - service-operator
      - analyst
    opa_policy_ref: policies/dispute-machine-access

  # Authentication for incoming requests
  authentication:
    methods:
      - type: oauth2_client_credentials
        issuer: https://auth.hub.acme.com
      - type: api_key
        header: X-API-Key
```

#### Operator Reconciliation

| Action | Behavior |
|--------|----------|
| **Create** | Register Machine Definition in Machine Registry, configure I/O Gateway routes |
| **Update** | Update Machine Definition, refresh exposed tools |
| **Delete** | Remove Machine from registry, remove I/O Gateway routes |

#### Validation Rules

1. **Workbench must exist** and be deployed
2. **Exposed scenarios must exist** with HTTP signal triggers
3. **Exposed standalone tools must exist** in Tool Registry
4. **Exposed machine tools must be accessible** by the workbench
5. **Access control must be valid** (workbenches/roles must exist)

### Scenario as a Tool Operator

Exposes a Scenario as a callable Tool. A single Scenario becomes one Tool with multiple operations (one per HTTP signal type). This prevents tool explosion while maintaining discoverability.

> **Note:** Scenario as a Tool is typically configured as part of [Workbench as a Machine](./workbench-as-a-machine.md) pattern. Use ScenarioAsTool CRD when exposing a single scenario independently.

#### Key Design Decision

| Approach | Description |
|----------|-------------|
| **Entire Scenario = One Tool** | The Scenario is exposed as a single tool |
| **Each HTTP Signal = One Operation** | Different signal types become operations of that tool |

This prevents tool proliferation — a scenario with 5 signal types creates 1 tool with 5 operations, not 5 tools.

#### ScenarioAsTool CRD

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAsTool
metadata:
  name: dispute-eligibility-tool
  namespace: acme-bank
spec:
  # Source Scenario
  scenario_ref: dispute-eligibility-check

  # Tool Identity
  tool:
    name: dispute-eligibility
    display_name: "Dispute Eligibility Check"
    version: "1.0.0"
    description: "Check and manage dispute eligibility"

  # Operations (one per HTTP signal type)
  operations:
    - signal_type: eligibility.check
      operation_name: check
      description: "Check if transaction is eligible for dispute"
      input_schema:
        type: object
        properties:
          transaction_id: { type: string }
          customer_id: { type: string }
        required: [transaction_id, customer_id]
      output_schema:
        type: object
        properties:
          eligible: { type: boolean }
          reason: { type: string }
          dispute_types: { type: array, items: { type: string } }
      execution:
        mode: synchronous
        timeout_seconds: 30
    
    - signal_type: eligibility.bulk_check
      operation_name: bulk-check
      description: "Check eligibility for multiple transactions"
      input_schema:
        type: object
        properties:
          transactions: { type: array, items: { type: object } }
      output_schema:
        type: object
        properties:
          results: { type: array }
      execution:
        mode: asynchronous
        timeout_seconds: 120

  # Dispatcher Configuration
  dispatcher_config:
    credential_mode: pass-through
    access_control:
      allowed_workbenches:
        - customer-service
        - mobile-app-backend
      allowed_roles:
        - analyst
        - operator
    retry:
      max_attempts: 3
      backoff:
        type: exponential
        initial_delay_ms: 100

  # Observability
  observability:
    metrics_enabled: true
    tracing_enabled: true
```

#### Operator Reconciliation

| Action | Behavior |
|--------|----------|
| **Create** | Register tool in Tool Registry with all operations |
| **Update** | Update tool registration, refresh operation schemas |
| **Delete** | Remove tool from Tool Registry |

#### Validation Rules

1. **Scenario must exist** with HTTP signal triggers
2. **Signal types must match** existing triggers in the scenario
3. **Schemas must be valid** JSON Schema format
4. **Access control** workbenches/roles must exist

### Scenario as an Agent Operator

Exposes a Scenario as an Agent that can be enrolled in Task Queues across Workbenches. This enables automated task completion within pre-existing Scenarios without modifying their original automation. The automating Scenario can use **any Hub Application type** — rule-based (Drools/DMN), workflow (Rhea), image processing, AI-powered (Seer), or any other runtime.

> **See Also:** [Scenario as an Agent Pattern](../../09-composite-systems-and-patterns/scenario-as-an-agent.md) for detailed architecture and usage guide.

#### Use Cases

| Use Case | Description |
|----------|-------------|
| **Task Automation** | Automate specific task types in existing Scenarios |
| **Load Sharing** | Scenario-Agent works alongside human agents |
| **Gradual Rollout** | Start with small percentage, increase over time |
| **Reusable Automation** | Same agent enrolled in multiple task queues |

#### ScenarioAsAgent CRD

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAsAgent
metadata:
  name: evidence-review-agent
  namespace: acme-bank
spec:
  # Source Scenario (the automating Scenario)
  source:
    workbench: evidence-automation
    scenario: evidence-review-automation
    
  # Agent Identity in IAM
  agent:
    id: scenario-agent-evidence-review
    display_name: "Evidence Review Automation"
    version: "1.0.0"
    description: "Automated review of evidence documents"
    
    # Skills (for skill-based routing in task queues)
    skills:
      - document_analysis
      - evidence_review
      - fraud_detection
      
    # Capacity settings
    capacity:
      max_concurrent_tasks: 10
      
  # Signal Configuration (how agent receives task notifications)
  signals:
    webhook_path: "/signals/agent/{{agent.id}}/notifications"
    webhook_secret_ref: "vault://scenario-agents/evidence-review/webhook-secret"
    
    # Trigger that maps task notifications to Scenario requests
    trigger:
      id: trg-task-notification
      scenario_id: evidence-review-automation
      
      events:
        - task.assigned
        - task.escalated
        - task.cancelled
        - request.cancelled
        
      transformation:
        type: low_code
        mapping:
          request_type: AgentTaskRequest
          source_context:
            workbench_id: "$.payload.source_workbench_id"
            request_id: "$.payload.source_request_id"
            task_id: "$.payload.task_id"
          payload_mapping:
            task_id: "$.payload.task_id"
            task_type: "$.payload.task_type"
            task_payload: "$.payload.task_payload"
            deadline: "$.payload.sla.deadline"
            
  # Deployments (where this agent will be enrolled)
  deployments:
    - target_workbench: dispute-operations
      task_queues:
        - queue_id: evidence-review-queue
          escalation_level: 0
          allocation_weight: 10  # 10% of tasks
          enabled: true
          
    - target_workbench: fraud-investigation
      task_queues:
        - queue_id: document-review-queue
          escalation_level: 1
          allocation_weight: 50
          enabled: true
          
  # API Configuration (how agent calls back to complete tasks)
  api_access:
    token_ref: "vault://scenario-agents/evidence-review/token"
    # API endpoints are discovered from target workbench at deployment time
```

#### Operator Reconciliation

| Resource | Create | Update | Delete |
|----------|--------|--------|--------|
| IAM Agent Identity | Create bot in Cipher IAM | Update profile, skills | Remove identity |
| Bot Token | Generate and store | Rotate token | Revoke token |
| HTTP Signal Endpoint | Register in Heracles | Update webhook config | Remove endpoint |
| Trigger | Create signal-to-request trigger | Update transformation | Remove trigger |
| Webhook Subscriptions | Register in each target workbench | Update event subscriptions | Remove subscriptions |
| Task Queue Enrollment | Enroll agent in specified queues | Update allocation weights | Unenroll agent |

#### Validation Rules

1. **Source Scenario must exist** and have a Hub Application configured
2. **Skills must be valid** identifiers in Cipher IAM skill catalog
3. **Target workbenches must be accessible** (cross-workbench permissions)
4. **Task queues must exist** in target workbenches
5. **Allocation weight must be 0-100** and sum with other agents ≤ 100

#### A2A Protocol Mode (Alternative)

For Scenarios participating in Agent-to-Agent multi-agent workflows (rather than task queues):

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAsAgent
metadata:
  name: dispute-specialist-agent
  namespace: acme-bank
spec:
  # Source Scenario
  source:
    workbench: dispute-operations
    scenario: dispute-consultation

  # Agent Identity
  agent:
    id: dispute-specialist
    display_name: "Dispute Specialist Agent"
    version: "1.0.0"
    skills:
      - dispute-analysis
      - regulation-interpretation

  # Communication Protocol (A2A instead of task-queue)
  protocol:
    type: a2a  # Agent-to-Agent protocol
    input_format: natural_language
    output_format: structured_response

  # Invocation Settings
  invocation:
    max_concurrent: 10
    timeout_seconds: 120

  # Access Control
  access:
    allowed_agents:
      - customer-service-agent
      - fraud-analyst-agent
```

### Workbench MS Teams Operator

Configures MS Teams integration for a Workbench.

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchMSTeams
metadata:
  name: dispute-ops-teams
  namespace: acme-bank
spec:
  # Workbench Reference
  workbench_ref: dispute-operations

  # Teams Configuration
  teams:
    tenant_id: "acme-365-tenant"
    team_id: "dispute-ops-team"

  # Bot Configuration
  bot:
    name: "Dispute Assistant"
    app_id: "{{vault:teams/app-id}}"
    app_secret_ref: "vault://secrets/teams/app-secret"

  # Chat Group Mappings
  chat_groups:
    - type: per_request
      name_template: "Dispute-{{request.id}}"
      auto_create: true
      participants:
        - role: assignee
        - role: supervisor
      archive_on_complete: true

    - type: workbench
      name: "Dispute Ops General"
      auto_create: true
      participants:
        - role: all_agents

  # Notifications
  notifications:
    - event: task_assigned
      send_to: assignee
      template: teams_task_card
    
    - event: sla_warning
      send_to: supervisor
      template: teams_sla_warning

  # Adaptive Cards
  adaptive_cards:
    - id: task_card
      template_path: "cards/task-card.json"
    - id: approval_card
      template_path: "cards/approval-card.json"
```

---

## Reconciliation Behavior

| Specification | Create | Update | Delete |
|---------------|--------|--------|--------|
| WorkbenchDeploymentSpec | Deploy resources, configure integrations | Rolling update | Undeploy gracefully |
| ScenarioAutomationSpec | Register triggers, bind tools | Version bump, revalidate | Deactivate triggers |
| ScenarioDeploymentSpec | Activate scenario, configure queues | Update SLAs, enrollment | Suspend scenario |
| HubApplicationSpec | Deploy application to runtime | Rolling deploy | Drain and remove |
| HubCompositeApplicationSpec | Validate structure, check references | Revalidate on changes | No-op (validation only) |
| HubCompositeApplicationDeployment | Resolve composite, create child deployments, populate routing table | Update children, recompile filters | Remove children, clear routing table |
| LogAlertSpec | Create alert rules in Watch | Update thresholds, patterns | Remove alert rules |
| MetricAlertSpec | Create metric alerts in Watch | Update conditions, thresholds | Remove metric alerts |
| ProbeSpec | Configure probes in Watch | Update schedules, criteria | Remove probes |
| SLOAlertSpec | Create SLO definitions in Watch | Update targets, burn rates | Remove SLO tracking |
| NotificationChannelConfig | Configure channels in Watch | Update channel settings | Remove channels |
| WorkbenchAsMachine | Register machine in registry | Update exposed tools | Remove from registry |
| ScenarioAsTool | Register tool | Update schema | Remove tool |
| ScenarioAsAgent | Register agent | Update capabilities | Remove agent |
| WorkbenchMSTeams | Configure bot, create channels | Update mappings | Remove integration |

---

## Developer Workflow

```
┌──────────────────────────────────────────────────────────────────────┐
│                      Developer Workflow                               │
│                                                                       │
│  1. Receive Normative Specification                                   │
│     └── From Process Architect                                        │
│                              │                                        │
│                              ▼                                        │
│  2. Create Hub Application Specification                              │
│     └── Code, runtime, dependencies                                   │
│                              │                                        │
│                              ▼                                        │
│  3. Create Scenario Automation Specification                          │
│     └── Triggers, tools, state machine                                │
│                              │                                        │
│                              ▼                                        │
│  4. Create Scenario Deployment Specification                          │
│     └── Queues, SLAs, enrollment                                      │
│                              │                                        │
│                              ▼                                        │
│  5. (Optional) Create Composite Pattern Specs                         │
│     └── Workbench as Machine, Scenario as Tool/Agent                  │
│                              │                                        │
│                              ▼                                        │
│  6. Commit to Git & Deploy                                            │
│     └── Operators reconcile                                           │
│                              │                                        │
│                              ▼                                        │
│  7. Handoff to Supervisor                                             │
│     └── For operational tuning                                        │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Related Documentation

- [Operators Overview](./README.md)
- [Process Architect Operator](./process-architect-operator.md) — Normative specs
- [Supervisor Operators](./supervisor-operators.md) — Operational configuration
- [Automation Runtimes](../automation-runtimes/README.md)
- [Signal Exchange](../signal-exchange/README.md)

---

*Developer Operators enable Infrastructure-as-Code for scenario automation and deployment, bridging normative requirements with operational reality.*

