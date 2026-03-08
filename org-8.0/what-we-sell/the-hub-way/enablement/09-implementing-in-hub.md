# Implementing The Hub Way in Olympus Hub

This document provides implementation guidance for engineers and platform architects configuring The Hub Way concepts (Hubs, Streams, Loops, Channels, Teams, and Machines) in Olympus Hub. It covers the technical configuration of Workbenches as Hubs, Stream and Loop implementation, Channel setup, Channel Product composition, and integration patterns.

---

## 1. Hub to Workbench: Configuring a Workbench as a Hub

In Olympus Hub, a Hub maps to a **Workbench** — the platform's unit of domain encapsulation. Configuring a Workbench as a Hub involves defining the domain model, Scenario specifications, agent pools, knowledge base, memory, and multi-tenancy hierarchy.

### 1.1 Domain Model

Define the domain model that governs the Workbench's operational scope.

**Business Entities**

Model the core entities the Workbench operates on. These are typically defined in the Hub Application's data model and stored in the Application Data Stores (Ganymede for relational, Callisto for key-value, Europa for search). Entity definitions drive validation rules, lifecycle states, and tool contracts.

```yaml
# Example: Dispute Operations domain entities
entities:
  - name: dispute
    lifecycle_states: [filed, investigating, pending_docs, review, resolved, closed]
    validation_rules:
      - amount_must_be_positive
      - currency_required
  - name: transaction
    lifecycle_states: [pending, posted, disputed, refunded]
```

**Entity Lifecycles**

Each Business Entity has a lifecycle with defined states. Lifecycle transitions are enforced by the Hub Application and may trigger downstream Scenarios or notifications. Document state transitions in the Scenario Normative Spec for compliance traceability.

**Validation Rules**

Validation rules are enforced at signal ingestion (via Trigger evaluation), at Application entry points, and at tool invocation. Define validation rules in the domain model and reference them in Scenario Normative Specs.

### 1.2 Scenario Definitions

Scenarios define what happens in the Workbench. Each Scenario has three specifications, created sequentially by Process Architect, Developer, and Supervisor.

**Normative Spec (Process Architect)**

Defines what ought to be done: roles, goals, SOPs, decision criteria, compliance requirements.

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioNormativeSpec
metadata:
  name: standard-dispute
spec:
  roles:
    - name: dispute-analyst
      goals: ["Investigate within 24 hours", "Document findings completely"]
  sops:
    - ref: sop-dispute-investigation
  compliance:
    - regulation: "Reg E"
      requirements: ["10-day provisional credit for $500+"]
```

**Automation Spec (Developer)**

Defines how it is automated: Hub Application binding, triggers, tool bindings.

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAutomationSpec
metadata:
  name: standard-dispute
spec:
  application:
    ref: dispute-handler
  triggers:
    - ref: dispute-filed-trigger
  tools:
    - name: transaction-lookup
      ref: core-banking-transactions
```

**Deployment Spec (Supervisor)**

Defines how it is deployed: task queues, SLAs, agent enrollment, activation.

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioDeploymentSpec
metadata:
  name: standard-dispute
spec:
  task_queues:
    - task_type: investigate
      queue_ref: tier-1-disputes
  sla:
    target_completion_hours: 72
  activation:
    enabled: true
```

### 1.3 Agent Pools

Agent pools implement The Hub Way's **Team** concept at the platform level. Teams are the human and AI agents enrolled to resolve a Hub's Scenarios. The configuration below defines who is eligible, how tasks are assigned, and how human-AI collaboration is structured.

Agent pools determine who can execute tasks in the Workbench.

**Human Agents**

Users are enrolled in Workbenches with roles. Enrollment is managed via Cipher IAM and Workbench enrollment configuration. Human agents authenticate via SSO (SAML/OIDC) and receive tasks through Channels (Agent Desk, MS Teams, MCP).

```yaml
# Task queue with human agent pool
task_queue:
  name: tier-1-disputes
  type: skill_based
  agents:
    - type: human
      role: dispute-analyst
      skills: [dispute-investigation]
