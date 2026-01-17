# Agent Model

> **How human and AI agents interact with Hub**  
> **Last Updated:** 2026-01-08

---

## Overview

Olympus Hub is built for **human-AI collaboration**. Both human and AI agents work within the same operational framework — receiving tasks, accessing tools, making decisions, and completing work. This document explains the agent model, how different agent types participate, how they collaborate, and how humans maintain **directability** over AI agents.

---

## The Agent Spectrum

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         AGENT SPECTRUM                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   HUMAN AGENTS                          AI AGENTS                            │
│   ────────────                          ─────────                            │
│                                                                              │
│   ┌────────────────┐                   ┌────────────────┐                   │
│   │   Business     │                   │   Capable AI   │                   │
│   │   Customer     │                   │   (General)    │                   │
│   │   (Self-serve) │                   │                │                   │
│   └────────────────┘                   └────────────────┘                   │
│                                                                              │
│   ┌────────────────┐                   ┌────────────────┐                   │
│   │    Operator    │                   │  Skilful AI    │                   │
│   │    (Agent)     │◀───COLLABORATE───▶│  (Domain)      │                   │
│   └────────────────┘                   └────────────────┘                   │
│                                                                              │
│   ┌────────────────┐                   ┌────────────────┐                   │
│   │   Supervisor   │                   │  Scenario AI   │                   │
│   │                │◀────OVERSEE──────▶│  (Enrolled)    │                   │
│   └────────────────┘                   └────────────────┘                   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Agent Types

### Human Agents

| Agent Type | Role | Primary Interaction |
|------------|------|---------------------|
| **Business Customer** | Self-service requestor | Portals, Chat, IVR |
| **Business Employee** | Internal requestor | Internal apps, Teams |
| **Operator (Agent)** | Task executor | Agent Desk, Teams |
| **Supervisor** | Team oversight | Supervisor Desk |
| **Process Architect** | Scenario designer | Workbench Studio |
| **Developer** | Automation builder | Workbench Studio, IDE |
| **Administrator** | Platform config | Control Center |

### AI Agents

| Agent Type | Capability | Use Case |
|------------|------------|----------|
| **Capable AI Agent** | General operational capabilities | Cross-domain tasks |
| **Skilful AI Agent** | Domain-specific expertise | Specialized operations |
| **Scenario as Agent** | Scenario published as agent | Task completion |
| **Hub Application Agent** | Application acting as agent | Automated processing |

→ **Details:** [Persona](./implementation-concepts/persona.md)

---

## Agent Lifecycle

### Human Agent Lifecycle

```
1. IDENTITY
   User created in enterprise IdP
       │
       ▼
2. AUTHENTICATION
   SSO via Cipher IAM (SAML/OIDC)
       │
       ▼
3. PERSONA ASSIGNMENT
   Assigned to Persona (Agent, Supervisor, etc.)
       │
       ▼
4. WORKBENCH ENROLLMENT
   Enrolled in specific Workbenches with Roles
       │
       ▼
5. TASK ELIGIBILITY
   Eligible for tasks matching Role + Skills
       │
       ▼
6. TASK EXECUTION
   Receives and completes tasks via Channels
```

### AI Agent Lifecycle

```
1. CREATION
   AI Agent Application developed
       │
       ▼
2. REGISTRATION
   Registered in Hub with identity (SPIFFE)
       │
       ▼
3. CAPABILITY DEFINITION
   Capabilities and tools defined
       │
       ▼
4. WORKBENCH ENROLLMENT
   Enrolled in specific Workbenches
       │
       ▼
5. TASK DELEGATION
   Receives delegated tasks from Hub Applications
       │
       ▼
6. EXECUTION & REPORTING
   Executes actions, reports outcomes
```

---

