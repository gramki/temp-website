# Scenario-Oriented Thinking: Core Concepts

> **Status**: 🟢 Design Complete  
> **Target Audience**: Process Architects, Developers  
> **Purpose**: Comprehensive understanding of scenario-oriented thinking foundations, concepts, and specifications

---

## Table of Contents

1. [Conceptual Foundations: DDD and AOSM](#conceptual-foundations-ddd-and-aosm)
2. [What is Scenario-Oriented Thinking?](#what-is-scenario-oriented-thinking)
3. [Core Concepts](#core-concepts)
4. [The Three Specifications](#the-three-specifications)

---

## Conceptual Foundations: DDD and AOSM

Scenario-Oriented Thinking isn't invented from scratch. It builds on two established conceptual frameworks that address long-standing problems in business process automation:

- **Domain-Driven Design (DDD)** — for modeling business domains with clear boundaries and shared language
- **Agent-Oriented Systems Modeling (AOSM)** — for modeling work as performed by agents (human and AI) with roles, goals, and judgment

### Domain-Driven Design (DDD) Foundations

| DDD Concept | Scenario Model Equivalent | What It Addresses |
|-------------|--------------------------|-------------------|
| **Bounded Context** | Domain / Workbench | Clear boundaries; each domain has its own language, rules, and entities |
| **Ubiquitous Language** | Normative Specification | Business and technical teams share vocabulary; scenarios named in business terms |
| **Domain Events** | Signals | Events that indicate something happened; triggers for scenarios |
| **Aggregates** | Scenarios | Cohesive operational units with clear boundaries; consistency scope |

**Why this matters:**

DDD addressed a core problem: **business domains get lost in technical implementation**. When business concepts are translated into code, the translation introduces drift. DDD's answer was: keep business concepts explicit, use the same language across business and technical teams, and maintain clear boundaries.

Scenario-Oriented Thinking applies these principles:
- **Scenarios ARE business situations** — not technical workflow diagrams
- **Normative specs use business language** — stakeholders can read and validate them
- **Domain boundaries are explicit** — integration across domains is deliberate, not accidental

### Agent-Oriented Systems Modeling (AOSM) Foundations

| AOSM Concept | Scenario Model Equivalent | What It Addresses |
|--------------|--------------------------|-------------------|
| **Agent** | Human / AI Agent | Performer of work — not just a box in a flowchart |
| **Role** | Normative Spec Roles | Responsibilities, not just task assignments |
| **Goal** | Scenario Goals | Outcomes to achieve, not just steps to complete |
| **Capability (KSA)** | Agent Capabilities | Knowledge, Skills, Abilities that agents bring |
| **Autonomy** | Operating Modes | How much discretion an agent has in a context |
| **PIDA Cycle** | Perceive, Interpret, Decide, Act | How agents engage with work |

**Why this matters:**

Traditional BPM treats humans as **task executors** — a box in the diagram that "completes" a task and moves to the next step. This misses what humans actually do:

| Traditional View | AOSM View |
|------------------|-----------|
| Human = task box | Human = agent with judgment |
| Human "completes" tasks | Human exercises discretion, collaborates, escalates |
| Any analyst can handle any case | Expertise matters; capabilities differ |
| Process defines what human does | Agent has goals, autonomy within guidelines |

**This isn't just about AI.** Whether your process involves humans, AI, or both, AOSM provides a richer model:

- **Humans as agents with judgment** — not interchangeable resources
- **Roles with responsibilities** — not just task assignments
- **Goals and autonomy** — "achieve this outcome within these guidelines"
- **Collaboration and escalation** — first-class concepts, not workarounds

### Hard Problems These Foundations Solve

These aren't theoretical concerns. They're pain points that process automation practitioners face repeatedly.

#### The "Lost in Translation" Problem

```
Business requirements → Technical specs → Code → Drift → "Why does it do this?"
```

**The pain:** Every translation loses fidelity. By the time requirements become code, the business intent is buried. When rules need to change, no one knows where they are.

**How DDD + Normative-First addresses it:**
- Ubiquitous language — same terms across business and tech
- Normative spec IS the authoritative source — not a translated artifact
- Scenarios named in business language — stakeholders recognize and validate them

#### The "Who Does What" Problem

**The pain:** Unclear responsibilities. "I thought you were handling that." Escalation confusion. Accountability gaps. Informal workarounds that no one documents.

**How AOSM + Normative Spec addresses it:**
- Explicit role definitions in normative spec
- RASCI-like assignment — who decides, who executes, who reviews
- Escalation rules as first-class specification, not afterthoughts
- Accountability is designed, not discovered after failures

#### The "Human as Task Box" Problem

**The pain:** Process models treat humans as interchangeable task executors. But in reality:
- Some cases need senior expertise
- Humans exercise judgment, not just follow steps
- Collaboration happens informally, outside the process model
- "Use judgment within guidelines" is hard to express

**How AOSM addresses it:**
- Humans are agents with capabilities, not task boxes
- Roles carry goals and autonomy levels
- Discretion is modeled — "resolve within SLA, escalate if X"
- Expertise matching — not all analysts are equal

#### The "Everything Depends on Everything" Problem

**The pain:** Changes cascade unpredictably. Modifying one rule breaks three others. Can't evolve domains independently.

**How DDD's Bounded Contexts + Domain Isolation addresses it:**
- Clear domain boundaries
- Explicit integration between domains — deliberate, not accidental
- Change within a domain doesn't cascade
- Each domain has its own scenarios, entities, knowledge

#### The "Why Does It Do This" Problem

**The pain:** Business logic buried in code. No traceability to requirements. When audit asks "what are the rules?", no one knows without reading code.

**How Normative-First + Goal Orientation addresses it:**
- Goals are explicit in normative spec
- Decision criteria documented, not buried
- Traceability: automation derives from normative
- The normative spec IS the documentation

### When These Foundations Add Most Value

| Context | Value |
|---------|-------|
| **Complex, multi-role processes** | Roles, goals, escalation need explicit modeling |
| **Human discretion is significant** | AOSM's agent model captures judgment, not just task completion |
| **Multiple domains interact** | DDD boundaries prevent coupling |
| **Audit and compliance matter** | Normative as source of truth provides traceability |
| **Processes evolve over time** | Structured specifications enable sustainable change |

| Context | Value May Be Lower |
|---------|-------------------|
| **Simple, single-step automation** | Overhead may not pay off |
| **Single person owns everything** | Formal role separation adds coordination cost |
| **Truly one-off scripts** | Structure is investment in evolution |

**The honest assessment:** The richer model isn't always necessary. But the problems it solves — translation drift, unclear responsibilities, humans as task boxes, domain coupling — are common enough that most non-trivial processes benefit.

---

## What is Scenario-Oriented Thinking?

### The Core Idea

**Scenario-Oriented Thinking** is a way of modeling business operations as **situational responses** rather than **sequential workflows**.

Instead of asking: *"What steps does this process have?"*

Ask: *"What situations does my business need to respond to, and how should each be handled?"*

### Traditional Process Thinking

```
Process: Dispute Resolution
├── Step 1: Receive dispute
├── Step 2: Investigate
├── Step 3: Make decision
├── Step 4: Notify customer
└── Step 5: Close case
```

**Characteristics:**
- Sequential steps
- Single path (or branching paths)
- Technology-agnostic procedure
- One definition covers all cases

### Scenario-Oriented Thinking

```
Domain: Dispute Resolution

Scenario: "Standard Dispute"
  → Routine case, clear rules, automated decision

Scenario: "High-Value Dispute"  
  → Requires analyst review, evidence gathering, human decision

Scenario: "Fraud Dispute"
  → Security team involvement, investigation, escalation path
```

**Characteristics:**
- Situational contexts
- Each scenario has distinct handling
- Roles, goals, and automation vary by scenario
- Business stakeholders recognize these as real situations

### Why This Matters

| Aspect | Traditional Process | Scenario-Oriented |
|--------|---------------------|-------------------|
| **Business alignment** | Technical workflow | Matches how stakeholders think about situations |
| **Situation recognition** | One process covers all | Distinct situations are explicitly modeled |
| **Measurement** | Process-level metrics | Scenario-level metrics |
| **Evolution** | Change affects everything | Change one scenario independently |
| **Automation choice** | Decided upfront | Derived later, often by AI |

---

## Core Concepts

### Scenario

A **Scenario** is a recognizable operational situation that your organization must respond to.

**Key characteristics:**
- Represents a distinct situation or problem
- Triggered by a signal (event, request, time) that indicates this situation
- Is recognizable to business stakeholders as a real situation
- Has a defined response (roles, goals, actions) — but the response is DERIVED from the situation, not what defines it

**Examples:**

| Domain | Scenario Examples | Why These Are Distinct Scenarios |
|--------|-------------------|----------------------------------|
| **Disputes** | Standard Dispute, High-Value Dispute, Fraud Dispute | Different roles, SLAs, compliance requirements |
| **Onboarding** | Individual Account, Business Account, Regulated Entity | Different verification, documentation, approval flows |
| **Payments** | Domestic Payment, International Transfer, High-Risk Payment | Different compliance, processing rules, approvals |
| **Support** | Simple Inquiry, Technical Issue, Formal Complaint | Different nature of problem, different signals |

**Note:** Each scenario represents a **fundamentally different situation** that business stakeholders recognize. Within each scenario, there are many decision rules (amount thresholds, customer risk levels, etc.) — those are NOT separate scenarios.

### Signal

A **Signal** is what triggers a scenario. It's the event or condition that initiates a response.

**Signal types:**
- **External event:** Customer action, partner message, regulatory notice
- **Internal event:** System alert, threshold crossed, status change
- **Time-based:** Scheduled check, deadline approaching, periodic review
- **Manual:** Human initiates a case

### Request

A **Request** is an instance of a scenario being handled. When a signal matches a scenario, a request is created.

```
Signal: "Dispute filed for $500 on Merchant ABC"
  ↓
Matches: "Standard Dispute" scenario
  ↓
Creates: Request #12345
  ↓
Handled according to scenario specifications
```

---

## The Three Specifications

Each scenario has three complementary specifications, each addressing a different concern:

### Normative Specification

**Owner:** Process Architect  
**Focus:** What ought to be done

**Contains:**
- **Roles:** Who is involved (analyst, supervisor, customer)
- **Goals:** What must be achieved (resolve within 24h, document decision)
- **SOPs:** Standard operating procedures to follow
- **Decision criteria:** Rules for making decisions
- **Evidence requirements:** What documentation is needed
- **Escalation rules:** When and how to escalate
- **Compliance requirements:** Regulatory constraints

**Example:**
```yaml
scenario: standard-dispute
normative:
  roles:
    - dispute-analyst
    - supervisor (escalation only)
  goals:
    - Resolve within 24 hours
    - Document decision with rationale
  decision_criteria:
    - Amount < $1000: Auto-approve if merchant history clean
    - Amount >= $1000: Analyst review required
  escalation:
    - If unresolved after 20h: Escalate to supervisor
```

### Automation Specification

**Owner:** Developer  
**Focus:** How it's automated

**Contains:**
- **Application:** What code/system handles this
- **Runtime:** What type of automation (rules, workflow, AI agent, hybrid)
- **Triggers:** How signals are routed to this scenario
- **Tool bindings:** What external systems are used
- **Data access:** What information is needed

**Example:**
```yaml
scenario: standard-dispute
automation:
  application: dispute-handler
  runtime: chronoshift  # Long-running case management
  triggers:
    - signal_type: dispute-filed
      conditions:
        amount: { lt: 1000 }  # Routes to this scenario; >= 1000 routes to high-value-dispute
  tools:
    - core-banking
    - merchant-gateway
    - notification-service
```

**Trigger conditions vs. decision rules:**
- **Trigger conditions** (in automation spec): Determine WHICH scenario handles a signal
- **Decision rules** (in normative spec): Define decisions WITHIN a scenario

The amount threshold here routes the dispute to the right scenario. Once in Standard Dispute, the normative spec's decision criteria handle further logic (auto-resolve vs. analyst review, etc.).

### Deployment Specification

**Owner:** Supervisor  
**Focus:** How it's deployed and operated

**Contains:**
- **Task queues:** Where work items land
- **Agent enrollment:** Who/what handles tasks
- **SLA parameters:** Response time, resolution time
- **Activation settings:** Enabled/disabled, percentage rollout
- **Operational overrides:** Time-of-day rules, holiday handling

**Example:**
```yaml
scenario: standard-dispute
deployment:
  task_queue: dispute-analyst-queue
  sla:
    response_time: 4h
    resolution_time: 24h
  agents:
    - dispute-analyst-team
    - dispute-ai-assistant (support role)
  activation:
    enabled: true
    rollout_percentage: 100
```

### Why Three Specifications?

**Separation of Concerns:**
- Business rules (normative) can change without touching code (automation)
- Automation can evolve without changing operational settings (deployment)
- Each persona owns their domain

**Independent Evolution:**
- Update SOPs without redeploying applications
- Change automation approach without changing business rules
- Adjust operational settings without code changes

**Clear Ownership:**
- Process Architect owns "what should happen"
- Developer owns "how it's implemented"
- Supervisor owns "how it's operated"

---

## Related Documentation

- [Entry Point](./scenario-oriented-thinking.md) — Overview and reading guide
- [The Core Argument](./scenario-oriented-thinking-argument.md) — Why this paradigm shift matters
- [Examples](./scenario-oriented-thinking-examples.md) — Concrete use cases
- [Adoption Guide](./scenario-oriented-thinking-adoption.md) — How to get started

---

[← Back to Entry Point](./scenario-oriented-thinking.md)