```

**AI Agents**

AI agents are registered in Hub with SPIFFE-based deployment identity and enrolled in Workbenches. They receive delegated tasks from Hub Applications and report outcomes. AI agents use EmploymentSpec for IAM provisioning and OPA policies for tool authorization.

```yaml
# Task queue with mixed human and AI agents
task_queue:
  name: evidence-review
  agents:
    - id: evidence-bot
      type: ai
      allocation_weight: 60
    - id: analyst-pool
      type: human
      allocation_weight: 40
```

**Enrollment**

Enrollment is Workbench-scoped. Process Architects or Supervisors configure which agents (human or AI) are eligible for which task queues. Enrollment determines task eligibility; Task Management assigns work based on availability, skills, and allocation weights.

### 1.4 Knowledge Base

The Knowledge Bank stores domain knowledge, SOPs, and runbooks for RAG retrieval by agents.

**Domain Knowledge**

Upload domain-specific documents, policies, and reference materials to the Workbench's Knowledge Bank. Reference knowledge in Scenario Normative Specs via SOP refs.

**SOPs and Runbooks**

SOPs are linked from Scenario Normative Specs. Runbooks provide step-by-step guidance for agents. Both are stored in the Knowledge Bank and retrieved via RAG when agents need context.

**Configuration**

Knowledge Bank is provisioned per Workbench. Configure document sources, indexing, and retention per Workbench requirements.

### 1.5 Memory Configuration

Memory Services provide agent memory at three levels. Configure per Workbench based on governance requirements.

**Enterprise Memory**

Stores decision records, evidence bundles, and cognitive audit data. Governed by the Cognitive Audit Fabric (CAF). Required for compliance-grade audit. Configure retention, schema validation, and CAF policies.

**Agentic Memory**

Session-scoped and request-scoped memory for AI agents. Not governed by CAF. Configure per agent deployment; typically short retention.

**User Memory**

User-scoped preferences and interaction history. Used for personalization across sessions.

**ESPP Taxonomy**

Enterprise Memory uses the ESPP (Episodic-Semantic-Procedural-Preference) taxonomy for record classification:

| Class | Description | Use Case |
|-------|-------------|----------|
| **Episodic** | Event-based, time-ordered, case-bound | Decision records, evidence bundles, incident timelines |
| **Semantic** | Learned beliefs, patterns, probabilistic inferences | Hypothesis records, pattern summaries, entity beliefs |
| **Procedural** | Learned skills, procedures, action sequences | Learned skills, procedures, tool usage patterns |
| **Preference** | User/agent preferences, interaction patterns | User preferences, agent behaviors, contextual preferences |

CAF enforces ESPP classification for Enterprise Memory. Configure memory capture policies and retention per memory class.

### 1.6 Multi-Tenancy: Tenant to Subscription to Workbench

The isolation hierarchy is:

```
Tenant (Enterprise)
    └── Subscription (Isolation Boundary)
            └── Workbench (Domain Environment)
                    ├── Dev-Lifecycle-Stage: DEV | STAGING | PROD
                    └── Blueprint (optional)
