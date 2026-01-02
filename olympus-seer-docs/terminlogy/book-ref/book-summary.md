# Book Summary: Integrating Artificial and Human Intelligence through Agent-Oriented Systems Design

**Author(s):** Systems Innovation Book Series  
**Publisher:** [Academic/CRC Press - Taylor & Francis]

---

## Executive Summary

This book presents a comprehensive framework for designing **Human-AI Teams** using **Agent-Oriented Systems Modeling (AOSM)**. It provides a model-based systems engineering approach to integrate artificial and human intelligence, treating AI agents as near-peers to humans within collaborative teams. The book emphasizes that both humans and AI agents share fundamental characteristics: they sense, act, and pursue goals—making them suitable for unified modeling and design.

---

## Part 1: Foundations

### Chapter 1: Introducing Human-AI Teaming

#### Why Human-AI Teaming Matters
- AI agents are becoming ubiquitous due to low-cost digital sensors, actuators, and computing power
- Modern systems require multiple humans and AI agents working together to accomplish joint work
- Complex teams require careful structuring to reliably fulfill the team's goal or purpose
- Designers must place more effort on structuring these teams as they become more complex

#### Key Definitions

**System**
> The holistic sum of interdependent parts that interact to achieve a specific purpose or goal.
- The interaction and interdependence of parts are inherent properties of a system
- Properties of the system emerge as components interact (**Emergence**)

**Agent**
> An entity that perceives its environment and acts upon that environment in pursuit of goals.
- Agents are a generalization of Humans and AI agents
- Each Human or AI agent is a type of Agent
- AI agents comprise at least one **Actuator** and one **Sensor**

**AI Agent**
> A goal-seeking software/hardware entity designed to exhibit "controlled autonomy"—acting autonomously only to the extent that it is beneficial to the physical entity (e.g., human) who is responsible for controlling it.

**Machine**
> A generic manufactured physical object that interacts with the environment (e.g., robot, automobile, aircraft). Machines are optional; systems may exist without them.

**Human-AI Team**
> A team comprising two or more Agents (humans and/or AI agents) that work interdependently through user interfaces to achieve system goals.

---

### The Four Components of Autonomy (Stevenson et al., 2023)

Autonomy requires **four preconditions**:

| Component | Definition |
|-----------|------------|
| **Authority** | The right to select or perform an action free from external control |
| **Availability** | Being present and able to perform the activities |
| **Capability** | Having the knowledge, skills, and abilities to select and perform activities |
| **Capacity** | Having resources available under specific circumstances (context-dependent) |

**Autonomy** is typically defined as the authority to select or perform an action free from external control or influence (Bradshaw, 2013).

**Autonomous Agents** are agents that create and pursue their own goals, as opposed to being controlled by another agent (Sterling & Taveter, 2009).

**Controlled Autonomy**: The agent should act autonomously only to the extent that it is beneficial to the physical entity (e.g., human) who is responsible for controlling it. AI agents cannot be held responsible for their actions and therefore should not be granted authority for actions which could reasonably result in harm.

#### Agency vs. Autonomy

**Agency** is the broader concept referring to an agent's capacity to act in the world. According to the book, *agents do not have to be autonomous or exhibit agency*—these are distinct qualities:

- **Agency** encompasses the agent's capacity to perceive, reason, and act
- **Autonomy** specifically refers to the *authority* to act free from external control
- An agent may have agency (capability to act) without having autonomy (authority to act independently)

This distinction is critical for AI systems: an AI agent may have full capability (agency) but operate under strict delegated authority (controlled autonomy).

---

## Responsibility and Capability: The PIDA Framework

### Critical Distinction: Responsibilities vs. Capabilities

The book provides a precise distinction between Responsibilities and Capabilities that is essential for agent design:

> **Responsibilities** are the **Perception, Interpretation, Decision, and Action (PIDA)** activities that the Human-AI Team must accomplish to fulfill a goal. That is, they are **tasks**.
>
> **Capabilities** are the **Knowledge, Skills, and Abilities (KSA)** needed to accomplish Responsibilities. That is, they are **qualities or attributes** of an agent.

#### The PIDA Model

Responsibilities can be categorized into four types of activities:

