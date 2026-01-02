# Agent-Oriented System (AOS): Definition, Structure, and Design Process

> **Reference Document**  
> **Audience:** Enterprise Architects, AI Engineers, Product Managers  
> **Last Updated:** January 2026

### Related Documents

- **[Raw, Trained, Employed](./raw-trained-employed.md)** — Zeta's terminology framework built on AOSM
- **[Book Summary: AOSM](./book-ref/book-summary.md)** — Comprehensive summary of the AOSM book

---

## Overview

This document defines what an **Agent-Oriented System (AOS)** is, describes its structural components using the **Agent-Oriented Systems Modeling (AOSM)** meta-model, and outlines the process for designing one.

The concepts here are grounded in the AOSM framework as described in:

> Sterling, L., & Taveter, K. (2009). *The Art of Agent-Oriented Modeling*  
> Stevenson et al. (2023). Four Components of Autonomy  
> *Integrating Artificial and Human Intelligence through Agent-Oriented Systems Design* (Systems Innovation Book Series, CRC Press)

---

## 1. Definition: What Is an Agent-Oriented System?

### 1.1 Formal Definition

> An **Agent-Oriented System (AOS)** is the holistic sum of interdependent agents (human and/or AI) that interact within an environment to achieve a specific purpose or goal, where each agent senses, interprets, decides, and acts in pursuit of those goals.

### 1.2 Key Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Holistic** | The system is more than the sum of its parts—emergent properties arise from agent interactions |
| **Interdependent** | Agents depend on each other; the system cannot achieve its purpose if any interdependent part is missing |
| **Goal-directed** | The system exists to achieve specific outcomes defined in a Goal hierarchy |
| **Agent-centric** | The fundamental units of design are agents, not functions or modules |
| **Purposeful** | Every agent fulfills Responsibilities in service of Goals |

### 1.3 Foundational Definitions

**System**
> The holistic sum of interdependent parts that interact to achieve a specific purpose or goal.
> — AOSM Meta-Model

**Agent**
> An entity that perceives its environment and acts upon that environment in pursuit of goals.
> — AOSM Meta-Model

Agents are a generalization—both Humans and AI Agents are types of Agent. This allows unified modeling of human-AI collaboration.

**AI Agent**
> A goal-seeking software/hardware entity designed to exhibit "controlled autonomy"—acting autonomously only to the extent that it is beneficial to the physical entity (e.g., human) who is responsible for controlling it.
> — AOSM Meta-Model

**Human-AI Team (HAT)**
> A team comprising two or more Agents (humans and/or AI agents) that work interdependently to achieve system goals.
> — AOSM Meta-Model

---

## 2. Structure: The AOSM Meta-Model

The AOSM meta-model defines the **ontology** of an Agent-Oriented System—what concepts exist and how they relate.

### 2.1 System Context

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              ENVIRONMENT                                     │
│            (Machines, sensors, tools, actuators the HAT interacts with)      │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                              DOMAIN                                    │  │
│  │               (Part of environment the system operates in)             │  │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │  │
│  │  │                            SYSTEM                                │  │  │
│  │  │         (Holistic sum of interdependent parts)                   │  │  │
│  │  │                                                                  │  │  │
│  │  │   ┌────────────────┐        ┌─────────────────────────────────┐ │  │  │
│  │  │   │   Machine(s)   │        │       Human-AI Team (HAT)       │ │  │  │
│  │  │   │   (0 or more)  │◄──────►│                                 │ │  │  │
│  │  │   └────────────────┘        │  ┌─────────┐    ┌───────────┐   │ │  │  │
│  │  │                             │  │  Human  │◄──►│  AI Agent │   │ │  │  │
│  │  │                             │  │  Agent  │    │           │   │ │  │  │
│  │  │                             │  └────┬────┘    └─────┬─────┘   │ │  │  │
│  │  │                             │       │     OPD      │         │ │  │  │
│  │  │                             │       └──────────────┘         │ │  │  │
│  │  │                             │        (2 or more agents)      │ │  │  │
│  │  │                             └─────────────────────────────────┘ │  │  │
│  │  └─────────────────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

> **Note on "Environment"**: In AOSM, Environment refers to the **operational context**—the machines, sensors, tools, APIs, databases, and actuators that the HAT perceives and acts upon. This is distinct from "deployment stage" (dev/staging/production), which is a software lifecycle concept.