```

**Tenant**

Top-level organizational boundary (e.g., acme-bank). All resources belong to a tenant.

**Subscription**

Isolation boundary within a tenant. Subscriptions separate environments (e.g., dev subscription vs prod subscription). Workbenches belong to a subscription.

**Workbench**

Domain environment within a subscription. Each Workbench has dedicated data stores (Ganymede, Callisto, Europa), Knowledge Bank, Memory Services, and runtime resources. Cross-workbench context sharing requires workbenches to be in the same subscription.

---

## 2. Stream Implementation

Streams represent work performed against explicit external commitments. They are coordinated collections of Scenarios triggered by external signals.

### 2.1 Scenario Specifications for Stream Scenarios

Stream Scenarios use the same three-spec structure as all Scenarios. The distinction is trigger origin: external signals activate Stream Scenarios.

**Normative Spec**

Define goals, roles, SOPs, and compliance for the Stream Scenario. Focus on the external commitment being fulfilled: who is the external party, what does "fulfilled" look like?

**Automation Spec**

- **Hub Application**: Bind the Scenario to the Hub Application that implements the logic (Atlantis, Rhea, ChronoShift, Seer, Perseus).
- **Triggers**: Configure triggers that match external signals. Triggers evaluate normalized signals from I/O Gateways (Heracles, Atropos, Dia, Cronus).
- **Tool bindings**: Bind tools (Machines) the Application needs: transaction lookup, customer notification, etc.

**Deployment Spec**

- **Task queues**: Map task types to queues (e.g., investigate → tier-1-disputes).
- **SLAs**: Set target completion hours, warning thresholds.
- **Agent enrollment**: Configure which agents serve which queues.

### 2.2 Trigger Configuration for External Signals

Signals from the environment flow: **I/O Gateway → Normalized Signal → Signal Exchange → Trigger Evaluator → Scenario activation**.

**Signal Flow**

1. External systems (or Machines) emit signals via push (Webhook, Atropos Inbox, SFTP) or pull (Atropos Subscription, Kafka Connect, SFTP Poll).
2. I/O Gateways (Heracles, Atropos, Dia, Cronus, Kale) normalize signals to the Normalized Signal DTO.
3. Signal Exchange receives the normalized signal.
4. Trigger Evaluator matches the signal to registered triggers.
5. Matching triggers activate Scenarios; Signal Exchange creates or correlates Requests and routes to Hub Applications.

**Trigger Types for Streams**

| Gateway | Protocol | Use Case |
|---------|----------|----------|
| Heracles | HTTP/REST/MCP | Customer files dispute via API |
| Atropos | Event Bus | Transaction completed event |
| Dia | File/Batch | Batch file uploaded |
| Cronus | Exception API | Business exception requiring attention |

Configure triggers in Scenario Automation Specs. Triggers define signal_type, payload conditions, and target Scenario.

### 2.3 Cross-Workbench Context Sharing for Cross-Hub Streams

When a Stream spans multiple Hubs (e.g., credit card application across Credit Card, Payments, Servicing), use **WorkbenchContextSharingSpec** to enable cross-workbench parent-child request relationships.

**WorkbenchContextSharingSpec CRD**

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchContextSharingSpec
metadata:
  name: retail-loans-context-sharing
spec:
  workbench_ref:
    name: retail-loans-workbench
  parent_contexts:
    - type: workbench
      workbench_ref:
        name: treasury-ops-workbench
      enabled: true
  child_contexts:
    - type: workbench
      workbench_ref:
        name: customer-lifecycle-ops
      enabled: true
```

**Mutual Acknowledgment**

Both workbenches must configure sharing. Parent workbench declares child_contexts (where it can create children); child workbench declares parent_contexts (who can be its parent).

**Access Tokens**

When a cross-workbench child is created, Signal Exchange generates JWT access tokens for the child to access parent context. Tokens are scoped to specific requests and have expiration.

**Lifecycle Cascade**

When parent completes or cancels, lifecycle events cascade to children (best-effort with retry). Child requests receive PARENT_COMPLETED or PARENT_CANCELLED.

**Subscription Constraint**

Both workbenches must be in the same subscription.

### 2.4 Stream Trace: Cognitive Audit Fabric (CAF)

Stream Traces provide compliance-grade observability and decision-grade audit records. CAF is the control plane; storage is in Enterprise Memory via Memory Services.

**CAF Capabilities**

- **Decision records**: What was decided, why, with what evidence.
- **Evidence bundles**: Context at decision time for reproducibility.
- **Explanation Service**: Human-readable explanations from records.
- **Record linking**: case_id binds all records for a Request; hub_metadata links to workbench, scenario, request.

**Stream Trace Design**

Design Stream Traces as part of Stream Specification. Define what must be recorded: decisions, timelines, outcomes, exceptions. CAF record types include Decision Records, Evidence Bundles, Context Snapshots, Outcome Records, Override Records, Incident Timelines.

**Integration**

Hub Applications and agents send decision updates through Signal Exchange. Signal Exchange routes to Enterprise Memory; CAF validates structure and enforces policies. Tool invocations are recorded in CAF for full audit trail.

### 2.5 Request Hierarchy for Multi-Scenario Coordination

Streams are coordinated collections of Scenarios. Request hierarchy enables parent-child relationships for multi-Scenario coordination.

**Same-Workbench Parent-Child**

