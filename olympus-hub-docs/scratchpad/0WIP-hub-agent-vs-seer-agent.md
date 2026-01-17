# Hub Agent vs Seer Agent

> **Status**: 🟡 Draft / WIP  
> **Target Audience**: Process Architects, CSAs, Agent Engineers, Developers  
> **Purpose**: Clarify the conceptual distinction between Hub Agent and Seer Agent

---

## The Confusion

- Both terms use "Agent"
- Both can participate in Task Queues
- Both can be assignees to Requests
- Both interact with Signal Exchange
- Both have IAM identities
- But they are NOT the same thing

---

## Core Distinction

### Hub Agent = Scenario with Agent-Like Behavior

- **Hub Agent** is a **pattern**, not a technology
- Any Scenario that can act autonomously like an agent
- The automation could be rule-based, workflow-based, OR AI-based
- Hub provides the **identity and participation model** for the agent
- Hub doesn't care what's inside — it cares about participation capability

### Seer Agent = AI Agent on Seer Platform

- **Seer Agent** is a **concrete AI implementation**
- Follows the Raw → Trained → Employed lifecycle
- Runs on Seer runtime (Atlantis containers)
- Has AI-specific capabilities: LLM reasoning, tool use, knowledge access
- Requires Training Spec and Employment Spec

---

## Relationship: Seer Agent ⊆ Hub Agent

- A Seer Agent is ALWAYS a Hub Agent (when deployed)
- A Hub Agent is NOT always a Seer Agent
- Hub Agent is the **superset**: any automation that participates like an agent
- Seer Agent is a **specific type** of Hub Agent: an AI agent on Seer runtime

