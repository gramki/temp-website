# Olympus Hub Documentation

> **Tracking:** [SPI-18123](https://zeta-saas.atlassian.net/browse/SPI-18123)

Olympus Hub is an operations management platform designed for large and medium enterprises to model, manage, and optimize business operations across any business domain through human-AI collaboration.

---

## 📚 Documentation Index

### 01 - Core Concepts

| Document | Description | Status |
|----------|-------------|--------|
| [Introduction](./01-concepts/introduction.md) | High-level introduction to "Everything is Ops" philosophy | ✅ Complete |
| [Ontology Reference](./01-concepts/ontology-reference.md) | Four-layer ontology: Perception → Normative → Execution → Automation | ✅ Complete |
| [Applicability Guide](./01-concepts/olympus-hub-applicability-guide.md) | Who should use Olympus Hub and where it delivers value | ✅ Complete |
| [Hub Applications](./01-concepts/hub-applications.md) | Automation artifacts that execute Scenarios | 🔴 Stub |

### 02 - System Design

| Document | Description | Status |
|----------|-------------|--------|
| [Hub Architecture](./02-system-design/hub-architecture.md) | Detailed system architecture: Workbenches, Agents, Signals, Operations | 🟡 WIP |

### 03 - Operations

| Document | Description | Status |
|----------|-------------|--------|
| [Case Management](./03-operations/case-management.md) | Case management in the agentic world | ⚠️ Notes |

*See [06 - UX Architecture](./06-ux-architecture/README.md) for user interaction channels*

### 04 - Subsystems

> **Expansion Tracking:** See [stubs-todo.md](./stubs-todo.md) for stub expansion progress

#### Signal Exchange (Data Plane)

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./04-subsystems/signal-exchange/README.md) | Signal Exchange — routes signals to applications | 🔴 Stub |
| [Message Envelope](./04-subsystems/signal-exchange/message-envelope.md) | Standard envelope for Application communication | 🔴 Stub |
| [Trigger Evaluator](./04-subsystems/signal-exchange/trigger-evaluator.md) | Trigger matching and transformation | 🔴 Stub |
| [Request Factory](./04-subsystems/signal-exchange/request-factory.md) | Request creation and updates | 🔴 Stub |
| [Application Router](./04-subsystems/signal-exchange/application-router.md) | Routes Requests to Hub Applications | 🔴 Stub |
| [Response Transformer](./04-subsystems/signal-exchange/response-transformer.md) | Response transformation for I/O Gateways | 🔴 Stub |
| [Flow Controller](./04-subsystems/signal-exchange/flow-controller.md) | Flow control and store-and-forward | 🔴 Stub |
| [Observer Notifications](./04-subsystems/signal-exchange/observer-notifications.md) | Async updates and notifications to observers | 🔴 Stub |

#### Workbench Management (Control Plane)

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./04-subsystems/workbench-management/README.md) | Workbench Management — Scenario, Trigger, Application definitions | 🔴 Stub |
| [Workbench Lifecycle](./04-subsystems/workbench-management/workbench-lifecycle.md) | Workbench states and transitions | 🔴 Stub |
| [Scenario Definitions](./04-subsystems/workbench-management/scenario-definitions.md) | Scenario configuration | 🔴 Stub |
| [Trigger Definitions](./04-subsystems/workbench-management/trigger-definitions.md) | Trigger configuration | 🔴 Stub |
| [Application Configuration](./04-subsystems/workbench-management/application-configuration.md) | Hub Application setup | 🔴 Stub |

#### I/O Gateways (Signal Providers)

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./04-subsystems/signal-providers/README.md) | I/O Gateway architecture and common responsibilities | 🟡 WIP |
| [Atropos - Event Bus](./04-subsystems/signal-providers/atropos-event-bus.md) | Event signal gateway (Kafka, RabbitMQ) | 🟡 WIP |
| [Cronus - Business Exceptions](./04-subsystems/signal-providers/cronus-business-exceptions.md) | Exception and Observation signal gateway | 🟡 WIP |
| [Heracles - API Gateway](./04-subsystems/signal-providers/heracles-api-gateway.md) | HTTP/REST/MCP signal gateway | 🟡 WIP |
| [Dia - File Gateway](./04-subsystems/signal-providers/dia-file-gateway.md) | File and batch input gateway | 🟡 WIP |
| [Kale - Scheduler](./04-subsystems/signal-providers/kale-scheduler.md) | Time-based signal generator | 🟡 WIP |