## How Agents Receive Work

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    WORK DISTRIBUTION                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   HUB APPLICATION                                                            │
│        │                                                                     │
│        │ Creates Task with:                                                  │
│        │   • Task Type                                                       │
│        │   • Required Skills                                                 │
│        │   • Priority                                                        │
│        │   • Context                                                         │
│        ▼                                                                     │
│   ┌──────────────────────────────────────────────────────────────────────┐  │
│   │                    TASK MANAGEMENT                                    │  │
│   │                                                                       │  │
│   │   ┌─────────────────────────────────────────────────────────────────┐│  │
│   │   │                 ASSIGNMENT STRATEGIES                           ││  │
│   │   │                                                                 ││  │
│   │   │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐   ││  │
│   │   │  │  Queue    │  │  Direct   │  │   Group   │  │ Delegation│   ││  │
│   │   │  │ (Skills)  │  │  (User)   │  │ (Any of)  │  │ (AI Agent)│   ││  │
│   │   │  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘   ││  │
│   │   │        │              │              │              │         ││  │
│   │   └────────┼──────────────┼──────────────┼──────────────┼─────────┘│  │
│   │            │              │              │              │          │  │
│   │            ▼              ▼              ▼              ▼          │  │
│   │   ┌─────────────────────────────────────────────────────────────┐  │  │
│   │   │                    AGENTS                                    │  │  │
│   │   │                                                              │  │  │
│   │   │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │  │
│   │   │  │   Human     │  │   Human     │  │    AI       │          │  │  │
│   │   │  │   Agent A   │  │   Agent B   │  │   Agent     │          │  │  │
│   │   │  │             │  │             │  │             │          │  │  │
│   │   │  │ • Queue     │  │ • Direct    │  │ • Delegated │          │  │  │
│   │   │  │   pick-up   │  │   assigned  │  │   task      │          │  │  │
│   │   │  └─────────────┘  └─────────────┘  └─────────────┘          │  │  │
│   │   │                                                              │  │  │
│   │   └──────────────────────────────────────────────────────────────┘  │  │
│   │                                                                       │  │
│   └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Assignment Methods

| Method | Target | Use Case |
|--------|--------|----------|
| **Task Queue** | Skill-based pool | General work distribution |
| **Direct User** | Specific human | Known expert needed |
| **User Group** | Any group member | Flexible assignment |
| **AI Delegation** | AI Agent | Automated processing |

→ **Details:** [Task Allocation](./implementation-concepts/task-allocation.md)

---

## Agent Interaction Channels

### Human Agent Channels

| Channel | Use Case | Features |
|---------|----------|----------|
| **Web Console** | Full-featured work | Complete task context, all tools |
| **MS Teams** | In-flow collaboration | Quick actions, notifications |
| **MCP** | AI assistant integration | Voice/chat with AI assistant |
| **REST API** | Programmatic access | Automation, scripting |

### AI Agent Channels

| Channel | Use Case | Features |
|---------|----------|----------|
| **Task Delegation API** | Receive tasks | Structured task context |
| **Tool Invocation** | Execute actions | Command Registry access |
| **Request Update API** | Report outcomes | Status and results |
| **Memory/Knowledge API** | Access context | RAG, agent memory |

→ **Details:** [Channel](./implementation-concepts/channel.md) | [Headless Access Service](./implementation-concepts/headless-access-service.md)

---

## Agent Capabilities

### What Agents Can Do

| Capability | Human | AI | Notes |
|------------|-------|-----|-------|
| **Receive Tasks** | ✓ | ✓ | Via queue or delegation |
| **View Context** | ✓ | ✓ | Request history, related data |
| **Execute Tools** | ✓ | ✓ | Command Registry |
| **Make Decisions** | ✓ | ✓ | With decision criteria |
| **Add Memos** | ✓ | ✓ | Document findings |
| **Escalate** | ✓ | ✓ | To higher tier |
| **Complete Tasks** | ✓ | ✓ | With outcomes |
| **Access Knowledge** | ✓ | ✓ | SOPs, runbooks |
| **Collaborate** | ✓ | ✓ | Chat, handoff |
| **Approve Decisions** | ✓ | Limited | Regulatory constraints |

### Tool Access

Agents access external capabilities through the **Command Registry**:

```
Agent
    │
    │ Needs to look up transaction
    ▼
Command Registry
    │
    │ Routes to appropriate Machine
    ▼
Machine: core-banking
    │
    │ Executes: get_transaction
    ▼
Result returned to Agent
```

---

## Human-AI Collaboration Patterns