When a Hub Application invokes another Scenario (as tool or agent) within the same workbench, a child request is created. Child inherits parent context by reference. Lifecycle cascades: parent COMPLETED → children COMPLETED.

**Cross-Workbench Parent-Child**

When WorkbenchContextSharingSpec is configured, parent-child can span workbenches. Child receives ancestor_context_tokens to access parent context. Lifecycle cascade is best-effort across workbench boundaries.

**Depth Limits**

Configure maximum hierarchy depth per workbench (default: 5). Prevents unbounded nesting.

---

## 3. Loop Implementation

Loops represent the Hub's internal discipline — recurring, disciplined practices triggered internally rather than by external requests.

### 3.1 Scenario Specifications for Loop Scenarios

Loop Scenarios use the same three-spec structure. The distinction is trigger origin: internal triggers (schedule, internal events, thresholds, administrative action) activate Loop Scenarios.

**Normative Spec**

Define goals, roles, SOPs for the Loop. Focus on internal discipline: what output does the Loop produce, who consumes it?

**Automation Spec**

- **Hub Application**: Bind to the Application implementing the Loop logic.
- **Triggers**: Configure internal triggers (Kale for schedules, Atropos for internal events, threshold-based, administrative).
- **Tool bindings**: Bind tools for data access, ML pipelines, reporting.

**Deployment Spec**

- **Task queues**: For Loops involving agents, map task types to queues.
- **SLAs**: For agent-involved Loops, set completion targets.
- **Activation**: Enable/disable Loop Scenarios; control start/end dates.

### 3.2 Internal Trigger Configuration

**Schedules (Kale)**

Kale is the I/O Gateway for time-based signals. Configure cron-like schedules for periodic Loops: daily reconciliation, monthly interest accrual, weekly compliance reports.

```yaml
trigger:
  type: time_schedule
  source: kale
  schedule: "0 2 * * *"  # Daily at 2 AM
  scenario_ref: daily-reconciliation
```

**Event-Driven (Signal Exchange / Atropos)**

Loops can be triggered by internal events: batch load completes, threshold breached, Stream produces exception. Configure triggers that match internal event signals. Atropos Event Bus carries events; Signal Exchange evaluates triggers.

**Threshold-Based**

Configure triggers that fire when metrics exceed thresholds. Integrates with Olympus Watch or custom metric sources. Threshold breaches emit signals to Signal Exchange.

**Administrative Triggers**

Operators can manually trigger Loops via Workbench Studio or API. Use administrative trigger configuration for ad-hoc runs.

### 3.3 Hub Applications for Fully Automated Loops

Some Loops are fully automated — no agent involvement. The Hub Application handles all logic.

**Runtime Selection**

- **ChronoShift**: Long-running durable workflows (Temporal). Use for multi-step Loops with wait states.
- **Perseus**: Batch processing, file handling, ETL.
- **Atlantis**: Custom microservices for deterministic logic.
- **Rhea**: BPMN workflows for structured flows.

**Configuration**

Bind the Loop Scenario to a Hub Application that runs without task delegation. The Application reads data, computes, and optionally emits signals (e.g., to trigger a Stream when fraud is detected). No task queues or agent enrollment needed.

### 3.4 Loop Metrics via Hub Analytics

The Hub Analytics subsystem provides operational data for Loops.

**Metrics Available**

- Request metrics: created, completed, SLA compliance.
- Task metrics: assignment time, completion time.
- Application health: CPU, memory, error rates.
- Scenario-level analytics.

**Integration**

Hub Analytics consumes operational data from Application Data Stores and integrates with Olympus LakeStack Report Center. Supervisors and Maintainers access reports via Report Consoles (Agent Desk, Supervisor Desk, Steward Desk).

---

## 4. Channel Implementation

Channels are the collaboration surfaces through which humans and agents participate in Scenarios. Each Channel embodies identity, authentication, access control, and interaction model.

### 4.1 Persona-Channel Configuration per Workbench

Channels are persona-scoped. Configure which Channels are available for which personas per Workbench.

**Persona-Channel Matrix**

| Persona | Typical Channels |
|---------|-------------------|
| Agent | Agent Desk, MS Teams, MCP |
| Supervisor | Supervisor Desk, MS Teams, MCP |
| Process Architect | Workbench Studio |
| Developer | Workbench Studio, CLI |
| Customer | Web portal, voice, chat, MCP |
| Partner System | REST API |

