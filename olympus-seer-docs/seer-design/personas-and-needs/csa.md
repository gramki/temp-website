# Cognitive Systems Architect (CSA)

> **Status:** Reference Document  
> **Last Updated:** 2026-01-09  
> **Related:** [Role Definitions](./roles.md) | [APO Reference](./apo.md)

---

## The Problem CSA Solves

Agents are not deterministic software. They reason, adapt, and sometimes surprise. Without architectural discipline, agentic systems become:

- Unpredictable in failure modes
- Unobservable in reasoning
- Ungovernable when things go wrong
- Incompatible when they need to work together
- Unscalable when the organization grows

Traditional software architecture assumes you control the execution path. Agent architecture must assume you *influence* the reasoning path — and prepare for when you can't.

**CSA exists because intelligence needs structure to be governable.**

---

## The CSA Mandate

> **CSA owns how cognition is allowed to work.**

This means:

| CSA Owns | CSA Does NOT Own |
|----------|------------------|
| Cognitive patterns and reasoning models | Why the agent exists (APO) |
| Agent-to-agent interaction models | Implementation details (AE) |
| Failure semantics and escalation design | Runtime enforcement (ARE) |
| Design-time constraints | Business prioritization (APO) |
| Multi-agent system architecture | Compliance judgments (ARAO) |

**The distinction matters.** CSA doesn't decide what agents should do — CSA decides *how they're allowed to think* while doing it.

CSA designs the guardrails on cognition. APO chooses the destination. AE builds the vehicle. ARE operates it safely.

---

## Why This Role Is Different

### It's Not Traditional Software Architecture

Software architects design data flows, APIs, and system boundaries. CSA designs *reasoning flows*, *decision boundaries*, and *cognitive constraints*.

| Software Architect | CSA |
|-------------------|-----|
| "How should services communicate?" | "How should agents collaborate?" |
| "What's the data model?" | "What's the reasoning model?" |
| "How do we handle errors?" | "How do we handle wrong decisions?" |
| "What are the API contracts?" | "What are the cognitive contracts?" |

### It's Not the Agent Product Owner

APO defines what the agent should accomplish. CSA defines *how it's allowed to reason* toward that goal.

### It's Not the Agent Engineer

AE implements the design. CSA creates the design that makes implementation possible and safe.

---

## What CSA Cares About

### 1. Are the Reasoning Patterns Sound?

