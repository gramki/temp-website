# Appendix C: AOSM Foundations

Seer's design is grounded in **Agent-Oriented Systems Modeling (AOSM)**, Zeta's meta-model for agent-oriented enterprises. This appendix provides background on the key AOSM concepts that inform Seer's architecture.

---

## What is AOSM?

AOSM is a conceptual framework for designing enterprise systems where AI agents and humans collaborate. It provides:

- **Vocabulary:** Consistent terminology for agent-related concepts
- **Models:** Frameworks for understanding agent behavior and governance
- **Patterns:** Reusable approaches to common agent design challenges
- **Principles:** Foundational rules that govern agent-human collaboration

## Key AOSM Concepts

### KSA: Knowledge, Skills, Abilities

What agents know and can do.

| Component | Definition | Seer Mapping |
|-----------|------------|--------------|
| **Knowledge** | What the agent knows (facts, policies, procedures) | Knowledge bindings in TrainingSpec |
| **Skills** | What the agent can do (capabilities, tool use) | Skill configurations in TrainingSpec |
| **Abilities** | The agent's capacity to apply skills effectively | Guardrails and authority in Specs |

### PIDA: Perceive, Interpret, Decide, Act

The cycle of agent behavior.

```
Perceive → Interpret → Decide → Act
    ↑                            ↓
    └────────── Feedback ────────┘
```

| Phase | Description | Seer Implementation |
|-------|-------------|---------------------|
| **Perceive** | Receive input from environment | Signal intake, context assembly |
| **Interpret** | Understand meaning and relevance | LLM reasoning with knowledge |
| **Decide** | Choose action based on goals and constraints | Decision with guardrails |
| **Act** | Execute chosen action | Tool invocation with audit |

### OPD: Observability, Predictability, Directability

The three properties that distinguish enterprise-ready agents.

| Property | Definition | Seer Delivery |
|----------|------------|---------------|
| **Observability** | Agent behavior is inspectable | Full audit trail, decision records, explanations |
| **Predictability** | Agent behaves within known bounds | Immutable guardrails, authority ceilings |
| **Directability** | Humans can steer agent behavior | Override, kill switch, escalation |

### RASCI: Accountability Model

Who is responsible for what.

| Role | Definition | Application to Agents |
|------|------------|----------------------|
| **Responsible** | Does the work | Agent performs the task |
| **Accountable** | Ultimately answerable | **Always a human** |
| **Supporting** | Helps complete the work | Other agents, tools |
| **Consulted** | Provides input | Policies, precedents |
| **Informed** | Notified of outcomes | Stakeholders, audit |

**Critical Principle:** Agents can be Responsible, but humans are always Accountable.

### Controlled Autonomy

Agents act only within bounds set by accountable humans.

| Component | Definition |
|-----------|------------|
| **Authority** | What the agent is permitted to do |
| **Availability** | When the agent can act |
| **Capability** | What the agent can technically do |
| **Capacity** | How much the agent can handle |

**Autonomy = Authority ∩ Availability ∩ Capability ∩ Capacity**

An agent can only act when all four components are satisfied.

### Human-AI Team (HAT)

Coordinated collaboration between humans and AI agents.

| Principle | Description |
|-----------|-------------|
| **Shared Context** | Humans and AI operate in the same operational context |
| **Task Interoperability** | Same task queues serve both humans and AI |
| **Seamless Handoff** | Work transfers smoothly between humans and AI |
| **Human Oversight** | Humans supervise and can override AI |

## Agent Archetypes

AOSM defines four functional perspectives for agents:

| Archetype | Function | Rejectable Artifacts |
|-----------|----------|---------------------|
| **Thinker** | Reasoning, decisions | Decision Request, Decision Result |
| **Doer** | Executing actions | Action Request, Action Result |
| **Orchestrator** | Assigning work | Task Assignment |
| **Governor** | Observing, auditing | None (observations are facts) |

These are perspectives, not exclusive categories—a single agent may embody multiple archetypes.

## The Raw-Trained-Employed Model

AOSM's three-layer agent lifecycle model:

```
Raw Agent (Capabilities)
    ↓ + TrainingSpec
Trained Agent (Knowledge + Skills + Guardrails)
    ↓ + EmploymentSpec
Employed Agent (Delegated Authority)
```

| Layer | What It Adds | Who Controls |
|-------|--------------|--------------|
| **Raw** | Technical capabilities | Developer |
| **Trained** | Domain configuration | Domain Lead + Security |
| **Employed** | Authority delegation | Manager |

### Immutability Principle

Guardrails defined at training cannot be relaxed at employment. Each layer can add constraints but never remove them.

## How AOSM Informs Seer

| AOSM Concept | Seer Implementation |
|--------------|---------------------|
| **KSA** | TrainingSpec defines knowledge and skills |
| **PIDA** | Agent runtime implements the behavior cycle |
| **OPD** | Full observability, guardrails, override capability |
| **RASCI** | Manager assignment, delegation chains |
| **Controlled Autonomy** | Authority ceilings, kill switch |
| **HAT** | Task queue integration, human collaboration |
| **Archetypes** | Role-based governance and routing |
| **Lifecycle Model** | Raw → Trained → Employed progression |

---

**References:**
*   `aosm-meta-model/agent-oriented-system.md`
*   `aosm-meta-model/raw-trained-employed-agents.md`
*   `aosm-meta-model/controlled-autonomy.md`
