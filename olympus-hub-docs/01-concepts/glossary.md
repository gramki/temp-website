# Hub Glossary — Foundational Terms

> **Purpose:** Define key terminology that bridges Hub's concepts to broader industry language.

---

## Information-Centric Work

**Definition:** Work where the primary inputs, transformations, and outputs are information rather than physical matter.

### Characteristics

| Dimension | What It Includes |
|-----------|------------------|
| **Inputs** | Data, documents, signals, requests, specifications, requirements |
| **Transformation** | Analysis, interpretation, decision-making, synthesis, design, composition |
| **Outputs** | Decisions, records, communications, documents, code, applications |

### Examples of Information-Centric Work

- Processing a request and making a disposition decision
- Translating requirements into a design or implementation
- Drafting, reviewing, and approving documents or code
- Investigating an issue and determining root cause
- Coordinating between parties to resolve a problem
- Synthesizing information into recommendations or artifacts

### Software Development as Information-Centric Work

Software development is quintessentially information-centric work:

| Dimension | In Software Development |
|-----------|-------------------------|
| **Inputs** | Requirements, specifications, designs, existing code, bug reports — all information |
| **Transformation** | Understanding, reasoning, designing, coding, testing — all cognitive/analytical activities |
| **Outputs** | Code, tests, documentation, applications — all information artifacts |

**Key characteristics:**
- No physical material is transformed at any stage
- The "product" (software) is itself an information artifact
- Software can be copied infinitely at zero marginal cost — it's not a physical good
- All work patterns match information-centric patterns: processing requests, decision-making, coordination, documentation

### Contrast: Physical-Centric Work

| Dimension | Information-Centric | Physical-Centric |
|-----------|---------------------|------------------|
| **Inputs** | Data, documents, signals | Raw materials, components |
| **Transformation** | Cognitive, analytical | Mechanical, chemical |
| **Outputs** | Decisions, records, code | Physical products |
| **Primary medium** | Information | Matter |

### Agency in Information-Centric Work

When we say "agency is not essential," we refer to Scenario resolution, not Scenario definition. The normative layer — goals, SOPs, decision criteria, escalation rules — always requires cognitive faculties to create. What may not require agency is the resolution of situations that have been observed, learned, or accepted as sufficiently repeatable that machines can handle them. Over time, what requires agency shifts: novel situations become understood, and understood situations become automatable.

**Key points:**

- Many situations in information-centric work are repeatable and can be resolved entirely by machines
- Agency (human or AI involvement) is often needed for judgment, exceptions, novel situations — but not always
- Hub provides the same infrastructure (governance, audit, memory) regardless of whether agents are involved
- Traditional models try to eliminate agents for cost; Hub is agnostic to resolution model
- The evolution: novel situations → understood → automatable

**Evolution of Agency Requirements:**

```
Novel Situation          Understood Situation         Automatable Situation
     │                          │                            │
     ▼                          ▼                            ▼
Agency Essential ───────→ Agency Helpful ───────→ Agency Optional
(Cognitive work)          (Supervision/review)     (Exception only)
     │                          │                            │
     └──────────────────────────┴────────────────────────────┘
                    Learning and formalization
```

---

## Resolution Model

