# Training Spec CRD

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-11  
> **Parent**: [Seer-Hub Integration](./README.md)

---

## Overview

The **TrainingSpec CRD** defines a Trained Agent — a Raw Agent configured with organizational knowledge, domain-specific skills, prompts, and referenced capabilities. This CRD is managed by the **Seer Operator**.

---

## Naming Conventions

### Resource Naming

| Pattern | Example | Description |
|---------|---------|-------------|
| `{agent-name}-v{version}` | `dispute-triage-agent-v1` | Standard versioned training |
| `{agent-name}-{domain}-v{version}` | `analyst-disputes-v1` | Domain-scoped training |

### Display Name

Use pattern: `"{Name} (Training Spec)"` or include in `spec.context.identity.displayName`.

### Required Labels

```yaml
labels:
  seer.olympus.io/resource-type: training-spec
  seer.olympus.io/domain: {domain-name}
  seer.olympus.io/agent-type: {case-worker|orchestrator|specialist}
  seer.olympus.io/role: {role-name}
```

### Recommended Annotations

```yaml
annotations:
  seer.olympus.io/source-scenario: "{scenario-name}"
  seer.olympus.io/source-workbench: "{workbench-name}"
  seer.olympus.io/genesis-date: "{date}"
  seer.olympus.io/conceived-by: "{persona}: {identity}"
```

---

## CRD Definition

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: trainingspecs.seer.olympus.io
spec:
  group: seer.olympus.io
  names:
    kind: TrainingSpec
    listKind: TrainingSpecList
    plural: trainingspecs
    singular: trainingspec
    shortNames:
      - ts
      - training
  scope: Namespaced
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          required:
            - spec
          properties:
            spec:
              $ref: '#/components/schemas/TrainingSpecSpec'
            status:
              $ref: '#/components/schemas/TrainingSpecStatus'
```

---

## Full Schema

```yaml
apiVersion: seer.olympus.io/v1
kind: TrainingSpec
metadata:
  name: fraud-analyst-v2
  namespace: acme-disputes
  labels:
    seer.olympus.io/domain: disputes
    seer.olympus.io/role: case-analyst
    app.kubernetes.io/version: "1.7.0"
  annotations:
    seer.olympus.io/description: "Fraud case analysis agent for dispute resolution"
    seer.olympus.io/owner: disputes-team

