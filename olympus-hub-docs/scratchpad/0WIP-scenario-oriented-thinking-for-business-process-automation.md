# Scenario-Oriented Thinking for Business Process Automation

> **Status:** 🟡 Draft — Outline  
> **Audience:** Automation Product Owners, Process Architects, Developers  
> **Purpose:** Help teams think about business process automation in terms of Scenarios

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Conceptual Foundations: DDD and AOSM](#2-conceptual-foundations-ddd-and-aosm) — What established theories ground this model
3. [What is Scenario-Oriented Thinking?](#3-what-is-scenario-oriented-thinking)
4. [Core Concepts](#4-core-concepts)
5. [The Three Specifications](#5-the-three-specifications)
6. [Benefits](#6-benefits-of-scenario-oriented-thinking) — Normative-first, AI-ready, evolution without debt
7. [Trade-offs](#7-trade-offs-and-what-this-model-requires) — What this model requires
8. [**The Core Argument**](#8-the-core-argument-why-this-paradigm-shift-matters) — Why this paradigm shift matters *(central thesis)*
9. [Comparison with Alternatives](#9-comparison-with-alternative-approaches) — BPM, Low-Code, Temporal, Custom Code
10. [Every Process Needs This](#10-every-process-needs-this-model) — Why even "simple" processes benefit
11. [Adoption and Migration](#11-adoption-and-migration)
12. [Conclusion](#12-conclusion)

---

## 1. Introduction

### Purpose of This Document

This guide helps **Automation Product Owners (APOs)**, **Process Architects (PAs)**, and **Developers** understand and apply **scenario-oriented thinking** when designing business process automation.

### What This Document Covers

- The conceptual model of scenario-oriented thinking
- How to identify and design scenarios
- The three-specification model (normative, automation, deployment)
- Why normative specifications are the center of gravity
- How this model prepares for AI-assisted automation

### What This Document Does NOT Cover

- Hub platform specifics (workbenches, promotion, development workflow)
- For Hub implementation details, see [Hub Development Flow Guide](../../10-guides/hub-development-flow/README.md)

### Who Should Read This

| Persona | What You'll Gain |
|---------|------------------|
| **Automation Product Owner** | Framework for identifying automation opportunities as scenarios |
| **Process Architect** | Model for designing business processes with clear specifications |
| **Developer** | Understanding of how automation requirements are structured |

---

## 2. Conceptual Foundations: DDD and AOSM

Scenario-Oriented Thinking isn't invented from scratch. It builds on two established conceptual frameworks that address long-standing problems in business process automation:

- **Domain-Driven Design (DDD)** — for modeling business domains with clear boundaries and shared language
- **Agent-Oriented Systems Modeling (AOSM)** — for modeling work as performed by agents (human and AI) with roles, goals, and judgment

### 2.1 Domain-Driven Design (DDD) Foundations

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

### 2.2 Agent-Oriented Systems Modeling (AOSM) Foundations

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

### 2.3 Hard Problems These Foundations Solve

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

### 2.4 When These Foundations Add Most Value

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

## 3. What is Scenario-Oriented Thinking?

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

## 4. Core Concepts

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

## 5. The Three Specifications

Each scenario has three complementary specifications, each addressing a different concern:

### 5.1 Normative Specification

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

### 5.2 Automation Specification

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

### 5.3 Deployment Specification

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

## 6. Benefits of Scenario-Oriented Thinking

### 6.1 Normative as Source of Truth

**Business rules are explicit and authoritative:**
- Normative specification captures what should happen — not as a side document, but as the source
- Rules don't hide in code, emails, or people's heads
- When rules change, the normative spec changes — automation follows

**AI-ready structure:**
- AI agents need structured input to generate automation
- Normative specs provide: goals, roles, decision criteria, SOPs, compliance rules
- Derivation becomes possible: normative → generated automation

**Drift is minimized:**
- Traditional: requirements in docs, rules in code → drift apart
- Scenario model: automation derives from normative → stays aligned
- Changes flow: business updates normative → agents regenerate/update automation

### 6.2 Business Alignment

**Scenarios match business understanding:**
- Business thinks in situations: "When a high-value dispute comes in..."
- Scenarios ARE those situations — not abstract workflow diagrams
- Stakeholders recognize and validate scenarios directly

**Clear ownership:**
- Business owns what should happen (normative)
- Technical owns how it's implemented (automation)
- Operations owns how it runs (deployment)
- No confusion about who decides what

### 6.3 Evolution Without Debt

**Processes change. This model handles it:**
- Regulations change → update normative, regenerate automation
- Business rules change → update normative, not code
- Operational needs change → update deployment, not automation

**Compare to hardwired code:**
- Change means: find the code, understand it, modify it, test it, deploy it
- Knowledge lost when developers leave
- Fear of changing anything → legacy burden

**With scenario model:**
- Change means: update the specification, derivation handles the rest
- Knowledge is in the specs, not people's heads
- Evolution is sustainable

### 6.4 Multi-Approach Automation

**Same model, different runtimes:**
- Some scenarios suit rule-based automation
- Some scenarios suit workflow orchestration
- Some scenarios suit AI agents
- Some scenarios need human handling

**Why this matters:**
- You don't pick one automation approach for everything
- Each scenario gets the right approach
- AI agents can handle more scenarios over time — the model doesn't change

### 6.5 Measurability and Traceability

**Natural boundaries:**
- Metrics per scenario (SLA compliance, throughput, cost)
- Clear attribution: which scenario handled this request?
- Audit scope is scenario-level, not system-level

**Improvement is targeted:**
- Identify underperforming scenarios
- Improve specific scenarios without touching others
- A/B test at scenario level

---

## 7. Trade-offs and What This Model Requires

### 7.1 Upfront Structure

**You must design normative specs explicitly:**
- This isn't "just write code and ship it"
- Business rules, roles, goals, SOPs must be captured
- Upfront effort before automation begins

**Why this is worth it:**
- The alternative is rules buried in code, undocumented, unmaintainable
- The upfront structure enables AI-assisted derivation
- Evolution becomes sustainable, not a rewrite

**When this feels heavy:**
- One-off scripts that will never change (but are they really one-off?)
- Prototypes and experiments (but will they become production?)
- Be honest: most "simple" processes eventually need to evolve

### 7.2 Scenario Boundary Decisions

**Scenarios are identified by WHAT situation they represent, not HOW they're handled.**

The key question is: **What problem or situation are we sensing?**

| Right Approach | Wrong Approach |
|---------------|----------------|
| "What situation is this?" | "How do we handle this?" |
| "What signal indicates this situation?" | "What processing steps are different?" |
| Identified by the nature of the problem | Identified by implementation differences |

**The test:**
- Different situation (e.g., fraud indicator vs. standard dispute) → different scenarios
- Same situation, different parameters (e.g., amount thresholds) → same scenario, different rules

**Why this matters:**
- Scenario-oriented thinking separates WHAT from HOW
- You identify scenarios based on the situation, not the solution
- HOW it's solved (BPM, rules, AI, workflow) is the automation spec — derived later, often by AI
- Focusing on "how we handle it" puts the cart before the horse

### 7.3 Three Personas, Three Specifications

**Coordination is required:**
- Process Architect, Developer, Supervisor must communicate
- Changes spanning specifications need alignment
- More structured than "developer owns everything"

**But consider the alternative:**
- Developer owns everything → business rules in code → business can't change rules without developer
- No separation → no clear ownership → confusion about who decides what
- The coordination cost is the cost of clear ownership

### 7.4 Discipline to Maintain Specifications

**Specifications must be kept current:**
- If normative specs become stale, the benefit disappears
- If automation diverges from normative, you're back to drift

**How AI changes this:**
- When automation is derived from normative, drift is harder
- Changes to normative trigger regeneration
- The discipline becomes: keep normative accurate, not: keep code and docs in sync

---

## 8. The Core Argument: Why This Paradigm Shift Matters

### The Problem with Current Automation Platforms

**All automation platforms focus on HOW to automate, leaving out:**
- **WHY** — the purpose, the problem being solved
- **WHAT** — the situation, the goals to be achieved

BPM gives you workflow orchestration. Low-code gives you visual flow builders. Temporal gives you durable execution. All assume you know WHAT you want — they help with HOW.

**But where does the WHAT live?**
- In requirements documents that get written once and forgotten
- In analysts' heads
- In emails and meeting notes
- Eventually, buried in code as implementation details

**To leverage AI effectively, we must fundamentally change the approach:** Put the normative (WHY, WHAT, goals) at the center. Let AI handle the HOW.

---

### Why This Matters Now

#### 1. AI Needs Structured Input to Generate Automation

AI can write code. But from WHAT input?

| Current State | Problem |
|---------------|---------|
| Requirements in Confluence | AI can't reliably extract intent |
| Rules in people's heads | AI has no access |
| Business logic in scattered emails | No structured input |
| SOPs in PDF documents | Not machine-actionable |

Structured normative specifications give AI what it needs:
- Clear goals
- Explicit decision criteria
- Defined roles and responsibilities
- Compliance constraints

**Without normative specs, AI-generated automation is guesswork. With them, it's derivation.**

#### 2. The Bottleneck is Shifting

| Era | Bottleneck | Platform Focus |
|-----|------------|----------------|
| **Pre-automation** | Manual execution | Digitize processes |
| **Early automation** | Coding is expensive | Make coding easier (BPM, workflow tools) |
| **Low-code era** | Developers are scarce | Let non-developers build |
| **AI era** | WHAT should happen | **Normative specifications** |

When AI can generate code, the value shifts to: **clear articulation of goals, rules, constraints.**

Platforms that don't capture normative become commodity execution layers. The differentiation moves to who has the best articulation of WHAT should happen.

#### 3. Business-Tech Alignment is Structurally Broken

**Current model:**
```
Requirements (business) → Translation → Code (developers) → Drift → "Legacy"
```

- Business can't read code
- Developers become bottlenecks for rule changes
- Translation introduces errors
- Drift is inevitable
- Knowledge leaves when people leave

**Normative-first model:**
```
Normative (business-owned) → Derivation (AI-assisted) → Automation → Validation against normative
```

- Business owns the authoritative source
- AI translates, humans review
- Derivation, not duplication
- Normative IS the documentation

**This is a structural fix, not a process improvement.**

#### 4. The Evolution Problem is Real

Every organization has processes where:
- The code does something, but no one knows WHY
- Regulations change, and finding what to update is archaeology
- The person who knew the rules left years ago
- Changing anything is terrifying

**If rules are in code:** Change requires developers, reverse-engineering, hope.

**If normative drives automation:** Change means updating the spec; derivation handles the rest.

---

### Addressing Concerns

#### "Normative specs will become stale, just like requirements docs"

**The structural difference:**
- Requirements docs are TRANSLATED into code, then forgotten
- Normative specs DRIVE automation — they're not an intermediate artifact

**Bidirectional verification:**
- When normative is co-located with automation, you can detect drift in BOTH directions
- AI can flag when implementation diverges from normative
- Reverse correlation is possible: code ↔ normative

**The incentive changes:**
- If automation derives from normative, stale normative = broken automation
- The system makes drift visible, not hidden

#### "AI-generated automation isn't mature enough"

**AI as validator, not just generator:**
- AI doesn't just generate FROM normative — it validates AGAINST normative
- AI is significantly better when it can cross-verify its work
- Normative spec becomes acceptance criteria for generated automation

**Continuous verification:**
- Not "generate once and forget"
- AI can continuously check: does automation still match normative?
- Humans remain in the loop, but AI does more with a spec to validate against

**Preparing for the trajectory:**
- AI capability is improving rapidly
- The model prepares for where AI is going, not just where it is
- Even partial AI assistance is valuable with good normative input

#### "Some domains don't need this structure"

**Domain coherence over per-scenario optimization:**
- The value isn't just per-scenario efficiency
- Keeping domain context together enables comprehension of the whole business domain
- Trade-offs should be assessed at domain level, not per automation need

**Where the structure adds most value:**
- Processes that evolve over time (most of them)
- Multiple stakeholders with distinct concerns
- Audit and compliance requirements
- AI-assisted automation is part of the strategy

**Where structure may be overhead:**
- Genuinely one-off scripts that will never change (rare in practice)
- Single person owns everything end-to-end (temporary state)
- Speed to first deployment matters more than long-term evolution (short-term thinking)

**The honest assessment:** Most "simple" processes eventually need to evolve. Most "one-off" scripts become production. The structure is investment in sustainability.

#### "Existing platforms could add normative layers"

**This is a thinking model, not a product claim.**
- Nothing implies no one else can or will do this
- Others can implement the paradigm
- The value is in the paradigm shift, not exclusive capability

**However, adding it as an afterthought is different from designing around it:**
- Bolted-on requirements management ≠ normative as source of truth
- The paradigm shift is fundamental: WHAT drives HOW
- Retrofitting this onto execution-focused platforms changes their architecture

#### "The problem is organizational, not technical"

**Acknowledged — bad requirements aren't fixed by any alternative.**

But consider:
- Tooling shapes behavior
- If the platform REQUIRES normative specs, they get created
- Making normative first-class changes incentives
- Explicit, verifiable requirements are better than implicit, scattered ones

**The question is:** Does the approach make requirements better or worse?
- At minimum: makes them explicit and verifiable
- With AI: makes them actionable for derivation and validation
- Over time: creates institutional memory in specs, not heads

#### "Adoption barrier is real"

**Reframe:** This isn't because scenario-oriented thinking is unsuitable. It's because switching may not be valuable enough in specific contexts.

**Inertia is real but separate:**
- "We've always done it this way" is not an argument against the model
- "Switching cost exceeds benefit" is a valid assessment in some contexts

**Where switching is most valuable:**
- Organizations investing in AI-assisted automation
- Domains with significant evolution and compliance needs
- Teams with business-tech alignment problems
- Long-term thinking about maintainability

**Where switching may not be worth it:**
- Stable, simple processes with no evolution pressure
- Contexts where the current approach genuinely works
- Short time horizons where upfront structure can't pay off

---

### The Paradigm Shift in Summary

| Current Paradigm | Normative-First Paradigm |
|------------------|--------------------------|
| Platforms focus on HOW | Model focuses on WHAT, HOW is derived |
| Requirements → translate → code | Normative → derive → automation |
| Business rules in code | Business rules in normative specs |
| Developer bottleneck for changes | Business updates normative, AI regenerates |
| Drift is inevitable | Bidirectional verification catches drift |
| AI guesses from scattered docs | AI derives from structured normative |
| Knowledge in people's heads | Knowledge explicit in specifications |

**This is not incremental improvement. It's a fundamental change in what the source of truth is.**

---

## 9. Comparison with Alternative Approaches

### The Central Question

Every process automation approach has normative requirements — roles, goals, rules, SOPs, compliance. **The question is: where do they live, and what's the source of truth?**

| Approach | Where Normative Lives | Source of Truth | AI-Ready? |
|----------|----------------------|-----------------|-----------|
| **BPM** | Separate docs, annotations | BPMN diagram | Partially — structure exists but normative is secondary |
| **Low-Code** | Implicit in flows | The visual flow | Limited — rules scattered, not structured |
| **Workflow-as-Code** | In code, comments | The code | No — business rules are implementation details |
| **Custom Code** | Buried in code | The code | No — opaque to business and AI |
| **Scenario-Oriented** | Explicit normative spec | Normative specification | Yes — structured input for derivation |

### 9.1 Traditional BPM (Camunda, Pega, Appian)

**Strengths:**
- Mature, proven, industry-adopted
- Visual process modeling
- Strong workflow orchestration

**The paradigm issue:**

BPM treats the BPMN diagram as the source of truth. But BPMN is implementation — it's *how* the process flows. The normative requirements (why, what goals, what rules, what compliance) live elsewhere:

- In requirements documents that get written once and forgotten
- In analysts' heads
- In BPMN annotations that mix with implementation

**The result:** Process diagrams and business requirements drift apart. When audit asks "what are the rules?", you piece together docs and code.

**BPM's assumption:** Someone else captures requirements; we handle execution.

**Scenario model's approach:** Normative IS the source of truth; execution derives from it.

### 9.2 Low-Code (Power Automate, Zapier, OutSystems)

**Strengths:**
- Fast to build
- Accessible to non-developers
- Good for simple integrations

**The paradigm issue:**

Low-code optimizes for speed to first deployment. Rules become implicit in the visual flow — drag, drop, configure, ship.

- Where are the business rules? In the flow configuration.
- Where are the SOPs? Not captured.
- Who owns what? The person who built it.

**The result:** Fast automation, unclear rules, governance problems. Works for departmental automation; breaks down for enterprise processes.

**Low-code's assumption:** Speed matters more than structure.

**Scenario model's approach:** Structure enables sustainable evolution; speed without structure is debt.

### 9.3 Workflow-as-Code (Temporal, Cadence)

**Strengths:**
- Excellent developer experience
- Durable execution, reliability guarantees
- Strong debugging and observability

**The paradigm issue:**

Temporal is developer tooling. Business rules live in code:

```python
if amount < 500 and merchant.is_clean():
    return auto_resolve()
else:
    return escalate_to_analyst()
```

This is clean code. But:
- Business can't read it
- Business can't change it without developers
- Audit requires reading code
- Knowledge leaves when developers leave

**The result:** Developer-owned automation. Works when developers own the full lifecycle. Breaks down when business needs visibility and control.

**Temporal's assumption:** Developers own everything.

**Scenario model's approach:** Business owns normative; developers implement; the separation is structural.

### 9.4 Custom Code (Microservices, Event-Driven)

**Strengths:**
- Complete flexibility
- No platform constraints
- Can be optimized for anything

**The paradigm issue:**

This is where "rules buried in code" is the default:

```java
// Auto-resolve if under threshold and clean history
// Updated by @john in 2019, not sure why 500
if (amount < 500 && merchantHistory.isClean()) {
    return autoResolve();
}
```

- Why 500? Who decided? What's the SOP?
- When regulations change, who finds this code?
- When John leaves, who knows this exists?

**The result:** Flexibility that becomes rigidity. No one dares change what they don't understand.

**Custom code's assumption:** Developers will document and maintain.

**Scenario model's approach:** Make the normative explicit; derivation handles implementation.

### 9.5 The Paradigm Shift: Normative as Source of Truth

**Every approach has normative requirements. The question is:**

| Question | Traditional | Scenario-Oriented |
|----------|-------------|-------------------|
| Where do requirements live? | Separate docs, code, heads | Normative specification |
| What's the source of truth? | Implementation (code/diagram) | Normative (business rules) |
| Who can read/change rules? | Developers | Business (with governance) |
| How does change happen? | Manually update code | Update normative → derive automation |
| What about AI? | AI can't read scattered docs | AI has structured input for derivation |

**The AI-ready dimension:**

In a world where AI agents generate automation:
- **BPM/Low-Code:** AI could generate flows, but from what input? Scattered docs?
- **Workflow-as-Code:** AI could write code, but what are the rules?
- **Scenario-Oriented:** AI has structured normative spec → can derive automation

**This is why normative-first matters:**
- AI needs structured input
- Business understands normative (it's their domain)
- Derivation keeps things in sync
- Evolution is sustainable

---

## 10. Every Process Needs This Model

### The Fundamental Requirements

Any process automation — regardless of complexity — needs:

| Requirement | Why It's Universal | What Happens Without It |
|-------------|-------------------|------------------------|
| **Explicit rules** | Regulations change, business changes, people leave | Rules buried in code, knowledge lost |
| **Sandboxed development** | You need to iterate before production | Changes go live untested |
| **Controlled deployment** | You need to know what's running | No visibility, no control |
| **Sustainable evolution** | Everything changes over time | Rewrite code for every change |

**The scenario model provides all of these.** Not as optional features, but as the foundational structure.

### "It's Simple, Just Write Code"

This is the common alternative. What happens?

```
"Simple process, just code it"
    ↓
Rules embedded in code
    ↓
Works fine initially
    ↓
Regulation changes, business asks for update
    ↓
Developer hunts for the code, tries to understand it
    ↓
Makes changes, hopes nothing breaks
    ↓
No one remembers why the code does what it does
    ↓
Fear of touching anything
    ↓
"Legacy system" — 2 years old
```

**Every process evolves.** The question is whether evolution is sustainable or a rewrite.

### One Scenario Is Valid

You don't need multiple scenarios to benefit from this model.

**Single scenario examples:**
- Invoice processing with consistent rules → one scenario
- Email routing → one scenario
- Data sync → one scenario

**What you still get:**
- Normative spec documenting the rules
- Clear ownership (business, developer, ops)
- Sandboxed development
- Controlled promotion to production
- AI can derive automation from normative
- Evolution without rewriting

### Multiple Scenarios When Situations Differ

| Domain | One Scenario | Multiple Scenarios |
|--------|--------------|-------------------|
| **Disputes** | All are the same type of problem | Standard vs. fraud vs. high-value are fundamentally different situations |
| **Payments** | All are the same type of transaction | Domestic vs. international vs. high-risk are different situations with different signals |
| **Onboarding** | All are the same type of customer | Individual vs. business vs. regulated entity are different situations requiring different normative specs |

### How to Decide

**Same scenario** if:
- The situation is fundamentally the same
- The same signal type indicates it
- Differences are parameter values within the same situation (amount thresholds, etc.)

**Different scenarios** if:
- The situation is fundamentally different (business recognizes it as a distinct problem)
- Different signals indicate it (fraud flag vs. standard dispute filing)
- It requires a different normative specification (different goals, roles, compliance context)

**The test:** Would business stakeholders say "that's a different situation entirely" or "that's the same situation with different parameters"?

---

## 11. Adoption and Migration

### 11.1 Starting with Scenario Thinking

**Step 1: Identify Scenarios**
- What situations does your business need to respond to?
- What signals indicate each situation?
- What makes each situation fundamentally different (not how it's processed, but what it IS)?

**Step 2: Validate with Stakeholders**
- Do business stakeholders recognize these scenarios?
- Are the boundaries clear?
- Are any scenarios missing?

**Step 3: Design Normative Specifications**
- For each scenario: who, what goals, what rules
- This is the source of truth — invest here
- Document SOPs, decision criteria, compliance requirements

**Step 4: Derive Automation**
- What automation approach fits each scenario?
- AI can assist with generation from normative
- Human developers review and refine

**Step 5: Configure Deployment**
- How will work be assigned?
- What are the SLA requirements?
- AI can suggest; operators approve

### 11.2 Migrating Existing Processes

**From Hardwired Code to Scenarios:**
1. Identify triggers (what starts the process?)
2. Identify variation (are there distinct handling patterns?)
3. Extract business rules from code → normative spec
4. Identify implementation → automation spec
5. Extract operational settings → deployment spec

**From BPM to Scenarios:**
1. The BPMN diagram becomes input, not source of truth
2. Capture the normative that was implicit
3. Scenario boundaries may differ from process boundaries

**What Makes a Different Scenario:**

Scenarios are **coarse-grained** — they represent recognizable business situations, not individual decision rules.

| Different Scenario | Same Scenario, Different Rules |
|-------------------|-------------------------------|
| Fraud Dispute vs. Standard Dispute (different situation entirely) | Amount thresholds within Standard Dispute |
| Individual Onboarding vs. Business Onboarding (different verification, roles) | Different document requirements based on income |
| International Payment vs. Domestic Payment (different compliance, processing) | Different fee tiers based on amount |

**The test:** Do business stakeholders recognize this as a **fundamentally different situation** with different roles, goals, or compliance requirements? Or is it the same situation with different decision branches inside?

**Decision rules belong IN the normative spec, not as separate scenarios:**
```yaml
scenario: standard-dispute
normative:
  decision_criteria:
    - amount < 500 AND merchant_clean: auto_resolve
    - amount 500-1000: analyst_review  
    - customer_high_risk: extra_verification
```
These are rules **within** the Standard Dispute scenario — not separate scenarios.

### 11.3 Best Practices

**Normative-First:**
- Start with normative specification — it's the source of truth
- Get business validation before automation
- AI can generate automation from good normative specs

**Scenario Design:**
- One scenario per distinct situation
- Clear, recognizable names
- Start with fewer, split later if needed

**Ownership:**
- Process Architect owns normative
- Developer owns automation
- Supervisor owns deployment
- Clear boundaries reduce coordination overhead

---

## 12. Conclusion

### The Core Insight

**Normative specifications are the center of gravity.**

In a world where AI agents increasingly handle automation:
- Business should focus on **what should happen** (normative)
- AI agents derive **how it's implemented** (automation)
- AI agents assist with **how it's operated** (deployment)
- Humans curate, review, and handle exceptions

The three-specification model isn't just organizational hygiene — it's preparing for this future.

### Key Takeaways

1. **Think in situations, not steps** — Scenarios are operational situations, not workflow diagrams
2. **Normative is the source of truth** — Everything else derives from it
3. **Three specifications with clear ownership** — Business owns normative, developers implement, ops deploys
4. **AI-ready model** — Normative specs can drive AI-generated automation
5. **Every process needs this** — Even simple processes evolve; hardwired code becomes debt

### What Changes

| Traditional Approach | Scenario-Oriented + AI |
|---------------------|------------------------|
| Requirements in docs, rules in code | Normative is the authoritative source |
| Manual sync, inevitable drift | Automation derived from normative |
| Developer bottleneck for rule changes | Business changes normative, agents regenerate |
| Knowledge in people's heads | Knowledge explicit in specifications |

### Trade-offs

- ⚠️ **Upfront structure:** Requires explicit normative design
- ⚠️ **Mental model shift:** Different from "just write code"
- ⚠️ **Discipline needed:** Specifications must be maintained

These are the cost of a model that scales with AI assistance and organizational change.

---

## Related Documentation

- [Hub Development Flow Guide](../../10-guides/hub-development-flow/README.md) — Platform-specific development practices
- [Scenario Specification Types](../../02-system-design/implementation-concepts/scenario-specification-types.md)
- [Idea to Deployment Guide](../../10-guides/idea-to-deployment-guide.md)
- [Scenario Development Journey](../../08-personas-and-journeys/journeys/scenario-development.md)

---

*This document covers Scenario-Oriented Thinking as a conceptual model for business process automation. For Hub platform specifics (workbenches, development workflow, promotion), see the Hub Development Flow Guide.*
