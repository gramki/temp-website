# Hub Agent vs Seer Agent: Examples

> **Status**: 🟢 Design Complete  
> **Target Audience**: Process Architects, CSAs, Agent Engineers, Developers  
> **Purpose**: Concrete examples and use cases demonstrating Hub Agent and Seer Agent patterns

---

## Example 1: Rhea Workflow as Hub Agent (Non-Seer)

### Scenario

A bank needs to automate evidence review for dispute resolution. The automation uses rule-based logic (Rhea runtime) to validate documents and check amounts against thresholds. The automation should participate in the same task queue as human agents, allowing gradual rollout and load sharing.

### Architecture

**Scenario Definition**:
- **Scenario**: `evidence-review-automation`
- **Workbench**: `dispute-operations`
- **Hub Application**: Rhea workflow (BPMN) that processes evidence documents
- **Runtime**: Rhea (rule-based automation)

**ScenarioAsAgent CRD Configuration**:
```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAsAgent
metadata:
  name: evidence-review-agent
  namespace: acme-bank
spec:
  scenario_ref: evidence-review-automation
  
  agent:
    name: evidence-review-agent
    display_name: "Evidence Review Automation"
    automation_type: rule-based
    
  capabilities:
    - document-validation
    - amount-verification
    - rule-evaluation
    
  enrollment:
    task_queues:
      - queue_id: evidence-review-queue
        priority: 10
```

**Task Queue Enrollment**:
- Supervisor enrolls `evidence-review-agent` in `evidence-review-queue`
- Allocation weight: 10% (90% to human agents initially)
- Agent receives tasks like human agents

**Runtime Behavior**:
- Task assigned → Signal sent to Scenario
- Rhea workflow processes evidence
- Agent uses standard operations: `start_work`, `complete_task`, `abandon_task`
- If automation cannot handle, abandons to human queue

### Identity Model

- **Agent Persona**: `evidence-review-agent@acme.hub.io` (registered in Cipher IAM)
- **Deployment Identity**: Rhea runtime-specific (not SPIFFE)
- **Token Structure**: Only Agent Persona in `sub` claim (no `client_id`)

> **Reference**: [`Scenario as Agent`](../../02-system-design/implementation-concepts/scenario-as-agent.md) describes the pattern. [`Rhea Workflow Engine`](../../04-subsystems/automation-runtimes/rhea-workflow-engine.md) explains Rhea runtime.

---

## Example 2: Seer Agent as Hub Agent

### Scenario

A bank needs an AI-powered fraud analyst that can analyze transaction patterns, review customer history, and make recommendations. The agent uses LLM reasoning and tool access. It should participate in the fraud investigation task queue alongside human analysts.

### Architecture

**Raw Agent Development**:
- Agent code implements fraud analysis logic
- Capabilities: transaction analysis, pattern recognition, recommendation generation
- Tools: transaction lookup, customer history, fraud rules engine

**Training Spec**:
- Knowledge sources: fraud patterns, regulatory guidelines
- System prompts: fraud analyst persona, decision criteria
- Guardrails: PII protection, financial compliance
- Tool bindings: transaction API, customer service API

**Employment Spec**:
```yaml
apiVersion: seer.olympus.io/v1
kind: EmploymentSpec
metadata:
  name: fraud-analyst-emp-001
spec:
  training:
    ref:
      name: fraud-analyst-v2
      version: "1.7.0"
  
  workScope:
    workbench: acme-disputes
    scenario: fraud-investigation
    
  delegation:
    mode: scenario-scoped
    allowedTemplates:
      - fraud-analysis
      - transaction-review
```

**Scenario Binding**:
- Employment Spec binds to `fraud-investigation` Scenario
- Scenario provides Agent Persona: `fraud-analyst-agent@acme.hub.io`
- Agent Persona registered in Cipher IAM

**Hub Agent Participation**:
- ScenarioAsAgent CRD registers Scenario as agent
- Agent enrolled in `fraud-investigation-queue`
- Seer Agent deployed as Hub Application
- Agent participates via HTTP/REST, MCP, or A2A protocols

### Identity Model

- **Agent Persona**: `fraud-analyst-agent@acme.hub.io` (from Scenario)
- **Deployment Identity**: `spiffe://acme.hub.io/seer/agent/acme/fraud-analyst-pod-001` (from Employment)
- **Token Structure**: Both identities included (`sub` = Persona, `client_id` = SPIFFE)

> **Reference**: [`Agent Lifecycle`](../../../olympus-seer-docs/seer-design/implementation-concepts/agent-lifecycle.md) describes Raw → Trained → Employed progression. [`Employment Spec CRD`](../../../olympus-seer-docs/seer-design/hub-integration/employment-spec-crd.md) defines deployment configuration. [`Employed Agent as Hub Application`](../../../olympus-seer-docs/seer-design/hub-integration/employed-agent.md) explains Hub integration.

---

## Example 3: Composite Application (Multiple Agent Types)

### Scenario