### Pattern 1: AI Assists Human

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AI ASSISTS HUMAN                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Human Agent                          AI Agent                               │
│  ────────────                         ────────                               │
│                                                                              │
│  Receives dispute task                                                       │
│       │                                                                      │
│       │ "Help me analyze this dispute"                                       │
│       └───────────────────────────────────────────▶ AI reviews context       │
│                                                          │                   │
│       ◀───────────────────────────────────────────────────┘                  │
│       │ "Based on transaction patterns, this appears to be                   │
│       │  legitimate. Customer made 3 similar purchases last month."          │
│       │                                                                      │
│  Human makes decision (with AI insight)                                      │
│       │                                                                      │
│  Completes task                                                              │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Pattern 2: AI Executes, Human Approves

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AI EXECUTES, HUMAN APPROVES                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  AI Agent                             Human Supervisor                       │
│  ────────                             ────────────────                       │
│                                                                              │
│  Receives low-value dispute                                                  │
│       │                                                                      │
│  Gathers evidence                                                            │
│       │                                                                      │
│  Analyzes patterns                                                           │
│       │                                                                      │
│  Determines: "Recommend refund"                                              │
│       │                                                                      │
│       │ "Request approval for $45 refund"                                    │
│       └───────────────────────────────────────────▶ Reviews recommendation   │
│                                                          │                   │
│                                                     Approves/Rejects         │
│       ◀───────────────────────────────────────────────────┘                  │
│       │ Approved                                                             │
│       │                                                                      │
│  Executes refund                                                             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Pattern 3: Escalation Chain

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ESCALATION CHAIN                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  T+0:     Task assigned to AI Agent                                          │
│                │                                                             │
│                │ AI processes, but confidence < threshold                    │
│                │                                                             │
│  T+15m:   AI escalates to Tier-1 Human                                       │
│                │                                                             │
│                │ Human investigates, needs expert                            │
│                │                                                             │
│  T+2h:    Escalates to Tier-2 (cumulative)                                   │
│                │                                                             │
│                │ Tier-1 + Tier-2 collaborate                                 │
│                │                                                             │
│  T+3h:    Resolution reached                                                 │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

→ **Details:** [Escalation Matrix](./implementation-concepts/escalation-matrix.md)

---

## Agent Directability

**Directability** is the ability for humans to intervene in, redirect, or override AI agent behavior during cognitive operations. Hub implements directability through a rejection-escalation model.

### Agent Archetypes

Hub recognizes four functional archetypes that describe what an agent does at any moment. **An agent may wear all hats** — these are perspectives, not exclusive roles.

| Archetype | Function | Rejectable Artifacts |
|-----------|----------|---------------------|
| **Thinker** | Reasoning, decisions | Decision Request, Decision Result |
| **Doer** | Executing actions | Action Request, Action Result |
| **Orchestrator** | Assigning work | Task Assignment |
| **Governor** | Observing, auditing | None (observations are facts) |

### Rejection as Intervention Trigger

All directability flows from **rejection events**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AI AGENT DIRECTABILITY                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  AI Agent produces output                                                    │
│       │                                                                      │
│       │ (Decision Result, Action Result, etc.)                               │
│       ▼                                                                      │
│  ┌───────────────────────────────────────────────────────────────┐          │
│  │  REJECTION SOURCES                                            │          │
│  │                                                               │          │
│  │  • Guardrail: "Confidence below threshold"                   │          │
│  │  • Policy: "Amount exceeds auto-approval limit"              │          │
│  │  • Application: "Missing required evidence"                  │          │
│  │  • Another Agent: "Invalid transaction reference"            │          │
│  └───────────────────────┬───────────────────────────────────────┘          │
│                          │                                                   │
│                          ▼                                                   │
│  ┌───────────────────────────────────────────────────────────────┐          │
│  │  ESCALATION TASK CREATED                                      │          │
│  │                                                               │          │
│  │  Assigned via Scenario Escalation Matrix (Supervisor-defined) │          │
│  │  Accountable Human notified                                   │          │
│  └───────────────────────┬───────────────────────────────────────┘          │
│                          │                                                   │
│                          ▼                                                   │
│  ┌───────────────────────────────────────────────────────────────┐          │
│  │  HUMAN RESOLUTION OPTIONS                                     │          │
│  │                                                               │          │
│  │  • Override the decision (with new value)                    │          │
│  │  • Change context and re-run                                 │          │
│  │  • Reassign to different agent                               │          │
│  │  • Fail the scenario                                         │          │
│  │  • Create corrective action                                  │          │
│  └───────────────────────┬───────────────────────────────────────┘          │
│                          │                                                   │
│                          ▼                                                   │
│  ┌───────────────────────────────────────────────────────────────┐          │
│  │  CAF RECORDS                                                  │          │
│  │                                                               │          │
│  │  Override Record / ContextIntervention Record                 │          │
│  │  DirectiveResolution Record (ack + outcome)                   │          │
│  └───────────────────────────────────────────────────────────────┘          │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Directability Roles

| Role | Directability Responsibility |
|------|------------------------------|
| **Supervisor** | Defines all escalation matrices; handles escalated tasks; overrides decisions |
| **Agent** | Completes escalation tasks; may trigger rejection by abandoning |
| **Process Architect** | Defines guardrails and policies that trigger rejections |
| **Developer** | Implements application logic that may reject artifacts |

