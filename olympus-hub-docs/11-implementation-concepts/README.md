# Implementation Concepts

> **Purpose:** Document Hub-specific implementation concepts that extend the theoretical ontology into concrete platform capabilities.

---

## About This Section

The [Ontology](../01-concepts/ontology-reference.md) describes **what** Human-AI team operations should accomplish conceptually. This section describes **how** Olympus Hub implements those concepts with specific platform constructs, patterns, and mechanisms.

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
| [Tenant](./tenant.md) | Multi-tenant isolation unit | 🔴 TODO |
| [Subscription](./subscription.md) | Resource and billing boundary within a tenant | ✅ Complete |
| [Dev-Lifecycle-Stage](./dev-lifecycle-stage.md) | Workbench maturity tags (DEV, STAGING, PROD) | 🔴 TODO |
| [Promotion](./promotion.md) | Controlled artifact movement between workbenches | 🔴 TODO |
| [Blueprint](./blueprint.md) | Reusable workbench templates | 🔴 TODO |

### Signal Architecture

| Concept | Description | Status |
|---------|-------------|--------|
| [Signal Exchange](./signal-exchange.md) | Hub's central routing and orchestration engine | ✅ Complete |
| [I/O Gateway](./io-gateway.md) | Signal ingress/egress points (Heracles, Atropos, etc.) | 🔴 TODO |
| [Normalized Signal Format](./normalized-signal-format.md) | Standard DTO for signal transport | 🔴 TODO |
| [Message Envelope](./message-envelope.md) | Standard wrapper for application communication | 🔴 TODO |
| [Reminder Capability](./reminder-capability.md) | Time-based stimuli for parked workflows | 🔴 TODO |
| [Observer Pattern](./observer-pattern.md) | Module integration with Signal Exchange | 🔴 TODO |

### Application Architecture

| Concept | Description | Status |
|---------|-------------|--------|
| [Hub Application](./hub-application.md) | Concrete automation artifact running on a runtime | ✅ Complete |
| [Automation Runtime](./automation-runtime.md) | Execution host for Hub Applications | 🔴 TODO |
| [Hub Native Utilities](./hub-native-utilities.md) | Built-in platform applications and tools | 🔴 TODO |
| [Direct Tool Dispatcher](./direct-tool-dispatcher.md) | Bypass SX for synchronous tool invocation | 🔴 TODO |

### Request and Task

| Concept | Description | Status |
|---------|-------------|--------|
| [Request Lifecycle](./request-lifecycle.md) | Request states, updates, and transitions | 🔴 TODO |
| [Request Update](./request-update.md) | Append-only updates to request context | 🔴 TODO |
| [Task Allocation](./task-allocation.md) | Assignment algorithms and workload balancing | 🔴 TODO |
| [Escalation Matrix](./escalation-matrix.md) | Multi-level cumulative agent assignment | 🔴 TODO |

### User Experience Architecture

| Concept | Description | Status |
|---------|-------------|--------|
| [Persona](./persona.md) | Hub user types with distinct responsibilities | 🔴 TODO |
| [Channel](./channel.md) | Interaction interfaces (Web, MCP, REST, MS Teams) | 🔴 TODO |
| [Headless Access Service](./headless-access-service.md) | Backend services with channel adapters | 🔴 TODO |
| [Notification Services](./notification-services.md) | User notification subsystem | 🔴 TODO |

### Data Architecture

| Concept | Description | Status |
|---------|-------------|--------|
| [Application Data Store](./application-data-store.md) | Workbench-scoped storage (Ganymede, Callisto, Europa) | 🔴 TODO |
| [Memory Services](./memory-services.md) | Enterprise, Agent, and User memory | 🔴 TODO |
| [Knowledge Bank](./knowledge-bank.md) | RAG and document retrieval | 🔴 TODO |
| [Cognitive Audit Fabric](./cognitive-audit-fabric.md) | Memory control plane and audit | 🔴 TODO |
| [Hub Environment](./hub-environment.md) | Business/operations domain runtime configuration | 🔴 TODO |

### Configuration Model

| Concept | Description | Status |
|---------|-------------|--------|
| [CRD (Custom Resource Definition)](./crd.md) | Declarative configuration model | 🔴 TODO |
| [Operator](./operator.md) | GitOps-based resource reconciliation | 🔴 TODO |
| [Scenario Specification Types](./scenario-specification-types.md) | Normative, Automation, and Deployment specs | 🔴 TODO |

### Composite Patterns

| Concept | Description | Status |
|---------|-------------|--------|
| [Scenario as Agent](./scenario-as-agent.md) | Scenario published as task-completing agent | 🔴 TODO |
| [Scenario as Tool](./scenario-as-tool.md) | Scenario exposed as callable tool | 🔴 TODO |
| [Workbench as Machine](./workbench-as-machine.md) | Workbench exposed as Machine to other workbenches | 🔴 TODO |
| [Hub Application as Standalone Tool](./hub-application-as-standalone-tool.md) | Direct tool invocation bypassing SX | 🔴 TODO |

### DevOps and Lifecycle

| Concept | Description | Status |
|---------|-------------|--------|
| [Artifact Registry](./artifact-registry.md) | Container and CRD storage | 🔴 TODO |
| [Promotion Destination](./promotion-destination.md) | Target workbench/subscription for artifact movement | 🔴 TODO |
| [CI Subsystem](./ci-subsystem.md) | Build and test infrastructure | 🔴 TODO |
| [Hub Test Runner](./hub-test-runner.md) | Integration testing framework | 🔴 TODO |
| [APM (Application Performance Monitoring)](./apm.md) | Observability for Hub Applications | 🔴 TODO |

### Integration

| Concept | Description | Status |
|---------|-------------|--------|
| [MS Teams Integration](./ms-teams-integration.md) | Persona bots and chat group collaboration | 🔴 TODO |
| [Hercules Launcher](./hercules-launcher.md) | Deep linking service for cross-channel navigation | 🔴 TODO |

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

- [Ontology Reference](../01-concepts/ontology-reference.md) — Theoretical foundation
- [Decision Logs](../decision-logs/README.md) — Rationale for implementation choices
- [Subsystems](../04-subsystems/) — Technical details
- [Guides](../10-guides/) — Practical how-tos