#### Automation Runtimes (Hub Application Hosts)

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./04-subsystems/automation-runtimes/README.md) | Automation Runtimes architecture | 🔴 Stub |
| [Atlantis Runtime](./04-subsystems/automation-runtimes/atlantis-runtime.md) | Knative/KServe container runtime | 🔴 Stub |
| [Perseus Batch Processing](./04-subsystems/automation-runtimes/perseus-batch-processing.md) | File, Map-Reduce, Complex Event applications | 🔴 Stub |
| [Rhea Workflow Engine](./04-subsystems/automation-runtimes/rhea-workflow-engine.md) | BPMN workflow host | 🔴 Stub |
| [ChronoShift Temporal](./04-subsystems/automation-runtimes/chronoshift-temporal.md) | Temporal-based durable workflow host | 🔴 Stub |
| [Seer Case Automation](./04-subsystems/automation-runtimes/seer-case-automation.md) | Seer Agent Engine as Case Automation Runtime | 🔴 Stub |

#### Memory Services

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./04-subsystems/memory-services/README.md) | Memory Services architecture | 🔴 Stub |
| [Hub Agent Memory](./04-subsystems/memory-services/hub-agent-memory.md) | Agent Memory persistence and management | 🔴 Stub |
| [Hub Enterprise Memory](./04-subsystems/memory-services/hub-enterprise-memory.md) | Enterprise Memory persistence and management | 🔴 Stub |

#### Cognitive Audit Fabric (CAF)

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./04-subsystems/cognitive-audit-fabric/README.md) | CAF — Enterprise Memory Control Plane | 🔴 Stub |
| [Decision Records](./04-subsystems/cognitive-audit-fabric/decision-records.md) | Decision journaling and rationale capture | 🔴 Stub |
| [Explanation Service](./04-subsystems/cognitive-audit-fabric/explanation-service.md) | Explanation generation and narrative assembly | 🔴 Stub |
| [Evidence Bundles](./04-subsystems/cognitive-audit-fabric/evidence-bundles.md) | Evidence packaging and context preservation | 🔴 Stub |

#### Registry Services

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./04-subsystems/registry-services/README.md) | Registry Services architecture | 🔴 Stub |
| [Tool Registry](./04-subsystems/registry-services/tool-registry.md) | Tool catalog, schemas, permissions | 🔴 Stub |
| [Machine Registry](./04-subsystems/registry-services/machine-registry.md) | Machine catalog and capabilities | 🔴 Stub |
| [Environment Registry](./04-subsystems/registry-services/environment-registry.md) | Environment definitions and sandboxes | 🔴 Stub |

#### Knowledge Services

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./04-subsystems/knowledge-services/README.md) | Knowledge Services architecture | 🔴 Stub |
| [Knowledge Bank](./04-subsystems/knowledge-services/knowledge-bank.md) | RAG, ingress pipelines, content retrieval | 🔴 Stub |

#### Task Management

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./04-subsystems/task-management/README.md) | Task Management architecture | 🔴 Stub |
| [Task Queues](./04-subsystems/task-management/task-queues.md) | Task queue definitions and routing | 🔴 Stub |
| [Task Lifecycle](./04-subsystems/task-management/task-lifecycle.md) | Task states and transitions | 🔴 Stub |
| [Task Assignment](./04-subsystems/task-management/task-assignment.md) | Assignment to human and AI agents | 🔴 Stub |