| PIDA Activity | Description |
|---------------|-------------|
| **Perception** | Sensing and gathering information from the environment |
| **Interpretation** | Making sense of perceived information, understanding context |
| **Decision** | Selecting a course of action based on interpretation |
| **Action** | Executing the selected action in the environment |

#### The KSA Framework for Capabilities

Capabilities are the qualities that enable an agent to fulfill responsibilities:

| Capability Type | Definition |
|-----------------|------------|
| **Knowledge** | Information that the agent must *know* or *have access to* |
| **Skills** | Behaviors that the agent must *learn and perform* to do the task |
| **Abilities** | *Innate capacity* to perform skilled behaviors |

> Many responsibilities require both knowledge and skills or abilities and may even require multiple knowledge or skill capabilities.

#### Practical Application

For each Responsibility in the Goal–Responsibility diagram, designers should ask:
1. What **knowledge** does the agent need to accomplish this task?
2. What **skills** must the agent learn and perform?
3. What **abilities** (innate capacities) are required?

This distinction maps directly to Zeta's agent layers:
- **Capable Agents** possess core KSA through their code/implementation
- **Skilled Agents** are trained/configured with additional domain-specific knowledge
- **Employed Agents** are authorized to exercise their capabilities in specific contexts

---

## Part 2: The AOSM Meta-Model

### Chapter 2: Defining Your System

The **Agent-Oriented Systems Modeling (AOSM)** meta-model defines the core concepts and relationships for designing human-AI teams.

#### Meta-Model Components

```
┌─────────────────────────────────────────────────────────────────┐
│                        ENVIRONMENT                               │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                         DOMAIN                             │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │                       SYSTEM                         │  │  │
│  │  │  ┌────────────────┐    ┌────────────────────────┐   │  │  │
│  │  │  │    Machine     │    │    Human-AI Team       │   │  │  │
│  │  │  │  (0 or more)   │    │ ┌───────┐  ┌────────┐  │   │  │  │
│  │  │  │                │    │ │ Human │  │AI Agent│  │   │  │  │
│  │  │  └────────────────┘    │ └───────┘  └────────┘  │   │  │  │
│  │  │                        │      (2 or more)       │   │  │  │
│  │  │                        └────────────────────────┘   │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

#### Key Concepts from the Meta-Model

| Concept | Definition |
|---------|------------|
| **Environment** | The context in which the system operates and interacts |
| **Domain** | A part of the Environment in which the System operates |
| **System** | Composed of one or more Human-AI Teams and may include Machines |
| **Human-AI Team** | Comprised of two or more Agents (Humans or AI Agents) |
| **Goal** | A desirable state that one or more Agents desire to achieve |
| **Role** | A set of Responsibilities necessary to fulfill a Goal or set of goals |
| **Responsibility** | Abstract items that must be accomplished (functionally oriented, no presumed temporal sequence) |
| **Capability** | A set of knowledge, skills, and abilities necessary to fulfill a requirement |
| **Training** | Required by each agent (human or AI) to develop their knowledge, skills, and abilities |
| **Procedures** | Processes which encode the organization's protocols |

---

### OPD Elements: Agent Interaction

For agents to interact effectively as teammates, they require **OPD Elements**:

| Element | Definition |
|---------|------------|
| **Observability** | The ability to obtain information to understand the state of your teammate |
| **Predictability** | The ability to understand what your teammate will do in the future |
| **Directability** | The ability to require or request your teammate to perform a desired activity |

---

## Part 3: The AOSM Design Method

### Six High-Level Process Steps

The Agent-Oriented Systems Modeling (AOSM) design process consists of six high-level steps:

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
│         ↓                      (if design inadequate)│             │
│  6. Generate Specifications                          │             │
│                                                      ↑             │
│                              (return to step 3 if needed)         │
└──────────────────────────────────────────────────────────────────┘
```

This is **not a linear process**—it often requires revisiting earlier activities as new information is discovered or design decisions need to be reconsidered.

---

### Chapter 3: Goals and Responsibilities

**Goals** describe desired end states but do not attempt to describe how the agent achieves those goals.

- Goals can be pursued by all agents, including human and AI agents
- Goals drive the need for changes in the system
- Goals are hierarchical and can be decomposed into subgoals

