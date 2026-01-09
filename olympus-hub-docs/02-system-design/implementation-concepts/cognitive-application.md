# Cognitive Application

> **Category:** Application Architecture  
> **Status:** ✅ Complete

---

## Overview

A **Cognitive Application** is a specialized Hub Application that participates in the platform's memory and context infrastructure. While any Hub Application can process requests, a Cognitive Application is distinguished by its ability to:

1. **Emit Tasks** — Delegate work to human and AI agents via Task Management
2. **Compile Context** — Build and maintain request-level context for agents
3. **Emit Memory Records** — Produce structured episodic memory records adhering to CAF schemas
4. **Register Schemas** — Declare the memory record schemas it produces

Not every Hub Application is a Cognitive Application. Simple request-response automations (e.g., validation services, prediction tools) typically don't need these capabilities. However, any application that orchestrates agent work is **advised** to be modeled as a Cognitive Application.

---

## Relationship to Hub Application

Cognitive Application is not a separate kind—it is a **capability profile** of a Hub Application.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           HUB APPLICATIONS                                   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │                    COGNITIVE APPLICATIONS                                ││
│  │                                                                          ││
│  │  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐       ││
│  │  │  Seer Case       │  │  Rhea Workflow   │  │  Custom Container││       ││
│  │  │  Orchestrator    │  │  with Tasks      │  │  Application     ││       ││
│  │  └──────────────────┘  └──────────────────┘  └──────────────────┘       ││
│  │                                                                          ││
│  │  Characteristics:                                                        ││
│  │  • Emits tasks for agent work                                            ││
│  │  • Compiles context per request update                                   ││
│  │  • Produces episodic memory records                                      ││
│  │  • Registers memory record schemas                                       ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │              NON-COGNITIVE APPLICATIONS (Simpler)                        ││
│  │                                                                          ││
│  │  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐       ││
│  │  │  Decision Tool   │  │  Prediction      │  │  HTTP Tool       ││       ││
│  │  │  (Atlantis)      │  │  Service         │  │  Calling App     ││       ││
│  │  └──────────────────┘  └──────────────────┘  └──────────────────┘       ││
│  │                                                                          ││
│  │  Characteristics:                                                        ││
│  │  • Request-response only                                                 ││
│  │  • No task delegation                                                    ││
│  │  • No context compilation                                                ││
│  │  • May emit memory records (optional, but if regular, consider cognitive)││
│  └─────────────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Definition

A **Cognitive Application** is a Hub Application that:

| Capability | Description |
|------------|-------------|
| **Task Emission** | Creates tasks for human and AI agents to complete |
| **Context Compilation** | Builds and maintains request-level context with each relevant update |
| **Memory Record Emission** | Produces structured episodic memory records (decisions, evidence, handoffs, etc.) |
| **Schema Registration** | Declares the memory record schemas it will emit in its specification |

### Runtime Independence

Cognitive Applications are **not limited to a specific Automation Runtime**. They can run on:

| Runtime | Example Cognitive Application |
|---------|------------------------------|
| **Seer** | AI Case Orchestration Agent |
| **Rhea** | BPMN Workflow with human tasks |
| **ChronoShift** | Durable Workflow with agent checkpoints |
| **Atlantis** | Custom container application with task delegation |

The key differentiator is **behavior** (task emission, context compilation, memory records), not runtime technology.

---

## Context Compilation

### Responsibility Model

Cognitive Applications and agents have **mutually independent** but **complementary** context compilation responsibilities:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CONTEXT COMPILATION MODEL                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  COGNITIVE APPLICATION                        AGENT                          │
│  ────────────────────                        ─────                           │
│                                                                              │
│  Request-Level Context                       Task-Specific Context           │
│  • Compiled with each relevant update        • Compiled by agent as needed   │
│  • Available to all agents on request        • Specialized for agent's role  │
│  • Stored as Context records in request      • May use application context   │
│  • Tagged to request (default) or task       • Cannot be enforced            │
│                                                                              │
│       ┌─────────────────────────┐                                            │
│       │   Request Context       │                                            │
│       │   (compiled by app)     │────────────▶ Agent retrieves               │
│       │                         │              and may extend                 │
│       │   • Constraints         │                                            │
│       │   • Verified facts      │                                            │
│       │   • Applicable SOPs     │                                            │
│       │   • Prior decisions     │                                            │
│       └─────────────────────────┘                                            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Context Scope