#### Request Management

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./04-subsystems/request-management/README.md) | Request Management architecture | 🔴 Stub |
| [Request Lifecycle](./04-subsystems/request-management/request-lifecycle.md) | Request states, updates, session boundary | 🔴 Stub |
| [Request Storage](./04-subsystems/request-management/request-storage.md) | Request scope storage | 🔴 Stub |
| [Request Entity Binding](./04-subsystems/request-management/request-entity-binding.md) | Request to Business Entity mapping | 🔴 Stub |

#### Subscription Management

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./04-subsystems/subscription-management/README.md) | Tenant administration subsystem | 🔴 Stub |
| [Tenant Subscription Lifecycle](./04-subsystems/subscription-management/tenant-subscription-lifecycle.md) | Subscription states and transitions | 🔴 Stub |
| [Resource Management](./04-subsystems/subscription-management/resource-management.md) | Resource allocation and provisioning | 🔴 Stub |
| [Resource Configuration](./04-subsystems/subscription-management/resource-configuration.md) | Resource configuration per tenant | 🔴 Stub |
| [Budget Management](./04-subsystems/subscription-management/budget-management.md) | Quotas, limits, usage tracking | 🔴 Stub |
| [Branding and Themes](./04-subsystems/subscription-management/branding-themes.md) | Tenant customization and white-labeling | 🔴 Stub |
| [Administrators Management](./04-subsystems/subscription-management/administrators-management.md) | Tenant admin access and permissions | 🔴 Stub |

#### User Management

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./04-subsystems/user-management/README.md) | User personas across all scopes | 🔴 Stub |
| [Hub System Users](./04-subsystems/user-management/hub-system-users.md) | SRE and Customer Success (Publisher Domain) | 🔴 Stub |
| [Tenant Subscription Users](./04-subsystems/user-management/tenant-subscription-users.md) | Administrators, Architects, Developers, Auditors | 🔴 Stub |
| [Workbench Users](./04-subsystems/user-management/workbench-users.md) | Agents and Supervisors | 🔴 Stub |
| [Tenant Customers](./04-subsystems/user-management/tenant-customers.md) | Self-serve users and policies | 🔴 Stub |
| [Domain Management](./04-subsystems/user-management/domain-management.md) | Publisher and Tenant domains | 🔴 Stub |

#### Hub Native Utilities

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./04-subsystems/hub-native-utilities/README.md) | Native stateless tools (Decision, Prediction) | 🔴 Stub |
| [Decision Tools](./04-subsystems/hub-native-utilities/decision-tools.md) | Drools, DMN, JS pure-function decision services | 🔴 Stub |
| [Prediction Tools](./04-subsystems/hub-native-utilities/prediction-tools.md) | ML Models via Elara/Kserve | 🔴 Stub |
| [CAF Integration](./04-subsystems/hub-native-utilities/caf-integration.md) | Automatic CAF compliance for native utilities | 🔴 Stub |

#### Supporting Systems

| Document | Description | Status |
|----------|-------------|--------|
| [Cipher IAM](./04-subsystems/supporting-systems/cipher-iam.md) | Agent identity and authorization (SPIFFE) | ⚠️ Notes |
| [Hub Application APM](./04-subsystems/supporting-systems/hub-application-apm.md) | Application observability via Olympus Watch | 🔴 Stub |

### 05 - Infrastructure

> **Note:** Hub is built on the Olympus Platform. Infrastructure primitives (Kubernetes, Kafka, PostgreSQL) are abstracted by platform services. See [Olympus Platform Dependencies](./05-infrastructure/olympus-platform-dependencies.md) for the complete picture.

#### Platform Overview

| Document | Description | Status |
|----------|-------------|--------|
| [Olympus Platform Dependencies](./05-infrastructure/olympus-platform-dependencies.md) | Complete catalog of platform service dependencies | 🟡 WIP |

#### API & Protocol Layer

| Document | Description | Status |
|----------|-------------|--------|
| [Heracles Gateway](./05-infrastructure/heracles-gateway.md) | Kong-based MCP gateway design | ✅ Complete |
| [MCP Orchestrator](./05-infrastructure/mcp-orchestrator.md) | Tool orchestration and resource service | ✅ Complete |
| [Cloudflare Edge](./05-infrastructure/cloudflare-edge.md) | Edge layer, CDN, DDoS protection | 🔴 Stub |