**The Goal-Role-Responsibility Chain:**
```
Goals → Roles → Responsibilities → Capabilities → Agents
```

This chain flows through the center of the meta-model and serves as the focus for design.

- **Goals**, **Roles**, and **Responsibilities** exist regardless of how designers implement the human-AI team
- One can start the design process by understanding these elements in any current system implementation

---

### Chapter 4: Coordination and Interdependence

#### Team Interdependence Patterns (Thompson, 2003)

The coupling of interdependence between team members can be described as three types:

| Pattern | Description | Communication Need |
|---------|-------------|-------------------|
| **Pooled Interdependence** | Each entity performs separate functions that are **not time dependent**. Team members contribute independently to a shared pool. | Does not necessarily require communication |
| **Sequential Interdependence** | One individual must perform an activity **before** another can perform theirs. Like an assembly line—temporal ordering matters. | Requires communication so subsequent teammate knows when it's their turn |
| **Reciprocal Interdependence** | Team members must each perform **multiple interleaved tasks**, with back-and-forth exchanges. | Requires significant communication about order, timing, and completion status |

When work is repetitious, team members can rely on cues (e.g., elapsed time) to support interdependence without explicit communication.

#### Coordination

> **Coordination** can be defined as a cyclical communication process that enables synchronized actions of teammates who are working on interdependent tasks. (Crowston, 1991; Schneider et al., 2022)

Key aspects of coordination:
- While communication may occur in preparation or after-action phases, **coordination occurs during the action phase**
- Teammates can plan and practice coordination such that they do not require explicit coordination
- For effective coordination, each agent must be able to **observe and predict** the actions of team members

#### Implicit vs. Explicit Coordination

| Type | Description |
|------|-------------|
| **Implicit Coordination** | Teammates rely on shared understanding, cues, and predictable patterns to coordinate without direct communication |
| **Explicit Coordination** | Requires direct communication for synchronized action |

Communication is especially important when:
1. Task timing depends on external events
2. Tasks depend on other team members' prior work
3. Tasks for one goal have consequences for other team goals

---

### Chapter 6: AI Agent Architectures

The book describes four primary architectures for AI agents (based on Wooldridge, 2013):

#### 1. Logic-Based Architectures

- AI agent designer **symbolically codes** properties of the world in a database
- Combinations of property values are associated with specific actions
- **Advantages**: Straightforward to implement
- **Disadvantages**: 
  - Must accurately interpret sensor data
  - Database must cover all important conditions
  - Response time increases with number of logic statements
  - Difficult to predict behavior under all circumstances

#### 2. Reactive Architectures

- Agents use **local information** present in the environment to select actions
- Also called "subsumption architecture" (Brooks)
- Inspired by biological systems (e.g., neurons)
- **Advantages**: Simple, economical, robust
- **Disadvantages**: 
  - Must sense appropriate information accurately
  - Decisions may not be optimal (only uses local information)
  - Difficult to construct effective agents as layers increase
  - Behavior emerges at runtime—hard to predict

> A **reactive agent** can perceive (i.e., sense and interpret) its environment and respond to environmental changes in a timely fashion.

#### 3. Belief-Desire-Intention (BDI) Architectures

Combines **deliberation** with **means-ends reasoning**:

1. **Deliberation**: Agent decides what they want to achieve (selects/forms goals)
2. **Means-ends Reasoning**: Agent decides how to pursue the goal
3. **Options → Desires**: Available alternatives form the agent's desires
4. **Filtering**: Agent deliberates to form intentions from desires
5. **Intentions drive action**: Selected intentions constrain future reasoning

Key concepts:
- **Beliefs**: Agent's understanding of current and potential future states
- **Desires**: Available options the agent could pursue
- **Intentions**: Committed plans that persist and drive behavior

Agent behavior types:
- **Cautious agents**: Frequently reconsider their intentions
- **Bold agents**: Charge ahead without reconsidering intentions

> A **proactive agent** does not simply respond to changes in the environment but is able to pursue goal-directed behavior in an opportunistic fashion.

#### 4. Layered Architectures

Combines attributes of other architectures by implementing processes in **layers executed simultaneously**:
- May implement **reactive components** in one layer
- May implement **proactive components** in another layer
- Agent reasons across layers to form its response

