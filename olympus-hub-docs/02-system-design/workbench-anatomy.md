# Workbench Anatomy

> **What's inside a Workbench and how components relate**

---

## Overview

A **Workbench** is the fundamental operational unit in Olympus Hub — a self-contained domain environment where business operations are modeled, automated, and executed. This document explores the internal structure of a Workbench, its components, and how they work together.

---

## Workbench at a Glance

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            WORKBENCH                                         │
│                        (Domain Operational Environment)                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   WHAT IT MODELS                    HOW IT OPERATES                          │
│   ──────────────                    ────────────────                         │
│   • Business Entities               • Hub Applications                       │
│   • Scenarios                       • Task Queues                            │
│   • Tools & Machines                • Agents (Human + AI)                    │
│   • SOPs & Knowledge                • Consoles                               │
│                                                                              │
│   WHAT IT STORES                    HOW IT'S CONFIGURED                      │
│   ─────────────                     ─────────────────                        │
│   • Application Data                • Scenario Specifications                │
│   • Agent Memory                    • Environment Config                     │
│   • Knowledge Bank                  • Tool Bindings                          │
│   • Request History                 • Queue Settings                         │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Workbench Identity

Every Workbench has a clear identity within the Hub hierarchy:

```
Tenant (Enterprise)
    └── Subscription (Isolation Boundary)
            └── Workbench (Domain Environment)
                    ├── Dev-Lifecycle-Stage: DEV | STAGING | PROD
                    └── Blueprint (optional): Template it was created from
```

### Key Identifiers

| Attribute | Description | Example |
|-----------|-------------|---------|
| **ID** | Unique identifier | `dispute-ops-prod` |
| **Subscription** | Parent isolation boundary | `acme-prod` |
| **Tenant** | Parent enterprise | `acme-bank` |
| **Dev-Lifecycle-Stage** | Development phase | `PROD` |
| **Blueprint** | Source template (if any) | `dispute-management:2.0.0` |

→ **Details:** [Subscription](./implementation-concepts/subscription.md) | [Dev-Lifecycle-Stage](./implementation-concepts/dev-lifecycle-stage.md) | [Blueprint](./implementation-concepts/blueprint.md)

---

## Component Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         WORKBENCH COMPONENTS                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  SCENARIO LAYER                                                      │   │
│   │                                                                      │   │
│   │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │   │
│   │  │ Standard        │  │ Fraud           │  │ High-Value      │     │   │
│   │  │ Dispute         │  │ Dispute         │  │ Dispute         │     │   │
│   │  │                 │  │                 │  │                 │     │   │
│   │  │ Normative Spec  │  │ Normative Spec  │  │ Normative Spec  │     │   │
│   │  │ Automation Spec │  │ Automation Spec │  │ Automation Spec │     │   │
│   │  │ Deployment Spec │  │ Deployment Spec │  │ Deployment Spec │     │   │
│   │  └─────────────────┘  └─────────────────┘  └─────────────────┘     │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  APPLICATION LAYER                                                   │   │
│   │                                                                      │   │
│   │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │   │
│   │  │ Dispute Handler │  │ Fraud Detector  │  │ Notification    │     │   │
│   │  │ (ChronoShift)   │  │ (Seer)          │  │ (Atlantis)      │     │   │
│   │  └─────────────────┘  └─────────────────┘  └─────────────────┘     │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  DATA LAYER                                                          │   │
│   │                                                                      │   │
│   │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │   │
│   │  │ Ganymede        │  │ Callisto        │  │ Europa          │     │   │
│   │  │ (Relational)    │  │ (Key-Value)     │  │ (Search)        │     │   │
│   │  └─────────────────┘  └─────────────────┘  └─────────────────┘     │   │
│   │                                                                      │   │
│   │  ┌─────────────────┐  ┌─────────────────┐                          │   │
│   │  │ Memory Services │  │ Knowledge Bank  │                          │   │
│   │  │ (Agent Memory)  │  │ (RAG/Docs)      │                          │   │
│   │  └─────────────────┘  └─────────────────┘                          │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  EXECUTION LAYER                                                     │   │
│   │                                                                      │   │
│   │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │   │
│   │  │ Task Queues     │  │ Escalation      │  │ Agent Pools     │     │   │
│   │  │                 │  │ Matrices        │  │                 │     │   │
│   │  └─────────────────┘  └─────────────────┘  └─────────────────┘     │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Scenario Layer

