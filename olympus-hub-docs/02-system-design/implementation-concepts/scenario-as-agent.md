# Scenario as Agent

> **Category:** Composite Patterns

---

## Overview

**Scenario as Agent** is a composite pattern where a Scenario is registered as an agent that can be assigned tasks in another Scenario's task queue. This enables automations to participate alongside human agents, allowing for gradual automation, load sharing, and specialized processing.

---

## Ontology Context

### Relationship to Ontology

The ontology describes **Agent** as an executor of work and **Scenario** as an operational situation. This pattern bridges them by allowing scenarios to act as agents.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Agent | Scenario as Agent | Scenario acts as an agent |
| Scenario | Source of agent behavior | Scenario provides automation |

### Gap This Fills

The ontology treats agents and scenarios separately. This pattern addresses:
1. **Automation participation**: How can automations join human queues?
2. **Gradual automation**: How to automate some tasks, not all?
3. **Specialization**: How to route specific task types to automation?

---

## Definition

**Scenario as Agent** is a pattern where:
- A Scenario is registered as an Agent in Cipher IAM
- The agent is enrolled in another Scenario's task queue
- When tasks are assigned, the source Scenario handles them
- The Scenario uses standard agent operations (start, complete, memo)

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Cross-workbench possible |
| **Lifecycle** | Registered once; active while enrolled |
| **Ownership** | Developer creates; Supervisor enrolls |
| **Multiplicity** | One Scenario can be agent in many queues |

---

## Identity Model

When a Scenario is registered as an Agent, it provides the **Agent Persona** (business identity):

### Agent Persona from Scenario

- **Source**: Scenario defines the agent's human-like personality and business role
- **Storage**: Registered in Cipher IAM as an Agent Persona
- **Purpose**: Business identity for app-to-app interactions, authority delegation, audit attribution
- **Lifetime**: Tied to Scenario lifecycle (survives redeployments)

### ScenarioAsAgent CRD Registration

The ScenarioAsAgent CRD registers the Agent Persona in Cipher IAM:

```yaml
spec:
  # Source Scenario (provides Agent Persona)
  scenario_ref: dispute-automation
  
  # Agent Identity (Persona registration)
  agent:
    name: dispute-automation-agent  # Agent Persona name
    display_name: "Dispute Automation Agent"
    # This persona is registered in Cipher IAM
```

**Key Points**:
- Scenario provides the Agent Persona (business identity)
- ScenarioAsAgent CRD registers this persona in Cipher IAM
- For Seer Agents, the Deployment Identity (SPIFFE) is added at deployment time
- The Agent Persona is the "who" in business terms; Deployment Identity is the "which instance"

> **See**: [ADR-0129: Agent Identity Model](../../decision-logs/0129-agent-identity-model.md) for the two-layer identity model (Deployment Identity + Agent Persona).

---

## Rationale

### Why This Design?

Scenario as Agent enables:
1. **Gradual automation**: Start with humans, add automation
2. **Load sharing**: Split work between humans and automation
3. **Specialization**: Route specific types to automation
4. **Fallback**: Automation can abandon to human queue

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Direct integration** | Tight coupling; no queue participation |
| **Separate automation path** | Duplicated routing logic |
| **Replace humans entirely** | Not always feasible or desirable |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0007](../../decision-logs/0007-composite-pattern-technology-agnostic.md) | Technology-agnostic automation |

---

## Structure

### ScenarioAsAgent CRD

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAsAgent
metadata:
  name: dispute-automation-agent
  namespace: acme-bank
spec:
  # Source Scenario
  scenario_ref: dispute-automation
  
  # Agent Identity
  agent:
    name: dispute-automation-agent
    display_name: "Dispute Automation Agent"
    version: "1.0.0"
    description: "Automated dispute processing"
    
  # Capabilities
  capabilities:
    - document-validation
    - amount-verification
    - rule-evaluation
    
  # Automation type
  automation_type: rule-based    # rule-based | workflow | llm-agent
  
  # Communication
  protocol:
    type: http
    input_format: structured_task_payload
    output_format: structured_response
    
  # Enrollment
  enrollment:
    task_queues:
      - queue_id: tier-1-disputes
        priority: 10
      - queue_id: auto-eligible-disputes
        priority: 5
```

### Agent Lifecycle

```
1. REGISTRATION
   └── Scenario registered as Agent in IAM

2. ENROLLMENT
   └── Agent added to task queue(s)

3. TASK RECEIPT
   └── Task assigned → Signal sent to Scenario

4. TASK PROCESSING
   ├── Scenario receives signal
   ├── Hub Application processes
   └── Application uses Agent APIs

5. TASK COMPLETION
   └── Complete or abandon back to queue