### 2.2 Structural Elements

| Element | Definition | Cardinality |
|---------|------------|-------------|
| **Environment** | The operational context—machines, sensors, tools, APIs, actuators that the HAT perceives and acts upon. Represented concretely as connection strings, endpoints, and credentials. | 1 |
| **Domain** | The part of the environment the system operates within (e.g., "banking", "healthcare") | 1 per system |
| **System** | Composed of Human-AI Team(s) and optional Machines | 1 |
| **Human-AI Team (HAT)** | Collaborative unit of interdependent agents | 1 or more |
| **Agent** | Entity that perceives, decides, and acts in pursuit of goals | 2+ per HAT |
| **Human Agent** | A type of Agent (human team member) | 0 or more per HAT |
| **AI Agent** | A type of Agent with Sensors and Actuators | 0 or more per HAT |
| **Machine** | Physical or logical object the system interacts with (database, API, robot, device) | 0 or more |

### 2.3 Behavioral Elements

#### Goals

> A **Goal** is a desirable state that one or more agents desire to achieve.

Goals are hierarchical and can be decomposed:

```
System Primary Goal
    ├── HAT Goal 1
    │       ├── Subgoal 1.1
    │       └── Subgoal 1.2
    ├── HAT Goal 2
    └── External Actor Goals
```

#### The Goal-Role-Responsibility Chain

This chain flows through the center of the AOSM meta-model:

```
Goals → Roles → Responsibilities → Capabilities → Agents
```

| Element | Definition |
|---------|------------|
| **Goal** | Desirable end state to achieve |
| **Role** | A set of Responsibilities necessary to fulfill a Goal |
| **Responsibility** | A PIDA activity the agent must accomplish |
| **Capability** | Knowledge, Skills, Abilities (KSA) needed to fulfill Responsibility |
| **Agent** | The entity (human or AI) allocated to perform the work |

#### PIDA: The Four Types of Responsibility

Every Responsibility falls into one of four categories:

| Type | Definition | Example |
|------|------------|---------|
| **Perception** | Sensing and gathering information from the environment | Monitor transaction stream |
| **Interpretation** | Making sense of perceived information, understanding context | Identify anomalous patterns |
| **Decision** | Selecting a course of action based on interpretation | Determine if escalation needed |
| **Action** | Executing the selected action in the environment | Block transaction, alert human |

For each Responsibility, designers should ask:
- What **Knowledge** must the agent have?
- What **Skills** must the agent perform?
- What **Abilities** are required?

### 2.4 Capability Elements

**Capability** = Knowledge + Skills + Abilities (KSA)

| Component | Definition |
|-----------|------------|
| **Knowledge** | Information the agent must know or have access to |
| **Skills** | Behaviors the agent must learn and perform to accomplish tasks |
| **Abilities** | Innate capacity to perform skilled behaviors |
| **Training** | Process to develop KSA in an agent (human or AI) |
| **Procedures** | Processes encoding the organization's protocols |

### 2.5 Authority Elements: The Four Components of Autonomy

For an agent to act autonomously, it must have all four components (Stevenson et al., 2023):

| Component | Definition |
|-----------|------------|
| **Authority** | The right to select or perform an action free from external control |
| **Availability** | Being present and able to perform the activities |
| **Capability** | Having the KSA to select and perform activities |
| **Capacity** | Having resources available under specific circumstances |

**Autonomy** = Authority + Availability + Capability + Capacity

**Controlled Autonomy** (Required for AI Agents):
> The agent should act autonomously only to the extent that it is beneficial to the physical entity (e.g., human) who is responsible for controlling it.

AI agents cannot be held legally responsible for their actions, therefore:
- Authority should not be granted for actions that could reasonably result in harm
- A human must always be **Accountable**

### 2.6 Interaction Elements: OPD Requirements

For agents to work together as teammates, they require **OPD Elements**:

| Element | Definition |
|---------|------------|
| **Observability** | The ability to obtain information to understand a teammate's state |
| **Predictability** | The ability to understand what a teammate will do in the future |
| **Directability** | The ability to require or request a teammate to perform a desired activity |

### 2.7 Team Interdependence Patterns

Teams can exhibit three types of interdependence (Thompson, 2003):

