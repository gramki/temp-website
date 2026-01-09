# Subsystem Map

> **Subsystem boundaries, responsibilities, and dependencies**

---

## Overview

Olympus Hub is composed of integrated subsystems that work together to deliver the operations management platform. This document maps the subsystems, their boundaries, and how they relate to each other.

---

## Subsystem Categories

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         SUBSYSTEM CATEGORIES                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   CONTROL PLANE                          DATA PLANE                          │
│   ─────────────                          ──────────                          │
│   • Configuration management             • Signal processing                 │
│   • Resource provisioning                • Request routing                   │
│   • Operator reconciliation              • Task execution                    │
│   • Registry services                    • Agent interaction                 │
│                                                                              │
│   Subsystems:                            Subsystems:                         │
│   ├── Operators                          ├── Signal Exchange                 │
│   ├── Subscription Management            ├── Signal Providers (I/O)          │
│   ├── Workbench Management               ├── Automation Runtimes             │
│   ├── Registry Services                  ├── Task Management                 │
│   └── Artifact Registry                  ├── Request Management              │
│                                          └── Notification Services           │
│                                                                              │
│   SUPPORTING SYSTEMS                     USER-FACING SYSTEMS                 │
│   ──────────────────                     ────────────────────                │
│   • Security                             • Web consoles                      │
│   • Observability                        • Chat integration                  │
│   • Knowledge/Memory                     • API access                        │
│                                                                              │
│   Subsystems:                            Subsystems:                         │
│   ├── Cipher (IAM)                       ├── Angelos (Web)                   │
│   ├── Cognitive Audit Fabric             ├── MS Teams Integration            │
│   ├── Memory Services                    ├── Heracles (REST API)             │
│   ├── Knowledge Services                 └── MCP Channels                    │
│   └── Hub Analytics                                                          │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Core Subsystems

### Signal Architecture

| Subsystem | Purpose | Key Components |
|-----------|---------|----------------|
| **Signal Exchange** | Central routing and orchestration | Trigger Evaluator, Request Factory, Application Router, Flow Controller |
| **Signal Providers** | Protocol-specific I/O | Heracles (HTTP), Atropos (Events), Cronus (Exceptions), Dia (Files), Kale (Scheduler) |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SIGNAL ARCHITECTURE                                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   EXTERNAL                SIGNAL PROVIDERS              SIGNAL EXCHANGE      │
│   ────────                ────────────────              ───────────────      │
│                                                                              │
│   HTTP ──────────────────▶ Heracles ──┐                                     │
│                                       │    ┌─────────────────────────────┐  │
│   Events ────────────────▶ Atropos ───┼───▶│   Trigger Evaluator         │  │
│                                       │    │   Request Factory           │  │
│   Exceptions ────────────▶ Cronus ────┤    │   Application Router        │  │
│                                       │    │   Flow Controller           │  │
│   Files ─────────────────▶ Dia ───────┤    │   Observer Notifier         │  │
│                                       │    │   Reminder Service          │  │
│   Schedule ──────────────▶ Kale ──────┘    └─────────────────────────────┘  │
│                                                         │                    │
│                                                         ▼                    │
│                                               Hub Applications               │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

→ **Details:** [Signal Exchange](./implementation-concepts/signal-exchange.md) | [I/O Gateway](./implementation-concepts/io-gateway.md)

---

### Automation Runtimes

| Runtime | Type | Use Case |
|---------|------|----------|
| **Atlantis** | Container Runtime (Knative) | Procedures, Decision/Prediction Apps |
| **Rhea** | Workflow Engine (BPMN) | Deterministic workflows |
| **Seer** | AI Agent Runtime | LLM-based case automation |
| **ChronoShift** | Durable Workflow (Temporal) | Long-running operations, cases |
| **Perseus** | Batch Processing | File applications, map-reduce |