This allows agents to balance reactive responsiveness with deliberative planning.

#### Agent Classification Summary

| Agent Type | Key Characteristic |
|------------|-------------------|
| **Reactive Agent** | Perceives environment and responds to changes in timely fashion |
| **Proactive Agent** | Pursues goal-directed behavior, anticipates future events |
| **Interactive Agent** | Capable of interacting directly with other agents |
| **Social Agent** | Can interact with other agents to complete activities and help others |
| **Intelligent Agent** | Can be both reactive and proactive, as well as social |

---

### Chapters 5-7: Designing the "To-Be" System

These chapters cover:
- **Chapter 5**: Applying design goals
- **Chapter 6**: AI Agent Architectures (covered above)
- **Chapter 7**: Function Allocation and Capability Assessment

---

### Chapter 7: Function Allocation and Capability Assessment

This chapter addresses a critical design question: **How do we decide what to allocate to humans vs. AI agents?**

#### 7.1 Historical Context: Fitts' List (1951)

Paul Fitts (US Air Force) developed a list of 11 generic functions comparing what humans do better vs. what machines do better. While influential, the book cautions against misusing it.

**Three Fallacies of Fitts' List:**

| Fallacy | Description |
|---------|-------------|
| **Comparison Fallacy** | The 11 items are not clearly comparable—some describe procedures, others describe capabilities |
| **Context Independence Fallacy** | Capacities of both humans and machines vary depending on circumstances (workload, stress, fatigue) |
| **Granularity Fallacy** | Real functions rarely comprise solely one of Fitts' 11 items; actual work involves combinations |

#### 7.2 Leftover Principle

**Definition**: Allocate to automation everything that can be automated; humans handle what remains.

**Criticism**: 
- Treats humans as "leftover" components
- Ignores human strengths
- Leads to poor human factors design
- Results in humans performing only what machines cannot do, rather than what humans do well

#### 7.3 Compensatory Principle

**Definition**: Each entity (human or machine) compensates for the other's weaknesses, based on Fitts' List.

**Criticism**:
- Assumes static capabilities
- Real capacity varies with context (fatigue, workload, environmental factors)
- Oversimplifies the allocation decision
- Based on the fallacies of Fitts' List

**Key insight from the book**: Fitts pointed out that "humans are poor monitors"—ironic given that the Leftover Principle often relegates humans to monitoring roles.

#### 7.4 Recommended Approach: Capability-Based Allocation

The book recommends allocating functions based on which entity is **capable of satisfactory performance** given:
- The specific context and circumstances
- Available capacity (resources, time, attention)
- Required OPD characteristics
- The need for a human to remain **Accountable**

> "Functions should be allocated to the entity which is capable of satisfactory performance."

**Key Considerations for Allocation:**

| Factor | Question to Ask |
|--------|----------------|
| **Context Variability** | Does the agent's capacity vary with circumstances? |
| **Accountability** | Can this entity be held accountable for the outcome? (Only humans can) |
| **Failure Consequences** | What happens if this agent fails at this function? |
| **Workload** | Will this allocation overload or underload the agent? |
| **Coordination** | How will this allocation affect team coordination? |
| **OPD Requirements** | Can the team observe, predict, and direct this agent in this function? |

#### 7.5 Function Allocation vs. Task Allocation

| Aspect | Function Allocation | Task Allocation |
|--------|--------------------|-----------------| 
| **When** | Design time | Runtime/operational |
| **Who Decides** | Designers | Operators |
| **Scope** | Static assignment of capabilities | Dynamic assignment of specific work |
| **Flexibility** | Fixed in system design | Adapts to operational conditions |

---

### Chapter 8: Human–AI Agent Team Architectural Patterns

This chapter presents **reusable patterns** for structuring Human-AI Teams, addressing both dyadic (two-agent) and multi-agent team configurations.

