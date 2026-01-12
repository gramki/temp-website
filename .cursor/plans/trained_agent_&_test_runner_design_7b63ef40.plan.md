---
name: Trained Agent & Test Runner Design
overview: Create C2-level (Container) design documentation for Trained Agent Lifecycle Manager and Agent Test Runner subsystems, following the patterns established by Seer Sidecar and Raw Agent Lifecycle Manager designs. Both subsystems will have C2-level conceptual design with C3-level detail for critical mechanisms.
todos:
  - id: training-spec-manager
    content: Create C2-level design for Training Spec Manager covering spec structure, validation rules, Raw Agent compatibility, immutability enforcement
    status: pending
  - id: trained-agent-directory
    content: Create C2-level design for Trained Agent Directory covering registry, search by capabilities, version tracking, Employed Agents Discovery queries
    status: pending
  - id: trained-agent-operators
    content: Create C2-level design for Trained Agent Operators covering lifecycle management, state transitions (Drafted→Validated→Published→Active→Archived)
    status: pending
  - id: trained-agent-levers
    content: Create C2-level design for Trained Agent Levers covering publish/unpublish, deprecation, version freeze, impact on derived Employed Agents
    status: pending
  - id: training-feedback-services
    content: Create C2-level design for Training Feedback Services covering COS/Developer feedback, APO/PA feedback, team feedback routing
    status: pending
  - id: talm-scope
    content: Create SCOPE.md for trained-agent-lifecycle-manager with coverage summary, design status, intended depth
    status: pending
    dependencies:
      - training-spec-manager
      - trained-agent-directory
      - trained-agent-operators
      - trained-agent-levers
      - training-feedback-services
  - id: talm-readme
    content: Update trained-agent-lifecycle-manager/README.md with design documents table, architecture diagram, key design decisions
    status: pending
    dependencies:
      - talm-scope
  - id: test-deployment-jobs
    content: Create C2-level design for Test Deployment Jobs covering temporary Employment Spec generation, sandbox workbench deployment, teardown
    status: pending
  - id: behavior-validations
    content: Create C2-level design for Behavior Validations covering consistency checks, quality checks, assertion types
    status: pending
  - id: health-validations
    content: Create C2-level design for Health Validations covering pod health, model connectivity, memory stability checks
    status: pending
  - id: safety-validations
    content: Create C2-level design for Safety Validations covering guardrail enforcement, prohibited action blocking, safety assertions
    status: pending
  - id: atr-scope
    content: Create SCOPE.md for agent-test-runner with coverage summary, MVP vs parked scope, Hub Test Runner extension details
    status: pending
    dependencies:
      - test-deployment-jobs
      - behavior-validations
      - health-validations
      - safety-validations
  - id: atr-readme
    content: Update agent-test-runner/README.md with design documents table, Hub Test Runner relationship, key design decisions
    status: pending
    dependencies:
      - atr-scope
  - id: update-parked-capabilities
    content: Update agent-test-runner/parked-capabilities.md to reference new SCOPE.md and clarify MVP boundary
    status: pending
    dependencies:
      - atr-scope
---

# Trained Agent Lifecycle Manager & Agent Test Runner Detailed Design

Create comprehensive C2-level design documentation for two subsystems: **Trained Agent Lifecycle Manager** and **Agent Test Runner**. Follow the patterns established by the [Seer Sidecar design](.cursor/plans/seer_sidecar_detailed_design_cc77614a.plan.md) and [Raw Agent Subsystems design](.cursor/plans/raw_agent_subsystems_design_0cdeffd5.plan.md).

## Subsystem 1: Trained Agent Lifecycle Manager

Follow the same sub-component pattern as Raw Agent Lifecycle Manager, with parallel structure:

```mermaid
flowchart TB
    subgraph TALM[Trained Agent Lifecycle Manager]
        TSM[Training Spec Manager]
        TAD[Trained Agent Directory]
        TAO[Trained Agent Operators]
        TAL[Trained Agent Levers]
        TFS[Training Feedback Services]
    end
    
    subgraph External[External Systems]
        RALM[Raw Agent Lifecycle Manager]
        ALM[Agent Lifecycle Manager]
        SeerOp[Seer Operator]
        ATR[Agent Test Runner]
    end
    
    RALM -->|"Raw Agent capabilities"| TSM
    TSM --> TAD
    TSM --> SeerOp
    TAO --> TAD
    TAL --> TAD
    TFS --> TSM
    TAD -->|"Employed Agent Discovery"| ALM
    TSM --> ATR
```

### Sub-Components

| Component | Description | Key Capabilities |

|-----------|-------------|------------------|

| **Training Spec Manager** | Training Spec CRD structure, validation rules, Raw Agent compatibility | Spec structure, validation, immutability enforcement (guardrails) |

| **Trained Agent Directory** | Registry, search, Employed Agents Discovery | Search by capabilities, version tracking, dependency queries |

| **Trained Agent Operators** | Lifecycle management via Seer Operator | Registration, validation, versioning, state transitions |

| **Trained Agent Levers** | Publication controls, version management | Publish/unpublish, deprecation, version freeze (affects derived Employed Agents) |

| **Training Feedback Services** | Feedback collection and routing | COS/Developer feedback, APO/PA feedback, team feedback on improvements |

### Key Design Decisions

- **Guardrail Immutability**: Training Spec guardrails are immutable once published (cannot be relaxed at Employment)
- **Raw Agent Integration**: Training Specs reference Raw Agents; Raw Agent capabilities constrain Training Spec options
- **Seer Operator Boundary**: TALM is business logic; Seer Operator reconciles CRDs to Kubernetes state
- **Employed Agent Discovery**: Query capability in Directory (not separate service)

