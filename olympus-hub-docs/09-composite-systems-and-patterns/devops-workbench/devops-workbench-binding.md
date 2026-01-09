# DevOps Workbench Binding

> **Status:** 🟡 Draft
> **Category:** Composite Patterns / DevOps Workbench

---

## Overview

**DevOps Workbench Binding** enables bidirectional integration between a Business Workbench (A) and a DevOps Workbench (D):

| Direction | Mechanism | Purpose |
|-----------|-----------|---------|
| **A → D** | Signal routing via Atropos | Send development lifecycle events |
| **D → A** | Resource access via `{workbench-name}-gateway` | Query knowledge, memory, data |

This document specifies the CRDs and operators that orchestrate the binding.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEVOPS WORKBENCH BINDING ARCHITECTURE                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  BUSINESS WORKBENCH (A)                    DEVOPS WORKBENCH (D)             │
│  Subscription: acme-bank                   Subscription: acme-devops        │
│                                                                              │
│  ┌─────────────────────────────┐                                            │
│  │ 1. Tenant Admin creates     │                                            │
│  │    DevOpsWorkbenchBinding   │                                            │
│  │    CRD                      │                                            │
│  └──────────────┬──────────────┘                                            │
│                 │                                                            │
│                 ▼                                                            │
│  ┌─────────────────────────────┐                                            │
│  │ 2. DevOpsBindingOperator    │                                            │
│  │    (runs in A)              │                                            │
│  │                             │                                            │
│  │  • Validate binding spec    │                                            │
│  │  • Create ServiceAccount    │                                            │
│  │  • Generate BotToken        │                                            │
│  │  • Build manifest           │                                            │
│  └──────────────┬──────────────┘                                            │
│                 │                                                            │
│                 │ 3. Push BusinessWorkbenchManifest CRD + credentials       │
│                 │    (via secure cross-subscription API)                    │
│                 ▼                                                            │
│                                            ┌─────────────────────────────┐  │
│                                            │ 4. BusinessWorkbenchManifest│  │
│                                            │    CRD (created in D)       │  │
│                                            └──────────────┬──────────────┘  │
│                                                           │                  │
│                                                           ▼                  │
│                                            ┌─────────────────────────────┐  │
│                                            │ 5. ManifestOperator         │  │
│                                            │    (runs in D)              │  │
│                                            │                             │  │
│                                            │  • Register Machine         │  │
│                                            │  • Create Tool bindings     │  │
│                                            │  • Store credentials        │  │
│                                            └─────────────────────────────┘  │
│                                                                              │
│  RESULT:                                                                    │
│                                                                              │
│  ┌─────────────────────────────┐          ┌─────────────────────────────┐  │
│  │ Exposed Resources           │◀─────────│ dispute-ops-dev-gateway     │  │
│  │ • Knowledge Bank            │  Access  │ (Machine in D)              │  │
│  │ • Enterprise Memory         │  via     │                             │  │
│  │ • Data Stores               │  Bot     │ AI Agents query resources   │  │
│  │ • Scenario Metadata         │  Token   │ through this gateway        │  │
│  │ • CAF Records               │          │                             │  │
│  └─────────────────────────────┘          └─────────────────────────────┘  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## CRD: DevOpsWorkbenchBinding (in A)

This CRD is created by Tenant Admin in the Business Workbench to establish the binding.