#### 8.1.1 Patterns for Human–AI Team Dyads (Two-Agent Teams)

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Colocated Supervisory Control** | Human and AI agent are physically co-located; human supervises AI-controlled machine | Traditional automation with human oversight |
| **Connected Supervisory Control** | Human supervises remotely but maintains real-time connection to AI agent and machine | Remote operations, teleoperation |
| **Disconnected Supervisory Control** | AI agent operates machine autonomously when connection to human is unavailable | Autonomous vehicles, space/underwater systems |
| **Accident Prevention Pattern** | AI agent monitors for hazards and can override human control to prevent accidents; human controls unless collision is imminent | Safety-critical systems (auto-braking, collision avoidance) |
| **Decision Support Pattern** | AI agent aids human decision-making without controlling a physical machine; structures information for understanding, generating options, and selecting actions | Command-and-control, routing systems, advisory systems |

#### 8.1.2 Patterns for Larger Human–AI Teams (Multi-Agent)

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Dual-Mode Cognitive HAT** | One human coordinates multiple machines, each with embedded AI controller; a colocated decision support AI agent presents common operating picture and coordinates activities | Multi-drone operations, fleet management |
| **Subsumption Pattern** | Layered AI architecture where higher-level agents subsume lower-level behaviors; multiple layers of control (physical, level 2, level 3) | Complex robotic systems, hierarchical control |
| **Overwatch Pattern** | One agent monitors and oversees the work of other agents, ready to intervene | Quality assurance, supervisory monitoring |
| **Learner Prototype Pattern** | AI agent learns from observing human performance to improve its own capabilities | Apprenticeship learning, training systems |
| **Service Negotiator Prototype Pattern** | AI agent negotiates service levels or resource allocation among team members | Resource scheduling, workload balancing |

#### Key Concepts from Chapter 8

**Supervisory Control Continuum**:
The patterns range from tight human control to autonomous AI operation:
```
Colocated → Connected → Disconnected → Autonomous
     (More Human Control)      (More AI Autonomy)
```

**When Patterns Apply**:
- **Physical Machine Control**: Supervisory patterns
- **Decision Support Only**: Decision Support pattern (no machine involved)
- **Multiple Machines/Agents**: Dual-Mode Cognitive or Subsumption patterns

---

### 8.3 Modeling: Agent Diagram

The **Agent Diagram** captures the allocation of capabilities to specific agents and shows which agents will be members of the Human-AI Team.

---

### 8.4 Modeling: Allocated Agent Capability Table

Shows which capabilities are allocated to which agents (human or AI), revealing:
- Which capabilities are shared between agents
- Which capabilities are solely held by one agent
- Which agents carry the heaviest responsibility load

---

### 8.5 RASCI Allocation Table

**RASCI** = Responsible, Accountable, Supporting, Consulted, Informed

A responsibility assignment matrix adapted for Human-AI Teams:

| Role | Definition |
|------|------------|
| **Accountable (A)** | Agent that bears the risk and consequences of the outcome; justifies decisions; often the approval authority |
| **Responsible (R)** | Agent that executes the activities; may seek assistance or delegate but maintains obligation for completion |
| **Supporting (S)** | Agent that aids in accomplishing task activities |
| **Consulted (C)** | Agent that provides opinions, guidance, feedback, or recommendations |
| **Informed (I)** | Agent that is apprised of progress, decisions, and outcomes |

> Note: In Human-AI Teams, **Accountable** is almost always a **Human**—AI agents cannot bear legal or ethical accountability.

---

### Chapters 10-12: Validating the Design

- **Chapter 10**: Designing for exceptions
- **Chapter 11**: The coactive design process
- **Chapter 12**: Humans as team members

---

## Model-Based Systems Engineering (MBSE)

### SysML (Systems Modeling Language)

The book uses **SysML** as the primary modeling language, which extends UML (Unified Markup Language) for systems engineering:

- Provides diagrams for describing **structure**, **behavior**, and **requirements**
- Permits Systems Engineers to describe the entire system, including software and non-software components
- Key diagram types used:
  - **Block Definition Diagrams** (BDD) - system composition
  - **Internal Block Diagrams** (IBD) - component interactions
  - **Use Case Diagrams** - actor interactions
  - **Activity Diagrams** - process flows
  - **Goal Diagrams** - goal hierarchies

---

## Key Insights for AI Agent Design

### 1. Agents as Near-Peers
The book proposes a logical view where AI agents are **near-peers to humans**, existing conceptually outside the machine. This differs from physical views where AI may be embedded in hardware/software.