Each Workbench configures its Channel set. Domain experts decide which Channels apply (e.g., Payments Hub may not need voice).

### 4.2 Channel Types Available

| Channel Type | Description | Use Case |
|--------------|-------------|----------|
| **Web Console** | Agent Desk, Supervisor Desk, Workbench Studio | Task-oriented interfaces for agents, supervisors, architects |
| **MS Teams** | Me_Bot, Ask_Bot | Conversational, in-flow collaboration |
| **MCP** | Model Context Protocol | AI-native interaction; tools, prompts, resources |
| **REST APIs** | HTTP/JSON | System-to-system, programmatic |
| **CLI** | Command-line | SRE operations, developer tooling, administrative tasks |

### 4.3 Persona Scoping and OPA Access Control

**OPA Policies**

Access control is enforced via Open Policy Agent (OPA). Policies use access token claims, scopes, and delegation-templates. Configure OPA policies per Channel and per Persona.

**Persona Scoping**

Each Persona has a defined capability scope. Agent Persona: task execution, knowledge access. Supervisor Persona: queue management, escalation, directability. Policies restrict what each Persona can do through each Channel.

### 4.4 MCP Server Configuration

**MCP Server CRD**

MCP Servers are workbench-scoped CRDs that expose Hub capabilities via the Model Context Protocol. Each MCP Server uses a template kind that implies persona and capabilities.

```yaml
apiVersion: hub.olympus.io/v1
kind: AgentTemplate  # Template kind implies persona and capabilities
metadata:
  name: dispute-mcp-server
  labels:
    hub.olympus.io/workbench: dispute-ops-prod
spec:
  scenarios:
    - standard-dispute
    - fraud-dispute
  tools:
    - transaction-lookup
  access:
    policy_ref: policies/dispute-agent-mcp.rego
```

**Template Kinds**

- `business-user-template`: Request initiation/participation.
- `agent-template`: Task processing, knowledge.
- `supervisor-template`: Queue management, SLAs, directability.
- `creator-template`: Scenario design, feedback.
- `admin-template`: Subscription management.
- `auditor-template`: Decision investigation.

**Persona-Scoped Access Surfaces**

Each MCP Server exposes a persona-specific surface. OPA policies limit access based on token claims. Multiple MCP Servers per workbench allow segregation by functional or privilege boundaries.

### 4.5 Multi-Channel Scenario Participation

A single Scenario may involve multiple Channels simultaneously. Agent on Agent Desk, customer on voice, AI co-pilot via MCP — all participate in the same work.

**Configuration**

Scenarios do not specify Channels; Channels are Workbench-level. Configure which Channels each Persona can use. When a Scenario activates, participants join through their assigned Channels. Each authenticates through their Channel; access control is scoped to Persona and Scenario context.

---

## 5. Channel Product Implementation

Channel Products are organization-scoped composite experiences that compose Channels from multiple Workbenches into cohesive persona experiences. They are delivered through the Neutrino suite.

### 5.1 Organization-Scoped Composite Experiences via Neutrino

Neutrino provides the Digital Experience Studio and Channel orchestration. Channel Products are Neutrino concerns, not Workbench concerns.

**Scope**

- **Channel**: Hub-scoped; one domain's view of collaboration.
- **Channel Product**: Organization-scoped; composite experience across domains.

### 5.2 Composing Channels from Multiple Workbenches

A customer's mobile banking app is a Channel Product. It weaves Channels from:

- Payments Hub: balance, transfers.
- Credit Card Hub: card controls, statements.
- Customer Servicing Hub: disputes, support.

The customer experiences one app; behind it are multiple Hub Channels composed into a coherent structure.

**Composition Pattern**

Neutrino composes Hub Channels via:
- API aggregation (Neutrino APIs call multiple Hub REST endpoints).
- Navigation structure that spans domains.
- Unified identity (single sign-on across Channels).

### 5.3 Navigation Structure and Interaction Paradigm per Channel Product

**Navigation Structure**

Define how users move between domain capabilities. Channel Products own the navigation; Workbenches own the capability implementation.