```yaml
apiVersion: hub.olympus.io/v1
kind: DevOpsWorkbenchBinding
metadata:
  name: dispute-devops-binding
  namespace: acme-bank    # Business Workbench namespace
spec:
  # Target DevOps Workbench
  devops_workbench:
    workbench_id: dispute-devops
    namespace: acme-devops
    subscription_id: acme-devops-central    # Required if cross-subscription
    tenant_id: acme-corp                     # Required if cross-tenant
    
    # Endpoint for pushing manifest (discovered or explicit)
    api_endpoint: https://hub.acme-devops.olympus.io/api/v1
  
  # Signal routing configuration (A → D)
  signal_routing:
    enabled: true
    sources:
      - subsystem: automation-ideation
        events:
          - idea.submitted
          - idea.promoted
          - intent.completed
          - charter.created
      
      - subsystem: ci-subsystem
        events:
          - test.passed
          - test.failed
          - build.passed
          - build.failed
      
      - subsystem: artifact-registry
        events:
          - artifact.published
          - promotion.requested
          - promotion.completed
      
      - subsystem: feedback-services
        events:
          - feedback.promoted
          - problem.promoted
          - feedback.resolved
    
    # Optional filters
    filters:
      - source: ci-subsystem
        condition: "event.type in ['test.failed', 'build.failed']"
  
  # Resources exposed to DevOps Workbench (D → A access)
  exposed_resources:
    # Knowledge Bank access
    knowledge:
      enabled: true
      access: read
      collections:
        - "*"                    # All collections, or
        # - "sops"               # Specific collections
        # - "reference-docs"
    
    # Enterprise Memory access
    enterprise_memory:
      enabled: true
      access: read
      scopes:
        - workbench              # Workbench-level memory
        - scenario               # Scenario-level memory
    
    # Agent Memory access (optional)
    agent_memory:
      enabled: false             # Usually not exposed
    
    # Data Stores access
    data_stores:
      enabled: true
      stores:
        - type: ganymede         # Relational store (PostgreSQL)
          access: read
          schemas: ["dispute_data"]
        
        - type: callisto         # Key-value store (Redis)
          access: read
          namespaces: ["config", "cache"]
        
        - type: europa           # Search/analytics store (Elasticsearch)
          access: read
          indices: ["*"]
    
    # CAF Records access
    caf_records:
      enabled: true
      access: read
      record_types:
        - DecisionRecord
        - EvidenceBundle
        - OutcomeRecord
        - OverrideRecord
    
    # Scenario Metadata access
    scenario_metadata:
      enabled: true
      access: read
      include:
        - definitions            # Scenario definitions
        - configurations         # Application configs
        - triggers               # Trigger definitions
        - sops                   # SOP references
  
  # CRD Publishing (D → A writes via Git)
  # DevOps agents push CRDs to Business Workbench's Git repository
  # The Git repository is registered as a Machine in DevOps Workbench
  crd_publishing:
    enabled: true
    
    # Git endpoint for CRD publishing
    git:
      # The Business Workbench's Git repo is registered as a Machine in D
      machine_ref: dispute-ops-dev-git  # Registered in D via manifest
      repository: "https://git.acme-bank.com/workbenches/dispute-ops-dev"
      branch: main                      # Or feature branch for review
      path: "crds/"                     # Directory for CRD files
      
      # Commit configuration
      commit:
        author: "DevOps Agent <devops@hub.olympus.io>"
        message_template: "[DevOps] {action} {crd_kind}/{crd_name} from {scenario}"
      
      # Branch strategy
      branching:
        strategy: feature_branch        # feature_branch | direct_commit
        branch_prefix: "devops/"        # e.g., devops/scenario-refund-check
        auto_merge: false               # Require PR approval
    
    # Allowed CRD types (what DevOps agents can publish)
    allowed_specs:
      # Scenario Specifications
      - ScenarioNormativeSpec      # PA agent creates scenario definitions
      - ScenarioAutomationSpec     # Developer agent creates automation config
      - ScenarioDeploymentSpec     # Developer agent creates deployment config
      - TriggerSpec                # Developer agent creates triggers
      - SOPDocumentSpec            # PA agent creates SOPs
      
      # Application Specifications
      - HubApplicationSpec         # Developer agent scaffolds applications
      
      # Seer Agent Specifications (if agentic)
      - RawAgentSpec               # Developer agent creates agent definitions
      - TrainingSpec               # Developer agent creates training specs
      - EmploymentSpec             # Developer agent creates employment specs
      
      # Registry Specifications
      - MachineDefinition          # Define new machine types
      - ToolDefinition             # Define new tool types
      - MachineInstance            # Create machine instances
      - ToolInstance               # Create tool instances
      
      # Data Store Specifications
      - GanymedeStore              # Provision relational DBaaS
      - CallistoStore              # Provision key-value store
      - EuropaStore                # Provision search/analytics
      
      # Cognitive Services Configuration
      - KnowledgeBankConfig        # Configure knowledge bank
      - MemoryServicesConfig       # Configure memory services
    
    # Approval via Git workflow (PR-based)
    approval:
      mechanism: pull_request          # PR approval, not separate CRD
      reviewers:
        - role: process_architect      # For normative specs
        - role: developer              # For automation specs
        - role: tenant_admin           # For infrastructure specs
      auto_merge_conditions:
        - "labels.contains('auto-approve')"
        - "confidence >= 0.95 AND change_type == 'minor'"
  
  # Credential configuration
  credentials:
    # Token expiry (operator handles rotation before expiry)
    token_expiry: 90d
    
    # Rotation policy
    rotation:
      enabled: true
      frequency: 30d             # Rotate every 30 days
      overlap: 24h               # Old token valid for 24h after rotation

status:
  # Managed by operator
  phase: Bound | Pending | Error | Rotating
  
  binding_id: uuid
  
  # Credential status
  credentials:
    current_token:
      secret_ref:
        name: dispute-devops-binding-token
        namespace: acme-bank
      created_at: "2026-01-09T10:00:00Z"
      expires_at: "2026-04-09T10:00:00Z"
      next_rotation: "2026-02-08T10:00:00Z"
    
    previous_token:              # During rotation overlap
      secret_ref:
        name: dispute-devops-binding-token-prev
        namespace: acme-bank
      expires_at: "2026-02-09T10:00:00Z"
  
  # Manifest push status
  manifest:
    pushed_at: "2026-01-09T10:00:05Z"
    manifest_version: "v1.2.3"
    push_status: Success | Failed | Pending
  
  # Signal routing status
  signal_routing:
    status: Active | Paused | Error
    last_signal_at: "2026-01-09T15:30:00Z"
    signals_routed_24h: 1234
  
  conditions:
    - type: Ready
      status: "True"
      lastTransitionTime: "2026-01-09T10:00:10Z"
      reason: BindingEstablished
      message: "DevOps workbench binding is active"
```

