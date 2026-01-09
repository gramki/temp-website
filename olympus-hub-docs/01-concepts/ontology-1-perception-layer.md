# Ontology: Perception Layer

**Layer Question:** *"What's happening?"*

The Perception Layer is concerned with **observing and interpreting reality**. It captures how the **environment** and its components—machines, sensors, data feeds—generate **signals**. These signals are then interpreted by **triggers** into meaningful **scenarios** that Human–AI teams must respond to.

It is descriptive, not prescriptive: this layer does not say what should be done, only what *is happening*. It is the sensory nervous system of the ontology.

---

**Navigation:** [← Ontology Reference](./ontology-reference.md) | [Normative Layer →](./ontology-2-normative-layer.md)

---

## Table of Contents

- [Domain](#domain)
- [Workbench](#workbench)
- [Business Entity](#business-entity)
- [Environment](#environment)
- [Machine](#machine)
- [Sensors](#sensors)
- [Signal](#signal)
- [Request](#request)
- [Trigger](#trigger)
- [Scenario](#scenario)
- [OPD Elements](#opd-elements-observe-predict-decide)

---

## Domain
**Definition:** Conceptual scope of business operations (e.g., dispute resolution, reconciliation, KYC, fraud detection).  
**Role:** Frames typical [Scenarios](#scenario) and [Goals](./ontology-2-normative-layer.md#goal); contains [Business Entities](#business-entity).  
**Relationships:** Interacts with the [Environment](#environment); contains [Business Entities](#business-entity); **interpreted through a [Workbench](#workbench)**.

**Important:** Domain is a conceptual/notional construct—it is never directly modeled or instantiated in the framework. A Domain is **interpreted through a Workbench**, which is the operational realization of that domain.

**Example:** The "Dispute Resolution" domain is interpreted through a "Dispute Workbench" that defines how disputes are handled.

**See also:** [Workbench](#workbench), [Business Entity](#business-entity), [Environment](#environment), [Scenario](#scenario)

---

## Workbench
**Definition:** A logical unit encapsulating everything required to operate a business [Domain](#domain).  
**Role:** The operational realization of a Domain; the container for all domain-specific configuration, definitions, and runtime entities.  

**Relationships:**
- **Interprets** a [Domain](#domain) (1:1 notional mapping)
- **Contains** [Scenarios](#scenario) (one Workbench can have many Scenarios)
- **Contains** [Triggers](#trigger), [Signals](#signal), [Requests](#request), [Operations](./ontology-3-execution-layer.md#operation-abstract)
- **References** [Business Entities](#business-entity) relevant to the domain
- **References** [Environment](#environment) (Machines, Sensors in scope)
- **Has** [Tool Registry](./ontology-4-automation-layer.md#tool-registry) (whitelisted Tools)
- **Has** [Machine Registry](./ontology-4-automation-layer.md#machine-registry) (accessible Machines)
- **Has** [Task Queues](./ontology-3-execution-layer.md#task-queue) (for work distribution)
- **Has** enrolled [Agents](./ontology-3-execution-layer.md#agent) (Human and AI)
- **Has** [Knowledge Base](./ontology-2-normative-layer.md#knowledge-base-kb) (SOPs, policies, Runbooks)

**Workbench Contents:**

| Category | What It Contains |
|----------|------------------|
| **Domain Model** | Business Entities, lifecycle states, validation rules |
| **Environment** | Machines, Sensors in scope for this Workbench |
| **Scenarios** | Operational requirements (why, when, how) |
| **Triggers** | Signal → Request bindings |
| **Request Definitions** | Domain-specific Request types |
| **Tool Registry** | Whitelisted Tools (from System/Tenant registry) |
| **Machine Registry** | Accessible Machines (from System/Tenant registry) |
| **Task Queues** | Queues for work distribution by Role/Group |
| **Agents** | Enrolled Human and AI agents |
| **Knowledge Base** | SOPs, policies, Runbooks, Checklists |

**Workbench Lifecycle:**

| Stage | Description |
|-------|-------------|
| **Define** | Tenant creates Workbench definition (from Blueprint or empty) |
| **Configure** | Tenant configures Triggers, Scenarios, Task Queues, etc. |
| **Enroll** | Agents are enrolled to operate in this Workbench |
| **Operate** | Operations run within this Workbench |
| **Evolve** | Tenant continuously evolves the Workbench definition |

**Scoping:**
All of the following are **always scoped to exactly one Workbench**:
- Signals
- Triggers  
- Requests
- Scenarios
- Operations

**Workbench Blueprints:**
A Workbench can be created:
- **From a Blueprint**: System-level template that provides pre-configured patterns
- **From empty**: Start with no pre-configuration

```
Workbench Blueprint (System-level)
  └── instantiated as → Workbench Definition (Tenant-level)
       └── customized with tenant-specific config
```

**Example:** "Dispute Workbench" encapsulates everything for handling disputes—scenarios for fraud disputes, billing disputes, ATM disputes; enrolled analysts; registered investigation tools; task queues for dispute analysts.

**See also:** [Domain](#domain), [Scenario](#scenario), [Tool Registry](./ontology-4-automation-layer.md#tool-registry), [Machine Registry](./ontology-4-automation-layer.md#machine-registry), [Task Queue](./ontology-3-execution-layer.md#task-queue)

---

## Business Entity
**Definition:** A fundamental object within a [Domain](#domain) that represents a real-world concept of business significance. Business Entities are **what [Operations](./ontology-3-execution-layer.md#operation-abstract) act upon**.  
**Role:** The subject matter of operations; entities have state, lifecycle, and relationships that operations manage.  
**Relationships:**  
- Exist within a [Domain](#domain)  
- Managed by [Machines](#machine) (applications/systems)  
- Acted upon by [Operations](./ontology-3-execution-layer.md#operation-abstract)  
- Referenced in [Signals](#signal) (entity state changes trigger signals)  
- Subject to business rules and validation  

**Characteristics:**

| Aspect | Description |
|--------|-------------|
| **Identity** | Unique identifier within the domain |
| **State** | Current values of properties; may have lifecycle states (draft → active → closed) |
| **Lifecycle** | Creation, updates, state transitions, archival |
| **Relationships** | Links to other Business Entities (Customer → Orders → Payments) |

**Examples by Domain:**

| Domain | Business Entities |
|--------|-------------------|
| **E-commerce** | Customer, Order, Product, Payment, Shipment |
| **Banking** | Account, Transaction, Customer, Card, Loan |
| **HR** | Employee, Position, Department, Leave Request |
| **IT Operations** | Incident, Change Request, Configuration Item, Service |

**See also:** [Domain](#domain), [Machine](#machine), [Operation](./ontology-3-execution-layer.md#operation-abstract), [Signal](#signal)

---

## Environment
**Definition:** The *real* operational setting of an enterprise, including:
- Endpoints (HTTP/TCP) where systems are deployed.
- Access mechanisms (tokens, secrets).
- Event buses/topics to publish/subscribe.
- File drops / object stores for batch I/O.

**Role:** Hosts real I/O and produces [Signals](#signal).  
**Relationships:** Produces [Signals](#signal); contains [Machines](#machine) and [Sensors](#sensors); interacts with the [Automation Runtime](./ontology-4-automation-layer.md#automation-system).  
**Example:** Kafka topics for transactions, OAuth-secured APIs, S3 buckets for statement files.

**See also:** [Signal](#signal), [Automation Runtime](./ontology-4-automation-layer.md#automation-system)

---

## Machine
**Definition:** Deployed compute systems (apps, services, devices) within the [Environment](#environment). 

When the domain is about a functional business like Order Management, Inventory Management, then machines are the software applications that an enterprise uses to manage these functions. These are usually the Line-of-Business systems or the Core Systems (as in Banking). The signals of interest from these applications relate to changes in the functional domain.

When the domain is about technical operations of systems, then the Machine is the system being managed. The Sensors and signals of relevance differ between the functional and technical operations, while the machine in reference may still be the same.

**Role:** Emit or transform [Signals](#signal). Expose [Commands](./ontology-4-automation-layer.md#command--actuator) that can be invoked by [Agents](./ontology-3-execution-layer.md#agent).  
**Relationships:** May host [Sensors](#sensors); produces [Signals](#signal); exposes [Commands](./ontology-4-automation-layer.md#command--actuator).  
**Example:** A payment switch microservice emitting authorization events and exposing commands like `authorizeTransaction`, `reversePayment`.

**See also:** [Sensors](#sensors), [Signal](#signal), [Command / Actuator](./ontology-4-automation-layer.md#command--actuator)

---

## Sensors
**Definition:** Any mechanism that monitors the operational environment and reports what it observes. Sensors detect changes, anomalies, or events and convert them into [Signals](#signal).  
**Role:** Materialize "Observe" in OPD—the eyes and ears of the operational system.  
**Relationships:** Produce [Signals](#signal); may be embedded in [Machines](#machine) or deployed independently.

**Types of Sensors:**

| Category | Description | Banking Examples |
|----------|-------------|------------------|
| **Transaction Monitors** | Watch financial flows in real-time | Payment velocity monitors, Large transaction alerts |
| **Behavioral Analytics** | Detect unusual patterns | Login anomaly detection, Spending pattern analysis |
| **Compliance Monitors** | Ensure regulatory adherence | AML transaction screening, OFAC watchlist matching |
| **System Health** | Monitor technical infrastructure | Core banking uptime, API latency monitors |
| **Document Sensors** | Detect document arrivals/changes | Statement file arrival, KYC document upload |

**Examples (Banking):**
- **Fraud Tap:** Monitors card transactions and emits signals when spending patterns deviate from customer norms
- **AML Scanner:** Watches wire transfers and emits signals when beneficiary matches watchlist entries
- **Reconciliation Monitor:** Detects when account balances don't match between systems

**Examples (Technical):**
- **CPU/Memory Probe:** Publishes resource utilization metrics
- **Log Aggregator:** Detects error patterns in application logs

**See also:** [Signal](#signal), [OPD Elements](#opd-elements-observe-predict-decide), [Machine](#machine)

---

## Signal
**Definition:** Atomic observation/event (telemetry, log, message, file arrival).  
**Role:** Starts the runtime flow; sensed by I/O Gateways in the [Environment](#environment).  
**Relationships:** Produced by [Environment](#environment)/[Machine](#machine)/[Sensors](#sensors); fed into a [Trigger](#trigger).  

**Core Signal Types:**

| Type | Description | Example |
|------|-------------|---------|
| **Event** | State change published by [Machines](#machine) | Order placed, Payment completed |
| **Observation** | Information of interest, not yet a problem | High transaction volume, Unusual pattern |
| **Exception** | Error or failure requiring attention | Transaction failed, API timeout |
| **Request** | Explicit ask for operational attention | Password reset, Dispute filing (see [Request](#request)) |

### I/O Gateway Signal Types

Each I/O Gateway senses signals from specific protocols. These signal types are **extensible**—new I/O Gateways may introduce new signal types as the platform grows.

| I/O Gateway | Signal Type | Protocol Origin | Description |
|-------------|-------------|-----------------|-------------|
| **Atropos** | Event | Pub-Sub Event Bus | State changes from [Machines](#machine); Topics, Subscriptions |
| **Cronus** | Exception | Publisher API | Business-level errors requiring operational attention |
| **Cronus** | Observation | Publisher API | Business-level information of interest |
| **Heracles** | HTTP-Request | HTTP/REST/MCP | API calls from users, applications, or agents |
| **Dia** | Batch-Request | SFTP/HTTP/WebDAV | File arrivals containing batch data |
| **Kale** | Time-Signal | Scheduler | Scheduled triggers at defined intervals |

**Extensibility:** As new I/O Gateways are added (e.g., for new protocols like GraphQL, gRPC, WebSocket), new signal types can be introduced. The core ontology (Signal → Trigger → Request → Scenario → Operation) remains stable.

**Note:** All signals (except Request) flow through [Triggers](#trigger) which transform them into [Requests](#request). Requests have special behavior—see below.

**See also:** [Request](#request), [Trigger](#trigger), [Observe](#opd-elements-observe-predict-decide)

---

## Request
**Definition:** A [Signal](#signal) that explicitly asks for operational attention, always activating a [Scenario](#scenario) via an implicit [Trigger](#trigger).  
**Role:** The standardized input to [Operations](./ontology-3-execution-layer.md#operation-abstract); [Triggers](#trigger) bind protocol-specific signals to Requests, making Operations channel-agnostic.  

**Request Types (Framework-Level Classification):**

The framework classifies Requests into three types based on **the nature of the work** and **subject requirements**. This classification affects agent enablement, authorization models, and task assignment patterns.

> **Important:** The originator does NOT define the request type. Systems can originate any request type. Employees can originate Service Requests (assisted) or Business Requests. Only customers can self-serve (Service Requests only).

| Type | Nature | Subject | Self-Serve by Customer? |
|------|--------|---------|-------------------------|
| **Service Request** | Customer-facing work | **Required** — always a customer | ✅ Yes (only type) |
| **Business Request** | Business operations | **Optional** — may be customer | ❌ No |
| **System Request** | System/data integrity issues requiring **business resolution** | **Optional** — often an entity | ❌ No |

**Who Can Originate:**

| Request Type | Customer | Employee | System |
|--------------|:--------:|:--------:|:------:|
| **Service Request** | ✅ (self-serve) | ✅ (assisted) | ✅ |
| **Business Request** | ❌ | ✅ | ✅ |
| **System Request** | ❌ | ❌ | ✅ |

### Service Requests
A Service Request always has a **subject** identified as a customer of the business. The request represents customer-facing work.

**Origination modes:**
- **Self-service**: The customer initiates directly (portals, mobile apps, IVR)
- **Assisted**: An [Agent](./ontology-3-execution-layer.md#agent) initiates on behalf of the customer (contact center, branch)
- **System-initiated**: A system initiates on behalf of the customer (automated customer notification, API submission)

**Key Characteristics:**
- Always associated with an identified **subject** (the customer)
- **Only request type that allows customer self-serve**
- **Initiation authorization**:
  - Self-service: Identity-based (the customer themselves)
  - Assisted: Role-based (contact center agent, branch staff acting on behalf of customer)
  - System: Machine identity (application credentials, API keys)
- [Tasks](./ontology-3-execution-layer.md#task) within the [Operation](./ontology-3-execution-layer.md#operation-abstract) can be assigned to:
  - The subject (customer) themselves—enabled as a special participant type
  - [Agents](./ontology-3-execution-layer.md#agent) of the business/organization—based on roles or identity
- Framework treats customer participants as a **special agent type**—they must be enabled differently

**Example (Self-service):** A customer (subject) files a "Dispute Filing Request" via mobile app. During investigation:
- The customer is assigned a Task to upload supporting documents
- A Dispute Analyst (agent) is assigned a Task to review transaction history

**Example (Assisted):** A contact center agent files a "Dispute Filing Request" on behalf of a customer who called in. The customer remains the subject, but the agent initiated the request.

**Example (System-initiated):** A mobile banking API receives a dispute submission from the customer app and creates the Service Request. The customer is the subject.

### Business Requests
Internal business operations work. Can be initiated by employees or systems acting on business judgment.

**Origination modes:**
- **Employee-initiated**: Operations teams, back-office staff, managers
- **System-initiated**: Automated business operations (scheduled reviews, triggered workflows)

**Key Characteristics:**
- Does **not** enforce association with an external subject (customer), though optional
- Subject may be a customer, but this is a Business Request if the work is internal operations rather than customer-facing service
- Authorization modeled by [Roles](./ontology-2-normative-layer.md#role) and groups rather than just named individuals
- Participants are enrolled [Agents](./ontology-3-execution-layer.md#agent) (Human or AI) within the organization
- **Cannot be self-served by customers**

**Example (Employee):** A reconciliation analyst initiates a "Manual Adjustment Request" to correct a settlement discrepancy. No customer subject is required, though the request may optionally reference affected accounts.

**Example (System):** An automated compliance system triggers a "Periodic Account Review Request" based on scheduled checks. May reference customer accounts as subjects.

### System Requests
System-detected issues related to **data integrity, reconciliation, or consistency** that require **business domain resolution**—not technical/SRE resolution.

> **Important:** System Requests are NOT technical incidents. They are issues that systems detect but cannot auto-resolve, requiring business domain agents to make decisions and take action.

**Key Characteristics:**
- **Only originated by systems** (not customers or employees)
- Does **not** enforce association with an external subject (customer), though optional
- Subject is often a business entity (transaction, account, record) rather than a person
- Represents issues that:
  - Cannot be resolved by SRE/technical operations alone
  - Require business judgment to determine correct action
  - Involve data reconciliation, integrity, or consistency problems
- Authorization via machine identity mechanisms (application credentials, API keys, certificates)
- **Cannot be self-served by customers**

**Examples:**
- **Reconciliation failure**: Core banking and card network balances don't match—business agent must determine which is authoritative
- **Data integrity violation**: Conflicting records detected—business agent must decide resolution
- **Consistency error**: Out-of-order updates caused state corruption—business agent must review and correct
- **Failed validation**: Batch processor creates a "Failed Record Review Request" for records that failed business rules

---

**Key Characteristics (All Request Types):**
- **Implicit Trigger**: Requests always activate their target [Scenario](#scenario)—no explicit Trigger definition needed for Request→Scenario binding
- **Channel Agnostic**: A Request looks the same to [Operations](./ontology-3-execution-layer.md#operation-abstract) regardless of origin channel
- **Bound by Triggers**: [Triggers](#trigger) transform Events, Observations, Exceptions, and protocol messages into Requests

**Relationships:**  
- Is a type of [Signal](#signal)  
- Created by [Triggers](#trigger) from other Signals or protocol messages  
- Activates [Scenarios](#scenario) (implicit trigger behavior)  
- Acted upon by [Operations](./ontology-3-execution-layer.md#operation-abstract)  
- References [Business Entities](#business-entity)  
- May assign [Tasks](./ontology-3-execution-layer.md#task) to requestors (especially Service Requests)

**Domain-Specific Request Types:**  
Beyond this framework classification, each [Workbench](#workbench) defines its own **domain-specific request types** that are idiomatic to that domain (e.g., "Dispute Filing Request," "Clearance Exception Request," "Account Closure Request"). These are configured in the Workbench definition.

**See also:** [Signal](#signal), [Trigger](#trigger), [Scenario](#scenario), [Operation](./ontology-3-execution-layer.md#operation-abstract), [Task](./ontology-3-execution-layer.md#task)

---

## Trigger
**Definition:** A binder that transforms [Signals](#signal) and protocol messages into [Requests](#request), making [Operations](./ontology-3-execution-layer.md#operation-abstract) channel-agnostic.  
**Role:** The critical binding mechanism between I/O and Operations; executed by I/O Gateways ([Machines](#machine) in the [Environment](#environment)).  

**Trigger Responsibilities:**

| Responsibility | Description |
|----------------|-------------|
| **Filter** | Determine which incoming [Signals](#signal) should proceed |
| **Transform** | Convert protocol-specific format to/from [Request](#request)/Response |
| **Access** | Enforce authorization rules at I/O boundary |
| **Bind** | Map protocol message → [Request](#request) (input) and Response → protocol message (output) |

**Relationships:**  
- Receives [Signals](#signal) (Events, Observations, Exceptions) and protocol messages  
- Creates [Requests](#request) in standardized format  
- Defined in operational configurations (e.g., Workbench definitions)  
- Executed by I/O Gateways ([Machines](#machine))  

**Example:** On "5 failed logins" (Event), create "Suspicious Login Investigation" (Request).

**See also:** [Signal](#signal), [Request](#request), [Scenario](#scenario)

---

## Scenario
**Definition:** A situational context activated by a [Trigger](#trigger).  
**Role:** Determines which [Roles](./ontology-2-normative-layer.md#role) are involved and which [Automations](./ontology-4-automation-layer.md#automation) should be invoked.  
**Relationships:** Activated by [Trigger](#trigger); involves [Roles](./ontology-2-normative-layer.md#role); references their [Goals](./ontology-2-normative-layer.md#goal); invokes an [Automation](./ontology-4-automation-layer.md#automation).  
**Example:** "Unauthorized device login" involving Security Analyst, SRE, and an AI monitor.

**See also:** [Automation](./ontology-4-automation-layer.md#automation), [Role](./ontology-2-normative-layer.md#role)

---

## OPD Elements (Observe, Predict, Decide)

The OPD cycle is the fundamental cognitive loop that drives operational decision-making. Every operational response—whether by humans or AI—follows this pattern.

**Observe:** The act of sensing and capturing what is happening in the operational environment. Observations become [Signals](#signal) that can trigger operational responses.  
- **Banking Example:** Monitoring real-time transactions and detecting a $50,000 wire transfer to a new beneficiary in a high-risk country.

**Predict:** Using knowledge ([SOPs](./ontology-2-normative-layer.md#sop-standard-operating-procedure)) and analytical tools ([Prediction Applications](./ontology-4-automation-layer.md#prediction-application)) to anticipate outcomes, assess risk, or forecast what might happen next.  
- **Banking Example:** A fraud scoring model predicts 87% probability this transaction is fraudulent based on pattern analysis.

**Decide:** The act of choosing a course of action, performed by an [Agent](./ontology-3-execution-layer.md#agent), often aided by decision-support [Tools](./ontology-4-automation-layer.md#decision-application). Decisions produce a [Decision](./ontology-2-normative-layer.md#decision) outcome that drives subsequent [Actions](./ontology-3-execution-layer.md#action).  
- **Banking Example:** The fraud analyst decides to hold the transaction for manual review rather than auto-approve or auto-decline.

**The OPD Cycle in Practice:**

```
OBSERVE                    PREDICT                     DECIDE
   │                          │                           │
   ▼                          ▼                           ▼
What happened?          What might happen?         What should we do?
   │                          │                           │
   ▼                          ▼                           ▼
[Signals]              [Prediction Apps]          [Decision Apps]
                       [SOPs/Knowledge]           [Agent Judgment]
```

**See also:** [Decision](./ontology-2-normative-layer.md#decision), [Tool](./ontology-4-automation-layer.md#tool-abstract), [SOP](./ontology-2-normative-layer.md#sop-standard-operating-procedure)

---

**Navigation:** [← Ontology Reference](./ontology-reference.md) | [Normative Layer →](./ontology-2-normative-layer.md)

