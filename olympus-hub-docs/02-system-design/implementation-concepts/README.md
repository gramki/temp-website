# Implementation Concepts

> **Purpose:** Document Hub-specific implementation concepts that extend the theoretical ontology into concrete platform capabilities.

---

## About This Section

The [Ontology](../../01-concepts/ontology-reference.md) describes **what** Human-AI team operations should accomplish conceptually. This section describes **how** Olympus Hub implements those concepts with specific platform constructs, patterns, and mechanisms.

These implementation concepts are:
- **Hub-specific** — not generic workflow or operations theory
- **Concrete** — have specific behaviors, configurations, and constraints
- **Interconnected** — form a coherent implementation story
- **Decision-backed** — many have corresponding ADRs documenting the rationale

---

## Concept Index

### Platform Foundation

| Concept | Description | Status |
|---------|-------------|--------|
| [Tenant](./tenant.md) | Multi-tenant isolation unit | ✅ Complete |
| [Subscription](./subscription.md) | Resource and billing boundary within a tenant | ✅ Complete |
| [Dev-Lifecycle-Stage](./dev-lifecycle-stage.md) | Workbench maturity tags (DEV, STAGING, PROD) | ✅ Complete |
| [Promotion](./promotion.md) | Controlled artifact movement between workbenches | ✅ Complete |
| [Blueprint](./blueprint.md) | Reusable workbench templates | ✅ Complete |

### Signal Architecture

| Concept | Description | Status |
|---------|-------------|--------|
| [Signal Exchange](./signal-exchange.md) | Hub's central routing and orchestration engine | ✅ Complete |
| [I/O Gateway](./io-gateway.md) | Signal ingress/egress points (Heracles, Atropos, etc.) | ✅ Complete |
| [Normalized Signal Format](./normalized-signal-format.md) | Standard DTO for signal transport | ✅ Complete |
| [Message Envelope](./message-envelope.md) | Standard wrapper for application communication | ✅ Complete |
| [Reminder Capability](./reminder-capability.md) | Time-based stimuli for parked workflows | ✅ Complete |
| [Observer Pattern](./observer-pattern.md) | Module integration with Signal Exchange | ✅ Complete |

### Application Architecture

| Concept | Description | Status |
|---------|-------------|--------|
| [Hub Application](./hub-application.md) | Concrete automation artifact running on a runtime | ✅ Complete |
| [Cognitive Application](./cognitive-application.md) | Task-emitting, context-compiling application profile | ✅ Complete |
| [Automation Runtime](./automation-runtime.md) | Execution host for Hub Applications | ✅ Complete |
| [Hub Native Utilities](./hub-native-utilities.md) | Built-in platform applications and tools | ✅ Complete |
| [Direct Tool Dispatcher](./direct-tool-dispatcher.md) | Bypass SX for synchronous tool invocation | ✅ Complete |

### Request and Task

| Concept | Description | Status |
|---------|-------------|--------|
| [Request Lifecycle](./request-lifecycle.md) | Request states, updates, and transitions | ✅ Complete |
| [Request Update](./request-update.md) | Append-only updates to request context | ✅ Complete |
| [Task Allocation](./task-allocation.md) | Assignment algorithms and workload balancing | ✅ Complete |
| [Escalation Matrix](./escalation-matrix.md) | Multi-level cumulative agent assignment | ✅ Complete |
| [Agent Directability](./agent-directability.md) | Human intervention in AI agent operations | 🟡 Draft |

### User Experience Architecture

| Concept | Description | Status |
|---------|-------------|--------|
| [Persona](./persona.md) | Hub user types with distinct responsibilities | ✅ Complete |
| [Channel](./channel.md) | Interaction interfaces (Web, MCP, REST, MS Teams) | ✅ Complete |
| [Headless Access Service](./headless-access-service.md) | Backend services with channel adapters | ✅ Complete |
| [Notification Services](./notification-services.md) | User notification subsystem | ✅ Complete |

### Data Architecture

| Concept | Description | Status |
|---------|-------------|--------|
| [Application Data Store](./application-data-store.md) | Workbench-scoped storage (Ganymede, Callisto, Europa) | ✅ Complete |
| [Memory Services](./memory-services.md) | Enterprise, Agent, and User memory | ✅ Complete |
| [Knowledge Bank](./knowledge-bank.md) | RAG and document retrieval | ✅ Complete |
| [Cognitive Audit Fabric](./cognitive-audit-fabric.md) | Memory control plane and audit | ✅ Complete |
| [Hub Environment](./hub-environment.md) | Business/operations domain runtime configuration | ✅ Complete |