#### Platform Notes

| Document | Description | Status |
|----------|-------------|--------|
| [Traffic Management](./05-infrastructure/traffic-management.md) | Istio, SLIME, Aeraki notes (via Atlantis) | ⚠️ Notes |

#### Identity & Security

| Document | Description | Status |
|----------|-------------|--------|
| [Cipher IAM Infrastructure](./05-infrastructure/cipher-iam-infrastructure.md) | SPIFFE/SPIRE, identity, authentication | 🔴 Stub |

#### Workflow Engine

| Document | Description | Status |
|----------|-------------|--------|
| [Temporal Cluster](./05-infrastructure/temporal-cluster.md) | Durable workflow engine (ChronoShift) | 🔴 Stub |

#### Data Services (Olympus Platform)

| Document | Description | Status |
|----------|-------------|--------|
| [Ganymede RDBMS](./05-infrastructure/ganymede-rdbms.md) | Relational DBaaS — Hub internal + applications | 🔴 Stub |
| [Callisto KV Store](./05-infrastructure/callisto-kv-store.md) | Key-Value store for applications | 🔴 Stub |
| [Europa OpenSearch](./05-infrastructure/europa-opensearch.md) | Search and analytics (ELK-as-a-Service) | 🔴 Stub |
| [Redis Cache](./05-infrastructure/redis-cache.md) | Caching and rate limiting | 🔴 Stub |
| [Knowledge Bank Infrastructure](./05-infrastructure/knowledge-bank-infrastructure.md) | RAG and knowledge retrieval infrastructure | 🔴 Stub |

#### Observability

| Document | Description | Status |
|----------|-------------|--------|
| [Olympus Watch](./05-infrastructure/olympus-watch.md) | Observability as a service (APM, logs, metrics, traces) | 🔴 Stub |

### 06 - UX Architecture

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./06-ux-architecture/README.md) | UX Architecture and user interfacing applications | 🟡 WIP |
| [User Interaction Channels](./06-ux-architecture/user-interaction-channels.md) | Subject interaction patterns, Hercules Launcher | ⚠️ Notes |

*Coming soon: Hercules Launcher, Angelos Components, Ops Center UX, Neutrino Integration*

### 07 - Data Architecture

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./07-data-architecture/README.md) | Data architecture overview | 🟡 WIP |
| [Storage Architecture](./07-data-architecture/storage-architecture.md) | Layered storage model with selection guide | 🟡 WIP |
| [Application Data Stores](./07-data-architecture/application-data-stores.md) | Ganymede, Callisto, Europa for applications | 🔴 Stub |
| [Storage FAQ](./07-data-architecture/storage-faq.md) | Common questions for architects and developers | ✅ Complete |

### 10 - Guides

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./10-guides/README.md) | Guide index and reading order | 🟡 WIP |
| [Subscription Configuration Guide](./10-guides/subscription-configuration-guide.md) | Complete subscription configuration | 🟡 WIP |
| [Workbench Setup Guide](./10-guides/workbench-setup-guide.md) | Workbench configuration for a business domain | 🟡 WIP |

*Coming soon: Application Development Guide, Integration Guide, Agent Onboarding Guide*

### Project Tracking

| Document | Description |
|----------|-------------|
| [Todo](./Todo.md) | Outstanding documentation tasks |
| [Stubs Todo](./stubs-todo.md) | Subsystem stub expansion tracker |

---

## 🗺️ Quick Start Reading Order

1. **Start here:** [Introduction](./01-concepts/introduction.md) - Understand "Everything is Ops"
2. **Deep dive:** [Ontology Reference](./01-concepts/ontology-reference.md) - The conceptual foundation
3. **Evaluate fit:** [Applicability Guide](./01-concepts/olympus-hub-applicability-guide.md) - Is Olympus Hub right for you?
4. **Technical details:** [Hub Architecture](./02-system-design/hub-architecture.md) - Architecture and components

---

## 🏗️ Key Concepts

