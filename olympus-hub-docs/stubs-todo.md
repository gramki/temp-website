# Hub Subsystem Stubs — Expansion Tracker

> **Purpose:** Track stub files that need to be expanded into full design documents.

---

## Overview

This file tracks all subsystem stub documents created for Olympus Hub. Each stub provides a placeholder with scope, key concepts, and integration points. Stubs should be expanded into full design documents as the system design progresses.

---

## Stub Status Legend

| Status | Meaning |
|--------|---------|
| 🔴 Stub | Placeholder only — needs full design |
| 🟡 WIP | Work in progress — partial content |
| ✅ Complete | Ready for use |

---

## Subsystem Stubs

### Signal Exchange (`04-subsystems/signal-exchange/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [README.md](./04-subsystems/signal-exchange/README.md) | Signal Exchange overview — the data plane | 🔴 Stub | Critical |
| [message-envelope.md](./04-subsystems/signal-exchange/message-envelope.md) | Standard envelope, request states, response status | 🔴 Stub | Critical |
| [trigger-evaluator.md](./04-subsystems/signal-exchange/trigger-evaluator.md) | Trigger matching and transformation | 🔴 Stub | Critical |
| [request-factory.md](./04-subsystems/signal-exchange/request-factory.md) | Request creation and updates | 🔴 Stub | Critical |
| [application-router.md](./04-subsystems/signal-exchange/application-router.md) | Routing Requests to Hub Applications | 🔴 Stub | Critical |
| [response-transformer.md](./04-subsystems/signal-exchange/response-transformer.md) | Response transformation for I/O Gateways | 🔴 Stub | High |
| [flow-controller.md](./04-subsystems/signal-exchange/flow-controller.md) | Flow control and store-and-forward | 🔴 Stub | High |
| [observer-notifications.md](./04-subsystems/signal-exchange/observer-notifications.md) | Async updates and observer notifications | 🔴 Stub | High |

### Workbench Management (`04-subsystems/workbench-management/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [README.md](./04-subsystems/workbench-management/README.md) | Workbench Management overview — the control plane | 🔴 Stub | Critical |
| [workbench-lifecycle.md](./04-subsystems/workbench-management/workbench-lifecycle.md) | Workbench states and transitions | 🔴 Stub | High |
| [scenario-definitions.md](./04-subsystems/workbench-management/scenario-definitions.md) | Scenario configuration | 🔴 Stub | High |
| [trigger-definitions.md](./04-subsystems/workbench-management/trigger-definitions.md) | Trigger configuration | 🔴 Stub | Critical |
| [application-configuration.md](./04-subsystems/workbench-management/application-configuration.md) | Hub Application setup | 🔴 Stub | High |

### Automation Runtimes (`04-subsystems/automation-runtimes/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [README.md](./04-subsystems/automation-runtimes/README.md) | Automation Runtimes overview | 🔴 Stub | High |
| [atlantis-runtime.md](./04-subsystems/automation-runtimes/atlantis-runtime.md) | Knative/KServe container runtime | 🔴 Stub | High |
| [perseus-batch-processing.md](./04-subsystems/automation-runtimes/perseus-batch-processing.md) | File, Map-Reduce, Complex Event applications | 🔴 Stub | Medium |
| [rhea-workflow-engine.md](./04-subsystems/automation-runtimes/rhea-workflow-engine.md) | BPMN workflow host | 🔴 Stub | High |
| [chronoshift-temporal.md](./04-subsystems/automation-runtimes/chronoshift-temporal.md) | Temporal-based durable workflow host | 🔴 Stub | High |
| [seer-case-automation.md](./04-subsystems/automation-runtimes/seer-case-automation.md) | Seer Agent Engine as Case Automation Runtime | 🔴 Stub | High |

### Memory Services (`04-subsystems/memory-services/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [README.md](./04-subsystems/memory-services/README.md) | Memory Services overview | 🔴 Stub | High |
| [hub-agent-memory.md](./04-subsystems/memory-services/hub-agent-memory.md) | Agent Memory persistence and management | 🔴 Stub | High |
| [hub-enterprise-memory.md](./04-subsystems/memory-services/hub-enterprise-memory.md) | Enterprise Memory persistence and management | 🔴 Stub | High |