```
Hub Application
      │
      │ Deployed to
      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  AUTOMATION RUNTIMES                                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │  ATLANTIS   │  │    RHEA     │  │    SEER     │  │ CHRONOSHIFT │        │
│  │             │  │             │  │             │  │             │        │
│  │ Containers  │  │   BPMN      │  │  AI Agent   │  │  Temporal   │        │
│  │ Procedures  │  │  Workflows  │  │    Case     │  │  Durable    │        │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘        │
│                                                                              │
│  ┌─────────────────────────────┐                                            │
│  │         PERSEUS             │                                            │
│  │    Batch / File Processing  │                                            │
│  └─────────────────────────────┘                                            │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

→ **Details:** [Automation Runtime](./implementation-concepts/automation-runtime.md) | [Subsystems: Automation Runtimes](../04-subsystems/automation-runtimes/README.md)

---

### Work Management

| Subsystem | Purpose | Key Functions |
|-----------|---------|---------------|
| **Request Management** | Request lifecycle | Create, track, correlate, complete |
| **Task Management** | Task distribution | Allocation, queues, escalation |
| **Notification Services** | User notification | Multi-channel delivery |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  WORK MANAGEMENT                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   REQUEST MANAGEMENT              TASK MANAGEMENT                            │
│   ──────────────────              ───────────────                            │
│                                                                              │
│   ┌─────────────────────┐        ┌─────────────────────────────────────┐   │
│   │ Request Lifecycle   │        │ Task Allocation                      │   │
│   │   • CREATED         │        │   • Queue-based                     │   │
│   │   • IN_PROGRESS     │───────▶│   • Direct assignment               │   │
│   │   • ON_HOLD         │        │   • Group assignment                │   │
│   │   • COMPLETED       │        │   • AI delegation                   │   │
│   └─────────────────────┘        └─────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────┐        ┌─────────────────────────────────────┐   │
│   │ Request Storage     │        │ Escalation Matrix                   │   │
│   │   • Ganymede        │        │   • Time-based                      │   │
│   │   • Europa (search) │        │   • Cumulative assignment           │   │
│   └─────────────────────┘        └─────────────────────────────────────┘   │
│                                                                              │
│                           NOTIFICATION SERVICES                              │
│                           ─────────────────────                              │
│                                                                              │
│                           ┌─────────────────────────────────────────────┐   │
│                           │ Multi-Channel Delivery                       │   │
│                           │   • Email, SMS, Push                        │   │
│                           │   • MS Teams, Web Console                   │   │
│                           │   • Template-based                          │   │
│                           └─────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

→ **Details:** [Request Lifecycle](./implementation-concepts/request-lifecycle.md) | [Task Allocation](./implementation-concepts/task-allocation.md) | [Notification Services](./implementation-concepts/notification-services.md)

---

### Configuration Management

| Subsystem | Purpose | Key Functions |
|-----------|---------|---------------|
| **Operators** | GitOps reconciliation | Watch CRDs, reconcile state |
| **Subscription Management** | Resource boundaries | Provisioning, quotas |
| **Workbench Management** | Workbench config | Scenarios, triggers, applications |
| **Registry Services** | Resource registries | Machines, Tools, Environments |
| **Artifact Registry** | Container/CRD storage | Images, migrations |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CONFIGURATION MANAGEMENT                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   GIT REPOSITORY                         OPERATORS                           │
│   ──────────────                         ─────────                           │
│                                                                              │
│   ┌─────────────────────┐               ┌────────────────────────────────┐  │
│   │ Subscription Git    │               │ SRE Operator                   │  │
│   │                     │               │ Win Operator                   │  │
│   │ • Scenario specs    │   ◀──watch──▶ │ Resource Operators             │  │
│   │ • Application specs │               │ Workbench Operators            │  │
│   │ • Queue configs     │               │ Scenario Operators             │  │
│   └─────────────────────┘               └────────────────────────────────┘  │
│                                                                              │
│   REGISTRIES                             ARTIFACT REGISTRY                   │
│   ──────────                             ────────────────                    │
│                                                                              │
│   ┌─────────────────────┐               ┌────────────────────────────────┐  │
│   │ Machine Registry    │               │ Container Registry              │  │
│   │ Tool Registry       │               │   • Snapshot (dev)              │  │
│   │ Environment Registry│               │   • Production (promoted)       │  │
│   └─────────────────────┘               │ CRD Repository                  │  │
│                                         │ Data Store Migrations           │  │
│                                         └────────────────────────────────┘  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

→ **Details:** [Operator](./implementation-concepts/operator.md) | [CRD](./implementation-concepts/crd.md) | [Artifact Registry](./implementation-concepts/artifact-registry.md)

---

### Data Services

| Subsystem | Purpose | Key Functions |
|-----------|---------|---------------|
| **Application Data Store** | Transactional storage | Ganymede, Callisto, Europa |
| **Memory Services** | Agent memory | Enterprise, Agent, User memory |
| **Knowledge Services** | Document retrieval | RAG, Knowledge Bank |
| **Cognitive Audit Fabric** | Audit and control | Evidence, explainability |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DATA SERVICES                                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   TRANSACTIONAL                          SEMANTIC                            │
│   ─────────────                          ────────                            │
│                                                                              │
│   ┌─────────────────────┐               ┌────────────────────────────────┐  │
│   │ APPLICATION DATA    │               │ MEMORY SERVICES                │  │
│   │                     │               │                                │  │
│   │ Ganymede (SQL)      │               │ Enterprise Memory (shared)     │  │
│   │ Callisto (KV)       │               │ Agent Memory (per agent)       │  │
│   │ Europa (Search)     │               │ User Memory (per user)         │  │
│   └─────────────────────┘               └────────────────────────────────┘  │
│                                                                              │
│   ┌─────────────────────┐               ┌────────────────────────────────┐  │
│   │ KNOWLEDGE SERVICES  │               │ COGNITIVE AUDIT FABRIC         │  │
│   │                     │               │                                │  │
│   │ Knowledge Bank      │               │ Decision Records               │  │
│   │ RAG Retrieval       │               │ Evidence Bundles               │  │
│   │ Document Storage    │               │ Explanation Service            │  │
│   └─────────────────────┘               └────────────────────────────────┘  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

→ **Details:** [Application Data Store](./implementation-concepts/application-data-store.md) | [Memory Services](./implementation-concepts/memory-services.md) | [Knowledge Bank](./implementation-concepts/knowledge-bank.md) | [Cognitive Audit Fabric](./implementation-concepts/cognitive-audit-fabric.md)

---

### User-Facing Systems

| Subsystem | Purpose | Users |
|-----------|---------|-------|
| **Angelos** | Web console applications | All personas |
| **MS Teams Integration** | Chat bots | Agents, Supervisors, Users |
| **MCP Channels** | AI assistant interface | AI-enabled personas |
| **REST Channels** | Programmatic access | All (automation) |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  USER-FACING SYSTEMS                                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    WEB CONSOLES (ANGELOS)                            │   │
│   │                                                                      │   │
│   │   Hub Control Center    Workbench Studio    Agent Desk              │   │
│   │   (Administrator)       (Architect/Dev)     (Agent)                 │   │
│   │                                                                      │   │
│   │   Supervisor Desk       Steward Desk        Hub Home                │   │
│   │   (Supervisor)          (WB Admin)          (All)                   │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    INTEGRATION CHANNELS                              │   │
│   │                                                                      │   │
│   │   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐            │   │
│   │   │  MS Teams   │    │     MCP     │    │    REST     │            │   │
│   │   │  Me_Bot     │    │  AI Agents  │    │    API      │            │   │
│   │   │  Ask_Bot    │    │  Assistants │    │  Heracles   │            │   │
│   │   └─────────────┘    └─────────────┘    └─────────────┘            │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

→ **Details:** [Channel](./implementation-concepts/channel.md) | [Persona](./implementation-concepts/persona.md) | [MS Teams Integration](./implementation-concepts/ms-teams-integration.md)

---

### Supporting Systems

| Subsystem | Purpose | Key Functions |
|-----------|---------|---------------|
| **Cipher (IAM)** | Identity and access | SSO, RBAC, SPIFFE |
| **Hub Analytics** | Observability | Metrics, dashboards |
| **CI Subsystem** | Build and test | Runtime CI, test runner |
| **Hub Native Utilities** | Built-in tools | Checklists, decisions, predictions |

---

## Subsystem Dependencies

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SUBSYSTEM DEPENDENCY GRAPH                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   USER CHANNELS                                                              │
│       │                                                                      │
│       ▼                                                                      │
│   ┌───────────────────┐                                                     │
│   │  CIPHER (IAM)     │ ◀──────────────────────── All subsystems auth      │
│   └───────────────────┘                                                     │
│       │                                                                      │
│       ▼                                                                      │
│   ┌───────────────────┐     ┌───────────────────┐                          │
│   │  SIGNAL EXCHANGE  │────▶│  AUTOMATION       │                          │
│   │                   │     │  RUNTIMES         │                          │
│   └─────────┬─────────┘     └─────────┬─────────┘                          │
│             │                         │                                     │
│             ▼                         ▼                                     │
│   ┌───────────────────┐     ┌───────────────────┐                          │
│   │  REQUEST          │────▶│  TASK             │                          │
│   │  MANAGEMENT       │     │  MANAGEMENT       │                          │
│   └─────────┬─────────┘     └─────────┬─────────┘                          │
│             │                         │                                     │
│             ▼                         ▼                                     │
│   ┌───────────────────┐     ┌───────────────────┐                          │
│   │  NOTIFICATION     │     │  REGISTRY         │                          │
│   │  SERVICES         │     │  SERVICES         │                          │
│   └───────────────────┘     └───────────────────┘                          │
│             │                         │                                     │
│             ▼                         ▼                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                    DATA SERVICES                                     │  │
│   │   Application Data  •  Memory  •  Knowledge  •  Audit               │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Subsystem Index

| Category | Subsystem | Documentation |
|----------|-----------|---------------|
| **Signal** | Signal Exchange | [04-subsystems/signal-exchange](../04-subsystems/signal-exchange/README.md) |
| **Signal** | Signal Providers | [04-subsystems/signal-providers](../04-subsystems/signal-providers/README.md) |
| **Automation** | Automation Runtimes | [04-subsystems/automation-runtimes](../04-subsystems/automation-runtimes/README.md) |
| **Work** | Request Management | [04-subsystems/request-management](../04-subsystems/request-management/README.md) |
| **Work** | Task Management | [04-subsystems/task-management](../04-subsystems/task-management/README.md) |
| **Work** | Notification Services | [04-subsystems/notification-services](../04-subsystems/notification-services/README.md) |
| **Config** | Operators | [04-subsystems/operators](../04-subsystems/operators/README.md) |
| **Config** | Subscription Management | [04-subsystems/subscription-management](../04-subsystems/subscription-management/README.md) |
| **Config** | Workbench Management | [04-subsystems/workbench-management](../04-subsystems/workbench-management/README.md) |
| **Config** | Registry Services | [04-subsystems/registry-services](../04-subsystems/registry-services/README.md) |
| **Config** | Artifact Registry | [04-subsystems/artifact-registry](../04-subsystems/artifact-registry/README.md) |
| **Data** | Memory Services | [04-subsystems/memory-services](../04-subsystems/memory-services/README.md) |
| **Data** | Knowledge Services | [04-subsystems/knowledge-services](../04-subsystems/knowledge-services/README.md) |
| **Data** | Cognitive Audit Fabric | [04-subsystems/cognitive-audit-fabric](../04-subsystems/cognitive-audit-fabric/README.md) |
| **User** | MS Teams Integration | [04-subsystems/ms-teams-integration](../04-subsystems/ms-teams-integration/README.md) |
| **User** | User Management | [04-subsystems/user-management](../04-subsystems/user-management/README.md) |
| **Support** | CI Subsystem | [04-subsystems/ci-subsystem](../04-subsystems/ci-subsystem/README.md) |
| **Support** | Hub Native Utilities | [04-subsystems/hub-native-utilities](../04-subsystems/hub-native-utilities/README.md) |
| **Support** | Hub Analytics | [04-subsystems/hub-analytics](../04-subsystems/hub-analytics/README.md) |

---

## Related Documentation

| Document | Purpose |
|----------|---------|
| [Hub Architecture](./hub-architecture.md) | System overview |
| [Architecture Layers](./architecture-layers.md) | Ontology mapping |
| [Signal Flow](./signal-flow.md) | Signal processing |
| [Subsystems Section](../04-subsystems/) | Detailed subsystem docs |