### 2. Controlled Autonomy is Essential
AI agents should exhibit **controlled autonomy**—acting autonomously only to the extent beneficial to the responsible human. This is because:
- AI agents cannot be held legally responsible for their actions
- Authority should not be granted for actions that could reasonably result in harm

### 3. Agents Need the Four Components of Autonomy
For an agent to be truly autonomous, it must have:
- **Authority** to act
- **Availability** to perform
- **Capability** to execute
- **Capacity** in the given context

### 4. Interdependence is Key
Human-AI teams are characterized by **interdependence**—the system cannot achieve its primary purpose when one of the interdependent parts is not present.

### 5. OPD Elements Enable Teaming
Effective human-AI teaming requires:
- **Observability**: Can I understand my teammate's state?
- **Predictability**: Can I anticipate my teammate's actions?
- **Directability**: Can I request or require specific actions?

---

## Glossary of Key Terms

| Term | Definition |
|------|------------|
| **Abilities** | Innate capacity to perform skilled behaviors (component of Capability) |
| **Action** | Executing a selected action in the environment (PIDA component) |
| **Agent** | An entity that perceives its environment and acts upon it in pursuit of goals |
| **Agency** | The broader capacity of an agent to perceive, reason, and act in the world |
| **AI Agent** | A software/hardware agent exhibiting controlled autonomy |
| **AOSM** | Agent-Oriented Systems Modeling - the design method presented in this book |
| **Authority** | The right to select or perform an action free from external control |
| **Availability** | Being present and able to perform activities |
| **Autonomy** | The authority to select or perform an action free from external control |
| **BDI Architecture** | Belief-Desire-Intention architecture combining deliberation with means-ends reasoning |
| **Beliefs** | Agent's understanding of current and potential future states (BDI) |
| **Capability** | Knowledge, skills, and abilities (KSA) necessary to fulfill a responsibility |
| **Capacity** | Available resources under specific circumstances |
| **Controlled Autonomy** | Acting autonomously only to the extent beneficial to the responsible human |
| **Coordination** | Cyclical communication process enabling synchronized actions of interdependent teammates |
| **Decision** | Selecting a course of action based on interpretation (PIDA component) |
| **Desires** | Available options the agent could pursue (BDI) |
| **Directability** | Ability to require or request a teammate to perform a desired activity |
| **Domain** | Part of the Environment in which the System operates |
| **Emergence** | Phenomenon where interactions among objects generate new phenomena |
| **Environment** | Context in which the system operates |
| **Explicit Coordination** | Coordination requiring direct communication for synchronized action |
| **Goal** | A desirable state that agents desire to achieve |
| **Human-AI Team** | Two or more agents (humans and/or AI) working interdependently |
| **Implicit Coordination** | Coordination through shared understanding, cues, and predictable patterns |
| **Intelligent Agent** | An agent that can be reactive, proactive, and social |
| **Intentions** | Committed plans that persist and drive behavior (BDI) |
| **Interdependence** | Parts of the system that depend upon one another to achieve purpose |
| **Interpretation** | Making sense of perceived information, understanding context (PIDA component) |
| **Knowledge** | Information that the agent must know or have access to (component of Capability) |
| **KSA** | Knowledge, Skills, and Abilities - the components of Capability |
| **Layered Architecture** | Agent architecture combining reactive and proactive components in simultaneous layers |
| **Machine** | A manufactured physical object that interacts with the environment |
| **MBSE** | Model-Based Systems Engineering |
| **Observability** | Ability to obtain information about a teammate's state |
| **OPD Elements** | Observability, Predictability, Directability |
| **Perception** | Sensing and gathering information from the environment (PIDA component) |
| **PIDA** | Perception, Interpretation, Decision, Action - the four types of Responsibilities |
| **Pooled Interdependence** | Team members perform separate functions that are not time dependent |
| **Predictability** | Ability to understand what a teammate will do in the future |
| **Proactive Agent** | Agent that pursues goal-directed behavior and anticipates future events |
| **Procedures** | Processes encoding the organization's protocols |
| **RASCI** | Responsible, Accountable, Supporting, Consulted, Informed - responsibility assignment matrix |
| **Reactive Agent** | Agent that perceives environment and responds to changes in timely fashion |
| **Reciprocal Interdependence** | Team members perform multiple interleaved tasks with back-and-forth exchanges |
| **Responsibility** | PIDA activities (tasks) that the HAT must accomplish to fulfill a goal |
| **Role** | Set of Responsibilities necessary to fulfill a Goal |
| **Sensor** | Component of an AI agent that perceives the environment |
| **Actuator** | Component of an AI agent that acts upon the environment |
| **Accident Prevention Pattern** | HAT pattern where AI monitors for hazards and can override human control |
| **Colocated Supervisory Control** | HAT pattern with human and AI physically co-located |
| **Connected Supervisory Control** | HAT pattern with human supervising remotely via real-time connection |
| **Decision Support Pattern** | HAT pattern where AI aids human decision-making without machine control |
| **Disconnected Supervisory Control** | HAT pattern where AI operates autonomously when human connection is unavailable |
| **Dual-Mode Cognitive HAT** | Multi-agent pattern for human coordinating multiple AI-controlled machines |
| **Overwatch Pattern** | HAT pattern where one agent monitors and supervises others |
| **Sequential Interdependence** | One individual must perform an activity before another can perform theirs |
| **Subsumption Pattern** | Layered AI architecture with higher levels subsuming lower behaviors |
| **Skills** | Behaviors that the agent must learn and perform to do a task (component of Capability) |
| **Social Agent** | Agent that can interact with others to complete activities and help others |
| **System** | Holistic sum of interdependent parts interacting to achieve a purpose |
| **SysML** | Systems Markup Language - a UML extension for systems engineering |
| **Training** | Development of knowledge, skills, and abilities for agents |
| **Fitts' List** | 1951 comparison of 11 human vs. machine functions; influential but criticized for three fallacies |
| **Leftover Principle** | Allocation strategy where automation handles everything possible; humans handle the rest |
| **Compensatory Principle** | Allocation strategy where humans and machines compensate for each other's weaknesses |
| **Capability-Based Allocation** | Recommended allocation approach: allocate to the entity capable of satisfactory performance |
| **Function Allocation** | Design-time assignment of capabilities to humans or AI agents |
| **Task Allocation** | Runtime/operational assignment of specific work items |
| **Training Guardrail Principle** | Employed Agents cannot override guardrails set during Training |