### Configuration Model

| Concept | Description | Status |
|---------|-------------|--------|
| [CRD (Custom Resource Definition)](./crd.md) | Declarative configuration model | ✅ Complete |
| [Operator](./operator.md) | GitOps-based resource reconciliation | ✅ Complete |
| [Scenario Specification Types](./scenario-specification-types.md) | Normative, Automation, and Deployment specs | ✅ Complete |

### Composite Patterns

| Concept | Description | Status |
|---------|-------------|--------|
| [Scenario as Agent](./scenario-as-agent.md) | Scenario published as task-completing agent | ✅ Complete |
| [Scenario as Tool](./scenario-as-tool.md) | Scenario exposed as callable tool | ✅ Complete |
| [Workbench as Machine](./workbench-as-machine.md) | Workbench exposed as Machine to other workbenches | ✅ Complete |
| [Hub Application as Standalone Tool](./hub-application-as-standalone-tool.md) | Direct tool invocation bypassing SX | ✅ Complete |

### DevOps and Lifecycle

| Concept | Description | Status |
|---------|-------------|--------|
| [Artifact Registry](./artifact-registry.md) | Container and CRD storage | ✅ Complete |
| [Promotion Destination](./promotion-destination.md) | Target workbench/subscription for artifact movement | ✅ Complete |
| [CI Subsystem](./ci-subsystem.md) | Build and test infrastructure | ✅ Complete |
| [Hub Test Runner](./hub-test-runner.md) | Integration testing framework | ✅ Complete |
| [APM (Application Performance Monitoring)](./apm.md) | Observability for Hub Applications | ✅ Complete |

### Integration

| Concept | Description | Status |
|---------|-------------|--------|
| [MS Teams Integration](./ms-teams-integration.md) | Persona bots and chat group collaboration | ✅ Complete |
| [Hercules Launcher](./hercules-launcher.md) | Deep linking service for cross-channel navigation | ✅ Complete |

---

## Relationship to Ontology

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ONTOLOGY TO IMPLEMENTATION                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ONTOLOGY (What)                      IMPLEMENTATION (How)                  │
│   ──────────────                       ────────────────────                  │
│                                                                              │
│   Domain ─────────────────────────────▶ Workbench + Blueprint                │
│                                                                              │
│   Signal ─────────────────────────────▶ I/O Gateway + Normalized Format      │
│                                                                              │
│   Trigger ────────────────────────────▶ Signal Exchange + TriggerSpec        │
│                                                                              │
│   Scenario ───────────────────────────▶ Scenario Specifications (3 types)   │
│                                                                              │
│   Automation ─────────────────────────▶ Hub Application + Runtime           │
│                                                                              │
│   Operation ──────────────────────────▶ Request + Request Lifecycle          │
│                                                                              │
│   Task ───────────────────────────────▶ Task + Allocation + Escalation       │
│                                                                              │
│   OPD (Directability) ───────────────▶ Agent Directability + CAF Records    │
│                                                                              │
│   Agent ──────────────────────────────▶ Persona + Channel + Notification     │
│                                                                              │
│   Tool ───────────────────────────────▶ Tool Instance + Direct Dispatcher    │
│                                                                              │
│   Machine ────────────────────────────▶ Machine Instance + WB as Machine     │
│                                                                              │
│   Knowledge Base ─────────────────────▶ Knowledge Bank + Memory Services     │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Reading Order

### For Architects
1. Start with Platform Foundation concepts
2. Review Signal Architecture for data flow
3. Understand Configuration Model for declarative design

### For Developers
1. Start with Hub Application and Automation Runtime
2. Review Request Lifecycle and Task Allocation
3. Explore Composite Patterns for advanced use

### For Operators
1. Start with DevOps and Lifecycle concepts
2. Review Configuration Model for GitOps
3. Understand Data Architecture for storage decisions

---

## Related Documentation

- [Ontology Reference](../../01-concepts/ontology-reference.md) — Theoretical foundation
- [Decision Logs](../../decision-logs/README.md) — Rationale for implementation choices
- [Subsystems](../../04-subsystems/) — Technical details
- [Guides](../../10-guides/) — Practical how-tos