---

## CRD: BusinessWorkbenchManifest (in D)

This CRD is pushed by the DevOpsBindingOperator in A to the DevOps Workbench D.

```yaml
apiVersion: hub.olympus.io/v1
kind: BusinessWorkbenchManifest
metadata:
  name: dispute-ops-dev-manifest
  namespace: acme-devops    # DevOps Workbench namespace
  labels:
    hub.olympus.io/source-workbench: dispute-ops-dev
    hub.olympus.io/source-subscription: acme-bank
spec:
  # Source Business Workbench identification
  source_workbench:
    workbench_id: dispute-ops-dev
    workbench_name: "Dispute Operations - Development"
    namespace: acme-bank
    subscription_id: acme-bank
    tenant_id: acme-corp
    domain: dispute-resolution
    
    # Endpoint for resource access
    gateway_endpoint: https://hub.acme-bank.olympus.io/api/v1/workbenches/dispute-ops-dev
  
  # Machine to be registered in D
  machine:
    name: dispute-ops-dev-gateway
    description: "Gateway to Dispute Operations workbench resources"
    
    # Tools exposed via this machine
    tools:
      # ═══════════════════════════════════════════════════════════════════
      # READ TOOLS (Query resources in Business Workbench)
      # ═══════════════════════════════════════════════════════════════════
      
      # Knowledge Bank tools
      - name: query_knowledge
        description: "Query Knowledge Bank collections"
        endpoint: /knowledge/query
        method: POST
        access: read
        input_schema:
          type: object
          properties:
            collection: { type: string }
            query: { type: string }
            limit: { type: integer, default: 10 }
        output_schema:
          type: object
          properties:
            results: { type: array }
            total: { type: integer }
      
      - name: get_sop
        description: "Retrieve Standard Operating Procedure"
        endpoint: /knowledge/sops/{sop_id}
        method: GET
        access: read
      
      # Enterprise Memory tools
      - name: query_memory
        description: "Query Enterprise Memory"
        endpoint: /memory/query
        method: POST
        access: read
      
      # Data Store tools
      - name: query_documents
        description: "Query Ganymede document store"
        endpoint: /data/ganymede/query
        method: POST
        access: read
      
      - name: get_config
        description: "Get configuration from Callisto"
        endpoint: /data/callisto/{namespace}/{key}
        method: GET
        access: read
      
      - name: query_data
        description: "Query Europa relational store"
        endpoint: /data/europa/query
        method: POST
        access: read
      
      # CAF tools
      - name: get_decision_records
        description: "Retrieve decision records for a request"
        endpoint: /caf/decisions
        method: GET
        access: read
      
      # Scenario Metadata tools
      - name: get_scenario
        description: "Get scenario definition"
        endpoint: /scenarios/{scenario_id}
        method: GET
        access: read
      
      - name: list_scenarios
        description: "List all scenarios in workbench"
        endpoint: /scenarios
        method: GET
        access: read
      
  # ═══════════════════════════════════════════════════════════════════════
  # GIT MACHINE (for CRD publishing)
  # The Business Workbench's Git repository is registered as a separate Machine
  # ═══════════════════════════════════════════════════════════════════════
  git_machine:
    name: dispute-ops-dev-git
    description: "Git repository for Dispute Operations workbench CRDs"
    
    # Git endpoint configuration
    connection:
      repository: "https://git.acme-bank.com/workbenches/dispute-ops-dev"
      protocol: https                   # https | ssh
      auth_type: deploy_key             # deploy_key | token | ssh_key
    
    # Tools for Git operations
    tools:
      - name: git_clone
        description: "Clone repository to local workspace"
        operation: clone
        
      - name: git_pull
        description: "Pull latest changes"
        operation: pull
        
      - name: git_create_branch
        description: "Create a feature branch for changes"
        operation: create_branch
        input_schema:
          type: object
          properties:
            branch_name: { type: string }
            from_branch: { type: string, default: "main" }
        
      - name: git_commit_crd
        description: "Commit a CRD file to the repository"
        operation: commit
        input_schema:
          type: object
          properties:
            file_path: { type: string }      # e.g., crds/scenarios/refund-check.yaml
            content: { type: string }         # YAML content of CRD
            message: { type: string }         # Commit message
            branch: { type: string }          # Branch to commit to
        
      - name: git_push
        description: "Push commits to remote"
        operation: push
        input_schema:
          type: object
          properties:
            branch: { type: string }
        
      - name: git_create_pr
        description: "Create a Pull Request for review"
        operation: create_pr
        input_schema:
          type: object
          properties:
            source_branch: { type: string }
            target_branch: { type: string, default: "main" }
            title: { type: string }
            description: { type: string }
            reviewers: { type: array, items: { type: string } }
            labels: { type: array, items: { type: string } }
        output_schema:
          type: object
          properties:
            pr_url: { type: string }
            pr_id: { type: string }
        
      - name: git_list_files
        description: "List CRD files in repository"
        operation: list
        input_schema:
          type: object
          properties:
            path: { type: string, default: "crds/" }
            pattern: { type: string }        # e.g., "*.yaml"
        
      - name: git_read_file
        description: "Read a CRD file from repository"
        operation: read
        input_schema:
          type: object
          properties:
            file_path: { type: string }
            branch: { type: string, default: "main" }
  
  # Credentials for accessing the machine
  credentials:
    secret_ref:
      name: dispute-ops-dev-gateway-credentials
      namespace: acme-devops
    auth_type: bot_token
  
  # Binding metadata
  binding:
    binding_id: uuid
    binding_version: "v1.2.3"
    created_at: "2026-01-09T10:00:00Z"
    expires_at: "2026-04-09T10:00:00Z"

status:
  # Managed by ManifestOperator in D
  phase: Active | Pending | Error | Expired
  
  # Machine registration status
  machine:
    registered: true
    machine_id: dispute-ops-dev-gateway
    registered_at: "2026-01-09T10:00:10Z"
  
  # Tool availability
  tools:
    total: 8
    available: 8
    last_health_check: "2026-01-09T15:00:00Z"
  
  # Credential status
  credentials:
    valid: true
    expires_at: "2026-04-09T10:00:00Z"
  
  conditions:
    - type: Ready
      status: "True"
      lastTransitionTime: "2026-01-09T10:00:15Z"
      reason: MachineRegistered
      message: "Business workbench gateway is available"
```

