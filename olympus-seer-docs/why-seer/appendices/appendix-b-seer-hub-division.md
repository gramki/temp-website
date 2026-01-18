# Appendix B: Seer + Hub Division of Responsibility

This appendix clarifies the division of responsibility between Seer and Hub—two complementary systems that together form Zeta's enterprise agent platform.

---

## The Core Distinction

> *Seer governs the agents; Hub governs the operations they perform.*

| System | Focus | Analogy |
|--------|-------|---------|
| **Seer** | The Agent | HR Department—manages workers |
| **Hub** | The Work | Operations Department—manages work |

## Responsibility Matrix

| Dimension | Seer Owns | Hub Owns |
|-----------|-----------|----------|
| **Core Focus** | Agent identity, lifecycle, behavior | Work routing, execution, outcomes |
| **Lifecycle** | Raw → Trained → Employed | Request → Operation → Outcome |
| **Identity** | Agent identity, delegation chains (enterprise and request-scoped), two-layer identity model | User identity, access control, Channels (facilitate request-scoped delegation) |
| **Runtime** | Agent execution, model gateway | Signal routing, workflow execution |
| **Control Plane** | Agent Lifecycle Service, Specs | Workbench Management, Scenarios |
| **Data Plane** | Guardrail enforcement, context assembly | Memory services, knowledge services, tools |
| **Audit** | Agent behavior records | Decision records, evidence bundles, CAF |
| **Observability** | Agent Health Score, model metrics | Request traces, task metrics |
| **Governance** | Training guardrails, authority ceilings | Escalation matrices, policies |

## Detailed Breakdown

### What Seer Owns

#### Agent Identity & Authority
- Agent identity semantics (Raw, Trained, Employed layers)
- Two-layer identity model (Deployment Identity vs Agent Persona)
- Delegation model (how authority flows from humans to agents)
  - Enterprise delegation (scenario-scoped)
  - Request-scoped delegation (via Cipher IAM Extensions)
- Authority ceilings (layered limits and their enforcement)
- Kill switch logic (when and how to revoke authority)

#### Agent Lifecycle
- TrainingSpec and EmploymentSpec management
- Persona Twin lifecycle (Raw → Trained → Employed)
- Persona Twin Blueprint structure and management
- Version management with semantic versioning
- Promotion workflows with approval gates
- Rollback with state consistency
- Graceful retirement and deprecation

#### Agent Runtime
- Agent execution within Kubernetes
- Guardrail enforcement (input, output, behavioral)
- Context assembly from multiple sources
- Token budgeting and truncation

#### Model Gateway
- Unified API across LLM/SLM providers
- Intelligent routing (task, cost, latency-aware)
- Provider fallback and high availability
- Budget enforcement and virtual keys

#### Cost Governance
- Agent Health Score (AHS) calculation
- Cost-to-Health Ratio (CHR) monitoring
- Cost ceilings at agent, scenario, workbench levels
- Cost anomaly detection

### What Hub Owns

#### Work Management
- Signal Exchange (event routing)
- Request lifecycle management
- Task Management (queues, allocation)
- Workflow execution (Rhea, ChronoShift)

#### Memory & Knowledge
- Enterprise Memory storage (via Europa)
- Agent Memory storage (via Callisto, Europa, S3)
- Enterprise Knowledge services
- ETSL (Enterprise Temporal Semantic Layer)

#### Cognitive Audit Fabric
- Memory Store Catalog
- Record schema registry
- Explanation Service
- Enterprise Learning Services

#### Tools & Integrations
- Tool Registry (protocols, instances)
- Machine Registry
- MCP Router
- MCP Server CRD management and provisioning
- MCP Directory Service
- Hub Native Utilities

#### Operational Infrastructure
- Workbench Management
- Scenario specifications
- Hub Composite Applications (multi-agent topologies)
- COGW (Cognitive Operations Governance Workbench) workbench type
- Escalation matrices
- Observer notifications

## Integration Points

Seer and Hub integrate at well-defined boundaries:

| Integration | Seer Side | Hub Side |
|-------------|-----------|----------|
| **Context** | Context Assembly Engine requests | Memory/Knowledge services respond |
| **Tools** | Agent invokes tool | Tool Registry validates, executes |
| **Audit** | Agent emits records | CAF catalogs, stores, explains |
| **Identity** | Seer defines semantics | Cipher provides infrastructure |
| **Delegation** | Request-scoped delegation model (Cipher IAM Extensions) | Channels facilitate user consent and token delivery |
| **Memory** | Agent Memory SDK | Memory Services stores |
| **Workbench** | Agent operates within | Workbench provides context |
| **Collaboration** | Agent SDK supports MCP | MCP Server CRD, MCP Directory Service |
| **Persona Twins** | Persona Twin lifecycle, blueprints | Persona Twin operations, signal routing |

## Why Two Systems?

### Separation of Concerns

| Concern | Why Separate |
|---------|--------------|
| **Agent-specific** | Agent lifecycle, guardrails, model access—not general-purpose infrastructure |
| **Work-specific** | Signals, workflows, tasks—not agent-specific |
| **Evolution** | Systems evolve at different rates |
| **Teams** | Different expertise required |

### Complementary Capabilities

Neither system is complete without the other:

| Without Seer | Without Hub |
|--------------|-------------|
| Agents with no governance | Governance with no memory |
| No lifecycle management | No knowledge services |
| No model abstraction | No audit infrastructure |
| No agent identity | No operational context |

## The Combined Value

Together, Seer + Hub provide:

1. **Complete Agent Governance:** Identity, authority, lifecycle, guardrails
2. **Complete Operational Substrate:** Memory, knowledge, tools, audit
3. **Complete Enterprise Platform:** From agent conception to operational excellence

---

**References:**
*   `olympus-seer-docs/seer-design/introduction.md`
*   `olympus-seer-docs/seer-design/hub-integration/README.md`
*   `olympus-hub-docs/README.md`