| Pattern | Description | Communication Need |
|---------|-------------|-------------------|
| **Pooled** | Each agent performs separate functions not time-dependent; contributions to shared pool | Low—no direct coordination needed |
| **Sequential** | One agent must complete before another can start (assembly line) | Medium—handoff signaling |
| **Reciprocal** | Agents perform multiple interleaved tasks with back-and-forth exchanges | High—continuous coordination |

### 2.8 Accountability Elements: RASCI

The RASCI framework assigns responsibility for each activity:

| Role | Definition |
|------|------------|
| **Accountable (A)** | Agent bearing risk and consequences of outcome; justifies decisions. **Must be human.** |
| **Responsible (R)** | Agent executing the activities; ensures completion |
| **Supporting (S)** | Agent aiding in accomplishing the task |
| **Consulted (C)** | Agent providing opinions, guidance, recommendations |
| **Informed (I)** | Agent apprised of progress, decisions, outcomes |

> **Critical Rule**: In an AOS, the **Accountable** role must always be assigned to a human. AI agents can be Responsible, Supporting, Consulted, or Informed—but never Accountable.

---

## 3. Semantic Representation: AOS Schema

The following schema expresses the AOSM meta-model as a formal structure:

```yaml
AgentOrientedSystem:
  # Context
  environment:
    description: string
    domains: Domain[]
    
  # System of Interest
  system:
    id: string
    name: string
    description: string
    primaryGoal: Goal
    goals: Goal[]
    teams: HumanAITeam[]
    machines: Machine[]

# Team Structure
HumanAITeam:
  id: string
  name: string
  goals: Goal[]
  agents: Agent[]               # min 2
  coordinationPattern: "pooled" | "sequential" | "reciprocal"
  rasciAssignments: RASCI[]

# Agent Types
Agent:
  id: string
  name: string
  type: "human" | "ai"
  roles: Role[]
  capabilities: Capability[]
  training: Training
  procedures: Procedure[]
  autonomy: Autonomy
  opdRequirements: OPDRequirements

AIAgent extends Agent:
  type: "ai"
  sensors: Sensor[]             # min 1
  actuators: Actuator[]         # min 1
  controlledAutonomy: true      # always true for AI

HumanAgent extends Agent:
  type: "human"

# Goal Structure
Goal:
  id: string
  name: string
  description: string
  parent: Goal | null
  subgoals: Goal[]
  roles: Role[]                 # roles that serve this goal

# Role and Responsibility
Role:
  id: string
  name: string
  goals: Goal[]
  responsibilities: Responsibility[]

Responsibility:
  id: string
  description: string
  type: "perception" | "interpretation" | "decision" | "action"
  requiredCapabilities: Capability[]
  allocatedTo: Agent[]

# Capability
Capability:
  id: string
  knowledge: Knowledge[]
  skills: Skill[]
  abilities: Ability[]

Knowledge:
  id: string
  description: string
  source: string                # where this knowledge comes from

Skill:
  id: string
  description: string
  trainable: boolean

Ability:
  id: string
  description: string
  innate: boolean

# Autonomy
Autonomy:
  authority: AuthoritySpec
  availability: AvailabilitySpec
  capability: Capability
  capacity: CapacitySpec
  controlled: boolean           # must be true for AI agents

# Accountability
RASCI:
  responsibility: Responsibility
  accountable: HumanAgent       # must be human
  responsible: Agent[]
  supporting: Agent[]
  consulted: Agent[]
  informed: Agent[]

# Interaction
OPDRequirements:
  observability:
    stateExposure: string[]     # what state is visible
    monitoringMechanism: string
  predictability:
    behaviorModel: string
    guardrails: string[]
  directability:
    overrideMechanism: string
    commandInterface: string
```

---

## 4. Process: Designing an Agent-Oriented System

The AOSM design process consists of **six iterative steps**:

```
┌──────────────────────────────────────────────────────────────────┐
│  1. Define System Boundary                                        │
│         ↓                                                         │
│  2. Develop Understanding of "As-Is" System                       │
│         ↓                                           ↑             │
│  3. Define Goals and Understanding of "To-Be" System              │
│         ↓                                           │             │
│  4. Design "To-Be" System ─────────────────────────┘              │
│         ↓                      (if understanding inadequate)      │
│  5. Validate "To-Be" Design ────────────────────────┐             │
│         ↓                      (if design inadequate)│            │
│  6. Generate Specifications                          │             │
│                                                      ↑             │
│                              (return to step 3 if needed)         │
└──────────────────────────────────────────────────────────────────┘
```

