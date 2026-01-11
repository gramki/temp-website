# Hub Application

> **Category:** Application Architecture

---

## Overview

A **Hub Application** is the concrete automation artifact that executes Scenario logic. It is the software implementation of an [Automation](../../01-concepts/ontology-4-automation-layer.md#automation) — receiving Request Updates from Signal Exchange, processing business logic, delegating Tasks to Agents, and reporting outcomes. Hub Applications run on Automation Runtimes (Atlantis, Rhea, Seer, Perseus) and can be implemented using various technologies including rule engines, workflows, and AI agents.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Automation** as the "blueprint or recipe" for how an Operation should run, and **Automation Runtime** as the execution platform. Hub Application is the concrete manifestation of an Automation deployed on a Runtime.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Automation | Hub Application code/config | Hub App is the concrete automation artifact |
| Automation Runtime | Atlantis, Rhea, Seer, Perseus | Runtime hosts the Hub Application |
| Operation | Request instance | Hub App orchestrates the running operation |

### Gap This Fills

The ontology describes Automation abstractly. Hub Application specifies:
1. **Packaging**: How automations are containerized and versioned
2. **Deployment**: How automations are deployed to runtimes
3. **Communication**: How automations receive and send signals
4. **Composition**: How automations can be composed (as agents, tools, etc.)

---

## Definition

**Hub Application** is a deployable automation artifact that:
- Receives Request Updates from Signal Exchange
- Implements business logic for one or more Scenarios
- Delegates Tasks to human and AI Agents via Task Management
- Updates Request state with decisions, memos, and outcomes
- Can be exposed as an Agent, Tool, or standalone service

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-scoped; belongs to exactly one Workbench |
| **Lifecycle** | Built via Runtime CI; deployed per Workbench; promoted across stages |
| **Ownership** | Developer creates; Supervisor manages runtime configuration |
| **Multiplicity** | One Workbench can have many Hub Applications |

---

## Rationale

### Why This Design?

Hub Applications provide a clear separation between:
1. **What should be done** (Scenario specification) vs **How it's done** (Application implementation)
2. **Orchestration** (Signal Exchange) vs **Execution** (Hub Application)
3. **Infrastructure** (Runtime) vs **Logic** (Application code)

This enables:
- Multiple technology choices (AI, rules, workflows, code)
- Independent versioning and promotion
- Clear responsibility boundaries

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Inline Scenario logic** | Limited flexibility; no external tools |
| **Platform-only execution** | Can't support custom logic |
| **Serverless functions only** | Insufficient for stateful workflows |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0007](../../decision-logs/0007-composite-pattern-technology-agnostic.md) | Hub Applications can be any technology (not just AI) |
| [ADR-0023](../../decision-logs/0023-http-tool-calling-application.md) | HTTP Tool Calling Application as built-in type |

---

## Structure

### Hub Application Specification

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: dispute-handler
spec:
  display_name: "Dispute Handler"
  version: "1.2.3"
  
  # Runtime selection
  runtime:
    type: atlantis  # atlantis | rhea | seer | perseus
    
  # Container reference (from registry)
  container:
    image: "registry.hub.olympus.io/acme-bank/sub-dev/dispute-ops-dev/dispute-handler"
    tag: "1.2.3"
  
  # Scenarios this application handles
  scenarios:
    - standard-dispute
    - fraud-dispute
  
  # Communication preferences
  delivery:
    interface: http  # http | atropos | oms
    endpoint: "/handle"
    
  # Resource requirements
  resources:
    cpu: "500m"
    memory: "512Mi"
    
  # Environment configuration
  environment:
    variables:
      LOG_LEVEL: "INFO"
    secrets:
      - api-credentials
```

### Application Types

| Type | Runtime | Best For |
|------|---------|----------|
| **Container Application** | Atlantis | Custom code, microservices |
| **Workflow Application** | Rhea | BPMN workflows |
| **AI Agent Application** | Seer | LLM-based agents |
| **Batch Application** | Perseus | File processing, ETL |
| **HTTP Tool Calling** | Built-in | Simple HTTP integrations |

### Cognitive Application (Capability Profile)

Any Hub Application that emits **tasks**, compiles **context** for agents, and produces **memory records** is termed a **Cognitive Application**. This is not a separate type but a capability profile indicating the application participates in Hub's memory and context infrastructure.

| Capability | Description |
|------------|-------------|
| **Task Emission** | Creates tasks for human and AI agents |
| **Context Compilation** | Builds request-level context for agents |
| **Memory Record Emission** | Produces structured episodic memory records |
| **Schema Registration** | Declares memory record schemas in specification |

**Recommendation:** Any application that emits tasks is advised to be modeled as a Cognitive Application.

→ **Details:** [Cognitive Application](./cognitive-application.md)

---

## Behavior

### How It Works

**Request Handling:**
```
1. Signal Exchange receives signal
2. Trigger matches → Request created
3. SX routes Request Update to Hub Application
4. Application receives update via configured interface (HTTP/Atropos/OMS)
5. Application processes:
   ├── Query Knowledge Bank for context
   ├── Call Tools for external operations
   ├── Delegate Tasks to Agents
   └── Update Request state