---

## Relevance to Zeta's Agent Terminology

This book's meta-model directly informs Zeta's proposed agent terminology:

### Core Mappings

| AOSM Concept | Zeta Parallel |
|--------------|---------------|
| Agent with Abilities (technical) | **Raw Agent** - the deployable artifact with technical execution capabilities |
| Agent with Training, Knowledge, Skills, Procedures | **Trained Agent** - configured with domain knowledge, skills, and procedures |
| Agent playing a Role with Authority in a HAT | **Employed Agent** - delegated authority to act in a specific context |
| Capabilities (KSA) | Accumulated across all layers: Abilities (Raw), Knowledge/Skills (Trained), Authority (Employed) |
| Goals → Roles → Responsibilities → Capabilities | The layered progression from product capability to deployed authority |
| Controlled Autonomy | Authority delegation model—Employed Agent cannot override Training guardrails |
| OPD Elements | Raw Agent: for System Operators; Employed Agent: for HAT team participants |

### PIDA Responsibilities Across Agent Layers

| PIDA Activity | Raw Agent | Trained Agent | Employed Agent |
|---------------|-----------|---------------|----------------|
| **Perception** | Modality support, sensor integration | Domain-specific data sources | Context-specific data access |
| **Interpretation** | LLM reasoning, context management | Domain prompts, organizational knowledge | Delegator preferences, situational context |
| **Decision** | Orchestration capabilities | Guardrails, policies, procedures | Authority-scoped decision rights (within Training bounds) |
| **Action** | Tool framework, execution patterns | Trained tool integrations | Authorized tool access with credentials |

### Agent Architecture Patterns in Zeta Context

| Architecture | Zeta Application |
|--------------|-----------------|
| **Reactive** | Event-driven agent responses, real-time triggers |
| **BDI** | Goal-directed agent reasoning, intent formation |
| **Layered** | Combining fast reactive responses with deliberative planning |

### Team Interdependence in Multi-Agent Zeta Systems

