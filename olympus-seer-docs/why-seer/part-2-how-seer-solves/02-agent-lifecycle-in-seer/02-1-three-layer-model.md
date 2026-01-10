# 2.1 The Three-Layer Model in Seer

Seer implements the Raw, Trained, Employed agent lifecycle model through a combination of specification artifacts, CRD definitions, and runtime services. This section details how each layer is realized in the Seer platform.

## Implementation Overview

| Layer | Seer Artifact | Key Characteristics |
|-------|---------------|---------------------|
| **Raw Agent** | Container image + Raw Agent manifest | Deployable technical artifact with infrastructure identity |
| **Trained Agent** | Training Specification CRD | Configuration with knowledge, skills, guardrails |
| **Employed Agent** | Employment Specification CRD | Delegated authority for specific work context |

## Raw Agent Implementation

A Raw Agent in Seer is defined by:

### Container Image

The deployable artifact—a container image that includes:
- Orchestration code (agent loop implementation)
- Model integration libraries
- Memory access SDKs
- Tool invocation framework
- Observability instrumentation

### Raw Agent Manifest

A declaration of the agent's technical capabilities:

```yaml
apiVersion: seer.olympus.io/v1
kind: RawAgent
metadata:
  name: dispute-analyst-raw
  version: 2.4.1
spec:
  image: registry.zeta.io/seer/dispute-analyst:v2.4.1
  capabilities:
    modalities: [text, structured-data]
    patterns: [reasoning, tool-calling, multi-turn]
    models:
      supported: [gpt-4o, gpt-4o-mini, claude-3-5-sonnet]
  identity:
    type: spiffe
    trustDomain: platform.zeta.io
  resources:
    limits:
      concurrency: 100
      memory: 4Gi
      cpu: 2
```

### What Raw Agents Provide

- Technical execution capabilities (orchestration, model access)
- Infrastructure identity (SPIFFE, workload identity)
- Capacity constraints and resource limits
- Supported model list
- Channel compatibility (HTTP, gRPC, WebSocket)

### What Raw Agents Do Not Have

- Organizational knowledge
- Domain-specific skills
- Operational authority
- Business context

## Trained Agent Implementation

A Trained Agent is created by applying a Training Specification to a Raw Agent:

### Training Specification CRD

```yaml
apiVersion: seer.olympus.io/v1
kind: TrainingSpec
metadata:
  name: dispute-analyst-training
  version: 1.7.0
spec:
  rawAgent:
    name: dispute-analyst-raw
    versionConstraint: "^2.0.0"
  
  knowledge:
    sources:
      - type: knowledge-base
        ref: dispute-policies-v3
      - type: knowledge-base
        ref: regulatory-requirements-v2
  
  skills:
    - name: dispute-triage
      procedure: procedures/dispute-triage-v1
    - name: evidence-evaluation
      procedure: procedures/evidence-eval-v1
  
  prompts:
    system: prompts/dispute-analyst-system-v2
    style: formal-financial
    tone: professional
  
  guardrails:
    - ref: safety/no-financial-advice
    - ref: compliance/data-privacy
    - ref: operations/escalation-required
  
  tools:
    allowed:
      - protocol: case-lookup
      - protocol: customer-info
      - protocol: evidence-retrieval
  
  models:
    allowed: [gpt-4o, claude-3-5-sonnet]
    preferred: gpt-4o
```

### What Training Specifications Define

| Component | Purpose |
|-----------|---------|
| **Knowledge Binding** | Which knowledge sources the agent can access |
| **Skills** | Procedural capabilities and workflows |
| **Prompts** | System instructions, style, and tone |
| **Guardrails** | Immutable behavioral constraints |
| **Tools** | Which tool protocols the agent can use |
| **Models** | Which LLMs are permitted |

### Training Specification Versioning

Training Specifications follow semantic versioning:
- **Major:** Breaking changes to behavior or capabilities
- **Minor:** New capabilities, backward-compatible
- **Patch:** Bug fixes, minor refinements

## Employed Agent Implementation

An Employed Agent is created by applying an Employment Specification to a Trained Agent:

### Employment Specification CRD

```yaml
apiVersion: seer.olympus.io/v1
kind: EmploymentSpec
metadata:
  name: dispute-analyst-acme-production
  version: 3.2.0
spec:
  trainedAgent:
    name: dispute-analyst-training
    versionConstraint: "~1.7.0"
  
  workbench: acme-disputes
  
  workScope:
    scenarios: [dispute-resolution, customer-inquiry]
    temporal: continuous
    functional: tier-1-disputes
  
  authority:
    delegation:
      type: role
      role: dispute-analyst
      manager: disputes-team-lead
    ceilings:
      maxDecisionValue: 1000
      requiresApproval:
        - type: refund
          threshold: 500
  
  environment:
    tools:
      case-lookup:
        instance: acme-case-management
        credentials:
          secretRef: acme-case-api-key
      customer-info:
        instance: acme-customer-service
        credentials:
          secretRef: acme-customer-api-key
  
  resources:
    budget:
      monthly: 500
      perRequest: 2
    quota:
      dailySessions: 1000
  
  models:
    allowed: [gpt-4o]  # Further restricted from Training
```

### What Employment Specifications Define

| Component | Purpose |
|-----------|---------|
| **Workbench Binding** | Which business context the agent operates within |
| **Work Scope** | Scenarios, temporal scope, functional boundaries |
| **Authority** | Delegation model, ceilings, approval requirements |
| **Environment** | Concrete tool bindings, credentials, endpoints |
| **Resources** | Budget, quotas, capacity allocation |
| **Models** | Further restriction of allowed models |

### The Narrowing Constraint

Employment can only narrow what Training permits:
- Cannot add tools not in Training
- Cannot remove guardrails from Training
- Cannot expand model list beyond Training
- Cannot exceed authority limits from Training

## Lifecycle Service Integration

Seer's Agent Definition & Lifecycle Service manages all three layers:

| Function | Description |
|----------|-------------|
| **Specification Storage** | Version-controlled storage of all specs |
| **Validation** | Schema and constraint validation on submission |
| **Binding** | Linking Employment to Training to Raw |
| **State Management** | Tracking active/suspended/retired status |
| **Audit** | Recording all specification changes |

---

**References:**
*   `aosm-meta-model/raw-trained-employed-agents.md`
*   `olympus-seer-docs/seer-design/hub-integration/training-spec-crd.md`
*   `olympus-seer-docs/seer-design/hub-integration/employment-spec-crd.md`