### Cognitive Audit Fabric (`04-subsystems/cognitive-audit-fabric/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [README.md](./04-subsystems/cognitive-audit-fabric/README.md) | CAF overview — Enterprise Memory Control Plane | 🔴 Stub | Critical |
| [decision-records.md](./04-subsystems/cognitive-audit-fabric/decision-records.md) | Decision journaling and rationale capture | 🔴 Stub | Critical |
| [explanation-service.md](./04-subsystems/cognitive-audit-fabric/explanation-service.md) | Explanation generation and narrative assembly | 🔴 Stub | High |
| [evidence-bundles.md](./04-subsystems/cognitive-audit-fabric/evidence-bundles.md) | Evidence packaging and context preservation | 🔴 Stub | High |

### Registry Services (`04-subsystems/registry-services/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [README.md](./04-subsystems/registry-services/README.md) | Registry Services overview | 🔴 Stub | High |
| [tool-registry.md](./04-subsystems/registry-services/tool-registry.md) | Tool catalog, schemas, permissions | 🔴 Stub | High |
| [machine-registry.md](./04-subsystems/registry-services/machine-registry.md) | Machine catalog and capabilities | 🔴 Stub | Medium |
| [environment-registry.md](./04-subsystems/registry-services/environment-registry.md) | Environment definitions and sandboxes | 🔴 Stub | Medium |

### Knowledge Services (`04-subsystems/knowledge-services/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [README.md](./04-subsystems/knowledge-services/README.md) | Knowledge Services overview | 🔴 Stub | High |
| [knowledge-bank.md](./04-subsystems/knowledge-services/knowledge-bank.md) | RAG, ingress pipelines, content retrieval | 🔴 Stub | High |

### Task Management (`04-subsystems/task-management/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [README.md](./04-subsystems/task-management/README.md) | Task Management overview | 🔴 Stub | High |
| [task-queues.md](./04-subsystems/task-management/task-queues.md) | Task queue definitions and routing | 🔴 Stub | High |
| [task-lifecycle.md](./04-subsystems/task-management/task-lifecycle.md) | Task states and transitions | 🔴 Stub | High |
| [task-assignment.md](./04-subsystems/task-management/task-assignment.md) | Task assignment to agents (human/AI) | 🔴 Stub | High |

### Request Management (`04-subsystems/request-management/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [README.md](./04-subsystems/request-management/README.md) | Request Management overview | 🔴 Stub | High |
| [request-lifecycle.md](./04-subsystems/request-management/request-lifecycle.md) | Request states, updates, session boundary | 🔴 Stub | High |
| [request-storage.md](./04-subsystems/request-management/request-storage.md) | Request scope storage | 🔴 Stub | Medium |
| [request-entity-binding.md](./04-subsystems/request-management/request-entity-binding.md) | Request to Business Entity mapping | 🔴 Stub | Medium |

### Subscription Management (`04-subsystems/subscription-management/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [README.md](./04-subsystems/subscription-management/README.md) | Subscription Management overview | 🔴 Stub | High |
| [tenant-subscription-lifecycle.md](./04-subsystems/subscription-management/tenant-subscription-lifecycle.md) | Subscription states and transitions | 🔴 Stub | High |
| [resource-management.md](./04-subsystems/subscription-management/resource-management.md) | Resource allocation and provisioning | 🔴 Stub | High |
| [resource-configuration.md](./04-subsystems/subscription-management/resource-configuration.md) | Resource configuration per tenant | 🔴 Stub | Medium |
| [budget-management.md](./04-subsystems/subscription-management/budget-management.md) | Quotas, limits, usage tracking | 🔴 Stub | High |
| [branding-themes.md](./04-subsystems/subscription-management/branding-themes.md) | Tenant customization and white-labeling | 🔴 Stub | Low |
| [administrators-management.md](./04-subsystems/subscription-management/administrators-management.md) | Tenant admin access and permissions | 🔴 Stub | High |

### User Management (`04-subsystems/user-management/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [README.md](./04-subsystems/user-management/README.md) | User Management overview — all personas and scopes | 🔴 Stub | High |
| [hub-system-users.md](./04-subsystems/user-management/hub-system-users.md) | SRE and Customer Success (Publisher Domain) | 🔴 Stub | High |
| [tenant-subscription-users.md](./04-subsystems/user-management/tenant-subscription-users.md) | Administrators, Process Architects, Developers, Auditors | 🔴 Stub | High |
| [workbench-users.md](./04-subsystems/user-management/workbench-users.md) | Agents and Supervisors | 🔴 Stub | High |
| [tenant-customers.md](./04-subsystems/user-management/tenant-customers.md) | Self-serve users and policies | 🔴 Stub | High |
| [domain-management.md](./04-subsystems/user-management/domain-management.md) | Publisher and Tenant domain organization | 🔴 Stub | Medium |