This is **not a linear process**—it often requires revisiting earlier activities as new information is discovered.

---

### Step 1: Define System Boundary

**Purpose:** Establish what is inside vs. outside the system.

**Activities:**

| Activity | Output |
|----------|--------|
| Develop **Stakeholder Narratives** | Who cares about this system and why? |
| Depict **System in BDD** | Block Definition Diagram showing system composition |
| Depict **Domain in BDD** | The environment the system operates in |
| Identify **Domain Uses** | What does the domain need from the system? |
| Create **Use Case Diagram (UCD)** | Actor interactions with the system |
| Identify **Difficult Decisions** | Edge cases, exceptions, failure scenarios |

**Key Questions:**
- What is the System of Interest?
- What external systems/agents does it interact with?
- What is in scope vs. out of scope?

---

### Step 2: Develop Understanding of "As-Is" System

**Purpose:** Understand the current state before designing the future.

**Activities:**

| Activity | Output |
|----------|--------|
| Identify current **Human Agents** | Who does the work today? |
| Identify current **AI/Automation** | What automation exists? |
| Document current **Workflows** | How does work flow through the system? |
| Map current **Capabilities** | What KSA exists? |
| Identify **Pain Points** | What doesn't work well? |
| Understand current **Coordination** | How do agents collaborate today? |

**Key Questions:**
- How is the work done today?
- What are the current roles and responsibilities?
- Where are the gaps that AI could address?

---

### Step 3: Define Goals and Understanding of "To-Be" System

**Purpose:** Define what the future system should achieve.

**Activities:**

| Activity | Output |
|----------|--------|
| Define **Goal Hierarchy** | Hierarchical decomposition of objectives |
| Map **Goals to Roles** | Which roles serve which goals? |
| Define **Responsibilities (PIDA)** | What must be perceived, interpreted, decided, acted upon? |
| Identify required **Capabilities** | What KSA is needed for each responsibility? |
| Create **Concept Maps** | How do concepts relate to goals? |

**Goal Hierarchy Template:**

```
System Primary Goal: [What is the overarching purpose?]
    ├── HAT Goal: [What must the human-AI team achieve?]
    │       ├── Subgoal: [Specific outcome 1]
    │       └── Subgoal: [Specific outcome 2]
    ├── Stakeholder Goal: [What do external actors need?]
    └── Quality Goal: [Non-functional requirements]
```

---

### Step 4: Design "To-Be" System

**Purpose:** Design the future Human-AI Team structure.

**Activities:**

| Activity | Output |
|----------|--------|
| Create **Responsibility-Capability Diagram** | Map responsibilities to required capabilities |
| Create **Capability Assessment Table** | Assess human vs. AI capability allocation |
| Arrange Capabilities into **Roles** | Group related capabilities |
| Create **"As-Is" IBDs** for Roles | Internal Block Diagrams showing current interactions |
| Create **"To-Be" IBDs** for Roles | Redesigned interactions |
| Synthesize **Agent Diagram** | Which agents are allocated to which capabilities |
| Create **RASCI Allocation Table** | Responsibility assignment matrix |

**Capability Assessment Questions:**

For each Capability, ask:
1. Can a human do this? Should they?
2. Can AI do this? Should it?
3. What is the risk if AI fails?
4. What oversight is needed?
5. Who is Accountable?

#### Function Allocation: Beyond Simple Comparisons

The book (Chapter 7) discusses several **allocation strategies** that have been used historically, along with their limitations:

**Historical Context: Fitts' List (1951)**

Paul Fitts enumerated 11 generic functions comparing human and machine strengths. While influential, the book cautions against using Fitts' List as the sole basis for allocation decisions. Three common **fallacies** arise from misapplying it:
1. **Comparison Fallacy**: The 11 items are not clearly comparable—some describe procedures, others describe capabilities
2. **Context Independence Fallacy**: Capacities of both humans and machines vary depending on circumstances (workload, stress, fatigue)
3. **Granularity Fallacy**: Real functions rarely comprise solely one of the 11 items; actual work is more complex

**Allocation Strategies and Their Trade-offs**

