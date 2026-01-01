# Ontology: Automation Layer

**Layer Question:** *"How is it codified and scaled?"*

The Automation Layer represents the **codified definitions** of operations, and the systems that run them. Here, **automations** are the software representations of procedures, workflows, or cases. These definitions live inside an **automation system**, which is a software orchestration platform responsible for instantiating and supervising live operations.

This layer ensures consistency, scalability, and enforceability. It allows complex human–AI operations to be reliably repeated, monitored, and adapted by software systems.

---

**Navigation:** [← Execution Layer](./ontology-3-execution-layer.md) | [Ontology Reference](./ontology-reference.md) | [Diagrams →](./ontology-diagrams.md)

---

## Table of Contents

- [Automation](#automation)
- [Automation System](#automation-system)
- [Tool (abstract)](#tool-abstract)
- [Prediction Application](#prediction-application)
- [Decision Application](#decision-application)
- [Command / Actuator](#command--actuator)
- [Tool Registry](#tool-registry)
- [Machine Registry](#machine-registry)

---

## Automation
**Definition:** The **blueprint or recipe** for how an [Operation](./ontology-3-execution-layer.md#operation-abstract) should run. It is the codified definition (in software) that can be instantiated multiple times by the [Automation System](#automation-system).  
**Role:** Source of truth for executable behavior; defines the steps, decision points, and rules.  
**Relationships:** Invoked by [Scenarios](./ontology-1-perception-layer.md#scenario); instantiates [Operations](./ontology-3-execution-layer.md#operation-abstract); managed by the [Automation System](#automation-system).

**Analogy:** If an [Operation](./ontology-3-execution-layer.md#operation-abstract) is a meal being cooked, the Automation is the recipe. Many meals (operation instances) can be cooked from the same recipe (automation).

**Automation Formats:**

| Format | Best For | Banking Example |
|--------|----------|-----------------|
| **BPMN** | Structured workflows with clear sequences | Loan origination workflow |
| **CMMN** | Flexible case management | Fraud investigation case |
| **DMN** | Decision logic and rules | Credit approval decision table |
| **Code/DSL** | Complex or custom logic | Real-time fraud scoring procedure |

**Automation Components:**

```
Automation Definition
├── Entry Criteria (when can it start?)
├── Activities & Tasks (what work is done?)
├── Decision Points (what choices are made?)
├── Transitions (how does work flow?)
├── Roles Required (who participates?)
├── SLAs & Escalations (what are the time bounds?)
└── Exit Criteria (when is it complete?)
```

**Banking Examples:**
- **Dispute Resolution Automation:** Defines steps from intake → investigation → resolution → notification
- **Account Opening Automation:** Defines KYC checks → credit checks → account creation → welcome
- **Wire Transfer Automation:** Defines validation → AML screening → approval → execution

**See also:** [Operation](./ontology-3-execution-layer.md#operation-abstract), [Automation System](#automation-system), [SOP](./ontology-2-normative-layer.md#sop-standard-operating-procedure)

---

## Automation System
**Definition:** The **execution platform** where [Automations](#automation) are run. It is the software orchestration system that instantiates, monitors, and supervises live [Operations](./ontology-3-execution-layer.md#operation-abstract).  
**Role:** Hosts automations; handles instantiation, monitoring, escalation, and lifecycle management.  
**Relationships:** Receives [Signals](./ontology-1-perception-layer.md#signal) from the [Environment](./ontology-1-perception-layer.md#environment); supervises [Operations](./ontology-3-execution-layer.md#operation-abstract); runs/manages [Automations](#automation).

**Analogy:** If [Automation](#automation) is the recipe, the Automation System is the **kitchen**—the place with chefs (agents), equipment (tools), and the coordination to prepare meals (operations).

**Automation System Responsibilities:**

| Responsibility | Description |
|----------------|-------------|
| **Instantiation** | Create new [Operations](./ontology-3-execution-layer.md#operation-abstract) when [Scenarios](./ontology-1-perception-layer.md#scenario) are triggered |
| **Orchestration** | Coordinate work across [Agents](./ontology-3-execution-layer.md#agent) and [Tools](#tool-abstract) |
| **State Management** | Track operation progress, activity status, and data |
| **Task Assignment** | Route [Tasks](./ontology-3-execution-layer.md#task) to appropriate [Agents](./ontology-3-execution-layer.md#agent) via [Task Queues](./ontology-3-execution-layer.md#task-queue) |
| **SLA Monitoring** | Track time-based thresholds and trigger [Escalations](./ontology-3-execution-layer.md#escalation) |
| **Audit & Compliance** | Log all actions for regulatory and audit purposes |

**Examples of Automation Systems:**

| System | Type | Typical Use |
|--------|------|-------------|
| **Camunda** | BPMN/DMN Engine | Structured workflows |
| **Temporal** | Workflow Orchestration | Durable, long-running workflows |
| **Pega** | Low-Code Platform | Case management |
| **ServiceNow** | ITSM/Workflow | IT and enterprise operations |
| **Olympus Hub** | Operations Platform | Human-AI collaborative operations |

**Banking Example:**
When a "Dispute Filing Request" arrives:
1. Automation System receives the [Request](./ontology-1-perception-layer.md#request)
2. Instantiates the "Dispute Resolution" [Operation](./ontology-3-execution-layer.md#operation-abstract)
3. Creates [Tasks](./ontology-3-execution-layer.md#task) and assigns to [Task Queues](./ontology-3-execution-layer.md#task-queue)
4. Monitors SLAs and triggers [Escalations](./ontology-3-execution-layer.md#escalation) if needed
5. Tracks operation to completion

**See also:** [Scenario](./ontology-1-perception-layer.md#scenario), [Automation](#automation), [Operation](./ontology-3-execution-layer.md#operation-abstract)

---

## Tool (abstract)
**Definition:** Capabilities available to [Agents](./ontology-3-execution-layer.md#agent) that aid the OPD cycle: **Observe/Predict**, **Decide**, and **Act**.  
**Specializations:**  
- [Prediction Application](#prediction-application) — aids Observe/Predict  
- [Decision Application](#decision-application) — aids Decide  
- [Command / Actuator](#command--actuator) — aids Act  

**Relationships:** Used by [Agents](./ontology-3-execution-layer.md#agent); exposed by [Machines](./ontology-1-perception-layer.md#machine) (in the case of Commands).  
**Example:** Fraud scoring model (Prediction), decision dashboard (Decision), `lockAccount` API (Command).

**See also:** [Agent](./ontology-3-execution-layer.md#agent), [OPD Elements](./ontology-1-perception-layer.md#opd-elements-observe-predict-decide), [Machine](./ontology-1-perception-layer.md#machine)

---

## Prediction Application
**Definition:** A [Tool](#tool-abstract) that aids **Predict** (e.g., ML/analytics).  
**Role:** Provides forecasts/scores to inform [Decisions](./ontology-2-normative-layer.md#decision).  
**Example:** Model returning probability of fraud.

**See also:** [Tool](#tool-abstract), [Predict](./ontology-1-perception-layer.md#opd-elements-observe-predict-decide)

---

## Decision Application
**Definition:** A [Tool](#tool-abstract) that aids **Decide** (e.g., rule engines, DSS).  
**Role:** Supports or automates choice among actions.  
**Example:** Policy decision point evaluating access rules.

**See also:** [Decision](./ontology-2-normative-layer.md#decision), [Tool](#tool-abstract)

---

## Command / Actuator
**Definition:** An invocable capability exposed by a [Machine](./ontology-1-perception-layer.md#machine) that [Agents](./ontology-3-execution-layer.md#agent) can execute to effect change in the [Environment](./ontology-1-perception-layer.md#environment).  
**Also known as:** "Levers" in systems operations context; "Actuators" in robotics/AI agent terminology.  
**Role:** The interface between Agents and Machines; enables Agents to **Act** on the Environment. Commands are a specialization of [Tool](#tool-abstract).  
**Relationships:**  
- Exposed by [Machines](./ontology-1-perception-layer.md#machine)  
- Executed as [Actions](./ontology-3-execution-layer.md#action) by [Agents](./ontology-3-execution-layer.md#agent)  
- Registered in [Tool Registry](#tool-registry) (Commands are a type of Tool)  
- Used by both [Human](./ontology-3-execution-layer.md#human) and [AI Agent](./ontology-3-execution-layer.md#ai-agent)  

**Example:** `lockAccount`, `approveTransaction`, `restartService`, `updateFirewallRule`, `moveRobotArm`.

**See also:** [Tool](#tool-abstract), [Machine](./ontology-1-perception-layer.md#machine), [Actions](./ontology-3-execution-layer.md#action), [Agent](./ontology-3-execution-layer.md#agent), [Environment](./ontology-1-perception-layer.md#environment)

---

## Tool Registry
**Definition:** A catalog of [Tools](#tool-abstract) available for use by [Agents](./ontology-3-execution-layer.md#agent) in [Operations](./ontology-3-execution-layer.md#operation-abstract).  
**Role:** Central registry that enables Tool discovery, access control, and usage tracking.  
**Relationships:**  
- Contains [Tools](#tool-abstract) (Prediction Applications, Decision Applications, Commands/Actuators)  
- Referenced by [Workbenches](./ontology-1-perception-layer.md#workbench) (Tools are whitelisted per Workbench)  
- Used by [Agents](./ontology-3-execution-layer.md#agent) during [Operations](./ontology-3-execution-layer.md#operation-abstract)  

**Registry Levels:**

| Level | Scope | Managed By | Content |
|-------|-------|------------|---------|
| **System Registry** | Platform-wide | Platform Operators | Common Tools available to all tenants |
| **Tenant Registry** | Tenant-specific | Tenant Admins | Tenant-developed or licensed Tools |

**Inheritance Model:**
```
System Tool Registry (Platform-wide)
        │
        ▼
Tenant Tool Registry (Inherits, Extends, Overrides)
        │
        ▼
Workbench Tool Whitelist (Subset available in this Workbench)
```

**Tool Registration:**
- Tools are registered with metadata: name, version, capabilities, input/output schemas
- Tools can be versioned and deprecated
- Usage tracking for audit and analytics

**Example:** A "Fraud Detection Tool" is registered in the System Registry. Tenant inherits it, then whitelists it in the "Dispute Workbench" for use by Dispute Analysts.

**See also:** [Tool](#tool-abstract), [Workbench](./ontology-1-perception-layer.md#workbench), [Machine Registry](#machine-registry)

---

## Machine Registry
**Definition:** A catalog of [Machines](./ontology-1-perception-layer.md#machine) accessible within the [Environment](./ontology-1-perception-layer.md#environment) for a given scope.  
**Role:** Central registry for Machine discovery, credential management, and access control.  
**Relationships:**  
- Contains [Machines](./ontology-1-perception-layer.md#machine) and their exposed [Commands](#command--actuator)  
- Referenced by [Workbenches](./ontology-1-perception-layer.md#workbench) (Machines are made accessible per Workbench)  
- Accessed by [Agents](./ontology-3-execution-layer.md#agent) during [Operations](./ontology-3-execution-layer.md#operation-abstract)  

**Registry Levels:**

| Level | Scope | Managed By | Content |
|-------|-------|------------|---------|
| **System Registry** | Platform-wide | Platform Operators | Common infrastructure Machines |
| **Tenant Registry** | Tenant-specific | Tenant Admins | Tenant's enterprise systems |

**Inheritance Model:**
```
System Machine Registry (Platform infrastructure)
        │
        ▼
Tenant Machine Registry (Inherits, Extends, Overrides)
        │
        ▼
Workbench Machine Access (Subset accessible in this Workbench)
```

**Machine Registration:**
- Machines are registered with: endpoints, authentication, exposed Commands
- Command schemas (inputs, outputs) are discoverable
- Connectivity and health status tracked

**Example:** "Core Banking System" is registered in the Tenant Machine Registry with its exposed Commands (getAccountBalance, lockAccount, etc.). The "Dispute Workbench" is configured to access this Machine.

**See also:** [Machine](./ontology-1-perception-layer.md#machine), [Command / Actuator](#command--actuator), [Tool Registry](#tool-registry), [Workbench](./ontology-1-perception-layer.md#workbench)

---

**Navigation:** [← Execution Layer](./ontology-3-execution-layer.md) | [Ontology Reference](./ontology-reference.md) | [Diagrams →](./ontology-diagrams.md)