---

## Operators

### DevOpsBindingOperator (runs in A)

**Watches:** `DevOpsWorkbenchBinding` CRDs

**Reconciliation Loop:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEVOPSBINDINGOPERATOR RECONCILIATION                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. VALIDATE                                                                │
│     • Check DevOps workbench exists and is reachable                       │
│     • Validate exposed_resources configuration                             │
│     • Check permissions for cross-subscription push                        │
│                                                                              │
│  2. PROVISION CREDENTIALS                                                   │
│     • Create ServiceAccount for DevOps access                              │
│     • Generate BotToken with scoped permissions                            │
│     • Store token in Secret                                                │
│                                                                              │
│  3. BUILD MANIFEST                                                          │
│     • Generate BusinessWorkbenchManifest spec                              │
│     • Include all exposed resource tool definitions                        │
│     • Include credential references                                        │
│                                                                              │
│  4. PUSH TO DEVOPS WORKBENCH                                                │
│     • Authenticate with DevOps subscription API                            │
│     • Create/Update BusinessWorkbenchManifest CRD in D                     │
│     • Push credentials to D (stored in Secret)                             │
│                                                                              │
│  5. CONFIGURE SIGNAL ROUTING                                                │
│     • Register with Atropos for signal forwarding                          │
│     • Apply filters and source configuration                               │
│                                                                              │
│  6. UPDATE STATUS                                                           │
│     • Set phase to Bound                                                   │
│     • Record manifest version and push status                              │
│                                                                              │
│  7. SCHEDULE ROTATION (if enabled)                                          │
│     • Calculate next rotation time                                         │
│     • Schedule rotation job                                                │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Rotation Handling:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CREDENTIAL ROTATION FLOW                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. Generate new BotToken                                                   │
│  2. Push new token to D (as pending credential)                            │
│  3. Update manifest in D with new credential reference                     │
│  4. Wait for overlap period                                                │
│  5. Revoke old token                                                       │
│  6. Update status                                                          │
│                                                                              │
│  During overlap, both old and new tokens are valid                         │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Deletion Handling:**

