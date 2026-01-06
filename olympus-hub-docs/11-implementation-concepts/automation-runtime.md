# Automation Runtime

> **Category:** Application Architecture

---

## Overview

An **Automation Runtime** is the execution host for Hub Applications. Each runtime is specialized for a particular automation paradigm — containers (Atlantis), workflows (Rhea), AI agents (Seer), or batch processing (Perseus). Runtimes handle deployment, scaling, observability, and lifecycle management, while Hub Applications focus on business logic.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Automation Runtime** (called "Automation System" in some contexts) as the execution platform that hosts Automations and supervises Operations. Hub implements this with multiple specialized runtimes.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Automation Runtime | Atlantis, Rhea, Seer, Perseus | Specialized runtime implementations |
| Automation | Hub Application | Application runs on a Runtime |
| Operation | Request + Application instance | Runtime hosts running operations |

### Gap This Fills

The ontology describes Automation Runtime abstractly. Hub specifies:
1. **Runtime types**: Different runtimes for different automation styles
2. **Deployment**: How applications are deployed to runtimes
3. **Scaling**: How runtimes scale with demand
4. **Integration**: How runtimes connect to Signal Exchange

---

## Definition

**Automation Runtime** is an execution platform that:
- Hosts Hub Applications
- Receives requests from Signal Exchange
- Manages application lifecycle (deploy, scale, update)
- Provides observability (logs, metrics, traces)
- Handles CI for application builds

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Platform-wide; workbenches deploy to runtimes |
| **Lifecycle** | Managed by SRE; applications deployed by Developers |
| **Ownership** | Platform owns runtimes; Developers own applications |
| **Multiplicity** | Multiple runtimes available; one per paradigm |

---

## Rationale

### Why This Design?

Multiple specialized runtimes enable:
1. **Paradigm fit**: Right tool for each automation type
2. **Optimization**: Each runtime optimized for its paradigm
3. **Choice**: Developers select best runtime for their needs
4. **Evolution**: Add new runtimes without disrupting existing

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Single universal runtime** | Cannot optimize for different paradigms |
| **Arbitrary container orchestration** | No Hub-specific integration |
| **External runtimes only** | Inconsistent experience |

---

## Structure

### Hub Automation Runtimes

| Runtime | Paradigm | Technology | Best For |
|---------|----------|------------|----------|
| **Atlantis** | Container | Knative/KServe | Custom code, microservices, ML models |
| **Rhea** | Workflow | BPMN Engine | Structured business workflows |
| **Seer** | AI Agent | Agent Engine | LLM-based agents, agentic workflows |
| **Perseus** | Batch | Batch Processing | File processing, ETL, map-reduce |
| **ChronoShift** | Durable Workflow | Temporal | Long-running, durable workflows |

### Runtime Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AUTOMATION RUNTIME ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   SIGNAL EXCHANGE                                                            │
│         │                                                                    │
│         │ Routes requests to Application                                     │
│         ▼                                                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    AUTOMATION RUNTIME                                │   │
│   │                                                                      │   │
│   │   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │   │
│   │   │  Ingress    │  │  Scaling    │  │  Lifecycle  │                │   │
│   │   │  Handler    │  │  Controller │  │  Manager    │                │   │
│   │   └──────┬──────┘  └─────────────┘  └─────────────┘                │   │
│   │          │                                                          │   │
│   │          ▼                                                          │   │
│   │   ┌─────────────────────────────────────────────────────────────┐  │   │
│   │   │                  HUB APPLICATION INSTANCES                   │  │   │
│   │   │                                                              │  │   │
│   │   │   ┌─────────┐  ┌─────────┐  ┌─────────┐                     │  │   │
│   │   │   │Instance │  │Instance │  │Instance │  ...                │  │   │
│   │   │   │   1     │  │   2     │  │   3     │                     │  │   │
│   │   │   └─────────┘  └─────────┘  └─────────┘                     │  │   │
│   │   │                                                              │  │   │
│   │   └─────────────────────────────────────────────────────────────┘  │   │
│   │          │                                                          │   │
│   │          ▼                                                          │   │
│   │   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │   │
│   │   │  Olympus    │  │  Memory     │  │  Tool       │                │   │
│   │   │  Watch      │  │  Services   │  │  Registry   │                │   │
│   │   └─────────────┘  └─────────────┘  └─────────────┘                │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Behavior