| Pattern | Zeta Application |
|---------|-----------------|
| **Pooled** | Multiple agents contributing independently to shared knowledge |
| **Sequential** | Workflow-based handoffs between specialized agents |
| **Reciprocal** | Collaborative agents with back-and-forth deliberation |

### HAT Architectural Patterns Applied to Zeta

| AOSM Pattern | Enterprise AI Equivalent | Zeta Applicability |
|--------------|-------------------------|-------------------|
| **Decision Support Pattern** | Advisory AI agents | Customer service copilots, decision assistants—Trained Agent aids human without autonomous action |
| **Accident Prevention Pattern** | Guardrail/safety agents | Risk assessment, fraud detection—Training guardrails that cannot be overridden |
| **Dual-Mode Cognitive HAT** | Orchestration with specialists | Raw Agent orchestrator coordinating multiple Employed Agents |
| **Overwatch Pattern** | Governance monitoring | Audit agents, policy enforcement—one Employed Agent supervises others' work |
| **Connected Supervisory Control** | Human-in-the-loop workflows | Employed Agent with Accountable human maintaining real-time oversight |
| **Disconnected Supervisory Control** | Autonomous batch agents | Employed Agent with role delegation—operates when Accountable human unavailable |

### RASCI Framework for Agent Governance

The RASCI model provides a framework for Zeta's **Employed Agent** governance:

| RASCI Role | Agent Type | Implementation |
|------------|-----------|----------------|
| **Accountable (A)** | Always Human (Manager/Delegate) | Human who bears legal/business responsibility |
| **Responsible (R)** | Employed Agent | Agent executing the task within Training bounds |
| **Supporting (S)** | Trained Agents (tools, specialists) | Agents providing trained capabilities |
| **Consulted (C)** | Knowledge/RAG agents | Agents providing information/recommendations |
| **Informed (I)** | Audit/logging systems | Systems tracking outcomes for compliance |

> **Key Insight**: In regulated industries, the **Accountable** role must always be a human—AI agents cannot bear legal or ethical accountability. This aligns with Zeta's requirement that Employed Agents always have a human manager/delegate.

### Training Guardrail Principle (Zeta-Specific)

From AOSM's Controlled Autonomy concept, Zeta derives:

> **Employed Agents can specialize but never expand beyond Training.**

| Layer | Can Do | Cannot Do |
|-------|--------|-----------|
| **Raw Agent** | Provide technical Abilities | Grant organizational Knowledge or Skills |
| **Trained Agent** | Define guardrails, procedures, allowed tools | Grant Authority |
| **Employed Agent** | Operate within Training bounds, suggest learnings | Override Training guardrails |

This ensures that governance constraints established during Training are immutable at runtime.

---

## References from the Book

- Bradshaw, J. M. (2013). Autonomy: A proposed standard formalization.
- Brooks, R. A. (1986). A robust layered control system for a mobile robot (subsumption architecture).
- Crowston, K. (1991). Coordination theory and its application to organizational computing.
- Dawson, C. (2020). Systems thinking definitions.
- Delligatti, L. (2013). SysML Distilled.
- Friedenthal, S., et al. (2014). A Practical Guide to SysML.
- Inagaki, T. (2006). Design of human-machine interactions.
- Johnson, M., & Bradshaw, J. M. (2021). Coactive design.
- Johnson, M., et al. (2018). OPD framework for human-machine teaming.
- Larman, C. (2005). Applying UML and Patterns.
- March, J. G., & Simon, H. A. (1958). Organizations.
- Miller, C., et al. (2020). Human-AI team meta-model.
- Schneider, et al. (2022). Coordination in human-AI teams.
- Sterling, L., & Taveter, K. (2009). The Art of Agent-Oriented Modeling.
- Stevenson, et al. (2023). Four components of autonomy.
- Thompson, J. D. (2003). Organizations in Action: Social Science Bases of Administrative Theory. (Pooled, sequential, reciprocal interdependence)
- Wooldridge, M. (2013). An Introduction to MultiAgent Systems. (Agent architectures)

---

*Summary prepared for Zeta internal use. This summary captures key concepts and definitions to inform the design of Zeta's Agent Platform and associated terminology.*