Every agent needs:
- A defined reasoning approach (reactive, deliberative, reflective)
- Clear cognitive boundaries (what it thinks about vs. what it doesn't)
- Explicit decision points (where choices are made)
- Traceable reasoning chains (how conclusions are reached)

**If you can't draw the reasoning flow, the design isn't complete.**

---

### 2. Are Failures Well-Defined?

Agents fail differently than traditional software:

| Traditional Failure | Agent Failure |
|---------------------|---------------|
| Crash | Wrong decision |
| Timeout | Infinite reasoning loop |
| Exception | Hallucination |
| Bad input | Misunderstood context |

CSA designs failure semantics:
- What counts as a failure?
- How is failure detected?
- What happens when failure occurs?
- How is failure communicated?

**If failure modes aren't designed, they'll be discovered in production.**

---

### 3. How Do Agents Work Together?

Multi-agent systems require architectural decisions:

| Decision | Options |
|----------|---------|
| Coordination model | Hierarchical, peer-to-peer, marketplace |
| Communication pattern | Direct messaging, shared memory, event-driven |
| Conflict resolution | Voting, authority, escalation |
| Failure propagation | Isolated, cascading, contained |

CSA designs these interactions before they're built.

**If multi-agent coordination is ad-hoc, it will be chaotic.**

---

### 4. Is Escalation Designed?

When an agent can't handle something, it must escalate. CSA designs:

| Escalation Aspect | Design Decision |
|-------------------|-----------------|
| Trigger conditions | What causes escalation? |
| Escalation target | Who receives the escalation? |
| Context preservation | What information is passed? |
| Timeout behavior | What if no one responds? |
| Resolution recording | How is outcome captured? |

**If escalation isn't designed, agents will fail silently or endlessly retry.**

---

### 5. Is the Design Governable?

A governable design means:
- Reasoning can be observed
- Decisions can be explained
- Behavior can be constrained
- Changes can be validated

CSA ensures that designs support observability, explainability, and control — not as afterthoughts, but as core requirements.

**If governance is bolted on later, it won't work.**

---

## What CSA Owns

### Cognitive Patterns

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **ReAct** | Reason → Act → Observe loop | General-purpose agents |
| **Chain-of-Thought** | Step-by-step reasoning | Complex decisions |
| **Reflection** | Self-critique and correction | Quality-sensitive tasks |
| **Decomposition** | Break into subtasks | Complex multi-step work |
| **Orchestration** | Coordinate sub-agents | Multi-agent workflows |

CSA selects and constrains which patterns are acceptable.

---

### Agent Archetypes

| Archetype | Role | Design Considerations |
|-----------|------|----------------------|
| **Thinker** | Makes decisions | Decision quality, explainability |
| **Doer** | Executes actions | Tool safety, rollback capability |
| **Orchestrator** | Coordinates work | Task distribution, failure handling |
| **Governor** | Observes and enforces | Non-blocking, audit-focused |

CSA defines how archetypes interact and when to use each.

---

### Interaction Contracts

For multi-agent systems, CSA defines:

| Contract Element | Description |
|------------------|-------------|
| Message formats | Structure of inter-agent communication |
| Response expectations | Timeout, acknowledgment, completion |
| Authority boundaries | What each agent is allowed to request |
| Failure protocols | How failures are signaled and handled |

---

### Design Validation Criteria

Before implementation, CSA validates:

| Criterion | Question |
|-----------|----------|
| Bounded reasoning | Can the agent get stuck in infinite loops? |
| Observable decisions | Can we see what the agent decided and why? |
| Defined failure modes | Do we know how every failure manifests? |
| Escalation paths | Is there always a way out? |
| Testability | Can the design be validated before production? |

---

## How CSA Works With Others

| Role | CSA's Relationship |
|------|-------------------|
| **APO** | APO defines intent; CSA designs cognition to achieve it safely. |
| **AE** | CSA creates designs; AE implements them. CSA validates implementation matches design. |
| **ARE** | CSA designs escalation; ARE operates it. CSA consults on operability. |
| **KMO** | CSA designs knowledge access patterns; KMO ensures knowledge is available. |
| **COS** | COS reports behavior issues; CSA determines if design changes are needed. |
| **ARAO** | CSA designs controls; ARAO validates they meet policy requirements. |

---

## What CSA Does NOT Do

| Responsibility | Who Owns It |
|----------------|-------------|
| Decide why agents exist | APO |
| Implement agent code | AE |
| Operate agents in production | ARE |
| Approve autonomy levels | ARAO |
| Monitor ongoing behavior | COS |
| Curate knowledge | KMO |

CSA designs the blueprint. Others build, operate, and govern.

---

## The CSA Skill Profile

### Technical Depth

- Deep understanding of LLMs and agent frameworks
- Experience with distributed systems
- Knowledge of reasoning patterns and their trade-offs
- Familiarity with observability and tracing

### Architectural Thinking

- Ability to think in systems, not features
- Failure-mode analysis as a core skill
- Pattern recognition and application
- Long-term thinking about maintainability

### Communication

- Ability to translate between business intent and technical design
- Clear documentation of design decisions
- Effective validation with AE teams
- Explaining trade-offs to non-technical stakeholders

### Governance Mindset

- Designing for observability from the start
- Thinking about auditability and compliance
- Building in control points, not adding them later
- Appreciation for the tension between autonomy and control

---

## Anti-Patterns

| Pattern | Why It's Dangerous |
|---------|-------------------|
| "Let's figure out the architecture as we build" | No design = no predictability |
| "Each agent can reason however it wants" | Inconsistency = ungovernable |
| "Failure handling is an implementation detail" | Failure semantics are architectural |
| "We'll add observability later" | Observability must be designed in |
| "This agent only does one thing, it doesn't need architecture" | Even simple agents need constraints |
| "The model will figure it out" | Models need structure, not hope |

---

## Success Criteria

CSA is successful when:

- Every agent has a clear, documented reasoning model
- Failure modes are known before production
- Multi-agent interactions are predictable
- Escalation paths work as designed
- AE can implement designs without ambiguity
- ARE can operate systems because they're observable
- ARAO can audit systems because they're explainable

---

## Final Word

When someone asks:

> "How does this agent think?"

CSA's job is to answer:

> "Here's the reasoning pattern, the decision boundaries, the failure modes, and the escalation paths — all designed before a line of code was written."

If a design can't be drawn, explained, and validated, it isn't a design — it's a hope.

**Intelligence without architecture is chaos. CSA imposes the structure that makes agents trustworthy.**

---

*End of document*