| Strategy | Description | Limitation |
|----------|-------------|------------|
| **Leftover Principle** | Allocate to automation everything that can be automated; humans handle what remains | Treats humans as "leftover" components; ignores human strengths; leads to poor human factors design |
| **Compensatory Principle** | Each entity compensates for the other's weaknesses (based on Fitts' List) | Assumes static capabilities; real capacity varies with context; criticized for oversimplification |
| **Economic Allocation** | Allocate based on cost efficiency | May sacrifice safety, reliability, or human factors for cost |
| **Capability-Based Allocation** | Allocate based on which entity has the capability for satisfactory performance | More nuanced; accounts for context; the approach recommended by AOSM |

**The AOSM Approach: Capability-Based Allocation**

The book recommends allocating functions based on which entity is **capable of satisfactory performance** given:
- The specific context and circumstances
- Available capacity (resources, time, attention)
- Required OPD characteristics (Observability, Predictability, Directability)
- The need for a human to remain **Accountable**

> "Functions should be allocated to the entity which is capable of satisfactory performance."  
> — *Integrating Artificial and Human Intelligence through Agent-Oriented Systems Design*, Chapter 7

**Capability Assessment Questions:**

For each Responsibility, assess:

| Question | Implications for Allocation |
|----------|----------------------------|
| Does this require legal/ethical accountability? | **Human must be Accountable (A)**; AI may be Responsible (R) |
| Does capacity vary with context (workload, fatigue)? | Consider dynamic allocation; avoid assuming fixed capabilities |
| Is the task well-defined or novel? | Well-defined → AI may be suitable; Novel → Human judgment likely needed |
| What happens if the agent fails? | High-consequence → Ensure human oversight or override capability |
| Is 24/7 availability required? | Favors AI for Availability; human for Accountability |
| Does the task require relationship/trust? | Human allocation often preferred |

#### Connecting to Human-AI Team Patterns (Chapter 8)

Allocation decisions are not made in isolation—they shape the **team pattern** that emerges. The book (Chapter 8) provides patterns that embody different allocation philosophies:

| HAT Pattern | Allocation Philosophy | When to Use |
|-------------|----------------------|-------------|
| **Colocated Supervisory Control** | Human supervises; AI handles routine operations | Traditional automation with human oversight |
| **Connected Supervisory Control** | Human supervises remotely; AI maintains local control | Remote operations where human presence is impractical |
| **Disconnected Supervisory Control** | AI operates autonomously when human connection unavailable | Latency-sensitive or connectivity-limited scenarios |
| **Decision Support Pattern** | AI structures information; Human makes decisions | Advisory scenarios; no physical machine control |
| **Accident Prevention Pattern** | AI monitors and can override human to prevent harm | Safety-critical systems |
| **Overwatch Pattern** | One agent monitors others, ready to intervene | Quality assurance, compliance monitoring |
| **Dual-Mode Cognitive HAT** | Human coordinates multiple AI agents | Multi-agent workflows, orchestration |

**Pattern Selection Considerations:**

