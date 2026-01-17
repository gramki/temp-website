# Hub Agent vs Seer Agent: Customer Guide

> **Status**: 🟢 Design Complete  
> **Target Audience**: CSAs (Customer Solution Architects)  
> **Purpose**: Customer-facing explanations and decision guidance

---

## Overview

This guide helps CSAs explain Hub Agent vs Seer Agent to customers and make recommendations based on customer needs. It provides analogies, conversation guides, and decision frameworks suitable for customer discussions.

---

## Simple Analogies

### Hub Agent = Participation Model

**Analogy**: Hub Agent is like "employee status" — it describes how the automation participates in work, not what technology it uses.

- A Hub Agent can be rule-based (like a rule-following employee)
- A Hub Agent can be workflow-based (like a process-following employee)
- A Hub Agent can be AI-powered (like a thinking employee)

**Key Point**: Hub Agent describes *how* the automation works alongside humans, not *what* technology it uses.

### Seer Agent = AI Technology

**Analogy**: Seer Agent is like "AI capability" — it describes the AI technology (LLM reasoning, natural language understanding, knowledge access).

- Seer Agents use AI to understand and reason
- Seer Agents can learn from knowledge bases
- Seer Agents can use tools
- Seer Agents are always Hub Agents when deployed (they participate like employees)

**Key Point**: Seer Agent describes *what* technology the automation uses (AI), not *how* it participates.

---

## Customer Conversation Guide

### Opening Question

**Customer says**: "We need an agent to handle customer inquiries."

**CSA should clarify**: "Are you asking about:
1. How the automation participates in work (Hub Agent — task queues, assignments)?
2. What technology it uses (Seer Agent — AI reasoning, natural language)?"

### Follow-Up Questions

1. **"Do you need the automation to work alongside human agents in the same queue?"**
   - Yes → Hub Agent (participation model)
   - No → Regular Hub Application (event-driven)

2. **"Do you need AI capabilities (natural language understanding, reasoning, knowledge access)?"**
   - Yes → Seer Agent (AI technology)
   - No → Hub Agent with non-Seer runtime (Rhea, Perseus)

3. **"Do you need both?"**
   - Yes → Seer Agent (which is always a Hub Agent when deployed)
   - No → Choose based on primary need

### Common Customer Scenarios

**Scenario 1**: "We want to automate document processing with business rules."
- **Recommendation**: Hub Agent (non-Seer) with Rhea runtime
- **Reason**: Rule-based automation, needs task queue participation

**Scenario 2**: "We need an AI assistant that can understand customer questions."
- **Recommendation**: Seer Agent
- **Reason**: AI capabilities required, will participate as Hub Agent when deployed

**Scenario 3**: "We want to gradually automate some tasks, starting with simple ones."
- **Recommendation**: Hub Agent (non-Seer) initially, can add Seer Agent later
- **Reason**: Start with rule-based, add AI when needed

---

## Decision Matrix for Recommendations

| Customer Need | Recommendation | Rationale |
|---------------|----------------|-----------|
| **Task queue participation + AI reasoning** | Seer Agent | Seer Agent provides AI and is always a Hub Agent |
| **Task queue participation + rule-based logic** | Hub Agent (Rhea) | Rule-based automation in task queues |
| **Task queue participation + workflow orchestration** | Hub Agent (Perseus) | Workflow automation in task queues |
| **AI reasoning + no task queues** | Seer Agent (not as Hub Agent) | AI without queue participation |
| **Simple automation + no task queues** | Regular Hub Application | Event-driven, no agent participation needed |
| **Gradual automation rollout** | Hub Agent (start non-Seer, add Seer later) | Start simple, add AI when ready |

---

## Use Case Scenarios with Business Value

### Use Case 1: Insurance Claim Processing

**Customer Need**: Automate initial claim review to reduce processing time.

**Solution**: Hub Agent (Rhea) for rule-based claim validation
- **Business Value**: 
  - Faster initial processing (automated validation)
  - Human agents focus on complex cases
  - Consistent rule application
  - Gradual rollout (start with 10% allocation)

**Why Hub Agent**: Needs to participate in claim processing queue alongside human agents.

**Why Non-Seer**: Rule-based logic sufficient for initial validation.

### Use Case 2: Customer Service AI Assistant

**Customer Need**: AI assistant that can understand customer questions and provide answers.

**Solution**: Seer Agent for natural language understanding and knowledge access
- **Business Value**:
  - 24/7 customer support
  - Natural language interaction
  - Access to knowledge bases
  - Escalation to humans when needed

**Why Seer Agent**: Requires AI capabilities (LLM reasoning, natural language understanding).

**Why Hub Agent**: Participates in customer service queue, can escalate to humans.

### Use Case 3: Fraud Detection and Investigation

**Customer Need**: Automated fraud detection with human review for complex cases.

**Solution**: Hybrid — Seer Agent for pattern analysis, Hub Agent (Rhea) for rule-based checks
- **Business Value**:
  - Faster fraud detection (automated analysis)
  - Human review for complex cases
  - Pattern recognition (AI) + rule validation (rules)
  - Coordinated through shared Request state

**Why Hybrid**: Different capabilities needed — AI for pattern analysis, rules for validation.

**Why Both as Hub Agents**: Both participate in fraud investigation queue.

### Use Case 4: Document Processing Pipeline

**Customer Need**: Process documents through multiple stages (extraction, validation, approval).

**Solution**: Hub Agent (Perseus) for workflow orchestration
- **Business Value**:
  - Multi-stage processing automation
  - Human approval at key stages
  - Workflow visibility and tracking
  - Consistent process execution

**Why Hub Agent**: Needs to participate in document processing queue.

**Why Perseus**: Workflow orchestration required for multi-stage process.

---

## Operational Considerations

### Monitoring and Scaling

**Hub Agents** (all types):
- Monitor task completion rates
- Track queue participation
- Monitor allocation weights
- Scale based on queue demand

**Seer Agents** (additional):
- Monitor AI confidence levels
- Track token usage and budgets
- Monitor escalation rates
- Scale based on request volume and complexity

### Cost Considerations

**Hub Agent (non-Seer)**:
- Lower compute costs (rule-based or workflow)
- Predictable resource usage
- No AI model costs

**Seer Agent**:
- Higher compute costs (AI model inference)
- Token usage costs
- Variable resource usage based on complexity

**Note**: Cost differences reflect capability differences. Seer Agents provide capabilities (natural language understanding, reasoning) that non-Seer agents cannot provide.

---

## Related Documentation

### This Documentation Suite
- [`Hub Agent vs Seer Agent`](./hub-agent-vs-seer-agent.md) — Entry point and overview
- [`Core Concepts`](./hub-agent-vs-seer-agent-core.md) — Technical understanding
- [`Examples`](./hub-agent-vs-seer-agent-examples.md) — Concrete use cases
- [`Decision Framework`](./hub-agent-vs-seer-agent-core.md#part-3-decision-framework) — When to use what
- [`Anti-patterns`](./hub-agent-vs-seer-agent-anti-patterns.md) — When NOT to use Hub Agent pattern
- [`Architectural Details`](./hub-agent-vs-seer-agent-architectural-details.md) — C2-level implementation references