A dispute resolution Scenario requires multiple specialized agents working together: an analyst agent (Seer) that reviews evidence, a reviewer agent (Seer) that validates analysis, and an approver agent (Rhea) that applies business rules. All agents coordinate through shared Request state.

### Architecture

**Scenario Definition**:
- **Scenario**: `dispute-resolution`
- **Hub Applications**: 
  - Analyst Agent (Seer)
  - Reviewer Agent (Seer)
  - Approver Agent (Rhea)

**Sub-Personas**:
Each agent gets a distinct sub-persona, all deriving from the base Agent Persona:

- `dispute-analyst-agent@acme.hub.io` (Seer Agent)
  - Deployment Identity: `spiffe://.../analyst-pod-001`
- `dispute-reviewer-agent@acme.hub.io` (Seer Agent)
  - Deployment Identity: `spiffe://.../reviewer-pod-001`
- `dispute-approver-agent@acme.hub.io` (Rhea Agent)
  - Deployment Identity: Rhea runtime-specific

**Coordination Pattern**:
- All agents receive Request Updates from Signal Exchange
- Each agent operates independently with its own session
- Coordination through shared Request state (blackboard pattern)
- Analyst produces analysis → Reviewer validates → Approver applies rules

**ScenarioAsAgent Configuration**:
Each agent registered separately:

```yaml
# Analyst Agent
apiVersion: hub.olympus.io/v1
kind: ScenarioAsAgent
metadata:
  name: dispute-analyst-agent
spec:
  scenario_ref: dispute-resolution
  agent:
    name: dispute-analyst-agent
    sub_persona: analyst
```

```yaml
# Reviewer Agent
apiVersion: hub.olympus.io/v1
kind: ScenarioAsAgent
metadata:
  name: dispute-reviewer-agent
spec:
  scenario_ref: dispute-resolution
  agent:
    name: dispute-reviewer-agent
    sub_persona: reviewer
```

```yaml
# Approver Agent
apiVersion: hub.olympus.io/v1
kind: ScenarioAsAgent
metadata:
  name: dispute-approver-agent
spec:
  scenario_ref: dispute-resolution
  agent:
    name: dispute-approver-agent
    sub_persona: approver
    automation_type: rule-based
```

> **Reference**: [`Hub Composite Application`](../../02-system-design/implementation-concepts/hub-composite-application.md) describes multi-agent coordination. [`ADR-0129: Agent Identity Model`](../../decision-logs/0129-agent-identity-model.md) explains sub-personas for composite applications.

---

## Example 4: Customer-Facing Scenarios

### When Customer Needs Hub Agent (Non-Seer)

**Use Case**: Customer needs automated document processing that follows business rules. No AI reasoning required.

**Example**: Insurance claim processing
- **Scenario**: `claim-processing`
- **Hub Application**: Rhea workflow that validates claim forms, checks policy coverage, calculates payout
- **Runtime**: Rhea (rule-based)
- **Hub Agent**: Yes (via ScenarioAsAgent CRD)
- **Seer Agent**: No (no AI needed)

**Why Hub Agent**: Customer needs automation to participate in task queues alongside human claim processors, allowing gradual automation and load sharing.

### When Customer Needs Seer Agent

**Use Case**: Customer needs AI-powered customer service agent that can understand natural language, access knowledge bases, and make recommendations.

**Example**: Customer inquiry handling
- **Scenario**: `customer-inquiry`
- **Hub Application**: Seer Agent (Employed Agent)
- **Runtime**: Seer (Atlantis)
- **Hub Agent**: Yes (always, when deployed)
- **Seer Agent**: Yes

**Why Seer Agent**: Customer needs LLM reasoning, natural language understanding, and knowledge access capabilities that only Seer provides.

### Hybrid Scenarios

**Use Case**: Customer needs both rule-based automation and AI reasoning in the same workflow.

**Example**: Loan application processing
- **Scenario**: `loan-application`
- **Hub Applications**:
  - Credit check automation (Rhea) — rule-based validation
  - Risk assessment agent (Seer) — AI-powered analysis
- **Both as Hub Agents**: Yes (both participate in task queues)
- **Coordination**: Through shared Request state

**Why Hybrid**: Different parts of the process require different capabilities. Rule-based for deterministic checks, AI for complex analysis.

> **Reference**: [`Decision Framework`](./hub-agent-vs-seer-agent-core.md#part-3-decision-framework) provides guidance on when to use which pattern. [`Customer Guide`](./hub-agent-vs-seer-agent-customer-guide.md) offers customer-facing explanations.

---

## Related Documentation

### This Documentation Suite
- [`Hub Agent vs Seer Agent`](./hub-agent-vs-seer-agent.md) — Entry point and overview
- [`Core Concepts`](./hub-agent-vs-seer-agent-core.md) — Understanding and decision framework
- [`Anti-patterns`](./hub-agent-vs-seer-agent-anti-patterns.md) — When NOT to use Hub Agent pattern
- [`Architectural Details`](./hub-agent-vs-seer-agent-architectural-details.md) — C2-level implementation references
- [`Customer Guide`](./hub-agent-vs-seer-agent-customer-guide.md) — Customer-facing explanations