- **Supervisory Control Continuum**: As AI autonomy increases (Colocated → Connected → Disconnected), human oversight decreases but AI capability requirements increase
- **Physical vs. Information Systems**: Enterprise AI (Zeta's domain) typically uses Decision Support and Overwatch patterns rather than physical supervisory control
- **Multi-Agent Scenarios**: Dual-Mode Cognitive HAT and Orchestration patterns are most relevant for Zeta's multi-agent products

> **Key Insight**: The choice of HAT pattern constrains and is constrained by allocation decisions. A Decision Support pattern assumes humans make final decisions; an Overwatch pattern assumes the primary agent operates with significant autonomy while another monitors for exceptions.

---

### Step 5: Validate "To-Be" Design

**Purpose:** Ensure the design will work in practice.

**Validation Checklist:**

| Aspect | Validation Question |
|--------|---------------------|
| **Authority** | Do agents have the authority to perform their assigned responsibilities? |
| **Availability** | Are agents available when needed? |
| **Capability** | Do agents have sufficient KSA? |
| **Capacity** | Are resources (compute, time, budget) adequate? |
| **OPD** | Is the system Observable, Predictable, Directable? |
| **Accountability** | Is there always a human Accountable for each activity? |
| **Coordination** | Can agents coordinate effectively for their interdependence pattern? |
| **Failure Modes** | What happens when an agent fails? |
| **Override** | Can humans intervene when needed? |

**Validation Methods:**
- Scenario walkthroughs
- Simulation
- Prototype testing
- Stakeholder review

---

### Step 6: Generate Specifications

**Purpose:** Produce artifacts that enable implementation.

**Output Artifacts:**

| Artifact | Content |
|----------|---------|
| **Agent Specifications** | For each agent: identity, roles, capabilities, training requirements |
| **Interface Specifications** | How agents interact (APIs, protocols, UIs) |
| **Coordination Protocols** | How agents coordinate for each interdependence pattern |
| **Training Requirements** | What training (human and AI) is needed |
| **Authority Delegation Model** | How authority flows, constraints, revocation |
| **Monitoring Requirements** | OPD implementation—dashboards, alerts, logs |
| **Failure Response Procedures** | What happens when things go wrong |

---

## 5. Modeling Artifacts Summary

The AOSM design process uses **SysML** (Systems Modeling Language) diagrams:

| Artifact | Purpose | Used In Step |
|----------|---------|--------------|
| **Block Definition Diagram (BDD)** | System structure and composition | 1, 2 |
| **Internal Block Diagram (IBD)** | Information flows between components | 2, 4 |
| **Use Case Diagram (UCD)** | Actor interactions with system | 1 |
| **Activity Diagram** | Process flows | 2, 4 |
| **Goal Hierarchy Diagram** | Hierarchical decomposition of objectives | 3 |
| **Responsibility-Capability Diagram** | Links responsibilities to required capabilities | 4 |
| **Agent Diagram** | Allocates capabilities to specific agents | 4 |
| **RASCI Allocation Table** | Responsibility assignment matrix | 4 |
| **Capability Assessment Table** | Human vs. AI capability allocation decisions | 4 |

---

## 6. Mapping to Zeta's Agent Terminology

When designing agent products using AOSM:

| AOSM Concept | Zeta Representation |
|--------------|---------------------|
| **System** | The deployed agent solution |
| **HAT** | The human(s) + Employed Agent(s) working together |
| **AI Agent** | Raw Agent + Training + Employment |
| **Environment** | Operational Environment in Employment Spec—connection strings, credentials, tool endpoints |
| **Goals** | Customer outcomes the agent helps achieve |
| **Roles** | Defined in Training Spec |
| **Responsibilities (PIDA)** | What the agent perceives, interprets, decides, acts on |
| **Capabilities (KSA)** | Raw (Abilities) + Trained (Knowledge, Skills) |
| **Autonomy** | Employment Spec (Authority + constraints) |
| **OPD** | Observability/logging, predictability/guardrails, directability/override |
| **RASCI** | Manager/delegator (Accountable), Agent (Responsible) |
| **Training** | Training Spec + Training process |
| **Procedures** | Guardrails and procedures in Training Spec |

> **Key Distinction**: Training defines *what tools* the agent can use abstractly. Employment's Operational Environment provides the *concrete bindings*—the actual endpoints, credentials, and connection parameters for the specific deployment.

### Zeta Agent Layers as AOS Elements

| Zeta Layer | AOSM Equivalent |
|------------|-----------------|
| **Raw Agent** | AI Agent with Abilities (technical capabilities) |
| **Trained Agent** | AI Agent with Training, Knowledge, Skills, Procedures, Role |
| **Employed Agent** | AI Agent with Authority, allocated to HAT, RASCI assignment |

---

## 7. References

### Primary Sources

- *Integrating Artificial and Human Intelligence through Agent-Oriented Systems Design* (Systems Innovation Book Series, CRC Press/Taylor & Francis)
- Sterling, L., & Taveter, K. (2009). *The Art of Agent-Oriented Modeling*
- Stevenson et al. (2023). Four Components of Autonomy

### Supporting References

- Bradshaw, J. M. (2013). Autonomy: A proposed standard formalization
- Brooks, R. A. (1986). A robust layered control system for a mobile robot (subsumption architecture)
- Crowston, K. (1991). Coordination theory and its application to organizational computing
- Johnson, M., et al. (2018). OPD framework for human-machine teaming
- Thompson, J. D. (2003). *Organizations in Action* (Pooled, sequential, reciprocal interdependence)
- Wooldridge, M. (2013). *An Introduction to MultiAgent Systems* (Agent architectures)

---

## 8. See Also

- [Agent Terminology: Raw, Trained, Employed](./agent-is-not-one-thing.md)
- [Book Summary: AOSM Framework](./book-ref/book-summary.md)

---

*This document provides a foundation for designing Agent-Oriented Systems within Zeta's enterprise context. The AOSM framework ensures that human-AI collaboration is structured, accountable, and governable.*

