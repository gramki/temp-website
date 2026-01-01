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

#### I/O Gateways (Signal Providers)

| Document | Description | Status |
|----------|-------------|--------|
| [Overview](./04-subsystems/signal-providers/README.md) | I/O Gateway architecture and common responsibilities | 🟡 WIP |
| [Atropos - Event Bus](./04-subsystems/signal-providers/atropos-event-bus.md) | Event signal gateway (Kafka, RabbitMQ) | 🟡 WIP |
| [Cronus - Business Exceptions](./04-subsystems/signal-providers/cronus-business-exceptions.md) | Exception and Observation signal gateway | 🟡 WIP |
| [Heracles - API Gateway](./04-subsystems/signal-providers/heracles-api-gateway.md) | HTTP/REST/MCP signal gateway | 🟡 WIP |
| [Dia - File Gateway](./04-subsystems/signal-providers/dia-file-gateway.md) | File and batch input gateway | 🟡 WIP |
| [Kale - Scheduler](./04-subsystems/signal-providers/kale-scheduler.md) | Time-based signal generator | 🟡 WIP |

#### Automation Systems

| Document | Description | Status |
|----------|-------------|--------|
| [Atlantis Runtime](./04-subsystems/automation-systems/atlantis-runtime.md) | Knative/KServe container runtime | 🔴 Stub |

*Coming soon: Perseus, Rhea (BPMN), ChronoShift (Temporal)*

#### Supporting Systems

| Document | Description | Status |
|----------|-------------|--------|
| [Cipher IAM](./04-subsystems/supporting-systems/cipher-iam.md) | Agent identity and authorization (SPIFFE) | ⚠️ Notes |

*Coming soon: Seer (AI Agents), Angelos (UI Components)*

### 05 - Infrastructure

| Document | Description | Status |
|----------|-------------|--------|
| [Heracles Gateway](./05-infrastructure/heracles-gateway.md) | Kong-based MCP gateway design | ✅ Complete |
| [MCP Orchestrator](./05-infrastructure/mcp-orchestrator.md) | Tool orchestration and resource service | ✅ Complete |
| [Traffic Management](./05-infrastructure/traffic-management.md) | Istio, SLIME, Aeraki | ⚠️ Notes |

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
| [Storage Architecture](./07-data-architecture/storage-architecture.md) | Three-layer storage model: System, Tenant Spec, Operations | 🟡 WIP |

### Project Tracking

| Document | Description |
|----------|-------------|
| [Todo](./todo.md) | Outstanding documentation tasks |

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
Signal → Trigger → Scenario → Automation → Operation → Activities → Actions
```

### Four-Layer Architecture

| Layer | Question | Concepts |
|-------|----------|----------|
| **Perception** | What's happening? | Domain, Environment, Machine, Sensors, Signal, Trigger, Scenario |
| **Normative** | What ought to be done? | Role, Goal, SOP, Responsibility, Capability, Decision |
| **Execution** | How is it done? | Procedure, Workflow, Case, Activities, Actions, Agent |
| **Automation** | How is it codified? | Automation, Automation System, Tools, Actuators |

---

## 📁 Folder Structure

```
olympus-hub-docs/
├── README.md                    # This file - navigation hub
├── todo.md                      # Outstanding tasks
├── assets/                      # Images and diagrams
│   ├── human-ai-collab.png
│   └── olympus-hub-foundation-class-diagram.png
│
├── 01-concepts/                 # Conceptual foundations
│   ├── introduction.md          # "Everything is Ops" philosophy
│   ├── ontology-reference.md    # Four-layer ontology
│   └── olympus-hub-applicability-guide.md
│
├── 02-system-design/            # System architecture
│   └── hub-architecture.md      # Workbenches, Agents, Signals
│
├── 03-operations/               # Operational patterns
│   └── case-management.md       # Case & collaboration
│
├── 04-subsystems/               # Hub subsystems
│   ├── signal-providers/        # I/O Gateways
│   │   ├── README.md            # Overview
│   │   ├── atropos-event-bus.md # Event gateway
│   │   ├── cronus-business-exceptions.md # Exception/Observation gateway
│   │   ├── heracles-api-gateway.md # API gateway
│   │   ├── dia-file-gateway.md  # File gateway
│   │   └── kale-scheduler.md    # Scheduler
│   ├── automation-systems/
│   │   └── atlantis-runtime.md
│   └── supporting-systems/
│       └── cipher-iam.md
│
├── 05-infrastructure/           # Platform infrastructure
│   ├── heracles-gateway.md      # Kong/MCP gateway
│   ├── mcp-orchestrator.md      # Tool orchestration
│   └── traffic-management.md    # Service mesh
│
├── 06-ux-architecture/          # UX & User Applications
│   ├── README.md                # Overview
│   └── user-interaction-channels.md # Subject interaction
│
└── 07-data-architecture/        # Data Architecture
    ├── README.md                # Overview
    └── storage-architecture.md  # Three-layer storage model
```

---

## 🔗 Related Projects

| Project | Description |
|---------|-------------|
| **Olympus Seer** | AI Agent hosting platform |
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