```
When DevOpsWorkbenchBinding is deleted:
1. Revoke all tokens immediately
2. Delete BusinessWorkbenchManifest from D
3. Remove signal routing configuration
4. Clean up local resources (ServiceAccount, Secrets)
```

---

### ManifestOperator (runs in D)

**Watches:** `BusinessWorkbenchManifest` CRDs

**Reconciliation Loop:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MANIFESTOPERATOR RECONCILIATION                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. VALIDATE                                                                │
│     • Check manifest is from authorized source                             │
│     • Validate credential Secret exists                                    │
│     • Check credential is not expired                                      │
│                                                                              │
│  2. REGISTER MACHINE                                                        │
│     • Create Machine resource for {workbench-name}-gateway                 │
│     • Configure endpoint and authentication                                │
│                                                                              │
│  3. CREATE TOOL BINDINGS                                                    │
│     • For each tool in manifest, create Tool resource                      │
│     • Bind tools to the Machine                                            │
│     • Make tools available to DevOps scenarios                             │
│                                                                              │
│  4. STORE CREDENTIALS                                                       │
│     • Validate credential Secret is properly formatted                     │
│     • Configure Machine to use credentials                                 │
│                                                                              │
│  5. HEALTH CHECK                                                            │
│     • Verify gateway endpoint is reachable                                 │
│     • Test tool invocations                                                │
│                                                                              │
│  6. UPDATE STATUS                                                           │
│     • Set phase to Active                                                  │
│     • Record machine and tool status                                       │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Credential Rotation Handling:**

```
When new credentials are pushed:
1. Validate new credential Secret
2. Update Machine with new credentials
3. Verify connectivity with new credentials
4. Mark old credentials as deprecated
```

**Expiry Handling:**

```
When manifest expires:
1. Set phase to Expired
2. Disable Machine (tools unavailable)
3. Notify DevOps admin
4. Wait for renewed manifest from A
```

---

## Security Model

### Permission Scoping

The BotToken generated in A is scoped to only the exposed resources:

```yaml
# ServiceAccount permissions (generated by operator)
apiVersion: hub.olympus.io/v1
kind: ServiceAccountPermissions
metadata:
  name: dispute-devops-binding-sa
  namespace: acme-bank
spec:
  permissions:
    # Knowledge Bank
    - resource: knowledge-bank
      actions: [read]
      scope:
        collections: ["*"]
    
    # Enterprise Memory
    - resource: enterprise-memory
      actions: [read]
      scope:
        levels: [workbench, scenario]
    
    # Data Stores
    - resource: ganymede
      actions: [read]
      scope:
        collections: ["*"]
    
    - resource: callisto
      actions: [read]
      scope:
        namespaces: [config, cache]
    
    - resource: europa
      actions: [read]
      scope:
        schemas: [dispute_data]
    
    # CAF Records
    - resource: caf
      actions: [read]
      scope:
        record_types: [DecisionRecord, EvidenceBundle, OutcomeRecord, OverrideRecord]
    
    # Scenario Metadata
    - resource: scenarios
      actions: [read]
```