### The Operational Pattern

```
Signal → Trigger → Request → Scenario → Hub Application → Activities → Actions
  │                                          │
  └──────────────────────────────────────────┘
           (via Signal Exchange)
```

### Four-Layer Architecture

| Layer | Question | Concepts |
|-------|----------|----------|
| **Perception** | What's happening? | Domain, Environment, Machine, Sensors, Signal, Trigger, Scenario |
| **Normative** | What ought to be done? | Role, Goal, SOP, Responsibility, Capability, Decision |
| **Execution** | How is it done? | Procedure, Workflow, Case, Activities, Actions, Agent |
| **Automation** | How is it codified? | Automation, Automation Runtime, Tools, Actuators |

---

## 📁 Folder Structure

```
olympus-hub-docs/
├── README.md                    # This file - navigation hub
├── Todo.md                      # Outstanding tasks
├── stubs-todo.md                # Stub expansion tracker
├── assets/                      # Images and diagrams
│
├── 01-concepts/                 # Conceptual foundations
│   ├── introduction.md
│   ├── ontology-reference.md
│   └── olympus-hub-applicability-guide.md
│
├── 02-system-design/            # System architecture
│   └── hub-architecture.md
│
├── 03-operations/               # Operational patterns
│   └── case-management.md
│
├── 04-subsystems/               # Hub subsystems
│   ├── signal-exchange/            # Data plane: signal → application routing
│   ├── workbench-management/    # Control plane: Workbench definitions
│   ├── signal-providers/        # I/O Gateways
│   ├── automation-runtimes/      # Hub Application hosts
│   ├── memory-services/         # Agent & Enterprise Memory
│   ├── cognitive-audit-fabric/  # CAF - audit & explanation
│   ├── registry-services/       # Tool, Machine, Environment registries
│   ├── knowledge-services/      # Enterprise Knowledge / RAG
│   ├── task-management/         # Task queues, lifecycle, assignment
│   ├── request-management/      # Request lifecycle, storage, binding
│   ├── subscription-management/ # Tenant administration
│   ├── user-management/         # User personas and domains
│   └── supporting-systems/      # Cipher IAM
│
├── 05-infrastructure/           # Platform infrastructure
│   ├── olympus-platform-dependencies.md  # Platform services catalog
│   ├── heracles-gateway.md      # MCP gateway (Kong)
│   ├── mcp-orchestrator.md      # Tool orchestration
│   ├── cloudflare-edge.md       # Edge layer
│   ├── traffic-management.md    # Traffic notes (via Atlantis)
│   ├── cipher-iam-infrastructure.md  # SPIFFE/SPIRE
│   ├── temporal-cluster.md      # Durable workflows
│   ├── ganymede-rdbms.md        # Relational DBaaS (Hub + Apps)
│   ├── callisto-kv-store.md     # Key-value store
│   ├── europa-opensearch.md     # Search/analytics
│   ├── redis-cache.md           # Caching
│   ├── knowledge-bank-infrastructure.md  # RAG infra
│   └── olympus-watch.md         # Observability
│
├── 06-ux-architecture/          # UX & User Applications
│   ├── README.md
│   └── user-interaction-channels.md
│
├── 07-data-architecture/        # Data Architecture
│   ├── README.md
│   └── storage-architecture.md
│
└── 10-guides/                   # Practical Guides
    ├── README.md
    ├── subscription-configuration-guide.md
    └── workbench-setup-guide.md
```

---

## 🔗 Related Projects

| Project | Description |
|---------|-------------|
| **Olympus Seer** | AI Agent hosting platform — Agent lifecycle, runtime, and control plane |
| **Neutrino** | Customer interaction channels |
| **Angelos** | UI component framework |
| **Cipher** | Identity and Access Management |

---

## 📝 Document Status Legend

| Status | Meaning |
|--------|---------|
| ✅ Complete | Ready for use |
| 🟡 WIP | Work in progress, usable but incomplete |
| ⚠️ Notes | Raw notes, needs structuring |
| 🔴 Stub | Placeholder only |
