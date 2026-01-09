# Ontology: Visual Diagrams

This document contains visual representations of the Human–AI Team Operations ontology.

---

**Navigation:** [← Automation Layer](./ontology-4-automation-layer.md) | [Ontology Reference](./ontology-reference.md)

---

## Table of Contents

- [Mermaid Class Diagram (Layered)](#mermaid-class-diagram-layered)
- [Mermaid Ontology Graph](#mermaid-ontology-graph)

---

## Mermaid Class Diagram (Layered)

This diagram shows the class hierarchy and key relationships between ontology concepts. Colors indicate key entity types:
- 🟢 **Mint**: Infrastructure concepts (Workbench, Queues, Registries)
- 🟠 **Peach**: Agent concepts (Human, AI Agent)
- 🔴 **Rose**: Operation concept

```mermaid
---
config:
  layout: elk
  theme: forest
---
classDiagram
direction TB
    class Domain {
    }
    class Workbench {
    }
    class Business_Entity {
    }
    class Environment {
    }
    class Machine {
    }
    class Sensors {
    }
    class Signal {
    }
    class Request {
    }
    class Trigger {
    }
    class Scenarios {
    }
    class OPD_Element {
    }
    class Observe {
    }
    class Predict {
    }
    class Decide {
    }
    class Role {
    }
    class Goal {
    }
    class SOP {
    }
    class Knowledge_Base {
    }
    class Runbook {
    }
    class Checklist {
    }
    class Capability {
    }
    class Capacity {
    }
    class Decision {
    }
    class Information_Element {
    }
    class Data_Element {
    }
    class Operation {
    }
    class Workflow {
    }
    class Case {
    }
    class Procedure {
    }
    class Activity {
    }
    class Task {
    }
    class Escalation {
    }
    class Task_Queue {
    }
    class Action {
    }
    class Agent {
    }
    class Human {
    }
    class AI_Agent {
    }
    class Human_AI_Team {
    }
    class Training {
    }
    class Automation {
    }
    class Automation_System {
    }
    class Tool {
    }
    class Prediction_Application {
    }
    class Decision_Application {
    }
    class Command {
    }
    class Tool_Registry {
    }
    class Machine_Registry {
    }
    class Responsibility {
    }

	<<abstract>> OPD_Element
	<<abstract>> Operation
	<<abstract>> Tool

    Agent <|-- Human
    Agent <|-- AI_Agent
    OPD_Element <|-- Observe
    OPD_Element <|-- Predict
    OPD_Element <|-- Decide
    Tool <|-- Prediction_Application
    Tool <|-- Decision_Application
    Tool <|-- Command
    Machine --> Command : exposes
    Operation <|-- Workflow
    Operation <|-- Case
    Operation <|-- Procedure
    Environment --> Signal : produces
    Machine --> Signal : produces
    Sensors --> Signal : produces
    Signal --> Trigger : sensed by
    Trigger --> Request : creates
    Request --> Scenarios : activates
    Signal <|-- Request
    Domain -- Environment : interacts
    Domain --> Business_Entity : contains
    Workbench --> Domain : interprets
    Workbench --> Scenarios : contains
    Workbench --> Trigger : contains
    Workbench --> Task_Queue : has
    Workbench --> Tool_Registry : references
    Workbench --> Machine_Registry : references
    Workbench --> Knowledge_Base : has
    Workbench --> Agent : enrolls
    Machine --> Business_Entity : manages
    Operation --> Business_Entity : acts upon
    Role --> Goal : has
    Goal --> SOP : addressed by
    SOP --> Operation : governs
    Knowledge_Base --> SOP : contains
    Knowledge_Base --> Runbook : contains
    Knowledge_Base --> Checklist : contains
    Runbook --> Task : guides
    Checklist --> Signal : generates
    Responsibility --> Role : contributes to
    Capability --> Responsibility : fulfills
    Agent --> Capability : enabled by
    Agent --> Capacity : limited by
    Decision --> Goal : supports
    Information_Element --> Decision : informs
    Data_Element --> Information_Element : feeds
    Scenarios --> Role : involves
    Scenarios --> Goal : references
    Agent --> Role : plays
    Agent --> Capability : has
    Role --> Procedure : executes
    Responsibility --> Procedure : determines
    Operation --> Activity : prescribes
    Activity --> Task : some become
    Task --> Agent : assigned to
    Task --> Task_Queue : queued in
    Task --> Escalation : governed by
    Escalation --> Task_Queue : references
    Task_Queue --> Role : associated with
    Activity --> Action : consists of
    Agent --> Activity : performs
    Workflow --> Procedure : binds deterministically
    Case --> Procedure : aggregates non-deterministically
    Case --> Signal : may update with
    Case --> Agent : collaboration between
    Training --> SOP : may reference
    Human_AI_Team --> Agent : groups
    Scenarios --> Automation : invokes
    Automation --> Operation : instantiates
    Operation --> Activity : prescribes
    Automation_System --> Automation : runs/manages
    Automation_System --> Operation : supervises
    Agent --> Command : uses
    Tool_Registry --> Tool : catalogs
    Machine_Registry --> Machine : catalogs
    Human_AI_Team --> Automation_System : interacts
    Observe --> Signal : materializes as
    Predict --> SOP : based on knowledge
    Predict --> Prediction_Application : aided by
    Decide --> SOP : based on knowledge
    Decide --> Decision_Application : aided by
    Decide --> Decision : realizes
    Agent --> Tool : uses

	class Operation:::Rose
	class Agent:::Peach
	class Human:::Peach
	class AI_Agent:::Peach
	class Workbench:::Mint
	class Task_Queue:::Mint
	class Tool_Registry:::Mint
	class Machine_Registry:::Mint

	classDef Rose :,stroke-width:1px, stroke-dasharray:none, stroke:#FF5978, fill:#FFDFE5, color:#8E2236
	classDef Peach :,stroke-width:1px, stroke-dasharray:none, stroke:#FBB35A, fill:#FFEFDB, color:#8F632D
	classDef Mint :,stroke-width:1px, stroke-dasharray:none, stroke:#36B37E, fill:#E3FCEF, color:#006644

```

---

## Mermaid Ontology Graph

This diagram shows the relationships between all ontology concepts, organized by layer.

```mermaid
graph TD
%% Perception Layer - Domain & Workbench
Domain --contains--> Business_Entity
Workbench --interprets--> Domain
Workbench --contains--> Scenario
Workbench --contains--> Trigger
Workbench --has--> Task_Queue
Workbench --references--> Tool_Registry
Workbench --references--> Machine_Registry
Workbench --has--> Knowledge_Base
Workbench --enrolls--> Agent
Machine --manages--> Business_Entity
Operation --acts upon--> Business_Entity

%% Signal Flow
Signal --sensed by--> Trigger
Trigger --creates--> Request
Request --activates--> Scenario
Request --is a--> Signal
Scenario --invokes--> Automation
Automation --instantiates--> Operation
Operation --prescribes--> Activity
Activity --some become--> Task
Task --assigned to--> Agent
Task --queued in--> Task_Queue
Task --governed by--> Escalation
Escalation --references--> Task_Queue
Task_Queue --associated with--> Role
Activity --consists of--> Action

%% Operation Types
Operation --abstract type--> Workflow
Operation --abstract type--> Case
Operation --abstract type--> Procedure

%% Roles & Goals
Scenario --involves--> Role
Role --has--> Goal
Role --executes--> Procedure
Agent --plays--> Role
Agent --performs--> Activity

%% Normative Layer
Goal --addressed by--> SOP
SOP --governs--> Operation
Knowledge_Base --contains--> SOP
Knowledge_Base --contains--> Runbook
Knowledge_Base --contains--> Checklist
Runbook --guides--> Task
Checklist --generates--> Signal

%% Workflows & Cases
Workflow --binds deterministically--> Procedure
Case --aggregates non-deterministically--> Procedure
Case --may update with--> Signal
Case --collaboration between--> Agent

%% Automation Layer
Automation_System --runs/manages--> Automation
Automation_System --supervises--> Operation

%% Responsibilities & Capabilities
Role --composed of--> Responsibility
Responsibility --contributes to--> Role
Responsibility --fulfilled by--> Capability
Responsibility --determines--> Procedure
Capability --fulfills--> Responsibility
Agent --enabled by/has--> Capability
Capacity --limits--> Agent

%% Decisions
Decision --supports--> Goal
Information_Element --informs--> Decision
Data_Element --feeds--> Information_Element

%% OPD Elements
Observe --materializes as--> Signal
Predict --based on--> SOP
Predict --aided by--> Prediction_Application
Decide --based on--> SOP
Decide --aided by--> Decision_Application
Decide --realizes--> Decision

%% Tools & Registries
Agent --uses--> Tool
Tool --abstract type--> Prediction_Application
Tool --abstract type--> Decision_Application
Tool --abstract type--> Command
Machine --exposes--> Command
Tool_Registry --catalogs--> Tool
Machine_Registry --catalogs--> Machine
```

---

## How to Read These Diagrams

### Class Diagram Notation
- **Solid arrows with triangles (`<|--`)**: Inheritance (e.g., `Human` inherits from `Agent`)
- **Solid arrows (`-->`)**: Relationship with label
- **Dashed lines (`--`)**: Association
- **`<<abstract>>`**: Abstract type that must be specialized

### Ontology Graph Notation
- **Arrows with labels**: Directed relationships
- **Comments (`%%`)**: Section headers for clarity

---

**Navigation:** [← Automation Layer](./ontology-4-automation-layer.md) | [Ontology Reference](./ontology-reference.md)