### What's NOT Directability

| Concern | Reason | Where Handled |
|---------|--------|---------------|
| **Kill-switch** | Infrastructure concern | Seer Runtime (Agent Lifecycle) |
| **Authority Revocation** | Requires deliberation | Enterprise Learning workflow |
| **Governor Observations** | Facts, not proposals | Recorded as-is; feed Enterprise Learning |

→ **Details:** [Agent Directability](./implementation-concepts/agent-directability.md)

---

## Agent Identity and Security

### Human Agent IAM

| Aspect | Mechanism |
|--------|-----------|
| **Authentication** | SSO via SAML/OIDC |
| **Authorization** | RBAC scoped to Workbenches |
| **Session** | Secure session across Channels |
| **Audit** | Complete action audit trail |

### AI Agent IAM

AI Agents have **two-layer identity**:

| Aspect | Mechanism |
|--------|-----------|
| **Deployment Identity** | SPIFFE-based identity (OAuth Client equivalent) — infrastructure-level |
| **Agent Persona** | Scenario-derived business identity — carried in Delegation Access Tokens |
| **Authorization** | Fine-grained entity/action permissions |
| **Tool Access** | OAuth-like consent flows |
| **Credentials** | Secure vault management |

**Deployment Identity (SPIFFE)**:
- Infrastructure-level identity of the running agent pod
- OAuth Client equivalent — proves "this request is coming from this specific agent deployment"
- Used for mTLS, service mesh authentication
- Auto-provisioned by SPIRE during pod startup

**Agent Persona**:
- Business-level identity derived from Scenario
- Represents "who this agent is" in business terms
- Carried in Delegation Access Tokens (`sub` claim)
- Stored in Cipher IAM (Scenario references it)

> **See**: [ADR-0129: Agent Identity Model](../decision-logs/0129-agent-identity-model.md) for the complete two-layer identity model.

### Cross-Agent Authorization

| Pattern | Description |
|---------|-------------|
| **Delegation** | Human grants specific permissions to AI |
| **Impersonation** | AI acts on behalf with explicit consent |
| **Scope Limiting** | Time-bound or entity-scoped permissions |

---

## Agent Observability

### What's Tracked

| Metric | Purpose |
|--------|---------|
| **Task throughput** | Tasks completed per agent/time |
| **Response time** | Time to first action |
| **Completion time** | Total time to complete |
| **Quality scores** | Accuracy, compliance |
| **Escalation rate** | % of tasks escalated |
| **AI confidence** | AI decision confidence levels |

### Agent Dashboard

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT PERFORMANCE                                         Period: Today    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Agent: alice@acme.com                     Persona: Agent                    │
│                                                                              │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐                │
│  │ Tasks Completed │ │ Avg Resolution  │ │ Quality Score   │                │
│  │       23        │ │     45 min      │ │      4.8/5      │                │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘                │
│                                                                              │
│  AI Agent: dispute-ai-agent                Type: Skilful                     │
│                                                                              │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐                │
│  │ Tasks Processed │ │ Auto-Resolved   │ │ Escalated       │                │
│  │      156        │ │    142 (91%)    │ │    14 (9%)      │                │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘                │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Composite Patterns

Hub enables advanced agent compositions:

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Scenario as Agent** | Scenario exposed as task-completing agent | Cross-workbench delegation |
| **Scenario as Tool** | Scenario exposed as callable tool | AI agent orchestration |
| **Hub App as Standalone Tool** | Application as direct tool | Bypasses SX for sync calls |

→ **Details:** [Scenario as Agent](./implementation-concepts/scenario-as-agent.md) | [Scenario as Tool](./implementation-concepts/scenario-as-tool.md)

---

## Related Documentation

| Document | Purpose |
|----------|---------|
| [Hub Architecture](./hub-architecture.md) | System overview |
| [Signal Flow](./signal-flow.md) | How signals become agent tasks |
| [Workbench Anatomy](./workbench-anatomy.md) | Where agents work |
| [Persona](./implementation-concepts/persona.md) | User archetypes |
| [Channel](./implementation-concepts/channel.md) | Interaction interfaces |
| [Task Allocation](./implementation-concepts/task-allocation.md) | Work distribution |
| [Escalation Matrix](./implementation-concepts/escalation-matrix.md) | Escalation patterns |
| [Agent Directability](./implementation-concepts/agent-directability.md) | Human intervention in AI operations |
| [Cognitive Audit Fabric](./implementation-concepts/cognitive-audit-fabric.md) | Intervention audit records |