### Hub Native Utilities (`04-subsystems/hub-native-utilities/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [README.md](./04-subsystems/hub-native-utilities/README.md) | Native utilities overview (stateless + stateful) | 🔴 Stub | High |
| [decision-tools.md](./04-subsystems/hub-native-utilities/decision-tools.md) | Drools, DMN, JS pure-function decision services (stateless) | 🔴 Stub | High |
| [prediction-tools.md](./04-subsystems/hub-native-utilities/prediction-tools.md) | ML Models via Elara/Kserve (stateless) | 🔴 Stub | High |
| [caf-integration.md](./04-subsystems/hub-native-utilities/caf-integration.md) | Automatic CAF compliance for Decision/Prediction tools | 🔴 Stub | High |
| [checklist-service.md](./04-subsystems/hub-native-utilities/checklist-service.md) | Workbench-scoped scheduled multi-operation governance (stateful) | 🔴 Stub | High |
| [routine-service.md](./04-subsystems/hub-native-utilities/routine-service.md) | Agent-scoped scheduled operations — personal or assigned (stateful) | 🔴 Stub | High |
| [manual-task-application.md](./04-subsystems/hub-native-utilities/manual-task-application.md) | Pass-through app for manual tasks — 1:1 Request-Task wiring | 🔴 Stub | High |

### MS Teams Integration (`04-subsystems/ms-teams-integration/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [README.md](./04-subsystems/ms-teams-integration/README.md) | MS Teams Integration — Copilots, Chat Groups, Signal Routing | 🟡 WIP | High |
| [bot-architecture.md](./04-subsystems/ms-teams-integration/bot-architecture.md) | Me_Bot, Ask_Bot, Signal Exchange Bot details | 🟡 WIP | High |
| [chat-group-lifecycle.md](./04-subsystems/ms-teams-integration/chat-group-lifecycle.md) | Request → Chat Group mapping and lifecycle | 🟡 WIP | High |
| [message-flow.md](./04-subsystems/ms-teams-integration/message-flow.md) | Signal transformation and routing paths | 🟡 WIP | High |
| [ms-teams-integration-faq.md](./04-subsystems/ms-teams-integration/ms-teams-integration-faq.md) | Design decisions and Q&A | 🟡 WIP | High |
| [ms-teams-integration.md](./04-subsystems/signal-providers/ms-teams-integration.md) | Reference entry in Signal Providers | 🔴 Stub | Low |

---

## Existing Documents (Already WIP or Complete)

### Signal Providers (`04-subsystems/signal-providers/`)

| Document | Description | Status |
|----------|-------------|--------|
| [README.md](./04-subsystems/signal-providers/README.md) | I/O Gateway overview | 🟡 WIP |
| [atropos-event-bus.md](./04-subsystems/signal-providers/atropos-event-bus.md) | Event signal gateway | 🟡 WIP |
| [cronus-business-exceptions.md](./04-subsystems/signal-providers/cronus-business-exceptions.md) | Exception/Observation gateway | 🟡 WIP |
| [heracles-api-gateway.md](./04-subsystems/signal-providers/heracles-api-gateway.md) | HTTP/REST/MCP gateway | 🟡 WIP |
| [dia-file-gateway.md](./04-subsystems/signal-providers/dia-file-gateway.md) | File/batch gateway | 🟡 WIP |
| [kale-scheduler.md](./04-subsystems/signal-providers/kale-scheduler.md) | Time-based signal generator | 🟡 WIP |

### Supporting Systems (`04-subsystems/supporting-systems/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [cipher-iam.md](./04-subsystems/supporting-systems/cipher-iam.md) | Agent identity and authorization | ⚠️ Notes | High |
| [hub-application-apm.md](./04-subsystems/supporting-systems/hub-application-apm.md) | Application observability via Olympus Watch | 🔴 Stub | Medium |

---

## Data Architecture

### Data Architecture (`07-data-architecture/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [application-data-stores.md](./07-data-architecture/application-data-stores.md) | Ganymede, Callisto, Europa for applications | 🔴 Stub | High |

---

## Concept Documents

### Core Concepts (`01-concepts/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [hub-applications.md](./01-concepts/hub-applications.md) | Hub Application concept — automation artifacts | 🔴 Stub | High |

---

## Personas and Journeys

### Hub Personas (`08-personas-and-journeys/personas/`)

#### Workbench Designers