**Interaction Paradigm**

Match interaction paradigm to persona: task-oriented for agents, conversational for customers using chat, programmatic for partners. Channel Products orchestrate the paradigm; individual Channels provide the domain-specific interactions.

---

## 6. Integration Patterns

### 6.1 Machines: Connecting to Zeta and Third-Party Systems

Machines implement The Hub Way's **Machine** concept. The Machine Registry and Tool Registry provide the governance and discovery infrastructure for the deployed systems that supply capabilities to the Hub. Each Machine provides Tools — Prediction Applications, Decision Applications, and Commands/Actuators — that Teams invoke through Hub Applications to resolve Scenarios.

**Machines** are external systems that provide capabilities to Workbenches. They are registered in the Machine Registry and bound as tools in Scenario Automation Specs.

**Zeta Product Lines**

| Product | Role in Hub |
|---------|-------------|
| **Tachyon** | Processing — payments, cards, lifecycle |
| **Neutrino** | Digital experiences — customer interaction, channel orchestration |
| **Electron** | Lifecycle management — commercial cards, expense, benefits |

**Third-Party Systems**

Equally supported. Register Machines for core banking, fraud engines, CRM, document stores. Hub is system-agnostic; it cares how work is organized, not which systems are integrated.

**Machine Configuration**

Configure Machine instances in Workbench environment. Specify endpoint, credentials, signal emission (if Machine produces signals). Bind Machine commands as tools in Scenario Automation Specs.

### 6.2 Workbench as Machine

Expose a Workbench as a Machine for cross-Hub invocation. Other workbenches consume it as an external system.

**WorkbenchAsMachine CRD**

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchAsMachine
metadata:
  name: shared-services-machine
spec:
  workbench_ref: shared-services-prod
  exposed_tools:
    - type: scenario_tool
      ref: validation-tool
      alias: validate
  access:
    allowed_workbenches:
      - dispute-ops-prod
      - fraud-ops-prod
```

**Behavior**

- External calls only; no context inheritance by default.
- Consumer invokes tools via HTTP through Heracles Gateway.
- Authentication: bot credentials, credential forwarding, or service account.
- Authorization: provider checks allowed_workbenches and tool access.

**Use Case**

Shared validation services, common utilities, cross-domain capability reuse without cross-workbench context sharing.

### 6.3 Signal Exchange: Cross-Hub Event Propagation

**Outbound Events**

Hub Applications and Signal Exchange can publish events to Atropos. Downstream systems (other Hubs, external systems) subscribe to topics. Use for cross-Hub event propagation.

**Cross-Workbench Request Creation**

When WorkbenchContextSharingSpec is configured, Hub Applications can create child requests in other workbenches. Signal Exchange validates sharing, generates tokens, and dispatches to the target workbench's Signal Exchange. This enables cross-Hub Streams with shared context.

**Observer Pattern**

Signal Exchange dispatches Request Updates to registered observer modules (Task Management, Notification Services, MS Teams, CAF, Atropos). Observers subscribe by scope (Request, Workbench, Scenario, Tenant) and update types. Use for cross-system synchronization.

---

## Summary

Implementing The Hub Way in Olympus Hub requires:

1. **Hub configuration**: Domain model, three-spec Scenarios, agent pools (implementing Teams), Knowledge Base, Memory (ESPP taxonomy), Tenant → Subscription → Workbench hierarchy.
2. **Stream implementation**: External triggers, cross-workbench context sharing (WorkbenchContextSharingSpec), Stream Trace via CAF, request hierarchy for coordination.
3. **Loop implementation**: Internal triggers (Kale, Atropos, threshold, administrative), fully automated Hub Applications, Hub Analytics for metrics.
4. **Channel implementation**: Persona-Channel configuration, Channel types (Web Console, MS Teams, MCP, REST, CLI), OPA policies, MCP Server CRD, multi-channel participation.
5. **Channel Product**: Neutrino composition of Channels from multiple Workbenches into organization-scoped experiences.
6. **Integration**: Machines (implementing The Hub Way's Machine concept — Tachyon, Neutrino, Electron, third-party), Workbench as Machine, Signal Exchange for cross-Hub events and request creation.