### Runtime Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **Deployment** | Deploy containers/workflows from registry |
| **Scaling** | Scale instances based on load |
| **Health** | Monitor and restart unhealthy instances |
| **Routing** | Route requests to application instances |
| **Observability** | Collect logs, metrics, traces |
| **CI** | Build and test applications |

### Application Lifecycle

```
1. DEVELOP
   └── Developer writes application code

2. BUILD
   └── Runtime CI builds container/artifact

3. PUBLISH
   └── Artifact pushed to registry

4. DEPLOY
   └── Operator triggers deployment to workbench

5. SCALE
   └── Runtime scales based on demand

6. UPDATE
   └── New version deployed (blue-green, rolling)

7. RETIRE
   └── Application deactivated when replaced
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Signal Exchange | ← receives | Requests routed to applications |
| Artifact Registry | ← pulls | Container images/artifacts |
| Olympus Watch | → sends | Logs, metrics, traces |
| Memory Services | ↔ uses | Application state and memory |
| Tool Registry | → queries | Available tools for applications |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Registry source** | Applications only from subscription registry |
| **Workbench isolation** | Applications isolated per workbench |
| **Resource limits** | Applications constrained by quotas |
| **Network policies** | Applications follow workbench network rules |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Paradigm fit** | Right runtime for each use case |
| ✅ **Managed scaling** | Platform handles scale-out/in |
| ✅ **Integrated observability** | Built-in monitoring |
| ✅ **CI integration** | Build and deploy in one flow |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Runtime selection** | Clear guidance on when to use each |
| ⚠️ **Lock-in to paradigm** | Standard interfaces; migration paths |

---

## Examples

### Example 1: Atlantis Container Runtime

```yaml
# Hub Application on Atlantis
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: dispute-handler
spec:
  runtime:
    type: atlantis
    
  container:
    image: "registry.../dispute-handler:1.2.0"
    
  resources:
    cpu: "500m"
    memory: "512Mi"
    
  scaling:
    min_instances: 1
    max_instances: 10
    target_cpu_utilization: 70
    
  delivery:
    interface: http
    endpoint: "/handle"
    timeout_ms: 30000
```

### Example 2: Seer AI Agent Runtime

```yaml
# Hub Application on Seer
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: investigation-agent
spec:
  runtime:
    type: seer
    
  agent:
    model: "gpt-4-turbo"
    system_prompt_ref: investigation-prompt
    
  tools:
    - transaction-lookup
    - customer-history
    - knowledge-search
    
  memory:
    type: conversation
    retention: request_scoped
```

---

## Implementation Notes

### For Developers

- Choose runtime based on automation paradigm
- Use Runtime CI for consistent builds
- Configure appropriate resource limits
- Test locally before deploying

### For Operators

- Monitor runtime capacity and health
- Configure scaling policies per workbench
- Review resource utilization
- Manage runtime upgrades

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Hub Application](./hub-application.md) | Applications run on Runtimes |
| [Signal Exchange](./signal-exchange.md) | Routes requests to Runtime |
| [Artifact Registry](./artifact-registry.md) | Source of application artifacts |

---

## References

- [Automation Runtimes Subsystem](../04-subsystems/automation-runtimes/README.md)
- [Atlantis Runtime](../04-subsystems/automation-runtimes/atlantis-runtime.md)
- [Seer Case Automation](../04-subsystems/automation-runtimes/seer-case-automation.md)