| Document | Category | Status | Priority |
|----------|----------|--------|----------|
| [process-architect.md](./08-personas-and-journeys/personas/process-architect.md) | Workbench Designer | 🔴 Stub | High |
| [developer.md](./08-personas-and-journeys/personas/developer.md) | Workbench Designer | 🔴 Stub | High |

#### Workbench Operations

| Document | Category | Status | Priority |
|----------|----------|--------|----------|
| [supervisor.md](./08-personas-and-journeys/personas/supervisor.md) | Workbench Operations | 🔴 Stub | High |
| [agent.md](./08-personas-and-journeys/personas/agent.md) | Workbench Operations | 🔴 Stub | High |

#### Tenant Administration

| Document | Category | Status | Priority |
|----------|----------|--------|----------|
| [administrator.md](./08-personas-and-journeys/personas/administrator.md) | Tenant Administration | 🔴 Stub | High |
| [auditor.md](./08-personas-and-journeys/personas/auditor.md) | Tenant Administration | 🔴 Stub | Medium |

#### Hub System (Publisher)

| Document | Category | Status | Priority |
|----------|----------|--------|----------|
| [sre.md](./08-personas-and-journeys/personas/sre.md) | Hub System | 🔴 Stub | Medium |
| [customer-success.md](./08-personas-and-journeys/personas/customer-success.md) | Hub System | 🔴 Stub | Medium |

### Business Domain Actors (`08-personas-and-journeys/personas/business-domain/`)

| Document | Request Type | Status | Priority |
|----------|--------------|--------|----------|
| [business-customer.md](./08-personas-and-journeys/personas/business-domain/business-customer.md) | Service Request | 🔴 Stub | High |
| [business-employee.md](./08-personas-and-journeys/personas/business-domain/business-employee.md) | Business Request | 🔴 Stub | High |
| [business-system-actor.md](./08-personas-and-journeys/personas/business-domain/business-system-actor.md) | System Request | 🔴 Stub | High |

### Journeys (`08-personas-and-journeys/journeys/`)

| Document | Personas Involved | Status | Priority |
|----------|-------------------|--------|----------|
| [scenario-development.md](./08-personas-and-journeys/journeys/scenario-development.md) | Process Architect → Developer → Supervisor | 🟡 WIP | Critical |
| [workbench-configuration.md](./08-personas-and-journeys/journeys/workbench-configuration.md) | Administrator → Process Architect → Supervisor | 🔴 Stub | High |
| [request-lifecycle.md](./08-personas-and-journeys/journeys/request-lifecycle.md) | Business Actor → Signal → Application → Agent | 🔴 Stub | High |
| [audit-investigation.md](./08-personas-and-journeys/journeys/audit-investigation.md) | Auditor | 🔴 Stub | Medium |

---

## Infrastructure Stubs

> **Note:** Hub uses Olympus Platform services. Infrastructure primitives (Kubernetes, Kafka, PostgreSQL) are abstracted by platform services (Atlantis, Atropos, Ganymede).

### Infrastructure (`05-infrastructure/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [olympus-platform-dependencies.md](./05-infrastructure/olympus-platform-dependencies.md) | Complete catalog of platform service dependencies | 🟡 WIP | Critical |
| [cloudflare-edge.md](./05-infrastructure/cloudflare-edge.md) | Edge layer, CDN, DDoS protection | 🔴 Stub | Medium |
| [cipher-iam-infrastructure.md](./05-infrastructure/cipher-iam-infrastructure.md) | SPIFFE/SPIRE, identity, authentication | 🔴 Stub | High |
| [temporal-cluster.md](./05-infrastructure/temporal-cluster.md) | Durable workflow engine (ChronoShift) | 🔴 Stub | High |
| [ganymede-rdbms.md](./05-infrastructure/ganymede-rdbms.md) | Relational DBaaS — Hub internal + applications | 🔴 Stub | High |
| [callisto-kv-store.md](./05-infrastructure/callisto-kv-store.md) | Key-Value store for applications | 🔴 Stub | Medium |
| [europa-opensearch.md](./05-infrastructure/europa-opensearch.md) | Search and analytics (ELK-as-a-Service) | 🔴 Stub | Medium |
| [redis-cache.md](./05-infrastructure/redis-cache.md) | Caching and rate limiting | 🔴 Stub | Medium |
| [knowledge-bank-infrastructure.md](./05-infrastructure/knowledge-bank-infrastructure.md) | RAG and knowledge retrieval infrastructure | 🔴 Stub | High |
| [olympus-watch.md](./05-infrastructure/olympus-watch.md) | Observability as a service | 🔴 Stub | High |

