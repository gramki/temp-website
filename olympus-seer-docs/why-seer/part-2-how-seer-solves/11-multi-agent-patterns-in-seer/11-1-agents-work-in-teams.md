# 11.1 Agents Work in Teams

Enterprise processes require multiple specialized agents coordinating with humans. Seer agents don't work in isolation—they operate within Hub's collaboration infrastructure, working alongside other agents and humans to complete complex business operations.

## Why Teams, Not Solo Agents

### The Reality of Enterprise Work

Enterprise operations involve:

| Characteristic | Implication for Agents |
|----------------|------------------------|
| **Multiple domains** | No single agent has all knowledge |
| **Specialized skills** | Different tasks need different capabilities |
| **Human judgment** | Some decisions require human involvement |
| **Accountability chains** | Multiple approvers and reviewers |
| **Handoff points** | Work transfers between agents |

A dispute resolution process might involve: a triage agent, a document analysis agent, a policy lookup agent, a human supervisor for final approval, and a notification agent. No single agent can do all of this well.

### The Collaboration Imperative

Solo agents face fundamental limits:

| Limitation | Team Solution |
|------------|---------------|
| **Context window limits** | Divide work; each agent has focused context |
| **Capability specialization** | Agents specialize in what they do best |
| **Error isolation** | Failure in one agent doesn't cascade to others |
| **Human integration** | Seamless escalation to human agents |
| **Governance** | Governor agents observe without acting |

## Team Composition

### Agent Roles in a Team

A typical Seer team includes:

```
Case Orchestrator (Orchestrator)
    ├── Document Analyst (Thinker)
    ├── Policy Checker (Thinker)
    ├── Action Executor (Doer)
    ├── Human Supervisor (Human Agent)
    └── Compliance Monitor (Governor)
```

Each agent has a defined role with clear responsibilities.

### Role Boundaries

Clear boundaries prevent confusion:

| Boundary Type | What It Defines |
|---------------|-----------------|
| **Authority** | What the agent is allowed to do |
| **Scope** | What cases/scenarios the agent handles |
| **Handoff** | When and how to transfer work |
| **Escalation** | When to involve a supervisor |

## Team Operations

### Task Queues

Agents are organized around task queues:

```
Task Queue: evidence-review-queue
    ├── Evidence Review Bot (AI, capacity: 10)
    ├── Senior Analyst (Human, capacity: 5)
    └── Junior Analyst (Human, capacity: 8)
```

Task Management assigns work based on:
- Availability and capacity
- Skills required
- Allocation weights
- Escalation level

### Flexible Assignment

The same task can be handled by human or AI:

| Situation | Routing |
|-----------|---------|
| **Normal load** | AI handles routine cases |
| **Overflow** | AI takes overflow from humans |
| **Complex case** | Human handles directly |
| **AI uncertain** | Escalates to human |
| **After hours** | AI provides 24/7 coverage |

### Gradual Automation

Teams enable gradual AI adoption:

1. **Start human-only:** All tasks go to humans
2. **Pilot AI:** 10% of tasks route to AI agent
3. **Expand:** Increase to 50% based on performance
4. **Majority AI:** AI handles 80%, humans handle exceptions
5. **Full automation:** AI handles all, humans supervise

Allocation weights can be adjusted without code changes.

## Team Governance

### Supervisor Oversight

Every agent team has supervisor oversight:

| Supervisor Responsibility | How It Works |
|---------------------------|--------------|
| **Queue management** | Adjust allocation weights, priorities |
| **Escalation handling** | Receive and resolve escalations |
| **Performance monitoring** | Track completion rates, quality |
| **Agent management** | Enable/disable agents in queue |

### Team-Level Policies

Teams operate under defined policies:

```yaml
team_policy:
  name: dispute-resolution-team
  
  sla:
    initial_response: PT1H
    resolution: P3D
    
  escalation:
    timeout: PT4H
    path: [senior-analyst, team-lead, manager]
    
  quality:
    sample_rate: 0.1  # Review 10% of decisions
    reviewer: compliance-bot
```

### Audit at Team Level

All team interactions are audited:

- Task assignments
- Handoffs between agents
- Escalations and interventions
- Final outcomes

Each interaction is traceable back to specific agents and decisions.

---

**References:**
*   `olympus-hub-docs/04-subsystems/task-management/README.md`
*   `olympus-hub-docs/09-composite-systems-and-patterns/scenario-as-an-agent.md`