### Audit Trail

All access via the gateway is logged:

```json
{
  "event_type": "devops_gateway_access",
  "timestamp": "2026-01-09T15:30:00Z",
  "source": {
    "workbench_id": "dispute-devops",
    "agent_id": "pa-assistant",
    "request_id": "devops-req-12345"
  },
  "target": {
    "workbench_id": "dispute-ops-dev",
    "resource": "knowledge-bank",
    "action": "query",
    "parameters": {
      "collection": "sops",
      "query": "refund eligibility"
    }
  },
  "result": {
    "status": "success",
    "items_returned": 5
  }
}
```

---

---

## CRD Publishing Workflow (Git-Based)

DevOps agents create and update specifications by committing CRDs to the Business Workbench's Git repository. This follows the GitOps philosophy where Git is the source of truth.

### Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    GIT-BASED CRD PUBLISHING                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  DEVOPS WORKBENCH (D)                      BUSINESS WORKBENCH (A)           │
│                                                                              │
│  ┌─────────────────────────┐              ┌─────────────────────────────┐   │
│  │ {workbench}-gateway     │              │  Resource Gateway           │   │
│  │ (Machine for queries)   │  ────────▶   │  (Knowledge, Memory, etc.)  │   │
│  └─────────────────────────┘    READ      └─────────────────────────────┘   │
│                                                                              │
│  ┌─────────────────────────┐              ┌─────────────────────────────┐   │
│  │ {workbench}-git         │              │  Git Repository             │   │
│  │ (Machine for CRDs)      │  ────────▶   │  crds/                      │   │
│  └─────────────────────────┘    WRITE     │  ├── scenarios/             │   │
│                                 (commit)  │  ├── applications/          │   │
│                                           │  ├── registry/              │   │
│                                           │  └── seer/                  │   │
│                                           └──────────────┬──────────────┘   │
│                                                          │                  │
│                                                          ▼                  │
│                                           ┌─────────────────────────────┐   │
│                                           │  Hub Operators              │   │
│                                           │  (Reconcile CRDs → State)   │   │
│                                           └─────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CRD PUBLISHING WORKFLOW                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  DEVOPS WORKBENCH (D)                      BUSINESS WORKBENCH (A) GIT       │
│                                                                              │
│  1. DevOps Scenario runs                                                    │
│     (e.g., scenario-drafting)                                               │
│                                                                              │
│  2. AI Agent generates CRD content                                          │
│     ┌─────────────────────────┐                                             │
│     │ ScenarioNormativeSpec   │                                             │
│     │ {                       │                                             │
│     │   name: "refund-check"  │                                             │
│     │   tasks: [...]          │                                             │
│     │   roles: [...]          │                                             │
│     │ }                       │                                             │
│     └─────────────────────────┘                                             │
│                                                                              │
│  3. Agent creates feature branch (git_create_branch)                        │
│     Branch: devops/scenario-refund-check                                    │
│                                                                              │
│  4. Agent commits CRD file (git_commit_crd)                                 │
│     File: crds/scenarios/refund-check.yaml                                  │
│     ───────────────────────────────────────────────────────────────────▶    │
│                                                                              │
│  5. Agent pushes branch (git_push)                                          │
│     ───────────────────────────────────────────────────────────────────▶    │
│                                                                              │
│  6. Agent creates Pull Request (git_create_pr)                              │
│     ───────────────────────────────────────────────────────────────────▶    │
│                                            ┌─────────────────────────┐      │
│                                            │ Pull Request #42        │      │
│                                            │ "[DevOps] Add scenario  │      │
│                                            │  refund-check"          │      │
│                                            │ Reviewers: @pa-team     │      │
│                                            └─────────────────────────┘      │
│                                                                              │
│                                            7. PA reviews PR in Git UI       │
│                                                                              │
│                                            8. PA approves and merges        │
│                                                                              │
│                                            9. Operators reconcile:          │
│                                               ┌─────────────────────────┐   │
│                                               │ ScenarioNormativeSpec   │   │
│                                               │ applied to Hub          │   │
│                                               └─────────────────────────┘   │
│                                                                              │
│ 10. Merge event signal (via CI integration)                                 │
│     ◀───────────────────────────────────────────────────────────────────    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### CRD Types by Persona

