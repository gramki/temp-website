# System Design

> **Purpose:** Architecture documentation for Olympus Hub — how the system is structured, how components interact, and how concepts are implemented.

---

## Document Index

### Architecture Overview

| Document | Description | Audience |
|----------|-------------|----------|
| [Hub Architecture](./hub-architecture.md) | Executive overview, core philosophy, and system principles | Everyone |
| [Hub Design Philosophy](./hub-design-philosophy.md) | Theoretical foundations and design principles | Architects, Designers |
| [Architecture Layers](./architecture-layers.md) | Four-layer ontology mapping to Hub components | Architects |
| [Signal Flow](./signal-flow.md) | End-to-end signal processing narrative | Developers, Architects |
| [Workbench Anatomy](./workbench-anatomy.md) | Internal structure and components of a Workbench | Developers |
| [Agent Model](./agent-model.md) | Human and AI agent interaction with Hub | Developers, Product |
| [Subsystem Map](./subsystem-map.md) | Subsystem boundaries, dependencies, and responsibilities | Architects, Operators |

### Architecture Views

Curated perspectives of the same system for different stakeholders:

| View | Audience | Question Answered |
|------|----------|-------------------|
| [Data Flow View](./views/data-flow-view.md) | Data Engineers, Integration Architects | How does data move through the system? |
| [Runtime View](./views/runtime-view.md) | Developers, Operators | What runs where? |
| [Deployment View](./views/deployment-view.md) | Platform Engineers, DevOps | How is the system deployed and promoted? |
| [Security View](./views/security-view.md) | Security Architects, Auditors | How is the system secured? |
| [Persona Journey View](./views/persona-journey-view.md) | Product Managers, UX Designers | How do users experience the system? |
| [Integration View](./views/integration-view.md) | Enterprise Architects | How does Hub connect to external systems? |

### Implementation Concepts

Detailed documentation of individual platform constructs:

| Category | Concepts | Focus |
|----------|----------|-------|
| [Platform Foundation](./implementation-concepts/README.md#platform-foundation) | Tenant, Subscription, Blueprint, Dev-Lifecycle-Stage, Promotion | Multi-tenancy, resource isolation |
| [Signal Architecture](./implementation-concepts/README.md#signal-architecture) | Signal Exchange, I/O Gateway, Normalized Signal Format | Signal routing and transformation |
| [Application Architecture](./implementation-concepts/README.md#application-architecture) | Hub Application, Automation Runtime, Direct Tool Dispatcher | Automation execution |
| [Request and Task](./implementation-concepts/README.md#request-and-task) | Request Lifecycle, Task Allocation, Escalation Matrix | Work management |
| [User Experience](./implementation-concepts/README.md#user-experience-architecture) | Persona, Channel, Headless Access Service | User interaction |
| [Data Architecture](./implementation-concepts/README.md#data-architecture) | Application Data Store, Memory Services, Knowledge Bank | Storage and retrieval |
| [Configuration Model](./implementation-concepts/README.md#configuration-model) | CRD, Operator, Scenario Specification Types | Declarative configuration |
| [Composite Patterns](./implementation-concepts/README.md#composite-patterns) | Scenario as Agent/Tool, Workbench as Machine | Advanced composition |
| [DevOps & Lifecycle](./implementation-concepts/README.md#devops-and-lifecycle) | Artifact Registry, CI Subsystem, APM | Development workflow |
| [Integration](./implementation-concepts/README.md#integration) | MS Teams Integration, Hercules Launcher | External system integration |

→ **Full index:** [Implementation Concepts README](./implementation-concepts/README.md)

---

## Reading Order by Audience

### For Architects (New to Hub)

1. **[Hub Architecture](./hub-architecture.md)** — Philosophy and principles
2. **[Hub Design Philosophy](./hub-design-philosophy.md)** — Theoretical foundations
3. **[Architecture Layers](./architecture-layers.md)** — Four-layer mapping
4. **[Subsystem Map](./subsystem-map.md)** — Subsystem boundaries
5. **[Security View](./views/security-view.md)** — Security model
6. **[Deployment View](./views/deployment-view.md)** — Deployment topology
7. Dive into [Implementation Concepts](./implementation-concepts/README.md) as needed

### For Developers (Building on Hub)

1. **[Hub Architecture](./hub-architecture.md)** — Core concepts
2. **[Signal Flow](./signal-flow.md)** — End-to-end processing
3. **[Workbench Anatomy](./workbench-anatomy.md)** — Workbench internals
4. **[Runtime View](./views/runtime-view.md)** — Execution model
5. Start with [Hub Application](./implementation-concepts/hub-application.md) and [Automation Runtime](./implementation-concepts/automation-runtime.md)

### For Product Managers (Understanding Capabilities)

1. **[Hub Architecture](./hub-architecture.md)** — What Hub does
2. **[Agent Model](./agent-model.md)** — How agents interact
3. **[Persona Journey View](./views/persona-journey-view.md)** — User experience
4. Review [Persona](./implementation-concepts/persona.md) and [Channel](./implementation-concepts/channel.md)

### For Platform Engineers (Operating Hub)

1. **[Subsystem Map](./subsystem-map.md)** — System boundaries
2. **[Deployment View](./views/deployment-view.md)** — Topology and promotion
3. **[Runtime View](./views/runtime-view.md)** — Execution hosts
4. Start with [Operator](./implementation-concepts/operator.md) and [CRD](./implementation-concepts/crd.md)

---

## Folder Structure

```
02-system-design/
├── README.md                      ← You are here
├── hub-architecture.md            # Executive overview
├── hub-design-philosophy.md       # Theoretical foundations
├── architecture-layers.md         # Four-layer mapping
├── signal-flow.md                 # End-to-end signal processing
├── workbench-anatomy.md           # Workbench internals
├── agent-model.md                 # Human + AI agent model
├── subsystem-map.md               # Subsystem boundaries
│
├── views/                         # Curated architectural perspectives
│   ├── README.md
│   ├── data-flow-view.md
│   ├── runtime-view.md
│   ├── deployment-view.md
│   ├── security-view.md
│   ├── persona-journey-view.md
│   └── integration-view.md
│
└── implementation-concepts/       # 42 detailed concept documents
    ├── README.md                  # Concept index
    ├── tenant.md
    ├── subscription.md
    ├── signal-exchange.md
    ├── hub-application.md
    └── ... (38 more concept docs)
```

---

## Related Documentation

| Section | Purpose |
|---------|---------|
| [Concepts (01)](../01-concepts/) | Theoretical ontology and foundations |
| [Decision Logs (03)](../03-decision-logs/) | Architecture decision records (ADRs) |
| [Subsystems (04)](../04-subsystems/) | Technical subsystem documentation |
| [Personas (06)](../06-personas/) | Detailed persona definitions |
| [Guides (10)](../10-guides/) | Practical how-to guides |