```

---

## Behavior

### How It Works

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SCENARIO AS AGENT FLOW                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   WORKBENCH A                         WORKBENCH B                           │
│   (Consumer)                          (Provider)                            │
│                                                                              │
│   ┌───────────────┐                  ┌───────────────┐                     │
│   │ Scenario A    │                  │ Scenario B    │                     │
│   │ (Disputes)    │                  │ (Automation)  │                     │
│   │               │                  │               │                     │
│   │ Creates task  │                  │ Registered as │                     │
│   │       │       │                  │ agent in A    │                     │
│   │       ▼       │                  │               │                     │
│   │ ┌───────────┐ │                  │ Hub App       │                     │
│   │ │Task Queue │ │                  │ handles task  │                     │
│   │ │           │ │                  │               │                     │
│   │ │ Agent-Bot │◀├── enrolled ──────┤               │                     │
│   │ │ Agent-Alice│ │                  │               │                     │
│   │ └───────────┘ │                  │               │                     │
│   │       │       │                  │               │                     │
│   │ Assigns to    │    HTTP Signal   │               │                     │
│   │ Agent-Bot ────┼─────────────────▶│ Trigger       │                     │
│   │               │                  │       │       │                     │
│   │               │                  │       ▼       │                     │
│   │               │  Agent API call  │ Hub App       │                     │
│   │ Task complete │◀─────────────────┤ completes     │                     │
│   │               │                  │               │                     │
│   └───────────────┘                  └───────────────┘                     │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Hub Application Example

```python
class DisputeAutomationApp(HubApplication):
    """
    Hub Application acting as an agent.
    Can be rule-based, workflow, or AI-powered.
    """
    
    async def handle_task_assigned(self, request):
        task_context = request.payload.get("task_payload", {})
        task_id = request.payload.get("source_context", {}).get("task_id")
        
        # Start work on the task
        await self.agent_client.start_work(
            task_id=task_id,
            memo="Automated processing started"
        )
        
        # Process based on automation type
        try:
            result = await self.process_task(task_context)
            
            # Complete the task
            await self.agent_client.complete_task(
                task_id=task_id,
                outcome=result
            )
            
        except AutomationException as e:
            # Cannot handle; abandon to human queue
            await self.agent_client.abandon_task(
                task_id=task_id,
                reason="AUTOMATION_FAILED",
                memo=f"Releasing to human: {e}"
            )
```

### Automation Types

| Type | Implementation | Example |
|------|----------------|---------|
| **rule-based** | Business rules engine | Amount threshold checks |
| **workflow** | BPMN workflow | Multi-step validation |
| **image-processing** | Document OCR | Invoice extraction |
| **llm-agent** | AI-powered | Complex analysis |

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Task Queue | ← enrolled in | Receives task assignments |
| Agent APIs | → uses | Standard agent operations |
| Cipher IAM | ← registered | Agent identity |
| Signal Exchange | ← receives | Task assignment signals |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Agent registration** | Must be registered in IAM |
| **Standard operations** | Uses same APIs as human agents |
| **Queue enrollment** | Must be enrolled by Supervisor |
| **Abandon allowed** | Can release tasks to human queue |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Gradual automation** | Add automation alongside humans |
| ✅ **Load sharing** | Split work appropriately |
| ✅ **Fallback** | Automation can escalate to humans |
| ✅ **Transparent** | Same queue, same tracking |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Setup complexity** | ScenarioAsAgent CRD simplifies |
| ⚠️ **Debugging** | Full observability via Olympus Watch |

---

## Examples

### Example 1: Rule-Based Dispute Automation

```yaml
# ScenarioAsAgent for simple disputes
spec:
  scenario_ref: simple-dispute-automation
  
  automation_type: rule-based
  
  capabilities:
    - amount_under_100
    - first_time_dispute
    
  enrollment:
    task_queues:
      - queue_id: auto-eligible-disputes
```

### Example 2: AI-Powered Document Review

```yaml
# ScenarioAsAgent for document analysis
spec:
  scenario_ref: document-review-ai
  
  automation_type: llm-agent
  
  capabilities:
    - document_classification
    - information_extraction
    
  enrollment:
    task_queues:
      - queue_id: document-review-queue
```

---

## Implementation Notes

### For Developers

- Use standard agent APIs for task operations
- Always handle failures with abandon
- Add memos for transparency
- Log all decisions for audit

### For Supervisors

- Review automation performance
- Adjust queue priority as needed
- Monitor abandon rates

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Scenario as Tool](./scenario-as-tool.md) | Different pattern |
| [Task Allocation](./task-allocation.md) | Allocation assigns to agent |
| [Hub Application](./hub-application.md) | Implementation of agent |

---

## References

- [Scenario as Agent Pattern](../../09-composite-systems-and-patterns/scenario-as-an-agent.md)
- [Developer Operators](../../04-subsystems/operators/developer-operators.md)
- [ADR-0007: Technology Agnostic](../../decision-logs/0007-composite-pattern-technology-agnostic.md)