6. Application sends Request Update back to SX
7. SX broadcasts to observers
```

**Task Delegation:**
```
1. Application determines work needs agent involvement
2. Application creates Task with context:
   ├── Task type (from Scenario definition)
   ├── Task payload (context for agent)
   ├── Target queue (or default)
3. Task Management allocates to Agent
4. Agent completes task → Update flows back to Application
5. Application continues orchestration
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Signal Exchange | ↔ bidirectional | Receives requests, sends updates |
| Task Management | → creates | Delegates tasks to agents |
| Tool Registry | → queries | Discovers available tools |
| Machine Registry | → queries | Accesses external systems |
| Knowledge Bank | → queries | Retrieves context and knowledge |
| Memory Services | ↔ bidirectional | Reads/writes agent and enterprise memory |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Single workbench** | Hub Application belongs to exactly one Workbench |
| **Runtime compatibility** | Application must be compatible with selected runtime |
| **Scenario binding** | Application must handle at least one Scenario |
| **Version immutability** | Deployed version is immutable; promote new versions |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Technology flexibility** | Any language/framework that runs in containers |
| ✅ **Clear boundaries** | Application owns logic; platform owns orchestration |
| ✅ **Composable** | Can be exposed as Agent, Tool, or service |
| ✅ **Independently deployable** | Version and promote separately from Scenario |
| ✅ **Testable** | Hub Test Runner for integration testing |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Container overhead** | Lightweight runtimes; efficient scaling |
| ⚠️ **Learning curve** | Built-in types (HTTP Tool Calling) for simple cases |
| ⚠️ **Debugging complexity** | Olympus Watch integration; structured logging |

---

## Examples

### Example 1: Simple Dispute Handler

```python
# Hub Application using Atlantis runtime
from hub_sdk import HubApplication, RequestUpdate

class DisputeHandler(HubApplication):
    async def handle_request(self, update: RequestUpdate):
        # Extract context
        dispute = update.payload.data
        
        # Query knowledge for relevant SOP
        sop = await self.knowledge_bank.query(
            f"dispute handling SOP for {dispute['type']}"
        )
        
        # Delegate investigation task to human agent
        task = await self.create_task(
            task_type="investigate_dispute",
            payload={
                "dispute": dispute,
                "sop_reference": sop.id,
                "priority": "high" if dispute["amount"] > 1000 else "normal"
            },
            target_queue="tier-1-disputes"
        )
        
        # Update request with task created
        return RequestUpdate(
            status="IN_PROGRESS",
            memo=f"Investigation task {task.id} created"
        )
```

### Example 2: HTTP Tool Calling Application

```yaml
# Simple HTTP integration using built-in type
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: payment-validator
spec:
  type: http_tool_calling_application
  
  tool_config:
    tool_endpoint: "https://api.payment.acme.com/validate"
    method: "POST"
    auth:
      type: bearer
      token: "${env.PAYMENT_API_TOKEN}"
    timeout_ms: 30000
    
  transformations:
    input_transform: |
      function(input) {
        return { amount: input.amount, account: input.account_id };
      }
    output_transform: |
      function(response, request) {
        return {
          request_status: { status: "COMPLETED" },
          payload: { valid: response.body.is_valid }
        };
      }
```

---

## Implementation Notes

### For Developers

- Start with built-in types (HTTP Tool Calling) for simple integrations
- Use Hub SDK for consistent interaction patterns
- Always handle idempotency — you may receive the same update multiple times
- Structure logs for Olympus Watch compatibility

### For Operators

- Monitor application health via APM integration
- Configure scaling based on request volume
- Manage environment variables and secrets per workbench
- Review promotion requests for application changes

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Hub Application Deployment](./hub-application-deployment.md) | Running instance of a Hub Application (generated from ScenarioDeploymentSpec) |
| [Cognitive Application](./cognitive-application.md) | Capability profile for task-emitting, context-compiling applications |
| [Automation Runtime](./automation-runtime.md) | Hosts Hub Applications |
| [Signal Exchange](./signal-exchange.md) | Routes requests to Applications |
| [Request Lifecycle](./request-lifecycle.md) | Application orchestrates Request state |
| [Scenario Specification Types](./scenario-specification-types.md) | Application implements Automation Spec |
| [Composite Patterns](../../09-composite-systems-and-patterns/README.md) | Application can be Agent, Tool, etc. |

---

## References

- [Hub Applications (Ontology)](../../01-concepts/hub-applications.md)
- [Automation Runtimes Subsystem](../../04-subsystems/automation-runtimes/README.md)
- [HTTP Tool Calling Application](../../04-subsystems/hub-native-utilities/http-tool-calling-application.md)
- [ADR-0007: Technology Agnostic](../../decision-logs/0007-composite-pattern-technology-agnostic.md)