spec:
  # ============================================================
  # RAW AGENT REFERENCE
  # ============================================================
  rawAgent:
    # Reference to the Raw Agent container
    name: fraud-analyst-base
    version: "^2.0.0"              # Semver range
    registry: registry.olympus.io
    repository: seer/agents/fraud-analyst

  # ============================================================
  # CONTEXT DEFINITIONS
  # ============================================================
  context:
    # Agent identity and role
    identity:
      displayName: "Fraud Case Analyst"
      description: "AI agent specialized in fraud case analysis and resolution"
      role: case-analyst
      domain: disputes
    
    # PIDA mapping (Perceive, Interpret, Decide, Act)
    pida:
      perceive:
        - "Transaction data and patterns"
        - "Customer communication"
        - "Historical case information"
        - "Policy documents"
      interpret:
        - "Assess fraud likelihood"
        - "Identify risk factors"
        - "Evaluate evidence strength"
      decide:
        - "Recommend case outcome"
        - "Suggest investigation steps"
        - "Determine escalation need"
      act:
        - "Update case status"
        - "Request additional information"
        - "Escalate to human reviewer"

  # ============================================================
  # BEHAVIORAL CONFIGURATION
  # ============================================================
  behavioral:
    # System prompt (core agent persona)
    systemPrompt: |
      You are a Fraud Case Analyst AI agent working for ACME Bank's 
      Disputes Resolution team.
      
      Your role is to analyze fraud cases, assess evidence, and 
      recommend appropriate actions while ensuring compliance with 
      bank policies and regulatory requirements.
      
      Always:
      - Be thorough in your analysis
      - Cite evidence for your conclusions
      - Escalate when uncertain
      - Protect customer privacy
    
    # Skill prompts (task-specific instructions)
    skillPrompts:
      - name: analyze-transaction
        description: "Analyze a transaction for fraud indicators"
        prompt: |
          When analyzing a transaction:
          1. Check velocity patterns (frequency, amount trends)
          2. Verify device and location consistency
          3. Compare against customer's historical behavior
          4. Identify any known fraud patterns
          
          Provide a fraud likelihood score (0-1) with reasoning.
      
      - name: draft-customer-response
        description: "Draft response to customer inquiry"
        prompt: |
          When responding to the customer:
          1. Acknowledge their concern
          2. Summarize the investigation status
          3. Explain next steps clearly
          4. Provide expected timeline
          
          Tone: Professional, empathetic, clear.
      
      - name: recommend-outcome
        description: "Recommend case resolution"
        prompt: |
          When recommending a case outcome:
          1. Summarize the evidence
          2. Apply relevant policies
          3. Consider precedents
          4. Provide clear recommendation with confidence level
          
          If confidence < 0.7, recommend human review.
    
    # Style guidelines
    style:
      tone: professional
      verbosity: concise
      formality: formal
      languagePreference: en-US

  # ============================================================
  # GUARDRAIL REFERENCES (Immutable at Employment)
  # ============================================================
  guardrails:
    # Referenced guardrail definitions
    refs:
      - name: pii-protection
        version: "^1.0.0"
        namespace: platform-guardrails
      
      - name: financial-compliance
        version: "^2.1.0"
        namespace: acme-guardrails
      
      - name: escalation-triggers
        version: "^1.2.0"
        namespace: acme-guardrails
    
    # Inline guardrails (also immutable)
    inline:
      - name: amount-threshold
        type: decision-boundary
        config:
          maxAutonomousApproval: 5000
          requiresHumanAbove: 5000
          currency: USD
      
      - name: prohibited-actions
        type: action-block
        config:
          blocked:
            - "close_account"
            - "reverse_transaction_above_limit"
            - "modify_customer_data"

  # ============================================================
  # TOOL REFERENCES (Normative)
  # ============================================================
  tools:
    # Tool protocols (abstract, resolved at employment)
    protocols:
      - protocol: temenos-t24/get-transactions
        alias: get_transactions
        description: "Retrieve customer transaction history"
        permissions:
          - read
        usage: |
          Use to fetch transaction history for analysis.
          Specify date range and account ID.
      
      - protocol: fraud-engine/evaluate
        alias: check_fraud_rules
        description: "Evaluate transaction against fraud rules"
        permissions:
          - read
        usage: |
          Use to get rule-based fraud assessment.
          Returns rule matches and risk score.
      
      - protocol: case-management/update-status
        alias: update_case
        description: "Update case status and notes"
        permissions:
          - write
        usage: |
          Use to record investigation progress.
          Include rationale for status changes.
    
    # Hub-native tools
    hubTools:
      - name: memory.search_precedent
        description: "Search similar past cases"
      - name: memory.get_case_history
        description: "Get current case history"
      - name: knowledge.search
        description: "Search policy documents"

  # ============================================================
  # KNOWLEDGE BASE REFERENCES
  # ============================================================
  knowledge:
    bases:
      - name: dispute-policies
        ref: dispute-policies-kb
        namespace: acme-knowledge
        description: "Bank dispute resolution policies"
        retrievalStrategy:
          type: semantic
          topK: 5
          minScore: 0.7
      
      - name: fraud-patterns
        ref: fraud-patterns-kb
        namespace: acme-knowledge
        description: "Known fraud patterns and indicators"
        retrievalStrategy:
          type: hybrid
          topK: 10
          semanticWeight: 0.7
          keywordWeight: 0.3
      
      - name: regulatory-requirements
        ref: reg-requirements-kb
        namespace: platform-knowledge
        description: "Regulatory compliance requirements"
        retrievalStrategy:
          type: semantic
          topK: 3

  # ============================================================
  # MEMORY CONFIGURATION
  # ============================================================
  memory:
    # Agent Memory store requirements
    agentMemory:
      stores:
        - name: case-dialog
          type: conversation
          compaction:
            strategy: summarize
            tokenBudget: 4000
            summarizeAfter: 20
        
        - name: case-entities
          type: kv
          description: "Extracted entities from current case"
        
        - name: session-audit
          type: log
          ragEnabled: true
          description: "Session action audit trail"
    
    # Enterprise Memory access patterns
    enterpriseMemory:
      read:
        - type: episodic
          purpose: "Search precedents"
        - type: semantic
          purpose: "Access learned patterns"
      write:
        - type: episodic
          records:
            - DecisionRecord
            - EvidenceRecord
            - OutcomeRecord

  # ============================================================
  # EVALUATION CONFIGURATION
  # ============================================================
  evaluation:
    # Sandbox test scenarios
    scenarios:
      - name: standard-fraud-case
        description: "Typical unauthorized transaction case"
        expectedBehaviors:
          - "Analyzes transaction patterns"
          - "Identifies fraud indicators"
          - "Recommends appropriate action"
      
      - name: edge-case-high-value
        description: "High-value transaction requiring escalation"
        expectedBehaviors:
          - "Recognizes amount threshold"
          - "Escalates to human reviewer"
    
    # Quality metrics
    metrics:
      - name: accuracy
        target: 0.85
        evaluator: human-review
      - name: policy-compliance
        target: 1.0
        evaluator: rule-based
      - name: response-time
        target: 30s
        evaluator: automated

  # ============================================================
  # VERSIONING
  # ============================================================
  version:
    spec: "1.7.0"
    compatibility:
      rawAgent: "^2.0.0"
      guardrails:
        pii-protection: "^1.0.0"
        financial-compliance: "^2.1.0"