**Definition:** The pattern of participation between Machines and Agents in resolving a Scenario. It describes *who/what* resolves the work, not *what kind* of work it is (that's the Work Pattern).

> **Note:** This may also be referred to as "Execution Model" in some contexts. Hub uses "Resolution Model" to emphasize the goal-oriented nature of Scenario resolution.

| Resolution Model | Description | Agent Role | Example |
|------------------|-------------|------------|---------|
| **Pure Automation** | Machines resolve entirely; no agent involvement | None | ETL job, scheduled report generation |
| **Automation with Exception Escalation** | Machines resolve; agents engage only for business exceptions | Exception handling | Data reconciliation with conflict resolution |
| **Automation with Checkpoint Approval** | Machines resolve; agents approve at defined points | Gate approval | Payment batch processing with threshold approval |
| **Agent-Assisted Automation** | Automation does the work; agents guide, review, or correct | Guidance, review | AI-drafted document with human editing |
| **Human-AI Teaming** | Human and AI agents collaborate throughout | Co-resolution | Complex case investigation with AI research |
| **AI-Autonomous** | AI agents operate independently within governance | Primary resolver | Automated customer inquiry resolution |
| **Human-Supervised AI** | AI proposes; humans approve each action | Approval per action | High-risk financial decisions |
| **Pure Human Collaboration** | Humans work together; platform provides infrastructure | Primary resolver | Strategy session, creative brainstorming |
| **Human with Tool Support** | Human resolves; machines provide capabilities on demand | Primary resolver with tools | Analyst using data queries and calculators |

**Machines as Implicit Infrastructure:**

All resolution models may involve Machines providing capabilities (tools, commands, data access). The model describes the primary actors making decisions and driving resolution, not every participant. Machines are infrastructure for resolution, not actors in resolution.

**Resolution Model × Work Pattern:**

Resolution Model describes *who/what* resolves the work. Work Pattern describes *what kind* of work it is. Together, they define how work actually happens:
- A Queue-Based work pattern can be resolved through Pure Automation (machines process items) or Human-AI Teaming (agents collaborate on complex items)
- A Case-Based work pattern typically requires Human-AI Teaming or AI-Autonomous resolution, but may include automated segments

---

## Collaboration and Integration — A Terminology Bridge

Hub unifies traditional enterprise concepts under a single collaboration model. This table maps common terminology to Hub's unified view:

| Traditional Term | Traditional Meaning | Hub Equivalent |
|------------------|---------------------|----------------|
| **Integration** | Machine-to-Machine communication (APIs, ETL, data sync) | Machine-Machine collaboration |
| **Collaboration** | Humans working together, or humans with systems | Agent-Agent collaboration |
| **Orchestration** | Coordinating multiple systems/services | Scenario with multiple Machines and/or Agents |
| **Workflow** | Human task routing | One resolution pattern within a Scenario |

**Key points:**

- In Hub, all are forms of "collaboration" — entities working together toward a goal
- What's traditionally called "integration" is Machine-Machine collaboration in Hub
- Hub provides unified infrastructure regardless of participant types
- Enterprise architects can see their integration patterns as Hub Scenarios

---

## Operation

**Definition:** A situation in information-centric work that needs attention, decision, or action.

### The Core Statement

> All operations in information-centric work are situations that need attention, decision, or action. Hub models each such operation as a **[Scenario](../02-system-design/implementation-concepts/scenario-specification-types.md)**.

### Examples

| Operation (Situation) | What Needs to Happen | Hub Scenario |
|-----------------------|----------------------|--------------|
| A loan application arrived | Assess eligibility, make decision | Loan Assessment |
| A production incident occurred | Diagnose, mitigate, resolve | Incident Response |
| A feature needs to be implemented | Design, build, test, deploy | Feature Development |
| A customer complaint was filed | Investigate, resolve, respond | Complaint Resolution |
| Code changes need review | Evaluate quality, approve/reject | Code Review |

### Relationship to Scenario

**Operation** is the situation that needs attention.
**[Scenario](../02-system-design/implementation-concepts/scenario-specification-types.md)** is Hub's model for that operation — goal-oriented, not procedure-oriented.

This allows natural usage:
- "Hub is an operational platform" — a platform for handling operations
- "Operations Center" — where you work on operations
- "Scenario" — the specific Hub concept for modeling an operation

---

## Scenario

**Definition:** Hub's model for an operation — a goal-oriented definition of what needs to be achieved, not a step-by-step procedure.

### Key Characteristics

| Characteristic | What It Means |
|----------------|---------------|
| **Goal-oriented** | Defines outcomes to achieve, not steps to follow |
| **Situation-based** | Represents a recognizable business situation |
| **Agent-executed** | Humans and AI agents determine how to achieve the goals (though resolution may not require agents) |
| **Three specifications** | Normative (what), Automation (how), Deployment (where) |

### How Scenarios Differ from Workflows

| Traditional Workflow | Hub Scenario |
|---------------------|--------------|
| Defines the steps | Defines the goal |
| Prescribes the sequence | Prescribes the constraints |
| Human executes the flow | Agent achieves the outcome |
| Exceptions are errors | Exceptions are variations |

### The Three Specifications

Every Scenario is defined by three complementary specifications:

1. **Normative Specification** — What ought to be done (roles, goals, SOPs, decision criteria)
2. **Automation Specification** — How it's automated (triggers, applications, tools)
3. **Deployment Specification** — How it's deployed (queues, SLAs, activation)

→ See [Scenario Specification Types](../02-system-design/implementation-concepts/scenario-specification-types.md) for details.

---

## Operational Platform

**Definition:** A platform for modeling, managing, and automating operations in information-centric work.

### What This Means for Hub

Olympus Hub is an operational platform that:

1. **Models operations as Scenarios** — goal-oriented definitions, not rigid procedures
2. **Manages operations through Requests** — collaboration surfaces where agents work together
3. **Automates operations via Hub Applications** — codified logic that handles routine work
4. **Enables governed collaboration** — human and AI agents working together with structure, memory, and governance

### Why "Operational Platform" (Not "Infrastructure Platform")

Hub provides more than infrastructure. It provides:

| Dimension | What Hub Offers |
|-----------|-----------------|
| **Scenario-Oriented Operations** | Scenarios define goals; Requests are collaboration surfaces |
| **Domain Encapsulation** | Workbenches isolate business domains |
| **Resolution Spectrum** | Pure automation through human collaboration; see [Resolution Model](#resolution-model) |
| **Persona-Channel Framework** | Multi-surface access (Web, Teams, MCP, REST) |
| **Automation Platform** | Hub Applications, Machines, Runtimes |
| **Infrastructure Foundation** | Context, structure, memory, governance |

"Infrastructure" captures only the last dimension. "Operational platform" captures the full scope.

---

## Related Concepts

| Term | Definition | Where Defined |
|------|------------|---------------|
| **Request** | An instance of a Scenario; a collaboration surface where agents work together | [Request Lifecycle](../02-system-design/implementation-concepts/request-lifecycle.md) |
| **Workbench** | Hub's unit of domain encapsulation; contains scenarios, agents, knowledge, memory | [Workbench Anatomy](../02-system-design/workbench-anatomy.md) |
| **Hub Agent** | A participation pattern for any entity that handles work in Hub | [Agent Model](../02-system-design/agent-model.md) |
| **Hub Application** | Automation artifact that implements scenario logic | [Hub Application](./hub-applications.md) |

---

*This glossary defines foundational terms. For the complete ontology, see [Ontology Reference](./ontology-reference.md).*