| Scope | Description |
|-------|-------------|
| **Request-level** | Default. Context compiled by application is available to all agents working on any task in the request. |
| **Task-tagged** | Optional. Application can add context records tagged to a specific task. These are still visible to all agents but indicate task-specific relevance. |

### Context Delivery

Agents retrieve context from the request. When context is updated:

1. Application adds context records to REQUEST_UPDATE
2. Signal Exchange records updates in request history
3. Interested agents are notified of the update
4. Agents query request to retrieve updated context

---

## Memory Record Emission

### Expectation

Both Cognitive Applications and agents (human and AI) are expected to emit episodic memory records during request processing.

| Actor | Memory Record Emission |
|-------|------------------------|
| **Cognitive Application** | Emits decision records, context snapshots, milestone records |
| **AI Agent (via Seer)** | Emits reasoning traces, evidence bundles, handoff context |
| **Human Agent** | Aided by Task Solver components to build and emit appropriate records |

### Task Solver Support

Human agents use **Task Solver** components in the Agent Desk UI. These components:

- Present appropriate forms based on task type
- Guide agents to capture required information
- Build structured memory records from agent input
- Emit records on behalf of the agent

See [Agent Task Operations](../../04-subsystems/task-management/agent-task-operations.md) for Task Solver details.

### Write Path

All memory records flow through Signal Exchange:

```
Application/Agent
        │
        │  REQUEST_UPDATE with memory_records[]
        ▼
Signal Exchange
        │
        ├── Validates records against registered schemas
        │   • Valid → routed to memory stores
        │   • Invalid → retained in request history, marked invalid
        │
        ├── Enriches with hub_metadata
        │
        └── Routes to Atropos topic per memory class
                │
                ▼
        Memory Store Writer Service
                │
                ▼
        Enterprise Memory (OpenSearch via Europa)
```

---

## Schema Registration

### Registration Scopes

Memory record schemas can be registered at multiple scopes:

| Scope | Registrar | Use Case |
|-------|-----------|----------|
| **Application** | Developer | Schemas specific to one application |
| **Workbench** | Developer / Supervisor | Schemas shared across applications in a workbench |
| **Platform** | Hub Team | Standard CAF schemas (Decision, Evidence, Handoff, etc.) |

### Schema Resolution

When validating a memory record:

1. Signal Exchange looks up the schema by `content_type` and `version`
2. Resolution order:
   - Application-registered schema
   - Workbench-registered schema
   - Platform-provided schema
3. **Latest version wins** for a given type
4. If same version exists at both Application and Workbench scope, **Workbench definition survives** (operator alerts on conflict)

### Application Specification

Cognitive Applications declare their memory record schemas in their specification:

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: fraud-case-orchestrator
  namespace: acme-bank
spec:
  display_name: "Fraud Case Orchestrator"
  version: "2.1.0"
  
  runtime:
    type: seer
  
  # Cognitive Application capabilities
  cognitive:
    enabled: true
    
    # Context compilation
    context:
      compile_on_update: true
      context_types:
        - constraints
        - verified_facts
        - applicable_sops
        - prior_decisions
    
    # Memory record schemas this application emits
    memory_schemas:
      - schema_id: "com.acme.fraud.FraudDecisionRecord"
        version: "1.0.0"
        uri: "./schemas/fraud-decision-record.json"
      - schema_id: "com.acme.fraud.InvestigationEvidence"
        version: "1.0.0"
        uri: "./schemas/investigation-evidence.json"
    
    # Schemas this application uses (from workbench or platform)
    uses_schemas:
      - "hub.olympus.io/caf/DecisionRecord/v1"
      - "hub.olympus.io/caf/HandoffContext/v1"
  
  scenarios:
    - fraud-investigation
    - fraud-resolution