Scenarios define **what happens** in the Workbench. Each Scenario represents a recognizable operational situation with three specifications:

| Specification | Owner | Content |
|---------------|-------|---------|
| **Normative Spec** | Process Architect | Roles, Goals, SOPs, Decision Criteria, Compliance |
| **Automation Spec** | Developer | Hub Application binding, Triggers, Tools |
| **Deployment Spec** | Supervisor | Task Queues, Agent Pools, SLAs, Activation |

### Scenario Elements

```yaml
# Example: Standard Dispute Scenario
scenario:
  name: standard-dispute
  
  # Normative (What ought to be done)
  roles:
    - dispute-analyst
    - supervisor
  goals:
    - "Investigate within 24 hours"
    - "Document findings completely"
  sops:
    - sop-dispute-investigation
    - sop-customer-communication
  compliance:
    - "Reg E: 10-day provisional credit"
  
  # Automation (How it's automated)
  application: dispute-handler
  triggers:
    - dispute-filed-trigger
    - document-uploaded-trigger
  tools:
    - transaction-lookup
    - customer-notification
  
  # Deployment (How it's deployed)
  queues:
    investigate: tier-1-disputes
    review: supervisor-review
  sla:
    target_hours: 72
    warning_hours: 48
```

→ **Details:** [Scenario Specification Types](./implementation-concepts/scenario-specification-types.md)

---

## Application Layer

Hub Applications are the **automation artifacts** that implement Scenario logic. They run on Automation Runtimes.

### Application Types

| Type | Runtime | Best For |
|------|---------|----------|
| **Container App** | Atlantis | Custom microservices |
| **Workflow App** | Rhea | BPMN deterministic flows |
| **AI Agent App** | Seer | LLM-based reasoning |
| **Batch App** | Perseus | File processing, ETL |
| **Durable Workflow** | ChronoShift | Long-running cases |

### Application Registration

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: dispute-handler
  namespace: acme-bank
spec:
  display_name: "Dispute Handler"
  version: "1.2.3"
  runtime: chronoshift  # Long-running case
  container:
    image: "registry.../dispute-handler"
    tag: "1.2.3"
  scenarios:
    - standard-dispute
    - fraud-dispute
  delivery:
    interface: http
    endpoint: "/handle"
```

→ **Details:** [Hub Application](./implementation-concepts/hub-application.md) | [Automation Runtime](./implementation-concepts/automation-runtime.md)

---

## Data Layer

Each Workbench has dedicated data stores for different purposes:

### Application Data Stores

| Store | Type | Purpose |
|-------|------|---------|
| **Ganymede** | Relational (PostgreSQL) | Structured business data, transactions |
| **Callisto** | Key-Value (Redis) | Session state, caches, counters |
| **Europa** | Search (Elasticsearch) | Full-text search, analytics |

### Memory and Knowledge

| Store | Purpose |
|-------|---------|
| **Memory Services** | Agent memory (Enterprise, Agent, User levels) |
| **Knowledge Bank** | SOPs, runbooks, documents for RAG retrieval |

### Data Isolation

```
Workbench A (dispute-ops-prod)
├── Ganymede: dispute-data
├── Callisto: dispute-cache
├── Europa: dispute-search
└── Knowledge Bank: dispute-knowledge

Workbench B (reconciliation-prod)
├── Ganymede: recon-data     ← ISOLATED, no cross-access
├── Callisto: recon-cache
└── Europa: recon-search
```

→ **Details:** [Application Data Store](./implementation-concepts/application-data-store.md) | [Memory Services](./implementation-concepts/memory-services.md) | [Knowledge Bank](./implementation-concepts/knowledge-bank.md)

---

## Execution Layer

The Execution Layer manages **how work gets done** by agents.

### Task Queues

```yaml
task_queues:
  - name: tier-1-disputes
    type: skill_based
    skills:
      - dispute-investigation
    priority_order: ["critical", "high", "normal"]
    
  - name: supervisor-review
    type: direct
    assignees:
      - role: supervisor
```

### Escalation Matrices

```yaml
escalation:
  - name: dispute-escalation
    cumulative: true  # Previous levels remain assigned
    levels:
      - timeout_minutes: 120
        assign_to: tier-1-disputes
      - timeout_minutes: 240
        assign_to: tier-2-disputes
      - timeout_minutes: 480
        assign_to: supervisor-review