status:
  # Managed by Seer Operator
  state: Published          # Drafted | Validated | Published | Active | Archived
  publishedAt: "2026-01-08T10:00:00Z"
  activeEmployments: 3
  lastValidation:
    timestamp: "2026-01-07T15:30:00Z"
    result: passed
    scenarios: 5/5
  conditions:
    - type: Ready
      status: "True"
      lastTransitionTime: "2026-01-08T10:00:00Z"
    - type: Validated
      status: "True"
      lastTransitionTime: "2026-01-07T15:30:00Z"
```

---

## Schema Reference

### spec.rawAgent

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ | Raw Agent name |
| `version` | string | ✅ | Semver version range |
| `registry` | string | ❌ | Container registry (default: platform) |
| `repository` | string | ❌ | Image repository path |

### spec.context.identity

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `displayName` | string | ✅ | Human-readable agent name |
| `description` | string | ❌ | Agent description |
| `role` | string | ✅ | Assigned role identifier |
| `domain` | string | ✅ | Business domain |

### spec.behavioral

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `systemPrompt` | string | ✅ | Core agent persona prompt |
| `skillPrompts` | array | ❌ | Task-specific instruction sets |
| `style` | object | ❌ | Communication style preferences |

### spec.guardrails

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `refs` | array | ❌ | References to Guardrail CRDs |
| `inline` | array | ❌ | Inline guardrail definitions |

> **Critical**: Guardrails are immutable once published.

### spec.tools.protocols

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `protocol` | string | ✅ | Tool protocol identifier |
| `alias` | string | ❌ | Agent-facing tool name |
| `permissions` | array | ✅ | `read`, `write`, `execute` |
| `usage` | string | ❌ | Usage instructions for agent |

### spec.memory.agentMemory.stores

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ | Logical store name |
| `type` | string | ✅ | `conversation`, `kv`, `log`, `document` |
| `compaction` | object | ❌ | For conversation stores |
| `ragEnabled` | boolean | ❌ | Enable RAG search |

---

## Lifecycle States

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Drafted   │────►│  Validated  │────►│  Published  │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                                               ▼
                    ┌─────────────┐     ┌─────────────┐
                    │   Archived  │◄────│   Active    │
                    └─────────────┘     └─────────────┘
```

| State | Description | Can Deploy? |
|-------|-------------|-------------|
| **Drafted** | In development, editable | ❌ |
| **Validated** | Passed sandbox tests | ❌ |
| **Published** | Approved, available | ✅ |
| **Active** | Has active employments | ✅ |
| **Archived** | Superseded, frozen | ❌ (new) |

---

## Operator Responsibilities

The **Seer Operator** handles:

| Responsibility | Action |
|----------------|--------|
| **Validation** | Ensure referenced Raw Agent exists and is compatible |
| **Guardrail Resolution** | Resolve and lock guardrail references |
| **State Transitions** | Manage lifecycle state changes |
| **Version Compatibility** | Verify version constraints |
| **Hub Registration** | Register as available HubApplicationSpec |

---

## Hub Integration

When a HubApplicationSpec references a TrainingSpec:

```yaml
# HubApplicationSpec
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: fraud-case-analyst
spec:
  runtime: seer
  seerTrainingRef:
    name: fraud-analyst-v2
    namespace: acme-disputes
    version: "1.7.0"
```

The Hub Operator:
1. Validates the TrainingSpec exists and is Published/Active
2. Does **not** validate TrainingSpec contents (Seer's responsibility)
3. Creates the HubApplicationSpec referencing the TrainingSpec

---

## Related Documentation

- [Agent Lifecycle Manager](../subsystems/agent-lifecycle-manager/README.md) — Employment spec management
- [Trained Agent as Hub Application](./trained-agent.md) — Hub integration
- [Employment Spec CRD](./employment-spec-crd.md) — Deployment configuration
- [Guardrails](../subsystems/agent-identity-authority.md) — Guardrail framework

---

*TrainingSpec CRD defines what an agent knows and can do — the bridge between Raw capability and organizational role.*