### Removed (Abstracted by Platform Services)

The following were removed as they are implementation details abstracted by Olympus Platform:

| Removed Document | Abstracted By |
|-----------------|---------------|
| `kubernetes-platform.md` | Atlantis (Compute IaaS) |
| `istio-service-mesh.md` | Atlantis (Compute IaaS) |
| `kafka-event-bus.md` | Atropos (Event Bus aaS) |
| `postgresql-database.md` | Ganymede (RDBMS aaS) |

---

## UX Architecture

### UX Architecture (`06-ux-architecture/`)

| Document | Description | Status | Priority |
|----------|-------------|--------|----------|
| [README.md](./06-ux-architecture/README.md) | UX Architecture overview — meta approach, persona-channel-use case | 🟡 WIP | High |
| [hub-control-center.md](./06-ux-architecture/hub-control-center.md) | Tenant Admin console | 🔴 Stub | High |
| [publisher-consoles.md](./06-ux-architecture/publisher-consoles.md) | SRE and Customer Success consoles | 🔴 Stub | Medium |
| [workbench-studio.md](./06-ux-architecture/workbench-studio.md) | Designer environment for Process Architects and Developers | 🔴 Stub | High |
| [hub-home.md](./06-ux-architecture/hub-home.md) | Landing page for Agents and Supervisors | 🔴 Stub | High |
| [agent-desk.md](./06-ux-architecture/agent-desk.md) | Agent operations console | 🔴 Stub | High |
| [supervisor-desk.md](./06-ux-architecture/supervisor-desk.md) | Supervisor management console | 🔴 Stub | High |
| [steward-desk.md](./06-ux-architecture/steward-desk.md) | Workbench admin console | 🔴 Stub | Medium |
| [mcp-channels.md](./06-ux-architecture/mcp-channels.md) | MCP Gateway architecture for AI integration | 🔴 Stub | High |
| [angelos-framework.md](./06-ux-architecture/angelos-framework.md) | UI component framework | 🔴 Stub | High |
| [hercules-launcher.md](./06-ux-architecture/hercules-launcher.md) | Launch URL service for deep linking | 🔴 Stub | Medium |
| [neutrino-integration.md](./06-ux-architecture/neutrino-integration.md) | Customer channel integration | 🔴 Stub | High |

---

## Seer Integration Requirements

These stubs are particularly important for Seer integration:

| Subsystem | Seer Dependency |
|-----------|-----------------|
| **Signal Exchange** | Routes Requests to Seer Case Orchestration Agents |
| **Workbench Management** | Defines Scenarios that bind to Seer Applications |
| **Memory Services** | Seer agents use Hub memory storage services |
| **Cognitive Audit Fabric** | CAF governs decision record structure; provides explanation service |
| **Knowledge Services** | Seer Context Assembly retrieves from Hub Knowledge Bank |
| **Tool Registry** | Seer agents invoke tools registered in Hub |
| **Task Management** | Seer agents receive and complete tasks via Hub |
| **Seer Case Automation** | Hub invokes Seer as an Automation Runtime |
| **Hub Native Utilities** | Seer agents invoke Decision Tools and Prediction Tools with automatic CAF compliance |

---

## Expansion Priority Order

1. **Critical** — Signal Exchange, Workbench Management (trigger-definitions, trigger-evaluator, application-router), CAF (decision records, explanation, evidence), Olympus Platform Dependencies, Scenario Development Journey
2. **High** — Memory Services, Task Management, Automation Runtimes (Rhea, ChronoShift, Seer Case), Hub Native Utilities (Decision Tools, Prediction Tools), Hub Applications concept, Infrastructure (Temporal, Cipher IAM, Ganymede, Knowledge Bank, Olympus Watch), Hub Personas (Process Architect, Developer, Supervisor, Agent, Administrator), Business Domain Actors (Business Customer, Business Employee, System Actor), Journeys (Workbench Configuration, Request Lifecycle), UX Architecture (MCP Gateways, Workbench Studio, Agent/Supervisor Desk, Angelos, Neutrino)
3. **Medium** — Registry Services, Knowledge Services, Request Management, Infrastructure (Cloudflare, Redis, Callisto, Europa), Personas (Auditor, SRE, Customer Success), Journeys (Audit Investigation), UX Architecture (Hub Control Center, Hercules Launcher, Publisher Consoles, Admin Desk)
4. **Lower** — Perseus, Machine/Environment Registries

---

*Last updated: 2026-01-04*