### Files to Create

| File | Description |

|------|-------------|

| [`trained-agent-lifecycle-manager/training-spec-manager.md`](olympus-seer-docs/seer-design/subsystems/trained-agent-lifecycle-manager/training-spec-manager.md) | Spec structure, validation, Raw Agent compatibility |

| [`trained-agent-lifecycle-manager/trained-agent-directory.md`](olympus-seer-docs/seer-design/subsystems/trained-agent-lifecycle-manager/trained-agent-directory.md) | Registry, search, Employed Agent discovery |

| [`trained-agent-lifecycle-manager/trained-agent-operators.md`](olympus-seer-docs/seer-design/subsystems/trained-agent-lifecycle-manager/trained-agent-operators.md) | Lifecycle management, state transitions |

| [`trained-agent-lifecycle-manager/trained-agent-levers.md`](olympus-seer-docs/seer-design/subsystems/trained-agent-lifecycle-manager/trained-agent-levers.md) | Publication controls, deprecation |

| [`trained-agent-lifecycle-manager/training-feedback-services.md`](olympus-seer-docs/seer-design/subsystems/trained-agent-lifecycle-manager/training-feedback-services.md) | Feedback collection from COS, Developer, APO/PA, team |

| [`trained-agent-lifecycle-manager/SCOPE.md`](olympus-seer-docs/seer-design/subsystems/trained-agent-lifecycle-manager/SCOPE.md) | Coverage summary, design status |

---

## Subsystem 2: Agent Test Runner

Extends Hub Test Runner with agent-specific testing capabilities for temporary Employed Agent deployments in sandbox workbench instances.

```mermaid
flowchart TB
    subgraph ATR[Agent Test Runner]
        TDJ[Test Deployment Jobs]
        BV[Behavior Validations]
        HV[Health Validations]
        SV[Safety Validations]
    end
    
    subgraph HubTR[Hub Test Runner]
        TS[Test Suite CRD]
        TE[Test Execution]
        TR[Test Results]
    end
    
    subgraph Sandbox[Sandbox Environment]
        SWI[Sandbox Workbench Instance]
        TEA[Temporary Employed Agent]
    end
    
    ATR -->|extends| HubTR
    TDJ -->|deploys| TEA
    TEA -->|runs in| SWI
    BV --> TEA
    HV --> TEA
    SV --> TEA
```

### MVP Scope (Validations)

| Validation Type | Description | Go/No-Go Check |

|-----------------|-------------|----------------|

| **Behavior Consistency** | Agent responds consistently to same inputs | Pass/Fail |

| **Behavior Quality** | Basic output quality checks (completeness, format) | Pass/Fail |

| **Health** | Pod health, model connectivity, memory stability | Pass/Fail |

| **Safety** | Guardrail enforcement, prohibited actions blocked | Pass/Fail |

### Parked Scope (Evaluations) - Deferred per ADR-0077

- Quality scoring and benchmarks
- Regression testing across versions
- Adversarial testing
- CI/CD quality gates

### Key Design Decisions

- **Temporary Deployment Model**: Creates temporary Employment Spec + deploys in sandbox workbench
- **Extends Hub Test Runner**: Adds agent-specific Test CRD types and assertions
- **Sandbox Isolation**: All tests run in sandbox workbench instances with isolated data

### Files to Create

| File | Description |

|------|-------------|

| [`agent-test-runner/test-deployment-jobs.md`](olympus-seer-docs/seer-design/subsystems/agent-test-runner/test-deployment-jobs.md) | Temporary Employed Agent deployment for testing |

| [`agent-test-runner/behavior-validations.md`](olympus-seer-docs/seer-design/subsystems/agent-test-runner/behavior-validations.md) | Consistency and quality validations |

| [`agent-test-runner/health-validations.md`](olympus-seer-docs/seer-design/subsystems/agent-test-runner/health-validations.md) | Pod health, connectivity, stability checks |

| [`agent-test-runner/safety-validations.md`](olympus-seer-docs/seer-design/subsystems/agent-test-runner/safety-validations.md) | Guardrail enforcement validation |

| [`agent-test-runner/SCOPE.md`](olympus-seer-docs/seer-design/subsystems/agent-test-runner/SCOPE.md) | Coverage summary, MVP vs parked scope |

---

## Integration Points

### Trained Agent Lifecycle Manager

| Integration | Direction | Purpose |

|-------------|-----------|---------|

| Raw Agent Lifecycle Manager | Inbound | Raw Agent capabilities constrain Training Spec |

| Agent Lifecycle Manager | Outbound | Employed Agent Discovery queries |

| Seer Operator | Outbound | CRD reconciliation |

| Agent Test Runner | Outbound | Training Spec validation testing |

| Context Compiler | Outbound | Retriever configurations in Training Spec |

### Agent Test Runner

| Integration | Direction | Purpose |

|-------------|-----------|---------|

| Hub Test Runner | Extends | Test Suite CRD, execution framework |

| Trained Agent Lifecycle Manager | Inbound | Training Spec for test deployment |

| Agent Runtime | Outbound | Temporary Employed Agent deployment |

| Sandbox Workbench | Outbound | Test execution environment |

---

## Implementation Details Deferred

Following the pattern from other subsystem designs:

- Detailed CRD schemas
- Complete API specifications (REST/gRPC endpoints)
- Storage backends and indexing strategies
- Specific algorithm implementations
- Error code taxonomies
- Wire format details