```

### Agent Pools

| Pool Type | Description |
|-----------|-------------|
| **Human Agents** | Users enrolled with roles in this workbench |
| **AI Agents** | AI applications enrolled as agents |
| **Groups** | Logical groupings for assignment |

→ **Details:** [Task Allocation](./implementation-concepts/task-allocation.md) | [Escalation Matrix](./implementation-concepts/escalation-matrix.md)

---

## Configuration and Environment

### Hub Environment

Each Workbench has environment configuration that is **not promoted** (specific to each workbench instance):

```yaml
environment:
  variables:
    LOG_LEVEL: "INFO"
    MAX_CONCURRENT_REQUESTS: "100"
    
  secrets:
    - name: DATABASE_PASSWORD
      secret_ref: ganymede-db-password
      
  machines:
    - name: core-banking
      endpoint: "https://core.acme.com/api"
      credentials_ref: core-banking-creds
```

### Tool Bindings

Tools connect the Workbench to external capabilities (Machines):

```yaml
tools:
  - name: transaction-lookup
    machine: core-banking
    command: "get_transaction"
    
  - name: customer-notification
    machine: notification-service
    command: "send_email"
```

→ **Details:** [Hub Environment](./implementation-concepts/hub-environment.md)

---

## Workbench Lifecycle

### Creation

```
1. Select Blueprint (optional)
2. Specify Subscription and Dev-Lifecycle-Stage
3. Hub provisions:
   ├── Data stores (Ganymede, Callisto, Europa)
   ├── Knowledge Bank
   ├── Memory Services
   └── Runtime resources
4. Process Architect defines Scenarios (Normative Specs)
5. Developer builds Applications (Automation Specs)
6. Supervisor configures Deployment (Deployment Specs)
7. Activate Scenarios
```

### Promotion

Workbenches don't promote directly — their **artifacts** promote across subscriptions:

```
dispute-ops-dev (DEV stage, DEV subscription)
    │
    │ Promote artifacts (Hub Apps, Scenario Specs)
    ▼
dispute-ops-staging (STAGING stage, DEV subscription)
    │
    │ Promote artifacts (with approval)
    ▼
dispute-ops-prod (PROD stage, PROD subscription)
```

What promotes:
- Hub Application images
- Scenario specifications (all three types)
- Data migrations

What doesn't promote:
- Environment configuration
- Secrets
- Runtime data

→ **Details:** [Promotion](./implementation-concepts/promotion.md) | [Dev-Lifecycle-Stage](./implementation-concepts/dev-lifecycle-stage.md)

---

## Workbench Relationships

### Internal Relationships

```
Scenario ──references──▶ Hub Application
    │
    ├──references──▶ SOPs (Knowledge Bank)
    ├──references──▶ Tools (bound to Machines)
    └──maps to──▶ Task Queues
                     │
                     └──assigns to──▶ Agent Pools
```

### External Relationships

| Relationship | Description |
|--------------|-------------|
| **Workbench as Machine** | This workbench exposed as Machine to other workbenches |
| **Scenario as Tool** | Scenario exposed as callable tool |
| **Scenario as Agent** | Scenario published as task-completing agent |

→ **Details:** [Workbench as Machine](./implementation-concepts/workbench-as-machine.md) | [Scenario as Tool](./implementation-concepts/scenario-as-tool.md) | [Scenario as Agent](./implementation-concepts/scenario-as-agent.md)

---

## Observability

Each Workbench has built-in observability:

| Aspect | What's Monitored |
|--------|------------------|
| **Signal throughput** | Signals received per Scenario |
| **Request metrics** | Created, completed, SLA compliance |
| **Task metrics** | Assignment time, completion time |
| **Agent performance** | Tasks per agent, quality scores |
| **Application health** | CPU, memory, error rates |

→ **Details:** [APM](./implementation-concepts/apm.md)

---

## Related Documentation

| Document | Purpose |
|----------|---------|
| [Hub Architecture](./hub-architecture.md) | System overview |
| [Signal Flow](./signal-flow.md) | How signals flow through workbenches |
| [Agent Model](./agent-model.md) | How agents work within workbenches |
| [Subscription](./implementation-concepts/subscription.md) | Isolation boundary |
| [Blueprint](./implementation-concepts/blueprint.md) | Workbench templates |