```

### Workbench-Level Registration

Schemas shared across applications are registered at workbench level:

```yaml
apiVersion: hub.olympus.io/v1
kind: MemorySchemaSpec
metadata:
  name: fraud-workbench-schemas
  namespace: acme-bank
spec:
  workbench_id: fraud-ops
  
  schemas:
    - schema_id: "com.acme.fraud.CustomerRiskProfile"
      version: "1.0.0"
      content:
        type: object
        properties:
          customer_id: { type: string }
          risk_score: { type: number }
          risk_factors: { type: array, items: { type: string } }
          assessed_at: { type: string, format: date-time }
        required: [customer_id, risk_score, assessed_at]
```

---

## Signal Exchange Validation

Signal Exchange validates all memory records attached to REQUEST_UPDATE messages:

### Validation Behavior

| Condition | Action |
|-----------|--------|
| **Schema found, record valid** | Route to memory store via Atropos |
| **Schema found, record invalid** | Mark invalid, retain in request history, do NOT route to memory store |
| **Schema not found** | Mark as unvalidated, retain in request history, alert operator |

### Invalid Record Handling

Invalid records are **not discarded**. They are:

1. Recorded in request history with `validation_status: "INVALID"`
2. Include validation errors for debugging
3. Available for audit and troubleshooting
4. NOT written to enterprise memory stores

This ensures:
- **No data loss** — invalid records are preserved
- **Clean memory stores** — only valid records are indexed
- **Debuggability** — developers can see what went wrong

---

## Comparison: Cognitive vs Non-Cognitive

| Aspect | Cognitive Application | Non-Cognitive Application |
|--------|----------------------|--------------------------|
| **Tasks** | Emits tasks for agents | No task emission |
| **Context** | Compiles and maintains request context | No context compilation |
| **Memory Records** | Expected to emit records | Optional (but if regular, should be cognitive) |
| **Schema Registration** | Required | Not applicable |
| **Complexity** | Higher — manages agent coordination | Lower — request-response |
| **Use Cases** | Case management, investigations, approvals | Validation, prediction, integration |

---

## Implementation Guidance

### When to Use Cognitive Application

Use a Cognitive Application when:

- Work involves **human or AI agents** who need context
- Decisions need to be **auditable** with evidence
- Request processing spans **multiple interactions**
- **Handoffs** occur between agents or shifts
- **Institutional learning** from outcomes is valuable

### When to Use Non-Cognitive Application

Use a simple Hub Application when:

- Processing is **fully automated** with no agent involvement
- Request is **single-step** (validate, predict, transform)
- No **auditability** requirements beyond logs
- No **context** needs to be shared with other components

### Migration Path

A non-cognitive application can become cognitive by:

1. Adding `cognitive.enabled: true` to specification
2. Registering memory record schemas
3. Implementing context compilation logic
4. Emitting appropriate memory records

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Hub Application](./hub-application.md) | Parent concept — Cognitive Application is a capability profile |
| [Task Management](../../04-subsystems/task-management/README.md) | Cognitive Applications emit tasks |
| [Memory Services](../../04-subsystems/memory-services/README.md) | Stores emitted memory records |
| [CAF Record Schema Registry](../../04-subsystems/cognitive-audit-fabric/record-content-schema-registry.md) | Schema registration and validation |
| [Signal Exchange](../../04-subsystems/signal-exchange/README.md) | Routes updates and validates records |
| [Agent Task Operations](../../04-subsystems/task-management/agent-task-operations.md) | Task Solver for human agents |

---

## References

- [Hub Application](./hub-application.md)
- [Memory Record Routing](../../04-subsystems/signal-exchange/memory-record-routing.md)
- [Episodic Memory Store](../../04-subsystems/cognitive-audit-fabric/episodic-memory-store/README.md)
- [Context Snapshots](../../04-subsystems/cognitive-audit-fabric/episodic-memory-store/context-snapshots.md)