| Persona | CRDs They Review (PR Approver) | CRDs Their AI Agent Creates |
|---------|--------------------------------|----------------------------|
| **Process Architect** | ScenarioNormativeSpec, SOPDocumentSpec | Intent → Scenario conversion |
| **Developer** | ScenarioAutomationSpec, ScenarioDeploymentSpec, HubApplicationSpec, TriggerSpec, Seer Agent Specs | Scaffolded apps, automation config |
| **Tenant Admin** | MachineDefinition, MachineInstance, ToolDefinition, ToolInstance, DataStore specs | Infrastructure provisioning |

### PR-Based Approval Workflow

Since CRDs are committed to Git, approval happens through the standard Pull Request workflow:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PR APPROVAL WORKFLOW                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. DevOps Agent commits CRD to feature branch                              │
│     └── Branch: devops/scenario-refund-check                                │
│                                                                              │
│  2. Agent creates Pull Request                                              │
│     └── Title: "[DevOps] Add ScenarioNormativeSpec: refund-check"          │
│     └── Labels: [devops, scenario, pa-review]                               │
│     └── Reviewers: Assigned based on CRD type                               │
│                                                                              │
│  3. Git platform triggers CI checks                                         │
│     └── CRD schema validation                                               │
│     └── Lint checks                                                         │
│     └── Dependency validation                                               │
│                                                                              │
│  4. Human reviewer (PA/Dev/Admin) reviews PR                                │
│     └── Can view diff, add comments, request changes                        │
│     └── Can edit CRD directly in branch                                     │
│                                                                              │
│  5. Reviewer approves and merges                                            │
│     └── Merge to main triggers operator reconciliation                      │
│                                                                              │
│  6. Operators apply CRD to Hub state                                        │
│                                                                              │
│  7. Merge event signal sent back to DevOps Workbench                        │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Reviewer Assignment Rules

| CRD Type | Auto-Assigned Reviewers | Labels |
|----------|-------------------------|--------|
| ScenarioNormativeSpec, SOPDocumentSpec | `@pa-team` | `pa-review`, `normative` |
| ScenarioAutomationSpec, HubApplicationSpec, TriggerSpec | `@dev-team` | `dev-review`, `automation` |
| Seer Agent Specs (Training, Employment) | `@dev-team`, `@seer-team` | `dev-review`, `seer` |
| MachineDefinition, ToolDefinition | `@admin-team` | `admin-review`, `registry` |
| DataStore specs | `@admin-team`, `@dba-team` | `admin-review`, `infrastructure` |

### Auto-Merge Conditions

PRs can be auto-merged if all CI checks pass AND:

| Condition | Description |
|-----------|-------------|
| `labels.contains('draft')` | Draft specs — will be reviewed later |
| `labels.contains('auto-approve')` | Explicitly marked for auto-merge |
| `change_type == 'docs-only'` | Only documentation/comments changed |
| `confidence >= 0.95 AND change_type == 'minor'` | High-confidence minor updates |

---

## Usage Example

### DevOps Agent Accessing Business Workbench Knowledge

```python
# In a DevOps scenario (e.g., scenario-drafting)
# PA Assistant Agent needs to understand existing SOPs

# 1. Agent uses the gateway machine tool
result = await tools.invoke(
    machine="dispute-ops-dev-gateway",
    tool="query_knowledge",
    input={
        "collection": "sops",
        "query": "refund eligibility check",
        "limit": 5
    }
)

# 2. Agent uses the knowledge to draft scenario
existing_sops = result["results"]
scenario_draft = await draft_scenario(
    charter=context.charter,
    reference_sops=existing_sops
)
```

---

## Related Documentation

- [DevOps Workbench Overview](./README.md)
- [DevOps Workbench Reference](./devops-workbench-reference.md)
- [Signal Routing via Atropos](./signal-routing-via-atropos.md)
- [Workbench as Machine](../workbench-as-a-machine.md)
- [Machine Registry](../../04-subsystems/registry-services/machine-registry.md)