```
┌─────────────────────────────────────────────────────────┐
│                     HUB AGENTS                          │
│  (Any Scenario that participates like an agent)         │
│                                                         │
│   ┌──────────────────┐  ┌───────────────┐              │
│   │   Rule-Based     │  │  Workflow     │              │
│   │   Automations    │  │  Automations  │              │
│   │   (Rhea)         │  │  (Perseus)    │              │
│   └──────────────────┘  └───────────────┘              │
│                                                         │
│   ┌─────────────────────────────────────────────┐      │
│   │              SEER AGENTS                     │      │
│   │  (AI Agents on Seer Runtime)                │      │
│   │                                              │      │
│   │  Raw Agent → Trained Agent → Employed Agent │      │
│   └─────────────────────────────────────────────┘      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## What Makes Something a "Hub Agent"?

A Scenario becomes a Hub Agent when it can:

1. **Participate in Task Queues** — receive tasks like a human agent
2. **Act as Request Assignee** — be explicitly assigned to handle a Request
3. **Have an IAM Identity** — registered as an Agent in Cipher IAM
4. **Produce Request Updates** — report decisions, memos, outcomes
5. **Be enrolled/unenrolled** — Supervisor can manage participation

### Hub Agent Lifecycle

```
Scenario Created → Registered as Agent in IAM → Enrolled in Task Queue(s) → Active
```

---

## How Seer Agents Become Hub Agents

A Seer Agent participates in Hub through:

1. **Scenario Binding** — Employed Agent is bound to specific Scenario(s)
2. **Signal Exchange Registration** — sx-observer routes Request Updates
3. **Hub Application Deployment** — Employed Agent IS a deployed Hub Application
4. **IAM Identity** — Employment grants SPIFFE identity + virtual key

### Seer Agent Deployment = Hub Agent Creation

```
TrainingSpec → EmploymentSpec → Employed Agent → Deployed Hub Application → Hub Agent
```

---

## Key Points to Call Out

### For Process Architects

- [ ] You design Scenarios — any Scenario CAN become a Hub Agent
- [ ] Hub Agent is a capability/pattern, not a specific technology choice
- [ ] You don't decide "Seer vs not-Seer" — that's an automation implementation decision
- [ ] Focus on: What should this automation be able to DO (participate in queues, be assigned, etc.)
- [ ] The "Scenario as Agent" pattern is Hub's way of enabling automation participation
- [ ] Normative Spec doesn't care about runtime — roles and SOPs are tech-agnostic

### For CSAs (Customer Solution Architects)

- [ ] When customer says "agent" — clarify: participation model (Hub) or AI technology (Seer)?
- [ ] Hub Agent = how it participates in work (queues, assignments, escalation)
- [ ] Seer Agent = how it thinks (LLM, tools, knowledge)
- [ ] Same Seer Agent can be Hub Agent in multiple Scenarios
- [ ] Multiple Seer Agents can participate in one Scenario (Composite Application)
- [ ] Customer may need Hub Agents that are NOT AI (rule-based, workflow-based)

### For Agent Engineers

- [ ] You develop Raw Agents and Training Specs — these are Seer concepts
- [ ] Your agent becomes a Hub Agent when deployed via Employment
- [ ] You DON'T configure Hub participation — that's in Scenario and Employment Specs
- [ ] Focus on: agent capabilities, knowledge, tools, guardrails
- [ ] Hub integration happens through: Request Updates, Task APIs, Signal Exchange
- [ ] Your agent code doesn't change whether it's "Hub Agent" or not — Hub identity is external

### For Developers

- [ ] Hub Application can be exposed as a Hub Agent (Scenario as Agent pattern)
- [ ] Seer Employed Agent IS a Hub Application when deployed
- [ ] Protocol interfaces (HTTP, MCP, A2A) are Hub's way to expose any Hub Agent
- [ ] When building automations: decide runtime (Rhea, Perseus, Seer, Atlantis) based on capability needs
- [ ] All runtimes can produce Hub Agents — only Seer produces AI agents

---

## Interaction Modes (Original Points, Expanded)

### How a Seer Agent Participates in Hub

1. **As Hub Application (Observer Pattern)**
   - Receives Request Updates from Signal Exchange
   - Processes updates, produces outcomes
   - Standard Hub Application behavior

2. **As Task Handler (Task Queue Pattern)**
   - Enrolled in Task Queue(s) via ScenarioAsAgent
   - Receives tasks like a human agent
   - Can accept, work, complete, or abandon tasks

3. **As Request Assignee (Delegation Pattern)**
   - Explicitly assigned to handle a specific Request
   - Full responsibility for Request lifecycle
   - Reports back via Request Updates

### How Seer Agents Collaborate

1. **Same Scenario (Composite Application)**
   - Multiple agents share Request state (blackboard pattern)
   - Implicit coordination through shared context
   - Example: Analyst + Reviewer + Approver agents

2. **Cross-Scenario (Task Delegation)**
   - Agent A delegates task to Agent B's queue
   - Escalation matrix determines routing
   - Example: Fraud Detection → Human Review queue

3. **As Tool (Scenario as Tool Pattern)**
   - One agent invokes another agent's Scenario as a tool
   - Request creates child Request
   - Example: Main Agent calls Specialist Agent for analysis

---

## Identity Model Differences

### Hub Agent Identity

- **Agent Persona**: Business identity derived from Scenario
  - Registered in Cipher IAM as Agent type
  - Scenario-bound — identity tied to Scenario
  - Participation-focused — what can it DO in Hub
  - Enrollment state — active in which queues/scenarios
- **Deployment Identity**: Varies by runtime
  - For Seer Agents: SPIFFE ID (infrastructure-level)
  - For other runtimes: Runtime-specific deployment identity

### Seer Agent Identity

Seer Agents have **two-layer identity**:

1. **Agent Persona** (Business Identity):
   - Derived from Scenario (same as Hub Agent)
   - Registered in Cipher IAM
   - Used for: access tokens, audit, delegation chains

2. **Deployment Identity** (Infrastructure):
   - SPIFFE ID at Employment (OAuth Client equivalent)
   - Virtual Key for Model Gateway access
   - Used for: mTLS, service mesh authentication

**Additional Seer-Specific**:
- Follows Raw → Trained → Employed progression
- Delegation chain tracking (who granted authority)
- Unified delegation model (scenario-scoped or request-scoped)

### Composite Identity

When Seer Agent is Hub Agent:
- **Agent Persona**: Shared — both Hub and Seer use the same Scenario-derived persona
- **Deployment Identity**: Seer adds SPIFFE layer (infrastructure authentication)
- Hub sees it as Hub Application with Agent capabilities (persona-based)
- Seer sees it as Employed Agent with Hub integration (persona + SPIFFE)

> **See**: [ADR-0129: Agent Identity Model](../decision-logs/0129-agent-identity-model.md) for the complete two-layer identity model.

---

## Protocol Interfaces

Hub provides these protocol interfaces to ALL Hub Agents (regardless of runtime):

| Protocol | Use Case | Notes |
|----------|----------|-------|
| **HTTP/REST** | Standard request/response | Task APIs, Request Updates |
| **MCP** | Multi-turn, tool-based interaction | AI assistant integration |
| **A2A** | Agent-to-agent communication | Cross-agent collaboration |

- These are HUB capabilities, not Seer-specific
- Seer Agents use these through Hub, not directly

---

## Common Misconceptions

| Misconception | Reality |
|--------------|---------|
| "Hub Agent = AI Agent" | Hub Agent is any automation that participates like an agent |
| "Seer Agent doesn't need Hub" | Seer Agents are always deployed within Hub Scenarios |
| "Must choose Hub OR Seer" | Seer Agents ARE Hub Agents when deployed |
| "Hub Agent has no AI" | Hub Agent can have AI (Seer) or not (Rhea, Perseus) |
| "A2A is only for Seer" | A2A is Hub protocol, available to all Hub Agents |

---

## Decision Guide: When to Use What Term

| Context | Use "Hub Agent" | Use "Seer Agent" |
|---------|-----------------|------------------|
| Discussing participation in queues | ✓ | |
| Discussing AI capabilities | | ✓ |
| Designing Scenario | ✓ | |
| Developing agent code | | ✓ |
| Configuring enrollment | ✓ | |
| Configuring training/knowledge | | ✓ |
| Explaining to business users | ✓ (simpler) | |
| Explaining to AI engineers | | ✓ (precise) |

---

## Open Questions / To Expand

- [ ] How does authority delegation differ between Hub Agent and Seer Agent?
- [ ] What are the monitoring/observability differences?
- [ ] How do quotas/budgets apply differently?
- [ ] What's the upgrade path from non-AI Hub Agent to Seer Agent?
- [ ] How does versioning work differently?
- [ ] Examples: pure Hub Agents (non-Seer) in common use cases

---

## Related Documentation

- [Scenario as Agent](../02-system-design/implementation-concepts/scenario-as-agent.md)
- [Hub Application](../02-system-design/implementation-concepts/hub-application.md)
- [Agent Model](../02-system-design/agent-model.md)
- [Agent Lifecycle (Seer)](../../olympus-seer-docs/seer-design/implementation-concepts/agent-lifecycle.md)
- [Employed Agent as Hub Application](../../olympus-seer-docs/seer-design/hub-integration/employed-agent.md)